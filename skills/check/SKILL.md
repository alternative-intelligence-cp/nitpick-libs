---
name: check
description: Verify cross-reference integrity in a Nitpick ecosystem repository — every relative markdown link resolves, every decision cited is declared and every one declared is cited, no duplicate decision numbers, every open-question reference resolves, and no absolute path or credential leaks into a tracked file. Run before every commit that touches meta/, and before closing any cycle.
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

## Before you trust a clean run

The script has a negative control: it is known to catch all six classes. If you
extend it, extend the control too. A check that has never failed has not been
shown to work.
