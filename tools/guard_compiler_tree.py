#!/usr/bin/env python3
"""PreToolUse guard for the Nitpick ecosystem: three rules, one script.

1. THE COMPILER TREE IS READ-ONLY from any session started outside it. It
   runs verification and parity passes measured in hours, and its own
   orchestration rules forbid editing a tree while a harness runs on it.
2. A LIBRARY OR APPLICATION REPOSITORY IS WRITTEN ONLY WHEN CLAIMED on the
   board (W-7), unless the session was started inside that repository.
3. THE WORKBENCH'S OWN FILES ARE WRITTEN ONLY BY ITS NAMED WRITER (W-16):
   the board's `Workbench writer:` line names a session id, or says `none`.
   BOARD.md itself is exempt -- it IS the lock. Taking it is always possible
   and always in the history; the session refused afterwards is the one that
   lost it. Without the exemption nobody could ever hand the lock over: the
   first live run of this rule locked out the session that wrote it.

Covers Bash, Write, Edit and NotebookEdit in one place, because a guard that
covers the file tools and not the shell (or the reverse) has a hole exactly
where somebody will walk.

Self-scoping is on the SESSION'S PROJECT DIRECTORY (`CLAUDE_PROJECT_DIR`),
not on the hook's per-call `cwd`, because `cwd` follows the shell's `cd` and
a `cd` into the compiler tree -- a read, and allowed -- would otherwise
disarm the guard for the next call. The per-call `cwd` is still what
relative targets resolve against, because it is what the shell will use.

THE RULE THAT MATTERS: a write is judged by its TARGET, never by whether the
command text mentions a tree. The first version of this guard refused
`cat > START.md <<EOF` because the heredoc body described the compiler. A
guard with false positives gets disabled, which is worse than no guard.

Known limits, stated: an interpreter heredoc that writes (`python3 - <<PY`)
cannot be classified from the command text; a target containing an
unexpanded variable (`"$REPO"`) cannot be resolved and is not judged. The
airtight mechanism for the first is the sandbox's `filesystem.denyWrite`,
which is configured nowhere (BOARD.md question 3, the author's call).

The heredoc limit is ALSO named in the compiler refusal message itself, not
only here. Guidance resists a temptation only where somebody is standing when
it matters: a docstring is read by whoever edits this file, and a refusal is
read by whoever just met it. The `devteam` run measured this working -- a
verifier that had never seen the finding met such a message and reported it
did not use the workaround because the message named it.

Reads the PreToolUse JSON on stdin. Prints a deny decision, or nothing.
"""
import json, os, re, shlex, sys


def env_path(name, default):
    return os.path.realpath(os.path.expanduser(os.environ.get(name) or default))


COMPILER = env_path("NPK_COMPILER_DIR", "~/Workspace/REPOS/nitpick")
LIBS = env_path("NPK_LIBS_DIR", "~/Workspace/REPOS/nitpick-libs")
APPS = env_path("NPK_APPS_DIR", "~/Workspace/REPOS/nitpick-apps")
WORKBENCHES = (LIBS, APPS)
BOARD = os.path.join(LIBS, "BOARD.md")

# Commands whose non-flag arguments are ALL things they write to.
WRITE_CMDS = {
    "rm": "a removal", "rmdir": "a removal", "unlink": "a removal",
    "shred": "a removal", "tee": "tee", "truncate": "a truncate",
    "mkdir": "a create", "touch": "a create", "chmod": "a permission change",
    "chown": "an ownership change", "chgrp": "an ownership change",
    "patch": "patch",
}
# Only the LAST argument is written; the rest are SOURCES, and reading a
# source out of the compiler tree is exactly what this guard must allow.
DEST_LAST_CMDS = {"cp": "a copy", "install": "an install", "rsync": "an rsync", "ln": "a link"}
# Both ends: the destination is written AND the source is removed.
BOTH_ENDS_CMDS = {"mv": "a move"}
GIT_WRITE = {
    "add", "commit", "checkout", "switch", "restore", "reset", "revert",
    "merge", "rebase", "cherry-pick", "push", "pull", "fetch", "stash",
    "clean", "rm", "mv", "apply", "am", "init", "gc", "prune", "worktree",
    "tag", "remote", "config",
}
# Several GIT_WRITE members have READ-ONLY forms, and refusing one of those is
# a false positive -- this guard refused `git worktree list`, a read, as "a
# mutating git subcommand" until 2026-09-05, because the set is keyed on the
# subcommand and `worktree` covers both `list` and `add`. The subcommand alone
# cannot decide it, so the token AFTER it does. Anything not named here stays a
# write: the default is refusal and this table only ever narrows one.
GIT_READ_FORMS = {
    "worktree": {"list"},
    "stash": {"list", "show"},
    "remote": {"-v", "--verbose", "show", "get-url"},
    "tag": {"-l", "--list", "--contains", "--points-at", "--merged", "--no-merged"},
    "config": {"--get", "--get-all", "--get-regexp", "--list", "-l"},
}
# Bare `git tag` and `git remote` LIST. Bare `git stash` CREATES one, so the
# bare form is not a read for every subcommand and cannot be inferred.
GIT_BARE_READS = {"tag", "remote"}
HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1.*?^\s*\2\s*$", re.S | re.M)
SEPARATORS = {"&&", "||", ";", ";;", "|", "|&", "&"}
REDIRECTS = {">", ">>", "&>", "&>>"}


