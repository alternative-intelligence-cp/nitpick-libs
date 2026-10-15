<!-- Filed 2026-10-15 by nitpick-libs_19. Made by the API-credits runner (.internal/credits/run.sh, job docs-vs-code-nitpick-time-0.3-2026-10-15): headless claude -p on claude-sonnet-5-5, read-only tools, 113 turns, $2.40 of the plan's monthly API credits. Spot-checked by the seat before filing: TA-8 (README.md:184 reads "span/ # Duration interop and Period") and TA-11 (tests/unit/double_readings.npk:60–67 names the belts 40, 44, 60 and 61). Note: the verdict says three new findings, and the report lists four, TA-8 … TA-11. One edit for check_refs only: nitpick-time's own open rows are written without their `O-` prefix, because the workbench's checker reads a bare id as this registry's. It feeds 0.3.4's close by its TA ids. -->

# nitpick-time, documents against code at fa9fb37 — an audit before the cycle 0.3 close, 2026-10-15

**Verdict.** I found no defect in code, no document that is wrong, and no cross-reference that fails to resolve. The tree bears out everything cycle 0.3.3 and the cycle 0.3 README say about the double, its tests and the counts. I added up every count that could be added by reading and none disagrees. TA-1 … TA-7 are all fixed. The three new findings are wording. Nothing in the tree blocks the close, but 0.3.4 should fix those three and carry the compiler-side items listed under NOT CHECKED. I read everything and ran nothing.

## The earlier findings, TA-1 … TA-7

- **TA-1 — fixed.** `README.md:9-12` says "its first five subcycles done", and `CONTRIBUTING.md:7-10` and `CLAUDE.md:10-18` say the same.
- **TA-2 — fixed.**
  - `README.md:160-164` restates the row-by-row status, with the dated note.
  - `README.md:174` reads "realtime and boot clocks through `clock_gettime` and the monotonic one through the floor's `mono_now()`".
  - `src/host/host.npk:27` agrees.
- **TA-3 — fixed.** `tests/conformance/README.md:26-29,36` dates both phrases and carries the tagged 84 and 13. `tests/conformance/import.npk:118-120` dates the `ETimeZone` line. `src/lib.npk` has 84 `pub use` lines.
- **TA-4 — fixed.**
  - `TESTING.md:553` now reads "every test of a `src/host/` function".
  - `CONTRIBUTING.md:125-127`, `ROADMAP.md:267-269` and `meta/roadmap/0.8/README.md:18` carry the dated notes.
  - Nine files carry `// stress: 40`: `host_clocks`, `double_substitution` and the seven `system_zone_*` units.
  - No test calls a `host_*` function without it. The probe hits are comments only.
- **TA-5 — fixed.** `TIME_MODEL.md:203-204` has `sealed` on every field, and the dated note at `:210` explains it.
- **TA-6 — fixed.** `SPAN_MODEL.md:195` reads `ETimeValue`/`YearRange`, with the note at `:217`.
- **TA-7 — fixed.**
  - `examples/README.md:3-8` says "Nothing is here yet, and the harness has no such stage". It puts the examples at cycle 1.0.3, and the dogfood consumers in `nitpick-posix`.
  - `README.md:189` and `CLAUDE.md:1066-1068` say the same.
  - `meta/roadmap/1.0/README.md:17` has the 1.0.3 row.

## NEW FINDINGS

**TA-8 — wording.** The layout blocks still describe `src/span/` as only the Duration interop and `Period`.
- Doc: `README.md:184` and `CLAUDE.md:1057` read "span/ # Duration interop and Period".
- Code: `src/span/span.npk:244,261,279` hold `instant_of`, `instant_add` and `timestamp_of`, with `Instant` and `Timestamp`. `README.md:160` itself says instants exist.
- Fix: write "`Instant`, `Timestamp`, the conversions, the Duration interop; `Period` later".

