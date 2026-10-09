<!-- Filed 2026-10-09 by nitpick-libs_16. Made by the API-credits runner (.internal/credits/run.sh, job docs-vs-code-nitpick-fuzz-2026-10-09): headless claude -p on claude-sonnet-5-5, read-only tools, 79 turns, $2.58 of the plan's monthly API credits. Spot-checked by the seat before filing: FZ-1 (KNOWN_DEFECTS.md:218-219 says the M11 DEFs are fixed in 1.6.1e, and the compiler's OPEN_DECISIONS.md:2849 has DEF-154 OPEN), FZ-3 (PROGRESS.md:44 ticks M11, :972 says "M11 stays unticked", :1009 "M11 is done") and FZ-4 (PROGRESS.md:996 "four lower-priority compiler rows"). No edit to the report. -->

# nitpick-fuzz, documents against code at d44dfe3 — an audit

**Verdict.** The arithmetic holds. Every denominator I could count by reading agrees across `m11/CLAIMS.md`, `m11/RESULTS.md`, `REPORT.md` §12 and `PROGRESS.md`. The corpus, the ROWS files, the script references and the cross-references also match. What drifts is status and classification. `KNOWN_DEFECTS.md` says DEF-154 is fixed, and the compiler records it OPEN. F-044 files the frac print as "compiler right", and the compiler fixed it as DEF-231. `PROGRESS.md` contradicts itself on whether M11 is done. Three counts are wrong in prose: F-039's rows, the baseline-identical disagreements, and F-030's title. I found no program header whose claim contradicts a spec as it now stands. The disagreeing headers follow their reference's text on purpose; I checked only a sample against the specs, not the whole corpus. Nothing here is a defect in code.

## FINDINGS

**FZ-1 — a document wrong: `KNOWN_DEFECTS.md` says every M11 finding is fixed, and DEF-154 is OPEN.**
- `KNOWN_DEFECTS.md:218-219`: "**fixed in the compiler's subcycle 1.6.1e**, planned after 1.6.1d step 3" for DEF-144 … DEF-154. The list names DEF-154 at line 233.
- `OPEN_DECISIONS.md:2849`: "DEF-154 — OPEN (F-028, ninety-four rows…)". DEF-153 (line 2836) is "FIXED … for its rows", at landings 83 and 90 and 1.6.1e step 3. DEF-144 … DEF-152 are FIXED.
- `F-030/README.md:38` already says "DEF-154, open", so the repo disagrees with itself.
- Fix: say DEF-144 … DEF-153 are fixed and DEF-154 is open. Drop "planned after 1.6.1d step 3".

