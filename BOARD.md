# The board

**Live state.** What each stream is working on, what is claimed, what is
blocked, what is done. The durable plan is
[`WORKSTREAMS.md`](WORKSTREAMS.md).

> **The orchestrator owns this file** (W-8). An agent working a stream does not
> edit it — the orchestrator claims before the session starts and releases when
> the cycle closes. That is what keeps two agents out of one repository and
> removes every merge conflict by construction.

**Last updated:** 2026-09-03 · **Streams running:** 0 · **Phase:** planning
complete, implementation not started

---

## Legend

| State | Means |
|---|---|
| `—` | not started, not claimed, nothing blocking it |
| `CLAIMED s1` | stream 1 owns this repository right now; nobody else touches it |
| `BLOCKED on X` | cannot start until X closes; the reason is always a named cycle, never "waiting" |
| `DONE` | closed, archived to `done/`, and the next cycle's file written |

---

## Claim protocol

1. The orchestrator writes `CLAIMED sN` against the **repository**, not the
   cycle — a stream owns the whole repository while it works on it (W-7).
2. The agent works the cycle named in `WORKSTREAMS.md`'s order for that stream.
3. The cycle closes: full harness green, findings recorded, the next subcycle
   file written execution-grade.
4. The orchestrator moves the row to `DONE`, releases the claim, and checks
   whether any `BLOCKED` row just became available (W-9).

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
| 1 | `nitpick-time` | 0.0 … 1.0 (10) | — | independent. Smallest first item; finishes early and can take slack |
| 2 | `nitpick-parse` | 0.0 … 1.0 (15) | — | independent |
| 3 | `nitpick-conflint` | — | `BLOCKED on nitpick-parse 0.11` | repository not created; created at `nparse` 0.12's open (PA-103) |

## Stream 3 — system

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-sockets` | 0.0 … 1.0 (12) | — | independent |
| 2 | `nitpick-posix` | 0.0 … 1.0 (14) | `BLOCKED on O-N6` | **probe 02 must be answered before this is scheduled** (W-1). Nine of its cycles are ungated and are the slack this stream uses when a gate is not ready |

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
hardening cycle knows what it is waiting for.

| Compiler | Needed by | State |
|---|---|---|
| 1.5.1 – 1.5.4 (verification surface) | every library's hardening cycle | compiler at 1.5.0 |
| O-N2 (`npkg` builds a library) | retiring six Python harnesses | **not on the compiler's 1.5 or 1.6 map** — a request, not a date |
| O-N1 (`clone_exec` signal mask) | `ntui` 0.1.6, cosmetically | request raised |
| O-N5 (`npkg` multi-artifact) | `nitpick-posix`'s build | request raised |
| O-N6 (macro splices a `pick`) | `nitpick-posix`'s **shape** | **unanswered — probe 02** |

---

## Ready to start now

Independent of everything, roughly a day each, and each converts an unknown
into a fact (W-14):

- [ ] `nitpick-posix` 0.0.0 **probe 02** — gates a fourteen-cycle repository
- [ ] `nitpick-regex` 0.0.0 probes
- [ ] `nitpick-time` 0.0.0 probes
- [ ] `nitpick-sockets` 0.0.0 probes
- [ ] `nitpick-parse` 0.0.0 probes
- [ ] `nitpick-tui` 0.0.0 probes
