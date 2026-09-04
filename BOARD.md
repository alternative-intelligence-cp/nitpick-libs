# The board

**Live state.** What each stream is working on, what is claimed, what is
blocked, what is done. The durable plan is
[`WORKSTREAMS.md`](WORKSTREAMS.md); the past is [`RECORD.md`](RECORD.md).

> **The orchestrator owns this file** (W-8). An agent working a stream does not
> edit it — the orchestrator claims before a worker is dispatched and releases
> when the stream leaves the repository. That is what keeps two agents out of
> one repository and removes every merge conflict by construction.

**Last updated:** 2026-09-03 · **Width:** 1 — stream 2 ·
**Toolchain:** 950bb1d · .internal/toolchain/950bb1d/ · pinned 2026-09-03
**Workbench writer:** `6fb2f48d-250b-4880-879f-083132155bd9` since 2026-09-03 18:16 —
the first orchestrator session (`/npk:orchestrate width=1 start=nitpick-time
0.0.0`, cloud id `session_01FKJJPtsjVRxqDSPVsvh1nn`), which took the lock from
`0a61670c-…` after `ListAgents` showed no live `nitpick-libs-…` peer and that
session's work was committed (`59821a4`). One writer here (W-16, P-19): if this
names a session that is not you, do not write in this repository.
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
| s2 | `nitpick-time` | 0.0.0 — the language probes | *(no live worker)* | 2026-09-03 21:26 | `claude-opus-5` | **STOPPED on O-N4, O-N9, O-N10.** Ten probes worked, four commits, both checks clean, tree clean. **Owed before anything advances: a verifier on `9113487`** (W-21) — not run before this session's handoff because a verifier dies with the session that spawned it. Then probe 11, then 09/10 |

## Questions for the author

| # | Stream | Raised | Question | Recommendation |
|---|---|---|---|---|
| — | — | — | nothing pending | — |

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
| 1 | `nitpick-regex` | 0.0 … 1.0 (16) | — | independent; nothing gates it |
| 2 | `nitpick-tui` | 0.0 … 1.0 (18) | — | independent. Inherits stream 1's Unicode approach from `nregex` |
| 3 | `nitpick-logview` | — | `BLOCKED on nitpick-tui 0.14` | repository not created; created at `ntui` 0.15's open (T-115) |