**FZ-2 — a document wrong: F-044 and `ty1657` file the frac print as a documentation row, and the compiler fixed it as a defect.**
- `F-044/README.md:124-131`: the compiler "renders the stated format literally… Under the reference's letter it is not [wrong]".
- `m11/RESULTS.md:309` classes `ty1657` as F-044, a documentation row.
- `OPEN_DECISIONS.md:3834`: "DEF-231 — FIXED 2026-10-08 (landing 97… D-347)", the print "-2 5/8" for −(1 3/8). `OPEN_QUESTIONS.md:414-418` (O-N36) calls it "silent wrong answer, THE AUTHOR'S RULING". `TYPE_REFERENCE.md:1837` keeps the example, because "-2 5/8" is −2.625 under D-347.
- Consequence: the `wrong:` line of `m11/programs/ty1657.npk:5` ("canonical parts rendered ("-3 3/8")") describes the pre-D-347 compiler. By reading, at the pin the program computes −(2 5/8) and expects "-2 5/8", so it should agree.
- Fix: reclassify as a compiler row (DEF-231, FIXED at landing 97). Move it out of the documentation count (33 → 32, matching DEF-239's "32 TYPE"). Note that it now agrees.

**FZ-3 — a document wrong: `PROGRESS.md` calls M11 both done and unticked.**
- `PROGRESS.md:44` ticks "[x] **M11**", and line 1009 says "M11 is done".
- `PROGRESS.md:972`: "M11 stays unticked." Lines 64 and 969 say "Resume from 'M11 — the state at the stop'" and "(read this first to resume)".
- Fix: drop the "unticked" and "resume" wording.

**FZ-4 — a document wrong: `PROGRESS.md` gives F-039 four rows, and it has five.**
- `PROGRESS.md:996`: "F-039: four lower-priority compiler rows".
- `PROGRESS.md:1354` and `:2297` say 5. `F-039/README.md:1` says "five". ROWS.md has 5 rows. `REPORT.md:1111` counts 5.
- Fix: change line 996 to five.

**FZ-5 — a document wrong: `REPORT.md` says one disagreement differs at the baseline, and three do.**
- `REPORT.md:1118`: "Every disagreement gives the same result at the baseline (one, `cc0042`, with other codes)".
- `m11/RESULTS.md:110` (`cc0042`), `:222` (`tr0404`: baseline "npkc 0 , 0/0") and `:224` (`tr0435`: baseline "npkc 0 , 0/0") all differ. `REPORT.md:1140` and the F-043 row at `:1178` admit "two compiled".
- Fix: say "three: `cc0042`, `tr0404`, `tr0435`".

**FZ-6 — wording: F-030's title says nine documentation sentences, and it has eight.**
- `F-030/README.md:1`: "nine sentences the compiler contradicts… (documentation findings)".
- `F-030/README.md:4-5`: "Eight of the nine are documentation rows. The ninth is DEF-148". ROWS.md has 8 rows, and `REPORT.md:1166` says "eight".
- Fix: retitle as "eight".

**FZ-7 — wording and classification: the backward-pipe rows are filed as compiler departures, and the compiler says they are not defects.**
- `F-039/README.md:15` (b) and `F-046/README.md:26` (c) file `<|` taking its function on the right as a "compiler departure, lower priority". `REPORT.md:1111` counts them in the compiler rows.
- `OPEN_DECISIONS.md:3881`: "F-039 (b) is not a defect: `<|` takes its function on the RIGHT, as `|>` does, and corrects F-031's pipe row (DEF-239)".
- F-031 (`F-031/README.md:22`, ROWS.md:16) still says the compiler refuses `func() <| val` because the function side is a call. Only F-039:22 corrects that, and F-031 carries no pointer to it.
- Fix: move F-039 b and F-046 c to the documentation class. Add the correction note to F-031.

**FZ-8 — a document stale: `KNOWN_DEFECTS.md` and the findings carry no registry status for F-029 … F-048, so they cannot dedup the next run against the registry.**
- `KNOWN_DEFECTS.md` stops at DEF-154 (F-028). `F-033:91`, `F-034:56` and `F-030:41` say "the registry at `93bcb66` has no entry". The compiler now registers all of them.
- FIXED: F-037 = DEF-227 (landing 94); F-041 = DEF-229 (landing 96); F-047 = DEF-230 (landings 98 and 103); the frac print `ty1657` = DEF-231 (landing 97).
- OPEN: F-048 = DEF-232; F-038 = DEF-233; F-034 = DEF-234; F-029 and F-036 a = DEF-235; F-039 and F-042 = DEF-236; F-045 = DEF-237; F-046 = DEF-238; the documentation rows = DEF-239.
- Fix: add a section with these rows, dated.

**FZ-9 — wording: the count of known defects at the baseline is inconsistent.**
- `README.md:9-11`: "found five places… a move out of `fixed` storage, a write through a lent parameter, a generic identity function, an imported table…". It names four. `PLAN.md:16`: "The five known defects of `KNOWN_DEFECTS.md`".
- `known/` holds four defect families (DEF-99, 102, 104, 105: 4+5+3+7 = 19 rows). DEF-106 was "added on 2026-09-26, after M4" (`KNOWN_DEFECTS.md:93`). DEF-103 appears only under "Other known defects".
- Fix: name the fifth (DEF-103, by inference), or say four.

**FZ-10 — wording: stale docstring and stale line references.**
- `gen/m11_rows.py:2` says "the two findings made of claims (F-027, F-028)". The script's `FINDINGS` dict (lines 19-33) maps 15 findings.
- The reference line numbers in findings and results are HUNT2's. The reference files have moved: the `MEMORY_REFERENCE.md` `wildx_alloc` example is now at line 168, where CLAIMS says 126. Lines 177, 215 and 228 are the same shift. A reader following `MEMORY:126` today lands on the wrong text.
- `F-030:14-17` cites MEMORY:174 and :184, where CLAIMS has `me0173` and `me0183`. These are one-off anchor differences.
- Fix: say the line numbers are at `9126350`, and fix the docstring.

## KNOWN

- **Landing 103 and `string_bytes`.** 1 013 corpus files bind `string_bytes` into a plain `uint8[]` and are refused NITPICK-TYPE-007 at the pin. I did not count them; the corpus has not adopted D-351 (`DECISIONS.md:22827`).
- **`ty1873`.** `m11/programs/ty1873.npk:3-4` claims "A fixed parameter may not be reassigned: ASSIGN-002" and expects `refuse:NITPICK-ASSIGN-002`. The compiler's DEF-238 b (F-046) is OPEN, and landing 102 makes it refused.
- **`mc0388`.** `m11/programs/mc0388.npk:3-5` expects `run:0` for a declaration name. Landing 106 will move it to refuse:NITPICK-MACRO-011.
- **Registry rows.** O-N30 (F-003 … F-010), O-N31 (F-011 … F-017), O-N33 (F-018 … F-028, "PARTLY DISCHARGED… STILL OPEN: F-028, DEF-154"), O-N35 (F-029 … F-032) and O-N36 (F-033 … F-048) all exist in `OPEN_QUESTIONS.md`. They match FZ-1 and FZ-8.

## CHECKED AND HELD

- **M11 denominators.** All 14 rows of the table in `m11/RESULTS.md:11-26` give claims = examples + rows + rules and claims = testable + untestable. Tested = agree + disagree. The totals are 3 385, 160, 856, 2 369, 513, 2 872, 2 587 and 285. The untestable reasons sum to 513 (135+117+77+75+69+29+8+3), and the disagreement-by-kind figures sum to 285.
- **Other copies of the table.** `m11/CLAIMS.md:13-30` and `REPORT.md:1051-1067` carry the same table. `m11/EXPECT.tsv` has 2 873 lines (header plus 2 872).
- **Disagreement classes.** The classes in `m11/RESULTS.md:46-59` and `REPORT.md:1102-1116` both sum to 285. The compiler-lower rows are 16+5+4+5+1+3 = 34, the documentation rows 94+8+5+6+7+6+18+13+33 = 190, the known rows 19, and the not-a-finding rows 2 and 17.
- **ROWS files.** The F-0xx ROWS.md row counts equal the totals: F-027 16, F-028 94, F-030 8, F-031 5, F-032 6, F-033 7, F-034 5, F-035 6, F-036 4, F-039 5, F-040 18, F-042 1, F-043 13, F-044 33, F-046 3. That is 224 in all.
- **Findings and sessions.** F-001 … F-048 all have directories. Sessions 7 and 8 match `OPEN_QUESTIONS.md`: 1 262 claims and 144 disagreeing, and 411 and 28.
- **M10.** `m10/` holds 223 programs (226 files minus CHECKLIST, RESULTS and EXPECT), and `m10/EXPECT.tsv` has 224 lines. The per-area table sums to 212/11 at HUNT2 and 210/13 at the baseline. The "of which" rows sum to 11 and 13.
- **M2 to M9.**
  - M2: generated and skipped per T and per P sum to 956 and 1 284.
  - M3: 612+230+56+25+22+5+2+4 = 956, and the 114 baseline anomalies decompose as 32+24+24+8+6+20.
  - M5: 604+270+48+22+3+3+2+4 = 956; 82 anomalies = 62 known + 20 new.
  - M8: 148 moved = 136 + 12; the 404 refusal codes are 394 cells plus 10 two-code cells.
  - M9: 7 571 cells, 28 519 skipped, 36 090 in all; REFUSE 3 210 + SAFE 4 361; the five sections sum to 7 571; the baseline and HUNT2 class tables sum to 7 571; the HUNT2 families sum to 197.
- **Recall suite.** `known/` holds 25 programs plus `rows.npk`. The suite has 19 rows at M1 and 25 after M9, which matches `PROGRESS.md`.
- **DEF status in `KNOWN_DEFECTS.md`.** DEF-99 (3f), 102/103/104 (3g), 105 (3h), 106 (4b), 107 (1.6.1 step 0), 108 (5c) and 116 (0c) match the `OPEN_DECISIONS.md` landings. DEF-118 … DEF-125, DEF-127 … DEF-135 (by step) and DEF-144 … DEF-153 (by number and F-id) match the "fixed in 1.6.1d/e" claims. DEF-96 `main` TYPE-083 and the `cstring[]:_~argv` form hold (`AST_REFERENCE.md:89-92`).
- **Scripts.** Every `gen/*.py` named in a document exists. `gen/m11_run.py` defaults to `--jobs 4` as stated, and `gen/m11_report.py` computes the 10 419-of-10 419 coverage rather than hard-coding it. All referenced `results/*/m11-disagree.jsonl` files exist.

## NOT CHECKED

- Whether any program's header contradicts a spec was sampled, not enumerated. I did not diff the 2 872 expectations against the specs.
- Anything needing a run: whether `ty1657` now agrees at the pin (by reading only); the 1 013 TYPE-007 count; every verdict, exit code, cell count and `heap:` figure in the results files.
- The `cells/` regeneration and the 7 930 functions of `check_leaves.py`.
- The count of programs in `m11/programs/`. The glob showed 2 403 `.npk` files against 2 872 tested claims; I take `sh:` claims to use scripts, but have not verified it.
- DEF-95, DEF-97 and DEF-98 fix shas (`dfbaf1a`, `f758995`, `395308f`) were not checked against any git history.
- The `.work/` clones and compiler commits `c3bdae2`, `6fb85d3`, `9126350`, `9f6f370`, `1b4f0c6` and `93bcb66` were not readable, so every "at HUNT2" measurement rests on the committed records.