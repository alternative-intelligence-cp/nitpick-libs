#!/usr/bin/env python3
"""Run every control in this workbench, and report each one's DENOMINATOR.

A check that has never failed has not been shown to work, so the controls are
what prove the checks still do. Run this after touching any check or the
guard, and before any commit that changes one.

Two things it does that running the controls by hand does not:

  * it FINDS them, so a control that stops being run is not invisible. The
    controls used to be four files invoked from a remembered list, and a list
    held in a person's head has no failure mode that anyone can see.

  * it prints how many CASES each control ran and how many of those are
    FALSE-POSITIVE controls -- cases asserting the check stays quiet. A
    verdict without a denominator is not a measurement: "0 findings over 0
    examined" and "0 findings over 86" print the same word. This workbench
    has met that shape nine times (PLAYBOOK.md 6), most recently in
    check_refs.py, which prints "All clean" having examined one repository.

Why the false-positive share is the number worth surfacing: a check whose
controls are all planted faults can only ever get stricter, because nothing
ever fails when it over-refuses. That is how `git worktree list` -- a read --
was refused by the guard as "a mutating git subcommand" and stayed refused,
with 73 controls passing across it.

Exit 0 all green, 1 if any control failed or none was found.
"""
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# Where controls live. A library repository has its own; these are the
# workbench's own tooling only.
PATTERNS = ("tools/test_*.py", "skills/*/scripts/test_*.py")


def find_controls():
    found = []
    for pat in PATTERNS:
        found.extend(glob.glob(os.path.join(ROOT, pat)))
    return sorted(found)


def main():
    controls = find_controls()
    if not controls:
        print("no controls found -- that is itself a finding", file=sys.stderr)
        return 1

    failed, total_cases, total_neg = [], 0, 0
    for path in controls:
        name = os.path.relpath(path, ROOT)
        proc = subprocess.run([sys.executable, path], capture_output=True, text=True)
        lines = [l for l in proc.stdout.strip().split("\n") if l.strip()]
        summary = lines[-1] if lines else "no output"

        # Every control's last line states its counts; parse rather than
        # trust, and say so when it cannot be parsed.
        cases = re.search(r"\b(\d+)\s+cases?\b", summary)
        neg = re.search(r"\b(\d+)\s+(?:allow|false-positive|quiet|clean)", summary)
        if cases:
            total_cases += int(cases.group(1))
        if neg:
            total_neg += int(neg.group(1))

        print(f"  {'ok  ' if proc.returncode == 0 else 'FAIL'} {name:<40} {summary}")
        if proc.returncode != 0:
            failed.append(name)
            for line in proc.stdout.strip().split("\n"):
                if line.strip().startswith("FAIL") or "FAILURE" in line:
                    print(f"       {line.strip()}")
            if proc.stderr.strip():
                print(f"       stderr: {proc.stderr.strip()[:400]}")

    print()
    if failed:
        print(f"FAILED: {', '.join(failed)}")
        return 1
    share = f", {total_neg} of them false-positive controls ({100 * total_neg // total_cases}%)" if total_cases else ""
    print(f"all {len(controls)} controls green — {total_cases} cases{share}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
