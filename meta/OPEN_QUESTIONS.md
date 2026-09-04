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

*The four below were raised by the first orchestrator session on 2026-09-03,
during cycle 0.2's dry run one. **They were first numbered Q-2, Q-3, Q-4 and
Q-5 on the board, which collided with Q-2, Q-3 and Q-4 above** — the
orchestrator numbered from an empty questions table rather than from this
registry. `check_refs.py` did not catch it, because a re-used number resolves:
the check finds a question referenced and never defined, not one defined
twice. That gap is itself a finding. The live documents use the numbers below;
`RECORD.md` keeps the wrong ones in the entries written before the correction,
because it is append-only.*

- ~~**Q-5 — should O-N4 be raised against the compiler?**~~ — **ANSWERED
  2026-09-03, yes**, by W-11 and the author: raised with the compiler session
  the same hour, accepted as its DEF-1, and never worked around. Numbered
  `Q-2` on the board when raised.
- ~~**Q-6 — work `nitpick-time`'s nine O-N4-unaffected probes, or idle the
  stream?**~~ — **ANSWERED 2026-09-03: work the nine**, at width one, against
  the current pin; only probe 04's cost waits on the re-pin. Numbered `Q-3`
  on the board when raised.
- ~~**Q-7 — should O-N8's narrow resolver defect be raised alongside
  O-N4?**~~ — **ANSWERED 2026-09-03, yes**, blocking nothing; accepted as the
  compiler's DEF-2 and scheduled first in 1.5.1b because it is independent.
  Numbered `Q-4` on the board when raised.
- ~~**Q-8 — does O-N9 block `nitpick-time` the way O-N4 does?**~~ —
  **ANSWERED 2026-09-03: yes, blocking**, by the author and **against the
  orchestrator's recommendation**, which read it as conformance rather than a
  block. The author's ground: a rule enforced only by a harness check the
  library writes for itself is a thin guarantee for a use-after-free and
  protects no consumer. The `SAFETY.md` rule and `check_no_view_returns` are
  kept as a belt rather than as the guarantee. Numbered `Q-5` on the board
  when raised.

*Raised by the second orchestrator session (`nitpick-libs-88`) on 2026-09-03,
numbered from this registry rather than from the board — which is the error the
note above records.*

- ~~**Q-9 — should this workbench stop hedging when it escalates a defect?**~~ — **ANSWERED 2026-09-03: yes, state what it blocks.** The author confirmed the compiler side's rule and it is now **W-27** in `WORKSTREAMS.md`: an escalation says what is blocked, what is inconvenienced and what is unaffected, and drops "no schedule pressure implied", which reads as modesty and is a withheld fact. Sequencing stays the author's. Original text: The
  compiler session reports an author rule on its side that **a defect a real
  program finds is fixed before planned work**, which is why O-N10 became a
  step in 1.5.1b rather than a backlog row. Every escalation this workbench sent
  on 2026-09-03 was framed "no schedule pressure implied" — under that rule,
  more deferential than the author actually wants, and the hedge costs
  information: it hides which defects are blocking. **Heard second-hand from
  the compiler session, never from the author**, which is why it is a question
  and not a practice. *Recommendation:* confirm the rule, and let the workbench
  state plainly what a defect blocks and what it does not, leaving the schedule
  to the author. Settled by: the author, and a line in `WORKSTREAMS.md` beside
  W-11 and W-23.
