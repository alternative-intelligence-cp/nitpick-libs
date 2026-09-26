# Pre-close audit — `nitpick-time` cycle 0.1

**Filed by the orchestrator under W-22**, 2026-09-26. The auditor wrote nothing; this file is its final message, reproduced
below the line — extracted from its transcript by script, not retyped — **inside a fence, with three mechanical changes and no
other**: (1) the two absolute home-directory paths on its "Roots" line are written relative, because this workbench's leak scan
refuses them; (2) the message is fenced, because it quotes `nitpick-time`'s own question ids, which at workbench scope collide
with other repositories' (`meta/OPEN_QUESTIONS.md`, *"Library questions this board cites"*: quoted evidence belongs in a fence),
and its 6 inner fence lines are re-marked `~~~` so they do not close the outer one; (3) its 1 occurrences of an empty
array type followed by a parameter list are written with a space between the brackets and the parenthesis, because the reference
checker reads that pair as a link even inside a fence. **The close worker (0.1.5's second half) triages every finding** — W-22
requires each to be addressed or explicitly deferred with a reason, not selected from — and the auditor recommends that C1 to C4
be fixed rather than declined.

**Repository** `nitpick-time` at `3fac625` · **pin** `c970483` · **agent** `npk:auditor` on `opus` (`s2-ntime-0.1-audit`), ~32 min.

## What the orchestrator verified before filing

- The report's status and verdict: **ACCEPT**, 19 findings — 12 contradiction, 1 unverified claim, 1 dormant, 2 stale, 3 cosmetic.
- **C3, spot-checked:** `bytes_view`, a public function returning a `uint8[]` view of a `Bytes`, stands at
  `src/core/bytes.npk:366`, and `check_no_view_returns` appears nowhere under `harness/`.
- **C8, spot-checked:** `check_no_format_string` appears only as a `PENDING` entry (`harness/checks.py:1437`, live from 0.4),
  never defined as a check.
- The trees were left clean: `git status --porcelain` empty in `nitpick-time` and in this workbench.

---

```markdown
# Audit: nitpick-time, cycle 0.1 (the civil calendar), pre-close (W-22)

status: ACCEPT

- **Audited:** `nitpick-time` at `3fac625` (equal to `origin/main`). Scope was cycle 0.1's twelve subcycle files, plus the specs, decisions, harness, `src/` and `tests/`.
- **Pin:** `c970483`, with `sha256sum -c` OK for both `npkc` and `npkrt.o`. Control pin `c3bdae2`. Every compiler claim was read with `git show c970483:<path>`, never from `../nitpick/build/`.
- **Mechanical checks:** `check_refs` is clean (81 md files, leak scan 248 of 248). `check_record 0.1.5` is clean.
- **Nothing written:** no repository was written. Scratch programs were built only in the session scratchpad. No harness run was made; nothing below depends on one. `free -g` showed 141 GiB available.
- **Roots:** REPO=`nitpick-time/` (the workbench's checkout) and COMPILER=`../nitpick` (the compiler's checkout). Paths below are REPO-relative, because the workbench's leak scan refuses absolute home paths in a filed file.

**Summary: 19 findings.** 12 contradiction, 1 unverified claim, 1 dormant, 2 stale, 3 cosmetic.

- The calendar and its exhaustive gate hold at the pin, and the reader port is exact.
- The findings sit in what the documents claim the harness does, and in live rules the close's sweeps did not reach.
- C1 to C4 should be fixed rather than declined.

---

## Contradiction

### C1: Part E does not turn a lexer move red, and the one move between the kept pins passes it

**Location:**
- `CLAUDE.md:24-26`
- `harness/lexical.py:80-85`
- `harness/selfcheck.py:1492-1497`
- `meta/specs/TESTING.md:245-248` (V-1k) and `:512`
- `meta/DECISIONS.md:5540-5544` (TM-199)
- `harness/README.md:75-79`
- `meta/roadmap/0.1/0.1.5.md:6659-6661`, where cycle 0.2's adoption decides whether to re-read the lexer on E2's signal

**Claim:** "the pinned compiler, one program of every form a run can observe, so a re-pin that moves the lexer is a red run."

**Evidence:**
- E2's program (`_FORMS_TEXT`, `_FORMS_SIX`) observes 7 forms (`_FORMS_EXIT` 10-16).
- It has no block string, raw string, escaped quote, empty string or `&{}` interpolation. `lexical.py` mirrors all of these, and a run can observe each.
- I rebuilt E2 from the harness's own constants in scratch (`npkc`, then `llc -O0`, then `ld.lld`):

~~~
c970483 lexical_forms: run exit 0
c3bdae2 lexical_forms: run exit 0
c970483 blockform (string:s = """a""b""";): run exit 0
c3bdae2 blockform: npkc exit 1: NITPICK-LEX-005 blockform.npk:3:23: unterminated string literal
~~~

- The lexer moved between the kept pins on a form the reader mirrors: the block-string close, DEF-98, which `lexical.py:55-58` itself records. E2 is green at both pins.
- E1 cannot catch this either, because its expectations are fixed in Python.

**Resolve:**
- Add the missing forms to E2, each with an asserted value. For example `"""a""b"""` has length 4 and `r"a\b"` has length 3.
- Restate the claim so it names only the forms actually asked.
- Or have §12.3 item 5 re-read `src/frontend/lexer.npk` at every re-pin, whatever E2 says.

### C2: `check_error_budget` counts names, but the compiler counts module-qualified identities

**Location:**
- `harness/checks.py:342-345` ("it must not be possible to acquire one by writing a line of code")
- `harness/checks.py:366-371` (`declared` is keyed by bare name)
- `harness/checks.py:391-395` (the report text this close rewrote)
- `harness/selfcheck.py:992-997`

**Evidence at the compiler, `c970483`:** two modules each declare `pub error:ETimeValue;` and have a `fail` site.
~~~
NITPICK-REACH-003 ... 8 identities: moda.ETimeValue, modb.ETimeValue, Unreachable, ...
~~~

**Evidence in the harness:** the same two declarations, one in `cal` and one in `zone`, built with `selfcheck._mini_tree`.
~~~
headline: 1 identit(y|ies) declared over 7 file(s) in src/, against a budget of 3
problems: []
~~~

- `check_failsafe_arms` also agrees with REACH-003 and would not catch it (`arms.py:150-188`, `:240-261`).
- The control this close added (`selfcheck.py:992-997`) declares `ETimeParse` in `cal`, while S-4 assigns it to `fmt`. The control requires silence, yet the new report line says each identity "arrives with the module `SAFETY.md` S-4's table names for it".
- There is no instance today: `src/` declares only `cal.ETimeValue` (`cal.npk:135`). Cycle 0.2's `span` is S-4's next module that "raises `cal`'s".

**Resolve:**
- Key the count by (module, name).
- Fail on a budgeted name declared in two modules, or outside S-4's module, and plant both cases.
- Fix row 34's control.

### C3: SAFETY.md S-22 is broken by a public function, and its check was never built

**Location:**
- `meta/specs/SAFETY.md:1047-1051`: "No function in `src/` returns a `uint8[]` … `check_no_view_returns` on cycle 0.0.3's harness list is what makes it enforced".
- `src/core/bytes.npk:366`

**Evidence:**
- `pub func:bytes_view = uint8[] (Bytes->:b)` has existed since 0.0.4 and is re-exported at `src/lib.npk:130`.
- `check_no_view_returns` is not in `checks.LIVE`, not in `checks.PENDING`, and not among TESTING.md §2's 18 rows.
- I diffed every `check_*` name in the documents against the harness. It is the only one with no decision behind it.
- Cycle 0.0.0 already corrected this exact claim elsewhere (`meta/roadmap/done/0.0/0.0.0.md:836-839`: "It is not on any list"). S-22 kept it anyway.
- No decision exempts `bytes_view`, and S-22 itself says loosening it takes a decision.
- `meta/roadmap/0.4/README.md:94,114` plans against S-22.

**Resolve:**
- Take a decision: either restate S-22 (`bytes_view`'s root is pointer-shaped, which is S-22's own legal row, and S-18e governs its lifetime) or change `bytes_view`.
- Then build the check with a plant, or list it in `PENDING` with a cycle, before 0.4.

### C4: VERIFICATION.md says every index traps, citing a decision that says the opposite for pointers

**Location:** `meta/specs/VERIFICATION.md:85`: "Every index is bounds-checked and traps (D-070)", under the heading "discharged for free".

**Evidence:**
- D-070 at the pin is titled "bounds live in the array type, not the pointer type".
- The pin's emitter (`src/backend/ir/ir_expr.npk:9789-9812`) guards the slice, array, simd and List branches. The pointer branch has no guard: "pointers are thin (D-038) and carry nothing to check".
- `probe13d` asserts at this pin that an out-of-range bare-pointer read returns its planted −9999 and does not trap.

**Resolve:** restate the bullet to D-070's actual scope, and list the bare-pointer residue (S-17b and S-17c) as an obligation the library carries.

### C5: HOST.md H-7 attributes the opposite of the compiler's posture, under the wrong decision

**Location:** `meta/specs/HOST.md:71-76`: "returns the error rather than trapping … the compiler's own posture on the same call (D-061)".

**Evidence:**
- D-061 is about removing the `(!)` marker. It names no call, and it prescribes `#unreachable()`, which traps.
- The compiler's posture on this call is D-176 §3 (compiler `meta/specs/DECISIONS.md:12177-12182` at `c970483`): "the floor still guards the impossible branch with the D-061 trap".

**Resolve:** cite D-176 §3 correctly, and state the errno-forwarding choice as ntime's own (S-5), not the compiler's.

### C6: S-4's arm totals are hand-copied, yet the documents say they cannot go stale

**Location:**
- `meta/specs/SAFETY.md:117-119`: "this row cannot go stale in silence"
- `README.md:88-89`, new at this close: "generated and checked against the compiler on every run"

**Evidence:**
- `check_failsafe_arms` compares the bill computed from source with REACH-003 and prints the result as a report (`arms.py:240-326`).
- Nothing reads S-4's written totals.
- None of the totals is tagged: the tree's 18 `[[sweep:]]` tag names include no arm bill.
- The same untagged numbers appear at `SAFETY.md:84-90`, `README.md:86-87`, `CLAUDE.md:28`, `src/lib.npk:165,231` and in `ROADMAP.md`'s constraint paragraph.
- If a bill moved, the run would stay green and every one of these documents would go stale.

**Resolve:** tag the totals and have `check_denominators` measure them from the arm-bill rows, or reword the claims.

### C7: SAFETY.md says the system-arm half "never grows again", and the same section shows it growing twice

**Location:**
- `meta/specs/SAFETY.md:128-136`, undated
- Against `SAFETY.md:152-160` and `:84`

**Evidence:**
- `DecreasesViolated` arrived at 0.1.0b and `LimitViolated` at 0.1.0c. Both are machinery arms, and together they moved the umbrella's bill from 11 to 13.
- 0.1.2's planning measured that `till` and `loop` also arm `BadStep` (`meta/roadmap/0.1/README.md:227-230`).

**Resolve:** add a dated note saying only the arithmetic arms are front-loaded.

### C8: `check_no_format_string` is described as enforcing, but it is only a `PENDING` name with a false reason

**Location:**
- `CLAUDE.md:401-403` ("makes adding one a red run")
- `src/fmt/fmt.npk:16-17`
- `CONTRIBUTING.md:57-58` ("exists")
- The printed reason at `harness/checks.py:1437-1440` and `TESTING.md:108`: "There is no function in `src/` at all yet"

**Evidence:**
- No such function is defined in the harness; the name exists only in `PENDING`, live from 0.4.
- `src/` has held 39 functions since 0.0.4, including `bytes_extend_str(…, string:src)`.
- A format-string function added today would leave the run green.

**Resolve:** say "goes live at 0.4" in all three places, and give a true pending reason.

### C9: `tests/probe/README.md`'s first rule is broken by eleven of its own probes

**Location:** `tests/probe/README.md:15-16`: "imports nothing from `src/`". This is 0.0.0's P-1, promoted to a standing rule.

**Evidence:**
- `lexical.imports` shows 11 of 49 probes importing from `src/`: `probe15`, `probe16` through `probe16i`, and `probe19`.
- All eleven have rows in the table this close completed.
- No decision amends P-1.

**Resolve:** date and restate the rule, or record the decision that changed it.

### C10: `meta/OPEN_QUESTIONS.md` gives two contradictory numbering rules, and omits a question ntime raised

**Location:** `meta/OPEN_QUESTIONS.md:16-20` ("`O-N` numbering is per repository") against `:1184-1192` ("allocated in the workbench's registry … do not take the next number"; the file "re-states the ones `ntime` raised").

**Evidence:**
- O-N25 was "raised … from `nitpick-time`'s 0.1.4b planning" (the workbench registry, lines 456-478). It became DEF-107 and then D-325, which is declared at `c970483`.
- This tree mentions O-N25 zero times (`git grep -c 'O-N25'`).
- The cycle's findings list (`0.1.5.md:7045-7049`) records `bytes_take` but not the language decision it produced.

**Resolve:** date the header, add an O-N25 entry, and add one line to the cycle's findings.

### C11: V-1k says non-source files are read as text, but two scanners read every file as latin-1

**Location:**
- `meta/specs/TESTING.md:248-251`
- `harness/checks.py:1128` and `:1389`

**Evidence:**
- Both `check_specs_current` and `check_denominators` read `.md`, `.py`, `.toml` and `.txt` through `lexical.read`. `0.1.5.md:552` says so; V-1k omits it.
- This is the mechanism behind the worker's execution finding 1. I re-measured it, and it is latent: over the 219 targets, 6 806 citations are found under UTF-8, 6 806 under latin-1, and 0 lines differ.

**Resolve:** triage finding 1 (either repair it names), and restate V-1k to cover §1.5's three kinds of read.

### C12: V-1l and TM-200 promise whitespace "between any two tokens", but `_RAW_INDEX` allows none after the dot

**Location:** `harness/checks.py:827`

**Evidence:**
- At the pin, `b .⏎ arr [2i64]` compiles and reads the element (exit 0).
- `check_raw_index` is RED on `v.items⏎[0i64]` (the T3 plant), but silent on `v.⏎items[0i64]`, on `v . items [0i64]` and on `b.body. ptr[0i64]`.
- There is no exposure today: `items` and `body` are `hidden`, so the compiler refuses these outside their modules (`TYPE-080`).

**Resolve:** allow whitespace after the dot and plant it, or narrow V-1l's claim.

## Unverified claim

### U1: C-12 is "certified" by a unit that cannot fail on it

**Location:** `0.1.5.md:665`, "C-12 | `every_month_length`". The record re-derived this row by citation, not by assertion (`7096-7110`).

**Evidence:**
- `every_month_length` cites C-12 only to explain its formula (lines 20-27).
- It never passes a field outside C-4's range. Inside that range, C-12's own arithmetic (`CALENDAR.md:306-308`) says an `int32` never overflows.
- C-12's totality claim is argued in `cal.npk:344-349` and `:378-381`, and asserted nowhere. No test forges a `CivilDate` (`git grep 'wild CivilDate|=>! *CivilDate|255u8' -- tests` finds nothing), and no mutation matrix names a C-12 mutant.

**Resolve:** add a unit that builds `CivilDate`s at the `int32` and `uint8` edges through `wild` storage (C-8c's opt-out) and requires no trap. Or mark the row "argued, not asserted".

## Dormant

### D1: TM-201's `#wild_slice` length check is owned by no cycle's checklist

**Evidence:**
- TM-201 makes it "the hardening cycle's, 0.8", but `0.8/README.md` has no item for it, and §8.5 plans only `check_check_registry`.
- `git grep -i 'wild_slice|length check|TM-201|TM-144'` over `meta/roadmap/0.2` to `1.0` and `ROADMAP.md` finds nothing. This is the same shape as the TM-144 deferral that was lost.
- Separately, V-14e (`TESTING.md:549-551`) narrows TM-201's trigger to "cycle 0.2's `check_int128_sites`, when it goes live". O-X6's new note says that check may wait for cycle 0.7.

**Resolve:** add an item to 0.8.4's checklist, and use TM-201's trigger in V-14e.

## Stale

### S1: VERIFICATION.md P-9's loop counts

**Location:** `meta/specs/VERIFICATION.md:284-307`, which says "The `while` count stays 48", with thirteen `for`.

**Evidence:**
- At `d16315f` (0.1.3) the tree had 48 `while` and 13 `for`. At `3fac625` it has 52 and 16.
- The four new `while` loops are 0.1.3c's (`probe18`, `vec_churn_clear`, `vec_churn_pop`, `vec_moves`). The three new `for` loops are 0.1.4's (`every_oracle_date`).
- The property still holds: 52 `decreases`, 0 `unbounded`.

### S2: `ROADMAP.md`'s opening census (lines 6-11)

**Evidence:**
- It says "One decision batch … TM-001 … TM-030"; there are 132 decisions, up to TM-201.
- It counts 7 open questions; there are 10: O-N1, O-N2, O-N3, O-X1, O-B1, O-X3, O-X4, O-X6, O-X8, O-X9.
- "No cycle … blocked on a decision" sits beside O-X6's note that nothing turns its check on until the question is answered.
- This is one of §1.9's ten pages.

## Cosmetic

- **K1:** The execution record (`0.1.5.md:6822-6825`) and §1.11 describe DEF-127 to DEF-130 as edge-counting defects.
  - At the compiler (`40deffa`), DEF-127 is the `for`-binding scope leak in the emitter, and DEF-128 is the type's-edge case.
  - I checked for exposure: none of the 16 `for` loops shadows an outer binding that is read after it.
  - The record is committed (W-28), so the correction goes in the second half's record.
- **K2:** `nitpick.toml`'s range "`probe16b` … `probe16i`" includes `probe16e`, which is `expect-exit: 0`. The count of 14 is right only if 16e is excluded.
- **K3:** TM-201 says "nothing checks a slice's length argument". The compiler checks `0 <= len <= 2^47` at every call (D-315). What is unchecked is whether the length is `count` rather than `cap`.

## The worker's execution findings, re-measured

1. latin-1 prose and `\b`: true and latent. See C11.
2. "the blob `1148a2fd…`": true. `1148a2fd…` is the file's sha256; the git blob id is `e8186ca5…`.

## Checked and found clean

- **Decisions:** 77 distinct compiler decisions are cited. All are declared at `c970483` except D-327, which is correctly described as "in no pin of ours". I read about 30 of them against what they are cited for; beyond D-061 and D-070 in C4 and C5, all matched.
- **Error codes:** `TYPE-047`'s own message cites D-065, and `TYPE-085` is the loan-read-only code.
- **The port:**
  - `lexical.py` is AST-equal to `nitpick-regex` `fb37391` with docstrings removed.
  - E1's constants are text for text (23 lines, 10 imports).
  - Every form the docstring mirrors matches the pin's `lexer.npk` and `p_parse_import`.
- **C-8c:** its three record-only rows re-measured the same at `c970483`.
- **Calendar arithmetic:**
  - The range figures hold: first day −4 371 587, 7 304 484 days, and the seconds bounds.
  - The era bounds hold, −9999-01-01 is a Monday, 9999-12-31 is a Friday, and years 1 … 9999 hold 3 652 059 dates.
  - C-7 is asserted for all seven values in both conventions.
- **Verbatim and text-for-text claims:**
  - The `cal` types match CALENDAR.md §3.
  - `ValueFault` matches S-3 (14 variants).
  - The `Pod` block matches `nitpick-regex` (11 lines).
  - The B-12 shapes match the code, and there are 13 named bounds.
  - The prelude `List<T>` matches the dated note in SAFETY.md.
- **Counts:**
  - The umbrella re-exports 59 names: 11 + 13 + 13 + 22.
  - There are 49 probes, 28 run and 21 refused, and all are in the README.
  - 75 running files plus 37 refused make 112, and 112 = 35 + 77.
  - The defect corpus has 36 files in 8 subdirectories.
  - The self-check plants 40 = 20 + 8 + 9 + 3.
  - TESTING.md §2 has 18 rows, 14 live and 4 pending, and they match the harness, so TM-201's "the four agree" holds.
  - The sweep timing sums add up.
- **Other checks:**
  - The oracle's digest fold is a bijection per step, so one wrong value always changes the digest.
  - The thirteen superset handlers are harmless, as the close judged.
  - A reason-sweep by shape for O-N19, O-N20 and O-N23 found everything live dated or struck, and the superseded decisions carry their markers.
  - CURRENCY.md is current. ISO 8601-1's successor is still a committee draft with its comment period closed on 2026-07-25 ([ISO project 90784](https://www.iso.org/standard/90784.html)).
- **Left clean:** `nitpick-time`, the workbench and the compiler all show an empty `git status --porcelain`. The newest file in `nitpick-time`'s ignored directories predates this audit.

**Verdict:** ACCEPT. Close with every finding triaged, and fix C1 to C4 rather than decline them: C1 is the signal cycle 0.2's adoption relies on, C2 is the error budget's only guard, and C3 and C4 state guarantees the code does not have.
```
