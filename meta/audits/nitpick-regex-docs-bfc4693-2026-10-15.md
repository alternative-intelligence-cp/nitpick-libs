<!-- Filed 2026-10-15 by nitpick-libs_19. Made by the API-credits runner (.internal/credits/run.sh, job docs-vs-code-nitpick-regex-0.2-2026-10-15): headless claude -p on claude-sonnet-5-5, read-only tools, 119 turns, $2.55 of the plan's monthly API credits. Spot-checked by the seat before filing: RA-9 (meta/roadmap/0.2/README.md:38 reads "No open questions"; src/hir/repr.npk:102 derives Copy only; nothing under src/ is named hir_eq or calls .eq() and RA-12 (nitpick.toml:127–134 says "SIX of the eight files"; src/ holds 22 .npk files). Note: the verdict says four new findings, and the report lists five, RA-9 … RA-13. One edit for check_refs only: nitpick-regex's own open row N10 is written without its `O-` prefix. It feeds 0.2.6's close by its RA ids; RA-9 asks the close to record a decision. -->

# nitpick-regex, documents against code at bfc4693 — an audit before the cycle 0.2 close, 2026-10-15

**Verdict.** By reading, I found no defect in code and no decision the code contradicts. Every count, name, signature and test claim I could trace held. That covers H-9, H-13, H-15, H-16, H-17 and H-18, RX-232 … RX-240, the unit totals, the pending list and the self-check's case list. All eight earlier findings hold fixed. The new findings are four documents, and all four are things the 0.2.6 close should settle. One is a question that README says is closed but that is still open: RA-9. The other three are stale wording: RA-10, RA-11 and RA-12. Nothing here needs a run, but I ran nothing, so every "green" count below is the records' word.

## Earlier findings (75dd51e, RA-1 … RA-8)

- **RA-1 fixed.** `tests/README.md:6` says `compile`, `positive`. Lines 8 and 10 say "*not declared yet*". The dated note is at :13–16.
- **RA-2 fixed.** `harness/treecheck.py:21` carries the dated note on the sentence. `ALL` at :1468 lists ten checks.
- **RA-3 fixed.** `meta/OPEN_QUESTIONS.md:717` is the dated re-read at `7e91730`. I did not re-verify its compiler claim.
- **RA-4 fixed.** `nitpick.toml:155–156` now says "since cycle 0.2.0 one the HIR's (`hir_nodes_read`; the documents audit's RA-4)". `tests/rejection/` holds 25 files, which is 2+19+3+1.
- **RA-5 fixed.** `README.md:11` says "its first six parts … are done".
- **RA-6 fixed.** `CLAUDE.md:175` and `src/api/api.npk:30` now say "a closed list of the ways … to be malformed", with no number.
- **RA-7 fixed.**
  - `HIR.md:81` says `check_hir_kinds_total` is 0.2.6's.
  - `HIR.md:148` and `:193` record that H-8 is built.
  - `src/core/limits.npk:73` carries its dated note.
- **RA-8 fixed.** Both transcripts open with a redirect note (`tests/probe/TRANSCRIPT.txt:1–2`, `tests/conformance/TRANSCRIPT.txt:1–2`). The old `meta/roadmap/0.0/` paths in the bodies stay, as W-28 allows.

## New findings

**RA-9 — document wrong (a settled-looking cycle carries an unmade decision) — Hir comparison.**
- Doc, README: `meta/roadmap/0.2/README.md:38`, "RX-015, RX-031. Settled. **No open questions.**"
- Doc, decision: `meta/DECISIONS.md:1374–1376`, "Whether `Hir` comparison takes the derive is a cycle 0.2 decision with that cost on the table". `meta/OPEN_QUESTIONS.md:242` repeats it for N10's residue.
- Doc, spec: `meta/specs/HIR.md:54–57` calls `HirNode` "copyable, storable in an array, and **comparable**".
- Code: `src/hir/repr.npk:102` and `:114` give `HirNode` and `GroupInfo` `#[derive(Copy)]` only. `HirKind` at :89 does the same.
- Code: no `.eq()` and no `hir_eq` exists under `src/`.
- Code: the tests compare dump text, for example `hir_props.npk:150`.
- No RX- number from 0.2.0 to 0.2.4 takes the decision.
- Fix: at 0.2.6, record that a HIR is compared by its dump text (H-15), with no derive and no error channel. Then date N10's residue, H-2's "comparable", and the cycle README's "No open questions".

