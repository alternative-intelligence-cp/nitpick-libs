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
    # The fixture is ASSEMBLED rather than written literally. Since the leak
    # scan widened to every tracked TEXT file it reads this control too, and a
    # literal here makes the suite flag itself -- a false positive in the one
    # check with a security shape, which is how a guard gets switched off. An
    # exclusion list would also have worked and would have been worse: it is a
    # check narrower than its name, which is the defect this ecosystem has now
    # found seven times.
    ("leak", lambda r: append(r, "meta/specs/A.md", "\nMeasured at /" + "home/someone/secret.\n"), {"leak"}),
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
    # A tracked file deleted and NOT staged. `git ls-files` reads the index so
    # it is still listed, and opening it used to raise FileNotFoundError and
    # take the whole check down with a traceback — in exactly the state the
    # rule mandates, since check_refs is required to run BEFORE `git add`.
    # Removing A.md also breaks README's link to it and orphans X-1, which is
    # correct and is why all three kinds are expected: the point of the case is
    # that the check REPORTS instead of dying, and still reaches every later
    # check on the files that do exist.
    ("tracked-file-missing", lambda r: (r / "meta" / "specs" / "A.md").unlink(), {"tracked-file-missing", "broken-link", "defined-uncited"}),
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


def run(repo, env=None):
    r = subprocess.run([sys.executable, str(SCRIPT), str(repo)], capture_output=True, text=True,
                       env=env)
    kinds = {l.strip()[1:].split("]")[0] for l in r.stdout.splitlines() if l.strip().startswith("[")}
    return r.returncode, kinds, r.stdout


# The CASES table above checks WHICH FAULTS are found. These two check WHAT WAS
# EXAMINED, which is a different property and was the unchecked one: check_refs
# enumerates with `git ls-files` but silently falls back to a recursive rglob
# when git is unavailable, and from the workbench root those denominators are
# 34 files and 334 -- the second spanning five separate library checkouts. The
# fallback is not wrong; reporting either one without saying which is. Measured
# 2026-09-05: with git absent the check said "57 finding(s)" under the same
# repository label as a true clean-over-34.
def denominator_cases(repo, nogit_dir):
    out = []
    _, _, with_git = run(repo)
    out.append(("denominator-stated",
                "git ls-files" in with_git and "files via" in with_git))
    # The LEAK scan runs over every tracked TEXT file, not the markdown set, so
    # it has its OWN denominator and that number must print too. Without this
    # case the widened scan could silently narrow back to markdown and every
    # line would still read "clean" -- which is the precise failure the
    # denominator rule exists to prevent, one level down.
    out.append(("leak-denominator-stated",
                "leak scan" in with_git and "text of" in with_git))
    # python is found via sys.executable, so emptying PATH removes git alone.
    _, _, no_git = run(repo, env=dict(os.environ, PATH=str(nogit_dir)))
    out.append(("fallback-announces-itself",
                "rglob FALLBACK" in no_git))
    return out


def main():
    fails = []
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        b = base(tmp)
        for name, mutate, expected in CASES:
            repo = tmp / name / "fx"
            shutil.copytree(b, repo)
            mutate(repo)
            rc, kinds, _ = run(repo)
            ok = kinds == expected and (rc == 0) == (not expected)
            print(f"  {'ok ' if ok else 'FAIL'} {name:<20} expected {sorted(expected) or 'clean'}, got {sorted(kinds) or 'clean'} (exit {rc})")
            if not ok:
                fails.append(name)
        nogit = tmp / "nogit-bin"
        nogit.mkdir()
        for name, ok in denominator_cases(b, nogit):
            print(f"  {'ok ' if ok else 'FAIL'} {name:<20} {'denominator reported' if ok else 'DENOMINATOR NOT REPORTED'}")
            if not ok:
                fails.append(name)
    print()
    if fails:
        print(f"{len(fails)} FAILURE(S): {', '.join(fails)}")
        return 1
    neg = sum(1 for _, _, expected in CASES if not expected)
    total = len(CASES) + 2  # + the two denominator cases
    print(f"All {total} cases correct ({len(CASES) - neg} fault classes, "
          f"{neg} false-positive control{'' if neg == 1 else 's'}, "
          f"2 denominator cases).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
