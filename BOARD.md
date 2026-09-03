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
| s2 | `nitpick-time` | 0.0.0 — the language probes | `s2-ntime-0.0.0-1902` | 2026-09-03 19:02 | `claude-opus-5` | **STOPPED on O-N4** (W-11). The re-dispatch lands the record only; the stream does not proceed until Q-3 is answered |

## Questions for the author

| # | Stream | Raised | Question | Recommendation |
|---|---|---|---|---|
| Q-2 | s2 | 2026-09-03 19:02 | **O-N4 — `npkc` is quadratic in the size of one declaration**, on three independent axes (array-initialiser elements, function-body statements, string-literal bytes). TM-007's tzdb is 26 838 rows: 281 s and **30.9 GiB** to compile. A 16 GiB machine cannot build `ntime`; CI cannot; every consumer pays it. Reproduction: [`nitpick-time/tests/probe/defect/README.md`](nitpick-time/tests/probe/defect/README.md) | **Raise against the compiler** (W-11). Nothing in the language changes — it is `npkc`'s implementation. Never worked around: shrinking, splitting or blob-encoding the table each buys the number back and buries a compiler bug in library code that would outlive it. **Do not let O-N4 settle O-Z1 as "ship a subset"** |
| Q-3 | s2 | 2026-09-03 19:02 | Probes **02, 03, 05-11 are unaffected** by O-N4 - it is a resource cost, not a semantics change. Work the nine against the current pin while O-N4 is open, or idle the stream until it lands? | **Work the nine.** They convert nine unknowns into facts at no risk, and O-N4 changes none of their answers. Probe 04's verdict is already recorded; only its *cost* waits on the re-pin. Idling stream 2 buys nothing |
| Q-4 | s2 | 2026-09-03 19:02 | A second, narrow `npkc` defect met by accident: a root file whose `mod:` differs from its basename, with a sibling carrying that basename, **silently merges both files and emits two `define i32 @main` at exit 0**; `llc` then refuses the IR. Six-line reproduction in the same README | **Raise alongside O-N4, blocking nothing.** It costs `ntime` nothing (the house rule is already `mod:` = basename). The resolver already has the exact diagnostic and simply does not apply it when the name resolves to a different file |

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
| O-N2 (`npkg` builds a library) | retiring six Python harnesses | **not on the compiler's 1.5 or 1.6 map** — a request, not a date |
| O-N1 (`clone_exec` signal mask) | `ntui` 0.1.6, cosmetically | request raised |
| O-N5 (`npkg` multi-artifact) | `nitpick-posix`'s build | request raised |
| ~~O-N6~~ (macro splices a `pick`) | `nitpick-posix`'s **shape** | **ANSWERED 2026-09-03: no.** Probe 02, seven programs. A macro is not shareable across modules at all (`MACRO-007`); `failsafe` is generated instead (PX-100). Shape changed, schedule did not |

---

## Ready to start now

Independent of everything, roughly a day each, and each converts an unknown
into a fact (W-14):

- [x] `nitpick-posix` 0.0.0 **probe 02** — gated a fourteen-cycle repository; ran 2026-09-03, negative, absorbed
- [ ] `nitpick-regex` 0.0.0 probes
- [~] `nitpick-time` 0.0.0 probes - **stopped on O-N4**. Probes 01 and 04 ACCEPTED; 04 found the defect. Nine probes unworked pending Q-3
- [ ] `nitpick-sockets` 0.0.0 probes
- [ ] `nitpick-parse` 0.0.0 probes
- [ ] `nitpick-tui` 0.0.0 probes