**RA-10 — wording — `check_hir_kinds_total`'s owner.**
- Doc: `meta/specs/TESTING.md:235`, "no — **cycle 0.2**".
- Doc: `meta/roadmap/0.2/README.md:70` and `:129`, and `HIR.md:81`, put it at 0.2.6. Its compiler and oracle halves are pending until 0.6 and 0.5.
- Fix: write "cycle 0.2.6" in that cell when the check goes live.

**RA-11 — wording — `CLAUDE.md` still reads as if nothing is pending and `HirNode` is unmeasured.**
- `CLAUDE.md:124`, "**Nothing is PENDING any more**", is followed by dated notes at :128–133 that put three units pending.
- `CLAUDE.md:366–373` still says `HirNode` "does not exist in `src/` until cycle 0.2" and that its size is "**unmeasured**". The dated note after it gives 40.
- The notes make both readable, but this is the document every session reads first.
- Fix: rewrite both passages at the close instead of annotating them again.

**RA-12 — wording — dated "now" and a consumer claim.**
- `nitpick.toml:127–134` still says "SIX of the eight files" and, in the 0.2.2 note, "`src/` holds 21 files now … reach 19 of them". `src/` holds 22 files and the suites reach 20. The 0.2.2 note's "now" is dated, but it now misleads.
- `meta/specs/README.md:24` lists HIR.md as "desugaring, normalisation, literal extraction". It omits the computed properties (H-9, H-17, H-18).
- `HIR.md:214` says `CAN_MATCH_EMPTY` is used by "`SYNTAX.md` Y-21's iterator rule". Y-21 (`SYNTAX.md:647`) and A-14 (`meta/specs/API.md:240`) advance after any empty match and read no flag.
- Fix: refresh these three at the close. The first needs the count or a pointer to the runner's line. The third should say the one-pass engine's eligibility is the consumer.

