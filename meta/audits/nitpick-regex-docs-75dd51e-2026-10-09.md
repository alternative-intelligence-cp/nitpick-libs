<!-- Filed 2026-10-09 by nitpick-libs_15. Made by the API-credits runner (.internal/credits/run.sh, job docs-vs-code-nitpick-regex-2026-10-09): headless claude -p on claude-sonnet-5-5, read-only tools, 145 turns, $6.74 of the plan's monthly API credits. Spot-checked by the seat before filing: RA-4 (25 .npk files in tests/rejection/ on main) and RA-6 (CLAUDE.md:155, "thirty ways to be malformed", read through `git show main:`). The auditor read a moving working tree: regex's 0.2.1a planner was rehearsing on the throwaway branch p021a-rehearse-2 in the real checkout, as this repository's planners do, and no finding depends on a slice type. One edit for check_refs only: RA-3's title names regex's own row G1 without its `O-` prefix, because the workbench's checker reads a bare id as this registry's. nitpick-regex's next dispatch carries this audit by its RA ids. -->

# nitpick-regex, documents against code at 75dd51e — an audit

**Verdict.** I found no defect in code and no decision the code contradicts. Every count, enumeration and signature I could check by reading held, down to the case numbers in the 0.2.0 and 0.2.1 execution records. Eight places where a document says something the tree does not bear out remain. Two are plainly wrong: `tests/README.md` names a stage the manifest struck, and a `treecheck.py` docstring promises output the check does not print. One is a stale compiler claim in `OPEN_QUESTIONS.md`, whose core conclusion still holds. The other five are stale counts, status text, or present-tense rules for work owned by a later subcycle. Nothing here needs a run to settle.

The tree moved while I read: 0.2.1a's `fixed uint8[]` landed, e.g. in `src/syntax/parse.npk` and `tests/unit/hir_build_classes.npk`, and `.git/logs/HEAD` shows branch `p021a-rehearse-2`. None of the findings depends on a slice type.

## FINDINGS

**RA-1 — document wrong — `tests/README.md` names a stage that is struck for this library.**
- Document: `tests/README.md:7`, `` | `conformance/` | `accept` | ``.
- Tree: `nitpick.toml:74-78` declares the suite `stage = "compile"`, `kind = "positive"`. `meta/specs/BUILD.md:291-292` (B-4a, RX-117) says "the `accept` stage is not available to this library". `harness/README.md:32` calls declaring `accept` a manifest error.
- The same table's rows `oracle/ | program` and `fixtures/ | fixture` name stages or suites the manifest does not declare. Both are future (0.5 and later), but the table does not say so.
- Fix: write `compile`/`positive` for conformance, and mark the oracle and fixtures rows as not yet declared.

**RA-2 — document wrong — a `treecheck.py` docstring says `check_layering` prints a note it does not print.**
- Document: `harness/treecheck.py:20-22`, "`check_layering` says in as many words that six of this library's eight `src/` files are reached by no suite at all".
- Tree: `check_layering` at `treecheck.py:151-214` adds one note, the oracle note at `:210-212`, and nothing about reach. `src/` now holds 21 `.npk` files (20 layer files plus `lib.npk`).
- Fix: delete the sentence, or make it a note the check prints.

**RA-3 — document wrong (compiler claim, partly stale) — `OPEN_QUESTIONS.md`'s own row G1 (in its `O-` series) says the compiler's folder has no member-access arm.**
- Document: `meta/OPEN_QUESTIONS.md:711-713`, "There is no arm for an index expression, a member access, an array literal or a struct literal." It was last re-verified at `3d15ac9` (`:763-769`), two pins before `5fbaf4a`.
- Compiler: `nitpick/src/frontend/type_resolve.npk:1622-1624` has `ExprMemberAccessExpr` calling `fold_variant`, which D-338 added (`MACRO_REFERENCE.md:649-655`).
- Still true: there is no index arm in `fold_expr` (`:1495-1661`). `fold_string_builtin` still folds exactly the four names it did (`:2768-2795`). So "comptime cannot index a string" (`CLAUDE.md:230`) holds.
- The compiler source I read is its working tree, not a pin.
- Fix: amend the arm list with a dated note, and re-date the re-verification.
- Related and already filed as E2-9 in `meta/audits/ecosystem-early-2026-10-09.md`: O-Y2 (`OPEN_QUESTIONS.md:258`) reverses RX-201. I did not re-report it.

