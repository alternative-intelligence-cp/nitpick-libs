# The Nitpick library playbook

How a library in this ecosystem is set up and planned. Written after
`nitpick-tui` was planned end to end, so that the next four — and the ones
after them — do not re-derive it.

**This is a workbench document.** It lives beside the library checkouts rather
than inside one, because it belongs to none of them. Each library's `CLAUDE.md`
points at it as `../PLAYBOOK.md`.

---

## 1. The order of work

Specs first, then decisions, then a cycle map, then execution-grade subcycles,
then code. This is the compiler's own order and its cycle notes credit it with
catching most of the design holes that would otherwise have been found by
writing the wrong code twice.

| # | Deliverable | What it is |
|---|---|---|
| 1 | repository setup | `.gitignore`, the directory tree with a README per directory, `nitpick.toml`, `README.md`, `CLAUDE.md`, `CONTRIBUTING.md` |
| 2 | `meta/specs/` | the authority on behaviour — one document per concern, ~10–16 of them |
| 3 | `meta/DECISIONS.md` | every settled design decision, numbered, with reasoning and the alternatives declined |
| 4 | `meta/OPEN_QUESTIONS.md` | what is not settled, each with a recommendation, split by whose it is |
| 5 | `meta/roadmap/ROADMAP.md` | the cycle map |
| 6 | `meta/roadmap/<cycle>/README.md` | one per cycle: subcycle map, checklist, gate, watch-fors |
| 7 | `meta/roadmap/0.0/0.0.*.md` | cycle 0.0 execution-grade, subcycle by subcycle |
| 8 | GitHub | description and topics |

**Later cycles get a rich README, not an execution-grade file.** Each cycle's
opening subcycle file is written at the *previous* cycle's close, by the
session that just learned what that cycle taught. Cycle 0.0 is the exception —
it is written up front because there is no previous cycle.

---

## 2. What the language imposes

Every one of these is a compiler decision, not a preference, and each has bitten
a design that ignored it. `../nitpick/meta/specs/` is the authority; this is the
list of the ones that reach a library.

| Rule | Where | What it costs a library |
|---|---|---|
| `defer` does **not** run on a trap | D-014 | cleanup that matters lives in `failsafe`, which means it must not allocate, lock, or await |
| a trap is a whole-program event; no task resumes | D-063 | there is no "the worker cleans up" |
| `failsafe`'s `pick` must **name** every error that can reach it | REACH-002 | **every public `error:` you declare is an arm every consuming program owes.** §3 |
| reachability is **import-scoped** | 1.4.8 | module decomposition decides what a consumer owes |
| there are **no closures** | D-018 | callbacks are values the runtime interprets, or bare function values with no capture. Pull APIs beat push APIs |
| plain integer `+ - *` **traps** on overflow | D-210 | widen explicitly and narrow with `=>!` at a point known to fit |
| `/` and `%` by zero trap; signed `MIN / -1` traps | D-007 | a divisor is checked or proven on the same path |
| indexing is bounds-checked and traps | D-070 | an out-of-range index is a crash, not corruption — route every index through one accessor pair |
| owning values are **move-only** | TYPE-046 | no binding-to-binding copies of a `string`, `buffer`, `OwnedFd`. **A value stored in an array must have no owning field** |
| borrows are second class | D-004 | a view cannot be returned, stored past the call, sent, or held across `await` |
| a struct holding a borrow cannot be **returned** | D-004 | build it by struct literal at the call site |
| `exit 0` with live `wild` allocations traps | D-151 | every `wild` byte is paired on every path; **make the test programs exit 0 so a leak is a trap** |
| a clean exit with a registered child traps | D-188 | reap what you spawn |
| every blocking operation carries a **mandatory deadline** | D-056, D-176 | there is no unbounded read, write or wait |
| blocking is **task** suspension, never thread parking | D-071 | I/O goes through the reactor: `io_watch`, `suspend_io`, `io_ready` |
| inherited descriptors 0/1/2 stay blocking | D-071, D-185 | do not set `O_NONBLOCK` on them; open your own descriptor |
| there is **no `select`** across channels | D-072 | fan-in is one channel, or one `suspend_io` over several watched descriptors |
| an `async` function can never be `never fails` | D-163 | `raw await …` is unspellable; use `relay`, `?\|`, `?!` |
| a library **cannot declare a flag family** | D-230 | `TY_FLAGS` is four compiler-known families; yours is a plain integer with named constants |
| there are no static methods | D-185 | construction is a bare function, never `Type.new(…)` |
| there is no format-specifier language | D-053 | no `printf`, no `strftime`. Formatting is ordinary functions returning `string`, spliced by `&{ }` |
| `Default` and `Display` are not derivable | D-123 | a default that carries meaning is a value nobody chose |
| operator overloading is forbidden | OP_REFERENCE | `a.eq(b)`, not `==`, on anything that is not a scalar |
| **the runtime installs no signal disposition, for anything** | measured: no `rt_sigaction` in `npkrt.ll` | **every signal's default is live.** `SIGPIPE` terminates the process. A write to a pipe or socket whose peer died is lethal unless you passed `MSG_NOSIGNAL` (`send` only) or blocked the signal |

