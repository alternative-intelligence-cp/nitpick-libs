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

## Library questions this board cites — the second registry, and why it exists

**A library-local question id has no meaning at workbench scope, and citing one
here is how a reader is silently misled.** The section below says `O-N` numbers
collide; **so do the letters.** Measured 2026-09-06 across all six work
repositories rather than assumed:

```
O-X1   nitpick-regex, nitpick-time, nitpick-tui               THREE different questions
O-X2   nitpick-time, nitpick-tui                              two
O-B1   nitpick-regex, nitpick-sockets, nitpick-time,          FIVE
       nitpick-tui, nitpick-posix
```

*(That evidence is fenced deliberately, and the reason is this section's own
rule biting its author within a minute of being written: naming those ids in
prose **cites** them, and citing a colliding id is the exact thing forbidden
here. `check_refs` reported all three immediately. Measured output belongs in a
fence — `prose()` strips fences precisely so quoted evidence is not read as a
citation, and `test_check_refs.py`'s `fenced-id` control exists to keep that
true.)*

So `BOARD.md` and `RECORD.md` may cite a library question **only through an
entry here**, which names the repository. Anything else resolves to whichever
repository the reader happens to open.

**This section exists because the seventh orchestrator cited a bare `O-X8` on
the board, `check_refs` reported `undefined-question`, and the orchestrator was
one step from "fixing" the check to resolve library ids against sibling
repositories — which, for the first id in the table above, would have silently
resolved to the wrong question in two repositories out of three.** What stopped
it was measuring the collision premise instead of accepting the convention's
word for it. **A check
that reports a false positive invites being weakened, and the weakening looks
like a fix right up until you count.**

- **O-X8 — `nitpick-time`: how does a refusing constructor hand back its
  `ValueFault`?** Raised by `nitpick-time` 0.1.0, 2026-09-06, at pin `aaffb87`;
  defined in full at
  [`nitpick-time/meta/OPEN_QUESTIONS.md`](../nitpick-time/meta/OPEN_QUESTIONS.md)
  §`O-x — ours`. **NOT blocking**, and deliberately left open: every candidate
  adds a public name and TM-013 makes a public name a MAJOR-version commitment.
  The recommendation is a `never fails` companion classifier
  (`civil_date_fault(y, m, d) -> ValueFault`) with the constructor written over
  it so the rules live in one place; it needs an **eleventh `ValueFault` variant
  meaning "no fault"**, which amends `SAFETY.md` S-3's enum and is the
  substantive half of the decision. **Settle it when `src/fmt/`'s parser at 0.4
  gives it a real call site** — a name chosen without a caller is a name chosen
  blind.

  **It generalises past `nitpick-time`.** An `error:` identity cannot carry a
  payload anywhere in this language, so **every library here faces the same
  question** and none of the other four has been asked it yet. See the board's
  SHARED FINDINGS block.

---

## For the compiler — the registry

`O-N` numbering is **per repository**, and the numbers collide: `O-N2` is the
`npkg` gap in `nitpick-tui`, `nitpick-sockets` and `nitpick-posix`, and three
different things in the other three repositories. The workbench refers to
compiler requests by one id each, so this section is the registry: an item is
defined here under the id of the repository that first raised it, with every
repository's local id beside it. A new ecosystem-wide request takes the next
free number here, from `O-N8` on. Found by `check_refs.py` the moment this
file existed — the check works.

