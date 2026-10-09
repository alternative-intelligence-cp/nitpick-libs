<!-- Filed 2026-10-09 by nitpick-libs_15. Made by the API-credits runner (.internal/credits/run.sh, job landings-83-103-nitpick-parse): headless claude -p on claude-sonnet-5-5, read-only tools (Read, Grep, Glob), 33 turns, $0.41 of the plan's monthly API credits. Spot-checked by the seat before filing: PL-1 (PLUGIN_MODEL.md:52; IO_REFERENCE.md:31 for PL-2), each read at the cited line in both trees, every quote as given. nitpick-parse's next dispatch carries this audit by its PL ids. -->

# nitpick-parse against compiler 7e91730 (landings 83–103) — an audit

**Verdict.** One finding changes the plan: landing 103 breaks the library's byte-view signatures. The library is planned and has no source, so nothing is broken today, but the public contract needs rewriting before cycle 0.1. Every reader takes `uint8[]:src`, and `string_bytes` is the byte bridge B-11 names. At 7e91730 `string_bytes` returns `fixed uint8[]`, so the plain-slice reader refuses it with TYPE-007. The same kind shows up in the writer sink and in the probe set. The LLVM pin is stale (20.1.2 versus 20.1.8), and several statements about the compiler's cycle and state are stale. The other landings do not touch this library. The library is not in `libs_moved_103.txt`, which has no nitpick-parse section. Its only parse-named rows are `nitpick-regex/.../parse*.npk`.

## FINDINGS

**PL-1 — changes a plan (blocks 0.1 if left): reader and cursor signatures take plain `uint8[]`; a `string_bytes` result is `fixed uint8[]`.**
- Library:
  - `specs/PLUGIN_MODEL.md:52`: `pub func:json_reader = JsonReader(uint8[]:src, Options:opt);`
  - `PLUGIN_MODEL.md:131`: the same shape for `mini_reader`.
  - `specs/SCAN_MODEL.md:13`: `uint8[]:src;        // the caller's bytes — a borrow, never copied`
  - `SCAN_MODEL.md:41`: `cur_slice` returns "the borrowed `uint8[]`".
  - `specs/EVENT_MODEL.md:192`: `event_text(p, e) -> uint8[]`.
  - `EVENT_MODEL.md:243`: "constructed over a complete `uint8[]`".
  - `specs/VALUE_MODEL.md:84` (`doc_text`) and `:181` (`doc_num_text`) return `uint8[]`.
  - `specs/DIAGNOSTIC_MODEL.md:144`: `fault_render = NIL(ParseError:f, uint8[]:src, …)`.
  - `specs/GLOSSARY.md:8`: "the `uint8[]` the caller owns".
  - `roadmap/0.1/README.md:57`: `Cursor { uint8[]:src; int64:pos; }`.
  - `roadmap/0.2/README.md:43`: `event_text … -> uint8[]`.
  - Bridge: `specs/BUILD.md:147` (B-11), `string_bytes`, listed as prelude "fair game".
  - Test premise: `SCAN_MODEL.md:22`, "testable from a byte literal".
- Compiler: `TYPE_REFERENCE.md:1233-1243`: "`fixed T[]` is the READ-ONLY VIEW … A plain `T[]` converts to it … and it converts back to nothing (`NITPICK-TYPE-007` naming the rule…) … PRODUCED … by `string_bytes` (always…)". Also `IO_REFERENCE.md:36-38`, `MEMORY_REFERENCE.md:239-246`.
- Change:
  - Every read-only input, text and return slot becomes `fixed uint8[]`. That covers `src`, `Cursor.src`, `cur_slice`, `event_text`, `doc_text`, `doc_num_text`, `fault_render.src`, and the `Format` constructors.
  - A plain `uint8[]` caller still converts in, so the change widens the contract. A string caller needs `string_bytes` and nothing else.
  - `TRAITS_REFERENCE.md:71-75` and `TYPE-014` require an impl's slice parameter to be `fixed` exactly where the trait's is. Settle this before cycle 0.2.2, where the `Format` trait is fixed.
  - Cycles touched: 0.1 (`Cursor`), 0.2 (`event_text`, `EventSink`), 0.4 (`doc_*`), 0.5, and the 0.0.0 probes.
- Inferred, not measured: no probe has been run, so I have not seen the TYPE-007 report.

**PL-2 — changes a plan: the writer sink and the `Bytes` write path.**
- Library:
  - `specs/WRITER_MODEL.md:125` and `roadmap/0.5/README.md:45`: `func:put = NIL(Self->:self, Event:e, uint8[]:text);`
  - `roadmap/0.0/0.0.4.md:89`: "`view()` hands a borrowed `uint8[]` for the write path."
