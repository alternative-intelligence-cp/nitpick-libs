---
name: new-repo
description: Create and set up a new Nitpick ecosystem repository end to end — the gitignore, the directory tree with a README per directory, the manifest, CLAUDE.md and CONTRIBUTING.md, the registry entry, and the GitHub remote with its description and topics. Use when starting a new library under nitpick-libs or a new application under nitpick-apps.
argument-hint: "[repo-name]"
allowed-tools: Bash(git *) Bash(gh *) Bash(mkdir *) Bash(python3 *) Read Write Edit Glob
---

# Setting up a repository

**A repository is not finished at `git init`.** The complete unit is: the local
scaffold and a first commit, the GitHub repository created under
`alternative-intelligence-cp` and pushed, and a description and topics set. Do
all three in one pass. **Repository creation is never delegated** (W-26): the
orchestrator or the author runs this skill, because it is outward-facing and
it edits the registry.

## 1. Claim the names first

In the same commit that starts the work, add a row to `LIBRARIES.md` (a
library) or `APPS.md` (an application) claiming:

- the **package name** — the ecosystem's `n`-prefix convention: `ntui`,
  `nparse`, `nregex`, `nsockets`, `ntime`
- the **decision prefix** — two letters, distinct from every other, and not
  colliding with the single letters used as *rule* prefixes inside
  specification documents, nor with `D-` (the compiler's, permanently)

## 2. The scaffold

```
src/            the source; a README per subdirectory naming what lives there,
                which specification governs it, and which cycle builds it
tests/          probe, conformance, unit, fixtures, plus this project's own
                oracle stage — named for the property it checks, not for
                another project's "golden"
harness/        the Python build and test runner, until npkg can
tools/          generators; everything they emit is committed and
                regeneration-checked
examples/       built AND run by the harness, so a broken example is a red run
docs/           written at 1.0
meta/           specs/, DECISIONS.md, OPEN_QUESTIONS.md, roadmap/, research/
                (with CURRENCY.md — skills/research/SKILL.md §7), scratch/
```

**`.gitignore`** — build output, `*.o`, `*.ll` (negating any committed
fixture), `__pycache__`, `*.log`, generator inputs that are large and
reproducible, editor residue, `.internal`, `.claude/settings.local.json`. Plus
an explicit **"NOT ignored, deliberately"** block naming the generated tables
and fixtures with the reason for each.

> **In a workbench repository the ignore is `/*/`**, which ignores every
> top-level directory *including dot-directories*. Anything the workbench
> itself owns must be un-ignored by name or it vanishes silently.

**`nitpick.toml`** — the compiler's schema exactly: `[project]` with `target`,
`[build]`, `[toolchain]` pinned to the exact patch release with the four flag
lists, an **empty** `[dependencies]`, and a `[[test]]` table that starts empty
with a comment saying each cycle adds its own. An entry naming an empty
directory is a suite that reports green while checking nothing.

**`CLAUDE.md`** — the read order, the non-negotiables, and a pointer to the
board (`../BOARD.md` from a library, `../../nitpick-libs/BOARD.md` from an
app). **Count the levels**: `CLAUDE.md` sits at the repository root.

## 3. GitHub, in the same pass

```bash
gh repo create alternative-intelligence-cp/<name> --public --source=. \
  --remote=origin --push --description "<what it is, in one sentence>"
gh repo edit alternative-intelligence-cp/<name> --add-topic … (up to 20)
```

Topics are for **discoverability**, not decoration: the domain terms somebody
with this problem would actually search, plus the ecosystem set (`nitpick`,
`nitpick-lang`, `safety-critical`, `zero-dependency`, `formal-verification`)
so the family is findable together.

**Scan before pushing.** These repositories are public:

```bash
python3 ${CLAUDE_SKILL_DIR}/../check/scripts/check_refs.py .
```

which reports any absolute home path or credential in a tracked file.

## 4. Then plan, before any code

The order is specs → decisions → open questions → cycle map → cycle 0.0
execution-grade → code. `../PLAYBOOK.md` §1 is the full statement, and §12 is
what a finished plan looks like.

**Cycle 0.0 is always the language probes**, because *a construct that parses
is not a construct that works* — and a probe that fails changes the design,
which costs a day now and a cycle later.
