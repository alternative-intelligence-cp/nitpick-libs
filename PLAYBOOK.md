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
| `failsafe`'s `pick` must **name** every error that can reach it | REACH-002 | ~~**every public `error:` you declare is an arm every consuming program owes.**~~ **Every identity a REACHABLE `fail` site raises — public OR PRIVATE, qualified by the module that declares it (`m.E`) — is an arm every consuming program owes; a declaration never raised costs nothing.** *(Corrected 2026-09-26, the ecosystem audit's EC3, measured at `c970483`: a private `error:EPriv` raised in a public function charged its importer `m.EPriv`; a public one declared and never raised charged nothing.)* §3 |
| reachability is **import-scoped** | 1.4.8 | module decomposition decides what a consumer owes |
| there are **no closures** | D-018 | callbacks are values the runtime interprets, or bare function values with no capture. Pull APIs beat push APIs |
| plain integer `+ - *` **traps** on overflow | D-210 | widen explicitly and narrow with `=>!` at a point known to fit |
| `/` and `%` by zero trap; signed `MIN / -1` traps | D-007 | a divisor is checked or proven on the same path |
| ~~indexing is bounds-checked and traps~~ **a slice, fixed-array, SIMD-lane or `List` index is bounds-checked and traps — a bare-POINTER index is not** | D-070 (bounds live in the array type, not the pointer type; pointers are thin, D-038) | an out-of-range slice index is a crash, not corruption; **an out-of-range pointer index reads or writes whatever is there** (`nitpick-regex`'s probe 08b read 7 992 bytes past an allocation, exit 0) — route every index through one accessor pair, and confine the pointer accessors to the module that owns the block. *(Corrected 2026-09-26, the ecosystem audit's EC2: the pin's emitter guards the slice, array, SIMD and `List` branches, not the pointer branch.)* |
| owning values are **move-only** | TYPE-046 | no binding-to-binding copies of a `string`, `buffer`, `OwnedFd`. ~~**A value stored in an array must have no owning field**~~ **— FALSE at every kept pin, measured 2026-09-25: `string[2]`, an array of a struct holding a `string`, `Vec<string>` and `Bytes[2]` compile and run. TYPE-046 refuses a COPY of an owning place, not where an owner is stored — and a generic by-value accessor (`pass v.items[i]`) MOVES the element out, leaving a counted vacancy** **— AND IN `fixed` STORAGE A MOVE OF AN OWNING PLACE COMPILES AND FAULTS (O-N20, measured at every kept pin, 2026-09-25): `fixed` is emitted as an LLVM `constant` global and the move stores its vacancy into it — SIGSEGV at -O0 (`MachineFault`, 107, at `c3bdae2`), `Unreachable` (95) under `opt -O2`; a moved-out scalar `fixed string` gets no vacancy at all, so a second move is a second owner. An implicit move reaches it too: a plain `pass NAMES[i]` from a function returning `string`. The copy is refused, the move is not — `.clone()` is the read that runs clean.** **Nothing may depend on moving out of `fixed`: work that needs it is HELD until the compiler refuses the move** (W-27; `nitpick-time`'s tzdb version string, its PD-29) **— AND FROM THE PIN `c970483` (2026-09-26) IT DOES: `NITPICK-TYPE-084` refuses `move(...)` and the implicit move at `pass`, of a `fixed` binding or any part of it (1.6.0 step 3f, DEF-99). `.clone()` is the reading** |
| a by-value parameter of an **owning** type is a loan, and **read-only** | D-004, D-266; `TYPE-085` (1.6.0 step 3g, DEF-102); in the pin from `c970483` | no assignment to it or into it, no `@`/`$$i`/`$$m`, no pointer-receiver call, no stateful operation. **A callee that changes an owning value takes `move T:p`; one that needs the whole of it takes `.clone()`.** A copyable parameter is a copy and keeps every write. The one exemption the rule states is a call through a `dyn` receiver. A `for` binding over owning elements is a loan too (`nitpick-fuzz`'s F-001, refused the same). **Until `c970483` the write compiled and freed the caller's value** (O-N21) |
| a bare generic `T` **owns**, for every question about ownership | D-264 and its 1.6.0 step 3g note; `TYPE-047`, `TYPE-085` through `type_owns_for_move` (DEF-104); in the pin from `c970483` | a generic body is checked as though `T` were `string`. A lent `T` cannot be passed out or moved (`TYPE-047`) or addressed (`TYPE-085`). **The gate reaches `T` PLACES, not only parameters: `pass v.items[i]` out of a lent or pointed-to `Vec<T>` is a move out of a loan, refused `TYPE-047`** — an unchanged `nitpick-regex` went RED 78/223 on that alone. **There is no infallible generic by-value read.** `nitpick-regex` bounds its accessor by a library `Pod` trait (`vec_get<T: Pod>`, its RX-168) and spells removal `move`; a prelude marker is the author's S-108. *(Corrected 2026-10-09, E2-3: S-108 is SETTLED as D-327, 1.6.1c, 2026-09-26. The prelude declares the marker `Copy`, derivable for a struct of copyables; under `T: Copy` a plain copy is a copy and `list_get` reads an element `never fails`. `nitpick-regex`'s `Pod` retired into it: `vec_get<T: Copy>`.)* **Until `c970483` a generic identity function returned its lent argument as a second owner** (O-N22) |
| no **part** of a `fixed` binding is written after its declaration | D-287; `TYPE-086` (1.6.0 step 4b, DEF-106); in the pin from `c970483` | an element, a plain field, a compound assignment, a stateful operation on a part, a `fixed` local's element, anything under a `fixed` field. The whole binding's second assignment and a `fixed` field's own stay `ASSIGN-002`, and the binding has no address (`TYPE-071`). **A table is built once and read; a table that changes is a local or a heap value.** **Until `c970483` a part-write compiled and stored into an LLVM `constant`**: exit 95 where the part owns, and where it is plain, 107 at -O0 and **at -O2 the write silently dropped** (O-N24, found by `nitpick-fuzz`) |
| a `fixed T[]` is the **read-only view**: a plain slice converts to it and **never back** | D-348 (ii), D-350, D-351; `TYPE-007`, `TYPE-086`, `TYPE-071`; landing 103, in the pin `7e91730` only | a plain `T[]` converts to `fixed T[]` wherever one is expected — an argument, a field, a return, a `List<fixed T[]>` element — and the reverse is `NITPICK-TYPE-007` (a cast either way is `TYPE-032`). **A write through it is `NITPICK-TYPE-086`** (an element, a compound assignment) and the address of its element is `TYPE-071`. **`string_bytes` returns one, always (D-351)**, so a reader's slot must be spelled `fixed uint8[]`: `fixed uint8[]:v = string_bytes(s)`, and a parser that only reads its bytes declares `fixed uint8[]:src`. A plain `uint8[]` parameter refuses it, and a writer through the bridge is refused outright. In a bare type position (`List<fixed uint8[]>`, `func NIL(fixed uint8[])`) `fixed` precedes a slice type and nothing else (`PARSE-013`). An impl's slice parameter is `fixed` exactly where its trait's is (`TYPE-014`). **At `5fbaf4a` and before none of this exists: `string_bytes` yields a plain `uint8[]`, and a library harness is RED at `7e91730` until it re-spells its readers** |
| every path of every function **leaves explicitly** | D-323; `FLOW-001` (1.6.0 step 5c, DEF-108); in the pin from `c970483` | a body that can reach its closing brace is refused. A `NIL` function passes `NIL`, a fallible function names its failure on every path, and `main` exits. There is no implicit return and no implicit value. **The walk is conservative towards refusal** (CONTROL_REFERENCE's words): an `if` without `else` completes, a `while (true)` with no `break` never does, and every other loop and `when` completes as a whole — so a body ending in such a loop still owes a final `pass`, `fail` or trap. **Until `c970483` the emitter returned a zero, and for a fallible function a SUCCESS carrying zero** (O-N26) — a silent wrong answer, found by `nitpick-fuzz` |
| a zero-length array `T[0]` is a type, and **owns when `T` owns** | TYPE_REFERENCE §9.2, stated 2026-09-25 at the library side's request, measured at 1.6.0 step 3g | zero bytes wide (`[0 x T]`). **A struct with a `hidden string[0]` field is move-only at no cost in bytes**, while `int64[0]` copies freely — the way a library marks a struct move-only without paying for a field |
| borrows are second class | D-004 | a view cannot be returned, stored past the call, sent, or held across `await` |
| a struct holding a borrow cannot be **returned** | D-004 | build it by struct literal at the call site. *(2026-10-22, `nitpick-parse` 0.0.0's probe 08, measured at `7e91730`: true of a borrow of a LOCAL, and false of one of a PARAMETER's bytes, which a returned struct may hold.)* |
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
| **⚠ AT `c3bdae2` THE RUNTIME DOES INSTALL SIGNAL ACTIONS — the row below held only through `3d15ac9`** | measured: `rt_sigaction` in `runtime/npkrt.ll` — 0 mentions at `aaffb87` and `3d15ac9`, 2 at `c3bdae2`; D-291, D-307, DEF-68 | `SIGUSR1` → the stop handler; `SIGSEGV`, `SIGBUS`, `SIGILL`, `SIGFPE` → `MachineFault`; **`SIGPIPE` gets a returning handler, so a write to a dead peer answers `EPIPE` instead of killing the process** — plan for the error, not the death |
| ~~**the runtime installs no signal disposition, for anything**~~ | ~~measured: no `rt_sigaction` in `npkrt.ll`~~ | ~~**every signal's default is live.** `SIGPIPE` terminates the process. A write to a pipe or socket whose peer died is lethal unless you passed `MSG_NOSIGNAL` (`send` only) or blocked the signal~~ *(Corrected 2026-10-09, the ecosystem audit's E2-1: true only through `3d15ac9`, and row 74 above is the live one. From `c3bdae2` on, the floor installs `SIGPIPE`'s returning handler at startup, so a write to a dead peer answers `EPIPE`. `SIGTERM`, `SIGINT`, `SIGHUP` and the rest still keep their defaults. The kept pins `3d15ac9` and before still behave as the struck row says.)* |

> **The last row cost this ecosystem a shipped specification error.** `ntui`
> stated that `SIGPIPE` could be left unblocked *"because the floor already
> returns `EPIPE`"* — true of the case being thought about (a hung-up **tty**
> returns `EIO`) and false in general. `nitpick-sockets` caught it by grepping
> the runtime instead of accepting the claim; `ntui`'s T-113 is the correction.
> **Check the disposition, do not assume it**, and note that the right answer
> differs by library: a passive library passes `MSG_NOSIGNAL` and must not
> alter its host's signal state, while one that already owns the process's
> signals blocks it.
> 
> *(Corrected 2026-10-09, the early ecosystem audit's E2-1: the row this callout calls "the last row" is struck. At `c3bdae2` and after, `ntui`'s premise holds for a program on the floor's runtime, because `SIGPIPE` has a returning handler; it was false at `3d15ac9` and before. The lesson stands: check the disposition at the pin you build on, and do not assume it.)*

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

**Three more from `nitpick-time` 0.1.0, 2026-09-06, all measured at `aaffb87`
and carried on a VERIFIED PASS. They share a cause worth naming: every
specification in this ecosystem was written in the shape of a language that has
private fields and payload-carrying errors, because that is the shape its
authors came from.**

**⚠ THE FIRST OF THESE IS SUPERSEDED AT `c3bdae2`: the language now has what it
lacked.** Measured by `nitpick-time`'s and `nitpick-regex`'s planners on
2026-09-25. `sealed` and `hidden` (D-313, D-314) exist. A consumer's struct literal
of a type with a sealed field is refused (`NITPICK-TYPE-079`), and a declared but
unassigned value cannot be read (`NITPICK-ASSIGN-001`), so a library's *"cannot be
constructed invalid"* can now be made true. **But a sealed field is not a hidden
one:** it still admits a write THROUGH its pointer (`b.buf.ptr[0] = x`) and a
whole-struct copy (`Vec<int64>:w = v`) — **and that copy is a second handle on the block: after `vec_free(@v)`,
`vec_at(@w, 0)` reads the poison, exit 170, a use-after-free measured in `nitpick-time`**; only taking the field's address outside
its module is refused (`TYPE-079`) — the board's question 9. **A sealed field's ADDRESS is a write whatever the callee does:**
`@s.dense` handed to a callee that only reads through it is still `TYPE-079`, so a container holding containers
exposes them by value (`vec_get(s.sparse, k)`) or through its own functions, never `@s.inner`. **And `hidden` binds the
library's OTHER modules too** — `sparseset.npk` reading `Vec.items` is `TYPE-080` — because its line is the declaring
module, not the library. A limited field is
written **`sealed limit<R> int64:f`**, qualifier first; the compiler's
`TYPE_REFERENCE` §9.1.2 example (`limit<R> sealed`) is `NITPICK-PARSE-001`, and is
corrected in its 1.6.0 docs. The bullet below is kept as measured at `aaffb87`.

- **A `pub struct` has no private fields, and `opaque struct:Name = { … };` is
  refused** — the bodyless form is the extern-driver declaration (D-149). So a
  validating constructor guarantees the values **the library produces**, never
  the type: **a consumer's struct literal compiles, links and runs.** Any
  library claiming a type "cannot be constructed invalid" is claiming one
  register more than the language supports. The honest sentence is *this library
  never returns an invalid X, and a caller building one by struct literal has
  opted out*, and the enforceable half is a tree check over the library's own
  `src/`.
- **An `error:` identity cannot carry a payload.** `pub error:E(Detail);` is
  `NITPICK-PARSE-001`, exit 1, no `.ll`. A `Result<T>` is
  `{ T value, tbb32 err }`, so **the error half of every return is a code** and
  there is nowhere for a payload to live. §3's rule below — *declare one
  identity and put the detail in a rich value the caller reads* — therefore
  leaves a real question open in every library: **how does the detail actually
  reach the caller?** Answer it explicitly per repository rather than assuming
  a detail field that does not exist.
- **`fails <Identity>` is not a function-signature clause.** The contract window
  is a closed list: `requires`, `ensures`, `acquires`, `never fails`, `joins`,
  `pure`. **A fallible function simply omits `never fails`.** `fails` is a
  `VerificationKeyword` only because D-002's FFI contracts used it, and D-149
  removed those. It reads so natural that it was written into a *reviewed* plan
  file here and survived all the way to execution — which is the argument for
  this list existing at all.

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
  there is no `pick` while one is plainly in view. *(Changed by the compiler's
  landing 109, DEF-224 under D-352, in every pin since `c9baa9e`: the
  exhaustive `pick` may stand in a bare block at any depth, a statement
  macro's expansion being one, and never inside a conditional, a loop or an
  arm. So a `pick` in a bare block or a statement-position macro expansion is
  found now. Inside an `if`, a `loop` or an arm it is still `REACH-001`.
  From `nitpick-parse` 0.0.0's hand-on; landed 2026-10-22.)*
- **Locks, from the compiler's landing 127 (D-339), for the first library of
  ours that takes one.** A trait method that callers must reach while holding a
  guard declares its level exactly, `acquires N`. `acquires <= N` is a ceiling
  only, and a call through it is legal only with nothing held, or it is
  `NITPICK-LOCK-001`. And a function that hands on a user-levelled lease (a
  struct that is not a `Guard`) writes `acquires N`, since a binding raises the
  held level only to a hold it can see. A helper that takes and releases a lock
  inside and returns a number holds nothing. *(F69, and notice 127, 2026-10-17:
  no program of ours took a lock then; landed 2026-10-22.)*
- **A `buffer`, from the compiler's landing 128 (D-341).** A `#wild_slice` over a
  buffer's `.ptr` is a view of the buffer, so declare it in a block that ends
  before the buffer is written, moved or grown. `nitpick-time`'s `bytes_reserve`
  held two across its `b.body = move(fresh)`, `NITPICK-BORROW-015` twice. And
  the checked `b[i]` and `b[lo...hi]` replace `.ptr[i]` wherever a library wants
  the check. *(F70, and notice 128, 2026-10-17; landed 2026-10-22. Time's adoption
  of `2e1cb4a`, 0.4.0a, owes the first such block.)*

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
  *(Corrected 2026-10-09, the early ecosystem audit's E2-3: O-N9 is DISCHARGED. DEF-3 / D-249 landed at 1.5.1b step 2, and returning a view of a local, `string_bytes` and `string_from_bytes` included, is `NITPICK-BORROW-001` since `94874ce`. "A view is a parameter, never a return value" is still the language's rule (D-004), and the compiler enforces it now, so the harness check this bullet asked for is not owed for it. At `7e91730`, `string_bytes` yields `fixed uint8[]` (D-351; the §2 row on the read-only view).)*
  *(Note 2026-10-15, the compiler's landing 116, DEF-252: STORING a view is held to its block too. A view of a block's local, stored into a holder declared outside that block, is `NITPICK-BORROW-002` (D-004 rule 3 as DEF-42 reads it, since 1.5.5). Since landing 116 so is a CALLEE's store of it: `reset(@c, string_bytes(t))`, with `c` declared outside `t`'s block, compiled and read the freed body after the block, exit 170 at both legs (`nitpick-parse`'s probe 08h). **Our pin `7e91730` predates the fix, so until the re-pin at 118 the callee's form compiles here.** The remedy is the compiler's: declare the holder inside the block, store a copy, or pass the borrow down. The compiler's sweep and regex's renamed copy found the shape nowhere of ours.)*
  *(Note 2026-10-23, the compiler's advance notice F96 at landing 154: **DEF-288 (HIGH) is open in every compiler to 154, our pin `2e1cb4a` included.** The escape analysis reads a `for` binding as a PARAMETER, so a view or the address of one leaves its iteration with no diagnostic: `pass string_bytes(s)` from `for (string:s in arr)` over a local array compiles and its caller reads freed memory, a view of a binding over an inner-block array kept in an outer view local reads freed memory, and `for (Node->:q in ptrs) { pass @q; }` returns the binding's own slot, 107 at -O0 and 0 at -O2. **Until a re-pin carries the fix, keep a `for` binding's view and its address inside its iteration;** copying a scalar or an owned value out is fine, and a pointer is not (DEF-294, below). Open beside it: DEF-289 (HIGH), a pointee's view stored through a slice's element freezes nothing, and DEF-290, `t.p = @t.a; pass t;` hands up a struct pointing into the dead frame. The libraries' seat's census of 2026-10-23 found none of the three shapes in any library's files or plan patches.)*
  *(Note 2026-10-23, the compiler's advance notice F97 at landing 155: **DEF-288 and DEF-290 are fixed at 155**, where a `for` binding is a local bounded by its loop and a self-wired struct cannot leave its frame by value; the rule above holds until a re-pin carries 155. **Three more HIGH rows are open in every compiler, our pin included.** DEF-293: writing the iterated collection while the binding aliases an owning element reads freed memory, and nothing refuses it, so **do not write a collection inside a `for` over it.** DEF-292: `pass @p` of a pointer parameter `p` hands up `p`'s own slot in the dying frame, so **never hand up `@p` of a pointer parameter** (`@p.f` and `@(<-p)` are the pointee's and stand). DEF-294: a parameter's pointer carried out through a `for` binding's value loses its provenance, so the caller's result is not known to borrow the argument; **carry a pointer out by indexing the collection, `ptrs[i]`,** which is tracked. The libraries' seat's census of 2026-10-23 found none of these shapes in any library's files or plan patches.)*
  *(Note 2026-10-23, the compiler's advance notice F98 at landing 156: **DEF-296 (HIGH) is open in every compiler to 155, our pin included.** A view of a pointer parameter's pointee stored through a pointer local (`hp.v = …`, `(<-hp).v = …`, `<-hp = …`), a pointer field on the path, a slice local's element or a callee given a pointer local, into this frame's own storage, freezes nothing, so a later write of the pointee frees what the holder still views. **Until a re-pin carries 154 and 156, hold a pointer parameter's pointee's view only in a bare local declared from it (`fixed uint8[]:v = string_bytes(p.s);`) or in a struct literal at the holder's declaration, or copy the bytes.** At our pin any other store of it freezes nothing: a field or element assignment (`h.v = …`, the DEF-287 hole fixed at 154), a store through an indirection (DEF-296, fixed at 156), and a slice parameter's element (DEF-289's second face, still open). The libraries' seat's census of 2026-10-23 found none of its faces in any library's files or plan patches.)*
  *(Note 2026-10-24, the compiler's advance notice F99 at landing 157: **DEF-289's second face (a view stored through a slice PARAMETER's element) is fixed at 157, and five siblings stay open in every compiler, ours included: DEF-297 … DEF-301 (HIGH).** Until a re-pin carries 157 and their fixes: (1) hold a pointer parameter's pointee's view only as the DEF-296 note above says. Never put it in a slice's element, a slice field or a range's element (DEF-298, DEF-299, DEF-300), and never hand a slice to a callee that stores such a view in it, a slice that is a call's result included (DEF-301). (2) **While a view of an array, or of what one of its elements owns, is live, do not hand any range or slice of that array to a callee that writes through it.** At our pin every compiler admits it, and the callee's overwrite frees what the view reads; 157 refuses a range argument, and DEF-297, the slice local, stays open. (3) Do not hand a callee a view of this frame beside a slice it could store the view through (`put(t, @local)`, `put_ptr(@t[0i64], view)`): 157 refuses it as `BORROW-009`. The libraries' seat's census of 2026-10-24 found none of these shapes in any library's files or plan patches: no function writes through a slice parameter, and our slice parameters are `cstring[]` and `uint8[]`. **Widened at landing 157** (the compiler's census of the open shapes found none in any library or application): DEF-297 covers a slice field as well as a slice local; DEF-298 and DEF-299 cover a pointer field as well as a slice field (`put(b.q, p)`, `b.q.v = view`, `pb.q.v = view`), stored through, or for DEF-299 overwritten under a live view; DEF-301 covers a ternary as well as a call's result. Store a copy, or keep the holder and the viewed storage in one block.)*
  *(Note 2026-10-24, the compiler's landing 158: **DEF-302 (HIGH) is open in every compiler, ours included: a view taken through one name and a write through another, one of the two a pointer to the same storage.** While a view of some storage is live, write that storage through no other name: not through a pointer to it (`hp.o = …`, `(<-hp).o = …`, `<-hp = …`, or a callee given the pointer that writes it), not by the pointee's own name when the view was taken through a pointer (`h.o = …`, `h = …`, or a callee given `@h`), and not through a second pointer to it, a pointer at an element or field of it, or a pointer held in a struct's field, returned by a callee or copied. End the view's block before the write, or take the view as a copy. **DEF-303 (HIGH) is fixed at 159 and open at our pin:** an element reached through a range (`arr[lo...hi][i]`) was compared one position off, so a write through a range under a view of an element reads freed memory. Until a re-pin carries 159, never store or write through a range of an array or a `List`, and never hand a range's element by `@`: index the storage directly. The libraries' census of 2026-10-24 found no store of ours through a range (F100), and the compiler's census of DEF-302's fourteen shapes in our trees runs in 159's harness window.)*
  *(Note 2026-10-24, the compiler's advance notice F101 at landing 159: **once a re-pin carries 159, a slice handed to a writer is checked over its whole extent,** so three safe shapes are refused by design. Do not hand a writer a copy of a slice local while the original lives: hand the original. While a view of one element or one field of an array is live, hand a writer the range of the elements it writes, or the range itself, not a slice local over a wider run. Both spellings are legal at our pin. Writing them now saves an adoption fix at the re-pin. None is in our trees; no function of ours writes through a slice parameter (F99's census).)*
  *(Note 2026-10-24, the compiler's landing 159: **DEF-304 (HIGH) is open in every compiler, ours included: hold no pointer into a `List` element across any operation on that `List` that can grow, shrink, move or drop it** (`list_push`, `list_reserve`, `list_truncate`, `list_clear`, `list_pop`, an assignment over the `List` or a move out of it). A view of the element is refused already, but a plain address is judged by nothing. Take the pointer after the last such operation, or copy the element. By the same reasoning, re-take any pointer into a `Vec`'s or `Bytes`' storage after anything that can reallocate it. **DEF-302 is wider than its fourteen shapes** (nineteen more spellings, measured at 159), and a pointer with no name (a call's result) or one composed with a slice is DEF-305 (HIGH). The 158 note's rule covers them all: write viewed storage through no other name. The compiler's censuses found none of DEF-302's or DEF-304's shapes in our trees. Once a re-pin carries 160 (F102), a re-pointed pointer written under a view of its first target is refused by design, since the resolver is flow-insensitive: read the view before re-pointing, or store a copy.)*
  *(Note 2026-10-24, the compiler's advance notice F103 at landing 161: **DEF-306 (HIGH) is open, and no compiler closes it yet: never replace, reassign or drop a value lent to a spawned task (a `shared_arena`, or anything handed to a spawn) through a pointer to it, or by any name but the one handed to the spawn, while the task may still hold it.** The spawn-lend check tracks the crossing by that root alone. DEF-305 (a pointer that is a call's result, or one composed with a slice) is fixed at 161 but not in our pin, so the 158 note's rule still covers it: write viewed storage through no other name. The compiler's census found none of DEF-306's shape in our trees, and ours finds no `shared_arena` in our files or plans, and no borrow handed to a spawned task but in a refused probe.)*
  *(Note 2026-10-26, the compiler's advance notice F104 at landing 162: **DEF-304 is fixed at 162 but not in our pin, so the 159 note's rule stands: hold no plain pointer into a `List` element across any operation that can grow, shrink, reassign, move or drop that `List`.** Once a re-pin carries 162, such a pointer freezes the `List` (`BORROW-015` at the operation), and one still in scope but no longer used freezes it too (k304b, refused by design): hold the index and read `l[i]` after the operation, or end the pointer's block first. **DEF-307 (HIGH) is open in every compiler: a pointer into a `List` element reached other than by `@l[i]`, a call's result or one carried into a callee that reallocates the `List` through a pointer parameter, is judged by nothing. Write none.** A plain address into a fixed array element is untouched, since an array's storage does not move. The compiler's census found none of DEF-304's or DEF-307's shapes in our trees, and ours finds no `List` in our files or plans.)*
  *(Note 2026-10-26, the compiler's advance notice F105 at landing 163: **DEF-306 and DEF-308 are fixed at 163 but not in our pin, so the F103 and 158 notes' rules stand: never replace, reassign, destroy or move a value lent to a spawned task through a pointer to it, or by any name but the one handed to the spawn, while the task may still hold it; and write viewed storage through no other name, a callee handed a pointer to it included.** Once a re-pin carries 163, a crossing handed to a spawn by a pointer (a pointer local, a copy, a pointer field, a call's result, or an `@place` through a pointer) is lent at its target (`BORROW-016`), and a callee that replaces the whole pointee, handed a named pointer while a view of the pointee is live, is `BORROW-015` at the call. A pointer re-pointed after the lend or the view is refused too, by design, since the resolver is flow-insensitive: store a copy, or read the view and write before re-pointing. **Two faces stay open in every compiler, each HIGH, to be fixed first next week. DEF-309: write no whole pointee, and move none, through a pointer that is a call's result (`(<-(raw f(@s))) = …`, `move(<-(raw f(@h)))`). DEF-310: never `destroy` through a pointer held in a field (`pa.p.destroy()`), which escapes the `TYPE-091` that refuses `sp.destroy()` through a pointer local.** The compiler's sweep moved nothing of ours, and our census finds no spawn lending storage outside the sockets plan's probes, read by eye, no call's result written through, and no `destroy` through a pointer field.)*
  *(Note 2026-10-28, the compiler's advance notice F106 at landing 164: **DEF-309, DEF-310 and DEF-311 are fixed at 164 but not in our pin, so the 158, F103 and F105 notes' rules stand and widen. While storage is viewed or lent, write none of it through the dereference of a call's result, whole or below: not the pointee (`(<-(raw f(@h))) = …`), not a field or an element of it (`(<-(raw f(@h))).o = …`, `(<-(raw f(@arr)))[i].o = …`), not by a move out of it, and not by handing its address to a writer (`wr(@(<-(raw f(@h))))`). `destroy` only storage the function owns, reached through no pointer, slice or `Handle<T>`, the receiver included: never `pa.p.destroy()`, `l[i].destroy()` on a `List` or an array of pointers, or `pb.q.destroy()`. And in a function with a pointer parameter `p`, hand a call's result rooted at `p` (`raw f(p)`, `f` returning a pointer) to no writer, method, dereference write or address while a view through `p` or a spawn's lend of `p` is live.** DEF-311 closes DEF-305's parameter-rooted face, which the F103 note called fixed at 161; it closes only at 164. Once a re-pin carries 164, each is `BORROW-015` under a view, `BORROW-016` under a lend, and `TYPE-091` for the `destroy`. **Two faces stay open in every compiler, each HIGH, before M3. DEF-312: write no pointer field's target two levels below a call-result dereference under a view of what it points at (`(<-(raw f(@ph))).p.o = …`). DEF-307 (landing 165): hold no pointer into a `List` element reached through a call's result or carried into a callee that reallocates the `List`.** The compiler's sweep moved nothing of ours, and our census finds none of the shapes in our files, plans or the Team's branches; our code returns a pointer from one function only, in a refused probe. *Corrected 2026-10-29:* `nitpick-sockets`' probe 08, which runs, returns one too: `loopback`, a `wild int8->` from its own `calloc`, rooted at no parameter, which no rule of this note reaches (found by its 0.0.0 run 5, `be48f70`).)*
  *(Note 2026-10-29, the compiler's advance notice F107 at landing 165: **DEF-307 and DEF-314 are fixed at 165 but not in our pin, so the 158, F103, F105 and F106 notes' rules stand and widen. While a pointer into a `List` element is live, however it was obtained (a call's result handed the `List`, `raw first(@l)`; through a `List` pointer, `@(<-lp)[i]`; kept in a struct's field; a field of the element; or handed to a call beside the `List`), reallocate, replace, move or drop the `List` by no route: not by name, not through the dereference of a call's result, and not through a `List` pointer taken before the address (`(<-lp) = …`, `move(<-lp)`, `list_push`, `list_reserve`, `list_insert`, `list_clear`, `list_pop`, `list_truncate`, `list_remove`, `list_swap_remove`, or a callee that grows or replaces it).** Once a re-pin carries 165, each is `BORROW-015`. One safe shape is refused by design (k22): a struct holding a pointer TO a `List` beside an unrelated element-type pointer is refused at the `List`'s growth, so hold the two in separate bindings or structs. **Five faces stay open in every compiler, each HIGH; write none.** DEF-313 (with M3): store no slice of one parameter's storage into another pointer parameter's pointee (`bp.sl = p2.arr[…]`). DEF-315: call no `Self->` method on the explicit dereference of a call's result under a view or a lend of what it reaches (`(<-(raw f(@h))).m()`). DEF-316: write no slice element through the dereference of a call-result pointer to a slice local (`(<-(raw f(@t)))[i].o = …`). DEF-317: a call's result that is a slice taken from a local struct's slice field (`w(raw g(@b))`) is not traced to that field, so hand none to a writer while its storage is viewed or lent. DEF-312, widened: write nothing two levels below a call-result dereference, through a pointer to a pointer or a pointer field (`(<-(<-(raw f(@hp)))).o`, `(<-((<-(raw f(@ph))).p)).o`). Our libraries hold no `List` (their `Vec<T: Copy>` hands elements out by value), and the compiler's sweep moved nothing of ours.)*
  *(Note 2026-10-29, landing 165 verified at `ba27787`: **DEF-307 and DEF-314 are fixed at 165 but not in our pin, so the F107 note's rule stands. Six more faces of it stay open in every compiler, each HIGH, found by management's diff review of 165 and alike on 164's binaries and 165's; they are registered in landing 166's documents and close together at landing 171, by management's order of 2026-10-29, as the compiler's landing documents record it at `fb0f3d3` (they were set for 168), before M3. Write none.** DEF-318: return no element address from a call handed, by address, a struct, an array or another aggregate that holds the `List`. DEF-319 and DEF-322: hand no element address straight to a call that grows the `List` when it is a call's result, or taken on a place with no root such as a struct literal's field. DEF-320: point at no `List` nested in an element of a recursive type, since "the header never moves" is false there. DEF-321: hold no pointer into an inner `List` across a replacement or growth of that inner `List` through the outer one. DEF-323: declare no holder without an initialiser and then assign it an element address. An element address stored into another `List` is refused from 165. Our libraries hold no `List`, so none of the shapes.)*
  *(Note 2026-10-29, the compiler's advance notice F108 at landing 166: **DEF-315, DEF-316 and DEF-317 are fixed at 166 but not in our pin, so the F107 note's rules for them stand.** Call no `Self->` method on the dereference of a call's result (`(<-(raw f(@h))).m()`). Write no slice element below one (`(<-(raw f(@t)))[i].o = …`), and move none out, hand no writer its address and call no method on it. Hand no writer a slice that a call returns out of a struct carrier (`w(raw g(@b))`), or that is copied by name from a carrier through a pointer (`H2[]:s2 = bp.sl;`), while that storage is viewed or lent. Once a re-pin carries 166, each is `BORROW-015` under a view and `BORROW-016` under a lend. A carrier reached through four pointer links or more is refused as `BORROW-009` even with no view live; hold the carrier in a local and take the slice from it. Some safe shapes are refused by design, so write none: a pointer with two possible pointees handing out a slice; a carrier's slice copied, then written; a pointer re-pointed between taking a slice and writing it; and a slice handed out through two or more pointer links (DEF-325, LOW; a pointer FIELD by name, `w(c1.bp.sl)`, is refused already). **DEF-324 stays open in every compiler (HIGH, landing 167): write no getter that returns a view through an explicit dereference (`pass (<-q).sl`), since its caller's write is silent at every depth.** Every slice our functions return is `fixed`, so none of the shapes occurs in our code, and the compiler's sweep moved nothing of ours.)*
  *(Note 2026-10-29, landing 166 verified at `cd3cb4d`: **DEF-315, DEF-316 and DEF-317 are fixed at 166 but not in our pin, so the F108 note's rules stand, DEF-324's among them, until a re-pin carries 166. Two more shapes are open in every compiler. DEF-334 (HIGH, landing 169 by management's order of 2026-10-29, as the compiler's landing documents record it at `fb0f3d3`; it was set for 168): a function that returns a view of a by-value `string` parameter, as a slice or in a struct's slice field, is legal; but a caller that returns that view, or carries it in a holder, out of the frame or block that owns the argument compiles silently and reads freed memory. Hold such a view only where its argument lives. DEF-339 (landing 168 by the same order; it was set for 167): an async method spawned as `drop recv.m(args)` is no spawn to the escape and aliasing passes, so its arguments' lend and its receiver's crossing go unchecked; spawn none that way. Write none.** Our census14 finds DEF-334's shape in no caller of ours (probe10's in-place use is legal), and the compiler's census over 4,243 files finds no async method spawn of ours.)*
  *(Note 2026-10-29, DEF-345 registered OPEN HIGH by `management_6` at 11:53:32 and measured by `nitpick-compiler_51` on `cd3cb4d`: **`$$m x` of a binding not yet assigned compiles and marks `x` assigned, but nothing binds the callee to write it, and a local whose type does not drop is never zeroed (D-225's vacant value is for dropping types only). So a callee that writes part of a `uint8[16]`, or none of an `int32`, leaves the previous frame's bytes in a binding the caller reads as assigned: 85/85 at both legs for a scalar and for an array's unwritten tail, while a `string` reads as empty. Open in every compiler; the rule is the author's to settle through management, and the fix's landing follows his ruling. Write none: initialise every binding before handing it on as `$$m`, and never read storage that a `$$m` callee may have left unwritten.** Our trees hold no `$$m` in any `.npk` or plan patch (2026-10-29). `nitpick-sockets`' A-22 note, which said the language closes this, is corrected at its 0.0.1 re-cut with a probe 15b.)*
  *(Note 2026-10-29, the compiler's advance notice F109 at landing 167: **D-365, the author's ruling, makes a `=>!` or `=>` between two plain pointer types with unrelated pointees (`hp =>! S->` over an `H2->`) `NITPICK-TYPE-032` in safe code once a re-pin carries 167. Write none now. The same pointee, `any->` on either side, and the `wild` crossings stay legal. DEF-324, DEF-326, DEF-328 … DEF-332, DEF-338 and DEF-341 … DEF-343 are fixed at 167 but not in our pin, so the 158 and F108 notes' rules stand, and they reach every explicit dereference and cast. Write no function that returns a view through an explicit dereference (`pass (<-q).sl`, or `pass (<-hp).s;` of a local). Hand no callee that copies a carrier's slice into its destination (`dst.sl = (<-pl).sl;`) a carrier that dies before the destination. While storage is viewed, write it through none of these: a slice copied from a carrier, a field address a getter returns, a pointer retyped through `any->` or another cast, or a cast or local copy of a pointer parameter. Hand a call no view inside a ternary or a cast beside a write. And address no two-view holder's slice field through a pointer or a getter.** Once a re-pin carries 167, these are `BORROW-015` under a view, `BORROW-001` or `BORROW-002` when a local's view leaves, and `BORROW-013` at a claim beside a cast address. A step the aliasing walk cannot read stands for its root whole, and a write it cannot spell is `BORROW-009`. Five safe shapes are refused by design, so write none: a slice copied from a carrier and written through a dereference with no view live; a two-view holder's field address with no other view live; a disjoint field written through another pointer under a view through an `any->` cast dereference; a pointer re-pointed under a view through its cast dereference; and a disjoint field written through a local copy of a pointer parameter while the caller views another field. **Seven more defects are open HIGH in every compiler: DEF-327, DEF-337, DEF-340 and DEF-344 at landing 168, and DEF-333, DEF-335 and DEF-336 at 169, by management's order. Write none. DEF-327: declare no local that holds a view inside a pick expression's arm, since it gets no party; declare it before the pick. DEF-333: a temporary handed under `raw`, `?!`, `??!`, `relay` or a ternary escapes the temporary refusal, so bind it to a local before the call. DEF-335: hand a slice-storing callee no destination spelled through a pointer field, a dereference, a call's result, a cast, a move, a ternary or an unwrap. DEF-336: make no builtin view (`string_from_bytes`, `#wild_slice`) over a `#ptr_add` result, since the view records no root, and a write or free of the storage beside it is judged by nothing. DEF-337: put no `give` inside a loop, or inside an `if`'s then-branch, in a pick expression's arm. DEF-340: hand a spawn no by-value owner (the rule to come: such an argument crosses only by `move`). DEF-344: while a claim on storage is live, carry no address of it into a struct field, a copy, a callee-built struct or a call's result.** DEF-339 goes to 168 and DEF-334 to 169 (the 166 note), DEF-312 widened and DEF-325 to 170, DEF-318 … DEF-323 to 171 (the 165 note), and DEF-345 (above) to the landing after the author's ruling. The compiler's census finds none of our casts among the 405 D-365 reads. It finds no async method spawn of ours, no by-value owner handed to a spawn anywhere, and no `$$m` of ours. Its sweep moves one file of ours, `nitpick-time`'s probe 10 at :151, by parity, an over-refusal of the escape pass's summary (DEF-351, LOW, by F110), to be respelt at the re-pin that carries 167. Our DEF-336 census finds one site, the same probe's `tail_view` (:106), whose caller frees the block only after the view's last read. Sockets' twenty probes, merged at `049afd0` after the sweep, hold 17 pointer casts, every one a `wild` crossing.)*
  *(Note 2026-10-29, the compiler's addendum F110 to F109: **build 15 replaces build 14, which did not land, with one fix, for DEF-346. A callee that writes through a cast to another pointee type (`(<-(q =>! S->)).x = …` over an `any->` or `H2->` parameter), handed a pointer to viewed or lent storage, is `BORROW-015` at the call once a re-pin carries 167. Its named-pointer face (`any->:ap = (@h) =>! any->; drop wrs(ap);`) is silent in every compiler before 167, ours included. Write none: hand no such callee a pointer to storage that is viewed or lent, inline or named. Five more defects are open in every compiler. Write none. DEF-347 (HIGH, 168): in a callee, copy no pointer out of a pointer parameter's pointee or a parameter's field (`<-pp`, `hh.p`) to write through it or hand it on, since the copy enters no summary. DEF-348 (HIGH, 170): in a callee, write through no pointer field of a pointer parameter's pointee while the caller may view that storage, by any spelling, a `Self->` method or a `dyn` call included. DEF-349 (HIGH, 168): nest no more than three ternaries around a view-maker. DEF-350 (HIGH, 170): write through no pointer that a getter hands out of a holder's field while its pointee is viewed or lent. DEF-353 (MEDIUM, 168): the pointer judges skip a step they cannot read; no shape is named beyond the notes above.** The refusal at `nitpick-time`'s probe 10 :151 is DEF-351 (LOW), an over-refusal: a `#ptr_add` in the callee is read as a whole write of its pointer. DEF-352 (LOW) concerns a ternary's wild provenance under `TYPE-032`, and every pointer cast of ours has a `wild` target. Build 15's sweep over 5,327 files, sockets' twenty probes among them, moves no other file of ours, and DEF-346's refusal kind has no site in our trees.)*
  *(Note 2026-10-29, the compiler's second addendum F111 to F109: **build 16 replaces build 15 (`491ae09`), which did not land, and DEF-346's fix now judges at the caller. A plain address under a pointee-changing cast handed to a callee (`(@place) =>! any->`, or `(@place) =>! T->` to another pointee type) is judged whole at the call, against the views, lends and element addresses of the pointee, whatever the callee does with it: `BORROW-015` (`-016` under a lend) once a re-pin carries 167. Write none now: hand no callee such a cast of a place that is viewed, lent or element-addressed. A pointer value under a cast (`p =>! wild T->`, our shape) stays on the summary road, as F110's note gives it. The D-021 round trip, a callee writing a field through `q =>! H2->` back to the pointee's real type while the caller views another field of it, is refused at 167 as an accepted over-refusal: write through the real type, or end the view first. Two more defects are open HIGH in every compiler, for landing 168. Write neither. DEF-354: a pointee-changing cast inside a getter's argument (`(<-(raw ids(ap =>! S->))).x = …`). DEF-355: a view a getter returns through `(<-(q =>! S->)).x` from a named `any->` local, with the owner then written by name.** Every pointer cast of ours has a `wild` target (census15: 240, with 0 to `any->` and 0 to a plain pointer), so none of these has a site in our trees. Build 16's sweep over 5,327 files moves no file of ours but `nitpick-time`'s probe 10 at :151, DEF-351's artefact.)*
  *(Note 2026-10-29, the compiler's correction to F111: **two roads of the callee summary stay silent in every compiler, landing 166 and build 16 (`49754e4`) alike, the view reading freed bytes, so a re-pin that carries 167 does not close them. Write neither. DEF-356 (HIGH, 169): a view handed on through a callee's cast value. A callee returns `raw gety(q =>! S->)`, or stores it into a destination (`SV{ s: raw gety(q =>! S->), … }`), and the caller writes the owner while it holds the view, inline or named. Write no callee that returns or stores a view it makes through a cast. DEF-357 (HIGH, 169): a typed pointer local made by a cast to another pointee type (`S->:sp = ap =>! S->;` after `any->:ap = (@h) =>! any->;`, or `S->:sp = ((@h) =>! any->) =>! S->;`), written through (`wsx(sp)`, `sp.x = …`, `drop sp.sset()`) while the pointee is viewed. The F109 note's rule, to write viewed storage through no pointer retyped by a cast, holds for such a local after 167 as well.** F111's caller rule holds as stated, for a plain address under such a cast handed straight to a callee. `management_6`'s split ruling of 16:48 re-places the open defects, and its placements supersede those in the notes above: 168 takes DEF-327, DEF-337, DEF-339 and DEF-340; 169 takes DEF-344, DEF-347, DEF-349, DEF-353 and DEF-354 … DEF-357, with DEF-345 if the author approves the middle road; 170 DEF-333 … DEF-336; 171 DEF-312 widened, DEF-325, DEF-348 and DEF-350; 172 DEF-318 … DEF-323; DEF-351 and DEF-352 (LOW) come after 172. Our census16 finds no site of either road: no cast of an address in our trees, every one of our 240 pointer casts on a `wild` value (fresh or reallocated memory, a buffer's or a string's data pointer), no view returned or stored through a cast, and no pointer local made by a cast written through while its pointee is viewed.)*
  *(Note 2026-10-29, the author's ruling on DEF-345, (b), relayed by `management_6` at 17:29: **`$$m` of an unassigned binding is refused when its type does not drop, at compiler landing 169. A dropping type stays legal, since D-225 zero-fills the whole slot, and C#-style `out` rules come later, as a relaxation. Until 169 lands, nothing that ships hands an unassigned binding of any type on as `$$m`. After it, a dropping type is fine, and a non-dropping one stays out: by the compiler's refusal once a re-pin carries 169, and by hand until then.** Our trees hold no `$$m` (census15), so nothing is respelt. `nitpick-sockets`' probe 15b hands on an unassigned `uint8[16]`, which does not drop, so it is refused once a re-pin carries 169 and moves then to `tests/probe/refused/`.)*
  *(Note 2026-10-29, landing 167 verified at `49754e4` (`main` `baebe12`): **D-365 and DEF-324, DEF-326, DEF-328 … DEF-332, DEF-338 and DEF-341 … DEF-343 are fixed at 167, with DEF-346's fix and F111's caller rule, but not in our pin. So the F109, F110 and F111 notes' rules stand until a re-pin carries 167, and the correction's DEF-356 and DEF-357 rules after it as well. Seven over-refusals are now accepted on D-286's list. The seventh: a read-only callee handed a plain address under a pointee-changing cast is refused, as 166 refused it. So hand no callee, of any kind, such a cast of a place that is viewed, lent or element-addressed.** D-366 records the author's DEF-345 ruling (the note above). Our 4,086 programs: 0 different, and 1 newly refused, `nitpick-time`'s probe 10 at :151, DEF-351's artefact, respelt at the re-pin that carries 167. No floor byte moved.)*
  *(Note 2026-10-29, the compiler's advance notice F113 at landing 168: **DEF-327, DEF-337, DEF-339 and DEF-340 are fixed at 168, but not in our pin. So the write-none rules above for all four (DEF-339's in the 166 note, the rest in F109's) stand until a re-pin carries 168, three of them widened as F113 states them. DEF-337's covers a `give` in a pick expression's arm under either branch of an `if`, under a `while`, `for`, `loop` or `till`, or in a `when`'s body, `then` or `end`. DEF-339's covers `drop mod.f(…)` of a module-qualified async function as well as `drop recv.m(…)` of an async method: spawn neither. DEF-340's covers a by-value receiver as well as an argument: hand a spawn no `string`, `List` or struct holding one by value. It crosses only into a `move` parameter, as `move(s)` (`drop takestr(move(s))`) or as `s.clone()`, or as a sanctioned pointer (a Mutex, RwLock, CondVar, Barrier or shared_arena), and a `Channel` by value and plain data cross as before. (Corrected 2026-10-29 by F114: a clone handed to a by-value parameter is a temporary owner, itself `BORROW-004` at 168.) At 168 each is refused. A write of a root viewed by a holder declared in a pick expression's arm is `BORROW-015` there, and a `$$m` claim of it `BORROW-013`, wherever the pick stands. The root written after the pick under such a nested `give` is `BORROW-015`. A spawned method's pointer receiver is `BORROW-004`, and the arguments are lent until the join (`BORROW-016` at a destroy, an assignment or a move of the lent arena under the task). A by-value owner handed to a spawn is `BORROW-004`, whether or not the owner writes (direction (A)).** Five over-refusals are accepted by (A)'s design: a by-value owner whose owner never writes, the receiver's no-write twin, and a temporary owner as an argument or a receiver. DEF-358 is LOW, after 172: the emitter refuses a `for` over a pick expression that gives an array (`EMIT-002`, the checker silent), so write none. census17 finds no site of any of these in our trees. It finds no `pick` used as an expression, and two spawns, both of plain functions, in `nitpick-sockets`' probes. Probe 10's one by-value argument is an `OwnedFd` handed by `move`.)*
  *(Note 2026-10-29, the compiler's correction and addendum F114 to F113, from management's diff review of landing 168: **four more spawn holes are open HIGH in every compiler, 167's and 168's alike, for landing 169. Write none of them. DEF-359: put no pick expression in a spawned method's receiver, in a struct-literal receiver, or in a sanctioned pointer argument of a spawn. DEF-360: spawn no by-value `self` method through a pointer (`drop p.m()` with `p` a pointer, or `drop (@w).m()`). DEF-361: hand a spawn no generic `T` by value where `T` may be a `string` or another owner (`drop f::<T>(x)` in a generic body). DEF-362: spawn no method by a trait-qualified spelling (`drop Tr.m(recv, …)`); spell it `drop recv.m(…)`. At 168 the trait-qualified spelling admits a by-value owner and refuses a legal `move` argument: the one over-refusal 168 introduces, a known bug, fixed first in 169. A fifth hole, DEF-363, registered by `management_6` at 23:02, is open HIGH in every compiler too: call no async method that takes `self` by value through a pointer, at a spawn or an await, since its child frame gets the pointer's words.** The `.clone()` remedy in the note above is corrected in place: a clone crosses only into a `move` parameter. Three more refusals of run-time-clean programs are accepted on D-286's list, by direction (A)'s design: a string literal handed to a spawn by value, a by-value `string` parameter passed on to a spawn inside its callee, and a `fixed` string local. `management_6`'s queue of 23:02 supersedes the placements in the notes above. By its rule of the same message, our texts give a landing number only for the next landing, and cite every later group by its DEF numbers. So the next landing, 169, is DEF-359 … DEF-362 alone. After it, in order, come DEF-363 (the emitter's fix); then DEF-344, DEF-345 (D-366), DEF-347, DEF-349, DEF-353 and DEF-354 … DEF-357; then DEF-333 … DEF-336; then DEF-312 widened, DEF-325, DEF-348 and DEF-350; then DEF-318 … DEF-323; and then DEF-351, DEF-352 and DEF-358 (LOW). DEF-345's refusal (the note at :232) therefore comes with DEF-344's group, after DEF-363's fix, and probe 15b moves once a re-pin carries it. Our trees have no site of any of these. census17, census17d and census17e find no `pick` expression, no method, trait-qualified or generic spawn, and no async method taking `self` by value; our two spawns are both of plain functions.)*
  *(Note 2026-10-29, landing 168 verified at `1143343` (`main` `68f05a9`): **DEF-327, DEF-337, DEF-339 and DEF-340 are fixed at 168, but not in our pin. So the F113 note's rules, as F114 corrects them, stand until a re-pin carries 168. F114's DEF-359 … DEF-363 rules stand after it as well, since 168 does not close them. Fifteen over-refusals are now accepted on D-286's list, 168's five and F114's three the newest. DEF-362's refusal of a legal `move` argument under a trait-qualified spawn is not among them: it is a known bug, refused at 168 only, so spell such a spawn `drop recv.m(…)`.** Our 4,086 programs: 0 different and 0 newly refused; `nitpick-time`'s probe 10 at :151, newly refused at 167, is now refused by both. No floor byte moved.)*
  *(Note 2026-10-29, the compiler's advance notice F115 at landing 169: **DEF-359, DEF-360, DEF-361 and DEF-362 are fixed at 169, but not in our pin. So the F114 note's write-none rules for them stand until a re-pin carries 169, and two of them are refined. DEF-360's: at 169 a by-value `self` method spawned through a pointer is `BORROW-004` whatever the pointee's type, because of DEF-363; write `(<-p).m()`, or copy the pointee into a local first. DEF-361's: at 169 every generic `T` handed to a spawn by value is an owner, `BORROW-004`, a `T: Copy` instance too (a known over-refusal, with a fix owed); so hand a spawn no generic `T` by value at all. DEF-362's spelling rule stands until then too, though 169 removes its over-refusal: spell a spawn `drop recv.m(…)`, never trait-qualified. DEF-363's await face stays silent at 169, so its rule (the F114 note) stands until a re-pin carries DEF-363's fix.** A `.clone()` crosses only into a `move` parameter, as `-004`'s message now says. The compiler's census finds 0 sites of either face of DEF-363 outside its own tests, and census17, census17d and census17e find no site of any of the four in our trees.)*
  *(Note 2026-10-30, the compiler's addendum F116 to F115: **two more spawn holes are open HIGH in every compiler, 168's and 169's alike, and lead the group after DEF-363's landing. Write neither until a re-pin carries their fix. DEF-364: spawn no method on a by-value receiver that holds a borrow, named or inline (`drop h.rd()` with `H = { string->:p; }` taken as `self` by value); its free-function twin `drop rdf(h)` is already `BORROW-004`. DEF-365: hand a spawn no `T`, `Self` or associated type nested in `T?`, `T[n]`, `Result<T>` or a generic struct by value; at 169 the bare `T` is refused by DEF-361's fix, but the named nested faces are silent, and the `Self`, associated-type, `T[n]` and `Result<T>` faces are unmeasured.** F115's item (4) is corrected: only a trait's name before the dot is a qualifier, since the language has no type-qualified call (`PD.m(x)` is `TYPE-007`); the F115 note above does not carry the wording. census17f finds no site of either in our trees: no async parameter, `self` or not, takes a pointer-holding struct by value, and our 4 generic async definitions (sockets' probe06 and its patch copies) take their type parameters behind a pointer and are only awaited.)*
  *(Note 2026-10-30, landing 169 verified at `321f31f` (`main` `214a692`): **DEF-359, DEF-360, DEF-361 and DEF-362 are fixed at 169, but not in our pin. So the F114 note's write-none rules for them, as the F115 note refines them, stand until a re-pin carries 169. The rules for DEF-363, DEF-364 and DEF-365 stand after it as well, since 169 closes none of them: DEF-363's await face is silent at 169, a wrong value in safe code until its fix.** 170 carries DEF-363's fix with DEF-366 … DEF-368, which F117 will announce, and DEF-364 and DEF-365 lead the group after it, by `management_6`'s word of 01:37. Our 4,086 programs: 0 different and 0 newly refused. No floor byte moved.)*
  *(Note 2026-10-30, the compiler's advance notice F117 at landing 170: **DEF-366, DEF-367 and DEF-368 are pre-existing double frees in safe code (95/95 on 168 and 169), fixed at 170 but not in our pin. Write none of them until a re-pin carries 170. DEF-366: call no method whose receiver is `move Self:self` on an owner without `move`, by name, through a field or through a pointer, by UFCS, awaited or spawned; write `(move(x)).m()`, and through a pointer `(move(<-p)).m()`, which leaves the pointee vacant. DEF-367: copy no owner into a move slot (an initialiser, an assignment, `pass`, `give`, a `move` argument or receiver, a literal's element) through a ternary's arm, either side of `??` or `?|`, the value of `?!` or `??!`, the operand of `relay`, `=>`, `=>!` or `=> dyn`, or a part read through `?.`; write `move(…)` at the place inside: `is (c) : move(a) : move(b)`, `move(o) ?? d`, `r ?| move(d)`, `move(r) ?! E`. Plain data stays legal. DEF-368: move no owning part out of a value no binding holds (`(f()).s`, a literal's or a moved value's field, a call's pointee); bind it first, `T:t = f(); string:x = move(t.s);`, or `.clone()` the part.** DEF-363's fix lands at 170 too: an awaited by-value method through a pointer reads the pointee, and a spawn through a pointer is judged by the pointee's type (an owner or a type holding an address `BORROW-004`, plain data crossing); until a re-pin carries 170, the F114 and F115 notes' rules for it stand. After that re-pin, two LOW over-refusals, DEF-369 and DEF-370, refuse legal code: a ternary whose arms move two parts of one value is `MOVE-001` at the second arm (write a `pick`, whose arms take the same moves), and a parenthesised `pick` standing as a method's receiver is `TYPE-007` at each `give` (bind the pick's value first). census17g finds no site of any of them in our trees: our one `move T:self` method is nitpick-regex's refused probe18, and every place handed through those operators is plain data. Our 4,086 programs: 0 different and 0 newly refused. No floor byte moved.)*
  *(Note 2026-10-30, F117's addendum in landing 170's closing lines, from `management_7`'s diff review of 170: **three more holes, pre-existing in every compiler, lead landing 171. Write none of them. DEF-371: write no `Result{value: v}` literal with an owning `v`. At a `return` write `pass v`: the long form copies a place's owner, a double free, and asks none of `pass`'s other rules, so a lent owning parameter, a part of a pointer's pointee, a limited binding's field, a `fixed` binding or an owning `sealed` field from outside its module, handed on by `return Result{value: …}`, is a double free where `pass` refuses it. At any other slot (an initialiser, an assignment, a struct literal's field, a `move` argument) write `Result{value: move(v)}`. DEF-372: name no function with a `move` parameter as a value (`func int32(string) never fails:g = takes;` over `takes = int32(move string:s)`): a call through the value drops the argument twice, since a function type carries no `move`. Wrap it in a function whose parameter is not `move`. DEF-373: never write both `err` and `value` in one `Result` literal (`return Result{err: E, value: v}`): it leaks the owner on every error road and leaves a value no caller can read. The author retired that form, and 171 refuses it. A `Result` literal writes `err` or `value` alone, the long spellings of `fail` and `pass`.** census17h finds no `Result{` literal and no function type in our trees, and the compiler's census, by a scratch refusal build, finds 0 sites of DEF-371 or DEF-372 over the sweep's 5,335 files and the fuzz corpus's 23,898.)*
  *(Note 2026-10-30, landing 170 verified at `b122540`: **DEF-363, DEF-366, DEF-367 and DEF-368 are fixed at 170, but not in our pin. So the F117 note's write-none rules for DEF-366 … DEF-368, and the F114 and F115 notes' rules for DEF-363, stand until a re-pin carries 170. The rules for DEF-364 and DEF-365 (the F116 note) and for DEF-371 … DEF-373 (the note above) stand after it, since 170 closes none of them.** After that re-pin a spawn through a pointer is judged by the pointee's type: plain data crosses, and an owner or a type that holds an address is `BORROW-004`, so transfer the owner, `(move(<-p)).m()`, or hand a clone, `((<-p).clone() ?! E).m()`. 171 is DEF-371, DEF-372, DEF-373 and DEF-374 (LOW, a message), by `management_7`'s ruling (b) of 06:59, and DEF-364, DEF-365 and DEF-362's hardening note follow it with DEF-378, whose faces are the over-refusals DEF-364's fix brings, `(move(<-p)).m()` among them. Corrected in place 2026-10-30 07:13: as filed at 07:00 this sentence gave the 04:29 placement, which that ruling had replaced. Our 4,086 programs: 0 different and 0 newly refused. No floor byte moved.)*
  *(Note 2026-10-30, the compiler's advance notice F118 at landing 171: **DEF-371, DEF-372 and DEF-373 are fixed at 171, but not in our pin, so the F117 addendum note's write-none rules for them stand until a re-pin carries 171. After that re-pin, `return Result{value: v};` is `pass v;` written long: it moves `v` as `pass` does and refuses what `pass` refuses. Anywhere else a `Result` literal's value is a move slot, so a named owner there is written `move(v)`. A `Result` literal naming both `err` and `value` is `NITPICK-TYPE-101`, and a function with a `move` parameter named as a value is `NITPICK-TYPE-100` even when the parameter is plain data: a known over-refusal for `move int64`, so call such a function by name, or wrap it in one whose parameter is not `move`.** DEF-374 rewords TAINT-001's messages and moves no site. Three build-time faces, refused at build and never reaching an executable, are registered and unplaced. Write none of them: an instance of a generic enum inside a generic function (DEF-375, which `llc` refuses), `Self` by value in a trait's default body (DEF-376, `EMIT-002`), and a parameter typed by an associated-type path such as `T.Item`, instantiated at a concrete type (DEF-377). DEF-378 lands with the spawn group after 171 and keeps DEF-364's fix from refusing legal code such as `(move(<-p)).m()`. census17i finds no site of any of these in our trees or in the compiler's `lib/`: no `Result` literal, no function type, no generic enum, no trait method with a default body and no associated-type path. The six both-form literals F118 names are in the nitpick-fuzz copy, the fuzz seat's. Our 4,086 programs, which count that copy's: 2 newly refused, both fuzz programs with the both form, and 0 different. No floor byte moved.)*
  *(Note 2026-10-30, landing 171's closing lines: DEF-379 … DEF-385, registered after its commit with their rows in `b554096`, each pre-existing on 170 and 171 and fixed in no compiler. **Until each is fixed, by `management_7`'s interim guidance of 09:08:19 and 09:52:11: (1) read `.err` only where the error road is established, that is inside `if (r.is_error) { … }`, in the `(true)` arm of `pick (r.is_error)`, or after `if (!r.is_error) { pass …; }`; (2) never `fail` an `Error` that could be zero, such as one read off a success, one arriving through a parameter or a field path, or a field a `$$m` callee may leave unwritten; (3) never make a view with `string_from_bytes` or any other view-maker over an element address `@x[i]`; (4) return a value stored into a `move` parameter with `pass`, not the long form. Write none of these: an assignment to `.err` (DEF-380, a leak, and with a zero `Error` DEF-381, a fabricated success) or to `.is_error` (DEF-382, `EMIT-002`); `return Result{value: p}` where `pass p` would do (DEF-383, a use-after-free the escape summaries miss); a valued enum with no variant valued 0 inside a struct that is declared without an initialiser and claimed `$$m` (DEF-385, a fabricated success); and `return Result{value: v};` in a `comptime func:` (DEF-379, LOW, an over-refusal).** census17j finds no site of any of these in our trees: no `Result` literal, no assignment to `.err` or `.is_error`, and no valued enum. `nitpick-compiler_50`'s census of 09:19, a scratch checker over our 413 files, finds 47 reads of `.err` in 10 files, every one on an established error road; the eleventh file of our 34 code lines reading `.err`, sockets' refused probe 13b, never reaches that walk. The five `fail (self.…_refusal ?? Unreachable)` in time's `FakeHost` double take their errors only from named constants, and our 3 element addresses go to `byteset_add` and `vec_free`, which are not view-makers. DEF-383 lands with 172; DEF-380, DEF-381, DEF-382 and DEF-385 are the Result-fields group; DEF-384 goes with DEF-333 … DEF-336, or with DEF-318 … DEF-323.)*
  *(Note 2026-10-30, landing 171 verified at `224d907` (`main` `b554096`): **DEF-371, DEF-372, DEF-373 and DEF-374 are fixed at 171, but not in our pin. So the F117 addendum note's write-none rules for DEF-371 … DEF-373 stand until a re-pin carries 171, and after it the F118 note's account holds. The rules for DEF-364 and DEF-365 (the F116 note), for DEF-375 … DEF-378 (the F118 note) and for DEF-379 … DEF-385 (the note above) stand after that re-pin too, since 171 closes none of them.** After the re-pin the long form is `pass` written long, a `Result` literal's value elsewhere is a move slot, `TYPE-101` refuses the both form, and `TYPE-100` refuses a function with a `move` parameter named as a value. 172 leads with DEF-364, DEF-365, the qualifier hardening, DEF-378 and DEF-383, by `management_7`'s rulings of 06:59, 07:10, 09:08:19 and 09:52:11. Our 4,086 programs: 2 newly refused, both fuzz programs of our copy with the both form, the fuzz seat's, and 0 different. No floor byte moved.)*
  *(Note 2026-10-30, DEF-386 and DEF-387, by `management_7`'s interim rule of 11:42:38, its remedy corrected at 11:43:13: two HIGH holes, pre-existing on 171 and 172 and fixed in no compiler, numbered at 11:20 and 11:42 and registered in 172's record. The escape collector records nothing for an address whose place has no root, so every reader of a pointer's targets or of a call's argument refs misses it: a view reads rewritten bytes (13/13), an arena is destroyed under its task (a MachineFault, 107/107), and a frame address is handed back past `BORROW-001`, all silent at run time. **Write none of them: no `@` or `$$` of a place whose root is a call's result, such as `@(<-(raw f(…)))`, `$$(<-(raw f(…)))` or `@((<-(raw f(…))).k)`, and no method call through such a pointee, `(<-(raw f(…))).m()`, whose receiver is taken by address, whether as a pointer's new target, a call argument, a receiver or a returned address. Use the pointer the call returns as it is (`hp = raw ids(@h);`, which the analysis tracks), or bind it to a pointer local and use that local. Never re-derive an address from a pointee as `@(<-…)` or `$$(<-…)`.** Their twins with a rooted place are refused (`BORROW-015`, `BORROW-016`, `BORROW-001`). census17k finds none in our trees: no `@` or `$$` of a call-rooted place, no dereference of a call's result, no method call through a pointee, and no `@(<-…)` or `$$(<-…)` at all; the compiler's `lib/` has none either. A census of the library and application sites comes with the fix's sizing at 172's LAND DONE.)*
  *(Note 2026-10-30, DEF-388, by `management_7`'s interim rule of 12:05:42: a HIGH hole, pre-existing on 170, 171 and 172 and fixed in no compiler, numbered at 12:05. A `Result` literal outside a `return` is typed by the enclosing function's success type and wild context, not by its slot. So in a function returning `wild T->`, a plain `Result<T->>` slot takes `Result{value: NULL}` or a wild value unrefused, at an initialiser, a call argument, a struct field or an assignment, and unwrapped and dereferenced it is a MachineFault (107/107). Elsewhere the same literal is over-refused with `TYPE-007` whenever the function's `T` differs from the slot's. **Write no `Result{…}` literal anywhere but as a `return`'s direct operand. Write the value or the error at the `return` (`pass v;`, `fail E;`, `return Result{…};`), or bind the result of a call.** The notes at :241 and :244 still govern a `return`'s own literal. census17j finds no `Result` literal at all in our trees, and `nitpick-compiler_50`'s textual census finds none off a `return` line in the libraries proper, the applications, or the compiler's `src/`, `lib/`, `npkg/` and `tools/`. Our nitpick-fuzz copy's one, `as0307.npk`, is the fuzz seat's, and 171 refuses it as `TYPE-101`.)*
  *(Note 2026-10-30, the compiler's advance notice F119 at landing 172: **DEF-364, DEF-365, DEF-362's hardening, DEF-378 and DEF-383 are fixed at 172, but not in our pin, so the F116 note's write-none rules for DEF-364 and DEF-365 (:238), and :244's rule (4) for DEF-383, stand until a re-pin carries 172.** After that re-pin, a by-value receiver that holds a borrow is `BORROW-004` at a spawn. A type that holds a type parameter, `Self` or an associated type by value (`T?`, `T[n]`, `Result<T>`, a generic instance, `Bx<T>?`) is an owner at a spawn, refused unless its parameter is `move`, and a `T: Copy` instance stays refused. A spawned method's operand before the dot that has no recorded type and is not a trait's name is `BORROW-008`. A read through a live view whose type holds no address then holds no borrow, so a plain struct built from a byte or a length may be spawned by value (DEF-378). `return Result{value: v};` then carries `pass v;`'s escape summary (DEF-383), but its escape verdict still reads the whole literal: DEF-389, a LOW over-refusal, refuses `return Result{value: @hq.k};` as `BORROW-001` where `pass @hq.k;` passes. D-286's list of over-refusals accepted by design counts 16 with d5m. The rules at :246 and :247 stand, their holes fixed in no compiler. census17f and census17j find no site of F119's claims in our trees: no async parameter takes a pointer-holding struct by value, our 4 generic async definitions take their type parameters behind a pointer, and there is no `Result` literal. The sweep moves none of our files. Our 4,086 programs: 0 different and 0 newly refused. No floor byte moved.)*
  *(Note 2026-10-30, DEF-390, by `management_7`'s interim rule of 14:13:20: a HIGH hole, pre-existing on 171 and fixed in no compiler, numbered at 14:13. When a callee stores an address it was handed into storage it reaches through another argument, the caller's analysis records the store only if that destination argument is spelled `@place`, `$$place`, a pointer-typed local name or a slice. Any other spelling leaves the store unrecorded: a pointer-typed field (`hh.ptr`), a call's result, an array element, a by-value struct holding the pointer, or a pointer to a holder, two levels down. A later `pass v;` then hands back a dangling address, silent at run time (13/13). **Write none: pass no address of a local, nor a value holding one, to a callee that stores it through another argument, unless that destination argument is a direct `@local` at the call and the callee stores into that local itself. Through a holder it is the two-level face, silent even when the holder is a direct `@hh` (`setpp(@hh, @x)`). Give the callee the target's own address (`setp(@v, @x)`), or store no frame address through a callee at all and return a value instead.** census17l (its controls 4 of 4) finds no such call in our trees or the Team branches: of 25 storing callees, no call hands an address, or a local holding one, to a destination that is not a direct `@local` or that the callee stores into two levels down. Its one flagged row, `bytes_extend(@c, v)` in time's `tests/unit/bytes_growth.npk`, copies bytes and stores no address. The compiler's `lib/` and our nitpick-fuzz copy show none either. 172 is held for a regression this hole exposes. Widened on 2026-10-30 with DEF-392's note at :252 (`management_5`, 16:12:43): this rule reaches the callees the language calls implicitly, a `for`'s `next` and a template's `to_string`, as it reaches those a call names.)*
  *(Note 2026-10-30, DEF-391, by `management_7`'s interim rule of 14:31:25: a HIGH hole, pre-existing on 171 and fixed in no compiler, numbered at 14:31. An atomic of a pointer type (`atomic<T->>`, legal by D-182) carries a frame address untracked. `.store(@x)` sets no mark on its holder and `.load()`'s result carries nothing, so `v.a.store(@x); pass PS{ p: v.a.load(), k: 0i64 };` hands back a dangling address, silent at run time (13/13), with no pointer and no callee needed. By shape, `swap` and `compare_exchange` are the same family. **Write none: no `store`, `swap` or `compare_exchange` of a frame address (an `@local`, or a value holding one) into an atomic of a pointer type. Prefer atomics of plain values, or of heap-owned or static addresses.** census17m (its controls 4 of 4) finds no atomic of any type in our trees or the Team branches, and so no site. The compiler's `lib/` has one `.store`, of an `int64` value through `atomic_from_ptr::<int64>` in `nbridge.npk`, and our nitpick-fuzz copy has 22 atomics, none of a pointer type: no site in either.)*
  *(Note 2026-10-30, the compiler's addendum F120 to F119: landing 172 is rebuilt as one commit on `b554096`, replacing `99f83e7`, whose face 2 regressed (R1). **:248 stands, with face 2 narrowed: after a re-pin that carries 172, a dereference of a pointer to a frame local is still answered YES, `BORROW-001` at the read as on 171, throughout any function in which some call, a builtin or a builtin method among them, is handed an argument or a receiver carrying a borrow of the frame.** Face 2's relaxations hold only in a function that hands no borrow of its frame to any call. This is a stopgap, a fix owed and not a D-286 item: until DEF-390's fix, a lending function's dereference is refused even where the callee stored the caller's own pointer. To move a pointee out of a lending function, clone it first, `((<-p).clone() ?! E).m()`, or make the transfer `(move(<-p)).m()` in a function that hands no borrow to a call. The rules at :249 (DEF-390) and :250 (DEF-391) stand; both holes go in landing 176, DEF-312's. `mcpy` through `=>! wild any->` and then `pass v;` is the unchecked cast, by design (D-019). census17n finds no function in our trees that dereferences a pointer to its own local, so F120's claim holds and nothing of ours moves; the sweep's sites stay 0. The queue is numbered again: 173 the Result-fields group (DEF-380, DEF-381, DEF-382, DEF-385 and DEF-388), 174 the old list, 175 DEF-333's, 176 DEF-312's, 177 DEF-318's.)*
  *(Note 2026-10-30, DEF-392, by `management_5`'s interim rule of 16:12:43: a HIGH hole, pre-existing on 171 and fixed in no compiler, numbered at 16:12. The compiler's store matrix never applies the store of a call the language makes implicitly. A `for` over an Iterator calls `next(@it)` with no call node, so a `next` that stores `@(self.k)` into `self.p` lets `pass it;` after the loop hand back a frame address, silent at run time (13/13), while the explicit `it.next()` twin is refused. **Write none: no `Iterator` impl's `next` takes the address of `self` or of any part of it (`@self`, `@(self.…)`), or stores such an address anywhere.** **:249's rule (DEF-390) reaches the callees the language calls implicitly as well as those a call names: a `for`'s `next`, handed `@it`, and a template's `to_string`, handed its operand by value. So no `next` or `to_string` stores an address, one it takes or one its receiver holds, into storage reached through a pointer its receiver holds.** That is DEF-390's by-value-holder face in a template: `&{ h }` with `to_string` storing `self.src` into `self.dst.p`, then `pass v;`. census17o (its controls 4 of 4) finds two `Iterator` impls in our trees, regex's probes 12 and 12b, whose `next` takes no address of `self` and stores only integers into it, and no `ToString` impl. The Team branches and the compiler's `lib/` have neither, and our nitpick-fuzz copy's two `next`s take no address. DEF-392 goes in landing 176, DEF-312's, with DEF-390 and DEF-391. 172 is re-cut a third time, `ee62e5b` replaced, for two regressions through these implicit calls, so 172's verified note goes at :253.)*
  *(Note 2026-10-30, the compiler's second addendum F121 to F119: landing 172 is re-cut a third time, one commit on `b554096` replacing `ee62e5b`, which missed the language's two calls with no call node. **:251's lending rule now counts every call, those two among them: after a re-pin that carries 172, a function also lends when it runs a `for` over an `Iterator` by value (the loop calls `next(@it)`, D-166) or a template one of whose items carries a borrow of the frame (it calls `to_string` on each item, by value, D-168), so a dereference of a pointer to a frame local is still answered YES there, `BORROW-001` at the read as on 171.** A `for` over a range, a slice or an array does not lend, nor does one over an `Iterator` reached through a pointer parameter, nor a template whose items carry no borrow. A spawn of an `async` callee does not mark, since a spawn refuses every argument carrying a borrow of the frame but a sanctioned `Mutex` or `shared_arena` pointer; a pipe is `PARSE-014` (D-362). The transfer of an owning pointee is legal only in a function that hands no borrow to a call (D-180's dated note). It is the same stopgap, a fix owed: the twins that store nothing of the frame are refused as on 171 until DEF-390's and DEF-392's fixes narrow the rule. The rules at :249 … :252 stand; DEF-392 and DEF-390's four template and struct-literal faces go in landing 176, DEF-312's. census17n finds no function in our trees that dereferences a pointer to its own local, so F121's claim holds and nothing of ours moves; the sweep's sites stay 0.)*
  *(Note 2026-10-31, DEF-393 and DEF-395, by `management_10`'s interim rule of 00:25: two HIGH holes, numbered from `nitpick-compiler_53`'s probes of an outside review's two leads. DEF-393 is a regression in landing 172 (`2bbc59f`), fixed in no compiler until 173: a spawn handed a sanctioned pointer to a frame local never marks the function as lending, so 172's relaxed dereference (:251, :253) trusts a lock whose interior the task set to a frame address, and `pass move(<-sp)` hands it back, silent where 171 refused it (E1 or a MachineFault at run time, 107/107). DEF-395 is pre-existing on 171 and 172: the same lock leaves by value, `pass move(v)`. **Write none: a function that hands a spawn the address of one of its own locals (`@v`, `$$v`, or a pointer local holding one) neither passes, returns nor stores where it outlives the frame (through a pointer parameter, into a global, or into another spawn's argument) that local by value or a value built from it, such as `pass move(v)` or `pass v`, nor anything read through a pointer to its locals, or a value built from one, such as `pass (<-p)` or `pass move(<-p)`.** A sanctioned `Mutex`, `RwLock`, `CondVar`, `Barrier` or `shared_arena` pointer is the only frame address a spawn accepts at all. census17p (its controls 4 of 4) finds two spawns of ours handed a frame address, both sockets' refused probe 10b (`drop peek(@o)`, `BORROW-004` at the spawn) and its plan-patch copy, which pass back only `NIL`; nothing passed, returned or stored by value or through a pointer. The Team branches and the compiler's `lib/` have none, and the nitpick-fuzz copy's 15 spawns of a frame address pass nothing of the kind. DEF-393 is fixed in landing 173; DEF-395 goes there if its fix is closed and small, else with DEF-390 … DEF-392.)*
  *(Note 2026-10-31, DEF-394, by `management_10`'s interim rule of 00:25: a HIGH hole, pre-existing on 171 and 172 and fixed in no compiler until 173. A template literal (a backtick string with `&{…}` items) calls each item's `to_string` implicitly, and the typer never applies the `pure` or contract call rules to that call, so a template in a `pure` body or in a contract is accepted where the explicit `to_string()` is refused (`TYPE-061`, `TYPE-060`). Through a `limit<Rules>` binding whose clause is a template whose `to_string` stores, it reaches DEF-393's escape hole. **Write none: no template literal in a `pure` body or in any contract, which the typer counts six ways: a `requires` or `ensures` clause, a loop `invariant`, a `Rules` clause, `prove`, and a `decreases` measure. Write the explicit `to_string()` call, which the typer checks.** A template bound to an owning local in a `pure` body is already refused, `TYPE-061` at the binding. census17q (its controls 4 of 4) finds no template literal with items anywhere in our trees, the Team branches or the compiler's `lib/`, and no `for` over a non-range in a `pure` body of ours (management's widening, for a `for`'s implicit `next`); the nitpick-fuzz copy's 20 templates are all in plain bodies. DEF-394 is fixed in landing 173, at the typer.)*
  *(Note 2026-10-31, landing 172 verified at `2bbc59f`: **DEF-364, DEF-365, DEF-378 and DEF-383 are fixed at 172, and DEF-362's hardening is done, as :248, :251 and :253 describe, but not in our pin. So the F116 note's write-none rules for DEF-364 and DEF-365 (:238), and :244's rule (4) for DEF-383, stand until a re-pin carries 172. 172 also carries DEF-393, a regression fixed in no compiler until 173, so :254 stands until a re-pin carries 173 (DEF-395's half until one carries its fix), and :255 until one carries 173. The rest of :244 and the rules at :246, :247 and :249 … :252 stand after a re-pin to 172 or 173, their holes fixed in neither.** After that re-pin, :248's account holds with :251's and :253's stopgap: a dereference of a pointer to a frame local is `BORROW-001`, as on 171, throughout a function that lends any call a borrow of its frame. Verified by one sonnet agent and by hand: the six ladder rows (`npkc.ll` +47,541 B, `npkc.o` +23,216 B and `npkc` +20,736 B; `npkrt.o`, `builder.o` and `builder` unchanged), so no floor byte moved; the sweep over 5,342 files moves only 172's own tests (4,857 → 4,852); the manifest 7,658 obligations over 7,350 rows. Our 4,086 programs: 1,903 identical, 2,183 refused by both, 0 different and 0 newly refused. The landing numbers follow `management_10`'s queue of 00:33: 173 DEF-393 + DEF-394 (+ DEF-395 if closed and small), 174 the Result-fields group with DEF-388, 175 the old list, 176 DEF-333's with DEF-384 and DEF-389, 177 DEF-312's (where :249 … :253 say 176), 178 DEF-318's. The re-pin waits for DEF-286 and management's go (Q67).)*
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
  itself peaks at 11 GiB compiling its own root file — **`src/npkc.npk`,
  renamed from `src/main.npk` at the compiler's 1.5.1b step 1**. Two figures
  circulate for that build and they measure different things: **11 GiB peak
  RSS**, and **10.39 GiB peak *live* managed** from the `NPK_HEAP_STATS`
  instrument built at 1.5.1b step 0. Neither supersedes the other; quote the
  one you mean.

  *(Corrected 2026-10-09, the early ecosystem audit's E2-3: D-246 is SETTLED and landed at 1.5.1b step 4, 2026-09-04. An owning value no place takes is a TEMPORARY of its statement and is dropped when the statement ends, so `f(g(x))` no longer leaks and the binding workaround is not needed at any pin this workbench keeps. The figures above were measured at older pins and are kept as history, not re-measured. The "needed only at OWNING intermediates" test below describes the pre-D-246 leak set. D-246 lists what a statement TAKES (a declaration, an assignment, a `move` parameter, a literal slot, a `pass`) and never registers a view-maker's result.)*

  **The rule is needed only at OWNING intermediates, and the test is exact.**
  A temporary leaks if and only if its type drops — the checker's
  `type_drops`. It **does**: a `string` whose body is on the heap
  (`string_concat`, **`string_slice`, which has been an owned copy since
  D-186**, interpolation, `ToString`); a `buffer`; a struct or enum with an
  owning field or payload; a `dyn`, which owns its cell; an `OwnedFd`. It
  **does not**: a `uint8[]` from `string_bytes` *(corrected 2026-10-09, E2-2: a `fixed uint8[]` from `7e91730`, D-351; still a plain `uint8[]` at `5fbaf4a` and before)*, a `string` from
  `string_from_bytes`, a range-view `arr[lo...hi]`, a plain pointer, any
  scalar. So `f(string_bytes(s))` leaks nothing and needs no binding, while
  `f(string_concat(a, b))` leaks the whole concatenation. One caution on the
  wording: binding does **not** save you if the bound value is then passed
  with `move` into something that leaks it further — but that is ordinary
  ownership rather than this defect, and it is your bug instead of the
  compiler's.
- **Freeing a generic container's block does NOT drop its elements, and
  `exit 0` does not notice.** D-151's leak trap watches `wild` allocations; a
  `string` body is *managed*, so a `Vec<string>` freed without dropping its
  elements retained **125 MiB over two million elements and still exited 0**,
  and hit `HeapOom` under a 64 MiB cap. **"The suite's programs exit 0, so a
  missing `free` is a trap rather than a pass" is a claim about `wild` only** —
  it is written as an unqualified gate in more than one cycle plan in this
  ecosystem and it is not one. A container's `free` must drop each element,
  and the test for it is a memory cap, not an exit code.
- **The runtime poisons freed bytes with `0xAA` on every free** (`npkrt.ll`,
  D-183). A stale read is therefore loud and deterministic rather than
  probabilistic, which is what makes a dangling view *reproducible evidence*
  instead of a flake. Use it: a use-after-free probe asserts the poison.
- **`int64`'s MINIMUM cannot be spelled as a literal in any width** —
  `NITPICK-LEX-004`, because the literal envelope is 64-bit and the magnitude
  is one too large. The MAXIMUM is fine. So **a bound pair written by symmetry
  from a working upper bound is exactly what stops compiling**; build the
  minimum arithmetically instead. **The unsigned half is the same envelope:**
  every `uint64` literal above `INT64_MAX`, `18446744073709551615u64` among
  them, is `NITPICK-LEX-004` at the literal (the compiler's D-148), so build
  `UINT64_MAX` as `I64_MAX * 2u64 + 1u64`. *(`nitpick-parse` 0.0.0 §1.3, probe
  01b; landed 2026-10-22.)*
- **Measure `#size_of`; never derive it from field widths.** A `string` is
  **24** bytes, not a slice's 16, and `enum { Literal(uint16); … }` is **8**,
  not 6, because the payload aligns. Two drafts in one subcycle asserted the
  arithmetic answer and both were wrong.
- **Three spellings that fail with unhelpful diagnostics.** An explicit
  generic argument at a call site is a **turbofish**, `f::<int64>(x)`; plain
  `f<int64>(x)` is `NITPICK-PARSE-002` with no hint. A `pick` arm's variant
  must be **qualified**, `(Part.Year4)` and never `(Year4)`, which is
  `NITPICK-RESOLVE-002` — a `failsafe`'s bare `(HeapOom)` is not a
  counter-example, because those names are the prelude's. And a **lending
  `pick` may not bind a payload that owns heap storage**, `NITPICK-TYPE-046`;
  use `pick (move(v))`, or bind nothing and read through the selector.
- **`#[derive(Eq)]` on a payload enum does not compile, and `#[derive(Ord)]`
  on the same declaration silently compares tags only** — so
  `Literal(7).cmp(Literal(9))` is `Equal`. Raised as **O-N10**. Until it
  lands, do not derive either on an enum with payloads; write the comparison.
  *(Corrected 2026-10-09, the early ecosystem audit's E2-3: O-N10 is DISCHARGED. DEF-4 / D-250 landed at 1.5.1b step 3b: `derive(Eq)`, `Ord` and `PartialOrd` on a payload enum compare the tag, then the payload, since `94874ce`. A payload that owns (`string`, `buffer`, `List`, …) is refused at the declaration, `NITPICK-DERIVE-006`, so write the comparison only for that case.)*
- **`_~argv` marks a parameter DISCARDED, not merely unused.** Reading it is
  `NITPICK-TYPE-007`. A probe or program that wants `argv.len` must spell the
  parameter `cstring[]:argv`. Cheap, and it cost a probe a rewrite.

**`main` takes ONE parameter — write `func:main = int32(cstring[]:_~argv)`.** At
`c3bdae2` `npkc` also accepts `func:main = int32(int32:argc, cstring[]:argv)`,
emits a two-parameter `@main`, and hands the extra parameter an unrelated value
(`argc` negative with no arguments; at `3d15ac9` `argv` was wrong as well).
Reported on 2026-09-25 and confirmed as **DEF-96**: from 1.6.0 step 3c — landed on the compiler's
`main` at `d156c4f` (notice 55), though no pin of ours carries it yet — `NITPICK-TYPE-083` will refuse every `main` that is not exactly `int32(cstring[]:argv)` or
`int32(cstring[]:_~argv)` — no parameter, another type and another return included.
**Moving costs nothing at old pins:** `950bb1d` already accepts the one-parameter form,
so an old-pin control stays byte-identical. The ecosystem's exposure was seven files and
is zero.
*(Corrected 2026-10-09, the early ecosystem audit's E2-3: `NITPICK-TYPE-083` is live at every pin from `c970483` on. `c970483`, `5fbaf4a` and `7e91730` all carry it, and a two-parameter `main` is refused; only `c3bdae2` and earlier accept it. "No pin of ours carries it yet" and "will refuse" are history from 2026-09-25.)*

**`if (a.is_error || b.is_error)` clears neither `Result`'s taint** (`NITPICK-TAINT-001` on the read below it), and `raw` on a
fallible callee is `NITPICK-TYPE-042`: test each `Result` alone. *(`nitpick-time` 0.2.1's plan, 2026-10-01; landed 2026-10-05.)*

**`if (r.is_error) { #unreachable(); }` leaves `r.value` tainted at the pin `5fbaf4a`** (`NITPICK-TAINT-001`), while
`r ?| #unreachable()` compiles. The compiler fixed it at `93bcb66` (landing 93, DEF-225, this workbench's O-N34); it holds
here until the re-pin that carries that landing. *(`nitpick-time` 0.2.2's plan, 2026-10-01; landed 2026-10-05.)* *(2026-10-15, the ecosystem audit's E3-10: the pin `7e91730` carries landing 93, and `nitpick-time`'s 0.3.2a re-measured the statement form there. It compiles and runs on both legs (its `src/span/span.npk`), and O-N34 is struck.)*

**A reference's wording of a diagnostic's cause is not its site.** `0xFF` is `NITPICK-LEX-003` at the literal's FIRST byte,
where `LEXICAL_REFERENCE.md` §6.2 says "at the `x`". Measure a position before a plan, a test or a sentence quotes one.
*(`nitpick-regex` 0.1.4, 2026-10-01; landed 2026-10-05.)*

**At the pin, `int128` multiplication is inline** (`llvm.smul.with.overflow.i128`, no `__muloti4`), and `npkrt.o` defines only
`__divti3` and `__modti3`. *(`nitpick-time` 0.2.3's plan, 2026-10-01; landed 2026-10-05.)*

**At `5fbaf4a` an `async func` has no `npk.<module>.<name>` in the emission.** `npkc` emits its body as
`npk.resume.<module>.<name>` over a frame type `npk.frame.<module>.<name>`, so a reading of the emission keyed on
`npk.<module>.` does not see the function at all. Hold every function the source declares to the emission, and a miss
becomes a red run rather than a smaller denominator. *(`nitpick-time` 0.3.1, 2026-10-08; landed 2026-10-08.)*

**At `5fbaf4a` every `async` body's scope-exit join calls `npk_mono_now`, `npk_join_deadline`, `npk_run_until` and
`npk_thread_join`**, even the prelude's `ByteWriter.flush`, whose body is `pass NIL`. So whether an async function reaches
past the program's memory is read in its source, not in its emission's call graph. *(`nitpick-time` 0.3.1's fix,
2026-10-08; landed 2026-10-08.)*

**The emitter declares the runtime's whole table in every module**, so a `declare` in the emission proves nothing about use.
Read the call edges. *(`nitpick-time` 0.3.1's plan, 2026-10-08; landed 2026-10-08.)*

**A builtin's name is refused only for a function-typed local** (`NITPICK-RESOLVE-001`, the compiler's D-296).
`int64:read` and `int64:mono_now` compile and run at `5fbaf4a`, so "a local named after a builtin is refused" over-claims.
*(`nitpick-time` 0.3.1, 2026-10-08; landed 2026-10-08.)*

**An async prelude method that reaches the kernel is callable only from an `async func`.** At `5fbaf4a`, `ByteReader.seek`
(through `sys(8i64, …)`) awaited, called bare or drop-spawned in a synchronous function is `NITPICK-TYPE-043` each time.
And a ban list of names reads a method by its name alone: `w.read(` matches the builtin `read`, and `r.seek(` matches
nothing. *(`nitpick-time` 0.3.1, 2026-10-08; landed 2026-10-08.)*

**A `while … decreases` loop adds `DecreasesViolated` to every importer's bill, where a `for` over a range does not.**
*(`nitpick-time` 0.3.2's plan, 2026-10-08; landed 2026-10-08.)*

**At `7e91730` a call whose value is `NIL` takes a keyword, and `drop` takes only a `never fails` callee.** `drop g(…)` on a
fallible `g` is `NITPICK-TYPE-042` (*"`drop` is licensed only by a `never fails` callee (D-163)"*), and a bare `g(…);` is
`NITPICK-TYPE-039` (*"a `Result` is discarded here with no keyword"*) whether `g` is fallible or `never fails`. So a
specification's example written with `drop` fixes its callee's fallibility: write the example after the signature.
*(`nitpick-time` 0.3.4's close, writing `0.4.0.md`, 2026-10-15; the four forms measured again at the pin the same day, `drop`
on a `never fails` callee compiling as the control; landed 2026-10-15.)*

**`string_length` is no builtin at `7e91730`** (`NITPICK-RESOLVE-002`, *"cannot find `string_length` in this scope"*). The
compiler's `BUILTIN_REFERENCE.md` lists it in the planned `nlibc` string surface, whose names resolve only where a marked
table also lists them. A string's length is `string_bytes(s).len`. *(The same close and measurement; landed 2026-10-15.)*

**Through a generic bound, or on a pointer receiver, call a trait method with the dotted form.** `f.step()` reaches the
impl through a bound whether `step` takes `Self` or `Self->`, from the compiler's landing 118 (DEF-253 and DEF-254, both
fixed there; at `7e91730` the `Self->` form through a bound names a symbol nothing defines, and `llc` refuses the module).
The qualified form `Src.step(f)` is `NITPICK-TYPE-019` through a bound, by value or by pointer, and on a concrete pointer
receiver; only a concrete by-value receiver compiles it, where `TRAITS_REFERENCE.md` promises the bound form. That is
the compiler's DEF-255, open and low: measured on its landing 112 and still open at 118. *(The compiler's landing 118
and its registry, 2026-10-16; F60's sweep found no qualified trait call in our code or plans.)*

### A file's name is part of the language

A file's `mod:` declaration must equal its basename, and **no identifier may
begin with a decimal digit** — D-147 reserves that opening for numeric literals
so a lexer's first character decides. So no source file may be named
`01_thing.npk`; `mod:01_thing;` is `NITPICK-LEX-003` with `NITPICK-RESOLVE-005`
behind it. Probes are `probeNN_topic.npk` and conformance cases `caseNN_*`.

*Every one of the first six plans wrote `01_name.npk` before anybody compiled
one.* It is the cheapest possible bug and it survived six planning passes.

**This is about to be enforced harder, and the ecosystem should write to it
now.** The compiler's **D-248**, ratified 2026-09-03 and landing in its cycle
1.5.1b, makes `mod:<basename>;` the **mandatory first declaration** of every
source file, and permits `main` and `failsafe` **only in the root file of a
program**. Both are already this ecosystem's house rules, so the cost of
complying early is nothing and the cost of not is that every file breaks at
the re-pin: at the time D-248 was ratified, all seventeen `.npk` files in
`nitpick-time` and all eight in `nitpick-posix` already led with
`mod:<basename>;` and needed no change. Write new files that way and the
re-pin is free. The one shape D-248 forbids that this ecosystem has actually
written is a **macro in a shared module that expands to a `failsafe`** —
`nitpick-posix`'s `tests/probe/shared/pxfail.npk`, which is a *negative*
probe recording a refusal (O-N6, `MACRO-007`) rather than live code, and
which PX-100 already replaced with a generator.

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

**LANDED LONG AGO, AND O-N8 IS STRUCK (2026-09-25).** D-248 is live — a header that does not name its file is refused at the first step with `NITPICK-RESOLVE-012`, *"a file's header names the file"* — and the silent merge above is refused since `94874ce`: O-N8's own shape (a root whose header names a sibling's basename) was measured at all six kept pins on 2026-09-25 — accepted silently at `950bb1d` (exit 0, no diagnostic) and refused `NITPICK-RESOLVE-012` at `94874ce`, `0dfddac`, `aaffb87`, `3d15ac9` and `c3bdae2`. The paragraph above had been describing a fixed defect as live for three weeks, which is the stale-note shape this workbench keeps meeting.

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
5. **A harness check enforces it**: ~~the count and names of public `error:`
   declarations~~ **the identities the tree's reachable `fail` sites raise, keyed
   by (module, name), private declarations included**, diffed against the
   specification's table — `nitpick-time`'s TM-203 is the working shape.
   *(Corrected 2026-09-26, the ecosystem audit's EC3 and EC4: a check keyed by the
   bare name, or by public declarations alone, or matching one declaration per
   line, passes a planted extra identity in silence.)*
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
7. **At `c3bdae2` the floor is six, and two of them are new.** Every program's
   `failsafe` names `HeapBadRequest`, `HeapOom`, `Unreachable`, `WildLeak`,
   **`StackExhausted` and `MachineFault`** — the last two demanded in EVERY
   program since cycle 1.5, the canary included — and a harness's GENERATED `failsafe` templates owe them as surely as its files do. Beyond the floor, REACH demands
   what the program's own code can reach: `DecreasesViolated` wherever a root
   reaches a written `decreases` (20 of `nitpick-time`'s 61 roots, all through its
   own loops — the compiler's *"near-universal"* describes its own programs),
   `LimitViolated` where a limited value is written, `ShiftRange` at a computed
   shift. **`(BadStep)` for a `till` or `loop` with a literal step is spurious —
   the compiler's DEF-95 — so add it where demanded and drop it at DEF-95's
   notice.** `for (int64:i in a..b)` is inclusive and needs no measure and no arm.
8. **The exit codes are ONE convention across every library** (the
   orchestrator's, 2026-09-25): 91 `HeapBadRequest`, 92 `HeapOom`, 93
   `IntOverflow`, 94 `OutOfBounds`, 95 `Unreachable`, 96 `WildLeak`, **106
   `StackExhausted`, 107 `MachineFault`, 108 `DecreasesViolated`, 109
   `LimitViolated`, 115 `ShiftRange`, 116 `RequiresViolated`, 117
   `EnsuresViolated`**, and 99 for the wildcard. The new ones sit above 99 because
   every code from 80 to 99 was already in use somewhere, and 97, 89 and 90 already
   meant different things in different repositories. **A test whose computed exit
   equals an arm code cannot tell its answer from that trap**, so check every
   `// expect-exit:` whenever codes are assigned. **Three more, assigned
   2026-10-22 from `nitpick-parse`'s PA-109: 97 `DivByZero`, 98 `DivOverflow`
   and 110 `StaleHandle`.** 97 and 98 are as `nitpick-time`'s arms
   already spell them. 110 is the prelude's `StaleHandle`, which no library has needed
   yet. *`nitpick-regex`'s `tests/unit/vec_unit.npk:167` exits 110 as an
   assertion's own code, so that code moves below 91 at regex's next dispatch.*
9. **Add arms in the order the compiler can see them.** A REACH-002 demand stays
   hidden while an earlier phase refuses the file — `TYPE-072` refuses a
   clause-less loop before REACH ever runs — so write the loop clauses first, then
   read REACH-002 again, then add the arms. **An arm sweeper matches `(*)` only in
   the code part of a line** (a dry run matched one inside a comment and broke the
   file), and it carries a table of each deliberate refusal's subject, or it arms a
   probe with the one identity whose absence the probe asserts.
10. **A live contract adds an identity, and a live `requires` PRE-EMPTS a trap the body already has.** On an accessor
   whose body traps `OutOfBounds`, uncommenting a `requires` makes the out-of-range call trap `RequiresViolated` (116)
   before the body runs — measured on `nitpick-regex`'s `vec_get`, 116 where it was 94 — and every consumer then owes
   that arm. So *"hand-spell the trap so nothing changes when the clause is uncommented"* is false at `c3bdae2`:
   something changes in every consumer's `failsafe`. The board's Q-6 carries the consequence.

*(2026-10-22: the norm every library states against these rules, the compiler's S-134 R2 and R4 as the author
adopted them, is in [`LIBRARIES.md`](LIBRARIES.md) under Conventions.)*

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
  parser on `[[[[[…` blows the stack, and the language has no stack guard. *(Corrected 2026-10-15, the ecosystem audit's E3-1: false at every pin from `c3bdae2`. The compiler's D-305, settled 2026-09-18, makes a stack overflow "a controlled trap", `StackExhausted`, and every program's `failsafe` names it (§3 item 7). The rule below stands, because a trap still ends the program.)* Use
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
  seen through the lexer — and the compiler's step-0 baseline explains that
  flat memory: escaping that one string **requests 107 GiB in total**, so the
  cost is churn rather than retention, which is why RSS says nothing about it
  and wall time says everything. Controls place the cost in the *declaration*: an
  unread table costs what a read one costs, and 4 000 **separate** `fixed
  int64` bindings cost 0.61 s against one 4 000-element array's 4.19 s.
  **Identifier length is not a fourth axis, but it is an amplifier, and the
  mechanism is now known:** a 4 000-row file using this library's real
  identifiers peaks 11% above the same file built from a generic recipe,
  because the builders copy the accumulated *text* and a longer identifier
  lengthens every copied prefix. The earlier reading — that the
  identifier-length hypothesis "did not survive measurement" — was right that
  it is not an independent axis and wrong to leave the 11% unexplained.
  Raised as **O-N4** (the compiler's DEF-1), reproduced independently by the
  compiler session on a different build, and owned there. **Plan around it
  only by not generating enormous single declarations yet — never by
  reshaping a library's data to dodge it**, which buys the number back and
  buries a compiler bug in library code that outlives it.
  *(Corrected 2026-10-09, the early ecosystem audit's E2-3: O-N4 is DISCHARGED, linear on all three axes since `94874ce` (DEF-1, 1.5.1b step 3, where the builders write into a `Sink`). The numbers above are the `950bb1d` measurements, kept as history. "Plan around it" no longer applies; the second half of the sentence, never reshape data to dodge a compiler bug, stands as a rule.)*

**Evidence a claim at the size you can afford.** An emission *form* — what a
declaration is lowered to — is a property of the lowering and not of the
element count, so 300 rows evidences what 30 000 rows cost 281 s and 30.9 GiB
to observe once. Split a probe's questions by what each actually requires:
"do 30 000 rows compile" needs 30 000 rows, "is it emitted as a read-only
constant with no startup work" does not. And commit the transcript verbatim
with every command's exit code, rather than a prose summary of it — a summary
is not evidence, and `nitpick-time` 0.0.0 had its emission claims failed by
its own verifier for exactly that.

**The pinned tree cannot falsify a claim about unlanded compiler work.** The
pin is a snapshot of what has *landed*. Grepping it and finding nothing proves
"not landed yet" and never "not real" — and while the compiler is mid-cycle
those are wholly different facts. This workbench learned it the expensive way:
told that a view of a temporary refuses as `NITPICK-BORROW-012`, it grepped the
pin, found the highest allocated borrow code was `011`, announced that
`BORROW-012` did not exist, pushed that "correction" into a worker dispatch, a
verifier dispatch, the board and the record — and was wrong. The code is real,
allocated by DEF-3's step 2, living in an unlanded worktree the pin by
definition cannot show.

So when a claim concerns compiler behaviour, **establish which tree it is about
before checking it**, and write the answer down that way:

- **current behaviour** — check the pin, cite `file:line`, and it is authoritative;
- **behaviour of a fix in flight** — the pin is silent by construction. Only
  the session doing the work can confirm it, so ask, and label the fact as
  unlanded wherever it is recorded, naming the step that brings it;
- and when a document here references a diagnostic or rule the pin does not
  have, **that is a finding only if it is stated as current fact.** Stated as
  forward-looking, it is correct and useful.

**And cite the KIND, the branch or the symbol — not the line number.** Line
numbers are a property of one tree and the reader is in another. The dispatch
that carried this rule cited `ir_expr.npk` guards at 8667/8701/8722, taken from
the compiler's HEAD; at the pinned `950bb1d` the same code sits twelve lines
earlier, because an unrelated 1.5.1 insertion landed in between. The structure
was identical and the numbers were wrong, which is the worst combination —
right enough to be believed, wrong enough to send a reader to the wrong place.
`nitpick-time`'s own committed text cites `TY_SLICE`, `TY_ARRAY`, `TY_SIMD` and
`TY_POINTER` by name and is therefore true at both trees. Give a line number as
a convenience beside a name, never instead of one.

The corollary is about challenges rather than checks: **a challenge can be
worth making and still be wrong.** The query above was answered with "the plan
said no new code, and writing the rule found one shape the `@`-equivalence has
no arm for" — a thing the plan had not known, now getting a dated note at its
landing. Being wrong out loud, to a peer who can check, cost less than the
silence would have.

**The bounds guard is emitted for THREE type kinds, and `Vec` is not one of
them.** `../nitpick/src/backend/ir/ir_expr.npk`'s `ExprIndexExpr` calls
`emit_bounds_guard` on `TY_SLICE` (~8667), `TY_ARRAY` (~8701) and **`TY_SIMD`**
(~8722, a lane's constant bound). The `TY_POINTER` branch (~8676-8685) has
none — it goes straight to `getelementptr`. A qualifier is not part of a type
(`parse_type.npk:14-17`), so `wild T->:x` is a bare `TY_POINTER`; and every
`Vec<T>` in this ecosystem is modelled on the compiler's `List<T>`, whose
`items` is `wild T->` and commented "WILD, DELIBERATELY". **So an out-of-range
index into a `Vec` is a silently wrong value, not a trap**, and a library's
`Vec` access is checked by that library or not at all.
*(Corrected 2026-10-09, the early ecosystem audit's E2-3: FOUR kinds. The prelude's `List<T>` is guarded too: `l[i]` is bounds-checked against `count` (D-314), as the §2 index row says. At `7e91730` the four `emit_bounds_guard` calls in `ir_expr.npk` are near lines 10265, 10299, 10320 and 10347, so the positions above are stale. A library's own `Vec` over `wild T->` is still unguarded, and the pointer branch still has no guard.)*

Two things about how this was got wrong, which matter more than the fact:
**four repositories wrote "array, slice and buffer indexing is bounds-checked
and traps" and cited D-070** — whose own title is "`T[]` is a slice: bounds
live in the array type, **not the pointer type**". The sentence is *true about
the types it names* and was read as a general guarantee it never made, which is
the failure to guard against: not a false claim but a narrow one used broadly.
And `check_refs.py` passed all four, because **a wrong citation still
resolves** — a reference check finds what does not resolve, never what resolves
to the wrong thing. Read a decision's scope before citing its number.

**`>>` is arithmetic on a SIGNED operand and logical on an UNSIGNED one — the
operand's signedness decides.** There is one shift arm in the emitter, `ashr`
if signed else `lshr`. There is no `>>>`: it was a documented row that never
lexed, and it would have been a pure synonym if it had. Sourced from the
compiler's own emitter at 1.5.1b step 2, not from a probe — a probe here
measured only the unsigned half, at bit 63.

**Every sweep list in this ecosystem has been wrong on its first telling —
five running.** Four were short and one was **over-long**, so "assume yours is
short" is itself too narrow: assume it is *wrong*. The fourth was written by a
session that had just been handed this rule and was short by two; the fifth was
an orchestrator's dispatch naming four sites a claim had reached, where the tree
held three and one named site did not carry it at all — caught only because the
worker checked the list it was given instead of working from it. The misses were not
careless; each came from a command that did not cover its subject:

- *eight probes carrying a stale comment, and there were nine* — the missed one
  was the file every dispatch is told to skip, so it appeared in no transcript;
- *a `provisional` sweep that missed `Provisionally`* — the pattern was
  case-sensitive and the missed site was the most prominent hedge in the
  repository;
- *four sites claiming "DEF-3 adds no new diagnostic code", and there were
  five* — the fifth used a different wording of the same claim.
- *an enumeration of `npkc`'s `exit 2` sites, short by **two**, with one line
  number off by one* — written by a worker that had just been handed this very
  rule, and caught only by re-reading the source line by line rather than
  grepping it again.

**Confirming that a code path EXISTS is not confirming that your scenario
REACHES it.** Three failures in this ecosystem on one night were the same shape
wearing different clothes: a diagnostic code grepped for in the pinned tree when
the claim was about an unlanded one; line numbers taken from the compiler's HEAD
and quoted as the pin's; and a `pass 2i32` found in the driver, correctly, from
which a conclusion was drawn about imports that never go near it. In each the
observation was accurate and the inference was not. **Before citing a mechanism
as the cause of a behaviour, produce the behaviour** — one four-line file and
one command would have settled the last of the three in under a minute, and did,
once someone ran it.

**A commit subject names a CHANGE, not a FINDING — because a subject cannot be
corrected once it is pushed.** This ecosystem pushed
`cycle 0.0.1: the exit-2 list was short by two, and one of them bites
libraries`, and the six words after the comma are a claim that turned out to be
false. The file was corrected within the hour; the subject is permanent, CI has
run on the tree above it, and every `git log` from now on carries it. A subject
saying what the commit *did* — "the exit-2 list corrected" — would have aged
into a true sentence instead. Put the finding in the body, where a later commit
can answer it.

**And a transcript that claims to be verbatim must show where it was later
touched.** Correcting a wrong number in a committed transcript is the corrected
number **plus a dated note saying what it previously said and how the
correction was obtained** — never a silent edit, which leaves a file asserting
it faithfully records a run that reported something else. Same principle as the
record being append-only: a correction is added, not substituted.

So the rule below is necessary and not sufficient. **Run the grep at least
twice with different phrasings, make it case-insensitive (`-i`), and check the
count against a member you already know belongs.** A list is a claim like any
other and gets the same treatment: it is evidence only when a command produced
it and the command is written down beside it. And when the sweep is a
*deferral* — work handed to a later cycle — an undercount is invisible forever,
because the later worker sweeps exactly the list it is given.

**A list of files is produced by `git grep`, never by recall.** A count taken
from what a dispatch *compiled* is not a count of what is *in the tree*, and
the gap is not random: the files that fall out of working memory are exactly
the ones every dispatch is instructed to skip. `nitpick-time` 0.0.0 reported
eight probes carrying a stale comment and the tree had nine — the missing one
was `probe04_big_fixed_table.npk`, skipped by every dispatch because it costs
281 s and 30.9 GiB, therefore absent from every transcript, therefore absent
from the list. It cost a verifier FAIL and a dispatch. So any residue list,
deferral list or sweep list is generated by a command and pasted with the
command beside it, and the expensive files are the ones to check twice —
because the next worker will skip them for the same reason, and a deferral
that under-counts silently leaves work undone.

**A probe's `expect-` header is a hypothesis, not a verdict.** It records what
the probe was written to ask; the subcycle's results table records what
happened. They agree on a probe that confirmed its guess and disagree on every
probe that found something — which is the case a later reader is most likely to
be looking at. `nitpick-posix`'s `probe02g_cross_module.npk` says
`// expect-exit: 71` and was **REFUSED** `NITPICK-MACRO-007`; read as a verdict
it says a repository's shape depends on macro-generated `failsafe` visibility,
which is the opposite of what the probe established. Read the table.

**A differential check is only as wide as the thing it diffs — and the
undefined-symbol scan every repository here plans CANNOT SEE A SYSCALL.**
Measured, and independently reproduced: a program with `sys(39i64)` in `main`
has **the same 29 undefined symbols** as one without, the sorted sets differing
by nothing, because `npk_sys6` is already the prelude's and the symbol was never
undefined. A scan named "no syscalls" that diffs undefined symbols therefore
passes a program that makes syscalls, silently and for ever.

**The remedy works and is cheap, so use it: scan the IR's CALL EDGES.** The same
pair, run through a call-edge scan, flags the syscaller — `main` calls
`npk_sys6` — and passes the baseline. Every `meta/specs/BUILD.md` in this
ecosystem plans the symbol-diff version; the acceptance item that names it
should be read as unmet until the call-edge scan is what stands behind it.

**And measure the instrument before adopting it.** Counting `@npk_sys6` call
sites gives 2/3 at `-O0` and **5/6 after `opt -O2`**, because inlining
duplicates the floor's own sites. **An IR-shape claim measured only after
optimisation is a claim about the optimiser.** Take the number at both levels
or say which one you took.

**A CHECK THAT DID NOT APPLY READS EXACTLY LIKE ONE THAT PASSED.** A predicate
gating those scans answered "no" for every program when handed a relative path
— silently — so the scans would never have run while the suite stayed green.
This is the **third** shape of the same failure in this ecosystem, after the
`exit 0` leak gate and the `SAFETY.md` bounds promise, and the three together
name the pattern: **a check whose NAME describes the property while its
MECHANISM covers something narrower.** So a predicate that gates a check gets a
positive and a negative case, run against members you already know the answer
for — and prefer a runner that fails when the scanned count regresses over one
that merely prints it, because printing is what "green because it never ran"
looks like.

**`npkc`'s exit codes are an ALPHABET, they are nowhere documented, and rule
B-6 tells every harness here to assert on them.** Read out of `src/main.npk` *(corrected 2026-10-09, E2-3: the entry is `src/npkc.npk`, renamed from `src/main.npk` at the compiler's 1.5.1b step 1)*
and `src/driver/pipeline.npk` at the pin:

| code | means |
|---|---|
| `0` | success |
| `1` | **REFUSED**, with diagnostics — the compiler judged the program and said no |
| `2` | the driver **could not proceed and judged nothing** |
| `3` | a `failsafe` trap |

A `2` for a missing or directory root arrives with an **empty stderr**, silent by
construction, and a malformed command line prints only the usage there. So a runner
that logs only what the compiler said shows *no reason at all* for a failing test,
which is the worst possible presentation of the one code that means the run is broken.
Print the code itself, always. *(Corrected 2026-10-28 from `nitpick-sockets`' T7fix3,
measured at the pin `2e1cb4a`: an unknown argument exits `2` with the usage on stderr
(162 B), as does no argument (129 B); a missing root and a directory root exit `2` with
nothing on either stream. The `3` row had stood after this paragraph, where it rendered
outside the table.)*

**`2` IS NOT A REFUSAL.** A test that expects `1` and receives `2` was never
compiled at all — nothing was judged, so it proved nothing while reporting that
it did. `2` is reached by a **malformed command line**, the clearest case being
a root argument naming a file that is not there: `npkc no_such_root.npk` prints
nothing and exits 2.

> **Corrected 2026-09-04, and the correction matters more than the fact.** This
> entry first said "a `use` naming a path that is not there exits 2", and that
> is **false**. A missing *import* exits **1** with
> `NITPICK-RESOLVE-005: cannot find …` — measured three times by a verifier and
> again here. Only the *root argument* reaches the `pass 2i32` path:
> `graph_load_all`'s return is fed solely by its own direct call on the
> command-line file, while every `use` goes through `resolve_use`, which does
> its own existence check, pushes a diagnostic and returns not-found — so the
> generic "diagnostics exist" branch produces the ordinary refusal. **The
> mechanism was confirmed and the reachability was assumed**, which is the whole
> error: *finding the code path that returns 2 is not finding out what gets
> there.*

**And the real hazard is the opposite of the one first written here, which is
why it was worth getting right.** A missing import produces exit `1` — **the
very code a rejection fixture expects.** So a rejection test whose fixture path
is typo'd, or whose file is later moved, **passes for the wrong reason**: it
wanted a refusal, it got a refusal, and the refusal was about the path rather
than about the thing under test. Nothing anywhere reports this.

So a harness in this ecosystem:

- asserts the **specific integer**, never `!= 0` — `2` means the run is broken,
  not that the program was rejected;
- and for any rejection fixture, **asserts the diagnostic CODE as well as the
  exit code**. Exit `1` alone cannot distinguish "refused for the reason this
  test is about" from "the file was not there". Every library here imports by
  relative path until O-N2 closes, so moved and mistyped paths are the ordinary
  case rather than the exotic one.

**An exit status is ONE BYTE, so any expectation above 255 is silently wrong.**
A program that computes 321 and exits with it reports **65** — 321 mod 256 —
and nothing anywhere says so. The compiler is not involved; it is what `exit`
on a one-byte status does. The compiler session hit this writing a regression
program for DEF-4 and the value it wanted was a sum of comparison results.
**This ecosystem uses exit codes to carry probe results** — `0xAA`/170 for a
poison read, 94 for a bounds trap, 221 and 107 in the derive probes — so it is
our trap and not a curiosity, and it is the same family as the rule below: a
measurement channel narrower than the thing measured, failing silently rather
than loudly.

Two ways out, and pick before you write the probe. **Compose small weights that
cannot sum past 255** — the compiler's own regression pins 121 as
Less 100 + Equal 20 + Less 1, so each contribution is readable from the total
and every other comparison is checked by its own exit code instead. Or **use a
wider channel**: print the value and assert on stdout, keeping the status for
pass/fail alone. Swept 2026-09-04: no `expect-exit` header or recorded exit
claim in this ecosystem exceeds 255, so nothing needs correcting today.

**A timing not paired with an exit code is not a measurement.** A source file
that fails to compile stops early and looks fast, so a failing configuration
is indistinguishable from a quick one on wall-clock alone — and it will be the
*fastest* row in your table, which is exactly the row a curve is most sensitive
to. Record `npkc`'s exit status beside every number, and treat any timing
without one as absent. Both agents who measured O-N4 fell into this before
they were finished; neither would have caught it by reading the output.

**AND THE RULE IS "NO PIPELINE AT ALL WHEN A STATUS IS BEING RECORDED" — NOT
"BEWARE `${PIPESTATUS[0]}`".** Stating it as one idiom's trap is why it keeps
being paid. `$?` after *any* pipeline is the LAST command's status, so a
trailing `| head`, `| tail`, `| sed`, `| wc` silently reports the filter's
success as the measured command's. And `${PIPESTATUS[0]}` does **not** rescue
you inside a command substitution: `t=$(cmd | tail -1)` runs the pipeline in a
subshell, so the array you read afterwards belongs to the outer shell and is
`tail`'s. Three sessions in two days hit this, each having been warned by the
last, and one of them **had written the warning onto the board within the
hour**. The 0.0.1 worker hit it twice: once on a `grep` that matched nothing
and still reported `exit=0`, and once **inside a transcript generator**, where
`ls <missing> | sed` wrote `exit=0` into a file whose entire purpose is
verbatim evidence — caught only because an older recording of the same command
said `exit=2`.

**The tell, in every instance, is a status that disagrees with an artefact:**
a refusal that wrote no `.ll` reporting exit 0, a `grep` reporting success on
no matches. **Use `/usr/bin/time -o <file>` and redirect; capture `$?`
immediately, on its own line, with nothing between.** A pipeline is for
looking; it is never for measuring.

**FOURTH OCCURRENCE, AND THE ONE THAT SETTLES WHAT KIND OF PROBLEM THIS IS: the
0.0.3 worker hit it in its FIRST measurement, in a dispatch whose text told it
not to, in the paragraph it was working from.** `$NPKC --help 2>&1 | head -30;
echo $?` reported **0**; redirected with the status on its own line the same
command is **2** — re-confirmed by the orchestrator. Four sessions, four
warnings, four violations, each by someone who had just read the warning.

**Stop treating this as a thing to remember.** A rule violated by the person
reading it is not under-stated, it is **mis-formed**: the habit of appending
`| head` to look at output is older and faster than any instruction, and it
fires before the rule is recalled. **The fix is mechanical, and the check
already exists in this ecosystem's own vocabulary — pair every status with the
artefact it should have produced**, because a pipeline's borrowed `0` is
falsified the moment you ask what it wrote. Every one of the four was caught
that way and none by recall. **Where a harness records statuses, it should
refuse a captured status that has no artefact assertion beside it**, which
converts the rule from something a session must remember into something a run
cannot omit.

---

**AN EXHAUSTIVE TEST THAT RETURNS EARLY EXITS 0 EXACTLY LIKE ONE THAT RAN — AND
NOTHING ELSE DISTINGUISHES THEM EITHER.** Found by `nitpick-time` 0.0.3 and
worth more than its size suggests, because it is `§6`'s shape in the one place
this ecosystem had assumed it was safe: **the test program itself.** A probe
that sweeps a domain and returns early — a `break` on a boundary, a loop bound
computed one short — exits **0**, writes its artefact, and takes **no less wall
time worth noticing**. Every instrument this workbench has built asks for an
exit code and an artefact; both are present and both are correct. *"Swept the
domain and found nothing"* and *"swept three of it"* are once again
byte-identical.

**The program is the only witness, so make it testify: declare the domain in
the header and require the program to PRINT THE COUNT IT VISITED**, with the
harness comparing that against the declaration and failing on a mismatch. Four
lines of harness. `nitpick-time`'s self-check case 7 is built on exactly this
and its red message names **both** numbers — *"swept 3 of the 10 its header
declares"*. **Any library whose strongest claim rests on a sweep needs it**,
and every library here has one.

---

**A CHECK OVER SOURCE MUST NOT READ PROSE, AND THE FILE MOST LIKELY TO BREAK IT
IS THE ONE THAT DOCUMENTS THE RULE.** The module explaining a prohibition names
the prohibited thing while explaining it: `src/host/host.npk` says `mono_now()`
and `src/lib.npk` says `host_now_utc`, both in comments, so a grep-shaped
purity check **fails the repository on its own documentation**. The failure is
maximally confusing because the flagged line is the line arguing for the rule.
**Blank comments and string literals before scanning — and make the CLEAN
CONTROL a file where the banned form appears in a comment**, so the exemption
is proven rather than assumed. A purity check that passes only because nothing
in the tree documents itself has not been commissioned; it has been lucky.

---

**A NAMED-EXEMPTION LIST IS A STATEMENT ABOUT ONE TREE.** The both-directions
diff that makes such a list safe — every name still present, every present name
still named — is correct for the repository it describes and **fires on every
run against any other tree**. That is not hypothetical: a self-check that
points the runner at scratch trees does it constantly. **Scope the list to the
repository it describes**, and have the check say which tree it is asserting
about.

---

**THE COMPILER'S FRONTEND TOOLS ARE `.npk` SOURCE, NOT BINARIES — SO A HARNESS
PLAN THAT NAMES THEM CANNOT BE EXECUTED AS WRITTEN.** `tools/parse_check.npk`
imports twenty frontend modules and `tools/check.npk` the whole driver
pipeline. *"Build the compiler's tools once per run from the pinned checkout"*
therefore means **building the compiler**, from a tree that is routinely ahead
of the pin. **Any sibling whose harness plan names those tools has a step that
will not run**, and this is the third planning defect of the same family found
in three consecutive subcycles (TM-114's shared stage table, TM-117's assumed
separate compilation, this).

**The substitute, and it is better than the thing it replaces:** `npkc` has no
parse-only mode, but **a diagnostic's CODE FAMILY answers the question** — LEX
and PARSE are the parse phase and every other family is later, so **a file
refused at TYPE, BORROW or REACH necessarily parsed.** No extra tool, no build,
and it reads the compiler's own classification rather than a second
implementation of it.

---

**`NITPICK-REACH-003` LISTS THE IDENTITIES OWED, WHICH MAKES THE COMPILER AN
ORACLE FOR ANY LIBRARY'S ARM TABLE.** Compile a program that imports one module
and has no `failsafe`; the refusal names **every arm a consumer of that module
will owe**. That is the mechanically checkable form of *"and no more"* — the
half no build can catch, because **a superset of the required arms compiles and
runs perfectly**. `nitpick-time` 0.0.3 verified its bills in both directions
against this on three specimens (floor 4; `arms_lib` 5; `calc_lib` 8, which is
S-4b's predicted "four extra arms" measured rather than argued). **Remember the
count is PER PROGRAM** — the same diagnostic names four identities for one
fixture and six for another — so read each program's own bill and never
generalise one.

---

**READ THE COMPILER AT THE PIN, NEVER IN ITS WORKING TREE — AND THE GAP IS NOW
NON-ZERO BY DEFAULT.** Our pin and the compiler checkout are routinely at
different commits: on 2026-09-05 the pin was `0dfddac` while `../nitpick` sat
at `daa5057`, **two commits ahead** — from `git -C ../nitpick rev-list --count
0dfddac..HEAD`, run rather than estimated, after this very paragraph first said
"four" from memory and was corrected by the command it exists to recommend.
A `grep` in that
working tree answers a question nobody asked — *what does the compiler say
today* — while every claim this workbench makes is about **the compiler we
pinned and measured against**. The two failure directions are symmetric and
both silent: grepping the working tree can **confirm a stale claim as current**,
and grepping it for something a later cycle removed can **"prove" a fact the
pin still has**. Use `git -C ../nitpick grep <pat> <pin> -- '*.npk'` and
`git -C ../nitpick show <pin>:<path>`. Both cost nothing, both are exact, and
neither can drift. This is the same shape as everything else in this section —
an instrument whose name says "the compiler" while its mechanism says "the
compiler's tree at whatever commit somebody left it on."

---

**THE WRITE GUARD CANNOT SEE AN INTERPRETER HEREDOC, AND THIS HARNESS TELLS
SESSIONS TO USE ONE.** Measured 2026-09-05 by feeding `tools/guard_compiler_tree.py`
PreToolUse payloads on stdin, four controls against one existing compiler-tree
file:

| form | verdict |
|---|---|
| `echo x > <compiler file>` | **DENIED** |
| `sed -i s/a/b/ <compiler file>` | **DENIED** |
| `Write` tool at `<compiler file>` | **DENIED** |
| `python3 - <<PY` … `open('<compiler file>','w')` … `PY` | **ALLOWED, silently** |

The guard's own docstring states this limit and names the mitigation: *"The
airtight mechanism for the first is the sandbox's `filesystem.denyWrite`."*
~~**That mitigation is not deployed.** `denyWrite` appears nowhere
in `~/.claude/settings.json` or any project settings; `permissions.defaultMode` is
`auto` and the only hook wired is the guard itself. So the compensating control
the limit is documented against does not exist in this installation.~~
*(Corrected 2026-10-09, E2-7. True on 2026-09-05, when this was measured; the sandbox was deployed on 2026-10-01. A user-level `denyWrite` entry had been added by 2026-09-30, but with the sandbox off it did nothing (`RECORD.md:8372`). On 2026-10-01 12:39 the sandbox was applied at the author's go, in this workbench's untracked project settings: `sandbox.enabled`, `denyWrite` on `../nitpick`, `allowUnsandboxedCommands: false`. The lock was checked live, and a shell write outside the allowed paths was refused "Read-only file system" (`RECORD.md:8454-8458`). The inert user-level block was removed at the same time (`RECORD.md:8457`). On 2026-10-07 23:14 it was widened, at the author's request, by an `allowWrite` list for the test VM's runner (`RECORD.md:9420`). `BOARD.md:158` records the state: shell writes go only to the listed paths, and "`../nitpick` is read-only". The "only hook wired" clause is also stale: a `PostToolUse` context-warning hook has been on trial in this workbench since 2026-09-27 (`RECORD.md:7997`).*

*What the guard still cannot see, and the sandbox does not cover:*

- *The sandbox confines shell commands only; Edit and Write stay under the permission system (`RECORD.md:8372`). For those two tools the guard is the only control, and it refuses them correctly (table above).*
- *The settings file is for sessions started in this workbench (subagents inherit it). The author scoped it that way because a user-wide `denyWrite` would block the compiler's own sessions (`RECORD.md:8361`). A session started in a library or an apps repository runs under whatever settings that directory has, and none of this workbench's documents show them.*
- *The sandbox allows writes to the whole workbench tree and to `../nitpick-apps`. An interpreter heredoc into a library that `BOARD.md` does not show claimed (W-7), or into a workbench file by a session that is not the named writer (W-16), is therefore seen by neither the guard nor the sandbox. The sandbox closes the compiler tree and nothing else.*
- *The VM runner is excluded from the sandbox. It runs unsandboxed, outside `denyWrite`, when called bare.*
- *The settings file is untracked, and nothing in the tracked tree checks that it is present or that the installed Claude Code still accepts its keys (`RECORD.md:8421`: a rejected value once made a file be skipped). A lapse would leave no refusal, no finding and no record.*
- *Whether the guard's limit was ever reached is still unknown: nothing in the record measures it either way.*

**What makes it matter rather than merely exist:** a harness may ship a standing
instruction to prefer `sed`, heredocs and short scripts over the `Write` and
`Edit` tools — for its own reasons, unrelated to any of this. **This one does.**
A session under that instruction writes through the single form the guard cannot
judge, *by default and for every write*, and leaves no trace that it was not
watched: no refusal, no finding, nothing in any record. `CLAUDE.md` says the
write rules are "enforced by the guard where they can be", and a later reader has
no way to tell which writes those were.

The exposure that matters is not the orchestrator's own board edits — those are
writes it is entitled to make — but a **library worker** following the same
ambient instruction into `../nitpick`, which is the one thing
`library-sessions-write-scope` exists to prevent and which can invalidate a
verification run that has been going for hours.

**Do not read this as "the guard is broken."** Three of its four forms refuse
correctly, and a first draft of this very finding wrongly recorded `sed -i` as a
gap — the test used a path that did not exist, and the `sed` branch requires
`os.path.exists` precisely so a sed *expression* is not mistaken for a filename.
That check is correct and the retraction is the point: **a guard test must use a
target that exists, or it measures the test rather than the guard.**

*Sourced from the `devteam` pipeline's own finding "an ambient harness
instruction can silently disarm the guard", which was derived from this system
and met the same shape from the other side.*

**IS COMPLIANCE VISIBLE IN THE PRODUCT?** The most useful design test this
workbench did not have, and the one to apply to every rule written here. A rule
that asks somebody to be careful is not a mechanism; a rule that puts the
command beside the number it produced is, because a reader can check it without
re-running anything and whether or not the author was careful. This is why
`meta/DECISIONS.md:550`'s *"produced by `git grep -n 'D-151'` and not from
recall"* was worth writing even though the list it produced was still short —
the command was visible, so the gap was findable.

**AWARENESS IS NOT IMMUNITY — and this workbench keeps proving it in the
artifact where it documents the rule.** The 2026-09-04 session invented `RX-121`
minutes after writing the rule that numbers must come from the registry, and
then cited a nonexistent `RX-127` in the very note recording that collision. In
the same session it **silently deleted a paragraph of `BOARD.md`** with a
boundary-matched replacement, and `check_refs.py` was **clean straight across the
deletion**, because a removed paragraph breaks no reference. Every one of those
was committed by the session most steeped in the discipline at the moment it was
most steeped in it. **Prefer a check that fails to a rule that asks for care**,
and note the specific gap: nothing in this workbench detects *deleted content*.
Replace an exact known string rather than a span to the next blank line, and
when a span must be used, print what it consumed.

**`grep -r` AND `git grep` FROM THE WORKBENCH ROOT BOTH SEE ZERO LIBRARY FILES,
AND BOTH REPORT IT AS SILENCE.** Measured 2026-09-05, on `derive` in `*.npk`
across the tree: `grep -rl --include='*.npk' .` from the root → **0**;
`git grep -l -- '*.npk'` → **0**; the same grep aimed at `nitpick-time` → 7;
`grep -r --no-ignore-files` → **14**; `find … -print0 | xargs -0 grep -l` →
**14**. Two independent causes converge on one silence:

- **`grep` on this machine is `ugrep` 7.8.4, installed at `/usr/bin/grep`.**
  `grep --version` reveals it; `which grep` does not. ugrep honours ignore
  files in recursive mode, and this repository's root `.gitignore` opens with
  **`/*/`** — every top-level directory ignored, which is precisely how the
  workbench avoids embedding a library as a gitlink. **The rule that makes the
  repository correct is the rule that makes its sweeps blind.**
  **And given several files it prints in COMPLETION order**, not argument order —
  per-file counts and `grep -h` lines alike — so compare such output as a set, and
  read per file whenever the file matters (measured twice, 2026-09-25).
  *(Corrected 2026-10-05, measured: in the Bash tool, `grep` is now a shell FUNCTION that runs ugrep, and `/usr/bin/grep`
  is GNU grep 3.11. So the ugrep behaviour above belongs to plain `grep`, and `/usr/bin/grep` is the GNU instrument; name it
  when GNU behaviour is the claim. Found by `nitpick-regex` 0.1.3's planner, 2026-10-01.)*
  *(And the consequence, found at `nitpick-time` 0.2.3: the Bash tool's `grep` runs `ugrep --ignore-files`, so an Expect taken
  in a fresh `bash -c` is GNU grep's, while the same command typed into the Bash tool reads with ugrep's ignore-file rules.)*
- **`git grep` from the root cannot see a library either**, for an unrelated
  reason: each library is a *separate checkout*, so none of its files are in
  this repository's index.

**This is the worst form of the name-versus-mechanism shape, because it
produces no output to be sceptical of.** A `check_refs .` run at least prints
the name `nitpick-libs`, so a reader can see the denominator is one. **A sweep
that matches nothing prints nothing**: *"swept, no violations"* and *"swept
nothing"* are byte-identical, and there is no count to demand the denominator
of. Both of this workbench's own disciplines — *a list of files is produced by
`git grep`, never by recall*, and *ask for the denominator, not the verdict* —
route straight through it.

**It has already cost a real site list.** The stale citations to the deleted
`src/frontend/list.npk` were recorded as five sites in two files; re-derived
with a working instrument they are **six in three**, including two in a file no
sweep had ever opened. The old sweep matched the token `List` while the
property was *"cites the deleted `list.npk`"* — so it caught one line by
accident and missed every basename citation. **And the `.gitignore` that causes
this documents the same failure once already**, in its own comment: a directory
must be un-ignored by name *"or it vanishes silently — which is exactly what
happened on the first attempt to add the plugin."* That note was about
tracking. Nobody carried it across to searching.

**DO NOT GENERALISE THE RATIO — GENERALISE THE ASYMMETRY. The compiler
repository shows the same mechanism with the opposite consequence, and the raw
numbers there look identical to a bug.** Measured independently 2026-09-05:
from `../nitpick`'s root a plain sweep sees **19** `.npk` while
`--no-ignore-files` sees **76**, a 75% gap that reads exactly like ours. It is
not one. **All 57 of the difference are under `.internal/wt`** — live worktrees,
which are *copies* of the source — and excluding duplicate checkouts from a
source sweep is correct. `src/` itself is fully visible: 81 either way, 80
tracked. **Here the ignored directories ARE the subject matter; there they are
duplicate copies of it.** Same mechanism, opposite meaning, and only the first
is a defect. *"The compiler has a 75% blind spot"* would have been true as
arithmetic and false as a claim.

**Where it does bite over there**, and it is worth knowing rather than assuming:
a sweep meaning *"is this fix present in all three in-flight worktrees?"* would
silently see none of them, because those are exactly the ignored paths. The
question decides whether the ignore is right: **ask whether the ignored
directories are copies of your subject or instances of it.**

**THE RULE.** A sweep spanning libraries is run **per repository by name**, or
with `find … -print0 | xargs -0 grep`, or with `--no-ignore-files`. Never a
bare `grep -r` or `git grep` from the workbench root. **Commission the
instrument before believing it** — two independent tools agreeing on the same
file set is a measurement; one tool's silence is not. And **state the
denominator with every sweep result**: a sweep reporting no matches must also
report how many files it opened, or it has reported nothing.

**AND THE RULE HAS A LIMIT NOBODY HAD WRITTEN DOWN: WHEN THE PROPERTY IS NOT
LEXICAL, NO SWEEP IS THE CHECK — INCLUDING A CORRECT ONE.** This ecosystem's
standing discipline is *a list of files is produced by `git grep`, never by
recall*. That rule is right about **recall** and silent about **predicates**,
and four sessions in a row reached for `git grep` on a property it cannot
decide.

**The case, and the count is the evidence.** The stale citations to the deleted
`src/frontend/list.npk` were counted **five**, then **six**, then **seven**,
then **ten** — four sessions, four numbers, each produced by a real command
over a real denominator, each disagreeing with the last. The property is
*"cites the deleted file as though it still exists"*. **The same string appears
in a stale citation, in an accurate historical note (*"it **was**
`src/frontend/list.npk`"*), in a correction (*"now prelude functions **rather
than** `list.npk`'s"*), and in the proof that the file is gone (`git cat-file
-e <pin>:src/frontend/list.npk` → exit 128).** A sweep sees one class where
there are four. The final count of ten included **the very records documenting
the fix**, and the true answer to the question actually being asked — *how many
stale citations remain* — was **zero**.

**The tell that you are in this case:** the property contains a claim about
**truth or tense** — *cites something deleted*, *describes current behaviour*,
*is still accurate* — rather than about **presence**. Presence greps. Truth
does not. **A sweep is then the way you build the CANDIDATE list, and reading
is the check** — so report both numbers, *"N candidates swept, M confirmed by
reading"*, because a single number silently claims the sweep was the check.

**Why this outranks the ordinary version of the rule.** A blind sweep
(`grep -r` from the root) returns zero and is caught the moment anyone asks for
the denominator. **A lexically correct sweep of a semantic property returns a
plausible number over a stated denominator and survives every check this
workbench has** — it looks exactly like diligence. That is what let one count
be wrong four times while each session did the thing the playbook told it to.

**Three tooling facts from the 1.5 re-pin, 2026-09-25.** **The loop sweep's own tool
stopped compiling when it was archived:** `done/1.5/tools/loop_dump.npk`'s relative
`use` paths are one level short at its new depth, so notice 44's recipe fails as
written — build a copy at its pre-archive depth in scratch (the compiler fixes it in
its 1.6.0 docs). **A field-position `awk` over a transcript's prefixed `nm` lines
(`  | `) prints addresses, not sizes** — the prefix shifts every field, so a
comparison of sizes silently compared layout. **The widened leak scan fails any
repository whose committed transcripts hold absolute paths** — it has read every
tracked text file since 2026-09-06, after some transcripts were already committed —
and a failing scan blocks every worker commit, so check each sibling before its next
dispatch. **`check_refs` credits a passive-voice supersede to the NEAREST decision id before the word**, so a
row naming the new decision and then the old one in the passive reads as the new one replaced — write the active voice,
*"it supersedes <old>"*. **And a checked tag guards only itself:** `check_denominators` passed a harness whose prose said
33 beside its tag of 34, because the tag is checked and the untagged number beside it is not. **`gh run view --log` and `--log-failed` can print
nothing and exit 0 for a run whose log exists** — measured twice on 2026-09-25 — so read a run's log through
`gh api repos/<owner>/<repo>/actions/jobs/<job>/logs`, and never conclude from an empty print that there is no log. *(2026-10-15: a run-level `gh run view --log` printed 110 805 B for `nitpick-time` 0.3.4's plan verifier, so it can print the log as well as nothing. Either way it proves nothing about a job: read per job.)* *(2026-10-16: the shell tool's `allowed_domains` takes hosts, not patterns. Each entry is a domain (`api.github.com`), a wildcard only as a whole leading label (`*.blob.core.windows.net`), or an IP address, any with an optional `:port`. No scheme, no path, and no `*` inside a label: `productionresultssa*.blob.core.windows.net` is refused. One bad entry refuses the whole call before any of it runs, its `mkdir` included, so a later call that relies on it fails too. Three agents met it on 2026-10-15 and 2026-10-16, each on a job log. The list that worked each time for a job's log: `api.github.com`, `*.actions.githubusercontent.com` and `*.blob.core.windows.net`.)* **The general rule:** a tool that turns "nothing parsed" into an empty success is a silent wrong answer, and a cache can
hide it for hours (re-found 2026-10-01 by the sandbox trial; landed 2026-10-05). **A lexical "literal divisor" rule must require the literal
to stand ALONE:** one that allows an optional `(` and ends at `\b` admits `/ (400i64 + m)` and `/ 256i64 =>! uint8` —
which is 0 — so nothing that binds tighter than `/` may follow it (the compiler's `OP_REFERENCE` §0). **And a helper's
docstring is a claim to measure:** `nitpick-time`'s `code_lines` never blanked string bodies, though a retired check's
docstring and a reviewed plan both said it did.

**Reading source the way the compiler does — `nitpick-regex`'s fifth audit, 2026-09-25.** **Python's default text mode is
not the compiler's reading:** `newline=None` makes a lone carriage return a line end, while the compiler ends a `//`
comment at byte 10 only — so `// note<CR>use "x.npk"` is an import to the harness and a comment to the compiler. **Open
`.npk` source as bytes** (or `newline=""`). **And a `use` path is the string literal's DECODED value** — an escaped
`"..\x2f…"` path hid a syscall from the scan while the compiler followed it. **A check that clears a type by resolving
its name must refuse what it cannot resolve** (a macro splice named after a POD struct was cleared as that struct).
**A skip that prints nothing shows only as a denominator one short — print the skipped set.** **A tool that echoes its
path argument prints a home directory when handed `$W/…`**, and the leak scan then fails the record that pastes the
line — hand such tools relative paths. **A plan's hunks that carry whole `[[sweep:]]` tags turn its own commit red** —
spell tags differently in the plan and let the apply script write them whole; **prose that describes `check_refs`'
supersede trap re-triggers it**; and **a TM number in a script's printed output is a citation once quoted in a plan.**

**What `check_refs` and `check_denominators` actually read — measured at `nitpick-time` 0.1.3 and 0.1.3b, 2026-09-25.**
**Links resolve even inside fences**, so a specification hunk embedded in a plan must also resolve from the plan file's own
directory. **Decision and question citations are counted in prose with fences stripped but inline code NOT stripped**, so an
inline `PD-28 -> TM-177` cites a decision that does not exist yet — and so does a record naming *"the next free number,
TM-177"*: write *"the number after TM-176"*. **Any `O-<letter><n>` in a tracked markdown file's prose is read as a question
THAT repository must define**, so a library citing a registry id (O-N20) first needs its own entry for it, as `nitpick-time`'s
O-N17 to O-N19 have — a dispatch that says "cite the id" implies the entry. **`check_denominators` scans `meta/roadmap/`**, so a
plan that quotes tool output must mask whole sweep tags there. **And `check_specs_current` is report-only** — it never fails a
run — yet its expected lines still belong in a plan's expected output, or a careful executor stops on *"unresolved"*.

**What running a plan's tools taught — `nitpick-regex` 0.0.4e's rehearsals and its sixth W-22 audit, 2026-09-26.** **Importing a workbench script is a write:** `importlib` on `check_record.py` left `skills/check/scripts/__pycache__/` in the WORKBENCH, a W-16 breach from a library worker. Run a workbench tool as a program or under `python3 -B`, and read `git -C "$WB" status --short` before reporting. **`check_record` accepts a title's `— PLANNED` only without a date.** **`check_refs` reads a closing square bracket followed at once by an opening parenthesis as a link** — a slice-returning signature before its parameter list, even in a fence or a comment — so spell the type apart. **An edit engine's hand-amendment check must compare whole lines:** a new line that is a PREFIX of an old one matched, and the engine STOPPED on its own first edit. **A scratch commit made partway through a rehearsal sweeps the blocks' staged `git mv`s into it and falsifies the tally** — measure tallies in a clean clone. **This environment's safety check refuses `rm -rf "$A/x"`**, so every removal in a plan names `${VAR:?}`. **And a move with heavy edits needs a stated rename threshold:** of the nine `git mv`s in `06d5c00`, git's default similarity (`-M50%`) finds 1, and it takes `-M25%` to find all nine. A record that counts renames says which threshold it counted at — or moves in one commit and rewrites in the next, so git follows every move at its default. **And from `nitpick-time` 0.1.4c's planning, the same morning:** a script that tells an old pin from a new one by comparing against ONE pin's name goes wrong at the next pin — `0.1.4.md` §3's `importscope.py` (`pin == "c3bdae2"`) would strip the new arms at `c970483`; compare against an ordered list of pins. **A re-pin's sweep includes the programs no harness stage runs** (`nitpick-time`'s tzdb spike). **A number printed zero-padded in decimal where a tool conventionally prints hex** (the spike's `nm` sizes) reads wrong in base 16 — print the radix. **`nitpick-time`'s `check_specs_current` reads fenced text**, unlike `check_refs`, so a plan quoting a sweep that prints a new TM number cites it: mask new decision numbers in quoted output.

- **`pkill -f` and `pgrep -f` match their own command line.** A pattern that names the job also names the killer, so
  stop jobs by PID. *(`nitpick-regex` 0.1.3's plan, 2026-10-01; landed 2026-10-05.)*
- **Never leave the shell inside a library.** The sandbox's write list names `.`, and a `cd` that persists moves both the
  harness's idea of the session's working directory and what `.` may mean. Name a library by `git -C` or an absolute path;
  a subshell `( cd … )` is fine. Re-found 2026-10-02, when `nitpick-libs_13`'s `cd` into `nitpick-fuzz` moved the session's
  directory until it was moved back. *(`nitpick-time` 0.2.2, 2026-10-01; landed 2026-10-05.)*
- **Inside the sandbox, `ps` sees only its own call, and a `&` job dies with the call.** A leftover-process check rests on
  the harness's completion notice and the scratch, never on `ps`. *(2026-10-01; landed 2026-10-05.)*
- **A `\u` escape typed into an agent's tool call can arrive decoded.** Write such codepoints with a program (`chr()`), and
  grep for them the same way. *(`nitpick-regex` 0.1.4's plan, 2026-10-01; landed 2026-10-05.)*
- **A bash heredoc whose text contains its own end-marker line ends early** and runs the rest as shell. Write long text
  with a file tool. *(`nitpick-time` 0.2.4's plan, 2026-10-02; landed 2026-10-05.)*
- **A fence found by `text.index("### 4.2 ")` can match the plan's own block code.** Anchor at a line start.
  *(`nitpick-time` 0.2.3's plan; landed 2026-10-05.)*
- **A scratch tool's absence is a claim to check where its maker kept it**, not a fact. *(`nitpick-regex` 0.1.5, 2026-10-02;
  landed 2026-10-05.)*
- **`git apply` run from a scratch copy inside a checkout resolves its paths against the checkout.** Use `patch -p1 -d <copy>`,
  or `git -C` on a real clone. *(`nitpick-time` 0.3.0's plan, 2026-10-08; landed 2026-10-08.)*
- **`check_denominators` on its own measures 34 of 36 denominators**, so its result can be read only inside a full run.
  *(The same plan.)*
- **`git clone --shared` takes the source checkout's current branch.** Clone a design chain with `--branch main`.
  *(`nitpick-time` 0.3.1's plan, 2026-10-08; landed 2026-10-08.)*
- **A mutant anchor cannot hold a regex's `\n`**, which the mutation tool's `swap` reads as a newline. *(The same plan.)*
- **An exclusion pattern with a wildcard must match the whole path**, so a wildcard directory name excludes nothing under it.
  *(`nitpick-regex` cycle 0.1's close plan, 2026-10-08; landed 2026-10-08.)*
- **A blockquote note between a decision's heading and its first line swallows that line** by Markdown's lazy continuation,
  unless a blank line follows the note. *(`nitpick-regex` 0.1.6a, 2026-10-08; landed 2026-10-08.)*
- **`check_refs` reads links inside fences.** *(`nitpick-regex` 0.2.0's plan, 2026-10-08; landed 2026-10-08.)*
- **A scratch clone below the checkout reads two `check_refs` findings that the checkout does not.** *(`nitpick-regex` 0.2.0,
  2026-10-08; landed 2026-10-08.)*
- **GitHub's `ubuntu-24.04` runner restricts unprivileged user namespaces.** A process may create one but holds no
  capability inside it, so a test that mounts in its own namespace fails there. Lift it in a step before the harness, with
  `sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0`, printing the value before (1) and after (0): the runner is
  a fresh VM for one job. *(`nitpick-time` 0.3.2, PD-100, 2026-10-08; landed 2026-10-09.)*
- **The compiler side's per-file site counts are per ROOT, not distinct places.** Its sweep compiles every `.npk` as a root,
  so a site in a shared module counts once per file that reaches it: F45's regex section said 78 files and 400 sites, and the
  tree held 170 distinct places in 39 files (`src/`'s "10 files, 28 sites" was 5 places in 4 files). Both are right; they
  answer different questions, and a re-spelling touches the places. *(`nitpick-regex` 0.2.1a's plan, 2026-10-09; landed
  2026-10-09.)*
- **GitHub Actions reads a workflow as YAML 1.2, where a bare run of digits, one `e` and digits is a NUMBER: quote every hex
  value in a workflow** — a commit, a short commit, a digest. `NITPICK_COMMIT_SHORT: 7e91730` reached `nitpick-time`'s CI as
  `Infinity` (run 38022131137 printed "built from compiler Infinity"). PyYAML 6, which reads YAML 1.1, gives the string
  `'7e91730'`, so a plan that parses its workflow with PyYAML cannot see it; judge a scalar by YAML 1.2's core schema.
  Nothing asserted that row, so that run's verdicts stood; the fix quoted the five hex rows. *(`nitpick-time` 0.3.2a's work,
  `9929d17`, and its verifier, 2026-10-10; landed 2026-10-10.)*
- **A CI job's `timeout-minutes` is a ceiling, not a length: a plan states the measured length.** `nitpick-parse`
  0.0.1's plan told its worker to "allow its sixty minutes" for CI's first run, reading the job's `timeout-minutes: 60`
  (`ci.yml:44`) as a duration. That first run, at `c9baa9e` with no cache, took 4 min 14 s (job 119339969762, 16:22:16Z …
  16:26:30Z), 2 min 24 s of it LLVM 20.1.8's install. A worker told to allow an hour budgets an hour. Quote the last
  measured run's length, and keep the timeout as the bound. *(`nitpick-parse` 0.0.1's step 4 and record, 2026-10-21;
  landed 2026-10-21.)*
- **A pointer check that asks only whether the section exists passes a pointer to the wrong section.** `nitpick-parse`'s
  `pointers.py` confirms that a cited document has a `## <n>.` heading (its line 64), so `CURRENCY.md:17`'s
  "`SCAN_MODEL.md` §3" passed, while the rule it means, C-9, is in §4 (§3 is byte classification). A verified Expect and
  the plan's §1.7 carried the same pointer. A check is only as wide as its mechanism: check that the named rule or term
  is in the section the pointer names, and plant a pointer to a real but wrong section as the control. *(`nitpick-parse`
  0.0.1's step 5, 2026-10-21; landed 2026-10-21.)*
- **In a Claude Code shell, `grep` is a function, and `xargs grep` is another program.** The Bash tool defines `grep` as a
  shell function over an embedded ugrep, while `xargs`, `find -exec` and every script run `/usr/bin/grep` (GNU grep 3.11
  here). Their regex dialects differ. To ugrep, `[A-Za-z_\[\]-]` is one bracket of letters, brackets and a hyphen; to GNU
  grep it is a bracket that ends at the first `]`, followed by a required `-`. So a pattern checked at the prompt can
  match nothing under `xargs`, with no error, and a sweep that hides stderr reports a silent zero. Give every sweep a
  positive control in the same pipeline, such as each file's `mod:` line, or sweep in Python. *(This seat's sweep for
  F56, 2026-10-15: zero matches of every kind, where the Python sweep's control read 359 of 359; landed 2026-10-15.)*
- **`python3 -B` reaches no child process.** A harness that starts its own runner again, as a self-check does, passes `-B`
  itself, or a `python3 -B` run writes bytecode anyway: `nitpick-time`'s run left ten files under `harness/__pycache__/`
  until its self-check started the runner under `-B`, and none after. `nitpick-regex` 0.2.3 met the same. *(`nitpick-time`
  0.3.4's plan and close, `0fec132`, 2026-10-15; landed 2026-10-15.)*
- **"Refused by both" is not "unaffected".** A program that both compilers refuse at an earlier stage never reaches the
  stage a change is in, so a sweep's "0 newly refused" says nothing about it. From landing 113, every `nitpick-regex` file
  importing `src/syntax/parse.npk` was refused by `PARSE-001` at its line 223, a field named with a keyword. That was 76 of
  regex's 188 files, and they sat in "refused by both" through every later checker change, 116's borrow rule among them.
  So read a clean count with the stage each of its programs reached. Where an earlier refusal hides a library, sweep a
  scratch copy with only that refusal's cause fixed. A graph of a library's imports must follow `pub use` as well as
  `use`. *(This seat at F58, 2026-10-15. The first import graph missed `pub use` and read zero, and a direct control
  caught it. Landed 2026-10-15.)*
- **Read an environment variable only by its exact name** — `printenv NAME` or `"${NAME}"` — never by listing the environment
  and filtering it. On 2026-10-16 an `env | grep` printed a session's own messaging token, because its redaction matched
  values, not names. A filter can never be shown complete over a set it has not seen. *(`management_1`'s cross-seat rule,
  2026-10-16; landed 2026-10-16.)*

## 7. Repository conventions

**A repository that holds only documents is still a repository, and a loop
assembled by listing rather than by discovery will miss exactly the one nobody
thinks of as code.** Found 2026-09-06 at the seventh orchestrator's takeover:
the handover sweep that certifies every tree *"clean and level"* before the
writer lock changes hands had enumerated **seven** trees since it was first
written, and there are **eight**. The missing one was `nitpick-apps` itself —
`APPS.md`, `PLAYBOOK.md`, `README.md`, `LICENSE`, no source — already in
orchestrate §2.2's startup *read* set and already covered by `CLAUDE.md`'s *"a
library **or application** repository"*, so it was never excluded by decision.
Four orchestrators inherited the same hand-written list.

**It survived because every neighbouring count was right.** Three sets are in
live use in this ecosystem and each is correct under its own denominator: **six
repositories** (five libraries + `nitpick-posix`) is the *work* set; **seven
trees** is that six plus the workbench; **eight** is that seven plus
`nitpick-apps`. A reader checking any "all six repositories" claim finds it
sound, so nothing signals that the neighbouring seven is short. **This is the
same shape §6 names — a check whose NAME describes the property while its
MECHANISM covers something narrower — and here the mechanism was a list a human
typed once.**

The rule, and it costs one line: **discover the set, never list it, and print
the count beside the verdict.**

```bash
mapfile -t TREES < <(find . ../nitpick-apps -maxdepth 3 -name .git -printf '%h\n' | sort)
echo "sweeping ${#TREES[@]} trees"          # the count IS part of the verdict
for t in "${TREES[@]}"; do
  printf '%-34s dirty=%-3s ahead/behind=%s\n' "$t" \
    "$(git -C "$t" status --porcelain | wc -l)" \
    "$(git -C "$t" rev-list --left-right --count HEAD...@{u} 2>/dev/null | tr '\t' '/')"
done
```

A verdict without its denominator is not a measurement, and *"all N are clean"*
is two claims — that they are clean, and that there are N. **The second one is
the one nobody checks.**

**The same blindness has a second form, and it bit within hours of the rule
above being written.** `git grep -l` **reads the index**, so a sweep run before
`git add` silently skips every file the same commit is *adding*. A token
correction in `nitpick-time` 0.1.0 reported four files fixed; there were five.
**Use `git grep --untracked` whenever the commit adds files** — and note what
actually caught it: the workbench's own new rule to run `check_refs` a **second
time after staging**, which exists because `check_refs` enumerates with
`git ls-files` and has exactly the same blind spot. **One index-blind tool
caught another**, and neither would have caught itself.

**And a count is only as good as the run it came from.** The same subcycle wrote
`BUILD.md`'s parse split as *"64 parse cleanly + 16 refused later"* from a run
where a test was still failing; the committed tree is **66 + 15 + 2**. The
**tagged** number in that same sentence was right and the untagged ones beside
it were wrong. **Pair every count with its run's verdict, not merely with the
command that produced it** — a number taken from an intermediate RED run reads
exactly like one taken from a green one.

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
the exact patch release the pinned compiler names (20.1.8 from `7e91730`, D-349; 20.1.2 before) with the four flag lists **and the `triple` and `datalayout` rows** *(corrected 2026-10-09, E2-4: this said 20.1.2 and named neither row)*, an **empty** `[dependencies]`, and a
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
| `nitpick-posix` (an application, under `nitpick-apps/`) | `PX-` |

`D-nnn` always means the **compiler's** decisions and is never ours to amend.

**`PD-n` is a plan's draft label, not a decision number.** A plan drafts its decisions as `PD-n`, and each becomes its
repository's next decision number when the dispatching seat accepts it. The labels are now allocated ecosystem-wide, in
blocks: each plan takes the next block after the last label used anywhere, the dispatching seat names the block in the
dispatch, and the plan says so in its first commit (the Team brief's §8). Earlier labels were per repository and collide:
`nitpick-time`'s PD-66 and PD-72 are not `nitpick-regex`'s. So cite an old label with its repository, as `nitpick-time`
PD-66, and prefer the decision number it became. *(The ecosystem audit's E3-2, 2026-10-15; landed 2026-10-15.)*

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

**Landed 2026-10-05 from the record (`nitpick-time` 0.2.0's plan, 2026-09-30 23:55):**

- **Read a decision log's highest number by number, not by its last heading.** A log is not always appended in order.
  The read is `grep -o '^### TM-[0-9]*' meta/DECISIONS.md | sort -t- -k2 -n | tail -1`, and a plan names the command, not
  the number it saw.
- **A before/after helper lists `HEAD`'s tree, not the index.** Take its "after" once the change is committed: read before
  that, it compares the old tree with itself.
- **A check that reads a plan's fences also reads its filled `Expect`s.** Confirm it once with them committed, not only
  over the empty plan.
- **Proofread every added patch line.** `=NIL(` passed the compiler, the harness and a masked IR comparison; only reading
  caught it.
- **Run `check_refs` after every prose edit**, and after every commit that touches `BOARD.md` or `RECORD.md`: an absolute
  path and a registry number cited before it existed each slipped in and were caught a commit late. *(`nitpick-regex`
  0.1.3's plan, 2026-10-01, and two seats since; landed 2026-10-05.)*
- **The owner of a constant is the module that holds its one copy.** When an owner map permits its owner a literal, giving
  ownership to a module that only USES the constant permits a second copy. *(`nitpick-time` 0.2.2's plan, 2026-10-01;
  landed 2026-10-05.)*
- **`check_record` reads the committed record**, so run it after the commit: a staged record is a dirty tree to it.
  *(`nitpick-time` 0.2.4's plan, 2026-10-02; landed 2026-10-05.)*
- **Push each commit as it is made.** GitHub's push trigger runs on a push's HEAD commit only, so a commit pushed beneath
  another has no CI run of its own: cycle 0.1's move, `96aac77`, had none. *(`nitpick-time` cycle 0.2's close, 2026-10-02;
  landed 2026-10-05.)*
- **A cached download is held to a pinned sha256 before it is unpacked.** A cache keyed on a version string trusts whatever
  the first fetch got: a replaced or corrupted asset with the same version passes a `--version` check and then stays cached
  for good. So pin the digest in the workflow's `env`, download to a file, run `sha256sum -c` before `tar`, and say in the
  comment what the check guarantees. Measure the digest once from the real asset, with CI's own fetch as the second reading.
  *(Found 2026-10-22 at `nitpick-parse`'s `ci.yml:74`, "an immutable asset", unmeasured; time's and regex's LLVM installs
  had the same `curl | tar`. Each library takes the fix at its adoption of `2e1cb4a`; landed 2026-10-22.)*
- **A dated line says when the tree began to say it, and a measurement's date says when it was taken.** In a plan's
  patches, for every library:
  - a dated note carries the landing run's one date, by placeholder (regex's `@@DATE@@`), and a pin the note names beside
    that date is the pin the landing run builds at;
  - a decision not yet landed opens with that date too, and its drafting and acceptance dates stay in the plan's history.
    What it was decided on, its "measured at the pin X" evidence, stays as written in its body, and a dated note beneath
    it records a later re-measurement;
  - a decision already landed keeps its text and its date, and takes an added dated note;
  - a record of when or where a measurement was made (a `CURRENCY.md` row, a digest's "As of", "measured at compiler X")
    keeps the measurement's own date and pin. The placeholder would claim a measurement the landing run did not take;
  - a clause that states what the plan does must be true when it lands, so it is corrected rather than noted;
  - an `Expect` block is one run's output. A block a run retakes is retaken whole from that run, masked lines included,
    copied and never typed, and a block the run finds SAME throughout is left whole.
  *(The libraries' seat's rulings for `nitpick-parse` of 2026-10-21 and 10-22, and for sockets' and parse's adoptions of
  `2e1cb4a` on 2026-10-23, consolidated after parse's T11v found two of them in conflict; landed 2026-10-23.)*
- **A push's time is the pusher's `date` and its CI run's `createdAt`, never GitHub's events feed.** The feed can omit a
  push, or list it more than an hour late: at 10:27:17 on 2026-10-25 it listed the first and last of `nitpick-parse`
  0.0.1a's five pushes and not the three between. *(`nitpick-parse` 0.0.1a, its steps 2–4 and its work verifier's finding
  2, 2026-10-25; landed 2026-10-25.)*
- **A record that quotes a CI log line masks the runner's path.** `sha256sum -c` prints the asset's path under the runner's
  home directory, and `check_refs`' leak scan flags any home-directory path, the runner's included. *(`nitpick-parse`
  0.0.1a, its step 1, 2026-10-25; landed 2026-10-25.)*
- **A plan's check exits non-zero on everything it reports as wrong.** A check that prints a finding and exits 0 is safe
  only inside a block whose Expect the comparator holds. Run by hand, or by a later pass, it passes. Two of the libraries'
  plan tools did this on 2026-10-25: `nitpick-parse` 0.0.1a's `across.py` exits 0 on an emission diff, and
  `nitpick-sockets` cycle 0.0's `tools/twins.py` exits 0 on a restored stale text, with STALE 8. Each such check carries a
  control that plants the finding and proves the exit, and its README says what each exit means. *(`nitpick-parse` 0.0.1a's
  work verifier, its finding 3, and `nitpick-sockets` cycle 0.0's T7v4, its finding 4, 2026-10-25; landed 2026-10-25.)*

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
- **A deliberate REACH-002 refusal can pass D-237's set rule while testing the wrong
  identity**, because every REACH-002 line carries the same code. So each such
  refusal names every other arm REACH demands, and a check confirms that its single
  REACH-002 line names its subject.
- **Prove a sweep reached every loop:** plant `decreases 0i64 - 1i64` in each swept
  loop and require every one to trap under the tests. `nitpick-regex` caught 11 of
  11 in `src/` that way.
- **A harness's own messages go stale like prose.** `nitpick-regex`'s harness
  printed a pin-specific finding (every `src` file refused by `llc`) as
  present-tense fact on every run for four pins after it stopped being true. A
  message that states a measurement dates it.
- **A test's asserted value and a specification's stated value are two lists nobody diffs.** `nitpick-time`'s probe
  asserted the range's first day as -4 371 587 from its very first cycle, while `CALENDAR.md` and the public
  `NTIME_DAY_MIN` said -4 371 588 — both green for three weeks. **Diff them**, and when a value is wrong, show the test
  red at the old value before moving it.
- **Relations among numbers derived from one wrong number all hold.** Only a recomputation by an INDEPENDENT method
  catches the root — and **a second method that equals the first on part of its domain is one method there** (a
  400-year shift of zero), so force the two to differ across the whole range.
- **A control must be a case the WRONG implementation gets wrong**, not merely one the right implementation gets right:
  `y +% 1i64` as the control for "`+%` is not a division" also passes a checker that misreads `+%`, because `1i64` is a
  valid divisor either way; `y +% m` discriminates.
- **A control must also assert that its substitution matched.** A mutation applied by text substitution that matches
  nothing leaves the original program, which passes — so a no-op control reads as a caught mutant. Count the
  substitutions and fail on zero.
- **A probe that exits while an owning value is still live never reaches its drop**, so a fault AT the drop is
  invisible to it: a scalar-pass probe of O-N20 exited 0 on both legs, while the same pass with the string dropped in a
  callee stopped at 95 at all six kept pins. Put the drop inside the measured path — a function's return — or the probe
  measures nothing.
- **A control's result is its NAMED LINE, not its exit status.** A control that matched nothing was stopped by its
  own assertion, and the check it then pointed at a missing file crashed with exit 1 — which looks exactly like a
  caught corruption (`nitpick-time` 0.1.4's planning).
- **A test of an OWNED answer uses the source again before it reads the answer.** `bytes_take` returned a view of its
  sink typed as an owned `string` from cycle 0.0.4 to 0.1.4b, and its one test read the answer at once, so it
  passed; reusing the sink rewrites the text (13) and growing it frees it (12). O-N25 is the language half.
- **Derive every number an instrument prints from the source before you bound it**, and treat one that disagrees as
  a finding: `NPK_HEAP_STATS` counted 25 allocations where the source makes 26, and the missing one was that
  use-after-free.
- **A sample aligned with a period of the domain aliases with it.** 400 Gregorian years are exactly 20 871 weeks, so
  a weekly sample meets every 400-year leap day or none; a weekly sample passed a leap rule that drops them
  (measured). Sample off the period, or exhaustively.
- **A low address-space cap's control must share the program's runtime.** At `c3bdae2` a Nitpick program that
  allocates nothing takes `HeapOom` below about 10.5 MiB, while `/bin/true` runs from 2.75 MiB — so a `/bin/true`
  control at 8 MiB calls a correct remedy a leak. Control with a floor program built by the same toolchain.
- **A positive test whose expected value equals the vacant value tests nothing.** After one insert `sparse[3]` is 0 —
  which `calloc` also wrote. Choose inputs whose correct answer the untouched state cannot produce, and show a copy of the
  test expecting the vacant value FAILS.
  - **A payload-free enum's vacant value is its FIRST variant (tag 0).** So a read-back field asserted equal to the first
    variant cannot tell the value from vacant storage. `nitpick-time` 0.2.0's unit checked a second `Vec` read only through
    `clock == Monotonic`, and a vacant read passed it, measured. Assert a field whose expected value is not zero, or build
    the value with a later variant. *(2026-10-01 03:13; landed 2026-10-05.)*
- **Read `Result.value` only after testing `is_error`** (`NITPICK-TAINT-001` refuses it otherwise), so a refusal exits
  with the test's own code rather than an anonymous identity arm, and mutation results stay readable.
- **A tool's wrapper can launder a kill into a verdict.** The compiler seat's `clam.py` maps a child's SIGTERM or
  SIGKILL to its own timeout code, so six earlyoom kills sat in its evidence as *"Clam timed out"* until the machine's
  journal was read. Read how any harness maps a signal death before trusting a "timeout" or "failed" row — ours
  included. *(2026-10-16: read earlyoom with `journalctl -u earlyoom --since today`, which works from a sandboxed shell
  and shows its hourly line. `systemctl is-active earlyoom` cannot reach the system bus there ("Failed to connect to
  bus: Operation not permitted", exit 1), so it reads as inactive while earlyoom runs. A worker's did on 2026-10-15,
  and `management_0` confirmed the daemon active from its own shell.)*
- **A sweep for a rule's exposure must cover every place the rule's predicate reads, not the shape its defect was found in.** The O-N22 sweep checked lent bare-`T` PARAMETERS and reported no exposure. DEF-104's gate also reads `T` PLACES read out of a lent or pointed-to container, and an unchanged `nitpick-regex` went RED 78/223 at the pin that carried it. Read the fix's predicate, then sweep for everything it reads.
- **Striking a discharged defect's question does not retire the rule it justified.** `nitpick-regex`'s O-N13 was struck at its fifth triage, and seven live sites — a specification rule, a harness message, `CLAUDE.md` — still gave it as the reason for B-15a's rule 2. When a defect is discharged, sweep for the sites that cite it as a REASON, not only its own entry.
- **One new test file can move a run's total by two**: its suite judges it, and a parse sweep that compiles every `.npk` as a root counts it again — 218 became 220, and *"219"* was written three times before the run said otherwise. Predict a total from the harness's stages, not from the file count.
- **A harness step that copies a tree copies its manifest.** The compiler records source paths relative to the manifest
  root, in diagnostics and the site table alike (D-236), so a copy without its manifest emits different paths depending on
  where it sits, and a reproducibility check reddens on an unchanged tree. Found at `nitpick-regex` 0.1.2 (2026-10-01), the
  cause of §12's old `TMPDIR` bullet. *(Landed 2026-10-05.)*
- **Scratch can run every leg without symlinks.** Copy what a leg needs; a symlink into a library or this workbench is a
  hazard to remove later (a recursive delete follows it), never a necessity. *(`nitpick-time` 0.2.0's plan, 2026-09-30;
  landed 2026-10-05.)*
- **A check placed after an operation that refuses its mutant's effect never fires on that mutant.** Measure which exit each
  mutant reaches, and order the assertions so every line has one. *(`nitpick-time` 0.2.1's plan, 2026-10-01; landed
  2026-10-05.)*
- **An exit no library mutant can reach gets a test-side control**, an edit of the test itself, **or is labelled a guard** —
  never claimed seen red. *(The same plan.)*
- **A mutant that lands outside its case is information**, not noise: it says what else the change reaches. *(`nitpick-regex`
  0.1.3's plan, 2026-10-01; landed 2026-10-05.)*
- **A unit's case numbers stay below its `failsafe`'s exit codes (91 and up)**, so a case's own exit can never be read as a
  trap's. *(The same plan.)*
- **A case guarded by two independent checks cannot be reddened by a single-edit mutant.** When a decision rests on such a
  case, show it red by breaking every guard. *(`nitpick-regex` 0.1.3, 2026-10-01; landed 2026-10-05.)*
- **Take each boundary from both sides.** A sweep of boundary values from one side can be blind to the defect the boundary
  exists for. Every day's first instant is a whole number of days from the epoch, where truncating and flooring agree, so a
  truncating conversion passed all 7 304 484 of them. *(`nitpick-time` 0.2.2's plan, 2026-10-01; landed 2026-10-05.)*
- **A property test built only from values the validating constructors make cannot see an operation that bypasses the
  constructor.** Forge inputs through the opt-out (C-8c's). A `civil_to_utc` that wrote its own `Timestamp` literal passed the
  vectors and both sweep members; only forged inputs caught it. *(The same plan.)*
- **A mutant can be undone by the host language.** Python's `int()` reads `1_000_000` itself, so a mutant that inserts
  underscores changes nothing a Python check sees. Measure that a mutant goes red before claiming it. *(`nitpick-regex`
  0.1.4's plan, 2026-10-01; landed 2026-10-05.)*
- **A value-writing operation that keeps its own range check passes every constructed input.** A literal-writing
  `timestamp_add` passed them all; only a `nanos` forged past two seconds caught it. *(`nitpick-time` 0.2.3's plan;
  landed 2026-10-05.)*
- **A fact program used as a control needs a complete `failsafe`.** A stub stops at `NITPICK-REACH-001` and hides the
  result. *(`nitpick-time` 0.2.4's plan; landed 2026-10-05.)*
- **A check whose exemption is tied to the repository's own tree reports the exempt item over a copy.** Measure a copy
  with the copy's own harness. *(The same plan.)*
- **A check that finds a wide intermediate by its type's name misses a wide literal, and a check that reads spellings
  misses a wide value that nothing spells.**
  - `(3i256 * 5i256) =>! int64` narrows a constant to its low 64 bits in silence and passes, while the compiler refuses a
    narrower operand beside a wide literal (`NITPICK-TYPE-007`). So among spellings, a computation of literals alone was
    the gap. `nitpick-time`'s PD-91, accepted 2026-10-05, closed it at cycle 0.3.0 by reading a literal's width suffix.
  - **But a wide value need not be spelled.** A call's result passes a spelling check, and always has:
    `((raw wide()) * (raw wide())) =>! int64` in an unmarked function compiles, returns 49, and draws no finding. That is
    `nitpick-time`'s O-X11, dormant, for its 0.3.1 planner to decide.
  - A rule that every widening is spelled is not a rule that every wide value is. A sentence saying a gap is closed makes a
    claim about every path a value can take, so search for a counter-example before writing it.
  *(Cycle 0.2's close, 2026-10-02; landed 2026-10-05. Corrected 2026-10-08: until then this bullet called the literal "the
  whole gap", and `nitpick-time` 0.3.0's verifier found the call path.)*
- **An IR reading meant to see what the source does not spell must read `npkc`'s emission before `opt`.** At `5fbaf4a`,
  `npkc` keeps `llvm.smul.with.overflow.i256` both for a call's product and for a literal product, and `opt -O2` folds
  both to constants. *(`nitpick-time` 0.3.0's fix, 2026-10-08.)*
- **"Passes every check" is measured by a full run, never by the checks module alone.** `nitpick-time` 0.3.1's fix asked
  `harness/checks.py` about three plants and wrote "pass every check"; in full runs two were RED by the arm bill, one only in
  some modules: a `list_truncate` of descriptors was RED in `cal` and GREEN in `src/core/bytes.npk`, whose consumers already
  owed its arms. The run's module decides an arm-bill verdict. *(`nitpick-time` 0.3.1's wording fix, 2026-10-08; landed 2026-10-08.)*
- **A red-first prediction must cover the controls too.** *(`nitpick-time` 0.3.0's plan, 2026-10-08; landed 2026-10-08.)*
- **When a check's subject widens, read each of its messages for the old subject's noun**, not only its rule and docstring.
  *(`nitpick-time` 0.3.0, 2026-10-08; landed 2026-10-08.)*
- **A self-check row whose control is a real tree file fails first, and alone, the day that file holds what the row plants**,
  so the right check never names it. *(`nitpick-time` 0.3.1's plan, 2026-10-08; landed 2026-10-08.)*
- **A check that holds declared functions to the emission must say which ones it holds.** `nitpick-time`'s declared-function
  rule reads only the non-generic ones, so in a generic function that nobody instantiates no purity reading sees an async
  call, a drop or a function-typed alias. *(`nitpick-time` 0.3.1's fix, 2026-10-08; landed 2026-10-08.)*
- **An emission that contains the code closes a hole that token lists only narrow.** `nitpick-time`'s PD-99 instantiates every
  generic function of `src/` in one unit, so the emission checks read them all, and a generic with no instance is a finding.
  *(`nitpick-time` 0.3.2's plan, 2026-10-08; landed 2026-10-08.)*
- **A writer that skips a redundant field lets a wrong count pass every round trip.** Hold the redundant fields equal at the
  writer. *(`nitpick-regex` cycle 0.1's close, 2026-10-08; landed 2026-10-08.)*
- **Measure a loop bound at its edge.** *(`nitpick-regex` 0.2.0's plan, 2026-10-08; landed 2026-10-08.)*
- **To check "every case", generate the cases.** `nitpick-time` 0.3.2's first plan said its units saw every case a careless
  implementation gets wrong; a single-site enumeration of the section (293 mutants from fourteen operators) found 25 killable
  mutants they did not see. *(`nitpick-time` 0.3.2's revised plan, 2026-10-08; landed 2026-10-08.)*
- **A unit can make the machine state it needs**: a user and a mount namespace of its own, with an empty `tmpfs` over `/etc`,
  by syscalls in its own text. On GitHub's Ubuntu 24.04 runner that needs a CI step lifting AppArmor's userns restriction.
  *(`nitpick-time` 0.3.2's plan, 2026-10-08; landed 2026-10-08.)*
- **A test's own `alarm` turns a hang into a verdict.** A FIFO at `/etc/timezone` under the unit's `alarm(5)` ends a mutant
  that drops `O_NONBLOCK` by `SIGALRM`, where it would have stalled the run. *(`nitpick-time` 0.3.2's revised plan,
  2026-10-08; landed 2026-10-08.)*
- **`execve` yourself to build an environment the harness cannot.** A unit that re-executes itself with environments it lays
  out reaches cases that the harness's own mechanisms do not. *(The same plan.)*
- **A program run once against the runtime's allocator guard states a RATE, not a verdict.** The guard words are
  `secret ^ guardaddr ^ K_GUARD`, the secret from `getrandom(2)` at the first allocation, so a write of a fixed byte changes
  nothing whenever the guard's byte already holds it: one run in 256, by design (measured: 9 of 842 unseen; 800 of 800 caught
  when the write puts the guard's own byte plus one). Write a byte known to differ from the guard's, or quote the line as a
  rate. *(`nitpick-time` 0.3.2's worker, 2026-10-08; its mutant 295.5, caught by the guard alone on 398 of 400 legs, is the
  same rate; landed 2026-10-09.)*
- **A self-check that builds scratch trees carries its own toolchain rows, and a re-pin moves them too.** `nitpick-regex`'s
  `harness/selfcheck.py` writes each case tree's manifest with its own `llvm`, `triple` and `datalayout`: with only the tree's
  `llvm` row moved to 20.1.8, 21 of its 31 live cases went NOT red, each inner run refused at the toolchain check.
  `nitpick-time`'s self-check reads its rows from the tree's manifest, the better shape. *(`nitpick-regex` 0.2.1a's plan,
  2026-10-09; landed 2026-10-09.)*
- **A verifier rehearsing out of the checkout rebuilds the checkout's position.** A plan whose `env.sh` finds its inputs by
  the checkout's place (the workbench above it, the compiler beside that) runs in a stand-in workbench under `$TMPDIR` only
  when the stand-in holds every path the tools read: both pins, the private LLVM, the board's documents, a `--shared
  --no-checkout` clone of the compiler, and `.internal/toolchain/950bb1d`, which `rx120.sh`'s control reads. Find the set by
  reading the tools, not from a brief. *(`s1-nregex-0.2.1a-verify`, 2026-10-09; landed 2026-10-09.)*
- **A runner's marker set is read from what the compiler's reader tests, never from the shape of its strings.** A grep
  of `npkg/expect.npk` for quoted `name:` strings found eleven of its twelve markers and missed `expect-no-parse-error`,
  which has no colon, and `nitpick-parse`'s `harness/expect.py` then neither judged nor refused it: a file carrying it
  would read as prose, its expectation unchecked. List each `text_starts_with(body, …)` the reader runs, and have the
  runner judge or refuse every one by name. *(`nitpick-parse` 0.0.2, its step 1, 2026-10-28; landed 2026-10-28.)*

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
`decreases` `unbounded` `sealed` `hidden` — **new at the 1.5 re-pin: refused as
local names at `c3bdae2`** (`NITPICK-PARSE-002` at the declaration)

**`cfg` is reserved too, and `ppid` is not.** At `5fbaf4a`, `uid`, `gid`, `pid`, `tid`, `fd`, `thread`, `cfg` and `arena` are
each `NITPICK-PARSE-002` as a local's name, while `ppid` compiles beside them. *(`nitpick-time` 0.3.2's plan, measured
and verified, 2026-10-08; landed 2026-10-08.)*

**A FILE'S BASENAME CANNOT BE A KEYWORD EITHER** *(added 2026-09-26, the ecosystem
audit's EC7)*: a module declares `mod:<basename>;`, so `error.npk` and `raw.npk`
are refused — `NITPICK-RESOLVE-012` at 1:1 at `c970483`, **`NITPICK-PARSE-001` at the name (1:5) at `5fbaf4a`** *(re-measured 2026-10-02, `nitpick-regex` cycle 0.1's audit, S3: "expected a name: a keyword cannot be declared as a function, type or module name")* — measured: `nitpick-regex`'s planned
`error.npk` became `pattern_error.npk`, and `nitpick-sockets` plans a `raw.npk`.
Check a planned module's name against the compiler's keyword list before it
enters a plan. **Check a planned type's name against the prelude's as well:** `Reader` is a prelude trait at
`5fbaf4a`. *(`nitpick-regex` cycle 0.1's close, 2026-10-08; landed 2026-10-08.)*
**`stack`** — a MemoryQualifier beside `wild`, `wildx` and `defer`
(`../nitpick/meta/specs/LEXICAL_REFERENCE.md:52`), confirmed against that file
rather than reported.

**`stack` is the one that costs an hour, because it does not fail where you
wrote it.** It is the natural name for an explicit-stack parser's local. At
`nitpick-regex` 0.0.0's pin, using it produced `PARSE-002` at the declaration
followed by "this `{` is never closed" pointing at `main`'s closing brace — so
it read as a brace imbalance dozens of lines away, and it was bisected as one.
`nitpick-regex` 0.0.0 lost about an hour to exactly that. *(Re-measured
2026-10-21 at `c9baa9e` by `nitpick-parse` 0.0.1's step 6, in six scratch
programs: a local named `stack`, a `Vec<Frame>` in a helper, in `main` or
before a braced loop, or an `int64`, is `NITPICK-PARSE-002`, "expected an
expression", at the declaration, and each later line naming it is refused
again, `PARSE-002` and `PARSE-001`. In the loop's shape the errors run on to
the function's closing `};` and into the next function. A parameter named
`stack` is `NITPICK-PARSE-001`, "`stack` is a keyword and cannot name a
binding, a parameter, a field or a variant". None of the six prints "this `{`
is never closed", which the compiler issues only when the file ends inside a
block (`src/frontend/parse_stmt.npk:467–473` at `c9baa9e`, by that step's
reading), and the control, the same local named `frames`, parses and resolves.
Landing 136 (DEF-259) makes a local `T:keyword` `PARSE-001` at the name, so
the account moves again at the re-pin past 136.)* *(Re-measured 2026-10-23 at
`2e1cb4a`, which carries 136, in `nitpick-parse` 0.0.2's plan §1.16 by its
adoption (T12, on the Team seat; 35 of 35 blocks the same from a fresh clone,
its verifier running at this writing): a local named `stack` is
`NITPICK-PARSE-001` at its name and is refused again at each later use, a
parameter so named is `NITPICK-PARSE-001` once, and no brace error follows. At
this pin it fails where you wrote it.)* So if parse errors cascade
from one declaration through the lines after it, or claim an unclosed brace
when the braces are balanced, check whether a local or a parameter is named
after a qualifier before you touch anything else. **And a plan that writes a
playbook account as measured re-measures it at its own pin:** this one reached
`nitpick-parse`'s `CLAUDE.md` and `BUILD.md` as fact, at a later pin than the
one it was measured at. *(`nitpick-parse` 0.0.1's step 6, 2026-10-21; landed 2026-10-21.)*

Three shapes that surprise a C or Rust habit: adjacent string literals do not
concatenate; `discard(x);` takes parentheses and `defer { … }` takes no
trailing semicolon; declarations end `};` and control-flow blocks do not. And a
file's `mod:` name must equal its basename, or the loader reports
`NITPICK-RESOLVE-005` at line 1 and says nothing about the name. At `c3bdae2` it is D-248's `NITPICK-RESOLVE-012`, which does name it.

---

## 11. Prior art

`../ARCHIVE/` holds the prototype-era implementations. They are a **behavioural
oracle** — what the domain needed, what the edge cases were, which tests
existed — and their **dependency choices are not precedent**: most of them
reach C through an FFI that no longer exists, and several carry defects
recorded in the compiler's own audits. Read them for the domain; write the
design fresh.

**Landed 2026-10-05 (`nitpick-regex` 0.1.3's plan, 2026-10-01):** **a rule borrowed from another tool is that tool's only
once its source is read**, not its documentation's summary; and **a specification rule that says engines differ owes the
comparison**, measured, engine by engine.

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
- **Every fenced command has been run, verbatim.** Rehearsing a plan by extracting
  its code blocks and running them in a fresh clone found five defects in
  `nitpick-regex`'s 0.0.4b and 0.0.4c before any worker saw them: an unexported
  variable, two wrong greps, a restore check that could never pass, and a wrong
  control. A plan whose commands were never run is a draft.
- **A list built for one question is re-derived, not reused, for the next.**
  `nitpick-time` carried five rows *"built on the move-out primitive"* into a
  different question and read them for three cycles as *"owe an element drop"*;
  measured, `vec_pop` owes none (two million push/pop cycles at 120 B peak, against
  `vec_clear`'s 48 MB).
- **A count written before the step that adds files counts the old tree.** *"Exactly nine roots, and nowhere else"* was
  contradicted by the same plan's later probes — a tenth root. Date every such count to the step it is true at. (The
  compiler seat's *"your six … and nowhere else"* for DEF-96 was off by one the same day: the canary.)
- **A count of pins taken from the workbench's toolchain directories is not one repository's count of pins** — `3d15ac9`
  is kept here and was never `nitpick-time`'s.
- **Rehearse a plan in its real position, or record which legs ran.** A dry run in a relocated copy SKIPS any leg that
  finds a tool by a checkout-relative path (`nitpick-regex`'s floor leg reaches `../.internal/toolchain/950bb1d`), and a
  skipped leg reads exactly like a held one.

---

**A DEFECT'S EXTENT IS A SEPARATE MEASUREMENT FROM ITS EXISTENCE, AND ONLY THE
FIRST IS USUALLY TAKEN.** Found the hard way at `nitpick-time` 0.0.4, where the
orchestrator raised a compiler defect upstream as blocking **one** API row and
it blocked **five**. Reproducing a defect answers *does this happen*. It does
not answer *what else is built on the thing that broke*, and the second
question needs its own controls — here, four owning shapes against four scalar
controls from the same source, which showed the primitive was
`move(v.items[i])` in a generic function at an owning `T` and that **a loop is
a different caller, not a different primitive.**

**Understating an extent is the dangerous direction, and it fails silently.**
*"One row"* was precisely the reading that would have justified shipping a
generic `vec_clear<T>` that **does not drop its elements** — which passes an
`exit 0` leak gate, because D-151 counts `wild` blocks and cannot see a managed
body. An extent short by four rows would have been **discharged by a green
suite**. Overstating an extent costs a wasted message; understating one ships a
silent bug with a passing test beside it.

**The cost of correcting it was one message, and the fix's shape did not move.**
That is the general case: extent corrections are cheap upstream and expensive
downstream, so **measure the extent before raising, and if you did not, correct
it the moment you know.**

---

**A WORKER MUST NOT ASSIGN ITS OWN OPEN-QUESTION ID — IT SHOULD CITE THE NEW
QUESTION BY PATH AND LET THE ORCHESTRATOR NUMBER IT.** `O-N` is the workbench
registry's namespace and `O-X` a library's, and a worker cannot see what the
registry has issued. At 0.0.4 a worker filed a genuine compiler defect as
`O-N12`, which was already `nitpick-regex`'s settled `>>>` question, and
undoing it took **ten edits in ten files** — the cheapest error available to
make and among the more expensive to undo.

**It is also the error the registry's own opening paragraph warns about**, which
is the third time this ecosystem has recorded a number taken from memory rather
than from the file that issues them. **So the rule is mechanical rather than
attentional: a worker writes the reproduction directory's PATH, and the
orchestrator assigns the id when it registers the question.** The successor
worker at 0.0.4 did exactly this for a second defect it found and left it
deliberately unnumbered, which cost nothing and is the shape to copy.

---

**A LOW `ulimit -v` MEASURES THE LOADER, NOT THE PROGRAM — SO EVERY
ADDRESS-SPACE BOUND NEEDS A `/bin/true` CONTROL AT THE SAME CAP.** An
acceptance item here asserted that the non-leaking half of a pair "finishes
clean in under 768 KiB of address space". It does not, and neither does
anything else: `/bin/true` and the probe **flip at the same cap**, between
2688 and 2816 KiB, because at that size it is the dynamic loader that fails
rather than the program's own allocation.

**A bound that a trivial program also fails is not a statement about your
program.** The corrected gate is **one shared 64 MiB cap with opposite
outcomes** — `HeapOom` exit 92 for the leaking half, exit 0 for the correct one
— plus the peak-RSS pair as the quantitative half. **Any repository quoting an
address-space bound owes the same control**, and the number in this one was
inherited across three subcycles before anyone ran `/bin/true` beside it.

---

**AN EXEMPTION LIST'S BOTH-DIRECTIONS DIFF CHECKS THAT THE FILE STILL EXISTS,
NOT THAT ITS REASON STILL HOLDS — AND THAT IS THE FOURTH INSTANCE OF THIS
SECTION'S SHAPE FOUND INSIDE A MECHANISM WRITTEN TO PREVENT IT.** A file
exempted from a check carries a reason: *this cannot be spelled because the
compiler refuses it*. The diff that keeps such a list honest asks **is every
named file present, and is every present file named** — which is a question
about **membership** while the thing that decays is the **reason**.

**Measured at `nitpick-time` 0.0.5.** Two entries exempted for O-N17 said *in
their own text* that they would "fail the both-directions diff" on the day the
defect landed. **It landed. Both files went from stopping at `llc` to running
clean. The suite stayed GREEN at 40 units with both stale entries in place.**
The prediction was written down, was correct about the world, and the mechanism
it named could not see it come true.

**The remedy is cheap and it is the general one: an exemption records the
VERDICT it was written against** — `npkc` / `llc` / `ld` / `run:<code>` /
`none` — **and the harness re-derives that verdict every run.** Membership is
then still checked, and the reason is checked too. **Any list of "known
failures", "expected refusals" or "temporarily skipped" in this ecosystem owes
the same treatment**, because every one of them is a claim about the world that
was true on the day it was written.

---

**AN EMITTED `.ll`'s BYTE COUNT IS PATH-DEPENDENT; THE OBJECT'S IS NOT. QUOTE
THE OBJECT.** The same source compiled from two directories whose names differ
by **one character** produced `.ll` files **14 bytes apart** — one byte per
`npk.site.paths` entry — while the `.o` and the linked binary were
**byte-identical**. So an IR byte-count is partly a measurement of where you
built, and two sessions comparing IR sizes across different trees are comparing
their directory names as well as their compilers.

**This already cost a small false explanation here:** the canary's one-byte
difference against the compiler session's predicted value was written up as
*"two different source files"* — plausible, and a guess presented as a cause.
The real mechanism is this one. **Where a size must be compared across trees,
compare the OBJECT; where IR is the only thing available, compare the FUNCTION
COUNT**, which is what actually held exactly across the re-pin.

---

**`#size_of` DERIVED FROM FIELD WIDTHS WAS WRONG TWICE IN ONE TABLE OF AN
ALREADY-REVIEWED DOCUMENT, AND CARRIED 37% OF A DECISION'S HEADLINE NUMBER.**
`ZoneTransition` was recorded as 12 bytes and is 16; `ZoneEntry` as 16 and is
28. Both were arrived at by adding up field widths, which ignores alignment and
padding, and both survived review because the arithmetic looks right. The
playbook already said never to derive `#size_of`; this is what it costs when
someone does — **a size estimate low by more than a third, underneath a
decision every specification in the repository rests on.**

**Make the probe's EXIT CODE be `#size_of`**, so the number cannot be
transcribed wrongly: a program that exits with the width it measures is a
measurement no one can round.

---

**WHEN TWO CAREFUL PARTIES DISAGREE ON A COUNT, THE FIRST QUESTION IS WHAT SET
EACH ONE MEASURED — NOT WHO MISCOUNTED.** Three times in one day here, two
numbers conflicted and **both were right**:

| the dispute | resolution |
|---|---|
| `56` vs `57` internal defines | 57 is `^define internal`; the 56 was never re-derived, and the other numbers in its own sentence proved it |
| allowlist `112` / `57` / `113` / `106` | 112 = the object's 111 globals + `main`; 57 = the `.ll`'s `define internal` functions; 106 = the object's non-global symbols. **Three artefacts, three true counts** |
| `447` vs `454` zone files | 447 = TZif files by magic bytes; 454 = every regular file, the difference being seven metadata files |

**In all three the answer was a denominator nobody had stated**, and in none was
anybody careless. So the diagnostic move is not *recount* — it is **ask what
was counted**, and expect the sets to differ by something nameable.

**The corollary for reports: name the SET, not just the number.** *"447
non-symlink TZif files"* survives contact with a verifier; *"447 files"* does
not. The worker whose count was challenged had written the qualifier and was
vindicated by it.

---

**A VERIFIER'S `FAIL` IS EVIDENCE, NOT A VERDICT — ADJUDICATE IT BEFORE
RE-DISPATCHING ANYBODY.** §7 says a FAIL means re-dispatch with the finding in
`NOTES:`, and that is right when the finding is about the work. **It is not
always about the work.** At `nitpick-time` 0.0.5 the verifier returned FAIL on a
count, and the fault was **the dispatch's**: the orchestrator had supplied a
literal command (`find … -type f | wc -l`) that **could not produce the number it
was asserting**, because the claim was about TZif files and the command counted
every file. Re-dispatching the worker to "fix" a correct number would have been
the wrong response, and an obedient one.

**This is the fix for one failure mode producing another.** Supplying literal
commands was introduced precisely because a verifier had substituted reading for
running on checks needing setup. It worked — and it **moved the error out of the
verifier's reasoning and into the dispatcher's command.** That is not an
argument against supplying them. It is the reason the orchestrator runs the
decisive measurement itself before accepting either party's number: **the
adjudication cost one command and settled it beyond both.**

---

**THE MANDATED GATE ORDER MEANS A NEW FILE IS NOT EXAMINED BY THE GATE THAT
PRECEDES ITS OWN COMMIT.** `check_refs` enumerates with `git ls-files`, which
reads the **index**. The workbench's rule is *run it BEFORE `git add`* — which
exists for a good reason (an unstaged deletion is a finding rather than a
crash). But the two together mean a **newly created** file is not in the index
when its own gate runs, so **the gate reports clean over a denominator that
excludes the very file being added.**

**Measured 2026-09-06, on this workbench, in the act of filing an audit.** The
gate before the commit printed `nitpick-libs clean (34 files)`; the audit file
was committed; the next run printed `1 finding(s) (35 files)` — an absolute
path in the newly tracked file. **The check was right both times.** Its
denominator moved by one, and the one was the file at issue.

**This is the denominator lesson arriving in the workflow rather than in a
tool**, and it is invisible precisely because the gate is green: *"swept and
found nothing"* and *"swept everything except the thing you are adding"* print
identically. **The tell is the file count** — which `check_refs` now prints on
every line, so it is visible to anyone who reads it.

**The rule: when a commit ADDS a file, gate it twice** — once before `git add`
for the deletion case the order was written for, and once **after staging**, so
the new file is in the index the check reads. Or stage first and rely on
`tracked-file-missing` to report the deletion case, which the check has done
since `7da5c2d`. **A gate whose denominator omits the change being gated is not
gating that change.**

---

**ELEVEN WAYS A REHEARSED PLAN'S TEXT GOES STALE OR MISCOUNTS — FROM ONE DAY'S SUBCYCLES (`nitpick-time` 0.1.3 TO 0.1.4b,
`nitpick-regex` 0.0.4d; 2026-09-25/26), EACH FOUND AFTER REHEARSAL, SEVERAL AFTER THREE.**

- **A tag-writing script must be idempotent.** A re-run wrote six tags twice, 47 where 41 belong; each script now
  skips an edit already applied, and says so.
- **An untagged number beside a tag goes stale unseen** — a library question's *"25"* beside a tag saying 26, a CI header's *"86
  units"* — because the checker reads the tag and nothing reads the prose (§6's *"a checked tag guards only itself"*).
- **For each thing a commit moves or resizes, sweep for statements of its old place and its old size.** Three
  rehearsals swept four phrasings for stale claims and missed the two classes the plan's own changes made false:
  comments naming a moved function's old holder, and prose stating an enum's variant count (*"an eleventh variant"*). **A second instance, `nitpick-time` 0.1.4c: sweep a resized set's old count in WORDS as well as digits** — seven digit patterns passed a docstring saying *"six subdirectories … six places"*, true two resizes earlier; a sweep over statements of the set's membership found it.
- **A hunk written while a question was open goes stale when the author answers before execution.** The dispatch names
  every answered question, and the worker reads each against every hunk that mentions it — 0.1.3's Q-6 note still read
  *"it stays the author's"* after the author had answered.
- **Appending a row to a table whose note generalises over its rows falsifies the note on arrival** (*"every defect in
  it has since been fixed"*, above a new open defect). A hunk that adds a row owes a reading of the table's notes.
- **A sweep's recorded counts must come from the command the record prints.** Two of 0.1.3b's sweep sets had excluded
  a file the printed command does not; only re-running the printed commands on the committed tree found it.
- **An idempotent edit script whose edits APPEND does not stop when the tree disagrees — it RE-APPLIES.** Its old text
  survives inside its new, so a guard that skips "already applied" edits sees the old text and applies again:
  `nitpick-regex`'s `d4d_docs.py`, run over a tree where one of its lines had been amended by hand, exited 0 and appended
  a second decision block. **When a dispatch amends scripted text, amend the script before it runs — never the written
  file after.** **And build the check order into the script's skeleton: an appending edit's guard looks for the NEW text first,** because the new text contains the old — `nitpick-regex`'s cycle-0.0 close re-applied three edits on its second run minutes after its author read this item, and only its own summary (*"3 file(s) written"* on a run that should write none) gave it away.
- **A rehearsal that restores its tree cannot count the plan file in its predicted `git status` tally**, yet the worker
  always edits the plan in the same commit (its title, its record). Predict *"N plus the plan file"*, or every worker's
  tally is one short.
- **A rehearsal that stubs a file or skips the hand edits cannot predict a sweep that reads them** (0.1.4's stale-claim
  searches printed 6, 6, 4, 3, 17 against the rehearsal's 5, 6, 4, 1, 15). Predict *"the rehearsal's tree plus the
  hand-edited files"*, or rehearse the hand edits.
- **A statement that generalises over a list's members can live far from the list** — adding a member to
  `EXPECT_EXEMPT` falsified a comment in another function. A hunk that adds a member owes a grep for every statement
  of the bucket's membership, not only the notes beside the table.
- **The durable form of "quote a command's whole output" is a COMPARATOR**, a script extracted from the plan that
  diffs each step's output against its block — 0.1.4b's seven blocks came back 0 differences that way, CI's log
  included. Care drops lines; a comparator does not.

**AND TWO FROM A BLOCKING AUDIT FINDING, `nitpick-regex`'s BL-9 (2026-09-25):** **a second defence that reads through the
first defence's reader is not a second defence** — "never skip a file that declares `main`" asked the same reader as
the import it guarded, so one reader defect defeated both; take the second answer from another mechanism (here the
compiler's own IR) and test it alone with the first stubbed out. **And mutation-testing two defences with ONE reader
defect measures their independence against that defect only** — a reader that reads too many imports left each
holding, one that blanks too much failed both: mutate the shared dependency, not each defence's own code.

**AND NINE FROM THREE SUBCYCLES OF 2026-09-27 — `nitpick-regex` 0.1.0b and 0.1.1, `nitpick-time` 0.2.0a — landed by the
orchestrator (W-16); a tenth was already covered above.**
- **A plan that supersedes a decision in part sweeps every decision that states the old behaviour**, not only the one
  an audit named. Regex's 0.1.0b marked RX-141 and left RX-133 and two statements in `BUILD.md` saying the opposite.
- **A comparator proves the run equals the rehearsal, so it cannot see a hunk the rehearsal never wrote.** An omission
  is invisible to SAME; the only check for one is the executing worker's own sweep for statements of what each step
  moved. Regex's 0.1.0b worker made sixteen amendments in ten files that way, and time's 0.2.0a plan built the sweep in
  as block 7b, which caught eleven more during rehearsal.
- **A patch that writes a rule and the code it governs can disagree with itself, and SAME cannot see that either.**
  Read each new rule's stated values against the code and the test that pins them: regex's Y-30 said a group head's
  detail is its last byte, and the code gave the `-` of `(?-1`.
- **A sentence about what the tests do is a claim over the test set.** Grep the tests when the sentence is written.
- **A field that carries a value domain and a sentinel needs the sentinel outside the domain.** Regex's `BadGroupName`
  detail 0 means both "the pattern ended inside the name" and "a NUL in the name"; its worker recommends 0x110000,
  which no codepoint takes, to be decided with 0.1.4's escape details.
  *(Decided 2026-10-01 by RX-203: `NOT_A_CODEPOINT`, U+110000. Landed 2026-10-05.)*
- **Do not name a future decision number in prose.** `check_refs` reads it as an undefined reference, and a
  repository's own checks may read fenced blocks too (`nitpick-time`'s `check_specs_current` does). Write "the next
  decision", and let the step that declares it give the number.
- **Cite another repository's rule by repository and name, not by a bare id.** A bare id reads as this repository's,
  to a reader and to its checks: `nitpick-time`'s `check_specs_current` took regex's B-4e and the compiler's S-42 as
  its own.
- **A multi-commit plan rehearses `check_refs` at every commit, not only the last, and cites a decision in markdown in
  the step that declares it.** `check_refs` reads markdown only, so time's TM-212, which amends the CI workflow alone
  at step 6, was declared and uncited until step 7's `CLAUDE.md` cited it.
- **CI asserts the emission and prints the binaries.** D-265, measured on a second runner: at `5fbaf4a`, time's CI
  printed an `npkc` digest different from the workbench's (`f2ded3ec…` against `c8400793…`) while its `npkc.ll` matched
  the pin's row byte for byte. The emission is what a pin promises; a binary's bytes can differ by machine.

*Declined as already covered:* "paste a sweep's output, not a summary" (regex's 0.1.1) — the comparator item above,
and *"a sweep's recorded counts must come from the command the record prints."*

**AND FOUR MORE FROM `nitpick-regex` 0.1.1b (2026-09-28), the same family:**
- **A restatement of a decision outside `DECISIONS.md` goes stale with the code, just as the decision does.** A
  plan that leaves a decision "of its day" owes the same reading to each copy of it elsewhere: 0.1.1b's §7 left
  RX-167 so, and struck O-N22's copy of its list still named `drop_element` after RX-189 removed it. The worker's
  line-by-line reading of the sweep found it; the SAME count could not have.
- **A question's list of consequences is a hypothesis: measure each one before planning it.** Regex's R3 counted
  seven refused units where there were twelve files, and foresaw a check retiring into a belt where half of it is a
  rule that `Copy` does not cover.
- **An IR comparison offered as evidence of "no code change" names its masks.** This compiler's IR carries a
  site-line table that a comment line moves, and a generated drop numbering that a removed declaration moves; the
  pure bound was byte-identical, the steps that added comments were not.
- **Leave `TMPDIR` at its default when running regex's harness.** Set inside the repository, it reddens the harness's
  reproducibility check on an unchanged tree. The cause is not established; a session that keeps its scratch inside
  its write boundary will meet it, and regex's next planner owes the investigation.
  *(Retired 2026-10-05: the cause was found at `nitpick-regex` 0.1.2, 2026-10-01. The compiler records source paths relative to
  the manifest root (D-236), and the harness copied a tree without its manifest. The rule is §9's "a harness step that copies a
  tree copies its manifest"; regex's harness was fixed at 0.1.2, and `TMPDIR` may be set.)*

**Landed 2026-10-05 from the record (`nitpick-time` 0.2.0 and 0.2.0b, `nitpick-regex` 0.1.2; 2026-09-30 → 2026-10-01):**

- **Rehearse a later plan over a simulated record commit of the subcycle before it.** A plan cut while its predecessor is
  unfinished assumes that predecessor's record. Rehearsing it over a simulated record commit is what proves its patches
  apply to the tree they will meet.
- **A rehearsal proves the commands, not the prose.** Read each decision's text against the measurements it cites; a block
  can pass while the sentence beside it states something it never measured.
- **A stale-claim sweep's patterns get a positive control: the step's own hunks.** Run the patterns over the PARENT side of
  each patch, and require every hunk's old text to match, or name the kind of sentence the sweep cannot see. At
  `nitpick-time` 0.2.0b the rehearsed block (six case-sensitive patterns) found the old text of 19 of the patches' 45 hunks.
  Eleven sentences the decision had made stale were found only by the planner's reading, and a twelfth only by the worker's
  case-insensitive second sweep (22 phrasings, 390 lines).
- **Sweep a set's statements over joined text.** A line-based omission sweep cannot see a count whose words a line break
  splits or another word separates. `nitpick-time` 0.2.0's rehearsed block passed eight such stale statements, and
  `nitpick-regex` 0.1.2's block, over joined text, found five matches that `git grep` did not. Join the text, strip the
  comment markers, and match case-insensitively.
- **A gate written as a depth is a statement about one machine's stack and one optimiser's frame.** Measure where a recursion
  of the real shape traps before choosing the depth, and state the measurement beside the gate.
- **Keep decision numbers out of quoted code, too.** A code comment that a plan quotes in a fence carries its future decision
  number into the plan's markdown, where `check_refs` reads it as cited and undefined. *(`nitpick-time` 0.2.1's plan,
  2026-10-01; landed 2026-10-05.)*
- **Read a plan's new text against the glossary's "not used" table before applying it.** An omission sweep reads for stale
  FACTS and cannot see a WORD that a repository's glossary excludes: 0.2.1's plan, rehearsed three times, called a
  `Timestamp` "a wall-clock reading" in two probe headers and a decision, words `GLOSSARY.md` lists as deliberately not used.
  *(2026-10-01 08:38; landed 2026-10-05.)*
- **A recommendation's stated reason is a premise to measure**, like any other. *(`nitpick-regex` 0.1.3's plan, 2026-10-01;
  landed 2026-10-05.)*
- **A plan's claim that it strikes a step is checked against the patches**, which are what the worker applies. *(The same
  plan.)*
- **An amendment to a rehearsed text moves the instruments that count it.** Predict a comparator's DIFF lines from the
  amendment before its block runs. *(`nitpick-regex` 0.1.3, 2026-10-01; landed 2026-10-05.)*
- **Run the omission sweep at design time too**, not only once the patches exist, and **run `check_refs` at the plan commit**,
  which catches a future decision number written last. *(`nitpick-time` 0.2.2's plan, 2026-10-01; landed 2026-10-05.)*
- **Grep each REMOVED line's old phrase across the tree.** A phrase a plan rewrites in one file can live in a second. 0.2.2's
  plan, rehearsed three times, left "the exhaustive calendar and zone sweeps" in `BUILD.md` §3, and its executing worker found
  it. *(2026-10-01; landed 2026-10-05.)*
- **A resized set is also stated relative to one member** ("the same helper as the other five members'"), so sweep for the
  set's subject, not only its counts. *(The same subcycle.)*
- **A rule restated in passing elsewhere is found only by the sweep** (Y-28 restating Y-2). *(`nitpick-regex` 0.1.4's plan,
  2026-10-01; landed 2026-10-05.)*
- **A reading settled early is re-measured against its closest neighbour** when the subcycle that owns the construct arrives.
  *(The same plan.)*

**Landed 2026-10-05 (`nitpick-time` 0.2.3 → 0.2.4b, `nitpick-regex` 0.1.5's plan; 2026-10-01 → 2026-10-02):**

- **A model document's list is a premise, not a fact.** `SPAN_MODEL.md` §5 lacked `bytes_put_int`'s `int128` loop measure,
  in the tree since 0.1.0b, so a check written to its count would have been red on its first run; and it named
  `timestamp_to_civil`, which does not exist. Measure the tree before a check is written to a document's count.
- **A count written as a word beside its own enumeration is arithmetic nobody ran.** `ROADMAP.md`'s "Eleven questions are
  open" had been stale since 0.2.0a. Derive a set's size from the set, or state the members and no number.
- **Decision numbers trip `check_refs` in more shapes than prose.** "TM-n … superseded" within 60 characters is read as a
  citation, and so is `TM-2[0-9]+` inside a code block (as "TM-2", by `check_specs_current`). Name decisions by PD label,
  and write the pattern `TM-[0-9]+`.
- **An Expect that prints `check_specs_current`'s citation count depends on the plan's own text and on earlier records.**
  Mask the count.
- **A dry run of patches that follow `archive.py move` must stage the move first**, or `git apply --index` refuses.
- **A correction made by annotating a claim leaves its twins invisible to a search for removed lines.** Sweep the corrected
  file's siblings for the same claim in other words: the plan's sweep, reading "the three … sites", passed `probe02c`'s
  "§5's three `int128` sites", and the worker's second sweep found it.
  *Second instance (`nitpick-regex` 0.2.2, verified 2026-10-12):* RA-2's and RA-3's corrected claims had twins in
  `harness/stages.py`, `SAFETY.md` §7 and `nitpick.toml`. Block 5's patterns, built from what steps 1–4 changed, could not
  see them; the worker's second sweep, by the claims' own words, found them, and they were filed as three dated notes.
  The positive control (every hunk's old text matched by some pattern), applied to step 3's audit hunks, would have
  flagged them at planning.
- **When a check widens, sweep for the sentences that say what it could NOT see**, not only for its rule.
- **Emphasis splits a phrase in joined text.** A sweep's joined reading strips a line's leading comment marker and nothing
  else, so `CLAUDE.md`'s "checked **before** the trap" passed a pattern for "checked before the trap". Strip emphasis before
  matching, or allow it between words.
- **A plan patch's index hashes for a file with `@@DATE@@` are of the placeholder text.** Re-derive an amended patch's index
  lines by applying it raw; only context can tell whether a later subcycle's patch applies.
- **Re-cut only the amended section of a plan patch, and splice it in**, keeping the original's preimage hash. Re-cutting the
  patch whole over the real tree rewrites sections the amendment never touched.
- **A patch dated by the day it applies breaks a run that crosses midnight.** Date a run once.
- **A later step that takes a file whole undoes an earlier step's script edit to it.**
- **A claim inside an error sentence is a claim about the world, and needs research.** Holding a sentence "to the letter"
  holds its claims too.
- **A finding keyed by a value must name every bound with that value** (`NTIME_YEAR_MIN` and `NTIME_YEAR_MAX` share 9999).
- **Carry a deferral by a dated pointer at each sentence that over-claims until its fix lands**, not only by naming those
  sentences in the next plan: named only there, they stay live where a reader meets them. *(`nitpick-time` cycle 0.2's close
  and its verification, 2026-10-02; landed 2026-10-05.)*
- **A sweep measured in a clone before the commit is a measurement of that tree**, not of the one the commit makes. *(The same
  close.)*
- **An amendment to a rehearsed patch chain is mechanical and checkable.** Replay it raw; re-cut, requiring byte-identity;
  amend one step; and cherry-pick the later ones, so that a conflict marks exactly the hunk to re-cut. *(`nitpick-regex`
  0.1.5, 2026-10-02; landed 2026-10-05.)*

**Landed 2026-10-08 (`nitpick-time` 0.3.0 → 0.3.2's plans and work, `nitpick-regex` 0.1.6 → 0.2.1; all 2026-10-08):**

- **A fenced block that reads variables it never sets is a template, not a command.** "Every fenced command run verbatim"
  needs `env.sh` and a `REPO=` prefix first. *(`nitpick-time` 0.3.0's plan.)*
- **A sweep must not read plan files whose Expects quote that sweep.** *(`nitpick-regex` cycle 0.1's close plan.)*
- **A decision that corrects a REASON is swept for the reason in every wording**, not only the rule's. A reason is restated
  wherever the rule is sold or compared, not beside the rule. *(`nitpick-regex` 0.1.6a.)*
- **A predecessor's record, simulated by its title and ticks, cannot predict a later plan's sweep.** Simulate it with the
  evidence its own plan prescribes for each box, or mask the counts a record's lines can move. *(`nitpick-regex` 0.1.6b.)*
- **A patch that cites the plan's own sections goes stale when they move.** No comparator sees a citation, so check each one
  against the headings before the plan commit. *(The same.)*
- **Enumerate the domain before naming its exceptions, as before naming the universal.** A dispatch named four asynchronous
  prelude names off `nitpick-time`'s `check_purity` list; enumerating every function and method of the pinned prelude found a
  fifth, `LineBufWriter.flush`, through the private `tw_write_all`. *(`nitpick-time` 0.3.1's fix.)*
- **A structure a specification draws before any code is a hypothesis.** `HIR.md` H-2's three `int32` operands could not hold
  a Repeat that is a list member. *(`nitpick-regex` cycle 0.1's close.)*
- **Use a patch placeholder that no touched file holds.** *(`nitpick-regex` 0.2.0's plan.)*
- **A pointer in an added line is checked against the documents as the patches leave them**, rule numbers too.
  *(`nitpick-regex` 0.2.0.)*
- **Rule identifiers are future numbers too.** `check_specs_current` never fails, so a forward rule citation passes every gate
  a planner runs: write "the next rule", as with decisions above. That the plan skill should read its unresolved count is an
  `npk` finding, owed to the plugin's keeper. *(`nitpick-time` 0.3.2's plan.)*
- **A correction's list of sites is a claim about a set.** The orchestrator's four named texts for `nitpick-regex` 0.2.1 had
  thirteen twins in other words, found only by reading every sentence about where the build stops. *(`nitpick-regex` 0.2.1.)*
- **A rehearsed patch chain amends cleanly as replacements over the raw chain's trees**, with no count moved; the amendment
  bullet above gives the procedure. *(The same.)*
- **A currency gate is a claim about a set**, checked by enumerating the declared constants. `nitpick-time` 0.3.2's gate 9 said
  every kernel number was filed, and two verifier rounds found ten of its 23 declared constants with no row.
  *(`nitpick-time` 0.3.2's filing fixes.)*

**Landed 2026-10-09 (`nitpick-time` 0.3.2's work and `nitpick-regex` 0.2.1a's plan; 2026-10-08 and 2026-10-09):**

- **An adoption re-spells at the OLD pin first, then moves the pin.** The old compiler then testifies that the re-spelling
  changed no answer (every file's codes and sites identical, the full run green), and only then does the pin move. The old pin
  cannot prove the re-spelling TRUE: at `5fbaf4a` a write through a `fixed` slice (DEF-230) and a reassigned `fixed` parameter
  (DEF-248) compile in silence, so only the new pin's census shows that no slot is written through. Plant both shapes as the
  adoption's mutants. A re-pointed `fixed` local is refused at both pins; only the parameter was silent. *(`nitpick-regex`
  0.2.1a's plan and its verifier.)*
- **A number carried from a brief is a claim to check against the plan's own text.** `nitpick-time` 0.3.2's block 3m has 35
  rows; a handoff's "34" travelled into a worker's and a verifier's NOTES unchecked, and the verifier found it. *(`nitpick-time`
  0.3.2's verifier.)*
- **A count of sites is not a count of slots.** `nitpick-regex` 0.2.1a's plan said "the five `src/` locals", taking §1.3's
  five TYPE-007 sites for five locals; one of them is an ARGUMENT, re-spelled through its callee's parameter, and `src/` held
  four. A plan verifier's PASS and four SAME rehearsals passed it, because no block reads a decision's prose against the tree;
  the worker caught it by enumerating the set the sentence names before its patch applied. *(`nitpick-regex` 0.2.1a's worker.)*

**Landed 2026-10-15 (`nitpick-time` 0.3.4's plan and close, `nitpick-regex` 0.2.5's work; all 2026-10-15):**

- **A close's tools stage exactly the files they write**, so the plan's `RUNNING` title stays out of every commit but the
  record's, where a block's `git add -A` would carry it into a work commit. At `nitpick-time` 0.3.4 the title was the one
  unstaged change after each of five work commits. *(`nitpick-time` 0.3.4's plan and close.)*
- **A close reads every plan's §7 against the later cycles' READMEs.** A hand-on recorded only in a plan's §7 goes into the
  archive with the plan and has no live home. `nitpick-time` 0.3.4's planner found three, and the close carried them (H1 …
  H3). *(`nitpick-time` 0.3.4's plan.)*
- **Sweep for what a function SETS, not only for what it reads.** A step that makes a reader call a writer owes a sweep of
  every sentence saying that the reader writes or sets nothing. Since `nitpick-regex` 0.2.5's RX-242, RX-239's *"`hir_read`
  sets none"* (its `meta/DECISIONS.md:6434`) is false, and no sweep looked for it; 0.2.6 marks it. *(`nitpick-regex` 0.2.5's
  work.)*

**Landed 2026-10-16 (`nitpick-regex` 0.2.5a's plan, its fix round and its scoped re-verification; all 2026-10-16):**

- **A measurement of a declaration is not a measurement of the names it declares.** RX-134's `K`, a struct of three keyword
  fields, compiled at three pins and was read as "a field is its own namespace". Through `7e91730` a keyword field was the
  EMPTY name, one to a struct: a literal writing two of them is `NITPICK-TYPE-028`, *"'' is given twice"*. From `c9baa9e`
  each is `NITPICK-PARSE-001`. Measure a name by writing it and reading it back, and two of them together. *(`nitpick-regex`
  0.2.5a's plan.)*
- **An adoption's mutants can make the OLD pin testify to a change's completeness, not only to its harmlessness.** Put each
  changed site back alone. If the old pin refuses every one, its green run says the change is whole. `nitpick-regex`
  0.2.5a's fourteen rename mutants did this, each code site refused at both pins. This extends the 2026-10-09 bullet above,
  where the old pin could not prove a re-spelling true. *(The same.)*
- **Compare emissions across pins over ONE tree.** An added comment line moves a program's site table. Two trees at two pins
  therefore differ for two reasons at once. Compare two trees at one pin, or one tree at two pins, each pair through the
  compiler's normalisers (`attrnorm.py`, then `dropnorm.py`). *(The same.)*
- **A landing's sweep counts only the files its base compiles.** F47's "24 programs differ by flag tests" was measured while
  78 of `nitpick-regex`'s files were refused by both compilers of that leg (landing 103's `TYPE-007`). At the adoption of
  `c9baa9e`, landing 105 moves 78 of regex's 155 emitted files: 3 076 drops are made unconditional, flag tests only. Read a
  landing's count with the set it could compile, as §6's "refused by both" bullet says. *(The same.)*
- **A red run's summary shows each check's status.** A helper that prints only the tree checks' names, with the FAIL lines
  filtered out, shows a red check as green. `nitpick-regex` 0.2.5a's `env.sh` counts the checks by status. *(The same.)*
- **A verifier's counter-example is itself a general rule until it is measured where it stops.** Against "a keyword as a name
  of any kind is `PARSE-001`", plan verification 1 said "a local is `PARSE-002`". That holds only for a local declared
  `T:name`: one that `wild` or `fixed` leads is `PARSE-001` at `c9baa9e`. Measuring each kind found two that the compiler
  does not refuse at all, a generic parameter's and a variadic's name, each read as the empty name. The scoped
  re-verification then swept all 170 keywords through each kind. A function's, a type's and a module's name were refused
  for 166 of the 170 at `7e91730`, not for all of them, and `comptime` is refused as a generic parameter. A claim measured
  with one member of a set (`end`) is still a claim about the set. *(`nitpick-regex` 0.2.5a's fix round and its
  re-verification.)*

**Landed 2026-10-16 (`nitpick-regex` 0.2.5a's work, at its work verifier's PASS):**

- **A keyword-named declaration that compiles proves only that it was not refused. Declare two of a kind to learn what name
  it took.** This morning's first bullet, for a field, holds for a declaration's own name. At `7e91730`, `func:acquire`
  alone compiles and runs 0 / 0. Beside `func:any`, both define `@"npk.<module>."`, and llc refuses the second as a
  redefinition: the EMPTY name, the shape DEF-235 closed for a field. This seat's brief had said the four exempt keywords
  "compile as those names". The worker measured two together before writing the amendment, and the work verifier
  reproduced it. *(`nitpick-regex` 0.2.5a's work.)*
- **Check each citation, not each document: the same section cited rightly beside it proves nothing.** RX-245 cited
  `SAFETY.md` §6 twice: rightly for the `Match` fields, and wrongly for the `comptime` wall, which is §7. Two plan
  verifications, a design pass and every block passed it, since no comparator sees a citation (the 0.2.0 bullet above).
  The worker found it by reading each of the twenty added lines that carry a pointer against the documents, before step
  2's commit. *(The same.)*
- **An Expect quotes no path the leak scan reads as a home.** `check_refs` flags `/home/<word>` in a tracked file. So a
  plan whose Expect quotes a tool's message holding its temp directory carries a home path, and so does a fake `HOME`
  named `home/<word>` under the scratch directory. Print a placeholder for each place (`<scratch>`, `<tree>`), and name a
  fake home so that the scan cannot read it as one (`$G/hm`). The planner's own `check_refs` found both before its
  commit. *(`nitpick-time` 0.4.0a's plan.)*
- **A sweep's reading can be keyed before it is read.** Key each saved line by its file and line against the plan's class
  table, and `git blame` the new-text classes against the plan's and the work's commits. In `nitpick-time` 0.4.0a, 464 of
  464 lines keyed, 148 of them new and 316 older. The eye is then left only the lines the join cannot settle, and the
  plan's table checks the reading instead of guiding it. *(`nitpick-time` 0.4.0a's record.)*
- **A re-pin can make an accepted decision's stated reason stale while no program moves.** Parse's PD-140 declined a
  count of reports per code because the compiler's DEF-245 reported one failing header two or three times, and PD-144
  said a `buffer` could not be ranged at the pin (D-341, settled and unbuilt). Landings 130 and 128, both carried by
  `2e1cb4a`, made each reason the compiler's state before the pin, and every program of the plan stayed the same, so no
  census saw it: the adoption found it by reading each accepted decision's text against the landings it carries. Read
  them so at every re-pin. A reason gone stale takes a dated note at the decision's landing, saying what the new pin
  measures; a clause that states what the plan does must be true when it lands, and is corrected (sockets' PD-167).
  *(`nitpick-parse` 0.0.1a's adoption plan (T12), 2026-10-23.)*
