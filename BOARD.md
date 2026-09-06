# The board

**Live state.** What each stream is working on, what is claimed, what is
blocked, what is done. The durable plan is
[`WORKSTREAMS.md`](WORKSTREAMS.md); the past is [`RECORD.md`](RECORD.md).

> **The orchestrator owns this file** (W-8). An agent working a stream does not
> edit it — the orchestrator claims before a worker is dispatched and releases
> when the stream leaves the repository. That is what keeps two agents out of
> one repository and removes every merge conflict by construction.

**Last updated:** 2026-09-05 · **Width:** 1 — stream 2 only, confirmed by the author 2026-09-05 (question 4 answered; the dial turned down for quota, not a change of plan — `parallel-planning-serial-implementation`) ·
**Toolchain:** aaffb87 · .internal/toolchain/aaffb87/ · pinned 2026-09-05 22:47 · **tree clean, and the provenance CHECKED rather than inferred** — the 1.5.2d close. `build/npkc` was rebuilt from the pushed main checkout 22:41–22:45, so its mtime (22:45:33) is **500 s after** `HEAD`'s commit (22:37:13), which is §3's provenance test; the same test refused a binary in the morning. Verified here before copying, independently of the landing notice: **7 346 792 B**, sha256 `a3b0dadc…`, `sha256sum -c` OK, LLVM **20.1.2**, `0dfddac` is an ancestor of `aaffb87`. **`npkrt.o` is byte-identical to the 0dfddac pin's** (55 576 B, `c9ddbcff…`) — taken again and `cmp`-verified, not assumed (DEF-12's precedent). **`aaffb87` is docs-only over `0880771`, so the compiler SOURCE is `0880771`'s** — 1.5.2d step 4. **Commissioned before use, both directions:** the canary compiles at exit 0 writing a 50 560 B `.ll`; a malformed file exits 1 at `NITPICK-PARSE-001` writing none. **The mid-rebuild guard fired first and was right** — the binary was 97 s old and §3 said retry, which is the second re-pin running it has caught the orchestrator moving straight off a landing notice. Full provenance and 1.5.2d's five step commits are in `.internal/toolchain/aaffb87/PIN.md`'s `binary` line
**Workbench writer:** `00e68bc1-dc6d-4607-b8eb-72f7188a59c1` — session `nitpick-libs_s1`, the **sixth** orchestrator, took the lock 2026-09-05 at a briefed overlap with `nitpick-libs_s0`. **Freedom was verified THREE ways before taking it, not one:** this line read `none`, `.internal/` held only `toolchain/`, and the release commit `b992544` (16:17:22) was on `main` with all seven trees clean and level with origin. **To take it: this line first, then the marker; to release, marker first, then this line** — so an abrupt close cannot leave the lock naming a dead session. **Four hazards, each measured rather than inferred; the third was found at the 13:37 handover and the fourth at this one.** (1) The guard permits **any** session while this line reads `none`, so §2.1's refusal never fires and **its absence is not evidence the lock is free** — verify `.internal/` too. (2) **`CLAUDE_SESSION_ID` is EMPTY in a Bash tool call**, so §2.1's marker command writes a 0-byte file; take your id from the `~/.claude/projects/<slug>/<uuid>.jsonl` path, cross-check it against your scratchpad path, and expect **37 bytes**. (3) **A free lock is not the same as a clean tree.** At the 13:37 handover the incoming session asked the outgoing one *"are you done writing?"* instead of reading the `none` and taking it; the outgoing session nearly answered from memory, ran `git status`, and found an **uncommitted deletion it had not made** — the author had moved a tracked file out from under it. Committing on the "lock is free" reading would have swept another session's deletion into this one's commit. **During any handover overlap, ask the outgoing session directly and have it answer from `git status`, not from memory.** **Done again at this handover, and it paid again:** `nitpick-libs_s0` answered from `git status` — all seven trees `dirty=0`, `ahead/behind=0/0` — and volunteered that its remaining actions are **messages only**, which a tree read cannot tell you. (4) **A `nitpick-libs_sN` PEER YOU WERE NEVER TOLD ABOUT WILL APPEAR, AND ONE MESSAGE SETTLES IT.** At this takeover `ListAgents` showed **`nitpick-libs_s2`, idle, opened within a minute of this session**, while the handoff brief, the record and this board's own roster named only `s0` and `s1`. Orchestrate §2.1 says to stop and ask the author; **asking the peer itself is faster, cheaper and more certain** — it replied *idle, no task, nothing written, and I will message you before I write*, converting a guess into a fact in one message. That is the move the fourth orchestrator recommended for the unidentified `nitpick-e3` and did not take, leaving it open for two days. **The author's practice, confirmed by him at this handover, is a ROLLING POOL:** he pre-opens the next generation, and closes a spent session so it can return as the generation after next — `s0` closes here and comes back as `s3`, succeeding `s2`. **So a higher-numbered libs peer is normally your own parked successor, not a rival writer — but ask it anyway**, because the alternative is inference, which is exactly what two earlier orchestrators rightly refused to rest this lock on. One writer here (W-16, P-19).
**THE PEER SESSIONS, AND THEIR NAMES ARE NOW A CONVENTION RATHER THAN A
LABEL.** The author renamed every session on 2026-09-05 to `<project>_s<N>`,
where the project segment names the work area and `N` is the handoff
generation. Earlier boards and briefs warned that *"names are not durable,
`ListAgents` is the address book"* — true of the old machine-assigned labels
(`nitpick-bc`, `nitpick-36`, `nitpick-e3`), and now only half true: **the
project segment and the generation number are stable and worth reading.**
`ListAgents` remains the authority on who is *alive*, and the bracketed `[ref]`
is what disambiguates.

| Session | Was | Role |
|---|---|---|
| `nitpick-libs_s0` | `nitpick-libs-c6` | **this workbench's orchestrator — the current writer** |
| `nitpick-libs_s1` | — | this workbench's **successor**, open and idle, waiting for the handoff |
| `nitpick-compiler_s0` | `nitpick-bc` | the compiler session — **who to ask about `build/` and the pin** |
| `nitpick-compiler_s1` | `nitpick-e3` | the compiler's successor, open and idle |
| `claud-skills-devTeam_s0` / `_s1` | — | the `devteam` project pair, **idle to conserve quota** (note the project segment is spelled `claud-`, without the final `e`) |

**Two consequences worth acting on.** The unidentified idle peer the fourth
orchestrator declined to rest the lock on — `nitpick-e3` — is
`nitpick-compiler_s1`, the compiler's own waiting successor, confirmed by the
same `ListAgents` ref across the rename. It works another repository and will
not write here. And **an idle peer is parked on purpose, not stalled**: the
author is holding the `devteam` pair idle so the compiler and this workbench do
not run short of quota, so waking one has a cost he is actively managing.

**Phase:** cycle 0.2's dry run one is under way — `nitpick-time` 0.0 is the
first library cycle to be worked, and the loop is being judged against
[`meta/roadmap/0.2/0.2.7.md`](meta/roadmap/0.2/0.2.7.md) §2's pass mark.
*(This paragraph was accidentally deleted by the orchestrator's 13:40 edit — a
replacement span that ran to the next blank line and swallowed it — and restored
verbatim from `d91d0ca` at 14:10.)*

**~~THE RE-PIN IS DONE~~ — SUPERSEDED 2026-09-05 22:47 by the `aaffb87` re-pin above; kept because its four re-measurements are the before-values that one is measured against. Pinned `0dfddac` at 2026-09-05 15:58 — the 1.5.2c close —
and all four discharged stops were re-measured against it.** The morning's
question (*what is `build/npkc`, and is there a stable point to pin?*) was
settled by one message to `nitpick-compiler_s0` at 13:35 and the pin followed
its landing notice at 15:47. The working out is in `RECORD.md`; what a reader
needs now is below.

**The provenance test added to §3 this afternoon was exercised on both sides
within one day, which is what makes it commissioned rather than merely
written.** It **refused** the morning's binary as `tree unknown` — mtime
2026-09-04 19:42:54, seventeen hours *before* `HEAD` — and **passed** this one
as `tree clean`, mtime 15:56:34, nine minutes *after* `HEAD`'s 15:47:09. Every
number in the landing notice was verified here before copying rather than taken
on report; `94874ce` is an ancestor of `0dfddac`, so the pin moved forward.
`npkrt.o` is byte-identical to the previous pin's and was **taken again and
checked** rather than assumed. Full provenance, the three commits and their
harness numbers are in `.internal/toolchain/0dfddac/PIN.md`'s `binary` line.

**THE FOUR RE-MEASUREMENTS — the reason the pin was not taken this morning.**
All four were facts about `94874ce`; here is what they are against `0dfddac`.

| Stop | Verdict at the new pin |
|---|---|
| **O-N11** | **FIXED.** `case1_no_failsafe` and `case3_arm_contract_evaded` are now `npkc` **exit 1, `NITPICK-REACH-003`, no `.ll`** — where before it was `npkc` exit 0 and `llc` exit 1 on an undefined `@npk_failsafe`. `case2_failsafe_present` still exits 0 and emits. **THE IDENTITY COUNT IS PER PROGRAM, AND THIS BOARD'S "FOUR" WAS ONE CASE'S BILL ASSERTED OF ALL OF THEM. Corrected 2026-09-05 by the 0.0.1 worker and re-measured by the orchestrator directly before the board moved:** `case1` names **4** — `Unreachable, HeapOom, HeapBadRequest, WildLeak` — and `case3` names **6** — `probe11_arms_lib.EProbeZone, Unreachable, HeapOom, HeapBadRequest, WildLeak, IntOverflow`. **Both numbers were always real.** The earlier entry read *"the diagnostic says 4 identities — this board's correction against the six we were told is confirmed by the compiler's own output"*, which took one program's floor as the general answer and then cited the compiler's own mouth for it. **The board contained its own refutation:** checklist item 5 says `case1` has *"no import, no arithmetic and no allocation, so its bill is S-4b's floor of four"* — which is precisely why four is not `case3`'s number, `case3` importing `probe11_arms_lib` (hence `EProbeZone`) and doing arithmetic (hence `IntOverflow`). **A count that a diagnostic computes FROM THE PROGRAM cannot be corrected once for the set**, and "confirmed by the compiler's own output" is what made it feel settled. This is the after-value the two DEF-5 transcripts owe, and each records its own number |
| **O-N10** | **UNCHANGED.** All three `derive_payload_enum` cases behave identically on both pins through the full four-step recipe and match their `expect-exit` headers exactly (0, 121, 107). 1.5.2b's wholesale derive rewrite did **not** move it — which is precisely what had to be measured rather than assumed |
| **O-N9** | **UNCHANGED.** `probe10b` → `NITPICK-BORROW-012`, `probe10c` → `NITPICK-BORROW-001`, identical on both pins. `probe09b` exits 0 on both — *once its precondition is met; see below* |
| **O-N4** | **STILL DISCHARGED, BUT SLOWER.** `probe04` is **2.03–2.06 s at ~119 MB**, was **1.18 s at 74 624 KiB**. Against the original 281 s / 30.9 GiB it is still ~136× better, so nothing reopens |

**THE COMPILER GAINED A FIXED PER-PROGRAM COST, AND IT IS PAID BY PROGRAMS THAT
USE NONE OF THE NEW SURFACE. Measured differentially — both pinned compilers on
disk, same inputs, same machine.** A 14-line program that only does `exit 0i32`
with a `failsafe` (`probe11d_floor_only`):

| | `94874ce` | `0dfddac` | factor |
|---|---|---|---|
| wall | 0.10 s | **0.85 s** | **8.5×** |
| peak RSS | 21 456 KiB | **102 404 KiB** | **4.8×** |
| `.ll` emitted | 456 517 B | **845 282 B** | **+388 765 B** |

