---
name: worker
description: Work one cycle or subcycle in a Nitpick ecosystem repository — the claim check, the read order, the cycle discipline, the verification, the commit format and the close checklist. Use when planning or implementing any cycle in nitpick-tui, nitpick-parse, nitpick-regex, nitpick-sockets, nitpick-time or nitpick-posix, or in any application repository.
argument-hint: "[repo] [cycle]"
allowed-tools: Bash(python3 *) Bash(git *) Read Write Edit Grep Glob
---

# Working a cycle

## 1. Before touching anything

- **Check the claim.** `../BOARD.md` (from a library) or
  `../../nitpick-libs/BOARD.md` (from an app) says whether this repository is
  claimed and by which stream. **One writer per repository, always.** If it is
  claimed by another stream, stop and say so.
- **The compiler at `REPOS/nitpick` is read-only.** It runs verification and
  parity passes measured in hours, and its own orchestration rules forbid
  editing a tree while a harness runs on it. Reading it is expected and
  encouraged; writing to it is not, ever.

## 2. Read, in this order

1. `../PLAYBOOK.md` — the language constraints and the house rules
2. this repository's `CLAUDE.md`
3. `meta/specs/SAFETY.md`, then the specification the cycle touches
4. `meta/DECISIONS.md` — **before proposing any change**, because it is
   recorded why
5. `meta/roadmap/<cycle>/README.md`, then the subcycle file

## 3. The discipline

- **One commit per subcycle**, under a green full run.
- **The specifications are the authority.** Code that disagrees is a defect in
  the code. A specification that is wrong is amended by a numbered decision **in
  the same commit** as the work that revealed it — never by editing the text and
  moving on, and never by a comment.
- **A settled decision is superseded, never rewritten.**
- **Never work around a compiler defect.** Record the reproduction, stop, and
  raise it. A workaround buried in library code outlives the bug and is
  indefensible at verification time.
- **Verify a claim about the language against the compiler's source**, not
  against a summary — including a summary in these documents. That discipline
  is what caught a false claim about signal disposition that had already
  shipped in a specification.
- **`--only` iterates; it never concludes.** Nothing is committed on the
  strength of a filtered run.

## 4. Before every commit

```bash
python3 ${CLAUDE_SKILL_DIR}/../check/scripts/check_refs.py .
```

or invoke `/npk:check`. A commit touching `meta/` with findings outstanding is
a commit that breaks somebody's link.

## 5. The commit message

Body explains **why**, not what — the diff says what. End with exactly:

```
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
Claude-Session: <the session URL from the harness notice>
```

## 6. Closing a cycle

Not done until all of:

- [ ] every checklist item in the cycle's `README.md` ticked, or explicitly
      struck with a reason
- [ ] the cycle's gate met — read it again rather than remembering it
- [ ] findings written into the subcycle's execution record. **These are
      load-bearing**: this ecosystem's cross-cycle patterns exist only because
      somebody kept them
- [ ] any decision the cycle settled recorded, and any question it answered
      struck through in `OPEN_QUESTIONS.md` **with its decision number, never
      deleted**
- [ ] the *next* cycle's opening subcycle file written execution-grade, by you,
      now — while you still know what this cycle taught
- [ ] `/npk:check` clean
- [ ] the cycle moved to `meta/roadmap/done/` and `ROADMAP.md` updated
- [ ] the orchestrator told, so the board can be released

## What will bite

`meta/specs/BUILD.md` §7 or the playbook §10 has the reserved words. The ones
that read most like ordinary names: `buffer`, `raw`, `move`, `end`, `in`,
`limit`, `any`, `on`, `error`, `fd`, `unit`, `thread`, `channel`. Adjacent
string literals do not concatenate; `discard(x);` takes parentheses and
`defer { … }` takes no trailing semicolon; declarations end `};` and
control-flow blocks do not; a file's `mod:` name must equal its basename.
