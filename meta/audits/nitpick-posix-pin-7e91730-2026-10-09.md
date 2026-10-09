<!-- Filed 2026-10-09 by nitpick-libs_15. Made by the API-credits runner (.internal/credits/run.sh, job landings-83-103-nitpick-posix): headless claude -p on claude-sonnet-5-5, read-only tools (Read, Grep, Glob), 51 turns, $0.61 of the plan's monthly API credits. Spot-checked by the seat before filing: XL-1 (0.0.0.md:167; MACRO_REFERENCE.md:288-290; DECISIONS.md:22329-22334, D-340) and XL-4 (nitpick.toml:28), each read at the cited line in both trees, every quote as given. nitpick-posix's next dispatch carries this audit by its XL ids. -->

# nitpick-posix against compiler 7e91730 (landings 83–103) — an audit

**Verdict.** The library has no code and no `uint8[]`, `string_bytes`, mutex, float, generic or `comptime` use. Seven of the eight probes are macro probes, and the macro landing is the one that bites. Landing 92 (D-340) changed what probes 02a and 02c measure, so the verdict table in `0.0.0.md` §6 no longer reproduces. PX-100's decision survives and now rests on firmer ground. Nothing blocks a cycle. Four items change a plan or a document (XL-1 to XL-4), and XL-5 and XL-6 are wording. The library is absent from `libs_moved_103.txt`.

## FINDINGS

**XL-1 — changes a plan. Probe 02a's recorded verdict is no longer what the compiler gives, and the stated reason no longer holds.**
- Library: `meta/roadmap/0.0/0.0.0.md:167`: "`#posix_failsafe(e)` … **REFUSED** `NITPICK-RESOLVE-002` — the ARGUMENT resolves in the macro's definition scope, not the call site; `#caller(NAME)` is the sole opt-out".
- The same claim is at `meta/roadmap/0.0/README.md:54-55` ("Refused `NITPICK-RESOLVE-002` (argument hygiene)"). The "hygiene" reading also recurs at `0.0.0.md:94-96`.
- Compiler: `meta/specs/MACRO_REFERENCE.md:288-290` says "**An argument resolves at the invocation site.**" D-340 (`meta/specs/DECISIONS.md:22329-22334`) measured these exact files: "`probe02a_failsafe_macro.npk`: RESOLVE-002 at the argument gone, and REACH-001 in its place".
- Change: re-run 02a and record REACH-001. Record that "argument hygiene" was a compiler defect fixed by landing 92 (D-340), not a language rule. Say plainly that the old table row is historical, and add a dated note. PX-100 says a settled decision's text is never rewritten, so supersede or annotate it.
- Cycle: 0.0.0 and 0.0.4 ("every probe verdict recorded").
- Consequence: 02a is now a clean test of PX-100's first reason. The argument resolves, and the refusal is only the `pick` being one block deep. PX-100, `SAFETY.md` S-3 point 1 and O-N7 remain correct, and the generated `failsafe` still stands.

**XL-2 — changes a plan. Probe 02c's recorded verdict changed from REACH-001 to MACRO-008.**
- Library: `0.0.0.md:168`: "`#caller(e)` as the argument … REFUSED `NITPICK-REACH-001` — clears hygiene, then 'no pick'". Also `0.0/README.md:56-57`.
- Compiler: `MACRO_REFERENCE.md:326-327`: "**`#caller` in an argument is `NITPICK-MACRO-008`** where the argument was written outside every macro body". D-340 (`DECISIONS.md:22333-22334`): "`probe02c_caller_arg.npk`: `#caller(e)` as the argument is MACRO-008".
- Change: record the new code. 02c no longer reaches the reach analysis, so it cannot support the "block, not macro" chain. 02e, 02d and 02a now carry that chain.
- Same site, measured as probe 02c, probe 02g (below) and `pxfail.npk` all use `#caller(...)` in an argument at the call site. The `0.0.0.md` P-3 and §4 prose (`:85`, `:99`) assumes the same form.

**XL-3 — changes a plan. Probe 02g's expected diagnostic is unmeasured at 7e91730.**
- Library: `tests/probe/probe02g_cross_module.npk:15`, `#posix_failsafe_with(#caller(EProbeOwn));`, at module level, outside every macro body. `0.0.0.md:172` records "REFUSED `NITPICK-MACRO-007`".
- Compiler: `MACRO_REFERENCE.md:326-327` (as above), and `:263-268`: "Invoking a macro from another module is `NITPICK-MACRO-007`". D-340's sweep names only 02a and 02c, not 02g.
- This probe now offers two refusals, MACRO-008 at the argument and MACRO-007 at the invocation. Which one is reported, or whether both are, is not in the documents.
- Change: re-measure. Drop `#caller(...)` from the call, or note that MACRO-007 may now share the report with MACRO-008. PX-100's decisive reason (MACRO-007, D-124) is unchanged by 92 and is still stated at `MACRO_REFERENCE.md:263`.

**XL-4 — changes a plan. LLVM pin of 20.1.2 where the compiler now pins 20.1.8.**
- Library: `nitpick.toml:28`: `llvm = "20.1.2"`. `meta/roadmap/0.0/0.0.2.md:28`: "`harness/toolchain.py` — the LLVM 20.1.2 pin".
- Compiler: `meta/specs/TCB.md:53`: "LLVM 20.1.8 `llc`, `ld.lld` … — 20.1.2 from 1.4.5 until D-349 (2026-10-08)". The compiler's own `nitpick.toml:46` says `llvm = "20.1.8"` (landing 99).
- Change: repin both to 20.1.8 before cycle 0.0.2 builds the harness check. The harness asks the tools for their version, so a 20.1.2 pin would reject the toolchain.
- Caveat: `BUILD_REFERENCE.md:44` still shows `llvm = "20.1.2"`. It is the schema example, and the compiler's own manifest and TCB.md are the authority.

