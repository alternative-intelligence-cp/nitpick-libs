# The board

**Live state.** What each stream is working on, what is claimed, what is
blocked, what is done. The durable plan is
[`WORKSTREAMS.md`](WORKSTREAMS.md); the past is [`RECORD.md`](RECORD.md).

> **The orchestrator owns this file** (W-8). An agent working a stream does not
> edit it — the orchestrator claims before a worker is dispatched and releases
> when the stream leaves the repository. That is what keeps two agents out of
> one repository and removes every merge conflict by construction.

**Last updated:** 2026-09-03 · **Width:** 2 — streams 1 and 2 ·
**Toolchain:** 950bb1d · .internal/toolchain/950bb1d/ · pinned 2026-09-03
**Workbench writer:** `3e1777c3-c237-4c90-920c-a4a6b9df1e66` — session
`nitpick-libs-88`, the second orchestrator, took the lock 2026-09-03 20:56.
**Not a takeover:** the line read `none`, released at a clean stop by
`6fb2f48d-250b-4880-879f-083132155bd9`, with nothing in flight and no claim
holding a live agent. Taken board line first, then the marker file — the order
the guard enforces, and the reverse of what orchestrate §2.1 still says, which
is a live finding against 0.2.2. One writer here (W-16, P-19).
**Phase:** cycle 0.2's dry run one is under way — `nitpick-time` 0.0 is the
first library cycle to be worked, and the loop is being judged against
[`meta/roadmap/0.2/0.2.7.md`](meta/roadmap/0.2/0.2.7.md) §2's pass mark.

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
| s2 | `nitpick-time` | 0.0.0 — record and specification debts | `s2-ntime-0.0.0-2315` | 2026-09-03 23:15 | `claude-opus-5` | **Still STOPPED on O-N4, O-N9, O-N10, O-N11 — all four in 1.5.1b — and this dispatch does not touch any of them.** It clears the debts that do NOT need the re-pin, so that when the landing message arrives the next dispatch is probes 09/10 and the transcript re-recording and nothing else: **RX-111**'s false bounds promise at `specs/SAFETY.md:21`; the O-N10 and O-N11 *(provisional)* hedges, now that both numbers are allocated and accepted as DEF-4/D-250 and DEF-5; a 0.0.2 checklist line for the nine-probe leak-comment residue; and the record that the house view rule is **conservative rather than true**, which `src/fmt/` must not be planned against. **Still owed at the re-pin:** probes 09 and 10, and re-recording `missing_failsafe`'s two transcripts to `NITPICK-REACH-003` |
| s1 | `nitpick-regex` | **0.0.1 — the skeleton** | `s1-nregex-0.0.1-2315` | 2026-09-03 23:15 | `claude-opus-5` | **0.0.0 DONE and VERIFIED PASS** at `9b80d69` — the ecosystem's first completed subcycle. 23 probes, 6 commits, all 23 re-run by the verifier with every exit code and diagnostic matching, and the four weightiest claims independently re-derived from the compiler's source rather than re-read. Produced **RX-111** (below), **O-N12** (sent), and `stack` for the playbook. Small debts for the next dispatch here: the record's prose says "five commits" where the list and `git log` say six, and the local `O-N1…O-N4` want renumbering to `O-C` so they stop colliding with the registry |

## Questions for the author

| # | Stream | Raised | Question | Recommendation |
|---|---|---|---|---|
| — | — | — | nothing pending | — |

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

## Stream 1 — text

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-regex` | 0.0 … 1.0 (16) | `CLAIMED s1` | independent; nothing gates it. **RX-111 found and already corrected here — its `SAFETY.md:20` and Rule S-23's per-type table are the wording the other four take.** **Q-10 sweep — the leak gate that cannot fail:** 4 sites — `0.0/README.md:130`, `0.0/0.0.4.md:14`, `specs/SAFETY.md:25`, `0.0/0.0.0.md:314`. Fix at this stream's claim |
| 2 | `nitpick-tui` | 0.0 … 1.0 (18) | — | independent. Inherits stream 1's Unicode approach from `nregex`. **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `specs/SAFETY.md:24`, "An out-of-range cell index is a *crash*, not a smear". **Q-10 sweep — the leak gate that cannot fail:** 5 sites — `0.0/README.md:125`, `0.0/0.0.4.md:16`, `specs/SAFETY.md:27,216`, `0.0/0.0.0.md:353`. Fix at this stream's claim |
| 3 | `nitpick-logview` | — | `BLOCKED on nitpick-tui 0.14` | repository not created; created at `ntui` 0.15's open (T-115) |

## Stream 2 — data

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-time` | 0.0 … 1.0 (10) | `CLAIMED s2` | independent. **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `specs/SAFETY.md:21`, "A zone-table index out of range is a *crash*, not a wrong offset". **This repository is already claimed, so its fix rides the next `nitpick-time` dispatch** rather than waiting. Smallest first item; finishes early and can take slack. **Q-10 sweep — the leak gate that cannot fail:** **furthest along — the specs, `DECISIONS.md` and `0.0.4.md` already carry the correction**; only `0.0/README.md:100` and `0.0/0.0.0.md:299` lag, and both are in the worker's NOTES now |
| 2 | `nitpick-parse` | 0.0 … 1.0 (15) | — | independent. **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `specs/SAFETY.md:22` says "Indexing is bounds-checked and traps ... An index derived from input is a *crash*, not a smear". **The worst instance in the ecosystem** — a parser's index is attacker-influenced by definition, so this is a security claim and it is wrong. **Q-10 sweep — the leak gate that cannot fail:** **the worst case, 9 sites** — `0.0/README.md:104,135`, `0.0/0.0.4.md:20`, **`0.4/README.md:43`**, `specs/SAFETY.md:35,237,283`, `specs/VALUE_MODEL.md:214`, `0.0/0.0.0.md:354`. It is a parsing library, so managed bodies are everywhere and `string_slice` allocates (D-186); `0.4/README.md:43` puts the false gate on `doc_destroy`, which is exactly an owning structure D-151 cannot see. Fix at this stream's claim |
| 3 | `nitpick-conflint` | — | `BLOCKED on nitpick-parse 0.11` | repository not created; created at `nparse` 0.12's open (PA-103) |