- ~~**Q-10 — does `nitpick-time` 0.0.3 gain a cost-and-heap harness stage?**~~ — **ANSWERED 2026-09-03: yes, both, and sweep every repository for the gate.** 0.0.3 gains the cost-and-heap stage and 0.0.4's gate becomes a `peak_live` assertion, both when the re-pin lands; and the read-only sweep for the same unfalsifiable gate ran immediately — **it is in all five repositories**, see `RECORD.md`. Each repository's fix waits for its own stream's claim (W-7). Original text: The
  compiler's 1.5.1b step 0 builds an `NPK_HEAP_STATS` instrument and a `cost`
  harness stage measuring compile time and peak RSS per test. This library's
  stage list (`parse`, `accept`, `check`, `golden`, `sweep`, `program`, `repro`)
  has neither, and **O-N4 was found by accident** because one probe happened to
  be enormous — a monitored budget would have caught it as a property. The same
  stage would carry `NPK_HEAP_STATS`, which is the only instrument that can
  express 0.0.4's leak gate: that gate currently reads "the suite's programs
  exit 0, so a missing `free` on any path is a trap", and **as written it cannot
  fail**, because D-151 watches `wild` allocations and a managed `string` body
  is invisible to it. The compiler measured our own probe pair at peak_live
  41 321 against 400 101 320 bytes, both exiting 0. *Recommendation:* yes, and
  fold 0.0.4's gate rewrite into the same amendment — but it adds a stage to an
  execution-grade checklist and amends another cycle's gate, so it is a plan
  change the orchestrator does not make (W-16). Nothing is blocked meanwhile:
  neither can be built until the re-pin lands. Settled by: the author, then a
  worker amending `0.0.3.md` and `0.0.4.md`.

## For the compiler — the registry

`O-N` numbering is **per repository**, and the numbers collide: `O-N2` is the
`npkg` gap in `nitpick-tui`, `nitpick-sockets` and `nitpick-posix`, and three
different things in the other three repositories. The workbench refers to
compiler requests by one id each, so this section is the registry: an item is
defined here under the id of the repository that first raised it, with every
repository's local id beside it. A new ecosystem-wide request takes the next
free number here, from `O-N8` on. Found by `check_refs.py` the moment this
file existed — the check works.

- **O-N14 — there is no library object: `npkc` emits calls to `@npk_failsafe`
  and never a `declare`.** Raised by `nitpick-regex` 0.0.1, 2026-09-03, against
  the pinned `950bb1d`. Any translation unit that is not a program root compiles
  at `npkc` exit 0 and is then refused by `llc` for an undefined
  `@npk_failsafe`. **Confirmed at the emitter by this orchestrator**: the symbol
  is emitted as a `call` from `ir_func.npk` and `ir_stmt.npk` (three sites) and
  no `declare` for it exists anywhere in `src/backend/ir/`. **This is every
  library in this ecosystem, not one** — a library reaches the compiler only by
  being imported from a program root, and `BUILD_REFERENCE` §4.1's "each module
  compiles to its own object" is not achievable at this pin. **W-27: it BLOCKS**
  a per-module object, a `libnregex.o`, and separate compilation as documented;
  it **INCONVENIENCES** cycle 0.0.2's harness, which builds through a program
  root instead, and RX-008's symbol scan, which becomes differential; it
  **TOUCHES** nothing else — no rule, no API, no layering, and nothing was
  reshaped to dodge it. **Close kin to O-N11/DEF-5, and cheap:** one emitted
  `declare i32 @npk_failsafe(i32)` closes it outright and strengthens DEF-5's
  own case, since both are about a root's obligation to supply that symbol.
  Reproduction: `nitpick-regex/tests/conformance/TRANSCRIPT.txt` §A. Under
  verification at the time of writing.
- **O-N13 — a `pub use` is SILENTLY downgraded to a plain `use`.** Raised by
  `nitpick-regex` 0.0.1, 2026-09-03. When the same path was plain-`use`d earlier
  in the same file, `symtab_bind_import` declines a name already bound and
  returns the prior binding **without merging `SYM_PUB`**, at no severity and
  with no diagnostic. The re-export silently does not happen; the failure
  surfaces in the *consumer* as "cannot find X in this scope", a file away from
  the cause. **The same two lines in the opposite order are correct.** **W-27:
  it BLOCKS nothing** — the working order exists; it **INCONVENIENCES** once and
  expensively for each person who meets it, because nothing points at the cause;
  it **TOUCHES** nothing that compiles. **Every library with an umbrella module
  is one redundant `use` away from it**, and this ecosystem has six umbrellas
  planned. Same family as O-N10's quiet half: the loud failure is an
  inconvenience and the silent wrong answer is the defect. Reproduction:
  `tests/conformance/TRANSCRIPT.txt` §E2 against §E3. Under verification.