**XL-5 — wording. `UTILITY_MODEL.md` shows a statement-position macro `failsafe` that PX-100 retired.**
- Library: `meta/specs/UTILITY_MODEL.md:23`: `func:failsafe = int32(Error:e) { #posix_failsafe(e) };   // SAFETY.md S-2`. Also `0.0.0.md:85`.
- Library: `SAFETY.md` S-2 says the handler is generated into `failsafe.npk`, and PX-100 says the same.
- Compiler: the shape draws REACH-001 per D-340's sweep (`DECISIONS.md:22332-22333`). It also omits the trailing `;` that `MACRO_REFERENCE.md:295-299` shows.
- Change: replace it with `use "./failsafe.npk".*;`, or the generated file, in the §1 sketch.
- Not caused by 7e91730, but the new landing makes the shape a known refusal.

**XL-6 — wording. The compiler's cycle is stated as 1.5.**
- Library: `0.0.0.md:16` ("The compiler is at `../../../nitpick`, cycle 1.5"), `specs/VERIFICATION.md:3`, `ROADMAP.md:97`.
- Compiler: landings 92–103 are all "1.6.1e" (`DECISIONS.md:22278`).
- Change: restate as 1.6.1e, or drop the pin, in favour of the board's toolchain commit.
- Cycle: 0.0.0, VERIFICATION.

## NOT AFFECTED

Each was searched across `meta/` (excluding scratch), `src/`, `tests/`, the root files and the `.npk` files. The patterns were `fixed`, `uint8`, `string_bytes`, `Mutex|lock`, `comptime`, `=> dyn`, `unreachable`, `frac|flt32|flt64|float`, `generic|<T>` and `D-3[0-9][0-9]`.

- **103 and 98 (`fixed T[]`, `string_bytes`).** The only hits are `UTILITY_MODEL.md:15`, `fixed OptSpec[]:SPEC = [ … ];`, and `ARGUMENTS.md:61`, `args_parse(spec[], argv)`.
  - Both are prose sketches, not code. `OptSpec[]` is a table of structs, not bytes.
  - It does not conflict with `TYPE_REFERENCE.md:1233-1236` ("`fixed T[]` … a plain `T[]` converts to it … and it converts back to nothing"). The direction here is `fixed` into plain.
  - **Worth noting at the first `posix_start`/`args_parse` signature (cycle 0.1):** the spec parameter must be `fixed OptSpec[]`. A plain `OptSpec[]` parameter fed a `fixed` binding is TYPE-007 (`TYPE_REFERENCE.md:2082-2083`).
  - No `string_bytes` call, reader signature, byte buffer or `fixed` module state exists anywhere, and no `uint8[]` occurs at all.
- **102 (assigning to a `fixed` parameter).** No `fixed` parameter exists in any file.
- **101 (one report per lexer/parser mistake).** The only mistakes are probe 02's refusals, which are not lexer or parser seam errors. `LEX-003` and `RESOLVE-005` for a digit-led `mod:` name (PX-101) are cited at `DECISIONS.md:259-264`, and D-147 and LEX-003 are still current (`DECISIONS.md:10517`, `:10559`). The "one report" change touches only the count of reports, not which code is raised.
- **100 (sealed-field struct literal).** No struct literals or sealed fields exist.
- **99.** See XL-4.
- **97 (frac form).** The only mention is `ROADMAP.md:115`, "`int256` and `frac`", prose, no syntax.
- **96, 95.** No generics or templates in any `.npk` or document.
- **94 (`=> dyn`).** No dyn casts exist.
- **93 (bare `#unreachable();`).** No `#unreachable` exists. The prelude error `Unreachable` appears only as a `pick` arm in the probes and is unrelated.
- **92.** See XL-1 to XL-3.
- **91, 88, 89 (float literals).** No float literals exist.
- **90 (`comptime` orders strings).** No `comptime` appears in the library.
- **87 (DEF-179 constants), 83–86 (1.6.1e steps 3–3b).**
  - No lock, mutex or LOCK-001/-002 in the library. The matches for "lock" were all "block".
  - No `spawn`, `thread` or `atomic` appears either. SAFETY S-8 mentions a lock only as an unplanned hazard.
- **Citations that still hold, checked in the compiler:**
  - D-124 and MACRO-007 (`DECISIONS.md:9338`, `:9391`; `MACRO_REFERENCE.md:263-268`).
  - D-057 and §4's "becomes a block" (`MACRO_REFERENCE.md:54`).
  - REACH-001 and REACH-002 (`DECISIONS.md:999`, `:16309`, `:18339`).
  - D-147.
  - 02b, 02d, 02e and 02f are not named in D-340's change list.
  - One citation is unchecked: the prelude names in the arms (`HeapOom`, `HeapBadRequest`, `WildLeak` and the like).

## OPEN

- Whether MACRO-007 or MACRO-008 is reported first for 02g (XL-3). It needs a run.
- Whether `reach.npk`'s top-level-only walk (the O-N7 claim, "Find the ONE top-level pick…") is unchanged. D-340 says the reach analysis "does not see a `pick` an expansion's block holds", but this audit did not read `reach.npk`. I took 02e's refusal from the library's own record, not a run.
- Probes 02a, 02c and 02d carry `// expect-exit: 70`, but at 7e91730 they are refusals, so the header is not what they produce. `0.0.0.md:24-25` says 0.0.2 picks them up as `unit` entries. The documents do not say whether the harness has an expect-refusal convention.
- Whether the prelude's error-identity names in the probe arms are all still current. This needs a compile, not a read.