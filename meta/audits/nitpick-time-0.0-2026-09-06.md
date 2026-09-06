# Pre-close audit — `nitpick-time` cycle 0.0

**Filed by the orchestrator under W-22**, 2026-09-06. The auditor wrote nothing;
this file is its final message, reproduced verbatim below the line. **The close
worker (0.0.6) triages every finding** — W-22 requires each to be addressed or
explicitly deferred with a reason, not selected from.

**Repository** `nitpick-time` at `0c85648` · **pin** `aaffb87` · **agent**
`npk:auditor` on `claude-opus-5`.

## What the orchestrator verified before filing

Filing is not endorsement, but the three findings that most change what the
close must do were spot-checked here, and **all three reproduce**:

- **A1** — both of this repository's structs are single-line declarations:
  `pub struct:Vec<T> = { wild T->:items; int64:count; int64:cap; };` and
  `pub struct:Bytes = { buffer:body; int64:len; };`. The extractor's `continue`
  after the declaration match therefore skips their real fields, exactly as
  reported.
- **A2** — `src/core/bytes.npk:88` is `b.body = move(fresh);` under a comment
  reading *"THE OVERWRITE THAT DROPS THE OLD BODY (D-186)"*, while
  `bytes_view`'s comment at `:240` promises the view *"is valid exactly as long
  as the `Bytes` is"*. Those cannot both be true, and `bytes_view` and
  `bytes_push` are both public.
- **A4** — `.github/workflows/ci.yml:80` pins
  `0dfddac045bdab6abbd367b1ffb31de695b9bf22` under a comment claiming it is
  *"`../BOARD.md`'s pinned toolchain"*; the board's header reads `aaffb87`.

**A2 is the finding to read first.** It is the second use-after-free this cycle
on this library's own surface, and the first one — `vec_pop<T>` at 0.0.4 —
passed review and an independent VERIFIED PASS for the same structural reason:
**every gate this repository owns is a leak gate**, and a use-after-free is
found by a wrong answer rather than by a gate.

---

# Pre-close audit — `nitpick-time` cycle 0.0 at `0c85648`, pin `aaffb87`

Method notes: every sweep below reports its denominator. Where the property is not lexical I say how many candidates the sweep produced and how many I read. Compiler facts are read at `aaffb87` via `git -C ../nitpick show aaffb87:<path>` (the auditor wrote this as an absolute path; **rendered relative here by the orchestrator**, because `check_refs` refuses an absolute path in a tracked file and the leak scan is right to); external facts at their primary source at the exact tag. Nothing in the repository was modified — every experiment wrote to the session scratch directory, and the two compilations at `0dfddac` used `-o` into scratch.

---

## Ranked summary

**Would not let a cycle close over — 5:** A1, A2, A3, A4, A5.
**Would let it close, but they belong on 0.0.6's numbered findings list — the rest.**

---

# A. Would not close over

## A1 — `check_no_owning_fields` is blind to the struct form this repository actually writes (contradiction, demonstrated)

`harness/checks.py:437-455`, `_structs()`:

```python
m = _STRUCT_DECL.match(line)
if m:
    cur = m.group(1)
    out.setdefault(cur, [])
    continue                 # <- the rest of THIS line, i.e. the fields, is never read
```

A struct written on one line has its fields skipped, `cur` is never cleared (the closing `};` was on the same line), and the following lines are attributed to it as fields until some later line starts `};`.

Both of this repository's structs are one-liners: `src/core/vec.npk:111` and `src/core/bytes.npk:60`. What the extractor believes their fields are:

```
 Vec:   src/core/vec.npk:123   pub func:vec_init<T> = Vec<T>(int64:cap) never fails {
        src/core/vec.npk:124   int64:n = cap;
        src/core/vec.npk:129   wild int8->:mem = alloc(n * #size_of<T>());
        src/core/vec.npk:130   pass Vec{ items: mem =>! wild T->, count: 0i64, cap: n };
 Bytes: src/core/bytes.npk:63  pub func:bytes_init = Bytes(int64:cap) never fails {
        src/core/bytes.npk:66  pass Bytes{ body: buffer_new(n), len: 0i64 };
```

Neither type's real fields (`wild T->:items`, `buffer:body`) has ever been examined.

The same violation, both ways, run against `checks.check_no_owning_fields`:

```
multi-line (the self-check's fixture)                      -> 1 problem(s)
single-line (src/core/vec.npk's and bytes.npk's own form)  -> 0 problem(s)
```

`harness/selfcheck.py:614-621` plants the violation **multi-line**. So the check is red on the fixture its author wrote and silent on the identical fault written the way the repository writes structs. It is the exact failure the brief asked me to look for — a check that passes the test its author imagined.

It matters at 0.5, not today: `check_no_owning_fields` is the stated gate on `ZONE_MODEL.md` Z-7's row types (`vec.npk:70` says "`check_no_owning_fields` enforces rather than trusts"), and today it reports `0 table(s) ... against 2 struct(s)`, which reads as "nothing to check" rather than "cannot see".

**Resolves:** make `_structs` parse fields on the declaration line and terminate on the same line's `};`, and add a **single-line** plant to `PLANTED` beside the multi-line one.