**RA-13 — wording (small, 0.2.5's) — two limits stated outside §5.**
- `src/core/limits.npk:113` and `:117` hold `NREGEX_LITERAL_LIMIT` and `NREGEX_LITERAL_BYTES`, and `HIR.md` §5 names them.
- `meta/specs/SAFETY.md:386–394` is the table of nine rows and has neither.
- Fix: add the two rows when 0.2.5 enforces them.

## Known and expected, confirmed in one line each

- **N1 holds.** `0.2.3.md:1153` says "24 lines of the unit in all", and :1491 records the re-cut as 18.
- **N2 holds.** `0.2.3.md:1493`: the prelude check was over top-level `pub` lines.
- **Block 5, 17 of 53 lines.** This is documented as 0.2.3's finding at `0.2.4.md:887`. I did not open 0.2.3's own record for it.
- **0.2.4 carry-overs hold.**
  - `0.2.4.md:1197–1198` and :1678 state the compiler-tree reading.
  - The cycle README's 0.2.1 rows (lines 12, 64, 84) are undated.
  - `0.2.4.md:1582` says apply.py reads step 1 as STOP.
  - `kind_bits` at `dump.npk:152–156` has its three `pass` lines. I did not check the mutant table's single-row claim.
- **N3 holds.** `0.2.4.md:1613`: rx120's `950bb1d` leg prints SKIPPED.
- **CI digests** differ from PIN.md's rows as ci.yml documents; I did not re-read them.
- **Author-accepted items.** I did not treat RX-235's two consequences or the six 0.2.4 items as findings.

## Checked and held

- **Counts.**
  - `tests/unit/` holds 97 files: 37 in `core`, 25 in `syntax` and 35 in `hir`. The `hir` split is 9, 6, 4, 8 and 8 for 0.2.0, 0.2.1, 0.2.2, 0.2.3 and 0.2.4, as CLAUDE.md says.
  - Each total step from 283 to 334 matches the file counts: sweep, plus units run, plus new `src` files.
  - `0.2.4.md:1400`: 1+25+8+181+25+97 = 337, less three pending, is 334.
  - 33 probes split 25 / 8; 25 rejection fixtures; `src/` holds 22 files, which `0.2.4.md:1611` echoes as "22 files".
  - `harness/selfcheck.py` has 35 cases (1–34 and 3a): 31 live, with 5, 6, 7 and 14 pending. Cases 11, 12, 13 and 34 are the marker's reds.
  - `ALL` holds ten tree checks.
  - `harness/baseline/PENDING.txt` lists exactly the three pending units, and each marker is in its file.
  - Decisions end at RX-240.
- **Code against specs.**
  - H-4 and H-4a: nine kinds, with operands matching `repr.npk:89–110`.
  - H-8 and H-16: `hir_build` and `hir_build_refusal` have the signatures stated, and the product is refused at the `{` (`build.npk:89–94`, `:321–325`, `:363–372`).
  - H-13 and RX-235 … RX-236: `hir_normalise` splices, keeps an `Empty` alternative, drops an `Empty` piece, sorts and merges classes, and checks "fresh" by three counts (`normal.npk:253–268`).
  - H-17 and H-18: each cell of the table is in `list_facts` and `facts_of`.
  - H-18: `hir_push` and `hir_set` drop the bits, `hir_set` and `hir_set_root` stop on a computed tree, and `hir_props` computes or reads (`repr.npk:151–191`, `:405–411`).
  - The dump shows none of the five bits, and a stray bit still stops it (`dump.npk:152–156`, `:208`).
  - `hir.npk` re-exports every name the specs name, including `HIR_PROPS` and `HIR_COMPUTED`.
- **Tests behind the "every" and "fifty" claims.**
  - `hir_props_reference.npk` has exactly 50 rows. Its three byte-mode and codepoint twin pairs are rows 1/4, 29/30 and 32/33.
  - `hir_props.npk`: cases 1–14, 15–19 and 20–24 are as described, and the exits of the six stopping units are 94, 94, 94, 94, 94 and 108.
  - The gate's floors are 3000, 1500, 500, 200 and 100, with `repwraps` counted at its own draw (`hir_normalise_gate.npk:42–46`, `:321`, `:626–627`).
  - `hir_build_product.npk` cases 1, 2, 3, 10 … 13, 40, 41 and 70 are as the record gives them.
  - The `hir_build_product_fuzz.npk` floors and the 64 MiB cap markers match.
  - The `parse_fuzz.npk` totals match its constants (40 000 × 3 alphabets), and it has three alphabets.
  - `0.2.4_tools/mutants.tsv` has 72 rows.
- **Rules the code keeps.**
  - 70 `while` loops in `src/`, and 70 `decreases` clauses.
  - No `/` or `%` in `src/hir`.
  - One `error:` in `src/`, at `api.npk:32`.
  - `src/` has no `unbounded`.
  - Layering holds for `hir`: its imports are `core`, `unicode` and `syntax`.
- **Pins.**
  - `SAFETY.md:413`: the 23-byte pattern and byte 10 hold.
  - `meta/specs/SYNTAX.md:774–781`: three rows are left in Y-25's table.

## Not checked

- **Anything that needs a run.** The 334 figure, the mutant exits, the "both legs" claims, CI run numbers and rx120's legs. I took them from the records.
- **Compiler claims.** I did not re-read the compiler at e50eaf4, so RA-3's re-verification and the keyword and reserved-word claims at `7e91730` rest on the records.
- **0.2.5.** Excluded as instructed.
- **Documents read only for named items.**
  - Most of COMPILE.md, ENGINES.md, API.md, UNICODE.md, PERFORMANCE.md, COMPAT.md and GLOSSARY.md.
  - The cycle READMEs from 0.4 on, and most of DECISIONS.md before RX-222.
  - 0.2.3.md's and 0.2.4.md's step-by-step bodies; I read the sweeps, acceptance, mutant and CI sections, not every pasted block.
- **Mutant claims.** I did not check the fifty-four of seventy-two split for H-17, or the "forty-seven facets" count.
- **Harness internals.** The `check_error_kinds_tested` and `check_layering` logic beyond their tables.