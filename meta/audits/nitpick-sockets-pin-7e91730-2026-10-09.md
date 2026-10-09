<!-- Filed 2026-10-09 by nitpick-libs_15. Made by the API-credits runner (.internal/credits/run.sh, job landings-83-103-nitpick-sockets): headless claude -p on claude-sonnet-5-5, read-only tools (Read, Grep, Glob), 51 turns, $0.55 of the plan's monthly API credits. Spot-checked by the seat before filing: SL-1 (ADDRESS_MODEL.md:245) and SL-3 (nitpick.toml:40 against the compiler's nitpick.toml:46), each read at the cited line in both trees, every quote as given. nitpick-sockets's next dispatch carries this audit by its SL ids. -->

# nitpick-sockets against compiler 7e91730 (landings 83–103) — an audit

**Verdict.** The library is planned, with no source and no `.npk` files, so nothing breaks today. It has six findings: three change a plan and three are wording. The one that matters is that the address parsers and decoders are specified over a plain `uint8[]` (ADDRESS_MODEL A-5, A-22; VERIFICATION Z-2). Landing 103 makes `string_bytes` return `fixed uint8[]`, which a plain slice parameter refuses with TYPE-007. The stream model's Reader/Writer spelling is already correct. The LLVM pin of 20.1.2 is stale in 7 places, and CI built on it would fail against 7e91730. This library is not in `libs_moved_103.txt`, which has sections only for nitpick-fuzz, nitpick-regex and nitpick-time. That matches the absence of code, so it tells us nothing about the specs.

## FINDINGS

**SL-1 — changes a plan (cycle 0.1.3, 0.1.2; also 0.1.1 and the 0.0 probes)**
- The address codec and parsers take a plain `uint8[]` where they only read.
- Library:
  - `meta/specs/ADDRESS_MODEL.md:245`: "**Rule A-22 — a parser is a pure function over `uint8[]`** … It takes a byte slice, not a `string`, so a caller parsing out of a buffer does not build one first."
  - `ADDRESS_MODEL.md:108` and `:110`: `addr_decode(uint8[]:src, int64:len)`, `unix_decode(uint8[]:src, int64:len)`.
  - `meta/specs/VERIFICATION.md:64`: `func:sin_port_at = uint16(uint8[]:sa)`.
  - `meta/roadmap/0.1/README.md:65`: `unix_addr_path(uint8[])`.
  - `0.1/README.md:73`: "every parser takes `uint8[]`, not `string`".
  - `ADDRESS_MODEL.md:180` and `meta/DECISIONS.md` (SK-023): `unix_addr_path` "takes a byte slice".
- Compiler:
  - `meta/specs/TYPE_REFERENCE.md:1233-1243`: "`fixed T[]` is the READ-ONLY VIEW … a plain `T[]` converts to it … and it converts back to nothing (`NITPICK-TYPE-007` …). It is PRODUCED … by `string_bytes` (always …)".
  - `MEMORY_REFERENCE.md:240-246` says the same.
  - `IO_REFERENCE.md:38`: "`string_bytes(s)` IS one (D-351)".
- Consequence (inferred from those rules; no probe exists):
  - A caller who has a `string` — a config value or a CLI argument — has no way to reach a parser that wants a plain `uint8[]`.
  - The same holds for a view of `fixed` storage, or of a received buffer held in a `fixed` aggregate.
  - A-22 gives the exact case: "so a caller parsing out of a buffer does not build one first". The string case is the other half of that.
- Change:
  - Spell every read-only byte parameter `fixed uint8[]`: the parsers, `addr_decode`, `unix_decode`, `sin_port_at`, `unix_addr_path`, and every Z-2 accessor.
  - Keep a plain `uint8[]` only where bytes are written: `addr_encode:dest`, `unix_encode:dest`, and the receive `dest`.
  - Amend A-22 and the 0.1.2 and 0.1.3 checklists.
  - Add a 0.1.3 test: `socket_addr_parse(string_bytes(s))` must compile.

**SL-2 — changes a plan (cycle 0.0.4, 0.1.4, 0.2)**
- `Bytes::view()` returns a mutable view, which is the wrong type for a write path.
- Library: `meta/roadmap/0.0/0.0.4.md:61-62`: "`view()` hands a borrowed `uint8[]` for a write path." The same section's `take()` hands out an owned `string`.
- Compiler: `IO_REFERENCE.md:31`, `Writer.write` takes `fixed uint8[]:wsrc`, and `TYPE_REFERENCE.md:2080-2095` says the view's type carries the read-only right.
- Change:
  - `view()` should return `fixed uint8[]`. A plain `uint8[]` also converts into `write`'s slot, but a read-only view is the accurate type, and a `fixed` view cannot be passed back into a plain `uint8[]` slot.
  - That matters for the receive path: `Bytes` as a sink for `read` needs a separate writable accessor.
  - The spec does not say which accessor feeds `read`. Name both.

