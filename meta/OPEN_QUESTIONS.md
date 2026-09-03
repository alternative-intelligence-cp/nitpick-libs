# Open questions — the workbench

Questions about the orchestrator and worker system itself. `Q-` is a question
for the author; `O-N` is a gap in the compiler or its tooling. A question that
gets answered is struck through with the decision that answered it, never
deleted.

## For the author

- **Q-1 — which POSIX edition does `nitpick-posix` target?** Every document in
  that repository names POSIX.1-2017 as "the standard" and none mentions the
  2024 edition (IEEE 1003.1-2024, Issue 8), published two years ago. Found
  incidentally while reviewing the research question, not by a plan review.
  *Recommendation:* run the research skill's currency check on it as the
  first real research item (cycle 0.2's dry run can carry it), and let the
  digest drive a decision in that repository — this workbench does not decide
  it. Settled by: a `PX-` decision.
- **Q-2 — is a symlink acceptable for loading the plugin without the flag?**
  The documented skills-directory mechanism wants the plugin under
  `~/.claude/skills/<name>/`; a symlink from there to this checkout is the
  cheapest way to keep one copy. It is one command outside this repository,
  so it is the author's to run. *Recommendation:* yes, try it first;
  [`roadmap/0.2/0.2.6.md`](roadmap/0.2/0.2.6.md) says how to tell whether it
  worked.
- **Q-3 — should the sandbox's `filesystem.denyWrite` cover the compiler
  tree?** The guard classifies command text and cannot see an interpreter
  heredoc that writes; the sandbox can. Enabling the sandbox is a larger
  change with its own costs. *Recommendation:* not in cycle 0.2; revisit
  after the first width-3 window, when the evidence says whether the guard's
  limit was ever reached.
- **Q-4 — the default width.** Cycle 0.2 makes width an argument with a
  default of one. *Recommendation:* keep one as the default and pass a
  larger width explicitly per session, so the wide case is always a choice.

## For the compiler — the registry

`O-N` numbering is **per repository**, and the numbers collide: `O-N2` is the
`npkg` gap in `nitpick-tui`, `nitpick-sockets` and `nitpick-posix`, and three
different things in the other three repositories. The workbench refers to
compiler requests by one id each, so this section is the registry: an item is
defined here under the id of the repository that first raised it, with every
repository's local id beside it. A new ecosystem-wide request takes the next
free number here, from `O-N8` on. Found by `check_refs.py` the moment this
file existed — the check works.

- **O-N1 — `clone_exec` has no signal-mask slot.** Raised by `nitpick-tui`
  (its O-N1). Bites `ntui` 0.1.6 only, and it has a working answer already.
- **O-N2 — `npkg` cannot build a library, and `[dependencies]` resolves to
  nothing.** Raised by every repository: `nitpick-tui` O-N2, `nitpick-sockets`
  O-N2, `nitpick-posix` O-N2, `nitpick-time` O-N1, `nitpick-parse` O-N1,
  `nitpick-regex` O-N3. Blocks nothing — the Python harness is the plan — and
  has a long lead time. Not on the compiler's 1.5 or 1.6 map.
- **O-N5 — `npkg` cannot build more than one artifact.** Raised by
  `nitpick-posix` (its O-N5). Blocks nothing; the harness does it.
- ~~**O-N6 — a macro can splice a `pick` into a function body.**~~ —
  **ANSWERED 2026-09-03, negatively**, by `nitpick-posix` probe 02: a macro is
  invocable only in the module that declares it (`NITPICK-MACRO-007`), and
  `failsafe` is generated instead (PX-100). Kept struck, as the record of how
  the answer was reached.