**The `.ll` delta is exactly 388 765 B for both the floor program and the
30 000-row one — identical to the byte**, so it is a fixed prelude increase and
not a compile-time regression. Widened across **30 programs** in two libraries
that compile clean under both: **22 of 30 sit at exactly 388 765**, and all 8
that differ are derive or enum programs, where 1.5.2b/1.5.2c genuinely changed
semantics. Almost certainly D-257's price — the prelude implementing the
derivable traits for every scalar. **Impact, W-27: blocks nothing; inconveniences
every harness run in this ecosystem**, because our libraries compile *many small
programs* per run so a fixed per-program cost multiplies by program count rather
than by size — `nitpick-regex` 0.0.3's harness was 63/63 in 37.5 s, and +0.75 s
per program roughly doubles it — and raises per-compile peak ~5×, which matters
if a harness compiles in parallel; **does not touch correctness.** **Raised to
`nitpick-compiler_s0` 2026-09-05**, under the lifted constraint, with no ask
attached beyond confirming whether the price was known.

**`probe09b_environ_view_returned` CANNOT PASS WITHOUT AN ENVIRONMENT VARIABLE
THAT IS WRITTEN DOWN NOWHERE, AND IT FAILS WITH A CODE THAT LOOKS LIKE A REAL
VERDICT.** Its header says `expect-exit: 0`. Run bare it exits **10**, on both
pins. Exit 10 is its own `string_byte_length(hit) != 14i64` — **a substantive
code from the probe's own map**, so the failure reads as a finding about the
language rather than a missing precondition. It needs **`TZ=Europe/Kiev`**
exported; with that it exits 0 on both pins. The string `Europe/Kiev` appears in
the probe file **0 times**, in `0.0.0.md` **0 times**, and `tests/probe/` has no
`README.md`. **Extent established rather than fixed only where found:** three
program-stage probes read state outside the program. `probe08_readlink` exits 0
bare — no hidden precondition. **`probe09_environ_split` is the model and the
contrast**: it documents *"PRECONDITION: run with `TZ=Europe/Kyiv` exported"*
**and exits a dedicated `30` when it is missing, so an unmet precondition
announces itself.** Same author, same afternoon; one probe made its precondition
self-describing and the neighbouring one reused a substantive failure code and
said nothing. **This is stream 2's to fix at `nitpick-time` 0.0.1** — give
`probe09b` a dedicated precondition exit code and a `PRECONDITION:` line, on
`probe09_environ_split`'s pattern. It blocks nothing today because no harness
runs yet; **it will produce a false failure the first time 0.0.2's `program`
stage runs, and the failure will look like a compiler regression.**

**CI MAY PIN THE COMPILER BY COMMIT AND EXPECT THE PINNED BYTES — BUT ONLY
UNDER TWO CONDITIONS, AND `nitpick-time` 0.0.1 STEP 4 MUST WRITE BOTH.** Asked
of `nitpick-compiler_s0` at this handover and answered 2026-09-05, because our
pin is a **binary** we copied while CI would **build** one, and P-10 has CI pin
by commit. Those are the same artefact only if the build reproduces.

**The answer is yes, by decision rather than by luck**, and the mechanism is
worth knowing: **D-204** (1.4.5) makes the toolchain a build input — the
manifest's `[toolchain]` pins LLVM **20.1.2 exactly, patch release included**,
along with the four flag sets every `llc`, `opt` and `ld.lld` call is built
from; the harness's **repro** stage re-runs the same compiler on the same
inputs from a *different working directory* and requires identical bytes on
every full run; its **parity** stage byte-compares the harness's own `npkc`
against `npkg`'s `build/npkc` on every run (**1083 verdicts, byte-identical on
all three 1.5.2c runs**); and **D-236** renders every embedded source path
relative to the manifest root, so the build path cannot leak into the artefact.

**The two conditions CI must satisfy, and neither is optional:**

1. **The same LLVM patch release — 20.1.2, not 20.1.x.** A patch release can
   change instruction selection. That is *why* the pin is to a patch.
2. **The ladder invoked from the tree root** — `npkg build`, or the harness's
   builder. Invoked elsewhere it may not reproduce.

**And the gap this closes.** `nitpick-libs_s0` flagged, correctly, that it
could prove `HEAD` did not move during the 15:52–15:56 build but **could not
prove the tree was clean during it**, and advised writing the weaker claim.
That session then answered it directly: **the tree was clean at 15:47** — `git
status` printed nothing before the push, and the ladder ran after the push from
the tree root. **So the strong claim is now supported and may be written.**

**AND IT IS NO LONGER AN ARGUMENT — IT IS A MEASUREMENT. 2026-09-05: a fresh
detached worktree at `0dfddac`, nothing uncommitted, run through the same
ladder (`npkg build` from the tree root) reproduced BOTH pinned artefacts
byte-for-byte** — `npkc` **7 304 552 B, sha256 `38e48973…`** and `npkrt.o`
sha256 `c9ddbcff…`. **Checked here against our own pinned files rather than
read off their message: `sha256sum` over `.internal/toolchain/0dfddac/` returns
exactly those two digests.** So *"built from commit `0dfddac`"* is now exactly
as strong a claim as the pin itself, and **`nitpick-time` 0.0.1 step 4 may
write it plainly** — provided it also writes the two conditions above, which
are what the reproduction depended on. Had the rebuild differed, CI could not
have pinned by commit at all and P-10 would have needed revisiting; it did not.

**1.5.2d IS PLANNED AND RATIFIED AS D-262** (their `daa5057`, 16:44 — **verified
here as docs-only: four files, all under `meta/`, no `src/` and no `runtime/`,
and not yet pushed**, so **`0dfddac` remains our pin and is still an ancestor of
their `main`**). **Its step 2 moves our canary**, and the landing notice carries
the before and after. Nothing here waits on it.

**O-N17 IS FIXED, AT THE PRIMITIVE, AND OUR EXTENT CORRECTION IS WHY THAT IS
CHEAP.** `nitpick-compiler_s0`, 2026-09-05: `emit_move_out` (`ir_stmt.npk`)
handed `ll_type` the *place's recorded type* and built the vacant helper's
symbol from that raw id; it now builds it from the **element type through the
specialization**, so **our five operations are one fix**. They verified the
pop, the set and the loop-clear shapes link and run to exit 0 under D-151's
leak check, where all three fail under `0dfddac`. **The extent correction was
right and changed nothing about the fix's shape** — which is the good outcome,
and worth reading twice: correcting an understated extent cost us one message
and cost them nothing, while shipping against *"one row"* would have produced a
generic `vec_clear<T>` that silently does not drop. **It is step 4 of 1.5.2d,
under its harness now**; the landing notice names the commit.

**AND THE SILENCE THAT MADE THE WHOLE CLASS POSSIBLE IS CLOSED WITH IT.** The
drop-body emitter **now says `EMIT-002` aloud when a registered type cannot be
lowered, instead of emitting nothing** — *"that silence is why `npkc` said yes
and `llc` said no"*. **That is the general form of O-N11, O-N14 and O-N17**,
which were three instances of one shape: the frontend accepting and the emitter
quietly declining. **Our harness rule does not change** — the `program` stage
still runs all four steps, because `npkc` exit 0 is not well-formedness — but
the gap it guards has narrowed from a class to whatever remains outside the
registered-type path.

**S-39 — AN OWNING `List<T>` LOCAL ALIVE IN `main` AT EXIT 0 IS REPORTED AS
`WildLeak`, EXIT 94, AT OUR PIN TOO.** Told to us unprompted, found while
writing O-N17's test, and recorded for the author on their side. `exit` runs
joins and defers **and no drops, by decision** (D-183's amendment keeps the drop
walk off the shutdown path), and **a `List`'s buffer is the one managed storage
D-151 counts, because the prelude spells it `wild`.** Their working spelling
until the author rules: **keep the list inside a function that returns**, which
is what every `List` test in their tree does. Their recommendation is that the
buffer allocate through the managed heap's untracked entry, as a channel ring
does.

**What it means here, stated because the answer is not obvious:** for the
prelude's `List<T>` this is a surprise. For **our** containers it is the
enforcement we asked for — `Vec<T>`'s block is `wild` by P-23 precisely so that
an unpaired `vec_free` traps at exit under D-151. **So the same mechanism is a
defect there and a feature here, and the difference is whether the type's owner
intended `wild`.** No action for us; do not "fix" a `Vec` that traps at exit.

**O-N18 is their DEF-22**, recorded with our two controls, to be fixed after the
landing. **And the `string ==` / `TYPE_REFERENCE` §3.2 mismatch is accepted as
our item in their doc-sync backlog** — the language's answer is `.eq` (D-250:
comparisons of owning types are calls, not operators) and **the table is what is
wrong**. They asked for no separate item from us.

**1.5.2d's STEP STATUS, as of 2026-09-05 evening:** step 1 (the frontend's
three scaling defects) **committed and under its harness**; step 2 (the prelude
trim) **implemented and passing both runners' self-checks**, about to go under
its harness; **the allowlist fix (DEF-21, below) is the step after**; then docs
and the landing notice. **We re-pin when it lands, then re-measure — in that
order**, because a number taken against the old pin proves nothing about the
new one.

**DEF-21 — THE ALLOWLIST FINDING WAS ACCEPTED, AND IT WAS NOT KNOWN.** Raised
by this workbench 2026-09-05 under the lifted constraint and taken up the same
evening as the compiler's **DEF-21**, carrying our measurement with
attribution, **with a harness of its own** as a step in 1.5.2d. **The fix is
exactly the model our arithmetic implied: the allowlist is the runtime's
EXPORTS** — the non-internal `define`s plus the `module asm`'s `.globl` names —
**not every `define`.** Both halves move: the **57** internal defines leave the
list, so a program naming one is refused *at scan time by name* as D-206 meant
rather than at `ld.lld`; and the **2** `.globl` names enter it, since
`npk_clone_raw` was **a false refusal of a legal program**, the worse half.
They are checking whether the harness's `check_zero_dependency` builds its list
the same way and fixing it in the same step, and `BUILD_REFERENCE` §4.1's prose
will say *exports*.

**What made it a finding rather than a report, in their words, is the
arithmetic** — 109 + 2 = 111 identified the object as the authority and showed
the list had been built from the wrong side of it. **A measurement that pins
down the mechanism is worth more than a count that only shows something is
off**, and the difference cost one extra command.

**SEPARATE COMPILATION IS AN OPEN OFFER, DELIBERATELY NOT TAKEN UP YET.** That
session confirmed P-16's failure is not a compiler defect — *a program is one
object plus the runtime; a library is consumed as source through the module
graph* — and offered to put **separate compilation of library objects** to the
author as a design decision with its own row, with a recommendation, **if the
libraries need it. This workbench's answer is NOT YET, and the reason is a
number about to change.** The entire cost of the one-object model is that every
program re-emits the whole prelude, and step 2 removes ~94% of exactly that.
**Asking for a design change now would rest the case on a measurement we are
days from invalidating.** Re-pin when 1.5.2d lands, re-measure the 30-program
spread, and decide against real numbers. **If the case survives the trim, raise
it then; the offer is on the record and does not expire.**

**THE RE-PIN CHECKLIST — assembled 2026-09-05 because none existed and the
re-pin was being carried as a one-line instruction.** §3 has the general
procedure; this is what *this* re-pin owes on top of it:

**STATUS 2026-09-05 16:0x — items 1–5 are DISCHARGED; 6, 7 and 8 remain and
belong to the streams.** 1: answered and the `binary` line is written. 2: the
harnesses finished and the pin was taken after them. 3: `npkrt.o` taken again
and checked — byte-identical, verified not assumed. 4: all four re-measured,
results in the table above. 5: the after-value is measured
(`NITPICK-REACH-003`; **four** identities for `case1`, **six** for `case3` — the
count is per program, see the O-N11 row) and the two transcripts can now be
re-recorded — **that write belongs to `nitpick-time`'s stream at its claim
(W-7)**, not to the orchestrator. **6** (the six stale `list.npk` citations,
three files, two streams), **7** (`probe04b`'s rationale as historical) and
**8** (`check_refs` naming each repository) are unchanged and outstanding.

1. ~~**Establish the target commit and the binary's provenance**~~ — **DONE
   2026-09-05 13:35.** The answer is in the block above: `build/npkc` is a
   working-tree intermediate of 1.5.2 step 0, the pin point is the 1.5.2c
   close, and the compiler session sends the identity. **Still owed: write its
   reply into `PIN.md` as a `binary` line when the pin is taken**, as the
   previous pin did.
2. **Do not pin while a harness is running against the tree the binary came
   from**, and do not write into that tree — `library-sessions-write-scope`.
   Three are running as of 13:27; the notice at ~15:30 is the all-clear.
3. **Take `npkrt.o` again and check it.** Do not carry the identical-hash
   measurement above forward as an assumption.
4. **Re-measure O-N10 and O-N11 against the new pin — and note the compiler
   session's steers, which change what "correct" looks like for both.**
   Re-run **O-N4** and **O-N9** too; probe 04 now costs ~1.24 s, which is the
   point of its discharge.
   - **O-N11 is now a COMPILE-TIME refusal, not a runtime verdict.** A root
     with `main` and no `failsafe` is `NITPICK-REACH-003` **at `main`**,
     whatever the exit code (1.5.1b step 1b), and D-256…D-261 do not touch it.
     A verdict phrased as an exit code is measuring the wrong thing now.
   - **O-N10's shape moved with D-258.** A derived body reaches every member
     *through the trait it derives*, so a payload's type must implement that
     trait — asked at the **call** of `eq`/`cmp`/`clone` and refused there as
     `TYPE-017` naming the derive, the parameter and the bound (D-256),
     **never at the declaration**. A `string` PAYLOAD under the four that bind
     it (Eq, Ord, PartialOrd, Clone) is **`DERIVE-006` at the derive** — a
     lending `pick` cannot bind an owning payload — while a `string` FIELD of
     a struct derives fine through the prelude's four (D-257). `Hash` on an
     enum is the tag's; `ToString`/`Debug` render the variant name. Every
     derived diagnostic reports **at the derive's declaration** (D-259), and
     **a path containing `<derived-` in any output is a compiler defect the
     compiler session has asked us to report.**
   - **New surface to probe at the same time (1.5.2c):** a generic enum now
     derives as a generic struct does, so `Opt<T>` under a derive is legal and
     `Opt<Point>` compares only if `Point: Eq`, asked at the call.
5. **Re-record `nitpick-time`'s two DEF-5 transcripts** — an `npkc`
   `NITPICK-REACH-003` refusal replaces the `llc` failure — and note the
   identity count is **per program**: `case1` names **four**, `case3` names
   **six**. This line once read *"four, not six"*, which was true of `case1`
   and became a general claim two paragraphs later; **six was never wrong, it
   was another program's bill.**
6. **Correct the stale comments citing the deleted `src/frontend/list.npk`.
   THE COUNT IS SIX, IN THREE FILES — NOT FIVE IN TWO.** Re-derived
   2026-09-05 with an instrument that can actually see the library checkouts
   (see the sweep-blindness block below); the old list was produced by a sweep
   that could not. **The board's previous list was wrong in both directions.**
   The six real sites, each fixed at its own stream's claim (W-7):

   | # | Site | What it cites |
   |---|---|---|
   | 1 | `nitpick-regex/tests/probe/probe01_pod_inst_array.npk:24` | `src/frontend/list.npk` by path |
   | 2 | **`nitpick-regex/tests/probe/probe04_inherent_generic_impl.npk:18`** | `src/frontend/list.npk` by path — **a file the old sweep never saw at all** |
   | 3 | **`nitpick-regex/tests/probe/probe04_inherent_generic_impl.npk:47`** | `list.npk` by basename — **same unseen file** |
   | 4 | `nitpick-time/tests/probe/probe06_generic_vec.npk:14` | `src/frontend/list.npk` by path |
   | 5 | **`nitpick-time/tests/probe/probe06_generic_vec.npk:92`** | `list.npk` by basename — **missed by the old sweep** |
   | 6 | `nitpick-time/tests/probe/probe06_generic_vec.npk:107` | `list_init`, a function the deleted file defined |

   **And two the old list counted that are NOT findings:**
   `probe06_generic_vec.npk:49` and `:60` reference `List<T>` and D-246/D-247
   semantically and cite **no deleted path**; the board itself calls `:60`
   "exactly right". Leave them.

   **The mechanism of the error is the durable part.** The old sweep searched
   for the token **`List`** while the property is *"cites the deleted
   `list.npk`"*. Those are different sets: it caught `:107` by accident (that
   line says `list_init`, not `List`) and **missed every `list.npk` basename
   citation**. The same board paragraph asserts *"nothing here declares any
   `list_init`"* while its own count includes the line that names `list_init`
   — **the two halves of one paragraph contradict each other**, and neither
   half was re-derived. D-239's substantive conclusion is unchanged and was
   re-verified: no `struct:List`, no `mod:list`, no `list_push`, no
   `list_reserve`, so **no rename is required anywhere**; only the citations
   are stale.
7. **`probe04b_emission_shape.npk` exists as a 300-row stand-in *because probe
   04 cost 281 s*.** That reason is gone. Keep the file; record its rationale as
   historical rather than current.
8. **Run `check_refs.py` naming EACH repository, after the comment corrections
   and before `git add`**, and gate the commit on it — **reading the check's
   own exit status, not a pipeline's.** **It takes one directory and checks
   only that one:** `check_refs.py .` from the root prints `All clean` having
   examined the root alone (it does at least name `nitpick-libs` in its
   output, which is the one thing that keeps it honest). **Ran clean
   2026-09-05 13:33 over a denominator of seven** — the workbench root, the
   five library checkouts, and `../nitpick-apps/nitpick-posix` — all exit 0.
   Two traps live in this item: *if you pipe it, `$?` is the pipe's last
   command*, which let an ungated commit through on 2026-09-05 (use
   `${PIPESTATUS[0]}`); and **`check_refs` reports a `tracked-file-missing`
   finding** as of `7da5c2d`, so an unstaged deletion is a finding rather than
   a crash — which is the state the mandated pre-`git add` order puts it in.

**A CROSS-REPOSITORY SWEEP RUN FROM THE WORKBENCH ROOT SEES NONE OF THE FIVE
LIBRARIES, AND SAYS NOTHING ABOUT IT. BOTH OF THIS ECOSYSTEM'S CANONICAL SWEEP
TOOLS ARE AFFECTED. Measured 2026-09-05 by the fifth orchestrator; this is how
checklist item 6's site list was found to be wrong.**

Two independent causes land on the same silence:

- **`grep` on this machine is `ugrep` 7.8.4, installed at `/usr/bin/grep`.**
  `grep --version` says so; `which grep` does not. ugrep honours ignore files
  in recursive mode, and the workbench's own root `.gitignore` opens with
  **`/*/`** — it ignores *every* top-level directory, which is exactly how this
  repository avoids embedding a library as a gitlink. So the ignore rule that
  makes the workbench correct is the rule that makes its sweeps blind.
- **`git grep` from the root cannot see a library either**, and for a
  different reason: each library is a **separate checkout**, so its files are
  not in this repository's index at all. `git grep -l -i derive -- '*.npk'`
  from the root returns **nothing**, correctly and uselessly.

**The measurement, one pattern, five tools, same tree:**

| Invocation | `.npk` files matching `derive` |
|---|---|
| `grep -rl -i derive --include='*.npk' .` (from the root) | **0** |
| `git grep -l -i derive -- '*.npk'` (from the root) | **0** |
| `grep -rl -i derive --include='*.npk' nitpick-time` | 7 |
| `grep -rl -i derive --include='*.npk' --no-ignore-files .` | **14** |
| `find . -name '*.npk' -not -path '*/.git/*' -print0 \| xargs -0 grep -l -i derive` | **14** |

**The instrument was commissioned before it was believed:** the two tools that
see everything were diffed against each other and agree on the same 14 files,
so 14 is a measurement rather than one tool's opinion.

**Why this is the worst instance of `PLAYBOOK.md` §6's shape yet found here —
the sixth — and worse than `check_refs .`'s.** A `check_refs .` run at least
prints the name `nitpick-libs`, so its denominator of one is visible to a
reader who looks. **A sweep that matches nothing prints nothing at all.** There
is no verdict to be sceptical of, no count to ask for the denominator of, and
the output of "swept, no violations" is byte-for-byte the output of "swept
nothing". Every discipline this workbench has built — *a list of files is
produced by `git grep`, never by recall*; *ask for the denominator, not the
verdict* — routes straight through the one failure mode that produces no
number to interrogate.

**And this project has already been bitten by the same `.gitignore` line
once.** That file's own comment says each workbench directory must be
un-ignored by name *"or it vanishes silently — which is exactly what happened
on the first attempt to add the plugin."* The note was written about tracking;
nobody carried it across to searching.

**What it actually invalidated, and what it did not.** Checklist item 6's site
list: **wrong**, three sites missed including two in a whole file
(`nitpick-regex/.../probe04_inherent_generic_impl.npk`) that no previous sweep
had ever seen. D-248's *"swept all six repositories: zero violations"*:
**re-verified and correct** — 0 violations over a stated denominator of **87**
`.npk` files, a denominator the original claim never gave. Every other
cross-repository count on this board was produced before this was known and
**should be re-derived at the sweep that next touches it**, not trusted.

**THE RULE, and it is cheap: a sweep across libraries is run per repository by
name, or with `find … -print0 | xargs -0 grep`, or with `--no-ignore-files`.
Never with a bare `grep -r` or `git grep` from the workbench root.** State the
denominator with every result. A sweep that reports no matches must also report
how many files it opened, or it has reported nothing.

**Why the re-pin was NOT done at this stopping session:** it would leave a fresh
toolchain with **no verified measurement against it**, discarding the one this
session paid for. Everything verified today — O-N4, O-N9, O-N10, O-N11 — was
measured against **`94874ce`**, and that is the pin those verdicts belong to.
~~**The next session re-pins as its first action**~~ — **superseded 2026-09-05:
there is nothing to pin yet.** The re-pin is now *scheduled*, not owed on
sight: wait for the compiler session's 1.5.2c landing notice (expected ~15:30
on 2026-09-05), then run §3 with the checklist above. **Take `npkrt.o` again
and check it rather than assuming it unchanged** — DEF-12 already caught
this ecosystem once assuming the runtime half was identical.

**D-239 — step 5b moved `List<T>` and its functions into the PRELUDE, deleted
`src/frontend/list.npk` and its 46 imports, and a program's own `List` is now
refused by the loader. SWEPT ACROSS ALL FIVE LIBRARIES: NO COLLISION.** Nothing
here declares a `struct:List`, a `mod:list`, or any `list_init` / `list_push` /
`list_reserve` — **re-verified 2026-09-05 over a stated denominator of 87 `.npk`
files, so this conclusion stands and no rename is required anywhere.** ~~Five
occurrences of the token exist~~ — **that count was wrong, and so was the site
list built from it.** The property is *"cites the deleted `list.npk`"*, the old
sweep matched the token *`List`*, and the two sets differ: **six sites in three
files**, one of them a file no earlier sweep had ever seen. The corrected table
is checklist item 6 above; the reason the sweep could not see it is the
sweep-blindness block above. Every one is still **a comment**, so the residue is
stale citations to correct at the re-pin, each at its own stream's claim (W-7).
Note
`probe06_generic_vec.npk:60` already says D-247 makes *the COMPILER's* `List<T>`
owning, which is exactly right and consistent with RX-126.

**CATALOGUE-DON'T-RAISE IS LIFTED. Ruled by the author 2026-09-05: "raise as
found."** Defects met in library work now go to the compiler session **as they
are found, with their measurements**, rather than being held for a batch. The
constraint's original rationale — a closing fix batch on the compiler side —
had expired, and two orchestrators in a row declined to lift it on their own
judgment, which is the right instinct and is also how an expired rule survives
for days. **It was resolved by asking.** The evidence pointed the same way
before the ruling: **~~O-N16~~ was catalogued rather than raised and the
compiler session closed it the same day anyway**, so cataloguing bought nothing
there; and that session has since **asked us explicitly** to report one class on
sight — any output path containing `<derived-`. Raising still means what W-27
made it mean: **state what the defect blocks**, what it merely inconveniences,
and what it does not touch. Sequencing remains the author's.