> **The last row cost this ecosystem a shipped specification error.** `ntui`
> stated that `SIGPIPE` could be left unblocked *"because the floor already
> returns `EPIPE`"* — true of the case being thought about (a hung-up **tty**
> returns `EIO`) and false in general. `nitpick-sockets` caught it by grepping
> the runtime instead of accepting the claim; `ntui`'s T-113 is the correction.
> **Check the disposition, do not assume it**, and note that the right answer
> differs by library: a passive library passes `MSG_NOSIGNAL` and must not
> alter its host's signal state, while one that already owns the process's
> signals blocks it.

**Read `../nitpick/meta/specs/` rather than trusting this table.** It is a
summary of documents that are themselves the summary, and the compiler is
moving.

---

### Facts that only measurement produced

Every one of these was found by a probe, and every one had already been
written into a shipped plan the other way round. They are here because every
repository would otherwise rediscover them. The first two come from
`nitpick-posix`'s probe 02 and the rest from `nitpick-time`'s, both on
2026-09-03.

- **A macro is invocable only in the module that declares it**
  (`NITPICK-MACRO-007`, on D-124: an invocation's meaning depends on which
  module it is in). **A macro cannot be shared across a codebase.** Any plan
  whose shape is "one macro definition, many call sites in other modules" does
  not work, and `nitpick-posix` lost its headline mechanism to this. Where you
  want one definition serving many modules, the answer in this ecosystem is a
  **generator** writing a committed file, checked by regenerating and diffing —
  the instrument `ntui` already uses for the Unicode tables.
- **`failsafe`'s `pick` must be at the TOP LEVEL of the body.** The reachability
  walk reads only the body block's immediate statements — `reach.npk`'s comment
  says *"Find the ONE top-level pick over the parameter in failsafe's body"*. A
  `pick` inside an `if`, a `loop`, a bare block, or a statement-position macro
  expansion (which *becomes* a block, `MACRO_REFERENCE.md` §4) is invisible to
  it, and the program is refused `NITPICK-REACH-001` — a diagnostic that says
  there is no `pick` while one is plainly in view.

- **There is no checked narrowing cast.** `=>!` is the *unchecked* one and it
  **truncates silently** — `nitpick-time` probe 02 pinned four shapes of it,
  including a **positive `int128` narrowing to a negative `int64`**, because
  what is discarded is everything above the destination's sign bit. And `=>`
  at a narrowing is not a runtime check either: it is refused at compile time,
  `NITPICK-TYPE-009`. So a range check before a narrowing is **ordinary
  library code you must write**, not a belt the language provides, and
  `VERIFICATION.md` P-5's `prove` is the only other thing standing between a
  caller and a wrong answer. In a time library a silently negative narrowing
  is a future instant reported as long past.
