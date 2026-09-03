---
name: check
description: Verify cross-reference integrity in a Nitpick ecosystem repository — every relative markdown link resolves, every decision cited is declared and every one declared is cited, no duplicate decision numbers, every open-question reference resolves, and no absolute path or credential leaks into a tracked file — and verify a worker's committed REPORT block against the tree. Run before every commit that touches meta/, before closing any cycle, and on every report before the verifier runs.
allowed-tools: Bash(python3 *) Bash(git status*) Bash(git diff*) Read Grep Glob
---

# Reference integrity

This ecosystem's own finding, from the compiler's cycle notes: **every hole was
found by a check that diffs two lists, and none of them by a test.** This is
that check, applied to the planning layer.

## Run it

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/check_refs.py [repo ...]
```

No argument checks the current directory. Several arguments check several
repositories — useful from a workbench after a cross-cutting change:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/check_refs.py . nitpick-tui nitpick-parse \
  nitpick-regex nitpick-sockets nitpick-time ../nitpick-apps ../nitpick-apps/nitpick-posix
```

Exit 0 clean, 1 findings, 2 could not run. It reads **git-tracked** markdown
only, so a scratch file in `meta/scratch/` is not a finding.

## What each finding means

| Finding | What it is, and what to do |
|---|---|
| `broken-link` | a relative link whose target does not exist. Usually a path that moved, or a level miscounted — `CLAUDE.md` sits at the repository root, so a workbench is one level up from a library and two from an app |
| `duplicate-decision` | one number declared twice. The later one needs a new number; **never renumber the earlier**, because its citation is already elsewhere |
| `cited-undefined` | a decision cited that was never declared. Either the decision is missing or the citation is a typo — read the citing sentence to tell which |
| `defined-uncited` | a decision declared that nothing cites. Either a dead decision, or a specification that states a rule and forgot to attribute it. **The second is far more common and is the real value of this check** |
| `undefined-question` | an `O-`/`Q-` reference with no definition. Usually a prefix collision — a specification's internal rule prefix must not collide with `O-N`, `O-x` or `Q-` |
| `leak` | an absolute home path or a credential in a tracked file. These repositories are public |

## The rule this enforces

**A settled decision's text is never rewritten.** When a check finds a
contradiction, the fix is a *new* decision that supersedes and says why — the
old text stays, dated, because it records what was true when it was made.

## Verifying a record

The worker's REPORT block (`skills/worker/SKILL.md` §9) is committed as the
last entry of the subcycle file's execution record. Before the verifier runs:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/check_record.py <repo> <cycle>.<sub>
```

Exit 0 clean, 1 findings, 2 could not run. The findings:

| Finding | What it is |
|---|---|
| `no-file` | the subcycle file does not exist |
| `bad-status` | the title line's status is not `PLANNED`, `RUNNING (…)` or `DONE (…)` |
| `no-report` | no `REPORT <repo> <id>` block under `## Execution record`, or the last one names another subcycle |
| `missing-field` | a required key of the block is absent |
| `bad-report-status` | the status is not one of the six |
| `status-mismatch` | `DONE`/`READY-TO-CLOSE` with a title not `DONE`, or a stopped status with a title `DONE` |
| `unknown-commit` | a hash under `commits:` that the repository does not have |
| `head-subject` | `HEAD`'s subject does not begin `cycle <id>:` on a done-like status |
| `dirty-tree` | uncommitted paths |
| `unticked` | status `DONE` and an unticked, unstruck item under the subcycle's `###` heading in the cycle README |

## Before you trust a clean run

Both scripts have a negative control beside them, and each runs first in a
dry run: `scripts/test_check_refs.py` plants one fault per class and requires
exactly that class back (six classes and one clean case);
`scripts/test_check_record.py` does the same for the record check (ten
classes and one clean case). If you extend a script, extend its control. A
check that has never failed has not been shown to work — which is how the
first of these controls came to exist: the skill promised it before it did.