**~~O-N16~~ — CLOSED UPSTREAM 2026-09-04, same day it was catalogued.** The
compiler session corrected DEF-8's closing sentence in its `OPEN_DECISIONS.md`
§2f to give the reason rather than the false premise — our recipes *do* pass
copyable fields out of locals; a hand-written container never drops, so the old
clear skipped no drop; we are outside the recognition, not outside the shape.
Their commit `8dbef43`, docs only. **Catalogued rather than raised, and closed
anyway** — worth noting for the next session that the catalogue-don't-raise rule
cost nothing here.

**S-38 — RATIFIED BY THE AUTHOR AND IN FLIGHT AS THE COMPILER'S 1.5.2d. NO
LONGER OPEN, AND NOT OURS TO RE-REPORT.** Confirmed to this session by
`nitpick-compiler_s0` on 2026-09-05: they put it to the author directly with the
measurement and the recommendation, and he ratified it — *"lets go with your
recommendation"*. **Do not re-report it.** The previous board carried it as
*"the author decides"*, which was true when written and is now stale; a session
reading only that line would report a settled decision a second time.
**Originally raised by this workbench 2026-09-05 and taken up the same
afternoon** as the compiler's `OPEN_DECISIONS` **S-38** (their `a882188` —
verified here as docs-only, one file, one insertion, no `src/` or `runtime/`,
so **our pin at `0dfddac` is unaffected** and `sha256sum -c` still passes).
**The compiler session explicitly declined to close it as the price of D-257**
and asked that we carry it as open. It confirmed the mechanism: D-257's
generated scalar impls are **348 rows in thirteen families**, and 1.5.2b had
already recorded that *"every prelude impl body is emitted whether reached or
not"* with **+2.2% IR and +14% frontend time** measured on the compiler's own
tree. **What nobody had measured is the fixed per-program cost — which is
exactly what a per-program harness pays, and is why this workbench saw it and
they did not.** Of their three options the author took **(1)** reachability-driven
emission of non-generic prelude bodies via the demand walk the emitter already
runs for generic instances — deterministic, semantics-neutral, and *"worth doing
before 1.5.3 hangs contract obligations on every prelude function"*. But their
option **(2)** — *measure the frontend's share first* — was carried out before
any of it started, **and it changed the answer. That is the part worth reading.**