**SL-3 — changes a plan (cycle 0.0.1 CI, 0.0.0 pre-flight, and every cycle that builds)**
- The LLVM pin is stale: 20.1.2 where the compiler now pins 20.1.8.
- Library, 7 sites:
  - `nitpick.toml:40`: `llvm = "20.1.2"`.
  - `README.md:113`: "LLVM 20.1.2 — the same toolchain the compiler pins".
  - `CLAUDE.md:125`: "LLVM 20.1.2 exactly, pinned".
  - `meta/roadmap/0.0/README.md:63`.
  - `meta/roadmap/0.0/0.0.0.md:333`: "`llc` and `ld.lld` must be the pinned 20.1.2".
  - `meta/roadmap/0.0/0.0.1.md:52`: "installs LLVM 20.1.2".
  - `nitpick.toml:35-36` says "pinned to the exact patch release the compiler pins", so that claim is now false.
- Compiler:
  - `nitpick.toml:46`: `llvm = "20.1.8"`.
  - `meta/specs/TCB.md:53`: "LLVM 20.1.8 `llc`, `ld.lld` … — 20.1.2 from 1.4.5 until D-349 (2026-10-08)".
  - `INSTALL.md:25-26`: Ubuntu 24.04 "ships 20.1.2, which §6 refuses".
- Change:
  - Set 20.1.8 at all seven sites.
  - Add to the 0.0.1 CI step that `apt install llvm-20` is not enough on noble. CI must use the LLVM project's packages (INSTALL.md lines 54-61).
  - Re-measure any 0.0.0 probe baselines. They were taken under 20.1.2, and the toolchain pin is "a build input (D-204)".

**SL-4 — wording (cycle 0.3, 0.0 probe 06)**
- The Reader/Writer plan says "exact signatures" but never names the `fixed`.
- Library:
  - `meta/roadmap/0.3/README.md:31`: "with the prelude's **exact** signatures — `Self->`, `async`, `Duration:within`".
  - `meta/roadmap/0.0/0.0.0.md:182-190`: probe 06 "the trait's exact signature … TYPE-048".
  - `STREAM_MODEL.md:37-40` is already correct: `fixed uint8[]:wsrc` on `write`, plain `uint8[]:dest` on `read`.
- Compiler:
  - `IO_REFERENCE.md:36-39`: "an impl declares `wsrc` as the trait does (`NITPICK-TYPE-014` otherwise …)".
  - `TRAITS_REFERENCE.md:71-75` says the same.
- Change:
  - Add "`fixed uint8[]:wsrc` on `write`, TYPE-014" to both checklists.
  - Probe 06 should include a negative case: an impl that drops `fixed` is refused TYPE-014. That is a measurable fact for the board.

**SL-5 — wording (README.md:11, 0.0.0.md:24, specs/BUILD.md:10, OPEN_QUESTIONS.md:49, DECISIONS.md:53, specs/README.md:31, VERIFICATION.md:7)**
- The documents state the compiler's cycle as 1.5 (verification) and measure its tooling at "1.5.0 (2026-09-03)".
- Compiler:
  - `TYPE_REFERENCE.md:1233`, `IO_REFERENCE.md:36`: "1.6.1e landing 103".
  - `TCB.md:53` is dated 2026-10-08.
  - I found no one-line current-cycle statement in the compiler's ROADMAP (`ROADMAP.md:13` and `:296` are generic).
- Change:
  - Re-date the README and 0.0.0 cycle claims to 1.6.1e at 7e91730.
  - Keep BUILD.md §1's "npkg cannot build a library" as a dated measurement. Mark it "re-measure at 7e91730" rather than silently restating it. I did not re-check it.
  - VERIFICATION.md's cycle table (1.5.0 done; 1.5.1–1.5.4 pending) cannot be settled from the documents I read. See OPEN.