- Compiler: `IO_REFERENCE.md:31`, `async func:write = int64(Self->:self, fixed uint8[]:wsrc, …)`, and `:36`, "`write` takes the READ-ONLY VIEW … a plain view converts into `write`'s slot, `string_bytes(s)` IS one".
- Change:
  - `put`'s `text` becomes `fixed uint8[]`, mirroring the compiler's own writer. Otherwise a writer cannot be fed `string_bytes(key)` or an `event_text` result.
  - `Bytes.view()` may stay plain. A plain slice converts into a `fixed` slot, but `fixed` cannot convert back.
  - The `EventSink` trait must use `fixed` consistently with every impl (TYPE-014). Cycles touched: 0.0.4 (`Bytes`), 0.5, and the 0.7 writers.

**PL-3 — changes a plan: probes 06 and 08 (and 12) predate the `fixed T[]` type.**
- Library:
  - `roadmap/0.0/README.md:56`: "`probe08_slice_edges.npk` — a `uint8[]` borrow at the four escape-analysis edges".
  - `roadmap/0.0/0.0.0.md:251-269`: the four edges, and "a `Cursor` struct holding one".
  - `0.0.0.md:304`: probe 12, a `fixed` module-level table.
  - `0.0.0.md:223-243`: probe 06 and 07, a trait with `Self->` through a bound and through `dyn`.
- Compiler:
  - `TYPE_REFERENCE.md:1236`: a `fixed T[]` → plain conversion is TYPE-007.
  - `:1238`: "A write through it is `NITPICK-TYPE-086` and the address of its element `NITPICK-TYPE-071`".
  - `:1240-1243`: a range over a `fixed` array, or a slice read off a `fixed` struct, is also `fixed T[]`.
- Change:
  - Add a probe for `string_bytes` → plain `uint8[]` (expected TYPE-007, code recorded).
  - Add a probe for `string_bytes` → `fixed uint8[]` through a `Cursor` field and an `event_text`-shaped return.
  - Add a probe for a trait method with a `fixed uint8[]` parameter and an impl that drops the word (TYPE-014).
  - In probe 12, record that `TABLE[lo...hi]` over a `fixed` table is `fixed uint8[]` (`:1240`).
  - Reading the 256-byte class table (`SCAN_MODEL.md:86-88`) by index is unaffected by 98 and 103. Only writes and plain-slice conversions are refused.
  - Cycle touched: 0.0.0, which gates everything else.

**PL-4 — wording: LLVM 20.1.2 pinned in three places; the compiler pins 20.1.8 (D-349, landing 99).**
- Library:
  - `roadmap/0.0/0.0.1.md:53`: "installs LLVM 20.1.2".
  - `roadmap/0.0/README.md:69`: "CI … with LLVM 20.1.2".
  - `roadmap/0.0/0.0.0.md:356`: "`llc` and `ld.lld` must be the pinned 20.1.2."
- Compiler: `meta/specs/TCB.md:53`: "LLVM 20.1.8 `llc`, `ld.lld` … — 20.1.2 from 1.4.5 until D-349 (2026-10-08)".
- Change: say 20.1.8, or better, "the compiler's `[toolchain]` pin". Cycle touched: 0.0.1 (CI) and the 0.0.0 environment check.

**PL-5 — wording: statements about the compiler's state are stale.** These predate landings 83–103, so no landing caused them.
- Library:
  - `specs/BUILD.md:10`: "Read at the compiler's commit for cycle 1.5.0 (2026-09-03)".
  - `roadmap/0.0/0.0.0.md:27`: "cycle 1.5 (verification)".
  - `OPEN_QUESTIONS.md:61-63`: "`stack-depth` as an obligation kind scheduled for 1.5.8; nothing exists today".
  - `DECISIONS.md:271`: "does not exist today".
- Compiler:
  - `VERIFICATION_REFERENCE.md:930`: the `stack-depth` row is DERIVED by the runners from `terminate` rows, "no query, no guard", at 1.5.8c.
  - `NOTICES.md:58`: landing 46 (`def2728`) made the `stack-depth` rows live.
  - The compiler's cycle at 7e91730 is 1.6.1e.
- Consequence:
  - PA-022's grep-based `check_no_recursion` is still the right control, since the stack check "stays in every build" but nothing proves a bound for input-driven recursion.
  - O-N2's "nothing exists" and "1.5.8 as planned" are false. The `stack-depth` row now exists and is `open` unless `decreases` is stated.
- Change: re-date the BUILD.md §1 measurements and the O-N2 claim. The `npkg` and `[dependencies]` statements at `BUILD.md:12-22` are a 1.5.0 measurement that 83–103 do not address. Re-measure them (see OPEN).

**PL-6 — wording (optional): probe 07 and PA-071 could name landing 94.**
- Library: `PLUGIN_MODEL.md:75` (`builtin_open(...) -> dyn Format`); `0.0.0.md:236-240` (probe 07).
- Compiler: `DECISIONS.md:17346-17349`, landing 94 (DEF-227): "The explicit `dyn` cast (`x => dyn T`) lowers through `emit_fit` … a temporary is registered ONCE". The BOARD says "NO REFUSAL MOVES".
- Change: nothing is required. If probe 07 or `builtin_open` uses the explicit `=> dyn` form, record that it is owned exactly once (a drop-count assertion). Cycle: 0.0.0 and 0.2.2.