**TA-9 — wording.** The spec index omits the test double that HOST.md §3 carries.
- Doc: `meta/specs/README.md:28` reads "the one impure module: the clocks and the system-zone discovery".
- Spec: `HOST.md:154-199` (H-9 … H-11) is the test double, and TM-261 amends it.
- Fix: add "and its test double".

**TA-10 — wording.** The double's header attributes the compiler's diagnostic text to D-211 as though it were D-211's own words.
- Doc: `tests/double/host_double.npk:16-18`, `CLAUDE.md:33-35` and TM-261 quote "keep mutable process state in `main`'s scope where it flows through the calls that need it" as "the compiler's D-211".
- Compiler: that string is `NITPICK-TYPE-055`'s message, `src/frontend/type_stmt.npk:3062`, and the message cites D-211. D-211's own text is "mutable process state lives in `main`'s scope and flows explicitly" (`meta/specs/DECISIONS.md:15539-15540`).
- Fix: "`NITPICK-TYPE-055`, whose message cites D-211" in the three places, or leave it. The claim itself is right.

**TA-11 — wording.** The cycle README's tick for the double's demonstration names two belts where the test's header names four.
- Doc: `meta/roadmap/0.3/README.md:141` reads "`double_readings`' 60 and 61, the belts its header names".
- Test: `tests/unit/double_readings.npk:60-67` names four belts, 40, 44, 60 and 61. `0.3.3.md` §1.9 and the execution record say four.
- Fix: write "40, 44, 60 and 61".

## KNOWN AND EXPECTED, each still holds

- **`__pycache__` and `build/`.** `harness/selfcheck.py:296` starts the runner with `sys.executable` and no `-B`. `harness/__pycache__/` and `build/` are present in the working tree.
- **Block 5 and §3b.** The record gives block 5's counts (567 saved lines, 511 distinct) and points to §3b.
- **Rehearsed readings.** The `facts.sh` labels and the control-paragraph hunk are recorded as "left as rehearsed" (`0.3.3.md` §"Readings, left as rehearsed" and the control paragraph).
- **Batch heading.** The heading at `meta/DECISIONS.md:8713` still says the orchestrator accepted TM-260 … TM-262.
- **Compiler-defect candidates.** `0.3.3.md` §1.2 and §9 describe both. Nothing in `tests/double/` relies on either.

## CHECKED AND HELD

Counts below were added up by reading.

**Code against the specifications and decisions**
- **Seam and handles.** `HostReadings` has 5 methods in H-1's order and signatures, with `never fails` on `now_instant` and `system_zone` (`host_double.npk:72-78`), as TM-261 states. The setters, refusers and `stepped_host` have the signatures TM-261 gives.
- **Types and fields.** `HostClock`, `ZoneSource` and `SystemZone` are `host`'s own and the double declares none (`host.npk:91,188,198`). `FakeHost`'s fields are all `hidden`, and its start is the epoch, both instants at 0 ns, no zone, resolutions 1 ns, nothing refused.
- **Imports.** The double has 8 `use` edges: `host`, `span` six times, and `core` limits once, matching the cycle README and TM-260. `check_layering` (`harness/checks.py:204-366`) does what TM-260 says. Its three plants and three controls are in `selfcheck.py:1071-1088`.
- **`src/` unchanged.** `host.npk` still has 5 public functions and 3 public types, as H-1 and TM-256 say. By reading, the 0.3.3 work touched nothing in `src/`.
- **Spec dating.** H-9 and H-10 carry the TM-261 notes (`HOST.md:167,191`). BUILD B-17 (`BUILD.md:613`), TESTING §2 (`TESTING.md:46`) and V-11 (`:559`) carry theirs. DECISIONS has TM-249 and TM-256 marked "Read with TM-261".
- **Layering and exemptions.** `EXPECT_EXEMPT` holds 7 entries, the double the seventh (`run.py:122-194`). There are 5 `[[test]]` entries and the `golden` entry exists.
- **Compiler decisions.** D-211, D-165, D-287, D-298, D-348, D-349 and D-350 exist at e50eaf4 with the cited content. TYPE-055, 086, 035 and 084 and ASSIGN-002 exist in the compiler's frontend.

