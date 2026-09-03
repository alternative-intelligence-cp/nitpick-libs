#!/usr/bin/env python3
"""Control for check_refs.py: one planted fault per finding class, plus a
clean case. Each case must produce EXACTLY the expected set of kinds.

The check skill promised this control before it existed; the first flagless
session noticed. A check that has never failed has not been shown to work.
"""
import os, shutil, subprocess, sys, tempfile
from pathlib import Path

SCRIPT = Path(__file__).with_name("check_refs.py")
ENV = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t",
           GIT_COMMITTER_EMAIL="t@t")

FILES = {
    "README.md": "# fixture\n\nSee [the spec](meta/specs/A.md).\n",
    "meta/DECISIONS.md": "# Decisions\n\n### X-1 — the first decision\n\nBecause.\n",
    "meta/OPEN_QUESTIONS.md": "# Open questions\n\n- **Q-1 — a question.** With a recommendation.\n",
    "meta/specs/A.md": "# A\n\nRule A-1 (X-1). See Q-1 and [decisions](../DECISIONS.md).\n",
}


def git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, env=ENV)


def base(tmp):
    repo = tmp / "base" / "fx"
    for rel, text in FILES.items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    git(repo, "init", "-q")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "fixture")
    return repo


def append(repo, rel, text):
    p = repo / rel
    p.write_text(p.read_text() + text)
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "fault")


CASES = [
    ("clean", lambda r: None, set()),
    ("broken-link", lambda r: append(r, "meta/specs/A.md", "\n[missing](B.md)\n"), {"broken-link"}),
    ("duplicate-decision", lambda r: append(r, "meta/DECISIONS.md", "\n### X-1 — declared twice\n\nOops.\n"), {"duplicate-decision"}),
    ("cited-undefined", lambda r: append(r, "meta/specs/A.md", "\nAlso X-9.\n"), {"cited-undefined"}),
    ("defined-uncited", lambda r: append(r, "meta/DECISIONS.md", "\n### X-2 — nobody cites this\n\nDead.\n"), {"defined-uncited"}),
    ("undefined-question", lambda r: append(r, "meta/specs/A.md", "\nSee Q-2.\n"), {"undefined-question"}),
    ("leak", lambda r: append(r, "meta/specs/A.md", "\nMeasured at /home/someone/secret.\n"), {"leak"}),
]


def run(repo):
    r = subprocess.run([sys.executable, str(SCRIPT), str(repo)], capture_output=True, text=True)
    kinds = {l.strip()[1:].split("]")[0] for l in r.stdout.splitlines() if l.strip().startswith("[")}
    return r.returncode, kinds


def main():
    fails = []
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        b = base(tmp)
        for name, mutate, expected in CASES:
            repo = tmp / name / "fx"
            shutil.copytree(b, repo)
            mutate(repo)
            rc, kinds = run(repo)
            ok = kinds == expected and (rc == 0) == (not expected)
            print(f"  {'ok ' if ok else 'FAIL'} {name:<20} expected {sorted(expected) or 'clean'}, got {sorted(kinds) or 'clean'} (exit {rc})")
            if not ok:
                fails.append(name)
    print()
    if fails:
        print(f"{len(fails)} FAILURE(S): {', '.join(fails)}")
        return 1
    print(f"All {len(CASES)} cases correct ({len(CASES) - 1} fault classes and one clean run).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