## Stream 2 — data

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-time` | 0.0 … 1.0 (10) | `CLAIMED s2` | independent. Smallest first item; finishes early and can take slack |
| 2 | `nitpick-parse` | 0.0 … 1.0 (15) | — | independent |
| 3 | `nitpick-conflint` | — | `BLOCKED on nitpick-parse 0.11` | repository not created; created at `nparse` 0.12's open (PA-103) |

## Stream 3 — system

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-sockets` | 0.0 … 1.0 (12) | — | independent |
| 2 | `nitpick-posix` | 0.0 … 1.0 (14) | — | **O-N6 answered 2026-09-03 by probe 02** — negatively, and the repository absorbed it (PX-100: `failsafe` is generated). W-1 is discharged. Nine of its cycles are ungated and are the slack this stream uses when a gate is not ready. **Q-1 answered 2026-09-03:** POSIX.1-2024 (Issue 8) is current and its utility table moved by 19 entries — the first worker here files the digest and amends `SCOPE.md`, `CONFORMANCE.md` K-1 and `GLOSSARY.md`; the syntax guidelines are unchanged |

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
| **1.5.1b — the workbench's three defects** | `nitpick-time` 0.0.5, 0.5 and all `src/fmt/` work | **PLANNED AND RATIFIED 2026-09-03**, `meta/roadmap/1.5/1.5.1b.md` at the compiler's `4bf3e47`. Five commits: DEF-2 (our O-N8) first because it is independent, DEF-3 (our O-N9), DEF-1's three backend text builders (our O-N4), then **D-246** statement-end temporaries and **D-247** `List<T>` as owning. Starts when 1.5.1's last four steps land. The compiler session messages this workbench at the landing with the commit, whether `build/` was written after it, and the after-numbers on our own recipes |
| **D-248** (`mod:` header mandatory and first; `main`/`failsafe` root-only) | every library, at the re-pin | **RATIFIED**, lands in 1.5.1b. **Costs this ecosystem nothing if we keep writing as we do** — all 17 `.npk` in `nitpick-time` and all 8 in `nitpick-posix` already comply. See `PLAYBOOK.md` §2 |
| **D-249** (the `Views` column) | the fix behind DEF-3 / O-N9 | **RATIFIED**, lands in 1.5.1b |
| O-N2 (`npkg` builds a library) | retiring six Python harnesses | **not on the compiler's 1.5 or 1.6 map** — a request, not a date |
| O-N1 (`clone_exec` signal mask) | `ntui` 0.1.6, cosmetically | request raised |
| O-N5 (`npkg` multi-artifact) | `nitpick-posix`'s build | request raised |
| ~~O-N6~~ (macro splices a `pick`) | `nitpick-posix`'s **shape** | **ANSWERED 2026-09-03: no.** Probe 02, seven programs. A macro is not shareable across modules at all (`MACRO-007`); `failsafe` is generated instead (PX-100). Shape changed, schedule did not |
| **O-N4** (`npkc` quadratic in one declaration's size) | `nitpick-time` **0.0.5** (the tzdb size spike must compile a real emitted table) and **0.5** (the generator). TM-007's 26 838-row table costs 281 s and 30.9 GiB, so a 16 GiB machine and CI cannot build the library in its shipping shape, and every consumer pays it. It does **not** block 0.0.1–0.0.4, which carry no large declaration | **BISECTED 2026-09-03** — the frontend is *linear* on all three axes; the quadratic is three text builders in `src/backend/` that re-concatenate an accumulator per element, per trap site and per byte, compounded by D-183's never-dropped owning temporaries. Neither of the workbench's two relayed hypotheses (identifier length, then total source bytes) survived measurement. Scheduled in **1.5.1b**. **ACCEPTED 2026-09-03** by the compiler session, which owns `npkc`'s frontend. Recorded there as **DEF-1** (`meta/roadmap/OPEN_DECISIONS.md` §2f) with our numbers, controls and the exit-0 discipline. Proposed: a dedicated subcycle **1.5.1b** after 1.5.1 closes and before 1.5.2, one commit per defect under a full harness, **measured before it is touched so the fix is a number**, `big_fixed_array_cost.npk` as the regression case. Cause not yet confirmed and deliberately not guessed. **The schedule is the author's call.** That session messages us when 1.5.1b opens and again with the re-pin commit |
| **O-N10** (`derive` on a payload enum: refused, or silently tag-only) | nobody yet — `nitpick-time` exposes one payload enum and no rule needs a derive on it. **Blocks the first library that wants one** | **RAISED 2026-09-03.** `#[derive(Eq)]` is `NITPICK-TYPE-034`; `#[derive(Ord)]` compiles and reports `Literal(7)` equal to `Literal(9)`. The quiet half is the serious one. No file in the compiler's tree derives on a payload enum, so the gap is coverage; the ask includes a test there. Not blocking, so no author decision is pending |
| **O-N9** (D-004's escape rule unenforced for slice views) | `nitpick-time` in principle — every `src/fmt/` parser takes a `uint8[]` — and **BLOCKING by the author's ruling** — `src/fmt/` work and probes 09/10 wait for the compiler; the house rule "a view is a parameter, never a return value" is kept as a belt, not as the guarantee | **RAISED 2026-09-03.** `string_bytes(local)` returns a view that outlives its owner at exit 0 and reads freed memory; `@`-borrows in the same position are refused, so the rule is documented and under-enforced for one type. **Q-8: the author ruled it BLOCKING.** Accepted by the compiler as **DEF-3**, second of 1.5.1b's five commits — the borrow walk learns that a view-maker's result borrows its operand. The analyses currently name neither `string_bytes` nor `string_from_bytes`; the only view they know is the range-view `arr[lo...hi]` |
| **O-N8** (`mod:`/basename mismatch merges two files) | nobody — raised for correctness | **ACCEPTED 2026-09-03** as the compiler's **DEF-2**, same §2f, same owner and same 1.5.1b slot. Emits two `define i32 @main` at exit 0 and `llc` refuses the IR; the `NITPICK-RESOLVE-005` diagnostic for the same rule already exists and simply is not applied here. Costs `ntime` nothing |

---

## Ready to start now

Independent of everything, roughly a day each, and each converts an unknown
into a fact (W-14):

- [x] `nitpick-posix` 0.0.0 **probe 02** — gated a fourteen-cycle repository; ran 2026-09-03, negative, absorbed
- [ ] `nitpick-regex` 0.0.0 probes
- [~] `nitpick-time` 0.0.0 probes - **ten of eleven worked; stopped on O-N4, O-N9 and O-N10.** 01, 02, 03, 04, 05, 06, 07, 08 accepted with twins; 09 and 10 held pending O-N9; **11 not worked and is the next dispatch's first item**, being independent of every open disposition
- [ ] `nitpick-sockets` 0.0.0 probes
- [ ] `nitpick-parse` 0.0.0 probes
- [ ] `nitpick-tui` 0.0.0 probes
