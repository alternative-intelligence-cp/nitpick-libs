#!/usr/bin/env python3
"""PreToolUse guard: refuse writes into the compiler tree.

The compiler at REPOS/nitpick runs verification and parity passes measured in
hours, and its own orchestration rules forbid editing a tree while a harness
runs on it. Reading it is expected and encouraged; writing to it from a library
or application session is not.

Covers Bash, Write and Edit in one place, because a guard that covers the file
tools and not the shell (or the reverse) has a hole exactly where somebody will
walk.

Self-scoping: a session whose working directory is inside the compiler tree is
allowed everything, so work on the compiler itself is unaffected.

THE RULE THAT MATTERS: a write is judged by its TARGET, never by whether the
command text mentions the tree. The first version of this guard matched the
whole command and refused `cat > START.md <<EOF` because the heredoc body
described the compiler -- blocking a write to another repository entirely. A
guard with false positives gets disabled, which is worse than no guard.

Reads the PreToolUse JSON on stdin. Prints a deny decision, or nothing.
"""
import json, os, re, shlex, sys

COMPILER = "/home/randy/Workspace/REPOS/nitpick"

# Commands whose non-flag arguments are ALL things they write to.
WRITE_CMDS = {
    "rm": "a removal", "rmdir": "a removal", "unlink": "a removal",
    "shred": "a removal", "tee": "tee", "truncate": "a truncate",
    "mkdir": "a create", "touch": "a create", "chmod": "a permission change",
    "chown": "an ownership change", "chgrp": "an ownership change",
    "patch": "patch",
}
# Commands where only the LAST argument is written; the rest are SOURCES, and
# reading a source out of the compiler tree is exactly what this guard must
# allow. Treating every argument as a target refused `cp ../nitpick/npkc /tmp/`
# -- copying the compiler OUT, which is a read.
DEST_LAST_CMDS = {
    "cp": "a copy", "install": "an install", "rsync": "an rsync",
    "ln": "a link",
}
# `mv` is both: the destination is written AND the source is removed, so
# moving a file OUT of the compiler tree still modifies the compiler tree.
BOTH_ENDS_CMDS = {"mv": "a move"}
GIT_WRITE = {
    "add", "commit", "checkout", "switch", "restore", "reset", "revert",
    "merge", "rebase", "cherry-pick", "push", "pull", "fetch", "stash",
    "clean", "rm", "mv", "apply", "am", "init", "gc", "prune", "worktree",
    "tag", "remote", "config",
}
HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1.*?^\s*\2\s*$", re.S | re.M)


def strip_heredocs(cmd: str) -> str:
    """A heredoc body is DATA, not command. Removing it is what fixes the
    false positive that made this rewrite necessary."""
    prev = None
    while prev != cmd:
        prev, cmd = cmd, HEREDOC.sub("<<STRIPPED", cmd)
    return cmd


def under_compiler(target: str, cwd: str) -> bool:
    if not target or target.startswith("-"):
        return False
    t = os.path.expanduser(target)
    full = os.path.realpath(t if os.path.isabs(t) else os.path.join(cwd, t))
    return full == COMPILER or full.startswith(COMPILER + os.sep)


def targets(cmd: str, cwd: str):
    """Yield (target, description) for every write this command performs."""
    # Redirections: the token after > or >> (excluding 2>&1, >&2).
    for m in re.finditer(r"(?<![0-9&])>>?(?!&)\s*([^\s;|&()]+)", cmd):
        yield m.group(1), "a redirection"
    # `dd of=PATH`
    for m in re.finditer(r"\bof=([^\s;|&()]+)", cmd):
        yield m.group(1), "dd"

    try:
        toks = shlex.split(cmd, comments=True)
    except ValueError:
        toks = cmd.split()

    # `cd X && ...` moves the effective directory for everything after it.
    eff = cwd
    if len(toks) >= 2 and toks[0] == "cd":
        cand = os.path.realpath(os.path.join(cwd, os.path.expanduser(toks[1])))
        eff = cand
        toks = toks[2:]

    i = 0
    while i < len(toks):
        t = toks[i]
        if t in ("&&", "||", ";", "|"):
            i += 1
            continue
        base = os.path.basename(t)
        if base in WRITE_CMDS:
            for a in toks[i + 1:]:
                if a in ("&&", "||", ";", "|"):
                    break
                if not a.startswith("-"):
                    yield a, WRITE_CMDS[base]
        elif base in DEST_LAST_CMDS or base in BOTH_ENDS_CMDS:
            args = []
            for a in toks[i + 1:]:
                if a in ("&&", "||", ";", "|"):
                    break
                if not a.startswith("-"):
                    args.append(a)
            if base in BOTH_ENDS_CMDS:
                for a in args:
                    yield a, BOTH_ENDS_CMDS[base]
            elif args:
                yield args[-1], DEST_LAST_CMDS[base]
        elif base in ("sed", "perl") and any(
            a.startswith("-") and "i" in a for a in toks[i + 1:i + 4]
        ):
            for a in toks[i + 1:]:
                if a in ("&&", "||", ";", "|"):
                    break
                if not a.startswith("-"):
                    yield a, f"{base} -i"
        elif base == "git":
            rest = toks[i + 1:]
            gdir = None
            if len(rest) >= 2 and rest[0] == "-C":
                gdir, rest = rest[1], rest[2:]
            sub = next((r for r in rest if not r.startswith("-")), None)
            if sub in GIT_WRITE:
                yield (gdir if gdir is not None else "."), "a mutating git subcommand"
        i += 1

    # Anything yielded relative to a `cd`-shifted directory resolves there.
    if eff != cwd:
        return


def decide_bash(cmd: str, cwd: str):
    cmd = strip_heredocs(cmd)
    eff = cwd
    toks = cmd.split()
    if len(toks) >= 2 and toks[0] == "cd":
        eff = os.path.realpath(os.path.join(cwd, os.path.expanduser(toks[1])))
    for target, what in targets(cmd, cwd):
        if target and under_compiler(target, eff):
            return what
    return None


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    tool = data.get("tool_name")
    if tool not in ("Bash", "Write", "Edit", "NotebookEdit"):
        return 0
    cwd = os.path.realpath(data.get("cwd") or os.getcwd())
    if cwd == COMPILER or cwd.startswith(COMPILER + os.sep):
        return 0                                   # a compiler session may write
    ti = data.get("tool_input") or {}

    if tool == "Bash":
        what = decide_bash(ti.get("command") or "", cwd)
    else:
        target = ti.get("file_path") or ti.get("notebook_path") or ""
        what = "a direct write" if under_compiler(target, cwd) else None

    if what is None:
        return 0
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"Refused: {what} targeting the compiler tree at {COMPILER}, from a "
                "session outside it. The compiler is READ-ONLY from a library or "
                "application session -- it runs verification and parity passes "
                "measured in hours, and editing a tree while a harness runs on it "
                "invalidates the run. Reading, grepping and listing it are fine. If "
                "the compiler genuinely needs a change, record it as an O-N open "
                "question and raise it; do not make the edit."
            ),
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
