# The library registry

Every Nitpick library, its package name, its decision prefix, and where it is.
**Claim a name and a prefix here in the commit that starts the work**, so that
neither is taken twice.

## Libraries

| Repository | Package | Decisions | What it is | State |
|---|---|---|---|---|
| [`nitpick-tui`](https://github.com/alternative-intelligence-cp/nitpick-tui) | `ntui` | `T-` | terminal user interface | **planned** — 16 specs, 67 decisions, 18 cycles, 0.0 execution-grade |
| [`nitpick-parse`](https://github.com/alternative-intelligence-cp/nitpick-parse) | `nparse` | `PA-` | multi-format parsing over one event stream, with format plugins | **building** — 13 specs, 15 cycles; cycle 0.0 in flight at compiler `2e1cb4a`: its plan verified and merged 2026-10-16 (`fca1333`), with its research re-cut (`be5f446`) and its adoption of `c9baa9e`, the libraries' first re-pin (`cdddcf6`); 0.0.0 (the probes) and 0.0.1 (the skeleton, the manifest at LLVM 20.1.8, CI) worked on the Team seat and merged, the last on 2026-10-21 (`9f37f45`); 0.0.2's step cut and 0.0.1a, the adoption of `2e1cb4a` (the second re-pin), merged 2026-10-25 (`1dd6f77`); 0.0.2 (the harness) worked on the Team seat and merged 2026-10-28 (`ab927c8`); 0.0.3's amendments (its three harness gaps first) and step cut merged 2026-10-29 (`f6e8118`); 0.0.3 (the harness's second half) worked on the Team seat and merged 2026-10-29 (`8f10cb9`); decisions to PA-117; 0.0.4's amendments next |
| [`nitpick-regex`](https://github.com/alternative-intelligence-cp/nitpick-regex) | `nregex` | `RX-` | regular expressions, linear time guaranteed | **building** — cycles 0.0 … 0.2 closed, the last (the HIR) on 2026-10-20 at the pin `c9baa9e`, its close 0.2.6 the Team seat's chain, merged 2026-10-21: 347 units GREEN, with four pending outside them. Cycle 0.3, Unicode, is next: `0.3.0.md` is planned, and its drafts PD-184 … PD-188 were accepted by the author on 2026-10-21. 13 specification documents, decisions to RX-248, 16 cycles. *(Was "… cycle 0.2, the HIR, in progress … 0.2.5a, the adoption of compiler `c9baa9e`, verified 2026-10-16 … 0.2.6, the cycle's close, is next … decisions to RX-245" until 2026-10-21.)* *(Was "… 0.2.5a, the adoption of compiler `c9baa9e`, was planned and verified 2026-10-16, its two decisions accepted as RX-244 and RX-245, which its work writes; that work is next … decisions to RX-243" until 2026-10-16.)* *(Was "… 0.2.4 … 334 units GREEN, with three pending outside them … decisions to RX-240" until 2026-10-15.)* *(Was "… 0.2.3 … 318 units GREEN … decisions to RX-237" earlier on 2026-10-13.)* *(Was "… 302 units GREEN, with two pending until 0.3.4 … decisions to RX-234" until 2026-10-13.)* *(Was "… 294 units GREEN … decisions to RX-231" until 2026-10-12.)* *(Was "… 0.2.1 (desugaring) verified 2026-10-08 … decisions to RX-229" until 2026-10-09.)* *(Was "cycle 0.1 at its close, 0.1.0 to 0.1.5 verified … decisions to RX-213" until 2026-10-08.)* *(Was "planned — 14 specs, 37 decisions, 16 cycles, 0.0 execution-grade" until 2026-10-02.)* |
| [`nitpick-sockets`](https://github.com/alternative-intelligence-cp/nitpick-sockets) | `nsockets` | `SK-` | the BSD socket surface — AF_UNIX, TCP and UDP over IPv4/IPv6 | **planned** — 14 specs, 36 decisions, 12 cycles, 0.0 execution-grade at compiler `2e1cb4a`, its plan (0.0.0 … 0.0.5) merged 2026-10-25 (`5862558`) and its fix round 3 2026-10-29 (`af50100`); 0.0.0's amendments and step cut (round (i)) worked on the Team seat and merged 2026-10-29 (`424ec95`), PD-159 … PD-163 accepted; cycle 0.0.0 (the research gate and twenty probes at `2e1cb4a`) worked on the Team seat and merged 2026-10-29 (`049afd0`), `SK-101` … `SK-105`; 0.0.1's re-cut next |
| [`nitpick-time`](https://github.com/alternative-intelligence-cp/nitpick-time) | `ntime` | `TM-` | dates, times, durations and zones | **building** — cycles 0.0 … 0.3 closed, the last (the host boundary: the clocks, the system zone, the test double) on 2026-10-15 at the pin `7e91730`, its close 0.3.4 verified the same day: 146 units GREEN. Cycle 0.4 (formatting and parsing) is next: `0.4.0.md` is planned, and its drafts PD-149 … PD-154 await acceptance. 12 specification documents, decisions to TM-262, 10 cycles. *(Was "… cycle 0.3 (the host boundary) in progress: 0.3.0 … 0.3.2a … 0.3.3, the double, verified 2026-10-13 … 146 units GREEN" until 2026-10-15, the ecosystem audit's E3-7.)* *(Was "… 143 units GREEN with four pending … decisions to TM-259" until 2026-10-13.)* *(Was "… 0.3.2 (the system zone) verified, the last on 2026-10-09, 143 units GREEN … decisions to TM-257" until 2026-10-10.)* *(Was "… 0.3.0 and 0.3.1 verified on 2026-10-08, 134 units GREEN … decisions to TM-253" until 2026-10-09.)* *(Was "cycle 0.3 opened, `0.3.0.md` written … decisions to TM-245" until 2026-10-08.)* *(Was "planned — 13 specs, 30 decisions, 10 cycles, 0.0 execution-grade" until 2026-10-02: the cycle 0.2 audit's S5.)* |

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
| `ntui` **+ `nregex`** | a log viewer — follow, search and filter over a large file | **its own repository** under `nitpick-apps` | `APPS.md` (`T-104`, amended `T-114`, located `T-115`) and `ntui`'s `ROADMAP.md` 0.15 |
| `nsockets` | a TCP proxy with an admin socket over `AF_UNIX` | **`examples/` inside the library** — see the note below | `nsockets`'s `ROADMAP.md` 0.9 only |

**AN APPLICATION SERVES THREE PURPOSES, AND THE THIRD IS THE ONE NOBODY WRITES
DOWN.** The author's framing, 2026-09-06:

1. **A test that is not thrown away.** The exercise a library needs and a
   program somebody wants are the same artefact, so the coverage costs nothing
   that was not already being built.
2. **Work already scheduled.** `nitpick-posix` was a porting target from the
   prototype regardless. Pairing it with library validation is *"two birds with
   one stone"* — the marginal cost of the test bed is close to zero, because the
   sequencing is the only thing that changed.
3. **A usable demonstration, in the language, of something real** — *"rather
   than just a library or a 'trust me bro' description of what it should do."*

**The third is worth stating plainly because it is an argument about EVIDENCE,
and it is the same argument this ecosystem already applies to itself.** A library
can only be evaluated by reading it, or by believing its README. A working `grep`
can be **run**, by someone who will never read a specification. Internally this
project refuses "trust me" everywhere — planted faults, stated denominators,
premises measured rather than accepted — and a library shipped with nothing but
its own harness asks the outside world for exactly the credence it declines to
extend to itself. **The applications are how the claim becomes a demonstration.**

**AND POSIX STRUCTURALLY CANNOT COVER ALL FIVE, WHICH IS WHY THE OTHER
APPLICATIONS ARE REQUIRED RATHER THAN A FALLBACK.** Of the five libraries,
`nitpick-posix` reaches **three** — `nregex` (`grep`), `ntime` (`date`,
`crontab`, `at`), `nparse` (`awk`). It cannot reach **`nsockets`**, because the
POSIX utility set has essentially no networking utilities to write, and it barely
reaches **`ntui`**, whose natural large consumer `vi`/`ex` is *excluded from
`nitpick-posix` by `PX-004`* as its own project. **The two libraries POSIX cannot
serve are exactly the two whose consumers already live in their own
repositories** — so the design has accounted for this, and the own-repository
placement is a consequence of the standard's shape rather than a preference.

**A CONSUMER MAY SPAN LIBRARIES, AND TWO ALREADY DO** — the log viewer consumes
`ntui` **and** `nregex`, and `awk` consumes `nparse` **and** `nregex`. That is
worth stating because a shared consumer tests something no single-library
consumer can: **the seam**, where each library alone is correct and the pair is
wrong. Every defect this ecosystem has found the hard way lived at a seam of some
kind.

**The rule that makes a shared consumer safe rather than risky is MATURITY
ASYMMETRY, and both existing cases already obey it.** The newer library owns the
consumer and the older one is merely *used*: the log viewer is `ntui`'s dogfood
at its cycle 0.15 while `nregex` is far ahead and stable by then. **Two immature
libraries co-owning one consumer would couple their cycle schedules**, so either
one's slip blocks the other's validation, and a red in the shared program belongs
to neither of them until somebody bisects it. **Prefer: one owner, the rest
already finished.**

**A note on when to add more of them.** A shared consumer also multiplies
exposure to compiler churn — two libraries crossing one program means a compiler
change can redden the seam for reasons belonging to neither. That is expensive
while re-pins land weekly and a pin-dependent measurement can expire underneath a
library (see `RX-120`, which did exactly that on 2026-09-06), and cheap once the
compiler is in bug-fix and improvement mode. **The instinct to wait for that
before spanning libraries deliberately is right, and the reason is schedule
coupling rather than difficulty.**

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

**No library had any code when this registry was written.** *(2026-10-02: `nitpick-time` and
`nitpick-regex` now do — their rows say how far each has come.)* "Planned" means the specification set, the
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

**Decision prefixes:** `T-`, `PA-`, `RX-`, `SK-`, `TM-`, `PX-` (`nitpick-posix`, an application, claimed here on 2026-10-15 by
the ecosystem audit's E3-8, since `nitpick-apps/APPS.md` has no prefix column), and `D-` (the
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

## Conventions

Norms each library states in its own documents and keeps. The rules behind them are
[`PLAYBOOK.md`](PLAYBOOK.md)'s; this section records what the ecosystem adopted as a whole, and when.

### The error budget, so a large program's `failsafe` stays writable

*Adopted 2026-10-22 from the compiler's S-134 (its R2, and R4's library side), by the author's word at
03:44:01, relayed by `management_2`: "i agree with your recommendations, go with those". The question was
the author's own, on 2026-10-09: does a program that imports many libraries end up with a `failsafe`
nobody can manage?*

REACH-002 makes every identity a program can reach a named arm that its `failsafe` must write. That is the
acknowledgement the author wants forced (`PLAYBOOK.md` §3). The compiler's measurement for S-134 found that
the system set is most of every bill: the prelude declares 31 identities, the compiler's own `failsafe`
carries 40 arms, and a small program's carries 9 to 13. Each library adds its own few on top: one for regex,
two for parse, three for time, four for sockets and nine for tui, so 19 for all five (`nitpick-posix`'s
`SAFETY.md` S-5). So the union is kept small at its source:

1. **A library publishes its arm bill with its errors.** That is the exact set of arms a consuming program
   owes for each import, stated beside the identities that cause it. An out-of-date list is a defect.
2. **It keeps its public identities few,** under a stated ceiling. Adding one after 1.0 is a major version.
3. **It declares one umbrella identity where a distinction buys a consumer nothing.** A shutdown handler
   doesn't care which syntax error it was, so the detail goes in a value the caller reads.
4. **A consumer that wants the distinction reads the error's origin chain** (the compiler's D-179), not a
   separate arm.
5. **A generated `failsafe` stays a repository's own tool** (R4). `nitpick-posix` generates its sixty
   utilities' handlers (its PX-100), and any library or application may do the same. The compiler won't
   generate one, because a reviewed diff would then be the only acknowledgement. What it adds instead, at
   the end of its queue, is a `--reach` listing: the reachable set grouped by declaring module, which is the
   list of arms a program must write.

Each library states its budget and its bill in its `meta/specs/SAFETY.md`:

| Repository | Public identities, a ceiling | Where its arm bill is |
|---|---|---|
| `nitpick-regex` | one, `ERegexPattern` (S-8, RX-060) | §4: importing it costs one arm of its own; §4.2: what else an import charges |
| `nitpick-time` | three (TM-017) | §2, S-4 … S-4c: generated per module; `cal` costs 11 arms and the umbrella 13 |
| `nitpick-parse` | two, and no input can produce either (§3) | §3, S-7: the exact arm set per import |
| `nitpick-tui` | nine (§3) | §3, S-10: the exact arm set per import |
| `nitpick-sockets` | four (§3) | §3, S-9: the exact arm set per import |
| `nitpick-posix` | three of its own (S-6); an application, so it pays the libraries' bills | §3, S-5: the system set + 1 for `grep`, + 3 for `date`, + 19 for all five; its handlers are generated (PX-100) |

**What changes for a consumer later.** R1, the compiler's one language change for S-134, lets a `pick` arm
name several values with a comma: `(ntime.ETimeValue, ntime.ETzMissing) { exit 87i32; }`. A bill then
becomes one line per dependency per action, and every identity is still written. It is planned as a landing
at the end of the compiler's queue, so it is in no pin of ours yet. R3, a frozen named set acknowledged by
its name, was not adopted.

## What the first five taught

Findings from the planning passes that outlived the library that found them.
Each is now in `PLAYBOOK.md`; they are listed here because they are the
evidence for why it says what it says.

- **The runtime installs no signal disposition, for anything.** *(Corrected 2026-10-02, the
  ecosystem audit's EC1: true through compiler `3d15ac9` only. From `c3bdae2` the runtime installs
  signal actions — measured at the pin `5fbaf4a`, two `rt_sigaction` mentions in `runtime/npkrt.ll` —
  and `SIGPIPE` (DEF-68) gets a returning handler, so a write to a dead peer answers `EPIPE` instead
  of killing the process. `PLAYBOOK.md` §2's row above the old one says so. `nitpick-posix`'s PX-011
  and `APPS.md`'s three positions on `SIGPIPE` are EC1's too, re-decided at `nitpick-posix`'s next
  dispatch.)* Measured by
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