**Tests and counts**
- **The 163 `.npk` files.** 10 in `src/`; probes 59; support 4; defect 36; unit 42; sweep 8; fixture 1; conformance 1; golden 1; double 1. That sums to 163 and matches the tag at `run.py:649,681`. The equation `163 = 7 + 111 + 3 + 1 + 1 + 40` holds, with 111 = 59 + 42 + 8 + 1 + 1. `146 = 35 + 111`.
- **`double_readings`.** Its header's exit map matches the code, with 47 exits and 4 belts. 31 + 12 named = 43 reachable, so every exit but the four belts is reached. The 11 `failsafe` arms match "eleven".
- **`double_substitution`.** Its header's exit map matches the code, with one belt (exit 30). Its window, 1.6e9 … 4.1e9, is `probe03`'s (`probe03_timespec_sys.npk:44-45`).
- **The golden.** It has 9 lines. I re-added their lengths by hand: 100 + 100 + 103 + 126 + 155 + 142 + 130 + 148 + 162 = 1 166 B, as stated. The program's sequence and `oracle.py`'s agree line by line. 1760270400 is 2025-10-12 12:00 UTC.
- **Named mutants.** `named.tsv` has 18 rows: 3 + 2 + 2 + 5 + 6. The 283 = 88 + 188 + 7 arithmetic and the seven unseen are consistent with the double's text.
- **Patch shapes.** 8 `?|`, 4 `move(` and 1 non-literal `exit said;` in the five files, as §1.11 says.
- **Harness numbers.** The 119 plants fit `selfcheck.py`: 111 `PLANTED` + 3 + 5 view plants. `harness/README.md:547-560`, `ci.yml:56-58`, `nitpick.toml:141-143` and `CLAUDE.md:69` agree on 146, 119 and 163.

**Status, lists and cross-references**
- **Counts.** There are 193 `### TM-` headings, and the last is TM-262. ROADMAP says 193. OPEN_QUESTIONS has exactly 7 open: N1, N2, N3, X1, B1, X4 and X8. Q-7 is struck and the cycle README resolves it. All five 0.3 subcycle titles read DONE with the dates README, CLAUDE.md, CONTRIBUTING and ROADMAP give.
- **Specs and rows.** TESTING V-1a's 22 rows, 19 live and 3 pending are unchanged, and TM-260 declines a 23rd row. `HOST.md` H-12 … H-16 agree with `host.npk` for the surfaces I read.
- **Links.** All 0.3.3 links resolve: the tools directory with every file §0 names, the `tests/double/README.md` links, `CURRENCY.md`'s row for the oracle, and the cycle README's links. The §5 acceptance boxes are unticked in 0.3.0 through 0.3.3 alike, so that is the house convention and not a finding.

## NOT CHECKED

- **Anything that needs a run.** That covers the 146 green units, the plant tallies as printed, the 283 and 18 mutant verdicts, the 1 166 B golden as written (I only re-added it by hand), CI run 38359396395 and the IR sizes.
- **Compiler behaviour at the pin.** I did not re-measure the §1.2 forms. I read only the decision titles and texts named under CHECKED AND HELD.
- **Later compiler landings.** At e50eaf4 I did not check whether D-341 (cycle README adoption item 4, the `#wild_slice` sites) is built. That item must be handed on at the close. The compiler landings 104 … 111 are outside this audit by instruction. 0.3.3 §7's hand-ons — whether to export the seam, at 1.0, and the first golden formats, at 0.4 — need a home in 0.4.0's plan.
- **Earlier text.** The execution records of 0.3.0 … 0.3.2a beyond the lines cited. The per-function claims of `check_purity`, `check_call_edges` and `check_wide_types` over `src/`. Spec rules of cycles 0.4 and later.