- **D-004's escape rule is enforced for `@`-borrows and NOT for slice views.**
  Returning `@x` is `NITPICK-BORROW-001` — "a borrow cannot travel up" — and so
  is a struct literal holding `@local`. But `string_bytes` on a local `string`
  yields a `uint8[]` that returns out of its owning frame **with no
  diagnostic**, and reading it afterwards reads freed memory. Raised as
  **O-N9**. Until it lands, the house rule everywhere in this ecosystem is
  **a view is a parameter, never a return value**, and it wants a harness
  check rather than vigilance — any library whose functions take `uint8[]`
  (every parser) is one careless `return` from a silent use-after-free.
- **`f(g(x))` LEAKS when `g`'s result owns memory, and every Nitpick program
  pays it today.** Bisected by the compiler session on 2026-09-03 while
  chasing O-N4: an owning **temporary** that is never bound is never dropped.
  `t = string_concat(t, "b")` twenty thousand times peaks at 260 KiB, because
  the overwritten binding frees its old body; `t = string_concat(string_concat(t,
  "b"), "c")` twenty thousand times peaks at **429 740 KiB**, because the inner
  result is an unbound temporary passed as an argument and nothing ever frees
  it. This is D-183's "statement-end temporaries" debt, recorded at the
  compiler's cycle 1.2 and never scheduled; the fix is proposed as its D-246.
  **Until it lands, bind the intermediate**: `T:a = g(x);` and then `f(a)`,
  rather than `f(g(x))`. **There is no `let`** — the bound form names the
  type — and once bound, `a` drops at scope exit like every other bound owner.
  It is not a style preference: it is the difference between linear and
  quadratic memory in any loop that does it per element, and it is why `npkc`
  itself peaks at 11 GiB compiling its own `src/main.npk`.

  **The rule is needed only at OWNING intermediates, and the test is exact.**
  A temporary leaks if and only if its type drops — the checker's
  `type_drops`. It **does**: a `string` whose body is on the heap
  (`string_concat`, **`string_slice`, which has been an owned copy since
  D-186**, interpolation, `ToString`); a `buffer`; a struct or enum with an
  owning field or payload; a `dyn`, which owns its cell; an `OwnedFd`. It
  **does not**: a `uint8[]` from `string_bytes`, a `string` from
  `string_from_bytes`, a range-view `arr[lo...hi]`, a plain pointer, any
  scalar. So `f(string_bytes(s))` leaks nothing and needs no binding, while
  `f(string_concat(a, b))` leaks the whole concatenation. One caution on the
  wording: binding does **not** save you if the bound value is then passed
  with `move` into something that leaks it further — but that is ordinary
  ownership rather than this defect, and it is your bug instead of the
  compiler's.
- **`_~argv` marks a parameter DISCARDED, not merely unused.** Reading it is
  `NITPICK-TYPE-007`. A probe or program that wants `argv.len` must spell the
  parameter `cstring[]:argv`. Cheap, and it cost a probe a rewrite.

### A file's name is part of the language

A file's `mod:` declaration must equal its basename, and **no identifier may
begin with a decimal digit** — D-147 reserves that opening for numeric literals
so a lexer's first character decides. So no source file may be named
`01_thing.npk`; `mod:01_thing;` is `NITPICK-LEX-003` with `NITPICK-RESOLVE-005`
behind it. Probes are `probeNN_topic.npk` and conformance cases `caseNN_*`.

*Every one of the first six plans wrote `01_name.npk` before anybody compiled
one.* It is the cheapest possible bug and it survived six planning passes.