## A2 — `bytes_view`'s lifetime claim is false, and the failure is a use-after-free on the public surface (contradiction, demonstrated at the pin)

`src/core/bytes.npk:237-241`:

```
// THE BORROW OUTLIVES NOTHING IT SHOULD NOT: the slice refers to the sink's
// body, so it is valid exactly as long as the `Bytes` is.
```

`bytes_reserve` line 88 is `b.body = move(fresh);`, which drops the old buffer (D-186). So the view is valid as long as the `Bytes` is **and is not grown** — and `bytes_push`, `bytes_extend`, `bytes_extend_str` and `bytes_reserve` all grow it.

Two programs differing only in the initial capacity, built with the pinned `aaffb87` toolchain, output to scratch:

```
viewcontrol  (cap 64, no growth, view held across 40 pushes)  run exit=0    view still reads 65
viewstale    (cap  2, growth forced, otherwise identical)     run exit=30   the byte read back is 170 = 0xAA
```

`170` is the allocator's free poison (D-183, confirmed at `aaffb87:meta/specs/DECISIONS.md:12946`). The view read freed memory.

`bytes_view` and `bytes_push` are both public (`src/lib.npk:84` and `:90`), so a consumer following that comment writes a use-after-free that compiles, links, runs and reads poison — the same shape as the `vec_pop<T>` bug 0.0.4 shipped, in a comment written at 0.0.4 and left untouched at 0.0.5. Nothing in the gates sees it: `check_raw_index` reports 0 sites, `check_purity` is not about this, D-151 counts `wild` blocks and a `buffer` is managed, the symbol scan is blind, and no test holds a view across a growth.

**Resolves:** correct the comment to state the invalidation rule, and add a unit test with a control (the pair above is ready-made).

## A3 — CI has never run, and it will not go green: `llc --version`'s first line on the tarball CI installs carries no version (contradiction with a verified external source)

`harness/toolchain.py:58-63` takes **only the first line** and requires a dotted version in it:

```python
first = out.splitlines()[0] if out.splitlines() else ""
m = _VERSION.search(first)
if not m:
    raise ToolchainError("%s --version printed a first line with no dotted version in it, ...")
```

The module's own header records the three banners "measured at the pin" — `Ubuntu LLVM version 20.1.2` etc. Those are the **Ubuntu-vendored** build, which is what this workbench has (`llc --version` here prints exactly that; confirmed).

`.github/workflows/ci.yml:146` installs the **upstream release tarball**. Verified at LLVM's own source at tag `llvmorg-20.1.2`:

- `llvm/lib/Support/CommandLine.cpp:2524-2533`
  ```cpp
  #ifdef PACKAGE_VENDOR
      OS << PACKAGE_VENDOR << " ";
  #else
      OS << "LLVM (http://llvm.org/):\n  ";
  #endif
      OS << PACKAGE_NAME << " version " << PACKAGE_VERSION << "\n  ";
  ```
- `clang/cmake/caches/Release.cmake` at that tag: no `PACKAGE_VENDOR` (grep for `vendor` returns nothing).
- `.github/workflows/release-binaries.yml` at that tag: no `-DPACKAGE_VENDOR` in the cmake invocation (line 238-242).

So `llc --version` and `opt --version` from `LLVM-20.1.2-Linux-X64.tar.xz` begin `LLVM (http://llvm.org/):`, with the number on the **second** line. `ld.lld` is unaffected — its banner carries the number on line 1 either way.

The module's docstring already argues "the match is on the dotted number and not on the surrounding words". The mechanism is narrower than the argument: it is also on the *first line only*.

Worse, the failure surfaces in the wrong place. `run.py` runs the self-check first; each inner run reaches step 3, raises `ToolchainError`, prints `RED -- the toolchain is a build input (D-204)` and exits 1 having written no unit verdicts — so `Case.fails()` reports *"no `FAIL tests/unit/bad_exit.npk` verdict. The faulted file was not reported as a failing unit"* and the run dies at `RED -- the SELF-CHECK failed`. The first-ever CI run therefore fails with a message about the self-check not catching its planted fault, three levels from the cause.

**Verified clean about CI, so the close is not chasing ghosts:** the asset name and size are right (`LLVM-20.1.2-Linux-X64.tar.xz`, 2 021 628 328 B, from the GitHub releases API), and the tarball is a full CPack install (`CPACK_GENERATOR TXZ` over the install targets), so `llc`, `opt`, `ld.lld` and `llvm-config` are present.

**Resolves:** match against the whole `--version` output, not `splitlines()[0]`, and record both banner shapes in the docstring.

## A4 — CI pins the previous compiler and says it pins the current one (contradiction)

`.github/workflows/ci.yml:78-81`:

```yaml
  # ../BOARD.md's pinned toolchain, by FULL sha. `0dfddac` is the short form
  NITPICK_COMMIT: 0dfddac045bdab6abbd367b1ffb31de695b9bf22
```

`BOARD.md:13` reads `**Toolchain:** aaffb87 · .internal/toolchain/aaffb87/ · pinned 2026-09-05 22:47`. The comment's claim about the other document is false. `NPKC_SHA256_WORKBENCH` / `NPKRT_SHA256_WORKBENCH` (lines 87-88) are likewise `0dfddac`'s digests.

