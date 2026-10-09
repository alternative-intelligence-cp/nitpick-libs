<!-- Filed 2026-10-09 by nitpick-libs_15. Made by the API-credits runner (.internal/credits/run.sh, job docs-vs-code-nitpick-time-2026-10-09): headless claude -p on claude-sonnet-5-5, read-only tools, 123 turns, $5.29 of the plan's monthly API credits. Spot-checked by the seat before filing: TA-4 (TESTING.md:553 V-11; 8 test files carry `stress:`; probe03_timespec_sys.npk:79 reads CLOCK_REALTIME through sys) and TA-7 (examples/ holds only its README; nitpick.toml has 4 [[test]] entries). One edit for check_refs only: the list of nitpick-time's own open rows is written without their `O-` prefix, because the workbench's checker reads a bare id as this registry's. nitpick-time's next dispatch carries this audit by its TA ids. -->

# nitpick-time, documents against code at 989c772 — an audit

**Verdict.** The 0.3 documents bear out against the tree almost everywhere. I found no defect in code, no contradiction between a decision and the code, and no cross-reference that fails to resolve. Everything below is a document that is stale or overstated. Most of it is README-level status text and two "everything" claims.

**What I could and could not read.** I read the 0.3.2 mutant arithmetic, the plant counts, the unit arithmetic (134 → 143), the host module, the umbrella and the ban list. All of these agree with their documents by reading. None was re-run.

## FINDINGS

**TA-1 — wording. README.md opens with a status the same paragraph contradicts.**
- README.md:9-10: "cycle 0.3, the host boundary, is in progress — its first subcycle, the clocks, done on 2026-10-08".
- README.md:33-40 of the same block reports 0.3.1 and 0.3.2 as done.
- CONTRIBUTING.md:7-9 ("first three subcycles done") and CLAUDE.md:10-15 say three. ROADMAP.md:102 lists three as DONE.
- This is already filed: `meta/audits/ecosystem-early-2026-10-09.md:114` (E2-10).
- Fix: "its first three subcycles, the clocks, the purity instruments and the system zone, done on 2026-10-08".

**TA-2 — document wrong. README.md's layer table says only the calendar exists, and mis-describes the host row.**
- README.md:152: "The **calendar** row exists since cycle 0.1; every other row is a later cycle".
- Against the tree, `src/span/span.npk` has `Instant`, `Timestamp`, the conversions and the `Duration` interop; `Period` is the only part still future (README.md:158-159). The README's own opening block describes them.
- `src/host/host.npk:124-323` has the clocks and the system zone.
- README.md:163: "`clock_gettime` for the three clocks". HOST.md H-5 and `host.npk:138-139` read the monotonic clock through the floor's `mono_now()`, not `clock_gettime`. Only the realtime, boot and resolution reads use `sys`.
- Fix: restate the sentence per row (instants, the `Duration` half of spans and host exist; `Period`, zones and formats are later). Write "two of the three clocks through `clock_gettime`, the monotonic one through `mono_now()`".

**TA-3 — document wrong. `tests/conformance/README.md` describes an empty umbrella.**
- tests/conformance/README.md:23: "`import.npk` imports an umbrella that re-exports nothing, which is the point".
- Lines 31-34 say "importing `ntime` today costs a consumer exactly nothing" and "no arms beyond … a floor of four". Lines 28-30 date this to 0.0.1.
- `src/lib.npk:22` says it re-exports 84 names, and `import.npk:157-173` names thirteen arms.
- The 0.0.1 measurement is labelled as such. "Re-exports nothing" and "today" are not.
- Fix: say the file was written against an empty umbrella; it compiles against the 84-name one and carries a 13-arm `failsafe`.
- Related and cosmetic: `import.npk:115-116` still says "`ETimeZone` at 0.3". It sits in a paragraph kept as history, but `SAFETY.md:91` and `0.6/README.md:25` put the identity at 0.6.

**TA-4 — document wrong. "Everything that reads a clock" carries `// stress: 40`, but one probe does not.**
- TESTING.md:553: "`// stress: 40` on everything that reads a clock". CONTRIBUTING.md:122: "Anything that reads a clock runs forty times, not once."
- `tests/probe/probe03_timespec_sys.npk:79,105,121` reads `CLOCK_REALTIME` twice and `CLOCK_BOOTTIME` once through `sys(228, …)`.
- A search for `stress:` under `tests/` finds 8 files: `host_clocks` and the seven `system_zone_*` units. `probe03` is not among them.
- V-11's second sentence scopes the rule to `src/host/`'s functions, and `host_clocks.npk:2` does carry the marker, so the gate in 0.3/README.md:168 holds.
- Fix: write "every test of a `src/host/` function".

**TA-5 — stale. TIME_MODEL.md §4 shows the civil types unsealed.**
- TIME_MODEL.md:203-204: `pub struct:CivilDate = { int32:year; uint8:month; uint8:day; };`.
- `src/cal/cal.npk:199,206` and CALENDAR.md:126-127 have `sealed` on every field. CALENDAR.md:135-138 carries the dated amendment.
- TIME_MODEL.md has no note, although its §2 and §3 blocks were amended in the same way (`TIME_MODEL.md:50-53,149-153`).
- Fix: a dated note under the block pointing at CALENDAR.md C-8c, or `sealed` in the block.

**TA-6 — cosmetic. SPAN_MODEL.md §5's table row for `timestamp_add` names the wrong detail.**
- SPAN_MODEL.md:195: "checked, `ETimeValue`/`Overflow`".
- Code: `span.npk:351-352,363` give `ValueFault.YearRange`, as the note at SPAN_MODEL.md:212-216 says.
- The decision text is not rewritten by policy, so this is the table row only.

