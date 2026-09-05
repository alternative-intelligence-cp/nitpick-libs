#!/usr/bin/env python3
"""Gather claims about the compiler that an audit should verify at the source.

Finds candidates. Does NOT verify them -- the verification is reading
`REPOS/nitpick/`. A claim that cites only another document in this ecosystem
is not verified, which is the whole reason this list is worth having.

Usage:  gather_claims.py [repo ...]        (default: cwd)
"""
import re, sys, subprocess
from pathlib import Path

# A sentence is a candidate if it asserts something about the language or the
# runtime: it cites a compiler decision, names a compiler path, or names a
# runtime/floor symbol.
PATTERNS = [
    ("cites-D",      re.compile(r'\bD-\d{3}\b')),
    ("cites-rule",   re.compile(r'\bNITPICK-[A-Z]+-\d+\b|\bTYPE-\d+\b|\bREACH-\d+\b')),
    ("compiler-path",re.compile(r'\b(?:runtime/npkrt\.ll|src/(?:frontend|backend|driver)/[\w/]+\.npk|lib/n\w+\.npk|npkg/[\w]+\.npk|bootstrap/[\w/]+)')),
    ("runtime-sym",  re.compile(r'\bnpk_\w+|@npk\.\w+')),
    ("syscall-claim",re.compile(r'\bsyscall\s+\d+\b|\bioctl\b|\brt_sigaction\b|\bsignalfd\b|\beventfd\b')),
]
SENT = re.compile(r'(?<=[.!?])\s+(?=[A-Z*`\[])')


def tracked_md(repo: Path):
    """Returns (files, how). `how` names which enumeration ran and is REPORTED
    by the caller, because the two paths have very different denominators:
    measured 2026-09-05 from the workbench root, `git ls-files` sees 34
    markdown files and the rglob fallback sees 334 -- the root's own, plus 297
    in five separate library checkouts a single audit must not attribute to
    one repository, plus 3 under a gitignored `.internal/`.

    The `except` is narrow ON PURPOSE. It was `except Exception`, which
    swallowed any error at all -- including a bug inside the try -- into the
    ten-times-wider path, silently. An audit's evidence gatherer is the last
    tool that should quietly change what it gathered.
    """
    try:
        out = subprocess.run(["git", "-C", str(repo), "ls-files", "*.md", "**/*.md"],
                             capture_output=True, text=True, check=True).stdout
        return [repo / p for p in out.split("\n") if p.strip()], "git ls-files"
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ([p for p in repo.rglob("*.md") if ".git/" not in str(p)],
                "rglob FALLBACK -- git unavailable; may span nested checkouts")


def main(argv):
    repos = [Path(a).resolve() for a in argv[1:]] or [Path.cwd()]
    total = 0
    for repo in repos:
        rows = []
        files, how = tracked_md(repo)
        for f in files:
            text = f.read_text(encoding="utf-8", errors="replace")
            for n, line in enumerate(text.split("\n"), 1):
                kinds = [k for k, p in PATTERNS if p.search(line)]
                if kinds:
                    rows.append((f.relative_to(repo), n, ",".join(kinds), line.strip()))
        denom = f"{len(files)} files via {how}"
        # A repository with no claims used to `continue` and print NOTHING, so
        # "gathered and found none" and "gathered nothing" were byte-identical
        # -- the same silence as a sweep that matches nothing (PLAYBOOK.md 6).
        if not rows:
            print(f"\n=== {repo.name} — no claims found ({denom}) ===")
            continue
        total += len(rows)
        print(f"\n=== {repo.name} — {len(rows)} claim(s) to verify at the source ({denom}) ===")
        for path, n, kinds, line in rows:
            print(f"  [ ] {path}:{n}  ({kinds})")
            print(f"      {line[:150]}")
    print(f"\n{total} candidate(s). Verify each against REPOS/nitpick/ — a citation")
    print("of another document in this ecosystem does not count as verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