`meta/roadmap/0.0/README.md:74` marks CI `[~]` and says the acceptance "carries to the push that closes 0.0" — so this is a close item by the cycle's own accounting.

**Measured, so the triage is informed rather than fearful.** I built and ran the library and every unit at the *CI* pin `0dfddac` (output to scratch):

```
src/lib.npk                  builds clean at 0dfddac (npkc 0, llc 0)
tests/conformance/import.npk ran exit=0    want=0    OK
tests/unit/vec_pop_empty.npk ran exit=94   want=94   OK
tests/unit/vec_boundaries    ran exit=0    want=0    OK
tests/unit/vec_at_past_end   ran exit=94   want=94   OK
tests/unit/vec_set_past_end  ran exit=94   want=94   OK
tests/unit/bytes_put_int     ran exit=0    want=0    OK
tests/unit/bytes_growth      ran exit=0    want=0    OK
tests/unit/limits_named      ran exit=0    want=0    OK
```

`vec_pop<T>`'s new `move(s[...])` — written at `aaffb87` and never compiled at `0dfddac` before now — is fine. The three `EXPECT_EXEMPT` verdicts also hold at `0dfddac` (`tests/probe/defect/generic_owning_copy/TRANSCRIPT.txt:148-159` records `case1` `run:0` and `case4` reading the poison at `0dfddac` too). So the content is pin-portable; what is wrong is the pin and the comment.

**Resolves:** bump `NITPICK_COMMIT`, `NITPICK_COMMIT_SHORT` and both digests to `aaffb87` in the same commit that fixes A3, and re-read the three stale comments in that file (see D2).

## A5 — the cycle's proudest claim is wider than its mechanism: TM-137's check is uncommissioned and undocumented, and `V-14c` is false (dormant + contradiction)

`meta/specs/TESTING.md:260-267`, **Rule V-14c**: *"every check in §2 is commissioned the same way. The tree checks are pure functions of a directory, so the self-check plants one violation per check and requires each to find it..."*

§2's table has **14 rows**. `selfcheck.py`'s `PLANTED` covers 7 of the 8 `checks.LIVE` entries, and `part_b_specs_current` covers the eighth. **`check_expect_headers` is in §2's table (line 50) and is planted nowhere.** So V-14c's "every" is false, and the row it is false about is the check TM-115 was written to create.

Worse, and newer: **`check_exemptions_live` — the mechanism 0.0.5 built to fix TM-137 — is in neither place.**

```
$ git grep -ln 'check_exemptions_live'      # 8 files, 175 tracked
harness/run.py  meta/DECISIONS.md  meta/roadmap/0.0/0.0.5.md  meta/roadmap/0.0/README.md
tests/probe/defect/generic_element_move/README.md  (+3 .npk headers)
```

`meta/specs/TESTING.md` is not among them, and neither is `harness/selfcheck.py`. `TESTING.md` §2's `check_expect_headers` row still describes the *superseded* mechanism verbatim — *"The exemption list is diffed in both directions, so an exemption naming a file that is gone fails too"* — which is precisely the check TM-137 showed insufficient. `0.0.5.md:215-216` records it as "commissioned green at 6 of 6, and red with one verdict changed" — by hand, in one session, which is the state `selfcheck.py`'s own docstring condemns: *"three instruments had been commissioned by hand there, and three checks is not a runner."*

So of the two instruments that found this cycle's two worst faults, neither is in the automated self-check, and one is not in the specification at all.

**Resolves:** a `TESTING.md` §2 row and a `V-` rule for `check_exemptions_live`; a self-check case that plants a moved verdict; a self-check plant for `check_expect_headers`; and either honour V-14c or restate it with the exceptions named.

---

# B. The class question from the brief: what else the gates cannot see

The brief asked for the class, not the instance. Three answers, one of them demonstrated end to end.

## B1 — `check_raw_index`'s name is wider than its mechanism, and the evasion runs (dormant)

`harness/checks.py:498-501` is two literal substrings:

```python
RAW_INDEX_OWNERS = {".items[": "src/core/vec.npk", ".ptr[": "src/core/bytes.npk"}
```

Bind the bare pointer to a local and index the local. Built at `aaffb87`, output to scratch:

```
wild int64->:p = v.items;
int64:x = p[v.count + 4i64];
```

```
npkc exit=0  ll=62723 B ; llc exit=0 ; ld exit=0 ; run exit=13
```

Exit 13 is the program's "the value read is not 10" — four elements past the live prefix, read, no trap. And on that spelling:

```
check_raw_index -> 0 problem(s) | 0 raw-index site(s) over 2 file(s) in src/, 2 owner(s) allowed
```

The library contains no such alias today, so this is not a live defect — it is the answer to "what would it miss". The check enumerates the *known* bare pointers by field name; it does not find bare pointers. A new `wild X->` field at 0.5 called anything else is uncovered by construction, and no check notices a bare pointer that has no entry.

