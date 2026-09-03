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
- ~~**Q-2 — is a symlink acceptable for loading the plugin without the flag?**~~
  — **ANSWERED 2026-09-03, yes.** The author ran
  `ln -s ~/Workspace/REPOS/nitpick-libs ~/.claude/skills/npk` and a fresh
  session started in the workbench without `--plugin-dir` offered and ran
  `/npk:check`. One copy, no flag; the alias is now the fallback note.
  [`roadmap/0.2/0.2.6.md`](roadmap/0.2/0.2.6.md) §5's fallback was not needed.
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
- **O-N4 — `npkc` is quadratic in the size of one declaration.** Raised by
  `nitpick-time` (its O-N4), which is also the local id, so this section keeps
  it. Three independent axes — array-initialiser elements, function-body
  statements, string-literal bytes — with the string axis flat in memory and
  therefore a separate pathology. TM-007's 26 838-row tzdb costs 281 s and
  30.9 GiB, so the library is unbuildable in its shipping shape on a 16 GiB
  machine or in CI. **Blocks `nitpick-time` 0.0.5 and 0.5 only**; 0.0.1–0.0.4
  carry no large declaration. Reproduction committed at `nitpick-time`
  `8066e62`, `tests/probe/defect/`. **ACCEPTED by the compiler session
  2026-09-03** as its **DEF-1**, owned, and independently reproduced there on
  a different build; a subcycle 1.5.1b is proposed and the schedule is the
  author's. Re-pin the workbench toolchain when it lands.
- ~~**O-N7 — never existed; a misnumber by the orchestrator on
  2026-09-03.**~~ The resolver defect above was numbered `O-N7` on the board and
  in the playbook before this section's own rule was read: a new
  ecosystem-wide request takes the next free number **from O-N8 on**. The live
  documents were renumbered to **O-N8** within the hour; `RECORD.md` still
  says `O-N7` in the entries written before the correction, because it is
  append-only and is never rewritten. That is why this line exists — so the
  reference resolves and the mistake stays visible. `check_refs.py` caught it,
  which is the second time this file's existence has paid for itself.
- **O-N9 — D-004's escape rule is enforced for `@`-borrows and not for slice
  views.** Raised by `nitpick-time` 0.0.0 while mapping probes 09 and 10's
  borrow edges. `string_bytes` on a local `string` yields a `uint8[]` that can
  be **returned out of its owning frame with no diagnostic**, and reading it
  afterwards reads freed memory — measured, the caller gets something other
  than the byte it wrote. The same position with an explicit borrow *is*
  caught: returning `@x` is `NITPICK-BORROW-001`, "a borrow cannot travel up …
  (D-004 rule 2)", and so is a struct literal holding `@local`. So the rule
  exists, is documented, and is under-enforced for one type; D-186's inventory
  of view-makers names `string_from_bytes` as "the one remaining view-maker"
  without accounting for this direction. Bites `nitpick-time` broadly in
  principle — every parser in `src/fmt/` takes a `uint8[]` — but **is not
  O-N4-style blocking**, because obeying "a view is a parameter, never a
  return value" is conformance with a documented language rule rather than a
  workaround for a defect. Disposition is Q-5.
- **O-N8 — `npkc` silently merges two files when a `mod:` name mismatches its
  basename.** Raised by `nitpick-time` 0.0.0 alongside O-N4, but never given a
  local id there, so it is a new ecosystem-wide request and takes the next
  free number under this section's own rule. When a root file's `mod:` differs
  from its basename **and a sibling carries that basename**, `npkc` compiles
  the sibling too, merges both into one module, emits two `define i32 @main`,
  and exits 0; `llc` then refuses the IR. Without the sibling the
  `NITPICK-RESOLVE-005` diagnostic is exemplary, so the rule is known and
  merely not applied here. Blocks nothing and costs `nitpick-time` nothing.
  **ACCEPTED 2026-09-03** as the compiler's **DEF-2**, same owner and slot.
- ~~**O-N6 — a macro can splice a `pick` into a function body.**~~ —
  **ANSWERED 2026-09-03, negatively**, by `nitpick-posix` probe 02: a macro is
  invocable only in the module that declares it (`NITPICK-MACRO-007`), and
  `failsafe` is generated instead (PX-100). Kept struck, as the record of how
  the answer was reached.
