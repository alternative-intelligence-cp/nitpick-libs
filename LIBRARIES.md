# The library registry

Every Nitpick library, its package name, its decision prefix, and where it is.
**Claim a name and a prefix here in the commit that starts the work**, so that
neither is taken twice.

## Libraries

| Repository | Package | Decisions | What it is | State |
|---|---|---|---|---|
| [`nitpick-tui`](https://github.com/alternative-intelligence-cp/nitpick-tui) | `ntui` | `T-` | terminal user interface | **planned** — 16 specs, 67 decisions, 18 cycles, 0.0 execution-grade |
| [`nitpick-parse`](https://github.com/alternative-intelligence-cp/nitpick-parse) | `nparse` | `PA-` | multi-format parsing over one event stream, with format plugins | **planned** — 13 specs, 43 decisions, 15 cycles, 0.0 execution-grade |
| [`nitpick-regex`](https://github.com/alternative-intelligence-cp/nitpick-regex) | `nregex` | `RX-` | regular expressions, linear time guaranteed | **planned** — 14 specs, 37 decisions, 16 cycles, 0.0 execution-grade |
| [`nitpick-sockets`](https://github.com/alternative-intelligence-cp/nitpick-sockets) | `nsockets` | `SK-` | the BSD socket surface — AF_UNIX, TCP and UDP over IPv4/IPv6 | **planned** — 14 specs, 35 decisions, 12 cycles, 0.0 execution-grade |
| [`nitpick-time`](https://github.com/alternative-intelligence-cp/nitpick-time) | `ntime` | `TM-` | dates, times, durations and zones | **planned** — 13 specs, 30 decisions, 10 cycles, 0.0 execution-grade |

## Who consumes each library

**Every library has a named consumer, and this table is the first place all five
have appeared together.** The applications are the libraries' test bed — the
author's words: *"we were gonna use some of the nitpick apps stuff as the
consumers of some of the libraries we made here as a way to test them while
making useful things"*. A library exercised only by its own harness is tested by
the people who wrote it; that is the same argument as the planted fault, one
level up.

| Library | Consumer | Where it lives | Named in |
|---|---|---|---|
| `nregex` | `grep` | `nitpick-posix` | [`APPS.md`](https://github.com/alternative-intelligence-cp/nitpick-apps/blob/main/APPS.md), and `nitpick-posix`'s own README |
| `ntime` | `date`, `crontab`, `at` | `nitpick-posix` | `APPS.md` |
| `nparse` | a configuration linter — TOML, JSON and YAML, reporting **every** fault in a file rather than the first | **its own repository** under `nitpick-apps` | `APPS.md` (`PA-103`) and `nparse`'s `ROADMAP.md` 0.12, *"the dogfood consumer"* |
| `ntui` | a log viewer — follow, search and filter over a large file | **its own repository** under `nitpick-apps` | `APPS.md` (`T-104`, amended `T-114`, located `T-115`) and `ntui`'s `ROADMAP.md` 0.15 |
| `nsockets` | a TCP proxy with an admin socket over `AF_UNIX` | **`examples/` inside the library** — see the note below | `nsockets`'s `ROADMAP.md` 0.9 only |

**A consumer does not have to be a POSIX utility.** `nitpick-posix` is a
subcategory for the ones that are; anything else takes its own repository in the
parent `nitpick-apps` folder, which is where the linter and the log viewer are
already placed.

**Why each was chosen is recorded where it was decided, and the reasons are
worth reading before proposing a different one.** A pager would exercise `ntui`'s
screen model and almost no widgets, so the consumer is a viewer *with a filter
bar and a status line*, which exercises the whole stack. The linter is *"the only
planned program that exercises recovery and multi-fault rendering"* — reporting
one error per run would have tested none of it. And `grep` is the utility in the
set most likely to be pointed at hostile input, which is why `nregex` refusing
back-references is a library safety property and a stated `grep` conformance
departure at the same time.

**⚠ ONE ASYMMETRY, RECORDED AS A RECOMMENDATION RATHER THAN A DEFECT.**
`nparse`'s and `ntui`'s consumers are their own repositories; `nsockets`'s is in
`examples/` **inside the library it exercises**. The program itself is well
chosen — streams, Unix sockets, descriptor passing, the bounded accept loop,
half-close and `poll_set` in one thing that has a purpose — but the arrangement's
whole value is that the consumer is written *by someone using the library rather
than writing it*, and an `examples/` program is written by exactly the people who
wrote the library. Since a non-POSIX consumer may live in `nitpick-apps`, the
placement is a choice rather than a constraint. **Raised for `nsockets`'s stream
to decide at its claim (W-7); not changed from here.**

**No library has any code yet.** "Planned" means the specification set, the
decision log and the cycle map are written and cycle 0.0 is execution-grade.
Implementation is partitioned into streams by [`WORKSTREAMS.md`](WORKSTREAMS.md);
the number of streams running at once is a per-session choice, and one is
always a coherent plan (W-5).

## Why the prefixes are what they are

A decision is cited as `<prefix>-nnn` and must not collide with two other
things:

- **`D-nnn` is always the compiler's**, in `nitpick/meta/specs/DECISIONS.md`.
  Those are language decisions and are never a library's to amend.
- **Single letters are already used as *rule* prefixes inside specification
  documents** — `S-1` in a safety document, `X-1` in a text one, `I-1` in an
  input one, and so on, scoped to the document that defines them. A library
  whose decision prefix were a single letter would collide with its own rules.

Hence two-letter prefixes from here on. `nitpick-tui`'s `T-` predates the
convention and stays as it is, because a settled decision's citation is not
rewritten.

## Names taken

**Packages:** `ntui`, `nparse`, `nregex`, `nsockets`, `ntime`.

**Decision prefixes:** `T-`, `PA-`, `RX-`, `SK-`, `TM-`, and `D-` (the
compiler's, permanently).

**Also in use across the ecosystem**, and not available to a new library: the
compiler's own `lib/` modules — `nbridge`, `nfs`, `nhash`, `nio`, `nproc`,
`nstr`, `nsys`, `ntensor`, `nvec` — several of which are destined for an
`nlibc` sibling repository when the compiler's `meta/LAYOUT.md` moves them.

## Cross-library overlaps, recorded

Dependencies between libraries are **not planned**: `[dependencies]` is empty
everywhere, because the compiler's loader initialises its dependency-root list
empty and never populates it, so a cross-repository import resolves against
nothing (`O-N2`). Where two libraries genuinely overlap, the overlap is
recorded as an open question in **both**, and resolved when resolution lands.

| Overlap | Between | Recorded as |
|---|---|---|
| Unicode tables — character classes, case folding, property lookups | `ntui`, `nregex` | an `O-x` in each |
| datetime scanning — TOML carries four datetime types | `nparse`, `ntime` | an `O-x` in each |
| generated, version-pinned data tables committed as source | `ntui` (UCD), `nregex` (UCD), `ntime` (IANA tzdb) | one shape, three instances — the pattern is `ntui`'s T-021 |
| an accumulator over untrusted digits | all five | the playbook's §5, because it is a language-wide hazard rather than a library one |

## What the first five taught

Findings from the planning passes that outlived the library that found them.
Each is now in `PLAYBOOK.md`; they are listed here because they are the
evidence for why it says what it says.

- **The runtime installs no signal disposition, for anything.** Measured by
  `nitpick-sockets` — no `rt_sigaction` in `npkrt.ll` — after `ntui` had
  already shipped a specification claiming the opposite. `SIGPIPE`'s default is
  live and it terminates the process. `ntui`'s T-113 is the correction, and the
  right answer differs by library: a passive one passes `MSG_NOSIGNAL`, one
  that already owns the process's signals blocks it.
- **`acc = acc * 10 + d` is a remote denial of service.** D-210 traps on
  overflow, so a 23-digit number in a document, a length prefix on a socket or
  a year in a timestamp stops the program. C and Rust both wrap; this ecosystem
  does not. Found by `nitpick-parse`.
- **A backtracking regex cannot be rescued by a timeout here**, because D-062
  leaves no way to name a task and therefore nothing to cancel — and a
  CPU-bound loop never reaches an `await` to observe a wind-up request, so the
  scope-exit join hits its deadline and traps the whole program. Found by
  `nitpick-regex`, and it is why that library is automata-only.
- **An `arena<T>` element may not own anything.** `get` returns a copy (D-152)
  and owning values are move-only (TYPE-046), so a node holding a `string` does
  not compile — it is not a performance question. Found by `nitpick-parse`,
  raised as a request for one clarifying sentence in the compiler's
  `MEMORY_REFERENCE.md`.
- **The prototype's parsers are unbuildable, not merely unfashionable**: they
  keep their state in bare mutable module-level bindings, which D-211 has
  refused since 1.4.2b. Stronger evidence for "rewrite, do not port" than the
  duplication argument alone.

## Prior art

`../ARCHIVE/` holds the prototype-era implementations. They are a **behavioural
oracle** — what the domain needed, what the edge cases were, which tests
existed — and their **dependency choices are not precedent**: most reach C
through an FFI that no longer exists in the language, and several carry defects
recorded in the compiler's own audits.