Second, smaller instance in the same file: `SAFETY.md` S-17c's code block says the slice goes *"over `count`, never over `cap`"*, and nothing checks the length argument of `#wild_slice`. A future accessor laying the slice over `cap` gets a guard that accepts allocated-but-dead space, which is exactly the distinction `probe13b` exists to make — and `probe13b` is a probe about the language, not a check over `src/`.

## B2 — 21 committed expectations under `tests/probe/defect/` are evaluated by nothing (dormant)

24 `.npk` files live under `tests/probe/defect/`. Confirmed against the manifest's own selection:

```
suite selects 40 files; of those, under tests/probe/defect/: 0
```

Three are named in `EXPECT_EXEMPT` and *are* re-derived every run by `check_exemptions_live`. The other **21 carry an `expect-exit:` or `expect-error:` marker that no stage asserts**. `check_expect_headers` only checks the header is well-formed; `run_parse` only checks the parse-phase code family (`stages.parse_verdict` never compares the non-parse codes it saw against `e.errors`).

Among the 21:

```
derive_payload_enum/case2_ord_ignores_payload.npk    expect-exit: 121   (O-N10 regression)
derive_payload_enum/case3_hash_and_clone.npk         expect-exit: 107   (O-N10 regression)
view_escape/case1..case5                             expect-error: NITPICK-BORROW-001  (O-N9)
missing_failsafe/case1, case3                        expect-error: NITPICK-REACH-003   (O-N11)
generic_element_move/case1, case5                    expect-exit: 0     (the TM-137 fix)
generic_owning_copy/case2                            expect-error: NITPICK-TYPE-046
generic_owning_copy/case5_vec_at_destructive.npk     expect-exit: 11
```

This is the repository's entire regression corpus for four discharged compiler defects, and it asserts nothing. The inversion is sharp: the three files *exempt* from having an expectation get their verdict re-derived on every run; the 21 that *have* one do not.

It also explains why A4 is survivable — `case1_generic_move_out.npk`'s and `case5_generic_drop_loop.npk`'s brand-new `// expect-exit: 0` markers, which would be wrong at `0dfddac`, are inert.

`meta/specs/TESTING.md:50` describes the coverage as "every `.npk` is under `src/` (judged by 'it compiles'), or under `tests/` with an `expect-` marker of its own or a NAMED exemption" — which reads as coverage and is, for 21 files, membership in a bucket nobody evaluates.

**Resolves:** either a `[[test]]` entry per `defect/` subdirectory with the reason recorded, or an extension of `check_exemptions_live`'s verdict re-derivation to every `defect/` file (it already does exactly this work for three of them).

## B3 — other lists with the `EXPECT_EXEMPT` shape (weak point 2, swept and read)

Candidate sweep: `git grep -n 'EXEMPT\|EXPECTED\|KNOWN_\|SKIP\|PENDING\|ALLOW'` over 79 tracked `.md`/`.py`/`.toml` files gave 6 named tables. All 6 read:

| List | Location | Verdict |
|---|---|---|
| `EXPECT_EXEMPT` | `harness/run.py:81` | fixed at 0.0.5 (TM-137). Clean. |
| `CITATION_EXEMPT` | `harness/checks.py:660` | **two problems, below** |
| `HOST_ISOLATION_EXEMPT` | `harness/checks.py:592` | one entry, `src/lib.npk`, re-derived by construction. Clean. |
| `checks.PENDING` | `harness/checks.py:804` | four entries, each with a cycle. Not diffed against `TESTING.md` §2's pending table — nothing would notice if they disagreed (and they do; see D4). |
| `CALIBRATION` | `harness/selfcheck.py:706` | numbers 4/5/8 re-measured against `NITPICK-REACH-003` every run. **Exemplary** — this is the shape the others should have. |
| `manifest.KNOWN/DECLINED/WHOLE_TREE_STAGES` | `harness/manifest.py:90-114` | refuse by name in every direction. Clean. |

`CITATION_EXEMPT`'s two problems:

- **The whole-file entry can never expire.** `checks.py:737-739`: `if (rel, None) in exempt: excused.add((rel, None)); continue`. The `("harness/selfcheck.py", None)` exemption is marked excused as long as the file exists — the reason ("it contains DELIBERATELY dangling citations") is never re-derived. That is TM-137's shape exactly: the mechanism checks that the file exists, not that its reason holds. The same file's own table already argues against this for `checks.py` itself ("Exempting the whole file would stop the dozen REAL citations in it being checked") and then does it anyway one entry up. `selfcheck.py` cites V-14, V-15, D-179, D-237, TM-107, TM-112, TM-120, TM-126, S-1, S-4b, B-10 — none is checked.
- **The close will break two entries silently.** `0.0.6.md` step 7 is `git mv meta/roadmap/0.0 meta/roadmap/done/0.0`. `CITATION_EXEMPT` is keyed on repository-relative **paths**, and two of its four keys are `meta/roadmap/0.0/0.0.0.md` and `meta/roadmap/0.0/0.0.3.md`. After the move both become stale — and because `check_specs_current` **reports and never fails**, the run stays green. More broadly, `git grep -l 'roadmap/0\.0/\|0\.0/0\.0\.[0-9]'` gives **48 sites across 20 files**, two of them mechanisms (`harness/checks.py`, `harness/repro.py`) rather than prose. `/npk:check` will catch the 16 relative markdown links; it will not catch the Python keys or the citations inside `.npk` headers.