- **O-N19 — `NITPICK-TYPE-046` IS NOT ENFORCED INSIDE A GENERIC FUNCTION BODY,
  SO A BARE COPY OF AN OWNING ELEMENT COMPILES, LINKS, RUNS, AND LEAVES TWO
  OWNERS OF ONE HEAP BODY. THIS IS A USE-AFTER-FREE THAT EXITS 0.** Raised by
  `nitpick-time` 0.0.5, 2026-09-05, at pin `aaffb87`; **reproduced by the
  orchestrator before it was sent, end to end.** `T:answer = s[i]` at an owning
  `T` inside a generic function is **accepted** (`npkc` 0, `.ll` written); the
  identical statement with `string` written out is **refused** at
  `NITPICK-TYPE-046`. The case that drops the first owner and reads the second
  compiles, links, and **runs to exit 170 — the allocator's `0xAA` poison.**

  **The controls isolate it to the type parameter and nothing else:**
  `case2_concrete_bare_copy` (the type written out) → `npkc` **1**,
  `NITPICK-TYPE-046`, no `.ll`; `case1_generic_bare_copy` (the same statement at
  an owning `T`) → `npkc` **0**; `case3_generic_scalar` (generic, scalar `T`) →
  `npkc` 0, which is correct because scalars copy. **So the rule exists, is
  right, and is simply not asked of an unsubstituted type parameter.**

  **Mechanism, read at the pin rather than guessed:**
  `require_move_if_owning` (`src/frontend/type_expr.npk:404` at `0880771`)
  returns early unless `type_drops` is true, **which it is not of an
  unsubstituted `T`.**

  **Not a regression — reproduced at ALL FOUR pins this workbench has used**
  (`aaffb87`, `0dfddac`, `950bb1d`, `94874ce`). What changed is only that
  O-N17's fix made the consequence **runnable**: before it, the same program
  stopped at `llc`, so the hole was readable off the IR and never executed.

  **Impact (W-27). Blocks nothing here today** — `ntime` instantiates no owning
  `T` by design. **But it silently un-guards every generic container in the
  ecosystem, and the failure mode is a use-after-free rather than a leak**,
  which is the reason it is registered at once rather than carried. **A leak is
  found by a gate; this is found by a wrong answer.**

  **AND THIS LIBRARY SHIPPED IT.** `src/core/vec.npk`'s `vec_pop<T>` at 0.0.4
  was the defect's own `case1` function verbatim — **written, reviewed,
  verified PASS by an independent verifier, and committed**, because the
  compiler accepted it and every gate the repository owns is a leak gate.
  Fixed at 0.0.5, which now writes `move(s[…])` — the correct spelling of a pop
  at any `T`, costing nothing at a scalar, **so that is this library fixing its
  own bug and not routing around the compiler's.**

  Reproduction: `nitpick-time/tests/probe/defect/generic_owning_copy/` — five
  cases and a transcript across four pins. **The worker deliberately left it
  unnumbered and cited it by path**, which is the rule written after the
  `O-N12` collision, applied correctly the first time it mattered.

- **O-N18 — `.len` on a fixed-size array `T[N]` is accepted by the frontend and
  cannot be lowered by the emitter.** Raised by `nitpick-time` 0.0.4,
  2026-09-05, at pin `0dfddac`, writing `put_uint`'s allocation-free digit
  buffer; **reproduced by the orchestrator before it was sent.** `npkc` exits
  **1** and writes no `.ll`, with **`NITPICK-EMIT-002`** — whose own text says
  *"a defect in the compiler rather than in this program — report it with the
  construct at this position"*, **so the compiler is explicitly asking to be
  told**, which is the whole reason this is registered rather than absorbed.

  **Two controls place it at `.len` on the array TYPE, not at arrays:** a
  **slice** `uint8[]` asking `.len` compiles and writes; a local `uint8[20]`
  **indexed without `.len`** compiles and writes. It refuses at both storage
  classes — a local `uint8[20]` and a module `fixed uint8[3]`.

  **Impact (W-27). Blocks nothing.** `src/core/bytes.npk`'s digit buffer is a
  `uint8[20]` that never asks its length: the bound is `NTIME_DIGITS_MAX`, a
  named constant in `src/core/limits.npk`, which is what a reader should see
  anyway — so naming the bound is better style regardless and the workaround is
  not one. **Inconveniences** any code that would rather ask an array its
  length than name the constant. **Does not touch** correctness of anything
  that compiles.

  Reproduction: `nitpick-time/tests/probe/defect/fixed_array_len/`. **Stated
  gap, not closed:** its two controls are recorded *as comments inside*
  `case1_local_array_len.npk` with their exit statuses, **not as compilable
  files** — unlike `generic_element_move/`, which ships five real cases in the
  same commit. The results are true (re-run here), but a later session cannot
  re-execute a control that is a comment. **That is the `nitpick-regex` 0.0.3
  shape — a document describing evidence rather than holding it — and it is
  owed at this repository's next claim.**

