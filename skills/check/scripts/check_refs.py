#!/usr/bin/env python3
"""Cross-reference integrity for a Nitpick ecosystem repository.

Diffs the documents against each other. Every finding is something a human
wrote that no longer resolves; none of them needs judgement, which is why this
is a script and not a checklist.

Usage:  check_refs.py [repo-path ...]      (default: cwd)
Exit:   0 clean, 1 findings, 2 could not run
"""
import os, re, sys, subprocess
from pathlib import Path

LINK = re.compile(r'\]\(([^)#]+?)(?:#[^)]*)?\)')
DECL = re.compile(r'^###\s+(?:~~)?\*{0,2}([A-Z]{1,3}-\d+)', re.M)
OQ_DEF = re.compile(r'\b(O-[A-Z]\d+|Q-\d+)\b(?=\s*(?:—|~~))')
OQ_REF = re.compile(r'\b(O-[A-Z]\d+|Q-\d+)\b')
LEAK = re.compile(r'/home/[a-z_][a-z0-9_-]*|ghp_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY')


def tracked_md(repo: Path):
    """Markdown files git actually tracks — an untracked scratch file is not a finding."""
    try:
        out = subprocess.run(["git", "-C", str(repo), "ls-files", "*.md", "**/*.md"],
                             capture_output=True, text=True, check=True).stdout
        return [repo / p for p in out.split("\n") if p.strip()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in repo.rglob("*.md") if ".git/" not in str(p)]


def check(repo: Path):
    findings = []
    files = tracked_md(repo)
    if not files:
        return [("no-markdown", f"{repo}: no tracked markdown — wrong directory?")]

    # 1. every relative link resolves
    for f in files:
        for m in LINK.finditer(f.read_text(encoding="utf-8", errors="replace")):
            t = m.group(1).strip()
            if t.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if not (f.parent / t).resolve().exists():
                findings.append(("broken-link", f"{f.relative_to(repo)}: {t}"))

    # 2/3. decisions: defined, cited, and not duplicated
    dec = repo / "meta" / "DECISIONS.md"
    if dec.exists():
        ids = DECL.findall(dec.read_text(encoding="utf-8"))
        defined = set(ids)
        for d in sorted({i for i in ids if ids.count(i) > 1}):
            findings.append(("duplicate-decision", f"{d} declared {ids.count(d)} times"))
        prefixes = {i.split("-")[0] for i in defined}
        cited = set()
        for f in files:
            if f.name == "DECISIONS.md":
                continue
            txt = f.read_text(encoding="utf-8", errors="replace")
            for pre in prefixes:
                cited |= set(re.findall(rf'\b{pre}-\d+\b', txt))
        for d in sorted(cited - defined, key=lambda s: (s.split("-")[0], int(s.split("-")[1]))):
            findings.append(("cited-undefined", f"{d} is cited and never declared"))
        for d in sorted(defined - cited, key=lambda s: (s.split("-")[0], int(s.split("-")[1]))):
            findings.append(("defined-uncited", f"{d} is declared and never cited — dead decision, or a spec that forgot to cite it"))

    # 4. open questions referenced but never defined
    oq = repo / "meta" / "OPEN_QUESTIONS.md"
    if oq.exists():
        defined_q = set(OQ_DEF.findall(oq.read_text(encoding="utf-8")))
        refs = set()
        for f in files:
            if f.name == "OPEN_QUESTIONS.md":
                continue
            refs |= set(OQ_REF.findall(f.read_text(encoding="utf-8", errors="replace")))
        for q in sorted(refs - defined_q):
            findings.append(("undefined-question", f"{q} is referenced and never defined"))

    # 5. nothing machine-specific in a tracked file
    for f in files:
        for m in LEAK.finditer(f.read_text(encoding="utf-8", errors="replace")):
            findings.append(("leak", f"{f.relative_to(repo)}: {m.group(0)[:40]}"))

    return findings


def main(argv):
    repos = [Path(a).resolve() for a in argv[1:]] or [Path.cwd()]
    total = 0
    for repo in repos:
        if not repo.is_dir():
            print(f"!! {repo}: not a directory", file=sys.stderr)
            return 2
        fs = check(repo)
        name = repo.name
        if not fs:
            print(f"  {name:<18} clean")
            continue
        total += len(fs)
        print(f"  {name:<18} {len(fs)} finding(s)")
        for kind, msg in fs:
            print(f"      [{kind}] {msg}")
    if total:
        print(f"\n{total} finding(s). Each is something a human wrote that no longer resolves.")
        return 1
    print("\nAll clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