---

# C. Numbers that are derived rather than measured, and nothing would catch them (weak point 3)

Every number below was re-measured. The denominators: 165 tracked `.md`/`.py`/`.toml`/`.npk`/`.txt` files opened; 77 `.npk` files walked; 51 distinct compiler decisions checked over 420 citation sites.

## C1 — the whole-tree denominators moved from 50 to 77 and no live document followed

Measured now, replicating `run.py`'s own walk and `stages.read`:

```
total .npk in tree: 77   = 10 src/ + 67 tests/ + 0 elsewhere
library entry reaches: 4          suite roots: 40
reached by `use` from a suite root but not themselves roots: 3 (the probe11 support modules)
rooted by NOTHING but the parse stage: 30      (77 = 4 + 40 + 3 + 30)
tests/probe/*.npk non-recursive: 32   =  25 `expect-exit:` + 7 `expect-error:`
```

Every live document still carries the 0.0.3 figures. 11 sites in 6 files (roadmap execution records are excluded — those are history and correctly frozen):

| Site | Says | Is |
|---|---|---|
| `harness/run.py:453-461` | `50 = 1 + 27 + 3 + 19` | `77 = 4 + 40 + 3 + 30` |
| `harness/run.py:457` | "six ... placeholders, which `src/lib.npk` does not reach because it re-exports nothing yet"; "thirteen are the reproductions" | lib.npk re-exports 35; 24 reproductions |
| `harness/run.py:549` | "exactly the twenty-six probe programs" | 32 |
| `harness/stages.py:6` | "the nineteen files carrying `expect-exit:` and the seven" | 25 and 7 |
| `harness/stages.py:362` | "the twenty-six files in this tree that must NOT compile" | 15 carry `expect-error:` |
| `meta/specs/BUILD.md:155` | "the 19 files carrying `expect-exit:`" | 25 |
| `meta/specs/BUILD.md:232-236` | "twenty-six files here that must not compile"; "50 files = 36 + 13 + 1" | 15; 77 |
| `meta/specs/TESTING.md:20` | "the 19 files of 50 that no other stage roots" | 30 of 77 |
| `nitpick.toml:61,74,95` | "nineteen positive probes and seven"; "exactly the twenty-six"; "RE-MEASURED AT 0.0.2 AND CONFIRMED: 26 files, 19 and 7" | 25 and 7; 32 |
| `meta/OPEN_QUESTIONS.md:575` | "nineteen today" | 25 |

Nothing would catch any of these. The harness *prints* every denominator on every run (V-1b), and no document is diffed against the print. The cheapest durable fix is a check that reads the numbers out of these files and compares them to the sweep — the same shape `check_error_budget` already uses on `SAFETY.md` §2.

## C2 — `TESTING.md` V-1a's arithmetic does not close, and the row that falls out is the uncommissioned one

`meta/specs/TESTING.md:58-65`: *"Nine of the fourteen above are live as of cycle 0.0.3 ... The other four print on every run as `PEND`."* §2's table has 14 rows and 4 are pending, so 10 are live — 9 + 4 = 13. The missing row is `check_expect_headers`, which `run.py` counts as step 4 rather than as a tree check. `harness/README.md:103-105` repeats the same 9 + 4. The row that vanishes from the count is the same row V-14c is false about (A5). Its own arithmetic falsifies it.

## C3 — "eight ways", printed on every run, is seven

`harness/run.py:686` prints `this runner has been shown able to fail eight ways (V-14).` Case 6 is `PEND` until 0.5 (`selfcheck.py:806-818`), so seven faults are planted. Same overstatement at `harness/run.py:7`, `.github/workflows/ci.yml:48` ("eight faults planted in scratch trees, each requiring a RED run"), `CLAUDE.md` ("plants eight faults"), `harness/README.md:116`. `meta/roadmap/0.0/README.md:169` (the Gate) says **seven** and is the only one right.

Related, in the same line of output: `selfcheck.py:836` prints `"%d planted violation(s) caught, %d clean control(s) silent" % (len(PLANTED), len(PLANTED) + 1)` — nine plants, ten controls, from nine `PLANTED` rows each with one control.

## C4 — `manifest.py:86` says "`BUILD.md` §3 lists nine"; the table has eight rows

`meta/specs/BUILD.md:123-132` lists `compile, parse, accept, check, program, golden, sweep, fixture` — eight, which is also `len(KNOWN_STAGES)` in the same file. The four "further stages ... deliberately absent" (`resolve`, `runtime`, `verify`, `cost`) are outside the table and outside `KNOWN_STAGES`.

## C5 — `harness/README.md`'s cost table is a factor of four out, and `CLAUDE.md` points readers at it