**RA-4 — wording (stale count) — `nitpick.toml` counts 24 rejection fixtures; the directory holds 25.**
- Manifest: `nitpick.toml:142-148` lists 2 `failsafe_*`, "the other nineteen", and "three" syntax fixtures, which sums to 24.
- Tree: `tests/rejection/` holds 25, the extra being `hir_nodes_read.npk`, which imports `src/hir/hir.npk` (`:17`). `tests/rejection/README.md:185-189` and `CLAUDE.md:70-72` say 25 correctly.
- Fix: add "and one the HIR's, since 0.2.0" to the comment.

**RA-5 — document wrong (stale headline) — `README.md` status line contradicts its own paragraph.**
- Document: `README.md:11` says cycle 0.2 is open "and its first part, the arena, is done".
- Same file: `README.md:35-38` says 0.2.1 builds the HIR. `meta/roadmap/0.2/README.md:6`, `ROADMAP.md:57` and `CLAUDE.md:12-15` all say 0.2.0 and 0.2.1 are done.
- Fix: "its first two parts, the arena and the desugaring, are done".

**RA-6 — wording — "thirty ways" for the error kinds.**
- Documents: `CLAUDE.md:155` and `src/api/api.npk:30` say "thirty ways to be malformed".
- Tree: `PatternErrorKind` has 38 variants. I counted 6+5+5+4+7+7+4 at `src/syntax/pattern_error.npk:49-101`. `SAFETY.md:209-223` keeps "thirty" with dated notes saying it is a round number; these two sites have no such note.
- Fix: say "thirty-eight" or drop the number.

**RA-7 — wording (rule reads as live; owned by a later subcycle) — three present-tense statements about work not yet built.**
- `HIR.md:139-141` (H-8) says the repetition product "is checked as the HIR is built" and that `((a{1000}){1000}){1000}` "is refused at the third `{1000}`". `src/core/limits.npk:67` repeats it: "It is checked AS THE HIR IS BUILT".
- `HIR.md:77-78` (H-4) says "A tree check asserts every kind is produced by the parser, consumed by the compiler, and handled by the oracle".
- Tree: `NREGEX_REPEAT_PRODUCT` appears in `src/` only at its declaration and re-export (`limits.npk:73`, `core.npk:33`), so `hir_build` has no product check. `treecheck.ALL` (`:1463-1466`) has ten checks and no `check_hir_kinds_total`. `TESTING.md:221` and `0.2/README.md:72-75,100` own both, for 0.2.2 and 0.2.6.
- Fix: a dated "not until 0.2.2" or "not until 0.2.6" note at each site.

**RA-8 — cosmetic (stale cross-reference in records) — transcripts cite paths from before the 0.0 archive.**
- `tests/probe/TRANSCRIPT.txt:31,58,81,105` and `tests/conformance/TRANSCRIPT.txt:429` cite `meta/roadmap/0.0/0.0.4b.md`, `0.0.4.md`, `0.0.3.md`, `0.0.0.md` and `0.0.2.md`.
- Those files now live at `meta/roadmap/done/0.0/`. `check_specs_current` reads only markdown, so it cannot see them.
- Records are not rewritten under W-28. A dated redirect line would do, as `tests/probe/README.md:139-145` already does for the `refused/` moves.

## CHECKED AND HELD

- **Counts in the top documents.**
  - Probes: 33, split 25 / 8 (`README.md`, `CLAUDE.md`, `tests/probe/README.md:27-30`), counted by glob and by `expect-exit` / `expect-error` markers (`tests/probe/refused/` has 8 `expect-error`). No probe imports `src/`.
  - Rejection fixtures: 25, with the 2+19+3+1 composition.
  - `src/core` unit programs: 37.
  - Tree checks: ten (`treecheck.py:1463`). `check_no_syscalls` is a build step (`:1473`).
  - Self-check cases: 35, 31 live and 4 pending (`selfcheck.py:1216-1348`). Cases 11, 12, 13 and 34 are the marker's reds.
  - Pending units: exactly the two lines in `PENDING.txt:47-48`, and `tests/unit/hir_build_classes.npk:2` and `hir_build_fold.npk:2` carry `pending-until: 0.3.4 exit 1`.
- **The 294 arithmetic in the 0.2.1 record.** Parse sweep: 160 files (21 `src`, 3 harness, 136 tests). Units: 77 files. Rejection: 25. `1+25+8+160+25+75 = 294`, with the two pending units run outside the count. By reading only; I did not run it.
- **`HIR.md` against `src/hir/`.**
  - H-4 and H-4a: the nine kinds in H-4's order, and the operand table, match `repr.npk:66-86`.
  - Flag and anchor constants match `repr.npk:43-61`.
  - Size: `HirNode` is 40 by field widths, and `hir_size.npk:1` expects exit 40.
  - Accessors: every RX-223 and RX-224 accessor exists with the stated signature.
  - H-15: spelling, the 18-digit bound, and the refusals match `dump.npk`. The `OutOfBounds` stops are there (`:200,204,211`), and so is the walk bound (`:189`).
  - H-16: the signature `hir_build(uint8[]:pat, Ast:t, Hir->:out) -> int64` and each AST-kind row match `build.npk:148-310`. That covers anchor mapping, surrogate splitting, `Flags` erasure, and the Concat and Alternate rules. The stops (`leaf`, `resolve_items`, `fold_ranges`) and group numbering are as described.