**THE COST IS NOT THE PRELUDE'S SIZE.** On the floor-only probe the **frontend
holds 0.72 s of the 0.82 s** and emission only **0.10 s**, and a profile names
**three scaling defects** rather than prelude bulk: the bindings analysis
allocating one state slot **per statement of the whole program, for every
function** (**57%** of the run), and the type interner and the string interner
deduplicating by **linear scan** (13%, plus part of the lexer's 12%). Those are
fixed first as ordinary engineering with **no language change**; reachability-
driven emission follows (587 of the probe's 608 emitted functions are prelude
bodies). **Why this lands harder here than the raise assumed:** all three
defects scale with the number of programs compiled, so a harness that compiles
**many small programs pays them repeatedly** — the same structural asymmetry
that let this workbench see the cost when the compiler's own harness could not.
**And the durable lesson is option (2) itself: the obvious cause was measured
before it was believed, and it was wrong.** We had attributed the whole +0.75 s
to D-257's generated impls; five-sixths of it is three unrelated scaling
defects. Our measurement of the *cost* was sound and our inference about its
*cause* was not — and nothing on this board had marked that inference as one.

**We stop measuring this per program.** The two data points and the
22-of-30 constancy argument are what the decision needs, and any fix arrives
with its own before/after. **One canary is kept:
`nitpick-time/tests/probe/probe11d_floor_only.npk`, whose `.ll` is 845 282 B at
`0dfddac`** — that is the number to watch, and a change in it is the signal.

**THE RE-PIN IS DONE — `aaffb87`, 2026-09-05 22:47 — AND THE CANARY LANDED ON
ITS PREDICTION.** 1.5.2d closed and this workbench re-pinned immediately, then
re-measured. **The prediction was a real test and it passed:** the board said
*check the VALUE, not merely that it moved*, expecting ~50 000.

| | `0dfddac` | `aaffb87` | |
|---|---|---|---|
| canary `.ll` | 845 282 B | **50 560 B** | **−94.0%** |
| canary functions | 608 | **14** | predicted 14, **exact** |
| **full harness run** | **240 s** | **41.8 s** | **5.7× faster** |
| harness verdicts | 40 units, 0 fail | **40 units, 0 fail** | **unchanged** |

**The one-byte gap against their predicted 50 561 is two different source files,
not a discrepancy** — they measured their own floor probe, we measured ours, and
the function count matches exactly. **Stated rather than smoothed over, because
"close enough" is how a real difference gets absorbed the next time.**

**THE HARNESS IS GREEN AT THE NEW PIN AND NOTHING BROKE**, which was not
guaranteed: the compiler session warned that *"every emitted module holds only
the prelude functions it references, so any probe asserting a prelude symbol in
IR needs a use"*. No probe here did. **40 units, 0 failures, 5 pending — the
same verdicts, in a sixth of the time.**

**ALL FOUR DISCHARGED STOPS RE-MEASURED, and one improved.** **O-N11** —
`case1` names **4** identities and `case3` **6**, unchanged, so today's
per-program correction still holds at the new pin. **O-N4** — `probe04` is now
**1.18 s at 26 336 KiB**, against 2.03–2.06 s at ~119 MB on `0dfddac`: faster
*and* a quarter of the peak, so it stays discharged with room. **O-N9** —
`BORROW-012` and `BORROW-001` unchanged. **O-N10** — covered by the harness's
derive probes, green.

**OUR TWO DEFECTS BOTH LANDED IN THIS PIN.** **O-N17 is FIXED** — all five
cases now link and write objects, including `case1` and `case5`, which produced
`llc` exit 1 and no object at `0dfddac`; their IR also fell from 850 377 B to
55 652 B. **DEF-21, our allowlist finding, is 1.5.2d step 2b** — the allowlist
is now the runtime's **exports**: 112 entries with `main`, both `.globl` names
in, the 57 internal names out. **O-N18 still refuses** (`NITPICK-EMIT-002`),
as expected: it is their DEF-22, scheduled after the landing.

**WHAT CHANGES FOR EVERY LIBRARY AT THIS PIN, and the last one is a trap:**
`vec_pop`, `vec_set`, `vec_clear`, `vec_truncate` and `vec_free` at an owning
`T` link and drop; a program naming one of the **57 internal runtime symbols**
is now refused **at the scan, by name**, instead of at `ld.lld`; `npk_clone_raw`
is allowed, so a legal program that was falsely refused now passes; and
**every emitted module holds only the prelude functions it references, so any
probe asserting a prelude symbol in IR needs a USE.** `nitpick-time` has none;
**the other four repositories must check at their next claim.**

**THE CANARY IS NOW EXPECTED TO MOVE, AND WE KNOW ROUGHLY WHERE TO — WHICH
MAKES IT A REAL TEST RATHER THAN A TRIPWIRE.** `nitpick-compiler_s0` measured
1.5.2d step 2 on the same probe on their side: **845 282 B → about 50 000 B**,
a ~94% cut. So the next session must not read the change as a defect — read it
as the landing — **and must check the VALUE, not merely that it moved.** A drop
to ~50 000 confirms the trim; **a drop to something else, or no drop at all, is
the finding**, and it is one we could not have stated yesterday because we had
no expected value. **An expected number turns a canary into a prediction.** `nitpick-compiler_s0` sends the before/after at that point and has
asked for our 30-program re-measure afterwards, **which we should run**: it is
the only per-program evidence either side has, and re-running a measurement we
already know how to take is the cheapest confirmation available. **Re-pin
before re-measuring**, since a number measured against the old pin proves
nothing about the new one — that is the rule this workbench already paid for
once at the 0dfddac re-pin.

**Why this is worth reading twice: it is the second time in two days that
raising cost nothing and bought something.** O-N16 was catalogued rather than
raised and was closed upstream the same day anyway; S-38 was raised under the
lifted constraint and became a decision item with a recommendation within
twenty minutes. Both point the same way, and the constraint is now lifted.

**Awaiting the author on the COMPILER side** (their `OPEN_DECISIONS.md` §7),
none of it blocking us, two being semantics this ecosystem already builds
against: **S-24** derived comparisons over a generic parameter; **S-25**
`List<T>` in the prelude as struct and functions, implemented in step 5b;
**S-26** a partial move leaves the vacant value; **S-27** `exit` after
`wild_release_all()`, `TYPE-062`.

**THE `devteam` IMPORT — FOUR MECHANISMS LANDED 2026-09-05, SEVEN MORE LISTED.**
The full list, with what each costs and why it matters here, is
[`meta/audits/devteam-import-2026-09-05.md`](meta/audits/devteam-import-2026-09-05.md).
Landed: the guard now names the interpreter-heredoc limit **in its refusal
message** rather than only in its docstring (guidance goes where the temptation
is — `devteam` measured this changing an agent's behaviour); **`git worktree
list` is no longer refused as a write**, with thirteen new controls covering
each read form and its write twin; `tools/run_controls.py` finds and runs every
control and treats *"no controls found"* as a finding; and every control now
reports its **case count and false-positive share** — `111 cases, 50 of them
false-positive controls (45%)`.

**Doing that found a live defect of the worst class, now fixed.** `check_refs`
read an identifier inside a fenced block, and inside its own quoted output, as a
citation — so it reported `cited-undefined` against a file that had pasted
evidence, **which this workbench requires a worker to do**. A check that fires
on mandated behaviour puts the correct response and the safe response in
opposite directions. `prose()` now strips fences before the citation scans
(deliberately **not** before the leak scan). **Stated gap, not closed:**
verbatim output quoted *inline* is still miscounted, and cannot be fixed by
stripping inline spans because `` `RX-126` `` is how a real citation is written
here. The rule that implies — verbatim output belongs in a fence — is item 5's
business, not a check's.

**STOPPED 2026-09-04 13:40 at the author's request, at a clean stop**, to conserve a weekly quota being spread across several sessions. Both streams closed their subcycles and both were independently VERIFIED PASS. **Resume points:** s1 `nitpick-regex` **0.0.4** (`src/core/`), s2 `nitpick-time` **0.0.1** (the skeleton) — both planned, unblocked, and NOT dispatched. Stream 3 has still never run. **UPDATED 2026-09-05 by the fifth orchestrator: the re-pin question that stood in front of both resume points is ANSWERED and the answer is to wait until ~15:30** (see the block at the top). Width is **1**, so one stream runs; the board recommends **s2 `nitpick-time` 0.0.1**, whose gate is satisfied — 0.0.0 is `DONE` and the probes it names (01, 04, 06) have recorded verdicts — **but it is deliberately NOT dispatched before the pin lands**, because step 4 of that subcycle *pins the compiler by commit in CI* (P-10). Dispatching now would write the stale `94874ce` into a new CI workflow and guarantee an immediate bump commit, and steps 2 and 5 accept against a compiler we are about to discard. That is the same argument the previous session used for not re-pinning at a stopping point — a measurement belongs to a pin — pointed the other way. The questions table has **four** entries; question 4 (width) is answered, three stand.

---

## Legend

| State | Means |
|---|---|
| `—` | not started, not claimed, nothing blocking it |
| `CLAIMED sN` | stream N owns this repository; the in-flight table says what it is doing |
| `BLOCKED on <repo> <cycle>` | cannot start until that cycle is DONE; the reason is always a named cycle, never "waiting" |
| `DONE` | every cycle closed and archived to `done/` |

---

## In flight

| Stream | Repository | Subcycle | Agent label | Since | Model | Note |
|---|---|---|---|---|---|---|
| s2 | `nitpick-time` | **0.0.4 DONE — VERIFIED PASS** at `06f82c0`; harness **GREEN, 40 units, 0 failures, 5 pending, ~240 s**. `src/core/` exists: `vec.npk`, `bytes.npk`, `limits.npk`, **35 public names = 10 + 12 + 13**. 0.0.3 at `60e03bf`, 0.0.2 at `e101312`, 0.0.1 at `0c7e156`. **`ahead 4` is correct.** Next: **0.0.5 (the tzdb size spike)**, not dispatched | *(no live agent)* | 2026-09-05 21:03–22:0x | `claude-opus-5` worker, small-model verifier | **IT CORRECTED THE ORCHESTRATOR ON THE EXTENT OF ITS OWN DEFECT, AND THAT CORRECTION IS THE MOST VALUABLE THING IN THE SUBCYCLE.** O-N17 was raised — by me, upstream — as blocking **one** API row. It blocks **five**: the primitive is `move(v.items[i])` in a generic function at an owning `T`, and `vec_pop`, `vec_set`, `vec_clear`, `vec_truncate` and `vec_free` all sit on it, **a loop being a different caller and not a different primitive**. Confirmed here on `case5_generic_drop_loop` and by the verifier on all five cases with four scalar controls. **Understating it was the dangerous direction:** *"one row"* is exactly what would have justified shipping a generic `vec_clear<T>` that **silently does not drop**, which passes the `exit 0` gate because D-151 cannot see a managed body — an extent short by four rows, discharged by a green suite. **The compiler fixed it at the primitive within the hour, so all five are one fix** (1.5.2d step 4). **`vec_pop<T>` is HELD, not rewritten** (W-11). **THE VERIFIER RAN THE LITERAL COMMANDS THIS TIME** — the planted constant moved `check_constants_named`'s denominator 11/2 → 11/3, the `/bin/true` caps flipped between 2688 and 2816 KiB, all five defect cases compiled — which is the 0.0.3 fix working: it substitutes reading for running only where a check needs setup, so the dispatch now supplies the setup. **Zero stale `O-N12` citations remain; the seven that survive are deliberate records of the correction**, including an entry in this repository's own `OPEN_QUESTIONS.md` reading *"O-N12 — NOT THIS REPOSITORY'S"*, which inoculates the next worker who reaches for a number. **TM-131 corrected this subcycle's own acceptance:** a **low `ulimit -v` measures the LOADER, not the program** — `probe06c` and `/bin/true` flip at the same cap — so the old *"under 768 KiB"* figure was wrong and the gate is now one shared 64 MiB cap with opposite outcomes, 92 against 0 |
| s1 | `nitpick-regex` | **0.0.3 DONE — VERIFIED PASS** at `91657eb`, pushed, harness 63/63 in 37.5 s. Next: 0.0.4 (`src/core/`), **not dispatched** — this session is stopping | *(no live agent)* | 2026-09-04 | `claude-opus-5` | **RX-126 is this subcycle's most valuable output and it corrected THIS BOARD** — see its block above. O-N10 also discharged here (RX-125), on thirteen measured properties, **two of which `nitpick-time` cannot test** (its enum has one payload field per variant), so O-N10's verification is still owed there. RX-123 (both leak checkboxes), RX-124 (`parse` no longer depends on a compiler-repository tool) landed. O-N16 raised, numbered from `meta/OPEN_QUESTIONS.md:355`. **ACCEPTED WITH A KNOWN OVERSTATEMENT, carried to 0.0.4 rather than re-dispatched at a stopping session:** the verifier found that the mutation-test **transcripts are NOT committed** — `meta/roadmap/0.0/0.0.3.md` §4 holds a per-case attribution *summary table*, which is what the acceptance criterion actually required and is why this is a PASS — but **`harness/README.md` claims "§4 has the transcripts", and it does not**. `PLAYBOOK.md` §6 says a summary is not evidence, and `nitpick-time` 0.0.0 was once FAILED by its own verifier for exactly this, so the precedent cuts against letting the sentence stand. **0.0.4 must either commit the raw mutation runs with their exit codes, or correct that sentence to claim only what is there.** Do not let it pass a third time

## Questions for the author

| # | Stream | Raised | Question | Recommendation |
|---|---|---|---|---|
| 1 | s2 | 2026-09-04 | **Is a committed `REPORT` block immutable?** A worker left one of the six DEF-3 sites unedited because it sits inside a committed REPORT block, arguing a report records what a worker said on a date and must not be rewritten — correcting it in a later record entry instead. **This is the second dispatch to meet the question; the first left it open.** | **Ratify it, and write it into `WORKSTREAMS.md`.** The worker's reasoning matches this workbench's existing append-only rule and the finer form of it in `PLAYBOOK.md` §6 — what may be amended depends on whether the document records something that *happened*. Making it explicit costs one rule and stops a third dispatch re-deciding it |
| 3 | — | 2026-09-05 | **Should `filesystem.denyWrite` be configured?** The write guard cannot judge an interpreter heredoc (`python3 - <<PY` … `open(path,'w')` …) — measured, four controls, the other three forms refuse correctly. The guard's own docstring names the sandbox's `filesystem.denyWrite` as the airtight mechanism for exactly this, and **it is configured nowhere**. Meanwhile this harness ships a standing instruction preferring heredocs and `sed` over `Write`/`Edit`, so a session writes through the unjudged form *by default*. The real exposure is a library worker reaching `../nitpick` and invalidating a multi-hour verification run | **The author's call, and deliberately not acted on here** — this is a permissions/settings change and no session should make one on its own analysis. Options: configure `denyWrite` for `../nitpick`; or teach the guard to refuse `python3`/`perl`/`node` invocations that carry a heredoc at all when a compiler path appears anywhere in the payload (cruder, more false positives, and a guard with false positives gets disabled — the guard's own docstring warns of this); or accept it and say so in `CLAUDE.md`, which today claims enforcement "where they can be" without saying where those are . **A SECOND, OPPOSITE DEFECT IN THE SAME GUARD, found 2026-09-05: it refuses `git worktree list`, which is a READ**, as "a mutating git subcommand" — its `GIT_WRITE` set contains `worktree`, which has both read (`list`) and write (`add`/`remove`) subcommands. The guard's own docstring warns that *"a guard with false positives gets disabled, which is worse than no guard"*, so this is the failure mode it named. The two findings pull in opposite directions and should be fixed together: one form is unwatched, another is refused for reading |
| 2 | s1 | 2026-09-04 | **O-N10's verification is complete for `nitpick-regex` and cannot be completed for `nitpick-time`.** Two of the thirteen properties measured need an enum with more than one payload field per variant, which `nitpick-time`'s does not have | **No action needed now**, recorded so a later session does not read `nitpick-time`'s partial verification as an omission. The gap is a property of that library's types, not of the work |
| 4 | — | 2026-09-05 | **What width should the next session run?** The board carries **width 2**, confirmed by you on 2026-09-04, and both streams have a planned, undispatched subcycle ready (`nitpick-regex` 0.0.4, `nitpick-time` 0.0.1). Since that confirmation the binding constraint changed: the weekly quota is low and an experiment overspent it. Stream 3 has still never run | **Width 1 for the next session, then back to 2 when quota recovers** — this is `parallel-planning-serial-implementation`'s dial turned down, not a change of plan. The arithmetic is the argument: width 2 is two workers plus two verifiers, so **four dispatches before anything is verified**, and the re-pin has to be settled with the compiler session before either stream can be trusted anyway. Width 1 also puts the whole re-pin on one stream rather than duplicating it. **Model split, unchanged and working:** workers on `claude-opus-5` (stream 1's worker produced RX-126 by reading compiler source and drawing a distinction nobody asked for), verifiers on the small model per orchestrate §12 — both of 2026-09-04's verifiers returned PASS with real substance and one caught an overstatement the orchestrator would have let through |

**Q-9 — answered 2026-09-03 by the author: state what it blocks.** Landed as
**W-27** in `WORKSTREAMS.md`. The compiler side's rule is confirmed — *a defect
a real program finds is fixed before planned work* — so this workbench now says
plainly what a defect blocks, what it merely inconveniences and what it does not
touch, and drops "no schedule pressure implied", which reads as modesty and is
really a withheld fact. Sequencing stays the author's. O-N9 is the evidence the
hedge costs something: recommended here as conformance rather than a block,
overridden by the author, and the override cost nothing because the fix batched
with three others.

**Q-10 — answered 2026-09-03 by the author: both, and sweep for the gate.**
0.0.3 gains the cost-and-heap stage and 0.0.4's gate becomes a `peak_live`
assertion, both once the re-pin makes `NPK_HEAP_STATS` real. The read-only sweep
ran immediately, and **the unfalsifiable gate is in all five repositories** —
the site list is in `RECORD.md` and the per-repository notes are in the stream
tables below. Each fix waits for its own stream's claim (W-7); `nitpick-time`'s
two lagging sites go to the worker now, because that repository is claimed.

**RX-126 — D-247 DOES NOT MAKE A LIBRARY'S CONTAINER OWN, AND THIS BOARD SAID
IT DID. Found by stream 1, 2026-09-04; confirmed by the orchestrator against the
pin's own source before the board moved.** `decl_is_list`
(`../nitpick/src/frontend/type_layout.npk`, the `list_scope` / name / field
walk) recognises a `List` only when **all** of these hold: the declaration is
homed in the compiler's own `list` scope; it is a struct named **exactly
`List`**; and it has **exactly three fields, in order, named `items` (of pointer
type), `count`, `cap`**. D-247's owning behaviour keys on that predicate.

**No library here has such a type.** Every container in this ecosystem is
hand-written, differently named and differently scoped, so **D-247 changes
nothing for any of them.**

**What this board asserted and what is actually true:**

| The board said | The pin says |
|---|---|
| "`Vec<T>` does not own **until** D-247" | `Vec<T>` does not own, **full stop**. D-247 is not a date after which it does |
| "S-26 changes the drop flag and **D-247 makes the container own**, both in the same re-pin" | S-26's half stands; D-247's half never applied to us |
| the 125 MiB managed-body leak is a **before-number** that the re-pin moves | **it is not closed, and it is not going to be.** Stream 2 measured `probe06b` at **125 184 KiB, three times, at this pin** — independently corroborating stream 1's reading from the other direction |

**Impact, stated plainly.** The managed-body gap is permanent for
hand-written containers until a library closes it itself. **`RX-110` and
`RX-123` therefore stand at FULL strength** — the `exit 0` leak gate covers the
`wild` block alone, and the acceptance checkbox correction is not a temporary
measure pending a compiler fix. **0.0.4's leak acceptance needs a MEMORY CAP for
the managed half in every repository**, not just in `nitpick-regex` where it has
now been added. `nitpick-time`, `nitpick-parse` and `nitpick-tui` all carry
hand-written containers of the same shape and **all three inherit this
correction at their next claim.**

**And the three probes owed at the re-pin re-ran CLEAN — which is evidence the
shape is OUTSIDE DEF-8's scope, not evidence the fix is right for it.** Those
are different conclusions and only the first is supported. This distinction is
the finding; the clean result on its own would have read as the second.

**How it got here, which is the durable part.** The premise came off this board,
went into *both* of today's dispatches in the orchestrator's own words, and was
caught only because a worker checked a premise it had been handed instead of
building on it. **A dispatch's stated premises are claims, and a worker is the
last line that can falsify them.**

**Q-10 RESIDUE — THE SWEEP CORRECTED THE PROSE AND LEFT THE ACCEPTANCE
CHECKLISTS.** *(Deliberately NOT given an `RX-` number here: `RX-121` and
`RX-122` are already allocated in `nitpick-regex/meta/DECISIONS.md` and this
board nearly took one of them. `RX-` is one repository's namespace and this
finding spans five, so each repository allocates its own number when its stream
fixes it — `nitpick-regex`'s next free is **RX-123**. `check_refs.py` returned
clean on the collision, because it catches an undefined reference and never a
re-used one.)* Found 2026-09-04 by `nitpick-libs-44`; seven live sites in five
repositories.** Every repository's narrative text now carries the correct
formulation — *D-151 counts `wild` blocks, D-188 counts live drivers, and
neither sees a managed body*. But the **checkbox a worker actually ticks** still
states the unfalsifiable gate, in all five:

| # | Site | Note |
|---|---|---|
| 1 | `nitpick-regex/meta/roadmap/0.0/0.0.4.md:113` | s1 — fix at this claim |
| 2 | `nitpick-regex/meta/roadmap/0.0/README.md:170` | s1 — **names `vec_free`**, so it asserts the gate for precisely the managed case it cannot see, in the cycle that builds `Vec<T>` and `Bytes` |
| 3 | `nitpick-time/meta/roadmap/0.0/0.0.4.md:122` | s2 — fix at this claim |
| 4 | `nitpick-tui/meta/roadmap/0.0/0.0.4.md:103` | deferred to stream 1's claim (W-7) |
| 5 | `nitpick-parse/meta/roadmap/0.0/0.0.4.md:110` | deferred to stream 2's claim (W-7) |
| 6 | `nitpick-parse/meta/roadmap/0.0/README.md:104` | deferred — **the worst instance: it cites `(D-151)` in SUPPORT of the broad claim.** A wrong citation still resolves |
| 7 | `nitpick-sockets/meta/roadmap/0.0/0.0.4.md:91` | deferred to stream 3's claim (W-7) |

**Not findings, checked:** `nitpick-regex/meta/DECISIONS.md:539` quotes the false
form and immediately corrects it; `nitpick-time/…/0.0/README.md:83` is about
probe comments; `nitpick-tui/…/0.13/README.md:48` is a different sense of "leak".

**Why the sweep missed them, which is the durable part.** `nitpick-regex`'s
`meta/DECISIONS.md:550` records that its site list was *"produced by `git grep -n
'D-151'` and not from recall"* — the right instinct, and it still under-counted,
because **five of these seven checklist lines do not cite D-151 at all**. That
repository's own correction note says "four sites stated, and two more implied";
the tree holds two more it never saw. A generating command is only as wide as
its pattern, and the prose was corrected *because* the prose is where the
citations live.

**This is the fifth instance of the shape** `PLAYBOOK.md` §6 names — a check
whose NAME describes the property while its MECHANISM covers something
narrower — and the first found in **acceptance criteria** rather than in prose,
which is the worse place for it: prose is read, a checkbox is ticked.
**And the finder's own first sweep was short by one** (site 6), by filtering out
every line that mentioned D-151 on the assumption that citing it meant being
qualified. Three phrasings were needed. **Fix each at its own stream's claim
(W-7); do not fix another stream's repository.**

**Q-8 — answered 2026-09-03 by the author: O-N9 is BLOCKING**, like O-N4 —
**against the recommendation on this board**, which read it as conformance
rather than a block. Recorded as an override because that is what this table
is for. The reason it is defensible: a rule enforced only by a harness check
the library writes for itself is a thin guarantee for a use-after-free, and it
protects no consumer. So `src/fmt/` work waits for the compiler, probes 09 and
10 are held, and the `SAFETY.md` rule and `check_no_view_returns` are kept as
a belt rather than as the guarantee. **Cheaper than it looked when decided:**
the compiler session has since scheduled the fix as DEF-3 in 1.5.1b, in the
same batch as O-N4's, hours out.

---

## Claim protocol

1. The orchestrator writes `CLAIMED sN` against the **repository** in its
   stream table — a stream owns the whole repository while it works on it
   (W-7) — and a row in the in-flight table naming the subcycle, the agent
   label (`s<N>-<pkg>-<cycle>.<sub>-<HHMM>`), the time and the model. One
   commit: `board: claim <repo> <cycle>.<sub> for sN`.
2. One worker works that subcycle (W-15). When it reports, the verifier runs
   (W-21).
3. On PASS the in-flight row advances to the next subcycle. At a cycle's
   close the claim advances to the repository's next cycle if its gate is
   ready, else to its next ungated cycle (W-9), else it is released and the
   row removed: `board: release <repo>`. Then check whether any `BLOCKED`
   row just became free.
4. A claim with no live agent in the current session is stale — the
   orchestrate skill's recovery procedure runs before any dispatch (W-19).

**A claim is a commit.** The history of this file is the record of who worked
what and when, which is the thing the compiler's R8 says the orchestrator owns.

---

**EVERY `SAFETY.md` PATH IN THE STREAM TABLES BELOW WAS WRONG, IN ALL FIVE
ROWS, AND THE LINE NUMBERS WERE RIGHT — WHICH IS WHY NOBODY CAUGHT IT.**
Corrected 2026-09-05. The board said `specs/SAFETY.md:NN`; the file is
`meta/specs/SAFETY.md:NN` in **all five libraries**, checked one at a time
rather than inferred from the first. Eight occurrences across five lines — and
note `grep -c` reports **5**, because it counts *lines* and not *matches*,
which is the denominator lesson arriving in the instrument used to measure the
denominator.

**Why it survived: the wrong half was the half nobody verifies.** A line number
is obviously a thing to re-check and gets re-checked; a directory prefix reads
as part of the file's name and is copied forward. A worker following one of
these would have found no file at all — the *lucky* failure, since the
unlucky one is a path that resolves to something else. **A citation is a path
AND a line, and this ecosystem has been re-deriving line numbers while
copying paths.**

**AND TWO ITEMS WERE LISTED AS OWED AFTER THE TREE HAD ALREADY DISCHARGED
THEM** — `nitpick-time`'s RX-111 and its two lagging leak-gate sites, both
found by the 0.0.2 worker checking its inherited NOTES against the files
instead of working from them. **This is the opposite staleness from the kind
this board guards against.** Every check here asks *"is a claimed fix real?"*;
nothing asks *"is a claimed debt still owed?"* — and that direction costs a
whole dispatch, silently, because re-fixing a fixed thing looks exactly like
work. `nitpick-regex`'s RX-111 is likewise discharged. **Three genuinely
remain: `nitpick-tui`, `nitpick-parse`, `nitpick-sockets`.**

---

## SHARED FINDINGS — what `nitpick-time` learned that the siblings probably inherit

**Four things, found in three consecutive subcycles, and the reason they are
shared is the same in every case: these repositories were scaffolded from one
template, so a defect in the template is a defect in five trees.** Stated once
here with its evidence rather than pasted into five rows — this board already
carries `RX-120` verbatim four times, and text copied five ways is text that
drifts. **Each is carried into that repository's next dispatch by the
orchestrator; none is fixed in another stream's repository (W-7).**

**None of these blocks anything today.** Every one of them is a plan or a
document that will fail *when executed*, which is precisely why they are worth
carrying now rather than meeting one at a time.

| # | Finding | Who it hits | What to check, in one command |
|---|---|---|---|
| **1** | **TM-114 — `BUILD.md` §3's stage table is incomplete.** It was missing the compiler's **default `compile` stage** and assigned `tests/conformance/` to **`accept`** — *"accepted in silence"*, which is the O-N11 shape: a root with `main` and no `failsafe` is accepted at `npkc` exit 0 and refused only later | **all four siblings**, template-shared | Does your §3 carry a `compile` row, and what stage is `tests/conformance/` on? |
| **2** | **TM-117 — separate compilation DOES NOT EXIST, and this is the documented model rather than a defect.** Two `npkc`-produced objects are a duplicate-symbol error (`ld.lld` exit 1, 121 lines) because every compile emits the whole reachable graph **including the prelude**. `BUILD_REFERENCE` §4.1 at the pin: *"takes one program object and adds the runtime object; there is no parameter through which a third input could enter"* | **any sibling whose harness plan says "compile the library once, link each program against it"** — it is the natural decision to write, and `nitpick-time`'s P-16 said exactly that | `grep -n 'once' meta/roadmap/0.0/0.0.2.md` — a plan naming one library object cannot be executed as written |
| **3** | **The compiler's frontend tools are `.npk` SOURCE, not binaries.** `tools/parse_check.npk` imports twenty frontend modules and `tools/check.npk` the whole driver pipeline, so *"build the compiler's tools once per run from the pinned checkout"* means **building the compiler**, from a tree routinely ahead of our pin | **any sibling naming `tools/parse_check` or `tools/check` in a harness plan** | `git grep -n 'parse_check\|tools/check' -- 'meta/'` |
| **4** | **`NITPICK-REACH-003` LISTS THE IDENTITIES OWED — an OPPORTUNITY, not a defect.** Compile a program importing one module with no `failsafe` and the refusal names **every arm a consumer of that module will owe** | **every library with an error budget** — all five | Verified in `nitpick-time` both directions on three specimens: floor **4**, `arms_lib` **5**, `calc_lib` **8** |

**On #2, the framing matters more than the fact.** *"`npkc` has no separate
compilation"* is true and points at the compiler. *"Our plan assumed a model
the compiler never offered"* is also true, points at the plan, and is the only
one of the two that can be acted on. The compiler session confirmed it is not
a defect and **offered to put separate compilation to the author as a design
row if the libraries need it** — this workbench answered **not yet**, because
1.5.2d's step 2 removes ~94% of the cost that would motivate the ask. Re-pin,
re-measure, then decide. The offer is on the record and does not expire.

**On #4, the trap inside the opportunity:** the identity count is **per
program** — the same diagnostic names **four** identities for one fixture and
**six** for another, differing by an import and some arithmetic. This board
once generalised one program's floor to the set and cited the compiler's own
output for it. Read each program's own bill.

**And the substitute for #3 is better than the thing it replaces.** `npkc` has
no parse-only mode, but **a diagnostic's CODE FAMILY answers the question**:
LEX and PARSE are the parse phase and every other family is later, so **a file
refused at TYPE, BORROW or REACH necessarily parsed.** No extra tool, no build,
and it reads the compiler's own classification instead of reimplementing it.

**`nitpick-posix` IS A SIXTH TREE AND IS NOT EXEMPT — it is only out of
reach.** It lives in `../nitpick-apps/`, outside this workbench's write scope,
so nothing here may touch it; but it was scaffolded the same way, so **findings
1 and 3 plausibly apply to it and finding 4 certainly does** (it consumes three
of these libraries, so it owes their arms). **Say so at stream 3's claim rather
than letting the five-row table imply it was checked.** The table above lists
five because five is what this workbench can write to, and a scope boundary is
not a clean bill of health — which is exactly the *"a check whose name
describes the property while its mechanism covers something narrower"* shape
this ecosystem keeps meeting, arriving this time in a table's row count.

**Still outstanding from earlier sweeps, unrelated to the four above but owed
by the same three repositories:** `RX-111`'s false bounds promise remains in
**`nitpick-tui`** (`meta/specs/SAFETY.md:24`), **`nitpick-parse`** (`:22` — the
worst instance, since a parser's index is attacker-influenced) and
**`nitpick-sockets`** (`:28`). `nitpick-time` and `nitpick-regex` are
discharged, verified by reading.

---

## Stream 1 — text

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-regex` | 0.0 … 1.0 (16) | `CLAIMED s1` | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent; nothing gates it. **RX-111 found and already corrected here — its `SAFETY.md:20` and Rule S-23's per-type table are the wording the other four take.** **Q-10 sweep — the leak gate that cannot fail:** 4 sites — `0.0/README.md:130`, `0.0/0.0.4.md:14`, `meta/specs/SAFETY.md:25`, `0.0/0.0.0.md:314`. Fix at this stream's claim |
| 2 | `nitpick-tui` | 0.0 … 1.0 (18) | — | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent. **RX-120 — the undefined-symbol scan this repository's `BUILD.md` plans CANNOT SEE A SYSCALL** (measured in `nitpick-regex`, independently reproduced: 29 symbols each way, diff empty, because `npk_sys6` is already the prelude's). Replace it with an **IR call-edge scan**, which does distinguish them. Treat the acceptance item naming the symbol diff as unmet.  Inherits stream 1's Unicode approach from `nregex`. **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `meta/specs/SAFETY.md:24`, "An out-of-range cell index is a *crash*, not a smear". **Q-10 sweep — the leak gate that cannot fail:** 5 sites — `0.0/README.md:125`, `0.0/0.0.4.md:16`, `meta/specs/SAFETY.md:27,216`, `0.0/0.0.0.md:353`. Fix at this stream's claim |
| 3 | `nitpick-logview` | — | `BLOCKED on nitpick-tui 0.14` | repository not created; created at `ntui` 0.15's open (T-115) |

## Stream 2 — data

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-time` | 0.0 … 1.0 (10) | `CLAIMED s2` | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent. **RX-120 — the undefined-symbol scan this repository's `BUILD.md` plans CANNOT SEE A SYSCALL** (measured in `nitpick-regex`, independently reproduced: 29 symbols each way, diff empty, because `npk_sys6` is already the prelude's). Replace it with an **IR call-edge scan**, which does distinguish them. Treat the acceptance item naming the symbol diff as unmet.  **~~RX-111~~ — DISCHARGED HERE, verified by reading 2026-09-05.** `meta/specs/SAFETY.md:315` now reads *"An out-of-range read is **a wrong value**, not a crash"* and `:332` *"**An unchecked index is a WRONG ANSWER, not a crash**"*. The board carried it as outstanding after it had been fixed, and would have dispatched it a second time. **`nitpick-regex` is likewise discharged** (`:269`). **Three remain: `nitpick-tui`, `nitpick-parse`, `nitpick-sockets`** — checked individually, not inferred from this one. Smallest first item; finishes early and can take slack. **Q-10 sweep — the leak gate that cannot fail:** **DISCHARGED IN FULL, verified by reading 2026-09-05** — the specs, `DECISIONS.md` and `0.0.4.md` already carried it, and the two that were listed as lagging (`0.0/README.md:100`, `0.0/0.0.0.md:299`) **do carry the correction too**: `0.0.0.md` now reads *"Exit 0 means 'no `wild` allocation is live' (D-151) — that, and nothing more"*. **Nothing outstanding here.** Both this and RX-111 above were listed as owed after the tree had discharged them, found by the 0.0.2 worker checking its inherited NOTES against the files rather than working from them — **a board that is stale in the "still owed" direction costs a whole dispatch, and nothing in this ecosystem checks for it** |
| 2 | `nitpick-parse` | 0.0 … 1.0 (15) | — | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent. **RX-120 — the undefined-symbol scan this repository's `BUILD.md` plans CANNOT SEE A SYSCALL** (measured in `nitpick-regex`, independently reproduced: 29 symbols each way, diff empty, because `npk_sys6` is already the prelude's). Replace it with an **IR call-edge scan**, which does distinguish them. Treat the acceptance item naming the symbol diff as unmet.  **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `meta/specs/SAFETY.md:22` says "Indexing is bounds-checked and traps ... An index derived from input is a *crash*, not a smear". **The worst instance in the ecosystem** — a parser's index is attacker-influenced by definition, so this is a security claim and it is wrong. **Q-10 sweep — the leak gate that cannot fail:** **the worst case, 9 sites** — `0.0/README.md:104,135`, `0.0/0.0.4.md:20`, **`0.4/README.md:43`**, `meta/specs/SAFETY.md:35,237,283`, `specs/VALUE_MODEL.md:214`, `0.0/0.0.0.md:354`. It is a parsing library, so managed bodies are everywhere and `string_slice` allocates (D-186); `0.4/README.md:43` puts the false gate on `doc_destroy`, which is exactly an owning structure D-151 cannot see. Fix at this stream's claim |
| 3 | `nitpick-conflint` | — | `BLOCKED on nitpick-parse 0.11` | repository not created; created at `nparse` 0.12's open (PA-103) |

## Stream 3 — system

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-sockets` | 0.0 … 1.0 (12) | — | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent. **RX-120 — the undefined-symbol scan this repository's `BUILD.md` plans CANNOT SEE A SYSCALL** (measured in `nitpick-regex`, independently reproduced: 29 symbols each way, diff empty, because `npk_sys6` is already the prelude's). Replace it with an **IR call-edge scan**, which does distinguish them. Treat the acceptance item naming the symbol diff as unmet.  **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `meta/specs/SAFETY.md:28` says an out-of-range `sockaddr` read is "a *crash*, not a leak of adjacent memory" — a claim that there is no information disclosure, and it is wrong. **Q-10 sweep — the leak gate that cannot fail:** 5 sites — `0.0/README.md:134`, `0.0/0.0.4.md:14`, `meta/specs/SAFETY.md:26`, `specs/VERIFICATION.md:48`, `0.0/0.0.0.md:328`. Its `ANCILLARY_MODEL.md:67` and `SAFETY.md:221` are correctly scoped already ("takes no `wild` bytes") and are the model for the rest. D-188 covers the driver/process registry, not managed bodies. Fix at this stream's claim |
| 2 | `nitpick-posix` | 0.0 … 1.0 (14) | — | **Q-10 sweep — the leak gate that cannot fail:** 2 sites, both in `0.0/0.0.0.md:37,226` (`nitpick-apps/nitpick-posix`, outside this workbench's write scope). **O-N6 answered 2026-09-03 by probe 02** — negatively, and the repository absorbed it (PX-100: `failsafe` is generated). W-1 is discharged. Nine of its cycles are ungated and are the slack this stream uses when a gate is not ready. **Q-1 answered 2026-09-03:** POSIX.1-2024 (Issue 8) is current and its utility table moved by 19 entries — the first worker here files the digest and amends `SCOPE.md`, `CONFORMANCE.md` K-1 and `GLOSSARY.md`; the syntax guidelines are unchanged |

---

## The cross-stream gates

Each is mutual (W-3): the utility needs the library finished, and the library's
dogfood cycle needs the utility written **and used**.

| Gate | Needs | Blocks | Expected around |
|---|---|---|---|
| `nitpick-posix` 0.5 — `grep` | `nitpick-regex` closed | `nitpick-regex` 0.14 | s1 unit 16 ↔ s3 unit 17 |
| `nitpick-posix` 0.7 — `date`, `crontab` | `nitpick-time` closed | `nitpick-time` 0.7 | s2 unit 10 ↔ s3 unit 19 |
| `nitpick-posix` 0.11 — `awk` | `nitpick-parse` **and** `nitpick-regex` closed | — | s2 unit 25 ↔ s3 unit 23 — **tight; see below** |
| `nitpick-logview` | `nitpick-tui` closed, `nitpick-regex` closed | `nitpick-tui` 0.15 | s1, internal |
| `nitpick-conflint` | `nitpick-parse` closed | `nitpick-parse` 0.12 | s2, internal |

**The one tight gate.** `awk` wants `nparse` at about the moment stream 2 is
still finishing it. If stream 3 arrives first it takes `nitpick-posix` 0.12
(terminal, archive, compare) out of order — it is ungated — and returns to
`awk` after. W-9 is the rule; this is the case it was written for.

---

## Compiler dependencies

Nothing here blocks implementation. Recorded so that a stream reaching its
hardening cycle knows what it is waiting for. The ids are the workbench
registry's ([`meta/OPEN_QUESTIONS.md`](meta/OPEN_QUESTIONS.md) §"For the
compiler"), because `O-N` numbers are per repository and collide.

| Compiler | Needed by | State |
|---|---|---|
| 1.5.1 – 1.5.4 (verification surface) | every library's hardening cycle | compiler at 1.5.0 |
| **1.5.1b — the workbench's three defects** | `nitpick-time` 0.0.5, 0.5 and all `src/fmt/` work | **PLANNED AND RATIFIED 2026-09-03**, `meta/roadmap/1.5/1.5.1b.md` at the compiler's `4bf3e47`. Five commits: DEF-2 (our O-N8) first because it is independent, DEF-3 (our O-N9), DEF-1's three backend text builders (our O-N4), then **D-246** statement-end temporaries and **D-247** `List<T>` as owning — plus a **step 0** that builds `NPK_HEAP_STATS`, an allocator-level instrument for **managed** memory (allocated, peak_live, count), and a `cost` harness stage. Step 0 is the instrument this workbench's 0.0.4 gate needs and does not have (Q-10): run on our own two container probes it reports **peak_live 41 321 bytes against 400 101 320**, the pair that both exited 0. Starts when 1.5.1's last four steps land. **IN FLIGHT 2026-09-03 22:40. 1.5.1 is CLOSED and pushed (compiler `main` `e668f6a`).** 1.5.1b runs as cumulative prefixes, each in its own worktree behind a full ~3 h harness that must be green before it lands: **step 0** (the instrument, the `cost` stage, DEF-1's recipes and the baseline) committed, harness from 21:34; **step 1** (DEF-2, D-248) committed, harness from 22:05; **step 1b** (DEF-5) committed, harness from 22:11; **step 2** (DEF-3, D-249) written, its checker sweeping the compiler's own `src/` now. Steps 3 (the builders), **3b (DEF-4, now D-250)**, 4 (D-246) and 5 (D-247) follow, then the snapshot refresh and the landing message. Order confirmed: DEF-2 → DEF-3 → DEF-1 → D-246 → D-247, with 3b inserted between the builders and D-246. 1.5.1's four prefix harnesses are at the parity stage; step 0 is being built in a detached worktree, and **its first self-build found a defect in the instrument itself** (the exit-time report walked a heap-resident environment slice after the compiler's wholesale release), being fixed there — so 0.0.4's `peak_live` gate must be commissioned against a known-leaking and a known-clean control before it is trusted (Q-10). The compiler session messages this workbench at the landing with the commit, whether `build/` was written after it, and the after-numbers on our own recipes |
| **D-248** (`mod:` header mandatory and first; `main`/`failsafe` root-only) | every library, at the re-pin | **RATIFIED**, lands in 1.5.1b. **Re-checked 2026-09-03 against a consequence we had not been told: a module name is an IDENTIFIER**, so a `.npk` file named after a reserved word, or beginning with a digit, refuses under D-248 — the compiler renamed five of its own files for this. **Swept all six repositories: zero violations**, because `nitpick-regex` had already fixed its leading-digit case at `d6fb0ce`. Any NEW file must clear `PLAYBOOK.md` §10's list. **Costs this ecosystem nothing if we keep writing as we do** — all 17 `.npk` in `nitpick-time` and all 8 in `nitpick-posix` already comply. See `PLAYBOOK.md` §2 |
| **D-249** (the `Views` column) | the fix behind DEF-3 / O-N9 | **RATIFIED**, lands in 1.5.1b |
| **O-N12** (`>>>` and `string_repeat` documented and absent) | nobody — W-27: blocks nothing, both have substitutes | **SETTLED 2026-09-03 the way this workbench recommended — documents, not implementation** — landing inside 1.5.1b step 2's commit. The `>>>` row is gone and the `>>` row now states the rule that makes the table make sense: *arithmetic on a SIGNED operand, logical on an UNSIGNED one; the operand's signedness decides*, confirmed against the single shift arm in their emitter. `BUILTIN_REFERENCE` §2's "fast compiler intrinsics" sentence — the actual trap — now says none of those names resolves without a row in a marked table. `string_repeat` stays listed as planned library surface at this workbench's recommendation: the harm was the intrinsics sentence, and **no library here plans a string-utility surface**, so nobody is on it |
| O-N2 (`npkg` builds a library) | retiring six Python harnesses | **not on the compiler's 1.5 or 1.6 map** — a request, not a date |
| O-N1 (`clone_exec` signal mask) | `ntui` 0.1.6, cosmetically | request raised |
| O-N5 (`npkg` multi-artifact) | `nitpick-posix`'s build | request raised |
| ~~O-N6~~ (macro splices a `pick`) | `nitpick-posix`'s **shape** | **ANSWERED 2026-09-03: no.** Probe 02, seven programs. A macro is not shareable across modules at all (`MACRO-007`); `failsafe` is generated instead (PX-100). Shape changed, schedule did not |
| ~~**O-N4**~~ (`npkc` quadratic in one declaration's size) — **DISCHARGED, verified here** | **blocks nothing now.** It did block `nitpick-time` **0.0.5** (the tzdb size spike must compile a real emitted table) and **0.5** (the generator). TM-007's tzdb is 26 838 rows and the measured 281 s / 30.9 GiB is `probe04`'s **30 000** (`[30000 x ZoneTransition]` in the emitted IR) — the two counts had been conflated here and in `RECORD.md:2275`; the probe is the larger, so no conclusion moves, so a 16 GiB machine and CI cannot build the library in its shipping shape, and every consumer pays it. It does **not** block 0.0.1–0.0.4, which carry no large declaration | **DISCHARGED — VERIFIED HERE 2026-09-04 12:27, on this workbench's own measurement against pin `94874ce`, not on the correspondent's report.** Both recipes, three runs each, `/usr/bin/time -f "%e s  %M KiB" $NPKC <file> -o <out>.ll` — the command `tests/probe/defect/README.md:196` records for the before-numbers. `big_fixed_array_cost.npk` (4 000 rows): **0.24–0.25 s at 28 768–28 960 KiB**, was 5.30–6.19 s at ~593 592–593 992 KiB. `probe04_big_fixed_table.npk` (30 000 rows): **1.19–1.32 s at 74 936–74 996 KiB**, was 281 s and 30.9 GiB — **~430× less peak and ~227× less time**, against a reported 1.15 s / 75.2 MB, which this reproduces. The relation is no longer quadratic: 7.5× the rows costs 5.0× the time and 2.6× the peak (quadratic would be ~56×). **And the speed is not bought by emitting less** — the check that would have made this a hollow green. `npkc` exit 0 was paired every run with an `.ll` actually written (2 672 442 bytes), carrying `@"npk.probe04_big_fixed_table.TRANSITIONS" = constant [30000 x …]` with **30 000 `i64` rows present**; `llc -filetype=obj` then **accepts** it (exit 0, 0.61 s, 660 360 B), and the symbol lands in **`.rodata`, flags `A` and not `W`, size 0x75300 = 480 000 B = 30 000 × 16** — which independently re-confirms **S-19** (`fixed` module state is read-only, no startup initialisation). The `llc` leg was run because *`npkc` exit 0 is not well-formedness* — O-N11 is precisely that shape — so a discharge measured on `npkc` alone would not have been one. Instrument commissioned first, positive and negative: a real tree file (`probe11d_floor_only.npk`) exit 0 with an `.ll`, and a malformed file exit 1 with none. **`nitpick-time` 0.0.5 and 0.5 are UNBLOCKED.** History: | **BISECTED 2026-09-03** — the frontend is *linear* on all three axes; the quadratic is three text builders in `src/backend/` that re-concatenate an accumulator per element, per trap site and per byte, compounded by D-183's never-dropped owning temporaries. Neither of the workbench's two relayed hypotheses (identifier length, then total source bytes) survived measurement. Scheduled in **1.5.1b**. **ACCEPTED 2026-09-03** by the compiler session, which owns `npkc`'s frontend. Recorded there as **DEF-1** (`meta/roadmap/OPEN_DECISIONS.md` §2f) with our numbers, controls and the exit-0 discipline. Proposed: a dedicated subcycle **1.5.1b** after 1.5.1 closes and before 1.5.2, one commit per defect under a full harness, **measured before it is touched so the fix is a number**, `big_fixed_array_cost.npk` as the regression case. Cause not yet confirmed and deliberately not guessed. **The schedule is the author's call.** That session messages us when 1.5.1b opens and again with the re-pin commit |
| **O-N14** (no library object: `@npk_failsafe` called, never declared) · **O-N13** (a `pub use` silently downgraded) | **O-N14 blocks** per-module objects and separate compilation as `BUILD_REFERENCE` §4.1 documents them, **for every library here**; inconveniences 0.0.2's harness and one symbol scan. **O-N13 blocks nothing** but costs each person who meets it, and six umbrella modules are planned | **BOTH ACCEPTED 2026-09-04 and taken into 1.5.1b as step 3c**, after 3b. Verified on the compiler under test there: a non-root module carries seven `call i32 @npk_failsafe(...)` and no `declare`, and the root defines it — **so the fix is the one this workbench proposed: a unit that does not define it declares it.** Better than the ask, step 3c also adds an **`object` stage to both runners** whose units are non-root modules compiled to objects that `llc` must accept, **including a comment-only one — our `core` shape** — so §4.1's model is *measured on every run* instead of documented. O-N13's fix upgrades the prior binding's visibility when a repeated import carries `pub`, so the two orders mean the same thing, with a positive resolve unit shaped on our §E2/§E3 contrast |
| **O-N11** (`main` without `failsafe` compiles at exit 0; the arm contract is discharged by deleting the handler) | **nobody — W-27: blocks nothing here.** Every program this library ships has a handler, and `llc` catches a missing one in the next step of the same recipe. It **inconveniences** cycle 0.0.3's harness, which must stop reading `npkc` exit 0 as "well-formed" and gains an eighth selfcheck case. It does **not** touch the arm contract where a handler exists | **ACCEPTED 2026-09-03 as the compiler's DEF-5, committed at step 1b, harness running from 22:11. The diagnostic is `NITPICK-REACH-003` at `main`, listing every identity the handler owes** — **the count is NOT six.** This board carried six from the compiler session's message; `case1` has no import, no arithmetic and no allocation, so its bill is S-4b's floor of **four** — `Unreachable`, `HeapOom`, `HeapBadRequest`, `WildLeak`. Under verification, and deliberately written into no repository document: the worker recorded the diagnostic's shape and left the numbers to the re-pin, which is right for a number nothing yet depends on. That is the after-value our two transcripts must record at the re-pin., at our `b092a9e`, and taken into 1.5.1b immediately after step 1 (D-248), whose whole-graph pass over the root's declarations this is the missing question of. **The ask was granted in full:** the refusal lands at `main` and the diagnostic LISTS the identities the absent handler would owe. A root with neither `main` nor `failsafe` stays legal; a `failsafe` outside the root is refused by step 1. **Exposure measured across all six repositories: three files, every one a negative probe, no live code** — `nitpick-time`'s two DEF-5 reproductions, whose transcripts must be re-recorded at the re-pin (an `npkc` refusal replaces today's `llc` failure), and `nitpick-posix`'s `probe02g`, already refused at `MACRO-007`. Independently verified before it was sent. `npkc` accepts a root file with `main` and no `failsafe` at exit 0, emitting IR whose trap paths call an undefined `@npk_failsafe`; only `llc` refuses it, against the compiler's own D-013. **The quiet half is the serious one:** `reach_settle` returns early at `failsafe_decl == 0`, so the whole REACH-002 contract is enforced against programs that HAVE a handler and asked of nothing that has none — the same shape as O-N10, where the silent half mattered more than the refusal. The ask includes the diagnostic naming the arms the absent handler would owe, which `reach_settle` has just computed at the line where it returns early |
| **O-N10** (`derive` on a payload enum: refused, or silently tag-only) | nobody yet — `nitpick-time` exposes one payload enum and no rule needs a derive on it. **Blocks the first library that wants one** | **ACCEPTED as DEF-4, then WIDENED after measurement: ratified as D-250, step 3b.** It is not only payload enums — a derived `Eq`/`Ord` over a **struct with a derived-struct field** fails the same way inside `<derived-1>`, so step 3b covers named types in structs and enums alike, and an owning payload will refuse the derive **by name** rather than silently generate. **RAISED 2026-09-03, and ACCEPTED as the compiler's DEF-4** at our commit `eb8d6b4`, with a step proposed in 1.5.1b awaiting the author's ratification; it does **not** displace the DEF-2 → DEF-3 → DEF-1 order, so all four of this workbench's defects may land in one batch. `#[derive(Eq)]` is `NITPICK-TYPE-034`; `#[derive(Ord)]` compiles and reports `Literal(7)` equal to `Literal(9)`. The quiet half is the serious one. No file in the compiler's tree derives on a payload enum, so the gap is coverage; the ask includes a test there. Not blocking, so no author decision is pending |
| **O-N9** (D-004's escape rule unenforced for slice views) | `nitpick-time` in principle — every `src/fmt/` parser takes a `uint8[]` — and **BLOCKING by the author's ruling** — `src/fmt/` work and probes 09/10 wait for the compiler; the house rule "a view is a parameter, never a return value" is kept as a belt, not as the guarantee | **RAISED 2026-09-03.** `string_bytes(local)` returns a view that outlives its owner at exit 0 and reads freed memory; `@`-borrows in the same position are refused, so the rule is documented and under-enforced for one type. **Q-8: the author ruled it BLOCKING.** Accepted by the compiler as **DEF-3**, second of 1.5.1b's five commits — the borrow walk learns that a view-maker's result borrows its operand. The analyses currently name neither `string_bytes` nor `string_from_bytes`; the only view they know is the range-view `arr[lo...hi]`. **Two shapes DEF-3 distinguishes that our own six cases did not, and `src/fmt/` planning turns on them:** a view of a **temporary** — `string_bytes(string_concat(a, b))` returned — is refused outright as **`NITPICK-BORROW-012`** — **real, but NOT in the pinned toolchain**: DEF-3's step 2 allocates it and it lives only in the compiler's unlanded step-2 worktree, so grepping `950bb1d` for it finds nothing. This board briefly said the code did not exist, on exactly that grep; the pin proves "not landed", never "not real" (`PLAYBOOK.md` §6). **Why it needed a new code at all, which the plan had not known:** DEF-3's other refusals are all shaped like "as if `@` had been written at that argument" and are `BORROW-001`/`002`, but `@` of a temporary cannot be spelled, so no existing code's text is true of it and tracking it would need a root with no name — bind the intermediate first, after which the view is an ordinary borrow of that binding (and note it is doubly wrong today, since the `string_concat` temporary also leaks under D-246); but a view whose root is a **pointer-shaped binding** (a wild pointer, a slice, a cstring) is the *pointee's* borrow rather than a frame borrow — **and note which rule is which: TODAY's live mechanism is `borrows_only_param_rooted` (`escape.npk:507`), rooted at a PARAMETER, so "views are never returned" is already stricter than the language before DEF-3 lands; the pointer-shaped-root formulation is what DEF-3 introduces**, so `string_from_bytes(buf, n)` over an alloc'd block, returned, **stays legal**. So `nitpick-time`'s house rule "a view is a parameter, never a return value" is CONSERVATIVE, not the truth: it was written with no way to tell those apart. **Three further refinements from step 2's first whole-tree sweep, which found eight sites and refined the rule three times:** a view over `#ptr_add` **looks through to the pointer**; a `for` over a range **cannot carry a borrow whatever its bound reads**; and a struct literal is **rooted where its field values are**. The rooting checks now share one walk with the classifier. All three bear on `src/fmt/` and none is in our six cases |
| **O-N8** (`mod:`/basename mismatch merges two files) | nobody — raised for correctness | **ACCEPTED 2026-09-03** as the compiler's **DEF-2**, same §2f, same owner and same 1.5.1b slot. Emits two `define i32 @main` at exit 0 and `llc` refuses the IR; the `NITPICK-RESOLVE-005` diagnostic for the same rule already exists and simply is not applied here. Costs `ntime` nothing |

---

## Ready to start now

Independent of everything, roughly a day each, and each converts an unknown
into a fact (W-14):

- [x] `nitpick-posix` 0.0.0 **probe 02** — gated a fourteen-cycle repository; ran 2026-09-03, negative, absorbed
- [ ] `nitpick-regex` 0.0.0 probes
- [~] `nitpick-time` 0.0.0 probes — **nine worked, two held; four stops (~~O-N4~~ **discharged and verified here 2026-09-04**; O-N9, O-N10, O-N11 landed at the pin, not yet measured here).** 01–08 accepted with twins and verified PASS at `9113487`; **11 worked** — six programs, three defect cases and a support-module control — and produced the fourth stop; **09 and 10 held for 1.5.1b** by the author's ruling on O-N9, so the subcycle cannot close until the re-pin
- [ ] `nitpick-sockets` 0.0.0 probes
- [ ] `nitpick-parse` 0.0.0 probes
- [ ] `nitpick-tui` 0.0.0 probes