## NOT AFFECTED

Searches were over `meta/` excluding `scratch/`. The library has no `.npk` files.

- **102 (assigning to a `fixed` parameter).** `fixed` appears only for module tables (`DECISIONS.md:518`, `EVENT_MODEL.md:236`, `0.0.0.md:304`) and as an adjective ("fixed point", "fixed window", "fixed-capacity"). No planned parameter is `fixed`, and none is assigned to. After PL-1 adds `fixed uint8[]` parameters, none may be reassigned. `Cursor` advances `pos`, not `src`.
- **"fixed" as a size adjective.** Hits at `BUILD.md:167` ("a fixed-capacity ordered association list"), `0.0.4.md:32`, `0.0/README.md:16`, `roadmap/0.10/README.md:28,46` ("fixed window") and `TESTING.md:20,100`. Each is prose beside the keyword. This is the sibling's "size adjective" kind. I recommend rewording "a fixed window" and "fixed-capacity" in the roadmap and BUILD.md if the spec adopts `fixed uint8[]` as a type, to avoid confusion.
- **Byte buffers in `fixed` module state (98/103).** The only `fixed` module state is the read-only class table (C-8). `Bytes` is built over `buffer` and held per parse (E-22, "options are per parse, never global"). No buffer in `fixed` state is written.
- **101 (lexer/parser seam), 100 (D-337 sealed-field struct literal), 96 (unbounded generic), 95 (template ownership), 93 (`#unreachable();`), 92/D-340 (macro argument).** No source exists. Greps for `unreachable`, `macro`, `sealed`, and `Vec<` instantiation found nothing planned that these touch. The library says "no macro" (`PLUGIN_MODEL.md:11`, `DECISIONS.md:510`). `Vec<T>` is concrete in the plan.
- **97 (D-347, frac form), 91 (D-346, float literal fit), 88/89 (flt32/flt64 literals), 87 (DEF-179 constant families).**
  - Greps for `frac`, `flt64`, `flt32` and "float literal" show `flt64` and `frac64` only as accessor results (`VALUE_MODEL.md:171-181`; `DECISIONS.md:351-357,646`).
  - Format floats are parsed by the library's scanner at run time, not written as Nitpick source literals. The only floats are test-corpus data.
  - `frac64` is deferred to Q-3 (`OPEN_QUESTIONS.md:37`).
  - Re-check once 0.4 writes any `flt64` literal in source.
- **90 (D-338, `comptime` ordering strings).** No `comptime` appears in `meta/`.
- **94 (`=> dyn` explicit cast).** No pure-spec effect. See PL-6.
- **99.** Only the LLVM pin moved; see PL-4.
- **83–86 (1.6.1e steps 3–3b), LOCK-001/LOCK-002.**
  - `SAFETY.md:49`: "`nparse` has no concurrency. No task, no channel, no lock, no `await`."
  - `DECISIONS.md:90` agrees. Greps for `Mutex`, `mutex`, `spawn`, `thread`, `LOCK-` and `lock level` return only that prose, so no lock levels need naming.
  - The `await` mentions at `SCAN_MODEL.md:26` and `SAFETY.md:28` are D-004's escape rule, unchanged.
- **Cited compiler rules that still hold.**
  - D-004, D-018, D-041, D-070, D-078, D-123, D-147, D-151, D-152, D-183, D-185, D-206, D-210, D-211, D-237 and D-249 all exist in `DECISIONS.md` at 7e91730.
  - D-211 still reads "module bindings are `const`/`fixed` only".
  - `NITPICK-LEX-003` (`LEXICAL_REFERENCE.md:398`), `NITPICK-RESOLVE-005` (`BUILD_REFERENCE.md:184`) and `TYPE-046` (`TRAITS_REFERENCE.md:479`) are still cited as the library uses them.
  - D-004 rule 3 is amended by D-223 (a borrow never enters a `wild`-qualified slot), which is older than 83.
  - The library's PA- numbers are its own namespace. No collision with D-/DEF-/S- numbers was found.

## OPEN

- **D-223 and `Vec<T>`.** Whether the library's `Vec<T>` (`wild T->:items`) may ever hold `fixed uint8[]` elements, if a later cycle stores views, is not settled by the documents. This is not in the plan today; I did not check D-223.
- **BUILD.md §1 (npkg and dependency resolution).** The "no generic-project path" and "empty `[dependencies]`" claims are a 1.5.0 measurement. I did not check whether they still hold at 7e91730, and the landings 83–103 do not address them. Re-measure before cycle 0.0.2 (the harness).
- **`doc_text` return type.** Whether it should be `fixed uint8[]` or an owned copy depends on pool ownership (the D-8 borrow). The pool is the library's own storage, so a plain `uint8[]` would also type-check. This is a design choice, not a compiler constraint.