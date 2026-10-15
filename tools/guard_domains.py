#!/usr/bin/env python3
"""PreToolUse guard: keep the Team and Workspace domains from writing into each other.

  /home/randy/Team       -- sessions on the team account
  /home/randy/Workspace  -- sessions on the individual account

A session whose project directory (CLAUDE_PROJECT_DIR, falling back to the
hook's cwd) lies in one domain may READ the other freely but may not WRITE to
it. A session outside both domains is not judged. The rule is symmetric, so
the same script can be wired into either side's settings, or into the shared
~/.claude/settings.json to cover both at once.

A write is judged by its TARGET, never by whether the command text mentions
the other domain: `cat ~/Workspace/x > notes.md` is a read and is allowed.

Known limits: an interpreter heredoc that writes (`python3 - <<PY`) and a
target holding an unexpanded variable (`"$DIR/x"`) cannot be classified from
the command text and are not judged.

Reads the PreToolUse JSON on stdin. Prints a deny decision, or nothing.
"""
import json, os, re, shlex, sys

HOME = os.path.expanduser("~")
DOMAINS = {
    "Team": os.path.realpath(os.path.join(HOME, "Team")),
    "Workspace": os.path.realpath(os.path.join(HOME, "Workspace")),
}

WRITE_CMDS = {"rm", "rmdir", "unlink", "shred", "tee", "truncate", "mkdir",
              "touch", "chmod", "chown", "chgrp", "patch", "mv"}
DEST_LAST_CMDS = {"cp", "install", "rsync", "ln"}
GIT_WRITE = {"add", "commit", "checkout", "switch", "restore", "reset", "revert",
             "merge", "rebase", "cherry-pick", "push", "pull", "fetch", "stash",
             "clean", "rm", "mv", "apply", "am", "init", "gc", "prune",
             "worktree", "tag", "remote", "config", "clone"}
GIT_READ_FORMS = {("worktree", "list"), ("stash", "list"), ("stash", "show"),
                  ("remote", "-v"), ("remote", "show"), ("config", "--get"),
                  ("config", "--list"), ("config", "-l"), ("tag", "-l"),
                  ("tag", "--list")}
SEPARATORS = {";", "&&", "||", "|", "&", "\n"}
REDIRECT = re.compile(r"^(?:\d|&)?>>?(.*)$")


def domain_of(path):
    # Judge the literal path AND where it resolves to: Workspace/TMP is a
    # symlink out of the tree, and a symlink in could point back across.
    for candidate in (os.path.normpath(path), os.path.realpath(path)):
        for name, root in DOMAINS.items():
            if candidate == root or candidate.startswith(root + os.sep):
                return name
    return None


def resolve(target, cwd):
    if "$" in target or "`" in target:
        return None
    return os.path.normpath(os.path.join(cwd, os.path.expanduser(target)))


def segments(command):
    lexer = shlex.shlex(command, posix=True, punctuation_chars=";&|")
    lexer.whitespace_split = True
    lexer.commenters = ""
    seg = []
    for tok in lexer:
        if tok in SEPARATORS or set(tok) <= set(";&|"):
            if seg:
                yield seg
            seg = []
        else:
            seg.append(tok)
    if seg:
        yield seg


def bash_targets(command, cwd):
    """Yield (path, what) for every path the command would write."""
    try:
        segs = list(segments(command))
    except ValueError:
        return
    for seg in segs:
        args = []
        it = iter(range(len(seg)))
        for i in it:
            m = REDIRECT.match(seg[i])
            if m and not seg[i].startswith("2>&"):
                dest = m.group(1) or (seg[i + 1] if i + 1 < len(seg) else "")
                if not m.group(1):
                    next(it, None)
                if dest and dest != "/dev/null" and not dest.startswith("&"):
                    yield resolve(dest, cwd), "a redirect"
            else:
                args.append(seg[i])
        while args and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", args[0]):
            args = args[1:]
        while args and args[0] in {"sudo", "env", "nohup", "time", "command"}:
            args = args[1:]
        if not args:
            continue
        cmd, rest = os.path.basename(args[0]), args[1:]
        plain = [a for a in rest if not a.startswith("-")]
        if cmd == "cd":
            cwd = resolve(plain[0] if plain else HOME, cwd) or cwd
        elif cmd in WRITE_CMDS:
            for a in plain:
                yield resolve(a, cwd), cmd
        elif cmd in DEST_LAST_CMDS and plain:
            yield resolve(plain[-1], cwd), cmd
        elif cmd == "sed" and any(a.startswith("-i") or a == "--in-place" for a in rest):
            for a in plain[1:]:
                yield resolve(a, cwd), "sed -i"
        elif cmd == "git":
            repo, i = cwd, 0
            while i < len(rest) and rest[i].startswith("-"):
                if rest[i] == "-C" and i + 1 < len(rest):
                    repo = resolve(rest[i + 1], repo) or repo
                    i += 1
                i += 1
            if i < len(rest):
                sub = rest[i]
                nxt = rest[i + 1] if i + 1 < len(rest) else ""
                if sub in GIT_WRITE and (sub, nxt) not in GIT_READ_FORMS:
                    if sub == "clone":
                        dests = [a for a in rest[i + 1:] if not a.startswith("-")]
                        if len(dests) >= 2:
                            yield resolve(dests[-1], repo), "git clone"
                    else:
                        yield repo, "git " + sub


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    cwd = data.get("cwd") or os.getcwd()
    home_domain = domain_of(os.environ.get("CLAUDE_PROJECT_DIR") or cwd)
    if home_domain is None:
        return
    tool, inp = data.get("tool_name"), data.get("tool_input") or {}
    if tool in ("Write", "Edit", "NotebookEdit"):
        p = inp.get("file_path") or inp.get("notebook_path")
        targets = [(resolve(p, cwd), tool)] if p else []
    elif tool == "Bash":
        targets = list(bash_targets(inp.get("command", ""), cwd))
    else:
        return
    for path, what in targets:
        other = domain_of(path) if path else None
        if other and other != home_domain:
            reason = (f"Refused: {what} would write to {path}, inside the "
                      f"{other} domain ({DOMAINS[other]}). This session belongs "
                      f"to the {home_domain} domain and may read {other} but "
                      f"never write to it. Exchange files through git/GitHub "
                      f"or the other account's inbox under "
                      f"~/.local/share/diogenes/inbox/ (Diogenes' rule 9), or "
                      f"ask Randy to carry the change across.")
            print(json.dumps({"hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason}}))
            return


if __name__ == "__main__":
    main()