**TA-7 — dormant claim. `examples/` is described as built and run by the harness.**
- examples/README.md:3: "built and run by the harness, so a broken example is a red run". README.md:178 and CLAUDE.md:982 repeat it.
- `examples/` holds only that README. `nitpick.toml` has four `[[test]]` entries (probe, unit, sweep, conformance) and none for `examples/`. The stages in `harness/README.md:30-43` and `stages.py` have no examples stage.
- Fix: "planned for cycle 0.7" in the three places, or add a stage.

## CHECKED AND HELD

**Counts and tags**
- **Umbrella count.** `lib.npk` has 84 `pub use` lines (core 38, cal 22, span 16, host 8), matching `lib.npk:22` and CLAUDE.md:35. The 81, 76 and 68 history also reconciles.
- **Probes.** `tests/probe/*.npk` is 59 files, 29 `expect-error` and 30 run, as `nitpick.toml:71-89` tags.
- **Sweeps.** `tests/unit/sweep/` has 8 members, as `nitpick.toml:209` says.
- **Checks.** `checks.LIVE` has 13 entries, with 5 more driven outside step 5 = 19 live, and `PENDING` has 3 (`checks.py:3108-3152`; TESTING.md:105-109).
- **Ban list.** `PURITY_BAN` has 43 names in 7 classes (`checks.py:1314-1335`), as CLAUDE.md:59-61 and TM-252 say.
- **Decisions and open questions.** `DECISIONS.md` has 188 `### TM-` headings, as ROADMAP.md:40 says. OPEN_QUESTIONS has exactly 8 open: its own rows N1, N2, N3, N34, X1, B1, X4 and X8.

**The system-zone section (0.3.2)**
- The record's totals: 28 + 237 + 28 = 293; 25 red = 22 + 3; 20 + 6 + 2 = 28.
- Harness plants: 8 + 3 + 5 + 4 + 1 = 21 new emission, ban-list and generic plants, 95 → 116 (`selfcheck.py:1585-1755`). Unit arithmetic is 134 + 9 = 143, and library + repro + suite is 99 → 108.
- `system_zone_etc.npk`: exits 30..59 are the "thirty machines"; the 3 belts are 47, 48 and 58; the header lists 7 look-alike env names.
- Seven new units: `etc`, `tz`, `tz_colon`, `tz_colon_bare`, `tz_path`, `tz_empty`, `tz_raw`. `tz_raw` makes the two execve environments HOST.md:242-247 describes.
- `host_clocks.npk`: 10 of 14 mutants red, 4 unseen, matching H-3's list.

**Code against HOST.md and the cycle checklists**
- HOST.md H-1: five public functions, and the private helpers and numbers (6 numbers, 5 helpers) as `host.npk:19-30` counts them.
- Syscall numbers (228, 229, 89), clock ids (0, 1, 7), `O_NONBLOCK` 2048 and `O_CLOEXEC` 524288 agree with the code and the compiler prelude (`prelude.npk:1187,1191`).
- H-13 steps, H-14, H-15 and H-16 match `host.npk:217-323`. The descriptor is an `OwnedFd`, and the `n >= NTIME_PATH_MAX` refusal and the `zoneinfo/` component-start rule are present.
- Arm bills: `host` 11, umbrella 13, taken from SAFETY.md:87-93 and the tags. Arm bills are held by the harness's own `check_denominators` tags, so I did not re-derive them.
- `span.npk` against SPAN_MODEL.md §5, N-2 and the TIME_MODEL M-4 block. Duration limits of ±106 751 days, ±153 722 867 minutes, ±2 562 047 hours and ±15 250 weeks recompute correctly.
- `ValueFault` has 15 variants, so the "sixteenth" in CALENDAR.md:112-116 holds.
- `check_layering`'s host import set matches B-17 (`checks.py:204,247-265`). `check_purity` reads 9 of 10 `src/` files.
- 0.3 README items 1, 2, 4, 6, 7, 8 and 11 are ticked correctly (items 2 and 8 hold by the harness's own checks).
- Cross-references: the 0.3 `_tools/` links and `done/0.2/` links resolve, and the `#wild_slice` counts (9 in code, 14 lines) match the adoption note.
- Compiler decisions: D-061, D-140, D-148, D-176, D-210, D-221, D-248, D-264, D-304, D-314, D-328 exist, with the titles the library cites. D-313 (sealed, cited at `cal.npk:188`) sits on a line the search returned only as an omitted long match, so its title is not read. `npkrt.ll` carries the monotonic-clock block at line 3502.

## NOT CHECKED

- Anything needing a run. That covers the 143 green units, the plant counts as printed, the 293 mutants as rerun, IR byte sizes, CI run ids and `harness/README.md`'s "90/108 functions … 17 runtime symbols".
- `probe22` and every kernel claim: the 4 095-byte link ceiling, the apparmor lift, and `execve` of `/proc/self/exe`.
- The compiler at pin 5fbaf4a. Only decision titles and the runtime clock block were read. The checkout is at `7e91730`, so `D-341` (buffer indexing) post-dates the pin and was not applied.
- Future-cycle text in ZONE_MODEL, FORMAT_MODEL, COMPAT, VERIFICATION and the cycle 0.4–0.8 READMEs; the archived `done/` cycles; the research digests and `CURRENCY.md` rows; the 100+ lines of `0.3.0.md` and `0.3.1.md` records. I took the 0.3.2 record's tables by arithmetic only.
- SAFETY.md's S-4 generated table beyond the rows read, and the `tests/probe/defect/` READMEs.
- The 0.3.2 record's block hashes and CI log excerpts.