- **O-N17 — a generic function that moves OUT of an indexed element at an
  owning `T` calls a `@npk.vacant.<n>` helper the emitter never defines.**
  Raised by `nitpick-time` 0.0.4, 2026-09-05, against the pinned `0dfddac`, and
  **reproduced by the orchestrator before it was sent upstream.** `npkc` exits
  **0** and writes the `.ll`; `llc` exits **1** and writes no object, on
  `use of undefined value '@npk.vacant.1876'`. **Same shape as O-N14** — a call
  emitted against a symbol nothing declares — **and a different symbol, so the
  1.5.1b step 3c fix does not cover it.**

  **Three controls place the fault at exactly one combination — generic,
  owning, move-OUT — and no two of them:** a concrete move-out links, a generic
  move-out at a *scalar* `T` links, and a generic move-*in* at an owning `T`
  links. **The actionable half is a count rather than the error text.** All
  four cases **define the same five** `npk.vacant.*` helpers, so the definition
  pass is working; the three controls each **call three** of those five, while
  the failing case **calls four** and the fourth callee is not among them. The
  call site synthesises a `dty` the definition walk never visits, which points
  at the demand walk rather than at the helper-writing code.

  **Impact (W-27) — CORRECTED 2026-09-05, AND THE FIRST STATEMENT OF IT WAS
  WRONG IN THE DIRECTION THAT MATTERS. Blocks FIVE rows of `Vec<T>`, not one.**
  This entry, this board and the message that raised it upstream all first said
  *"one row — `vec_pop<T>`"*. **The primitive is `T:x = move(v.items[i])` in a
  generic function at an owning `T`**, and `vec_pop`, `vec_set`, `vec_clear`,
  `vec_truncate` and `vec_free` are all built on it — **a loop is a different
  caller, not a different primitive**, which is what the first reading missed.
  Measured with a non-owning control from the same source per case: four owning
  shapes give `npkc` 0 / `llc` 1 / no object, four scalar controls link and run
  at exit 0. **The orchestrator confirmed the generalisation directly on
  `case5_generic_drop_loop`** — a drop loop rather than a pop — `npkc` 0,
  `llc` 1, no object.

  **Why understating it was the dangerous direction, and this is the reason to
  read this paragraph twice:** *"one row"* is precisely what would have
  justified shipping a generic `vec_clear<T>` that **silently does not drop** —
  and that passes the `exit 0` leak gate, because D-151 counts `wild` blocks
  and cannot see a managed body. An extent understated by four rows would have
  been discharged by a green suite. **A defect's EXTENT is a separate
  measurement from its existence**, and only the first was taken before it was
  raised.

  **Does not block** the rest of that library:
  `ntime` plans no `Vec<T>` at an owning `T`, its `Layout` vector being a
  payload-free enum but for `Literal(uint16)` and its zone tables holding
  offsets into a name pool precisely so no row owns anything. **Does not touch**
  the correctness of anything that links. **`vec_pop<T>` is HELD, not written
  another way** — returning `NIL`, or restricting it to a scalar `T`, would be
  a workaround buried in library code that outlives the bug and later reads as
  a design choice nobody would question (W-11).

  **Why it stayed latent, which is the part worth keeping.** The prelude's
  `List<T>` has exactly **three** public functions at this pin — `list_init`,
  `list_reserve`, `list_push`; no `list_pop`, `list_at`, `list_set` or
  `list_free` — so **every move out of an element in the compiler's own tree is
  in a concrete function**, which is precisely the passing control. `BUILD.md`
  B-12 adopts this shape because it *"has been exercised across twenty-two
  families"*, and that sentence is **true of the half those families used**.
  It is not wrong; it is narrower than it reads — the same shape `PLAYBOOK.md`
  records for D-070's *"indexing is bounds-checked"*. **Two of this
  repository's findings now have that form, and both were found by writing the
  unexercised half.**

  **Numbering, recorded because it is the hazard this very section exists
  for:** the worker filed this as `O-N12`, which is already `nitpick-regex`'s
  settled `>>>`/`string_repeat` question. The registry ran O-N1…O-N16, so the
  free number was **O-N17**, assigned here by the orchestrator and corrected at
  the seven citations the worker had written. **A number taken from memory
  rather than from this file collides**, and the paragraph above says so in
  terms — awareness is not immunity.

  Reproduction, every command with its exit status beside the artefact it
  should have produced, and the four files:
  `nitpick-time/tests/probe/defect/generic_element_move/`. **Raised to
  `nitpick-compiler_s0` 2026-09-05** under the lifted constraint, explicitly
  as a catalogue-quality report rather than an interrupt to their 1.5.2d.