## Stream 3 — system

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-sockets` | 0.0 … 1.0 (12) | — | independent. **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `specs/SAFETY.md:28` says an out-of-range `sockaddr` read is "a *crash*, not a leak of adjacent memory" — a claim that there is no information disclosure, and it is wrong. **Q-10 sweep — the leak gate that cannot fail:** 5 sites — `0.0/README.md:134`, `0.0/0.0.4.md:14`, `specs/SAFETY.md:26`, `specs/VERIFICATION.md:48`, `0.0/0.0.0.md:328`. Its `ANCILLARY_MODEL.md:67` and `SAFETY.md:221` are correctly scoped already ("takes no `wild` bytes") and are the model for the rest. D-188 covers the driver/process registry, not managed bodies. Fix at this stream's claim |
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
| **O-N4** (`npkc` quadratic in one declaration's size) | `nitpick-time` **0.0.5** (the tzdb size spike must compile a real emitted table) and **0.5** (the generator). TM-007's 26 838-row table costs 281 s and 30.9 GiB, so a 16 GiB machine and CI cannot build the library in its shipping shape, and every consumer pays it. It does **not** block 0.0.1–0.0.4, which carry no large declaration | **BISECTED 2026-09-03** — the frontend is *linear* on all three axes; the quadratic is three text builders in `src/backend/` that re-concatenate an accumulator per element, per trap site and per byte, compounded by D-183's never-dropped owning temporaries. Neither of the workbench's two relayed hypotheses (identifier length, then total source bytes) survived measurement. Scheduled in **1.5.1b**. **ACCEPTED 2026-09-03** by the compiler session, which owns `npkc`'s frontend. Recorded there as **DEF-1** (`meta/roadmap/OPEN_DECISIONS.md` §2f) with our numbers, controls and the exit-0 discipline. Proposed: a dedicated subcycle **1.5.1b** after 1.5.1 closes and before 1.5.2, one commit per defect under a full harness, **measured before it is touched so the fix is a number**, `big_fixed_array_cost.npk` as the regression case. Cause not yet confirmed and deliberately not guessed. **The schedule is the author's call.** That session messages us when 1.5.1b opens and again with the re-pin commit |
| **O-N11** (`main` without `failsafe` compiles at exit 0; the arm contract is discharged by deleting the handler) | **nobody — W-27: blocks nothing here.** Every program this library ships has a handler, and `llc` catches a missing one in the next step of the same recipe. It **inconveniences** cycle 0.0.3's harness, which must stop reading `npkc` exit 0 as "well-formed" and gains an eighth selfcheck case. It does **not** touch the arm contract where a handler exists | **ACCEPTED 2026-09-03 as the compiler's DEF-5, committed at step 1b, harness running from 22:11. The diagnostic is `NITPICK-REACH-003` at `main`, listing every identity the handler owes** — for our own `case1` that is six: the four system identities every executable carries, the user's, and `IntOverflow` from a guarded `+`. That is the after-value our two transcripts must record at the re-pin., at our `b092a9e`, and taken into 1.5.1b immediately after step 1 (D-248), whose whole-graph pass over the root's declarations this is the missing question of. **The ask was granted in full:** the refusal lands at `main` and the diagnostic LISTS the identities the absent handler would owe. A root with neither `main` nor `failsafe` stays legal; a `failsafe` outside the root is refused by step 1. **Exposure measured across all six repositories: three files, every one a negative probe, no live code** — `nitpick-time`'s two DEF-5 reproductions, whose transcripts must be re-recorded at the re-pin (an `npkc` refusal replaces today's `llc` failure), and `nitpick-posix`'s `probe02g`, already refused at `MACRO-007`. Independently verified before it was sent. `npkc` accepts a root file with `main` and no `failsafe` at exit 0, emitting IR whose trap paths call an undefined `@npk_failsafe`; only `llc` refuses it, against the compiler's own D-013. **The quiet half is the serious one:** `reach_settle` returns early at `failsafe_decl == 0`, so the whole REACH-002 contract is enforced against programs that HAVE a handler and asked of nothing that has none — the same shape as O-N10, where the silent half mattered more than the refusal. The ask includes the diagnostic naming the arms the absent handler would owe, which `reach_settle` has just computed at the line where it returns early |
| **O-N10** (`derive` on a payload enum: refused, or silently tag-only) | nobody yet — `nitpick-time` exposes one payload enum and no rule needs a derive on it. **Blocks the first library that wants one** | **ACCEPTED as DEF-4, then WIDENED after measurement: ratified as D-250, step 3b.** It is not only payload enums — a derived `Eq`/`Ord` over a **struct with a derived-struct field** fails the same way inside `<derived-1>`, so step 3b covers named types in structs and enums alike, and an owning payload will refuse the derive **by name** rather than silently generate. **RAISED 2026-09-03, and ACCEPTED as the compiler's DEF-4** at our commit `eb8d6b4`, with a step proposed in 1.5.1b awaiting the author's ratification; it does **not** displace the DEF-2 → DEF-3 → DEF-1 order, so all four of this workbench's defects may land in one batch. `#[derive(Eq)]` is `NITPICK-TYPE-034`; `#[derive(Ord)]` compiles and reports `Literal(7)` equal to `Literal(9)`. The quiet half is the serious one. No file in the compiler's tree derives on a payload enum, so the gap is coverage; the ask includes a test there. Not blocking, so no author decision is pending |
| **O-N9** (D-004's escape rule unenforced for slice views) | `nitpick-time` in principle — every `src/fmt/` parser takes a `uint8[]` — and **BLOCKING by the author's ruling** — `src/fmt/` work and probes 09/10 wait for the compiler; the house rule "a view is a parameter, never a return value" is kept as a belt, not as the guarantee | **RAISED 2026-09-03.** `string_bytes(local)` returns a view that outlives its owner at exit 0 and reads freed memory; `@`-borrows in the same position are refused, so the rule is documented and under-enforced for one type. **Q-8: the author ruled it BLOCKING.** Accepted by the compiler as **DEF-3**, second of 1.5.1b's five commits — the borrow walk learns that a view-maker's result borrows its operand. The analyses currently name neither `string_bytes` nor `string_from_bytes`; the only view they know is the range-view `arr[lo...hi]`. **Two shapes DEF-3 distinguishes that our own six cases did not, and `src/fmt/` planning turns on them:** a view of a **temporary** — `string_bytes(string_concat(a, b))` returned — is refused outright as `NITPICK-BORROW-012`, bind the intermediate first (and note it is doubly wrong today, since the `string_concat` temporary also leaks under D-246); but a view whose root is a **pointer-shaped binding** (a wild pointer, a slice, a cstring) is the *pointee's* borrow rather than a frame borrow, so `string_from_bytes(buf, n)` over an alloc'd block, returned, **stays legal**. So `nitpick-time`'s house rule "a view is a parameter, never a return value" is CONSERVATIVE, not the truth: it was written with no way to tell those apart. **Three further refinements from step 2's first whole-tree sweep, which found eight sites and refined the rule three times:** a view over `#ptr_add` **looks through to the pointer**; a `for` over a range **cannot carry a borrow whatever its bound reads**; and a struct literal is **rooted where its field values are**. The rooting checks now share one walk with the classifier. All three bear on `src/fmt/` and none is in our six cases |
| **O-N8** (`mod:`/basename mismatch merges two files) | nobody — raised for correctness | **ACCEPTED 2026-09-03** as the compiler's **DEF-2**, same §2f, same owner and same 1.5.1b slot. Emits two `define i32 @main` at exit 0 and `llc` refuses the IR; the `NITPICK-RESOLVE-005` diagnostic for the same rule already exists and simply is not applied here. Costs `ntime` nothing |

---

## Ready to start now

Independent of everything, roughly a day each, and each converts an unknown
into a fact (W-14):

- [x] `nitpick-posix` 0.0.0 **probe 02** — gated a fourteen-cycle repository; ran 2026-09-03, negative, absorbed
- [ ] `nitpick-regex` 0.0.0 probes
- [~] `nitpick-time` 0.0.0 probes — **nine worked, two held; four stops (O-N4, O-N9, O-N10, O-N11).** 01–08 accepted with twins and verified PASS at `9113487`; **11 worked** — six programs, three defect cases and a support-module control — and produced the fourth stop; **09 and 10 held for 1.5.1b** by the author's ruling on O-N9, so the subcycle cannot close until the re-pin
- [ ] `nitpick-sockets` 0.0.0 probes
- [ ] `nitpick-parse` 0.0.0 probes
- [ ] `nitpick-tui` 0.0.0 probes