**And when it does go wrong it does not always say so.** `nitpick-time` 0.0.0
found that a root file whose `mod:` name mismatches its basename **while a
sibling file carries that basename** is not diagnosed at all: `npkc` compiles
the sibling too, merges both files into one module, emits IR with two
`define i32 @main`, and **exits 0**. `llc` then refuses the IR, a long way
from the cause. Delete the sibling and the diagnostic is exemplary —
`NITPICK-RESOLVE-005` names the rule and even anticipates the self-header
case — so the resolver knows the rule and simply does not apply it when the
name it was given happens to resolve to a different file. Raised as **O-N8**
(the compiler's DEF-2); until it lands, *a build that mysteriously grows a
second `main` is this, not your program*.

---

## 3. The error budget

**The single most important API constraint in this ecosystem, and it has no
analogue in any other language.**

REACH-002 makes every `error:` that can reach `failsafe` a **named arm** the
consuming program's `failsafe` must carry — and forgetting one is a compile
error. A library declaring thirty errors makes thirty arms mandatory in every
program that imports it.

So:

1. **Decide a budget, state it as a number, and treat it as a ceiling.**
   `nitpick-tui`'s is nine. A library whose failures are *numerous by nature*
   — a parser, a regex compiler — declares **one** identity and puts the
   detail in a rich value the caller reads, because a shutdown handler does not
   care which syntax error it was.
2. **Forward kernel errnos verbatim** (`fail r.err`). A dynamic operand does
   not enlarge the reachable set, so a forwarded errno costs no arm. Wrap only
   where the errno would tell the caller nothing.
3. **Module decomposition is part of the budget**, because REACH is
   import-scoped. Arrange the modules so a consumer importing the pure
   computation half owes nothing.
4. **Adding an identity after 1.0 is a MAJOR version** — it is a
   compiler-enforced source break in every consumer. Say so in the release
   policy.
5. **A harness check enforces it**: the count and names of public `error:`
   declarations, diffed against the specification's table.
6. **A `failsafe`'s `pick` needs `(*)` AND every reachable named arm — the
   wildcard discharges neither obligation for the other.** They are two
   different rules failing two different ways, and the budget above is only
   the second of them. `Error` has more values than a `pick` can list, so
   omitting the wildcard is `NITPICK-PICK-003` (exhaustiveness); omitting a
   reachable identity is `NITPICK-REACH-002`, and `(*)` does **not** cover it.
   This matters far beyond tidiness: **a file that trips either one compiles
   fast, because it stops early.** `nitpick-time` 0.0.0 timed five such files
   and drew the wrong conclusion from them before checking exit codes, and the
   compiler session hit the same class of trap on its first attempt to
   reproduce the curve — a different diagnostic (`RESOLVE-005`, exit 1 in
   0.04 s) and the identical failure. Two independent agents, same week.

---

## 4. Determinism and testability

The two properties that make a library in this ecosystem worth the trouble.

- **Same inputs, same bytes.** No environment read on a hot path, no clock, no
  `isatty`, no system database, nothing inferred from circumstance (D-076). If
  a function needs a fact, that fact is a parameter.
- **A headless core.** Put everything that touches the kernel behind one module
  boundary, and give it a test double. Everything above it is then exercised
  with no device, no network and no terminal — which is what makes the suite
  runnable in CI, under a debugger, and forty times over.
- **A clock supplied by the caller.** Anything with a timeout takes `now_ns`
  from its caller rather than calling `mono_now()` itself, so the timing
  behaviour is testable at the boundary where it matters.
- **An oracle, not just assertions.** `nitpick-tui` renders, parses its own
  output back with a miniature VT, and compares to what it started from. The
  general shape is: *if the library produces a representation, write the
  reverse and check the round trip.* A parser has one for free (parse ∘ print).
  This catches the bugs that produce plausible-looking output, and nothing else
  does.
- **Where a library has several implementations of one operation, require them
  to agree.** `nitpick-regex` has four engines plus a deliberately naive
  reference, and their agreement is a stronger oracle than any written
  expectation could be: **an optimisation that changes an answer is caught by
  the run that disables it, and by nothing else.** The reference implementation
  is written to be obviously correct and never to be fast.
- **The oracle stage is named for what it does, not for `ntui`'s.** "Golden" is
  a terminal library's word. A parser's is `roundtrip`, a regex library's is
  `agree`. Name yours after the property it checks.
- **A real conformance corpus is the gate**, where one exists. `nitpick-tui`'s
  segmenter is gated on the UCD's own `GraphemeBreakTest.txt`, not on
  hand-written cases, because hand-written cases test the rules the author
  understood.

---

## 5. Adversarial input

Most of these libraries parse or receive bytes somebody else controls. In a
language whose selling point is that a failure is a controlled stop, an input
that can stop the program is a defect.

- **An accumulator over attacker-controlled digits is the highest-risk line in
  any of these libraries.** `acc = acc * 10 + d` traps on overflow (D-210), so
  a 23-digit number in a JSON document, a length prefix on a socket, or a year
  in a timestamp is a **remote denial of service** — a failure C and Rust do
  not have, because both wrap. Route every input-derived multiply through one
  checked helper, and grep for the ones that are not.
- **No native recursion on attacker-controlled depth.** A recursive-descent
  parser on `[[[[[…` blows the stack, and the language has no stack guard. Use
  an explicit stack with a stated depth limit — **and remember the walk, the
  compare, the print and the drop**, because a tree built by a depth-bounded
  parser and freed by a recursive drop overflows at the end of a *successful*
  parse.
- **Every bound is a named constant in one file**, every one is exercised by a
  case sitting exactly on it and one exceeding it, and none of them is a
  `while` loop over attacker-controlled length without one.
- **Fuzz it, and commit what the fuzzer found** as a permanent case.
- **State the invariants the fuzzer checks**: never traps, always terminates,
  consumes every byte exactly once, allocation bounded.

---

## 6. Tooling, as measured at the compiler's cycle 1.5.0

- **`npkg` cannot build a library.** `npkg build` *is* the compiler's own
  bootstrap ladder — it assembles `bootstrap/seed/stage1.ll` and
  `runtime/npkrt.ll`, has the builder compile `[build] entry`, and names the
  result `npkc`. `target = "library"` is accepted by the schema and read by
  nothing.
- **`[dependencies]` resolves to nothing.** The loader's dependency-root list
  (`RootList`, `src/frontend/resolve_path.npk`) is created empty in
  `src/driver/pipeline.npk` and `rootlist_add` is called from nowhere. Only
  `./` and `../` paths resolve.
- **Therefore**: a Python `harness/` builds and tests the library, mirroring
  `bootstrap/harness/`'s relationship to `npkg`, and retiring the same way.
  Zero-dependency governs the artifact, not the workbench — the compiler's own
  `ORCHESTRATION.md` §6 says so.
- **Every import is relative** until that closes, and every such site carries a
  comment naming the open question so the day it lands the change is greppable.
- **`npkc` is quadratic in the size of ONE declaration** — not in the number of
  declarations, in the size of a single one — on three independent axes:
  elements in a module-level `fixed` array initialiser, statements in one
  function body, and bytes in one string literal. At 30 000 array rows that is
  **281 s and 30.9 GiB**; at 480 000 literal bytes, **308 s with memory flat**,
  which makes the string axis a separate pathology rather than the same one
  seen through the lexer. Controls place the cost in the *declaration*: an
  unread table costs what a read one costs, and 4 000 **separate** `fixed
  int64` bindings cost 0.61 s against one 4 000-element array's 4.19 s.
  Raised as **O-N4** (the compiler's DEF-1), reproduced independently by the
  compiler session on a different build, and owned there. **Plan around it
  only by not generating enormous single declarations yet — never by
  reshaping a library's data to dodge it**, which buys the number back and
  buries a compiler bug in library code that outlives it.

**Evidence a claim at the size you can afford.** An emission *form* — what a
declaration is lowered to — is a property of the lowering and not of the
element count, so 300 rows evidences what 30 000 rows cost 281 s and 30.9 GiB
to observe once. Split a probe's questions by what each actually requires:
"do 30 000 rows compile" needs 30 000 rows, "is it emitted as a read-only
constant with no startup work" does not. And commit the transcript verbatim
with every command's exit code, rather than a prose summary of it — a summary
is not evidence, and `nitpick-time` 0.0.0 had its emission claims failed by
its own verifier for exactly that.

**A timing not paired with an exit code is not a measurement.** A source file
that fails to compile stops early and looks fast, so a failing configuration
is indistinguishable from a quick one on wall-clock alone — and it will be the
*fastest* row in your table, which is exactly the row a curve is most sensitive
to. Record `npkc`'s exit status beside every number, and treat any timing
without one as absent. Both agents who measured O-N4 fell into this before
they were finished; neither would have caught it by reading the output.

---

## 7. Repository conventions

**`.gitignore`** — build output, `*.o`, `*.ll` (negating any committed
fixture), `a.out`, `__pycache__`, `*.log`, generator inputs that are large and
reproducible, editor residue, `.internal`, `.claude/settings.local.json`. Plus
an explicit **"NOT ignored, deliberately"** block naming the generated tables
and the fixtures, with the reason for each.

**Directories**, each with a short `README.md` naming what lives there, which
spec governs it, and which cycle builds it:

```
src/       the library, Nitpick only, layered with the direction of every arrow stated
tests/     probe, conformance, unit, golden, rejection, fixtures
harness/   the Python build and test runner
tools/     generators; everything they emit is committed and regeneration-checked
examples/  built AND run by the harness, so a broken example is a red run
docs/      written at 1.0
meta/      specs, DECISIONS.md, OPEN_QUESTIONS.md, roadmap, research, scratch
```

**`nitpick.toml`** — the compiler's schema exactly (`BUILD_REFERENCE.md` §1):
`[project]` with `target = "library"`, `[build]`, `[toolchain]` pinned to
20.1.2 with the four flag lists, an **empty** `[dependencies]`, and a
`[[test]]` table that starts empty with a comment saying each cycle adds its
own — because an entry naming an empty directory is a suite that reports green
while checking nothing.

**Reserved-word substitutions are ecosystem-wide, not per library.** §10's
table says which ordinary-looking names are taken; the replacements are shared
so the fourth library does not invent a fourth spelling: **`descr`** for a raw
descriptor number, **`sink`** for a byte destination, **`src`** for a byte
origin, **`hi`** for an upper bound, **`bound`** for a constraint,
**`cap_set`** for a capability set, **`mode_bits`** for a mode mask.

**Decision prefixes** are per library and distinct, because single letters are
already used for *rule* prefixes inside spec documents (`S-1` in a safety doc,
`X-1` in a text doc, and so on):

| Library | Prefix |
|---|---|
| `nitpick-tui` | `T-` |
| `nitpick-parse` | `PA-` |
| `nitpick-regex` | `RX-` |
| `nitpick-sockets` | `SK-` |
| `nitpick-time` | `TM-` |

`D-nnn` always means the **compiler's** decisions and is never ours to amend.

**A specification's internal rule prefix must not collide with `O-N`, `O-x` or
`Q-` either.** Rule prefixes are single letters scoped to their document (`S-1`
in a safety doc, `X-1` in a text one), and it is easy to reach for `Q-` in a
verification document or `O-N` in an "options" one — `nitpick-sockets` did
both, and had to renumber. Check before you number.

**Open-question prefixes**: `O-x` is ours, `O-N` is a gap in the compiler or
its tooling to be raised as a request, `Q-` is a question for the project's
author. A question that gets answered is **struck through with its decision
number, never deleted** — the question is part of the record of how the answer
was reached. An `O-N` id used outside its repository is the workbench
registry's id (`meta/OPEN_QUESTIONS.md` §"For the compiler"), because the
per-repository numbers collide.

---

## 8. The cycle map

- Cycle 0.0 is always **the language probes, the harness, and the storage
  primitives.** Probes first: small programs asking the compiler whether the
  shapes the design depends on are spellable. *A construct that parses is not a
  construct that works* — the compiler's cycle 0.4 was mostly repair, and every
  repair dated to the cycle that had parsed the construct. A probe that fails
  changes the design, and finding that out on day one costs a day.
- **The riskiest thing early**, not the thing most depends on. Everything above
  a device boundary is testable against a double, so the device goes early
  because it is where the unknowns are.
- **A probe answers "is this spellable"; a spike answers "how big is this
  actually".** When a cycle-0.0 risk is a *measurement* rather than a language
  question — how large is the compiled tzdb, what does the event stream cost
  per byte, how many steps does this engine take — the instrument is a spike,
  with **the thresholds decided in advance**, so that a bad number produces a
  stop rather than an improvisation. `nitpick-time` added one as 0.0.5 and it
  is what turned "compile the tzdb in" from a preference into a decision.
- **Instruments precede the constructs they guard.** The oracle is written and
  tested before the thing it judges, so the thing is developed against a
  checker that already works.
- **A decision precedes the cycle that needs it.** Each cycle's README lists
  its open questions; a cycle whose questions are open is not ready to start.
- **Verification obligations are written from cycle 0.0 onward**, in the
  syntax they will take, as comments, with property tests standing in until the
  compiler's 1.5 makes them real. The compiler's R9 is explicit that
  obligations discovered and never collected are the cheapest way to lose the
  campaign.
- **Cycle numbers sort lexically only to `0.9`.** The map is authoritative over
  lexical order; do not renumber to keep single digits.

---

## 9. Testing conventions

Adopted from the compiler marker for marker, so a reader moving between
repositories reads one thing.

```
// expect-exit: 7        // expect-error: NITPICK-TYPE-046
// expect-error-at: 14:9 // expect-note: …
// stress: 40            // argv: …
```

- **Assert on codes and exit codes, never on message text.**
- **A negative test with no expectation is a failing test.**
- **Unexpected diagnostics fail a test as surely as missing ones** (D-237): the
  set of codes reported must **equal** the set the expectations name.
- **Anything with a timing dimension runs forty times**, not once. Two of the
  compiler's most serious defects hid behind single green runs and neither
  reproduced in fewer than about twenty.
- **A red under stress is a stop sign, never a retry.**
- **The harness is itself tested**: a self-check feeds it wrong expectations and
  requires it to report every one as a failure, and it runs *first*.
- **Whole-tree checks that diff the library against the documents describing
  it.** Every hole the compiler found was found by a check that diffs two
  lists, and none of them by a test.

---

## 10. Reserved words that read like ordinary names

The full table is `../nitpick/CLAUDE.md`. The ones a library reaches for:

`buffer` `raw` `move` `drop` `pass` `fail` `relay` `give` `pick` `fall`
`end` `in` `mod` `limit` `any` `as` `on` `with` `where` `is` `is_err`
`error` `never` `fails` `defaults` `discard` `nodrop` `unit`
`fd` `pid` `tid` `uid` `gid` `thread` `channel` `atomic` `joins` `gives`
`Mutex` `Guard` `RwLock` `RGuard` `CondVar` `Barrier` `acquire`
`trit` `nit` `oflags` `prot` `mflags` `fmode` `Self` `Result` `Optional`
`Handle` `arena` `shared_arena` `Future` `Channel` `OwnedFd` `simd`
`complex` `array` `func` `range` `struct` `enum` `assoc` `opaque` `trait`
`impl` `Rules` `fixed` `NIL` `comptime` `derive` `macro` `inline` `noinline`

Three shapes that surprise a C or Rust habit: adjacent string literals do not
concatenate; `discard(x);` takes parentheses and `defer { … }` takes no
trailing semicolon; declarations end `};` and control-flow blocks do not. And a
file's `mod:` name must equal its basename, or the loader reports
`NITPICK-RESOLVE-005` at line 1 and says nothing about the name.

---

## 11. Prior art

`../ARCHIVE/` holds the prototype-era implementations. They are a **behavioural
oracle** — what the domain needed, what the edge cases were, which tests
existed — and their **dependency choices are not precedent**: most of them
reach C through an FFI that no longer exists, and several carry defects
recorded in the compiler's own audits. Read them for the domain; write the
design fresh.

---

## 12. What a finished plan looks like

- Every specification rule is numbered and normative.
- Every design decision is in `DECISIONS.md` with its reasoning **and the
  alternatives declined**, because the alternatives are what a later reader
  will propose.
- Every open item has a recommendation and a cycle that settles it, or a stated
  reason it stays open (it is a measurement, it is data, it is gated, it waits
  for a consumer).
- Every cycle has a checklist, a gate, and a "watch for".
- Every cross-reference resolves, every decision cited is defined, every
  decision defined is cited.
- **No cycle is blocked on a decision.**
- Every external dependency — a standard, a data release, a corpus, a
  reference implementation — is a row in `meta/research/CURRENCY.md` with the
  date it was checked (`skills/research/SKILL.md` §7).