- **O-N16 — DEF-8's landing note states a premise about this workbench that is
  false, and reaches the right conclusion by the wrong route.** Raised by
  `nitpick-regex` 0.0.3, 2026-09-04, against the pinned `94874ce`; its local id
  is also `O-N16`. ~~**CATALOGUED, NOT RAISED**~~ — **the catalogue-don't-raise
  constraint was LIFTED by the author on 2026-09-05 ("raise as found"), and
  O-N16 itself is the evidence that cataloguing bought nothing: the compiler
  session closed it upstream the same day it was catalogued.** New defects go
  to that session as they are found, with their measurements and with W-27's
  statement of what they block. The original reason recorded here — the
  compiler session was near its usage limit and its fix batch was closing — had
  expired. **This is a defect in a NOTE, not in
  the compiler**, and it is registered because the note is a reason a later
  reader would rely on. The compiler's `meta/roadmap/OPEN_DECISIONS.md` closes
  DEF-8 with *"Blocks nothing of the workbench's: their recipes pass values, not
  fields, out of owning locals."* **The premise is false.**
  `nitpick-regex/tests/probe/probe04_inherent_generic_impl.npk` has
  `func:len2 = int64(Vec<T>:self) never fails { pass self.count; }` — a `pass` of
  a **field**, out of a by-value local — and `probe08_sparse_set.npk`'s
  `sset_has` takes a `SparseSet` by value and reads through two nested `Vec`s.
  **The conclusion nevertheless holds, for a reason the note does not give:**
  DEF-8 clears the drop flag of an *owning* local, and by RX-126 a library's
  hand-written `Vec<T>` never owns — `decl_is_list` matches only a struct named
  exactly `List`, homed in the compiler's `list` scope, with fields `items`
  (pointer), `count`, `cap`. So the workbench is untouched because its
  containers are outside D-247's recognition, **not** because it does not write
  the shape. **W-27: blocks nothing, inconveniences nobody, and touches no
  schedule.** Its cost is entirely to a future reader: anyone checking their own
  exposure against the stated reason would check the wrong property, and the
  three probes re-running clean would confirm them in it. *Recommendation:*
  correct the note's reason rather than its verdict, and fold it into whatever
  batch reopens — it is one sentence and needs no code.
- **O-N15 — `npkg` accepts an `expect-exit:` above 255, which no run can
  satisfy.** Raised by `nitpick-regex` 0.0.2, 2026-09-04, against the pinned
  `950bb1d`. `expect_read` accepts the value and `run_binary` then compares it
  against a one-byte process status, so the test fails forever with a message
  that is true and useless. **W-27: blocks nothing, inconveniences nobody
  today** — swept, and nothing in this ecosystem expects an exit above 255 —
  and touches no schedule. *Recommendation:* file it at low priority. This
  repository's own `harness/expect.py` already refuses such a value (RX-122),
  so nothing here waits on it, and the same guard is the right shape for every
  library harness. **INDEPENDENTLY VERIFIED 2026-09-04** from the compiler's source at the pin: `expect_read`'s `expect-exit:` handling checks only `text_int`'s `is_error` with no upper bound, and `run_binary` compares the OS-truncated one-byte status against that unbounded value with `!=`. Sent to the compiler session.
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