**SL-6 — wording (several files)**
- "fixed" is used as a size adjective beside the keyword. Each use is harmless to the compiler; the risk is that a reader sees `fixed` and thinks of the binding.
- Library:
  - `ADDRESS_MODEL.md:92`: "a fixed 128-byte array".
  - `SAFETY.md:97` and `:218-219`: "fixed-capacity", "fixed array".
  - `ANCILLARY_MODEL.md:64`, `:178`; `OPEN_QUESTIONS.md:152-153`.
  - `meta/roadmap/0.5/README.md:29`, `:37`: "one fixed block", "a fixed 256-byte stack array".
  - `SOCKET_MODEL.md:185`: "passing a fixed 128 there".
  - `DECISIONS.md:284`: "small, fixed-size".
- Compiler: `TYPE_REFERENCE.md:2080-2095`, where `fixed` before a slice type is now a type spelling.
- Change: use "constant-size" or "fixed-length" for sizes; reserve the bare word `fixed` for the keyword. In the ancillary control buffer (N-4, S-22), say "stack array of 256 bytes". It is a stack local the library writes into, not a `fixed` binding, so the read-only rule 98/103 does not apply to it. I infer this from the spec text; no `.npk` exists to confirm.

## NOT AFFECTED

- Module-level `fixed` byte buffers (98, 103): the grep for `\bfixed\b` found only prose. There is no `fixed` module state, and the spec places no byte buffers in module state. `Vec`, `Bytes` and the control buffer are locals or owned cells.
- Landing 102, the `fixed` parameter refused on assignment: no spec reassigns a parameter. The `fixed` mentions in the library are size prose.
- Mutex lock levels (83, LOCK-001/002): grep for `mutex|lock|Mutex|LOCK-` in the library's specs found only `locked`-free prose. There are no mutexes or channel waits at levels. Concurrency is a per-scope task join over `io_ready`/`suspend_io`, with no shared mutable state (CONCURRENCY_MODEL §§1-4).
- D-338 `comptime` strings, D-346 float literals, 88–89 flt literals, 87 constant families, D-347 frac: no floats, no `comptime`, no `frac`. The only numeric constants are integers (`NSOCK_*`, errno, `AF_*`).
- D-340 macros, 93 `#unreachable`, 96 unbounded generics, 95 templates, 90–91: the library declares no macros, templates or unbounded generics. The one generic is `Vec<T>`, with a bounded `T` (BUILD.md B-13), and it is local.
- 94 explicit `=> dyn`: the specs use `dyn Writer` only as a consumer-side binding (STREAM_MODEL.md:47; probe 06; 0.3/README.md:34). No explicit `=> dyn` cast is written. The 0.3 and 0.0 `dyn Writer` tests, if written with the cast, would now get the corrected single-ownership behaviour — an improvement, not a break.
- 99 (LLVM 20.1.8): affects the library only through SL-3.
- 101 lexer/parser seam and 100 sealed struct literal: no source, and the documents do not use the constructs.
- 83–86 (1.6.1e steps 3–3b): nothing in the library depends on them.
- Cited compiler rules still hold:
  - TYPE-046 (move-only) is cited at `TYPE_REFERENCE.md:512`.
  - TYPE-057 (the `OwnedFd` channel refusal, SK-035) is in `OPEN_DECISIONS.md:134`: "refuse … permanently under TYPE-057".
  - TYPE-048 is cited in `IO_REFERENCE.md`. I did not find it in the references that I searched.
  - D-004 (borrows are second-class) and the other D-numbers cited — D-032, 062, 070, 071, 072, 151, 163, 185, 188, 192, 210, 237 — I did not individually re-verify against the 7e91730 decisions file. They predate landing 83, and I found nothing in the landings' text renumbering them. Treat those as unverified.
- SK- numbers are the library's own; nothing in the compiler renumbers them.

## OPEN

- The compiler documents do not state, in one line, the cycle the compiler is "at", so SL-5's replacement text is a judgment. The landing text says 1.6.1e.
- VERIFICATION.md's 1.5.x table (1.5.0 "done", 1.5.1–1.5.4 future) cannot be settled from the documents I read. Whether contracts (1.5.3) and `limit<R>` (1.5.2) have landed was not checked at 7e91730. Re-read the compiler's verification reference before cycle 0.1.
- Whether a read-only `fixed uint8[]` can be ranged and passed into `sendto`'s pointer-and-length arguments in `wild` context was not settled from the documents. STREAM_MODEL T-6 takes `ptr, len` from `wsrc`. The pointer-from-slice rule (TYPE_REFERENCE §9.2.1 around line 1250) needs a 0.0 probe — a small one, as SL-4's negative case.
- BUILD.md §1's claims that `npkg` has no generic project path and `[dependencies]` resolves to nothing were measured at 1.5.0. I did not re-measure them at 7e91730.