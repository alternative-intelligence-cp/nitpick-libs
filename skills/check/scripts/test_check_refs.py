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
    # --- FALSE-POSITIVE CONTROLS: content that must NOT produce a finding ----
    # Until 2026-09-05 this control had one negative case ("clean") and six
    # planted faults, so nothing here could ever fail by over-reporting. A
    # check whose controls are all faults can only get stricter.
    #
    # `quoted-finding` is the one that matters most. This workbench REQUIRES a
    # worker to paste check output verbatim into its committed REPORT block,
    # so if the check reads an identifier inside its own quoted finding as a
    # citation, it reports a fault against the file that obeyed it. That is
    # the worst class of check defect -- it puts the correct response and the
    # safe response in opposite directions, and the lesson an agent learns is
    # to paraphrase the evidence next time.
    ("fenced-id", lambda r: append(r, "meta/specs/A.md", "\n```\n### X-9 — an example inside a fence\n```\n"), set()),
    ("quoted-finding", lambda r: append(r, "meta/specs/A.md", "\n```\n[cited-undefined] meta/specs/A.md:4 X-9 is cited and never declared\n```\n"), set()),
    # A real citation written the way this workbench writes them -- in
    # backticks, in bold -- must still COUNT, or stripping quoted material
    # would silently turn genuine citations into `defined-uncited`.
    ("backticked-citation-still-counts", lambda r: append(r, "meta/DECISIONS.md", "\n### X-3 — cited only in backticks\n\nBecause.\n") or append(r, "meta/specs/A.md", "\nSee **`X-3`** for the rule.\n"), set()),
]

# KNOWN GAP, stated rather than closed: verbatim check output quoted INLINE
# (single backticks, not a fence) is still read as a citation. It is not
# fixable by stripping inline spans, because `X-3` in backticks is how a real
# citation is written here -- the case directly above asserts that. The rule
# this implies is that verbatim output belongs in a fence, and a rule is what
# it needs; a check that guessed which backticks were quotations would be
# inventing an agreement nothing requires.


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
    neg = sum(1 for _, _, expected in CASES if not expected)
    print(f"All {len(CASES)} cases correct ({len(CASES) - neg} fault classes, "
          f"{neg} false-positive control{'' if neg == 1 else 's'}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