def git_is_read(sub: str, rest) -> bool:
    """True when a GIT_WRITE subcommand was invoked in one of its read forms."""
    if sub not in GIT_READ_FORMS:
        return False
    after = rest[rest.index(sub) + 1:]
    if not after:
        return sub in GIT_BARE_READS
    return bool(GIT_READ_FORMS[sub] & set(after))


def strip_heredocs(cmd: str) -> str:
    """A heredoc body is DATA, not command."""
    prev = None
    while prev != cmd:
        prev, cmd = cmd, HEREDOC.sub("<<STRIPPED", cmd)
    return cmd


def inside(path: str, root: str) -> bool:
    return path == root or path.startswith(root + os.sep)


def resolve(target: str, cwd: str):
    """Absolute, real path of a target -- or None if it cannot be judged."""
    if not target or target.startswith("-") or "$" in target:
        return None
    t = os.path.expanduser(target)
    return os.path.realpath(t if os.path.isabs(t) else os.path.join(cwd, t))


def tokens(cmd: str):
    try:
        lex = shlex.shlex(cmd, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        return list(lex)
    except ValueError:
        return cmd.split()


def targets(cmd: str, cwd: str):
    """Yield (absolute target, description) for every write this command
    performs, following `cd`/`pushd` anywhere in the chain and subshells."""
    for m in re.finditer(r"\bof=([^\s;|&()]+)", cmd):          # dd of=PATH
        yield resolve(m.group(1), cwd), "dd"
    toks = tokens(cmd)
    eff, stack, seg = cwd, [], []

    def flush(seg, eff):
        if not seg:
            return eff
        base = os.path.basename(seg[0])
        args = [a for a in seg[1:] if not a.startswith("-")]
        if base in ("cd", "pushd"):
            dest = os.path.expanduser(args[0]) if args else os.path.expanduser("~")
            if "$" not in dest:
                return os.path.realpath(dest if os.path.isabs(dest) else os.path.join(eff, dest))
            return eff
        return eff

    i = 0
    n = len(toks)
    while i < n:
        t = toks[i]
        if t == "(":
            stack.append(eff); seg = []; i += 1; continue
        if t == ")":
            eff = flush(seg, eff); seg = []
            eff = stack.pop() if stack else eff
            i += 1; continue
        if t in SEPARATORS:
            eff = flush(seg, eff); seg = []; i += 1; continue
        if t in REDIRECTS:
            if i + 1 < n and not toks[i + 1].startswith("&"):
                yield resolve(toks[i + 1], eff), "a redirection"
                i += 2; continue
            i += 1; continue
        if t.startswith(">") or t.startswith("<"):            # >&, <, <<, 2>&1 pieces
            i += 1; continue
        seg.append(t)
        # judge write commands as their arguments arrive, against the CURRENT eff
        i += 1
        if i == n or toks[i] in SEPARATORS or toks[i] in ("(", ")") or toks[i] in REDIRECTS:
            base = os.path.basename(seg[0])
            args = [a for a in seg[1:] if not a.startswith("-")]
            if base in WRITE_CMDS:
                for a in args:
                    yield resolve(a, eff), WRITE_CMDS[base]
            elif base in BOTH_ENDS_CMDS:
                for a in args:
                    yield resolve(a, eff), BOTH_ENDS_CMDS[base]
            elif base in DEST_LAST_CMDS and args:
                yield resolve(args[-1], eff), DEST_LAST_CMDS[base]
            elif base in ("sed", "perl") and any(a.startswith("-") and "i" in a for a in seg[1:4]):
                for a in args:                 # the expression is not a file
                    r = resolve(a, eff)
                    if r and os.path.exists(r):
                        yield r, f"{base} -i"
            elif base == "git":
                rest = seg[1:]
                gdir = None
                if len(rest) >= 2 and rest[0] == "-C":
                    gdir, rest = rest[1], rest[2:]
                sub = next((r for r in rest if not r.startswith("-")), None)
                if sub in GIT_WRITE and not git_is_read(sub, rest):
                    yield resolve(gdir if gdir is not None else ".", eff), "a mutating git subcommand"
    # (a trailing segment is judged by the loop above on its last token)


def board_lines():
    try:
        with open(BOARD, encoding="utf-8", errors="replace") as f:
            return f.read().split("\n")
    except OSError:
        return []


def claimed(name: str, lines) -> bool:
    tag = f"`{name}`"
    return any(l.startswith("|") and tag in l and "CLAIMED" in l for l in lines)


def writer_allows(session_id: str, lines) -> bool:
    for l in lines:
        if l.startswith("**Workbench writer:**"):
            val = l[len("**Workbench writer:**"):]
            if re.search(r"\bnone\b", val):
                return True
            return bool(session_id) and session_id in val
    return True                                    # no writer line: not enforced


def repo_of(path: str):
    """(workbench, repo-name-or-None) if the path is under a workbench."""
    for wb in WORKBENCHES:
        if inside(path, wb):
            rel = os.path.relpath(path, wb)
            name = rel.split(os.sep)[0] if rel != "." else None
            if name and os.path.exists(os.path.join(wb, name, ".git")):
                return wb, name
            return wb, None
    return None


def judge(target, what, project, session_id, lines):
    """None, or (rule, reason) for a target this session may not write."""
    if target is None:
        return None
    if inside(target, COMPILER):
        return "compiler", (
            f"Refused: {what} targeting the compiler tree at {COMPILER}, from a "
            "session outside it. The compiler is READ-ONLY from a library or "
            "application session -- it runs verification and parity passes "
            "measured in hours, and editing a tree while a harness runs on it "
            "invalidates the run. Reading, grepping and listing it are fine. If "
            "the compiler genuinely needs a change, record it as an O-N open "
            "question and raise it; do not make the edit.\n\n"
            "Do not reach for an interpreter to do the same write. A heredoc "
            "like `python3 - <<PY` ... open(path,'w') ... PY cannot be "
            "classified from the command text, so it is NOT refused -- that is "
            "a KNOWN LIMIT of this guard, not permission. It is the first thing "
            "anyone finds after this message and it does not feel like evasion, "
            "which is exactly why it is named here rather than only in this "
            "file's docstring. This harness also ships a standing instruction "
            "preferring heredocs and `sed` over Write/Edit, so the unjudged "
            "form is the one you will reach for by default; prefer Write or "
            "Edit here, which this guard can actually see. And note what the "
            "backstop is NOT: nothing in this workbench reports the write "
            "afterwards. The refusal you are reading is the only mechanism "
            "watching, so going around it leaves a harness run of several hours "
            "invalidated with no record of what did it.")
    hit = repo_of(target)
    if not hit:
        return None
    wb, name = hit
    if name:
        repo = os.path.join(wb, name)
        if inside(project, repo) or claimed(name, lines):
            return None
        return "claim", (
            f"Refused: {what} into `{name}`, which no stream has claimed on "
            "BOARD.md. One writer per repository (W-7): the orchestrator claims a "
            "repository on the board before anyone writes to it. If you are "
            "working in this repository by hand, start the session inside it.")
    if target == BOARD or writer_allows(session_id, lines):
        return None                            # the board is the lock itself
    return "writer", (
        f"Refused: {what} into the workbench, and BOARD.md names another "
        f"session as the workbench's writer (this session is "
        f"{session_id or 'unknown'}). One writer here (W-16). If that session "
        "is gone, take the lock: set the `Workbench writer:` line to this "
        "session's id -- the board itself is always writable -- and record "
        "the takeover in RECORD.md.")


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    tool = data.get("tool_name")
    if tool not in ("Bash", "Write", "Edit", "NotebookEdit"):
        return 0
    cwd = os.path.realpath(data.get("cwd") or os.getcwd())
    project = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or cwd)
    if inside(project, COMPILER):
        return 0                                   # a compiler session may write
    session_id = str(data.get("session_id") or "")
    ti = data.get("tool_input") or {}
    lines = board_lines()

    verdict = None
    if tool == "Bash":
        # a newline separates commands as surely as `;` -- the first version
        # swallowed the line after a heredoc into the interpreter's segment
        cmd = strip_heredocs(ti.get("command") or "").replace("\n", " ; ")
        for target, what in targets(cmd, cwd):
            verdict = judge(target, what, project, session_id, lines)
            if verdict:
                break
    else:
        path = ti.get("file_path") or ti.get("notebook_path") or ""
        verdict = judge(resolve(path, cwd), "a direct write", project, session_id, lines)

    if verdict is None:
        return 0
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": verdict[1],
    }}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
