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


FENCE = re.compile(r"^```.*?^```", re.S | re.M)


def prose(text: str) -> str:
    """The part of a document that CITES, with fenced blocks removed.

    A fenced block is quoted material -- sample output, a transcript, a
    verbatim check finding -- not this document citing a decision. Scanning it
    reported `cited-undefined` against a file that had merely pasted evidence,
    and this workbench REQUIRES a worker to paste check output verbatim into
    its committed REPORT block. So the check fired on the behaviour the
    protocol mandates, which puts the correct response and the safe response
    in opposite directions: the lesson it teaches is to paraphrase evidence.

    Inline code spans are deliberately NOT stripped. `RX-126` in backticks is
    how a real citation is written throughout this workbench, so removing them
    would turn genuine citations into `defined-uncited`. That leaves verbatim
    output quoted INLINE still miscounted -- a stated limit, not a closed one.
    The rule it implies is that verbatim output belongs in a fence.
    """
    return FENCE.sub("", text)


def tracked_md(repo: Path):
    """Markdown files git actually tracks AND that exist on disk.

    Returns (files, missing). `git ls-files` reads the INDEX, so a tracked file
    deleted but not yet staged is still listed while `open()` on it raises
    FileNotFoundError. This crashed the whole check with a traceback -- and it
    crashed it in exactly the state this workbench MANDATES, because the rule
    is "run check_refs BEFORE `git add` and gate the commit on it", and an
    unstaged deletion is precisely the pre-`git add` state. A rule and a tool
    that cannot both be satisfied is a defect in one of them (PLAYBOOK.md 6).

    The missing ones are RETURNED rather than silently dropped, because
    quietly narrowing the file set is how a check comes to report "All clean"
    over a denominator it never states.

    Returns (files, missing, how) -- `how` names which enumeration ran, and it
    is REPORTED, because the paragraph above was true of narrowing and this
    function then WIDENED the set by ten without saying so. Measured
    2026-09-05 from the workbench root: `git ls-files` sees 34 markdown files,
    the rglob fallback sees 334 -- the root's own 34, plus 297 belonging to
    five separate library checkouts, plus 3 under a gitignored `.internal/`.
    With git absent from PATH this check reported "57 finding(s)" against a
    true answer of clean-over-34, under the SAME repository label, so every
    one of those 57 read as this repository's fault when each belonged to a
    repository W-7 forbids the running session to touch.

    So the fallback is not wrong, it is a different denominator, and the whole
    rule of this workbench is that a denominator is stated rather than
    implied. `git ls-files` cannot fail at a repository root; the reachable
    trigger is git missing from PATH, which is a CI shape, not a local one.
    """
    try:
        out = subprocess.run(["git", "-C", str(repo), "ls-files", "*.md", "**/*.md"],
                             capture_output=True, text=True, check=True).stdout
        listed = [repo / p for p in out.split("\n") if p.strip()]
        how = "git ls-files"
    except (subprocess.CalledProcessError, FileNotFoundError):
        listed = [p for p in repo.rglob("*.md") if ".git/" not in str(p)]
        how = "rglob FALLBACK -- git unavailable; may span nested checkouts"
    files = [p for p in listed if p.exists()]
    return files, [p for p in listed if not p.exists()], how


def check(repo: Path):
    """Returns (findings, denominator). The denominator is returned, not
    printed here, because a caller that reports findings without reporting
    what was examined is the failure this function's own docstring warns of."""
    findings = []
    files, missing, how = tracked_md(repo)
    denom = f"{len(files)} files via {how}"
    # Not a fault in the repository — a tracked file deleted and not yet
    # staged — but it narrows what every check below examined, so it is
    # reported rather than absorbed.
    for p in sorted(missing):
        findings.append(("tracked-file-missing",
                         f"{p.relative_to(repo)}: tracked but not on disk — "
                         "deleted and not staged? Not scanned by any check below"))
    if not files:
        return [("no-markdown", f"{repo}: no tracked markdown — wrong directory?")], denom

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
            txt = prose(f.read_text(encoding="utf-8", errors="replace"))
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
            refs |= set(OQ_REF.findall(prose(f.read_text(encoding="utf-8", errors="replace"))))
        for q in sorted(refs - defined_q):
            findings.append(("undefined-question", f"{q} is referenced and never defined"))

    # 5. nothing machine-specific in a tracked file. Deliberately NOT run
    # through prose(): a home directory pasted inside a fence is still leaked,
    # and quoting is exactly how one gets there.
    for f in files:
        for m in LEAK.finditer(f.read_text(encoding="utf-8", errors="replace")):
            findings.append(("leak", f"{f.relative_to(repo)}: {m.group(0)[:40]}"))

    return findings, denom


def main(argv):
    repos = [Path(a).resolve() for a in argv[1:]] or [Path.cwd()]
    total = 0
    for repo in repos:
        if not repo.is_dir():
            print(f"!! {repo}: not a directory", file=sys.stderr)
            return 2
        fs, denom = check(repo)
        name = repo.name
        # The denominator prints on EVERY line, clean or not. "Swept and found
        # nothing" and "swept nothing" are otherwise byte-identical, which is
        # the failure this ecosystem has now met six times (PLAYBOOK.md 6).
        if not fs:
            print(f"  {name:<18} clean            ({denom})")
            continue
        total += len(fs)
        print(f"  {name:<18} {len(fs)} finding(s)    ({denom})")
        for kind, msg in fs:
            print(f"      [{kind}] {msg}")
    if total:
        print(f"\n{total} finding(s). Each is something a human wrote that no longer resolves.")
        return 1
    print("\nAll clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