`harness/README.md:112-120`: self-check 78.3 s, parse (50 files) 40.1 s, suite (27 units) ~61 s, **full invocation 184 s**. `meta/roadmap/0.0/0.0.5.md:248` records `GREEN -- 40 unit(s), 0 failures; 5 pending, 43.1 s` and `CLAUDE.md` says "40 units green in about 42 s ... It was 241 s at `0dfddac`". `CLAUDE.md` also says "`harness/README.md` is the guide and carries the cost table". Both the wall times and the two denominators (50 files, 27 units) are pre-0.0.4.

## C6 — three live files still say the library computes nothing

Identical sentence in three places, false since 0.0.4:

- `harness/run.py:20-21` — "IT IS NOT evidence that the LIBRARY works. There is none yet; `src/` is placeholders. The first computation is `src/core/` at 0.0.4."
- `harness/README.md`, "What a green run does NOT mean" — same.
- `.github/workflows/ci.yml:37-44` and `:56-58` — "`src/` is six placeholder modules and an empty umbrella" (twice).
- `harness/checks.py:461-465` (`check_no_owning_fields`'s docstring) — "`src/` holds six placeholders and one umbrella; there is no table and no struct" — there are two structs.
- `harness/checks.py:227-231` (`check_layering`) — "It is 1 today because `src/lib.npk` re-exports nothing yet" — it is 4.
- `src/lib.npk:22-27` — "EMPTY TODAY, AND THAT IS THE POINT ... Because this file re-exports nothing" — the same file re-exports 35 names 40 lines below.

**Verified clean, for contrast:** every headline number I could re-derive is right. `limits.npk`'s four range constants recomputed independently with Hinnant's `days_from_civil` give `-4371588`, `2932896`, `-377705203200`, `253402300799` — all four match, and the three relations the file states hold. The tzdb arithmetic closes: `434928 + 20104 + 12516 + 6592 + 866 = 475006`; `+14304 = 489310`; `512000 − 489310 = 22690`; `22690 / 16 = 1418` rows; the estimate `322056 + 19872 + 7152 + 7039 = 356119`; `133191 / 356119 = 37.4%`. `BUILD.md` B-2b's "113 symbols" is 113 at **both** pins (`elf.runtime_allowlist` = 111 defined globals ∪ `{main, npk_failsafe}`).

---

# D. Inherited rather than re-derived (weak point 4)

## D1 — `0.0/README.md` claims an assertion that the tree does not contain

`meta/roadmap/0.0/README.md:71`, a ticked `[x]`:

> "All seven `src/` files compile at 844 793 B of IR, and `harness/run.py` **asserts the count is at least 7**, because a directory whose placeholder was deleted rather than replaced is invisible to the sweep"

```
$ grep -n 'at least\|>= *7\|len(in_src)\|MIN_SRC' harness/*.py
harness/run.py:281:            "tests/ + %d elsewhere" % (STEPS, len(files), len(in_src),
harness/run.py:297:    if len(in_src) + len(in_tests) + len(orphan) != len(files):
```

There is no minimum. The 0.0.2 rewrite ("replaced `harness/run.py`, not extended it", `0.0/README.md:105`) dropped it, and nothing noticed — the stated failure mode is live today. This is a rule stated as enforced and unenforced, in a ticked acceptance item, which is the class the audit skill calls dormant.

## D2 — `src/core/limits.npk` names a consumer that does not consume it

`src/core/limits.npk:113`: *"and `src/core/bytes.npk` sizes its stack buffer with this name."* `bytes.npk:144`: *"The bound is `NTIME_DIGITS_MAX`, which is the better spelling regardless."*

```
$ git grep -n 'uint8\[20\]' -- src/
src/core/bytes.npk:148:    uint8[20]:digits = ...
src/core/bytes.npk:209:    uint8[20]:digits = ...
```

`NTIME_DIGITS_MAX` appears nowhere in `bytes.npk`'s code (comments stripped), and `bytes.npk:54`'s `use "./limits.npk".*;` imports nothing that is used. The whole point of `limits.npk` — "EVERY ONE OF THEM, IN THIS FILE AND NOWHERE ELSE" — is defeated at the one site the file itself names, and `check_constants_named` cannot see it: `_NUMBER` requires four or more digits, and `CONSTANT_OWNER` has no entry for `20`.

## D3 — `SAFETY.md` contradicts itself about O-N17, 50 lines apart

- `meta/specs/SAFETY.md:546` (**S-18d**, TM-136): *"**O-N17 is fixed** at pin `aaffb87` — all five reproduction cases link and run."*
- `meta/specs/SAFETY.md:593-597` (**S-18c**'s blockquote): *"**The remedy is not available generically today.** A generic `vec_set<T>` that moves the outgoing element into a dying local is accepted by `npkc` at exit 0 and refused by `llc` — `../OPEN_QUESTIONS.md` **O-N17**"*

Both are live rules in the authority document. The second is false at the current pin. The correct current statement is TM-136's: the generic remedy is unavailable for a *different* reason (`NITPICK-MOVE-001` on the hoisted-slice loop), which is the whole point of the 0.0.5 finding.

Sweep denominator: 71 `O-N17` sites in 22 files, all read. The other 69 are correct or are frozen history. `meta/DECISIONS.md:2058`'s copy is inside settled TM-127 and is correctly frozen — but see D5.

## D4 — the specification's pending list and the harness's have drifted apart with nothing between them

`meta/specs/TESTING.md:67-72`'s pending table and `harness/checks.py:804`'s `PENDING` tuple carry the same four entries today, and nothing diffs them. `TESTING.md` §2's 14-row table and `checks.LIVE` + `checks.PENDING` + `check_expect_headers` + `check_exemptions_live` are likewise undiffed — which is why C2's count could be wrong and stay wrong, and why A5's missing row is invisible.

## D5 — TM-127 and TM-132 carry no supersession note, though the repository names the pattern

`CLAUDE.md`: *"A settled decision's text is never rewritten. Supersede it with a new numbered decision that says why (the compiler's D-085/D-202 pattern)."*

The compiler follows that pattern in its headings — 11 of 266 `## D-` headings carry an "amended by"/"superseded" note, e.g. `D-014 — ... **SETTLED; D-163 adds what a `defer` BODY may do**`. In `nitpick-time`, **0 of 68** `### TM-` headings do. TM-127 (`meta/DECISIONS.md:2010`) and TM-132 (`:2347`) both rest on a pre-fix reading of O-N17 and neither points forward to TM-136 (`:2634`). A reader arriving at TM-132 — the decision that restricts `Vec<T>` — gets the superseded reason with nothing to follow.

---

# E. Cross-repository and cross-document

## E1 — O-N18 and O-N19 exist in the workbench registry and in the compiler's backlog; this repository carries neither

```
$ git grep -n 'O-N18\|O-N19'        # nitpick-time, 175 tracked files
meta/roadmap/0.0/0.0.4.md:540:  ... Recommend O-N18 and a relay to the compiler session
```

That is the *request*, in a frozen execution record. The workbench registry has both:

- `meta/OPEN_QUESTIONS.md:156` — **O-N18**, `.len` on a fixed-size array
- `meta/OPEN_QUESTIONS.md:110` — **O-N19**, `NITPICK-TYPE-046` not enforced inside a generic body
- `BOARD.md:212` — "**O-N18 is their DEF-22**"; `:219` — "**O-N19 IS ACCEPTED AS A SOUNDNESS HOLE IN THE CHECKER**"

`nitpick-time/meta/OPEN_QUESTIONS.md` carries O-N1…O-N17 and stops. The two defects this cycle raised are referenced in the harness and in `SAFETY.md` S-18d only by path ("a SECOND compiler defect", "a THIRD compiler defect"), so from inside the repository their status is unfindable. The precedent is O-N17, which *is* carried locally at `meta/OPEN_QUESTIONS.md:579`.

Worth carrying with them, from `BOARD.md:252`: **O-N18 is fixed in 1.5.2e**, which is not yet the pin. When the pin moves, `check_exemptions_live` will fire on `fixed_array_len/case1_local_array_len.npk` (`npkc` → `run:0`) — that is the mechanism working, and the close should expect it rather than be surprised.

## E2 — `src/core/vec.npk:109` cites the wrong decision (unverified claim, resolved by reading the source)

```
// `Ord` derives in declaration order (D-051), so field order is semantic
```

At the pin, `D-051` is *"No `ostring`; portability lives in a `Path` type above `nlibc`"*. The rule cited belongs to **D-123**:

```
$ git -C ../nitpick show aaffb87:meta/specs/DECISIONS.md | sed -n '9028p;9040p'
| `Ord`, `PartialOrd` | lexicographic comparison in **declaration order** | ...
**`Ord` compares in declaration order.** It is the standard answer and it has a
```

`meta/specs/SAFETY.md:28` already cites this correctly (to `TRAITS_REFERENCE §2.5`), so the mis-citation is isolated to one site. `check_specs_current` cannot see it by design (`checks.py:632-636`: compiler `D-nnn` are "cited here by number and verified by reading"), which is exactly why it survived.

**Denominator for this class:** 51 distinct compiler decisions over 420 citation sites; all 51 resolve to a real heading at `aaffb87`; I read the heading of all 51 and the body of 8 (D-051, D-123, D-151, D-183, D-236, D-247, D-076, D-209). One mis-citation found.

## E3 — the allowlist figure differs between the board and this library, and both are right

`BOARD.md:610-613` records the compiler's own reconciliation: *"the allowlist is now the runtime's **exports**: 112 entries with `main`"*. `meta/specs/BUILD.md:92` says **113**. Measured, both are correct about different lists: `defined_globals(npkrt.o)` = 111 at both pins, plus `main` = 112 (the compiler's), plus `npk_failsafe` = 113 (ours, because a library object legitimately references it). B-2b explains the second half but does not name the 112 it will be diffed against. One sentence in B-2b would stop this number travelling — which is the board's own stated reason for writing the reconciliation down.

---

# F. Smaller items, all evidenced

| # | Location | Finding | Severity |
|---|---|---|---|
| F1 | `src/core/vec.npk:262-267` | *"`cap == 0` is the ownership bit that matters, and it is what a later `vec_free` of the same value would read."* `vec_free`'s body reads no field before `dalloc`. Measured: single free exit 0; free-then-push-then-free exit **95** (`Unreachable`). The runtime contains it; the stated mechanism is not the one that does. | contradiction |
| F2 | `meta/specs/SAFETY.md:415` vs `src/core/vec.npk:180`, `src/core/bytes.npk:97,109` | S-17c's rule reads *"over `count`, never over `cap`"*; three sites use `cap`. The exception is argued in source comments, not in an amendment — which `CLAUDE.md` forbids ("never by a comment"). S-18c carves out `vec_push` for the *drop* obligation only. | contradiction |
| F3 | `src/core/core.npk:6,11` | *"It is REPLACED at the cycle below, never deleted. WHEN: cycle 0.0.4"*. 0.0.4 is done; the placeholder survives beside the three real core modules. `CLAUDE.md`'s "the other five directories are still placeholders" counts directories and silently omits it. | stale |
| F4 | `meta/specs/VERIFICATION.md:77` | Row states the `Vec<T>` `at`/`set` obligation as `index < count`. `meta/specs/SAFETY.md:404-408` says that is incomplete and that it was *"corrected there at cycle 0.0.4"* — in `0.0.4.md`, not in the specification. A specification known to be wrong, left standing, with the correction in a roadmap file. | contradiction |
| F5 | `meta/specs/BUILD.md:322` | B-15's prefix list is `cal_`, `span_`, `zone_`, `fmt_`, `host_`. `src/core/` ships `vec_*`, `bytes_*`, `NTIME_*` and no `core_`. B-15 predates `src/core/` and was not amended; nothing checks it. | dormant |
| F6 | `meta/specs/SAFETY.md` | S-18d (line 543) is placed **above** S-18c (line 566). Cosmetic, but it is why the two contradicting paragraphs read as one argument. | cosmetic |
| F7 | `meta/roadmap/0.0/README.md:137` | `[ ] the hook for the real gate` (the `NPK_HEAP_STATS` `peak_live` assertion) is the cycle's one unticked box, and `0.0.6.md`'s checklist does not carry it forward. It will close by falling off the list unless 0.0.6 says where it goes. | dormant |
| F8 | `tests/probe/probe11e_unused_import_refused.npk` | The file name says "unused import refused"; the refusal is `NITPICK-REACH-002` about arms owed by an import, and the file's own prose says so. A name wider than its subject — noted because `src/core/bytes.npk:54`'s genuinely unused import is not refused, and the file name invites the opposite conclusion. | cosmetic |

---

# What I checked and found clean

So the next auditor knows the covered ground.

**Compiler claims re-verified at `aaffb87` (read-only, never in the working tree).** All 51 cited `D-nnn` resolve to real headings at the pin, across 420 citation sites; one is mis-cited (E2). Read in full and confirmed: **D-151** counts wild-role blocks only — `alloc`/`calloc`/`ralloc`/`aalloc`, with runtime-internal storage explicitly outside the set — so TM-106's claim is exact; and the compiler's own **S-39** (`aaffb87:meta/roadmap/OPEN_DECISIONS.md:162`) names *"the workbench's `Vec<T>`, its P-23"* and rules that D-151 keeps counting every `wild` block, so `vec.npk:270-273`'s exit-trap guarantee survives the 1.5.2e change. **D-183** does carry the `0xAA` poison (line 12946), so `run.py:120-128`'s citation is right. **D-236** (source paths relative to the manifest root) is what makes `repro.py`'s claim true, and I confirmed it in the artefact: `build/lib.repro-a.ll` and `.repro-b.ll` are byte-identical at 78 572 B and the embedded site paths are `src/core/bytes.npk`, not absolute — so 0.0.5's 14-byte caution and repro's claim are compatible, not contradictory.

**External claims re-verified at their primary source, at the exact tag.** `LLVM-20.1.2-Linux-X64.tar.xz` exists on `llvmorg-20.1.2` at 2 021 628 328 B; it is a full CPack install, so `llc`, `opt`, `ld.lld` and `llvm-config` are present; and it is built without `PACKAGE_VENDOR`, which is A3.

**Arithmetic.** The four calendar bounds recomputed independently from Hinnant's algorithm — all four exact, and `limits.npk`'s three stated relations hold. The tzdb table sums, the POSIX_RULES delta, the 512 000-byte budget, the 22 690-byte margin, the 1 418-row headroom and the 37% gap all close. B-2b's 113-symbol allowlist measured at both pins.

**Harness behaviour, measured rather than read.** All eight live tree checks run clean at HEAD with sane denominators (`check_specs_current`: 1 930 citations over 151 files, 257 declared rules, **0 unresolved, 0 stale exemptions**). The `check_expect_headers` buckets sum, and the six files with no marker are exactly the six `EXPECT_EXEMPT` entries. The manifest schema refuses `parse` (whole-tree), `accept` (declined) and `fixture` (unimplemented) **by name** in every direction, as documented. `selfcheck.py`'s nine planted violations and their controls do behave as claimed for the seven checks they cover.

**Pin portability.** The library and all eight runnable suite members I built at the CI pin `0dfddac` produce the correct artefacts and exit codes, including `vec_pop<T>`'s new `move`, which had never been compiled there.

**Not a finding, as the dispatch said:** the repository is ahead 5 of origin by design.