- **O-N12 — `>>>` and `string_repeat` are documented in the compiler's
  references and absent from the compiler.** Raised by `nitpick-regex` 0.0.0,
  2026-09-03, against the pinned toolchain `950bb1d`. `>>>` does not parse;
  `string_repeat` is documented and not there. **Blocks nothing** (W-27): both
  have working substitutes, and the substitute for `>>>` is that **`>>` on an
  unsigned operand is already logical**, measured at bit 63 — so `>>>` would be
  a pure synonym if it existed. *Recommendation, and it is the unusual one:*
  **fix the documentation, not the implementation.** The harm here is not a
  missing feature, it is a reference that describes `>>` as `ashr` and `>>>` as
  `lshr`, so a reader reaches for the operator that does not exist — which is
  precisely what happened, and cost a probe. Adding `>>>` would make the
  documentation true at the cost of a redundant operator; deleting it makes the
  documentation true and the language smaller. Settled by: the compiler session.
  Under verification at the time of writing.
- **O-N11 — a program with `main` and no `failsafe` compiles at `npkc` exit 0,
  and the REACH-002 arm contract is discharged by deleting the handler.**
  Raised by `nitpick-time` 0.0.0 probe 11 (its local O-N5), 2026-09-03, against
  the pinned toolchain `950bb1d`. **The number is allocated; the finding is
  PROVISIONAL until the verifier answers**, and it has not been sent to the
  compiler session — nothing moves before the verifier, including a sentence.
  Two halves. The loud one: `npkc` accepts a root file declaring `main` and no
  `failsafe` at exit 0, emitting IR whose trap paths call an undefined
  `@npk_failsafe`, and only `llc` refuses it. The compiler's own D-013 requires
  exactly one `failsafe` per executable. The quiet one, and the serious one:
  `reach_settle` is reported to return early when `failsafe_decl == 0`, so the
  whole arm contract is enforced against programs that HAVE a handler and asked
  of nothing that has none. **W-27 status: blocks nothing here** — every program
  this library ships has a handler, and `llc` catches a missing one in the next
  step of the same recipe. It **inconveniences** cycle 0.0.3's harness, which
  must stop reading `npkc` exit 0 as "well-formed" and gains an eighth selfcheck
  case. It does **not** touch the arm contract where a handler exists, nor any
  other analysis, nor any measurement this cycle took. The ask includes the
  diagnostic naming the arms the absent handler would owe — `reach_settle` has
  just computed that set at the line where it returns early — and notes it is
  close kin to the compiler's own open item that D-014's injected
  `ensures result > 0` on `failsafe` and its non-empty-body check "both
  currently exist nowhere": one pass over the root's declarations answers all
  three. Reproduction:
  `nitpick-time/tests/probe/defect/missing_failsafe/` (three cases, a
  transcript, and a support-module control that rules out the
  library-versus-executable diagnosis).
- **O-N1 — `clone_exec` has no signal-mask slot.** Raised by `nitpick-tui`
  (its O-N1). Bites `ntui` 0.1.6 only, and it has a working answer already.
- **O-N2 — `npkg` cannot build a library, and `[dependencies]` resolves to
  nothing.** Raised by every repository: `nitpick-tui` O-N2, `nitpick-sockets`
  O-N2, `nitpick-posix` O-N2, `nitpick-time` O-N1, `nitpick-parse` O-N1,
  `nitpick-regex` **O-G3** (renumbered from its local `O-N3` at 0.0.1, so `O-N` there now means this registry alone). Blocks nothing — the Python harness is the plan — and
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
- **O-N10 — `#[derive(…)]` on a payload enum is refused one way and silently
  wrong the other.** Raised by `nitpick-time` 0.0.0's probe 05. `#[derive(Eq)]`
  on an enum with a payload does **not** compile — `NITPICK-TYPE-034`, reported
  inside `<derived-1>` — while `#[derive(Ord)]` on the same declaration
  compiles and produces a **tag-only** `cmp`, so `Literal(7).cmp(Literal(9))`
  is `Equal`. The loud half is an inconvenience; **the quiet half reports two
  different values as equal** and is the one to raise loudest. No file in the
  compiler's own tree derives anything on a payload enum, so the gap is
  coverage rather than a decision. **Not blocking `nitpick-time`** — one
  payload enum is exposed and no rule needs either derive on it — but it
  blocks the first library that wants one, and it should be raised with a
  request for a test in the compiler's tree.
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
