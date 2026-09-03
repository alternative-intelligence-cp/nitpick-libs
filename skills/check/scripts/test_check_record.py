#!/usr/bin/env python3
"""Control for check_record.py: one planted fault per finding class, plus a
clean case. Each case must produce EXACTLY the expected set of kinds.

A check that has never failed has not been shown to work.
"""
import os, shutil, subprocess, sys, tempfile
from pathlib import Path

SCRIPT = Path(__file__).with_name("check_record.py")
NAME = "nitpick-fixture"
ENV = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t",
           GIT_COMMITTER_EMAIL="t@t")

README = """# Cycle 0.0 — fixture

## Checklist

### 0.0.0 — the probes
- [x] first
- [x] second

### 0.0.1 — the skeleton
- [ ] later
"""
REPORT = """REPORT nitpick-fixture 0.0.0
status: DONE
stream: s2
model: test-model
toolchain: abc1234
commits:
  - HEAD cycle 0.0.0: the probes
harness: not run: no harness until 0.0.2
  - $NPKC tests/probe/probe01_x.npk -> exit 0
check: clean
record: meta/roadmap/0.0/0.0.0.md — DONE
next: n/a
findings-for-playbook: none
open-questions-raised: none
for-the-author: none
compiler-defect: none
tokens-and-time: unknown
"""
SUB = "# 0.0.0 — the probes — DONE (2026-09-03)\n\nbody\n\n## Execution record\n\n- did the thing\n\n" + REPORT


def git(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, env=ENV)


def base(tmp):
    repo = tmp / "base" / NAME
    (repo / "meta/roadmap/0.0").mkdir(parents=True)
    (repo / "meta/roadmap/0.0/README.md").write_text(README)
    (repo / "meta/roadmap/0.0/0.0.0.md").write_text(SUB)
    git(repo, "init", "-q")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "cycle 0.0.0: the probes")
    return repo


def edit(repo, rel, old, new):
    p = repo / rel
    s = p.read_text()
    assert old in s, (rel, old)
    p.write_text(s.replace(old, new, 1))


def commit(repo):
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "cycle 0.0.0: the probes, again")


CASES = [
    # (name, mutation(repo), subcycle id, expected kinds)
    ("clean", lambda r: None, "0.0.0", set()),
    ("no-file", lambda r: None, "0.0.9", {"no-file"}),
    ("bad-status", lambda r: (edit(r, "meta/roadmap/0.0/0.0.0.md", "— DONE (2026-09-03)", "— WIP"), commit(r)), "0.0.0", {"bad-status"}),
    ("no-report", lambda r: (edit(r, "meta/roadmap/0.0/0.0.0.md", REPORT, ""), commit(r)), "0.0.0", {"no-report"}),
    ("missing-field", lambda r: (edit(r, "meta/roadmap/0.0/0.0.0.md", "model: test-model\n", ""), commit(r)), "0.0.0", {"missing-field"}),
    ("bad-report-status", lambda r: (edit(r, "meta/roadmap/0.0/0.0.0.md", "status: DONE", "status: FINISHED"), commit(r)), "0.0.0", {"bad-report-status"}),
    ("status-mismatch", lambda r: (edit(r, "meta/roadmap/0.0/0.0.0.md", "status: DONE", "status: BLOCKED"), commit(r)), "0.0.0", {"status-mismatch"}),
    ("unknown-commit", lambda r: (edit(r, "meta/roadmap/0.0/0.0.0.md", "commits:\n", "commits:\n  - deadbeef1 nothing\n"), commit(r)), "0.0.0", {"unknown-commit"}),
    ("head-subject", lambda r: git(r, "commit", "-q", "--amend", "-m", "wrong subject"), "0.0.0", {"head-subject"}),
    ("dirty-tree", lambda r: (r / "stray.txt").write_text("x"), "0.0.0", {"dirty-tree"}),
    ("unticked", lambda r: (edit(r, "meta/roadmap/0.0/README.md", "- [x] second", "- [ ] second"), commit(r)), "0.0.0", {"unticked"}),
]


def run(repo, sid):
    r = subprocess.run([sys.executable, str(SCRIPT), str(repo), sid], capture_output=True, text=True)
    kinds = {l.strip()[1:].split("]")[0] for l in r.stdout.splitlines() if l.strip().startswith("[")}
    return r.returncode, kinds


def main():
    fails = []
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t)
        b = base(tmp)
        for name, mutate, sid, expected in CASES:
            repo = tmp / name / NAME
            shutil.copytree(b, repo)
            mutate(repo)
            rc, kinds = run(repo, sid)
            ok = kinds == expected and (rc == 0) == (not expected)
            print(f"  {'ok ' if ok else 'FAIL'} {name:<18} expected {sorted(expected) or 'clean'}, got {sorted(kinds) or 'clean'} (exit {rc})")
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
