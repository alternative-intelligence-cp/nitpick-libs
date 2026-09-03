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
    try:
        out = subprocess.run(["git", "-C", str(repo), "ls-files", "*.md", "**/*.md"],
                             capture_output=True, text=True, check=True).stdout
        return [repo / p for p in out.split("\n") if p.strip()]
    except Exception:
        return [p for p in repo.rglob("*.md") if ".git/" not in str(p)]


def main(argv):
    repos = [Path(a).resolve() for a in argv[1:]] or [Path.cwd()]
    total = 0
    for repo in repos:
        rows = []
        for f in tracked_md(repo):
            text = f.read_text(encoding="utf-8", errors="replace")
            for n, line in enumerate(text.split("\n"), 1):
                kinds = [k for k, p in PATTERNS if p.search(line)]
                if kinds:
                    rows.append((f.relative_to(repo), n, ",".join(kinds), line.strip()))
        if not rows:
            continue
        total += len(rows)
        print(f"\n=== {repo.name} — {len(rows)} claim(s) to verify at the source ===")
        for path, n, kinds, line in rows:
            print(f"  [ ] {path}:{n}  ({kinds})")
            print(f"      {line[:150]}")
    print(f"\n{total} candidate(s). Verify each against REPOS/nitpick/ — a citation")
    print("of another document in this ecosystem does not count as verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