- **0.2 checklist case numbers** against the tests: `hir_build.npk` cases 1-9 / 10-14 / 15-19 / 20-23 / 24-27 / 30-49 / 50-58 / 60-69 (eight pairs) / 70-73 / 80-83; `hir_dump.npk` 26 texts, 33 refusals, shapes 30-36, six arena-built HIRs; `hir_unit` 50-58 and 69. Unit exits (94, 108, 40, 0 and so on) match the `expect-exit` markers.
- **Error budget and loops.**
  - One `error:` in `src/`, `api.ERegexPattern` (`api.npk:32`).
  - No `limit`, `requires` or `ensures` in `src/` except the `ListLen` fields in `core`.
  - Every `while` in `src/` carries `decreases`: 51 loops, 51 clauses.
  - No `/` or `%` in `src/`.
  - `.items[` and `.ptr[` appear only in `vec.npk` and `bytes.npk`.
  - `limits.npk` holds the nine `SAFETY.md` §5 rows, and the values agree.
  - The eleven-arm `failsafe` in the HIR units matches `SAFETY.md:251-253`.
- **Y-25 and §9.** The error-kinds table has four rows, and `PatternErrorKind` has 38 kinds. `AstKind` has 16 and `AstNode` is 56 by field widths (`ast.npk`), matching Y-26 and Y-27.
- **Harness.** The `rx120.sh` assertions (5 / 6 / `{npk_sys6}`), `SYMBOLS.txt` (5 symbols) and `EDGES.txt` (4 edges) agree. `RESIDUE.txt`'s `npk_string_equals` appears in `tests/unit/bytes_unit.npk` only. `ci.yml` pins the compiler by full sha and asserts the checkout, the LLVM version and the emission digest.
- **Compiler claims re-checked against `nitpick/meta/specs/DECISIONS.md` and `nitpick/src/prelude`.**
  - D-004, D-018, D-062, D-070, D-151, D-188, D-210, D-227, D-241, D-264, D-304, D-305, D-307, D-314, D-327, D-332 and D-351 say what the library cites them for.
  - D-185's "no static methods" is in its body (`:13851`).
  - The prelude `Reader` trait (`src/prelude/prelude.npk:1288`) and the `arena` keyword (`LEXICAL_REFERENCE.md:115`) exist.
  - TYPE-014, -017, -079, -080, -085, -086 and -087 are in the compiler's references.
- **Filed audits.** The RX-001…RX-080 intro, the dogfood-location contradiction and the O-N27/28 rows are already E2-10, E2-6 and E2-9 in `ecosystem-early-2026-10-09.md`. I did not repeat them.

## NOT CHECKED

- **Anything that needs a run.**
  - Unit totals (283, 285, 292, 294), CI run numbers, and the mutant exits (thirty-three, thirty-eight, forty-two).
  - "Both legs" claims, and the behaviour of `hir_build` on any input.
  - The 120 000-pattern fuzz total: I confirmed the constants (40 000 × 3 alphabets) and did not confirm there are three.
- **Compiler claims at a pin.** I read the compiler's working tree, not a pin, so I cannot say which of `5fbaf4a` or `7e91730` any compiler fact belongs to. I did not re-run the probe verdicts.
- **Whole documents not read closely.** Most of `COMPILE.md`, `ENGINES.md`, `API.md`, `UNICODE.md`, `PERFORMANCE.md`, `VERIFICATION.md`, `COMPAT.md` and `GLOSSARY.md`. These describe unbuilt layers, and I read them only for named items that exist in `src/`. Also not read: the cycle READMEs 0.4–1.0, the 0.0 and 0.1 archives, and most of `DECISIONS.md` before RX-218.
- **Specific items skipped.** The 61/81/86 loop counts in `CLAUDE.md:389` (dated, and the `decreases_read.txt` reading was not opened), and the `check_error_kinds_tested` logic beyond its table.
- **0.2.1a.** Excluded as instructed. Its changes landing mid-read are why my reads of `build.npk`, `dump.npk` and `repr.npk` predate the `fixed` change.