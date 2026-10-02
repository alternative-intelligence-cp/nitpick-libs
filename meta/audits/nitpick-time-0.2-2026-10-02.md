# Pre-close audit — `nitpick-time` cycle 0.2

**Filed by the orchestrator under W-22**, 2026-10-02. The auditor (`s2-ntime-0.2-audit`, `npk:auditor`, `opus` named, dispatched 2026-10-01 23:55, about 38 minutes, 582 018 tokens) wrote nothing; this file is its final message, reproduced below the line — extracted from its transcript by script, not retyped — **inside a fence, with two mechanical changes and no other**: (1) the four absolute home-directory paths on its "Roots" lines are written relative to this workbench, because its leak scan refuses them; (2) the message is fenced, because it quotes `nitpick-time`'s own decision and question ids, which at workbench scope collide with other repositories' (`meta/OPEN_QUESTIONS.md`, *"Library questions this board cites"*: quoted evidence belongs in a fence); its 4 inner fence lines already use `~~~`. **The verdict is ACCEPT, with 22 findings** (8 contradiction, 2 dormant, 5 stale, 7 cosmetic). **The close worker (0.2.4) triages every finding** — W-22 requires each to be addressed or explicitly deferred with a reason, not selected from — and the auditor recommends that C1 (by `SAFETY.md` S-12's operand check, not by narrowing the claim) and C2 to C4 be fixed rather than declined. **S3 and S5 are the orchestrator's**: the workbench board's stream-2 line, and `LIBRARIES.md`'s row for `nitpick-time`.

---

```
# Audit: nitpick-time, cycle 0.2 (instants and timestamps), pre-close (W-22)

status: ACCEPT

- **Audited:** `nitpick-time` at `71f51b8`, which equals `origin/main`. Scope: the seven subcycle files 0.2.0a … 0.2.3, the cycle README and its Gate, the specifications, TM-208 … TM-237, `harness/`, `src/` and `tests/`.
- **Pin:** `5fbaf4a`. `sha256sum -c` passes for `npkc` and `npkrt.o`. Every compiler claim was read with `git show` or `git grep` at `5fbaf4a`, never from `build/`.
- **Mechanical checks:**
  - `check_refs`: clean (88 md files, leak scan 353 of 353); its control passes 16 of 16.
  - `check_record 0.2.3`: clean. The six earlier subcycles report only `head-subject`, because HEAD is 0.2.3's record. That is expected.
- **Harness:** one full run, over a `git archive` export of HEAD under `$TMPDIR`.
  - Result: `GREEN -- 131 unit(s), 0 failures; 4 pending, 201.0 s`.
  - The gate's members printed `swept 7304484` and `swept 44236800` on both legs.
  - `14 live, 3 pending`; 82 plants.
- **CI on HEAD:** run 36960680373, job 110693458567, read through the jobs API (76 011 B). It shows `compiler HEAD == 5fbaf4a… (clean)`, `npkc.ll == the pin's emission, 30232291 B / 5630c2b4…`, and `GREEN -- 131`.
- **Probes:** 22 scratch programs at the pin.
  - Those that run were built `npkc` → `llc -O0`, and `opt -O2` → `llc -O2`, linked against the pin's `npkrt.o`, and run on both legs. The rest were put to `npkc` alone.
  - There were 15 further builds of C1's recommended fix, in a scratch copy.
  - All scratch was under `$TMPDIR`, and all of it is removed.
- **Nothing written:** no repository was written.
- **Roots:**
  - REPO = `nitpick-time`
  - WB = `.`
  - COMPILER = `../nitpick`
  - REGEX = `nitpick-regex`
  - Paths below are REPO-relative unless prefixed.

**Summary: 22 findings.** 8 contradiction, 2 dormant, 5 stale, 7 cosmetic.

- **The Gate holds, measured.** Both of its members and the M-7 stand-ins pass, and their counts were re-derived independently.
- **No memory-safety fault, and no silent wrong answer.** The library gives neither on any value its constructors can produce.
- **What the audit found:**
  - Refusals the documents claim and the code does not make. The known finding, C1, is one of these; C2 is another.
  - Four instruments that pass a planted violation in silence: C3, C4, C8 and D1, each measured.
- **Recommendation:** fix C1 (by S-12's operand check, not by narrowing the claim), and fix C2, C3 and C4 rather than decline them.

---

## Contradiction

### C1: `timestamp_add` traps on a forged `secs` near either end of `int64`, where four texts say a forged `Timestamp` is answered or refused "whatever it holds" — the known finding

**Location:**
- `meta/DECISIONS.md:7178-7180` (TM-234's last sentence) and `:7227-7228` (TM-235: "the function answers whatever it is handed")
- `src/span/span.npk:145-149`
- `meta/specs/VERIFICATION.md:172-173` (P-3's note) and `:194-196` (P-4's note)
  - P-4's note is true of the four forgeries the test makes, but general in its words.
- `meta/roadmap/0.2/0.2.3.md:44`, `:271` (PD-79) and `:272` (PD-80)
- The trap sites: `span.npk:292` (the add), `:295` (the borrow) and `:299` (the carry). All three run before `relay timestamp_of` at `:302`.

**Evidence.** My own runs, forged through `wild` storage as `timestamp_add_edges.npk` forges, with exits for −O0 / −O2:

~~~
secs = int64 max,                nanos 0,          d = +1 s        93 / 93   (the add)
secs = int64 max,                nanos 999999999,  d = +1 ns       93 / 93   (the carry)
secs = int64 min,                nanos 0,          d = -1 ns       93 / 93   (the borrow)
the same three with d = 0                                          refused / refused (ETimeValue)
secs = int64 max - 9223372036,   nanos 999999999,  d = int64 max   93 / 93
secs = int64 max - 9223372037,   nanos 999999999,  d = int64 max   refused
secs = int64 min + 9223372036,   nanos 0,          d = int64 min   93 / 93
secs = int64 min + 9223372037,   nanos 0,          d = int64 min   refused
~~~

- **Full extent:**
  - Any forged `secs` within 9 223 372 037 s (about 292 years) of either end of `int64` traps for some `Duration`.
  - Every other forged `secs` outside the range is refused.
  - A forged `nanos` alone is never trapped: `timestamp_of` refuses what one carry cannot repair.
- **Reach:** only `wild` storage can produce such a value.
  - A constructed `Timestamp` has |`secs`| ≤ 3.8 × 10¹¹.
  - `5i128 =>! Timestamp` is `NITPICK-TYPE-032` at the pin, measured.
  - The trap is loud, never silent.
- **It also contradicts a rule the specifications already state.** `meta/specs/SAFETY.md:395-398` (S-12): *"Every arithmetic entry point checks its operands against the supported range and returns the error; the trap remains as the belt for a path the check missed."* `timestamp_add` checks its result, through `timestamp_of`, and never its operand.

**Resolve — recommended: make the function total; do not narrow the claim.**
- **The fix:** two lines before the arithmetic.
  - A `t.secs` below `NTIME_SECS_MIN` or above `NTIME_SECS_MAX` fails `ETimeValue` (`YearRange`), which is `timestamp_of`'s own answer for that `secs`.
  - After those two lines, |`secs`| ≤ 3.9 × 10¹¹ through the add, the borrow and the carry.
- **Measured in a scratch copy at the pin:**
  - All ten forged cases above are refused, on both legs.
  - `timestamp_add_edges`, `timestamp_since_edges`, `civil_to_utc_edges`, `timestamp_construct` and `utc_vectors` still exit 0 on both legs.
  - There is no new identity: `span` already raises `cal.ETimeValue`.
- **One behaviour moves.** The test's forged `HI_SECS + 1`, moved back by −1 s, is answered today and refused after the fix. The test accepts either outcome.
- **It needs a decision superseding TM-234 in part.**
  - TM-234 declined "a range check of its own before the constructor's" because it would be a second check on the SUM.
  - This one checks the OPERAND, and one edit reddens it: delete it, and the forged cases are 93 again.
  - Add the three measured cases to the test's forged section.
- **Why not narrow the claim instead:**
  - S-12 already asks for the operand check.
  - `CALENDAR.md` C-8c says *"write downstream functions total where they can be — because it costs nothing and the opt-out exists"*.
  - Both siblings are total over forged input: `timestamp_since` by `int128` (TM-236), and `civil_to_utc` by bound.
- **On the board's wording** (WB:`BOARD.md:29`, "refuse before it adds, as `civil_to_utc` does by PD-67"):
  - `civil_to_utc` refuses nothing before it adds. It is total because its operands are narrow (`span.npk:112-115`).
  - Measured: forged years at `int32`'s two extremes, with every `uint8` field at 255, are refused (exit 10, both legs).
  - The precedent to cite is S-12 and C-8c.

### C2: M-3 is said to hold against "everything a consumer can write but the `wild` opt-out"; a consumer converts both ways in one line

**Location:**
- `meta/DECISIONS.md:6578-6581` (TM-221)
- `meta/specs/TIME_MODEL.md:68-77` (M-3: "Here that program does not compile"; its note: "What converts is `wild` storage")
- `README.md:19-21` ("cannot be built from a number or converted to a point on the UTC scale")
- `README.md:61-64` ("there is no conversion between them … a bug you cannot write here")
- `src/span/span.npk:19-24` ("a consumer can neither build an `Instant` from a number nor edit one")
- `src/lib.npk:265-268`
- `tests/probe/probe20_instant_literal_refused.npk:4` (its title)

**Evidence.** A consumer that imports `span` and writes no `wild` and no `=>!`:

~~~
Timestamp:t = (timestamp_of(1759363200i64, 250000000i64)).value      // a realtime reading
Instant:i  = raw instant_of((t.secs * 1000000000i64) + (t.nanos => int64), InstantClock.Monotonic);
instant_since(raw instant_add(i, raw duration_secs(5i64)), i)       // 5 000 000 000 ns
timestamp_of(i.ns / 1000000000i64, i.ns % 1000000000i64)             // == t
~~~

- `npkc` exits 0, and the program exits 0 on both legs. This is the timeout M-3 says does not compile.
- TM-216 (`meta/DECISIONS.md:6333-6337`) already says *"a caller who hands it a wall-clock reading has opted out in writing"*. TM-216 and TM-221 cannot both be right.
- The cycle README's own watch-for (`meta/roadmap/0.2/README.md:180-182`) says *"M-3's 'there is no conversion' is only true if a program attempting it fails to compile."*
- What the type does refuse is all true and all asserted (probes 20 … 21b).

**Resolve:**
- Restate the six sites to what is enforced: no implicit conversion, no conversion function, no `=>!`, no struct literal, no field write.
- Name the deliberate path that TM-216 calls an opt-out in writing.
- Mark TM-221's sentence.
- Add one `expect-exit: 0` probe that pins the deliberate path, so the restated claim is checked rather than stated.
- If the author wants the README's guarantee as written, that is a design question: a constructor whose name says it takes a raw reading. Settle it before 1.0 (TM-013).

### C3: `check_constants_named` lets a second copy of an owned number stand anywhere in `core`

**Location:**
- `harness/checks.py:696` (`if mod not in (owner, "core"):`) and `:499-501`
- `meta/DECISIONS.md:6687-6690` (TM-223) and `:7097-7100` (TM-232). Both say: "spelled once, in `src/core/limits.npk` … a literal … anywhere else in `src/` … is a finding".
- `meta/specs/SAFETY.md:505-516` (S-16's notes: "the one copy is `src/core/limits.npk`'s")

**Evidence:**
- I planted `86400i64` and `1_000_000_000i64` in `src/core/bytes.npk` in a scratch export. The check reports 0 findings, and its count of owned occurrences goes from 7 to 9.
- The same `86400i64` planted in `span.npk` is 1 finding.
- The check's granularity is the module (`module_of`). The decision texts say the file.

**Resolve:**
- Key the exemption to the file:
  - a `core`-owned value is allowed in `limits.npk` only, as `_BOUND_DECL` already is;
  - a `cal`-owned value is allowed in `src/cal/` and `limits.npk`.
- Add a plant in `src/core/bytes.npk`.
- Nothing in the tree moves: the seven owned occurrences are `limits.npk:123-124` and five in `cal.npk`.
- The alternative is to restate the three texts to say "the module".

### C4: `check_no_view_returns` does not read through an optional

**Location:**
- `harness/checks.py:1809-1832` (`_view_in`)
- `meta/specs/TESTING.md:50`
- `meta/specs/SAFETY.md:1205-1214` (S-22's 0.2.3a note)
- TM-228 (`meta/DECISIONS.md:6906`)

**Evidence:**
- This function compiles in a consumer at the pin (`npkc` 0, IR written), and it hands back a view of its parameter:
  `func:first_word = uint8[]?(uint8[]:src) never fails { if (src.len == 0i64) { pass NIL; } pass src; };`
- Planted in `src/core/bytes.npk` beside a `uint8[]` twin, the check reports one finding: the twin.
- `_SLICE` anchors on `[]$`, and `cstring` is matched exactly, so `cstring?` passes as well.
- Cycle 0.4's parsers are the first code likely to want "the rest, or none".

**Resolve:**
- Make `_view_in` read an optional's inner type.
- Plant `uint8[]?` and `cstring?`, each beside an `int64?` control.
- Restate §2's row, and mark TM-228.

### C5: the comment contracts write `answer` where an `ensures` clause takes `result`

**Location:**
- `meta/specs/VERIFICATION.md:56-58` (P-1b: "`answer` and `outgoing` for `result` and `old` (TM-130)") and `:77-78` ("mechanical — uncomment the clause")
- `meta/specs/VERIFICATION.md:161-164` and `:167-173` (P-3's sample, restated at 0.2.3)
- `meta/DECISIONS.md:4285-4286` (TM-164) and `:7226` (TM-235)
- `src/span/span.npk:225-226` and `:287-288`
- 21 more lines: 17 in `cal.npk`, 3 in `bytes.npk`, 1 in `vec.npk`

**Evidence:**
- At the pin, `ensures result >= 0i64` compiles.
- `ensures answer >= 0i64` is `NITPICK-RESOLVE-002 …:3:13: cannot find answer in this scope`.
- The compiler's reference, COMPILER@5fbaf4a:`meta/specs/VERIFICATION_REFERENCE.md:329` and `:344-346`: `result` is "legal in `ensures` alone, so no binding can shadow it."
- TM-130 (`meta/DECISIONS.md:2341-2344`) substitutes `answer` for local names only.
- `meta/roadmap/done/0.1/0.1.1.md:399-401` measured the live clause with `result`.
- The tree writes the keyword `old(…)` in its comment contracts (`bytes.npk:144`, `vec.npk:322`), so the substitution is applied to one keyword and not the other.
- So P-1b's "the switch is mechanical — uncomment the clause" is false of these lines.

**Resolve:**
- Write `result` in contract comments, and supersede TM-164's and P-1b's substitution for contract text.
- Restore P-3's sample to `result`.
- Sweep the 25 lines. `vec.npk:456`'s `answer` is a real local and stays.
- The alternative is to keep `answer` and restate the "mechanical" claim so it names the rename.

### C6: `instant_since` traps on a pair `instant_of` builds, where S-12 says a fallible arithmetic entry point returns the error

**Location:**
- `meta/specs/SAFETY.md:393-398` (S-12)
- `meta/specs/TIME_MODEL.md:96-99`: M-4's footnote, "cannot overflow in practice — the … origin is the boot"
- `meta/specs/TIME_MODEL.md:84` (`instant_of` takes any `int64`) and `:347` (§9's row omits the trap)
- `src/span/span.npk:126-127`

**Evidence:**
- `instant_since(instant_of(int64 max, Monotonic), instant_of(-1, Monotonic))` exits 93 on both legs.
- The control, the pair (max, 0), is answered exactly.
- The footnote was written when `instant_since` was `never fails`. TM-216 made it fallible and did not revisit the overflow.

**Resolve — the close's choice:**
- Either refuse: `ETimeValue`/`Overflow`, by a sign test before the subtraction, or by computing in `int128` with a §5 row.
- Or state the trap: in M-4, in §9's row, and as a named exception to S-12. I lean to stating it, for symmetry with `instant_add`, which is `never fails` and so must trap.

### C7: `SPAN_MODEL.md` §5 says "every site is enumerated"; six sites written in cycle 0.2 have no row

**Location:** `meta/specs/SPAN_MODEL.md:183-185` and its table at `:187-198`.

**Evidence:** these sites have no row:
- `instant_since` and `instant_add` (`span.npk:206-213`)
- `civil_to_utc` (`:256-262`); its no-overflow argument lives only in a comment, at `:112-115`
- `duration_mins`, `duration_hours` and `duration_weeks` (`:268-274`, `:280-282`), beside the one `duration_days` row

**Resolve:** add the six rows, each marked `no` in the `int128` column (which `check_int128_sites` reads without moving), or restate "every site".

### C8: the constants check shares a name and a literal reader with `nitpick-regex`'s, not a rule

**Location:**
- `meta/specs/TESTING.md:47` ("no bound outside `src/core/limits.npk`")
- `harness/checks.py:655`
- REGEX:`harness/treecheck.py:318-411` (RX-062, RX-202)

**Evidence:**
- In a scratch export I replaced `timestamp_of`'s `NTIME_SECS_MAX` with `253402300799i64`. The check reports 0 findings.
- This repository's check reads bound declarations and the four owned numbers. Regex's check reads literals at comparisons.

**Resolve:**
- Key every named bound's value to `core` in the owner map, with small structural values excepted (as regex's RX-062 `_SMALL` set does).
- Measured: no literal in `src/` outside `limits.npk` equals any of these values today, so nothing moves.
- The alternative is to restate the row as "no bound DECLARED outside".

## Dormant

### D1: S-15b's range check before every `=>!`, and N-20's reason beyond `int128`, are checked by nothing

**Location:**
- `meta/specs/TESTING.md:59-62` (V-1 credits `check_int128_sites` with "its arithmetic does not silently overflow")
- `meta/specs/SAFETY.md:433-436`
- `meta/specs/SPAN_MODEL.md:212-217`
- `harness/checks.py:1943`

**Evidence:**
- I appended two `span` functions in a scratch export: one with an `int256` intermediate and one with a `uint128` intermediate, each narrowed by a bare `=>! int64`. The `int256` one also compiles and runs at the pin.
- Every live tree check is silent on both. `check_constants_named` fired only on the plant's own `1000000000i256` literal.
- The same function written in `int128` is red.
- Today's twenty `=>!` in `src/` are guarded, or are pointer casts.

**Resolve:**
- Widen `_INT128` to every wide integer type, or restate N-20.
- Inventory the `=>!` sites in `src/`, or restate V-1.

### D2: P-3 asks every constructor and arithmetic entry point to carry its range as a contract; only three of `span`'s thirteen functions do

**Location:**
- `meta/specs/VERIFICATION.md:150-152`
- `src/span/span.npk`: contracts at `:225-228`, `:287-290` and `:308-310` only

**Evidence:**
- None at `instant_of`, `instant_since` or `instant_add`.
- None at `timestamp_to_utc`.
- None at `civil_to_utc`, which is a `Timestamp` constructor.
- None at the four `duration_*` constructors.
- No plan in cycle 0.2 weighed P-3 for these functions.
- P-11 (`:391-393`) hands over only what is written.

**Resolve:** write the contracts as comments, or narrow P-3 by a decision.

## Stale

### S1: `TIME_MODEL.md` §8 is cited for `instant_add`'s trap; the row is in §9

**Location:**
- `meta/DECISIONS.md:6343` (TM-216)
- `src/span/span.npk:127`
- `meta/roadmap/0.2/0.2.0.md:296`

**Evidence:**
- §8's table (`TIME_MODEL.md:307-310`) has no `Instant` row.
- §9's row (`:346`) has it, and did at the founding commit `c2887bd` too.

**Resolve:** correct `span.npk:127`, and add a marker to TM-216.

### S2: a compiler defect this repository found is recorded here as the language's rule

**Location:**
- `src/span/span.npk:97-101`
- `meta/DECISIONS.md:6611-6613` and `:6652-6653` (TM-222)
- `meta/roadmap/0.2/0.2.2.md:1614` (`compiler-defect: none`)
- `meta/OPEN_QUESTIONS.md:1257-1265`

**Evidence:**
- The `NITPICK-TAINT-001` refusal of the bare `#unreachable();` statement form is the workbench's O-N34 (WB:`meta/OPEN_QUESTIONS.md:258-285`).
- It is the compiler's DEF-225, fixed in landing 93 (`93bcb66`), which is after the pin.
- This repository's registry section has no O-N34 entry.

**Resolve:**
- Restate O-N34 here.
- Mark TM-222.
- Date `span.npk:97-101`, and hand the re-measure on to the adoption that carries landing 93.

### S3: the workbench board's stream-2 line carries work already done

**Location:** WB:`BOARD.md:29`.

**Evidence:** it lists as still carried three items that landed at 0.2.3a:
- the owner of 1 000 000 000 (TM-232);
- `_NUMBER`'s blindness to other spellings (TM-231);
- question 17's rewording (`7d86293`). The live description is 258 characters and equals `github.txt:5`.

Its precedent for C1 is also mis-stated (see C1).

**Resolve:** the orchestrator's.

### S4: `ROADMAP.md` says `check_purity` "goes live" at 0.3; it has been live since 0.0.3

**Location:** `meta/roadmap/ROADMAP.md:176` and `:267`.

**Evidence:** this run shows `ok check_purity`. 0.3's own README dated its row (`meta/roadmap/0.3/README.md:43`); the roadmap was not.

**Resolve:** date both lines before 0.2.4 writes `0.3.0.md`.

### S5: the workbench registry row for `nitpick-time` is stale

**Location:** WB:`LIBRARIES.md:15`.

**Evidence:** it reads "planned — 13 specs, 30 decisions, 10 cycles, 0.0 execution-grade".

**Resolve:** the orchestrator's.

## Cosmetic

- **K1:** TM-234 (`meta/DECISIONS.md:7187-7188`) says the sum "fits `int64` by nine orders of magnitude".
  - The seconds' sum fits by seven (2.6 × 10¹¹ against 9.2 × 10¹⁸).
  - Nine is the nanoseconds' margin.
  - A forged operand fits by none (C1).
- **K2:** `span.npk:107-112` says a forged reading is "never trapped or carried". That is true of the two forgeries it names. A forged hour of 24 is answered with the next midnight (measured, exit 11 on both legs), which C-8b allows. Say so.
- **K3:** `tests/unit/limits_named.npk:3-10` — the 0.2.3 worker left this header for the audit to weigh, and a dated note is warranted. The header says the file asserts `CALENDAR.md` §2's relations. It also asserts:
  - S-16's two factors (exits 17 and 18);
  - Z-19's offset (exit 16);
  - N-3's two `Duration` ends (exits 22 and 23).
- **K4:** S-16's notes do not record `timestamp_add`'s division by `NTIME_NANOS_PER_SEC`. The argument holds:
  - the IR guards it with the zero check (`npk_trap -4097`) and the MIN/−1 check (`-4098`);
  - `limits_named` exit 18 holds the value.
- **K5:** one file, two counts. `ci.yml:42` and `run.py:29` say "fifteen named bounds"; the check and `0.2.3.md` §1.2 count 13 bound declarations.
- **K6:** `GLOSSARY.md:9` defines an instant as "a point on the monotonic timeline". Since TM-215 an `Instant` is a reading of one of two clocks.
- **K7:** S-4's column header still reads "MEASURED at pin `c3bdae2`".

## Checked and found clean

- **The Gate** (`meta/roadmap/0.2/README.md:166-170`) holds.
  - Both members swept their full domains on both legs, here and in CI.
  - TM-224's 512 days, re-derived in Python: 512 distinct, 321 before the epoch, −9875-01-21 … 9915-10-06.
- **M-7 holds** after every operation that yields a `Timestamp`.
- **Re-derived independently, all equal:**
  - TM-235: 99 511 answered and 489 refused (206 above the range, 283 below); 24 896 carries and 24 971 borrows; the last value (−78 690 499 287 s, 983 031 784 ns).
  - TM-236: 48 617 answered and 51 383 refused; `Duration`'s two ends and their edge readings.
  - TM-233: the constructors' ends, and the stride.
- **Totality:** `civil_to_utc` and `timestamp_since` are total over forged input.
- **Runtime helpers:** no undefined `__muloti4`.
- **Compiler claims at `5fbaf4a`:**
  - the prelude's `duration_secs` (`prelude.npk:1045-1062`);
  - the 20 decisions cited in cycle 0.2's added lines are all declared;
  - DEF-165 is open at the pin, as cited;
  - `NITPICK-TYPE-032`'s text (`type_cast.npk:558`, `:699`);
  - `check_copy_impl` (`type_trait.npk:1277`);
  - the quoted runtime text at `npkrt.ll:3502-3506`;
  - `num_width.npk`'s 37 width suffixes and `numeric.npk`'s base-suffix order equal the harness's literal reader.
- **Shared rules with `nitpick-regex`:**
  - `lexical.py` is AST-identical to REGEX `7c0478a`, with docstrings removed.
  - `Vec<T: Copy>` is on the type and on all nine verbs, as RX-188 has it. Regex's element check is declined here by TM-214, with its reason.
- **Documents against the tree:**
  - `ValueFault` has 15 variants.
  - Both `=>!` in `span` are guarded, and there is no `+%`, `-%` or `*%` in `src/`.
  - `timestamp_until` is carried at cycle 0.7's README:59.
  - The arm bills are `span` 11 and the umbrella 13.
  - Every checklist tick holds, apart from the struck, decided `timestamp_until` box.
- **Currency:** every row in `meta/research/CURRENCY.md` was checked within the last six months. The one inline fetch was consistent with its row.
- **Left clean:**
  - `git status --porcelain` is empty in all four trees.
  - The only new entries in the workbench are the sandbox's zero-byte mount-point placeholders, which `.git/info/exclude` already names.
  - The scratch directory is removed.

**Verdict:** ACCEPT. Close with every finding triaged. Fix C1 (by S-12's operand check) and C2 to C4 rather than decline them.
```
