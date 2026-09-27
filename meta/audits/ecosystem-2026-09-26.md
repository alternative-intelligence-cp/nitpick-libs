# Ecosystem-wide audit — after the third cycle close (W-22)

**Filed by the orchestrator under W-22**, 2026-09-26 — the first ecosystem-wide audit, owed after the third close (`nitpick-time` 0.0,
`nitpick-regex` 0.0, `nitpick-time` 0.1), dispatched at the author's word. The auditor wrote nothing; this file is its final message,
reproduced below the line — extracted from its transcript by script, not retyped — **inside a fence, with two mechanical changes and no
other**: (1) the message is fenced, because it quotes library-local question ids, which at workbench scope collide across repositories
(`meta/OPEN_QUESTIONS.md`, *"Library questions this board cites"*: quoted evidence belongs in a fence), and its 14 inner fence lines
are re-marked `~~~` so they do not close the outer one; (2) 0 empty-bracket-then-parenthesis pairs spaced (none here). It cites no
absolute path. **Each finding names its owning repository, which triages it at its next dispatch**; the workbench's own are this seat's.

**Scope** all nine trees and the compiler at the pin `c970483` · **agent** `npk:auditor` on `opus` (`eco-audit-2026-09-26`), ~21 min, 349 k tokens.

## What the orchestrator verified before filing

- The report's summary: **23 findings** — 12 contradiction, 1 unverified claim, 3 dormant, 4 stale, 3 cosmetic; verdict: sound where
  exercised; EC1, EC4, EC5 and EC12 fixed before the owning repository's next dispatch; PLAYBOOK §2 and §3 (EC2, EC3) corrected before any
  new plan is written from them.
- **EC1, spot-checked:** the pin's `runtime/npkrt.ll` carries the SIGPIPE disposition (line 2084, *"SIGPIPE (13; DEF-68, 1.5.8 step 3)"*)
  and installs `@npk_pipe_handler` (line 2091, defined at 2111).
- **EC7, spot-checked:** `mod:raw;` compiled with the pinned `npkc` is `NITPICK-RESOLVE-012`, exit 1.

---

```markdown
# Audit: the ecosystem after the third close (W-22)

- **Scope:** all nine trees, plus the compiler at pin `c970483`. Every compiler claim below was read with `git -C nitpick show c970483:<path>`. The one exception is labelled as a forecast read from the compiler's HEAD.
- **Toolchain:** `nitpick-libs/.internal/toolchain/c970483/` (written `$PIN` below). `sha256sum -c` gives `npkc: OK` and `npkrt.o: OK`. Control pins: `c3bdae2` and `3d15ac9`.
- **Nothing written.** Scratch programs were built only in the session scratchpad (`$SCRATCH`). All paths below are relative to `REPOS/`.
- **Trees clean.** All nine trees and `nitpick` had empty `git status --porcelain` at the start and at the end.
- **The workbench moved during the audit.** It went from `20888bd` to `e7abd27`: the orchestrator's own board commits `b6d120b` and `e7abd27`. `BOARD.md` line numbers below are at `e7abd27`.
- **No harness was run.** `free -g` showed 139–140 GiB available.
- **Mechanical checks:** `check_refs` is clean on 8 of 9 trees. The ninth is EK3.

**Summary: 23 findings.** 12 contradiction, 1 unverified claim, 3 dormant, 4 stale, 3 cosmetic.

- **EC1 and EC2 break `nitpick-posix`'s plan at the pin.** The SIGPIPE premise no longer holds, and its control probes no longer compile.
- **EC5 and EC6 are regex harness checks that pass planted violations.** Neither has any instance in the tree today.

---

## Contradiction

### EC1: "The runtime installs no signal disposition" has been false since `c3bdae2`, and `nitpick-posix`'s PX-011 cannot be built as written

**Location:**
- `nitpick-apps/nitpick-posix`:
  - `meta/DECISIONS.md:116-124` (PX-011: "`yes` dies of `SIGPIPE` … exit status 141")
  - `meta/specs/SAFETY.md:136-150` (S-7)
  - `meta/roadmap/0.0/README.md:72` (probe 05: "the process must die of signal 13")
- `nitpick-apps/APPS.md:79-93`: "the runtime installs none, so every signal's default is live".
- `nitpick-libs/LIBRARIES.md:174-179`.
- `nitpick-tui`: `meta/DECISIONS.md:725-727` and `meta/specs/TERMINAL_MODEL.md:279-283`.
- `nitpick-sockets`: `meta/specs/SAFETY.md:17`, `CLAUDE.md:38`, `README.md:25`, `CONTRIBUTING.md:33`, `meta/DECISIONS.md:137-138`, `meta/roadmap/ROADMAP.md:40`, `meta/roadmap/0.0/0.0.0.md:154`.
- Only `nitpick-libs/PLAYBOOK.md:74` carries the correction.

**Evidence:**
~~~
$ git -C nitpick show c970483:runtime/npkrt.ll | sed -n '2084,2091p;2109,2113p'
  ; SIGPIPE (13; DEF-68, 1.5.8 step 3): a write to a pipe or socket whose reader
  ; is gone raises it in the writer, and its default action KILLS the process
  ; ... A handler that returns turns it into the value it always was: the write answers EPIPE.
  %r5 = call i64 @npk_sys6(i64 13, i64 13, i64 %ap, i64 0, i64 8, i64 0, i64 0)
define internal void @npk_pipe_handler(i32 %sig, ptr %info, ptr %uc) { entry: ret void }
$ git -C nitpick show c970483:tests/backend/programs/sigpipe_epipe.npk > $SCRATCH/s.npk
$ $PIN/npkc s.npk -o s.ll && llc -O0 -filetype=obj -relocation-model=static s.ll -o s.o \
    && ld.lld -static s.o $PIN/npkrt.o -o s && ./s; echo "exit=$?"
exit=32        # the write answered EPIPE; the process was not killed
~~~

**Impact:** The floor installs the handler before `main` runs, so "leave `SIGPIPE` at default" is not available to a Nitpick program. Under PX-011, `yes | head` would get `EPIPE`, not exit 141. Probe 05 as specified will fail.

The conclusions of `ntui` (T-113, block it) and `nsockets` (SK-013, `MSG_NOSIGNAL`) still hold. Their stated premise is wrong. APPS.md's rule, "know what the default is", is the one that got this wrong.

**Resolve:**
- `nitpick-posix` must decide again:
  - either reset `SIGPIPE` to `SIG_DFL` through a raw `sys(13, …)` before the utility's work;
  - or treat `EPIPE` on stdout as a clean exit, stating the status.
- Fix probe 05's expectation, and correct PX-011 and S-7.
- The workbench (`LIBRARIES.md`) and `nitpick-apps` (`APPS.md`) re-date their rows.
- `nitpick-tui` and `nitpick-sockets` re-date their premise sentences.

**Owners:** `nitpick-posix` (primary), `nitpick-apps`, `nitpick-libs`, `nitpick-tui`, `nitpick-sockets`.

### EC2: PLAYBOOK §2 and three unstarted libraries say every index traps (D-070); at the pin a pointer index does not

This extends the time audit's C4 to the workbench.

**Location:**
- `nitpick-libs/PLAYBOOK.md:53`: "indexing is bounds-checked and traps | D-070 | an out-of-range index is a crash, not corruption".
- `nitpick-parse/meta/specs/SAFETY.md:22`, `nitpick-sockets/meta/specs/SAFETY.md:28`, `nitpick-tui/meta/specs/SAFETY.md:24`.

**Evidence:**
~~~
$ git -C nitpick show c970483:meta/specs/DECISIONS.md | grep -n '^## D-070'
4919:## D-070 — `T[]` is a slice: bounds live in the array type, not the pointer type — **SETTLED**
$ git -C nitpick show c970483:src/backend/ir/ir_expr.npk | sed -n '9789,9793p'
        // A SLICE'S BOUNDS LIVE ON IT AND ARE CHECKED HERE (0.9.2, D-070):
        // ... where OOB detection COMES FROM, since pointers are thin (D-038) and carry nothing to check.
$ grep -n -i 'RX-111\|unchecked index\|pointer.*index' nitpick-libs/PLAYBOOK.md    # (no output)
~~~

`nitpick-regex`'s own check says the opposite of PLAYBOOK §2 (`harness/treecheck.py`, `check_accessor_confinement`'s docstring): "an out-of-range index in either READS AND RETURNS A HEAP WORD at exit 0 -- probe 08b measured 7 992 bytes past the allocation".

The three library sites are on the board as RX-111 carries ("Three remain: `nitpick-tui`, `nitpick-parse`, `nitpick-sockets`"). **PLAYBOOK §2 is on no list.** It is the page every new plan starts from.

**Resolve:** restate the §2 row to D-070's scope (slices, fixed arrays, SIMD lanes, `List`), and add the bare-pointer residue as a library obligation.

**Owner:** `nitpick-libs`. The three library SAFETY.md rows keep their existing carry.

### EC3: PLAYBOOK says every declared public `error:` is an arm; the pin charges raise sites, including private ones

**Location:**
- `nitpick-libs/PLAYBOOK.md:48`: "every public `error:` you declare is an arm every consuming program owes".
- `:337-338` (§3 item 5, the check shape it prescribes): "the count and names of public `error:` declarations".

**Evidence** (programs in `$SCRATCH`, each importing one module and declaring no `failsafe`):
~~~
# module: `pub error:ERegexPattern; pub error:EOther;`  — declared, never raised
NITPICK-REACH-003 ... -- 6 identities: Unreachable, HeapOom, HeapBadRequest, WildLeak, StackExhausted, MachineFault --
# module m: `error:EPriv;` (PRIVATE) and `pub func:f … { if (x < 0i64) { fail EPriv; } … }`
NITPICK-REACH-003 p.npk:3:1: ... -- 7 identities: m.EPriv, Unreachable, HeapOom, HeapBadRequest, WildLeak, StackExhausted, MachineFault --
~~~

A consumer can name the private identity: `(EPriv)` and `(m.EPriv)` both compile, exit 0. So a declaration costs nothing until it is raised, and a private raise site costs an arm.

`nitpick-time`'s TM-203 already left this shape. It counts `(pub )?error:` keyed by (module, name) (`nitpick-time/harness/checks.py:303`, `:360+`). `nitpick-time/harness/arms.py:12-18` records the declared-but-unraised half at `c3bdae2`.

**Resolve:**
- Restate the §2 row as "every identity a reachable `fail` site raises, public or private".
- Make §3 item 5 prescribe TM-203's shape plus a private-declaration rule.

**Owner:** `nitpick-libs`.

### EC4: `nitpick-regex`'s `check_error_budget` passes three planted extra identities

This is related to the time audit's C2, but it is not C2's shape: C2's own case, one name declared in two modules, is caught in regex.

**Location:** `nitpick-regex/harness/treecheck.py:86-87` (`_PUB_ERROR` and `_ANY_ERROR`, each matched with `re.match` per blanked line) and `:246-288`. `SAFETY.md:156-165` (S-8) says "Importing `nregex` costs your program's `failsafe` exactly one arm", and the docstring says "This check is what keeps the promise true".

**Evidence** (`python3 -B`, the harness imported read-only, trees in `$SCRATCH`):

| Plant | Result |
|---|---|
| `pub error:ERegexPattern;` in `api.npk` + `error:EInternal;` with a `fail EInternal` site in `core.npk` | `failures: []`, note "1 public and 1 private" |
| `pub error:ERegexPattern; pub error:EOther;` on one line | `failures= 0`, "1 public" |
| `pub error:ERegexPattern;` then `pub⏎error:EOther;` | `failures= 0`, "1 public and 1 private" |
| **Control:** `pub error:ERegexPattern;` in both `api.npk` and `core.npk` | **RED**, "the public error budget is 2 identity/identities" |

Every planted form compiles at the pin. From EC3, the private one charges every importer `core.EInternal`.

**Exposure today: none.** `src/` declares only `api.ERegexPattern` (`src/api/api.npk:32`) and has no `fail` site.

**Resolve:** read the whole blanked text rather than per-line `match`, count private declarations, and plant all three shapes.

**Owner:** `nitpick-regex`.

### EC5: regex's "only bounds check" misses spaced forms of the accessors it confines

This extends the time audit's C12. Time's version handled whitespace before `[`; regex handles whitespace on neither side.

**Location:** `nitpick-regex/harness/treecheck.py:438-441` (`_ACCESSORS = (".items[", …), (".ptr[", …)`, matched with `line.find`). `meta/specs/TESTING.md`'s row calls it "the only bounds check this library has".

**Evidence:**
~~~
# $SCRATCH/ptrsp.npk:  uint8:c = s.ptr [1i64];   uint8:d = s.ptr⏎    [2i64];
$ $PIN/npkc ptrsp.npk -o p.ll; ... ./p      →  npkc=0  run=0
# plant tree: src/syntax/cursor.npk holding `s.ptr [1i64]`, `s.ptr⏎[2i64]`, `v . items [0i64]`, `v.⏎items[0i64]`
check_accessor_confinement → failures: []
# control: the same file holding `s.ptr[1i64]` → control failures: 1
# regex src/ today, blanked by lexical.py, pattern \.\s*(ptr|items)\s*\[ :
exact-form sites: 15 spaced-form sites: 0
~~~

A `string`'s `.ptr` is not `hidden`, so unlike the time case, the compiler does not stop this outside the owning module.

**Resolve:** match `\.\s*(items|ptr)\s*\[` on blanked text, and plant the four shapes.

**Owner:** `nitpick-regex`.

### EC6: `nitpick-time`'s CI digest step contradicts the compiler's D-265 and regex's CI, and never prints the cross-machine claim

**Location:**
- `nitpick-time/.github/workflows/ci.yml:314-333`: "Byte-identical objects ACROSS machines … nobody has measured it … If a run shows them equal, a later commit may promote these four lines to an assertion". It prints `npkc` and `npkrt.o` only.
- Against `nitpick-regex/.github/workflows/ci.yml:222`: "S-42 measured it differing".

**Evidence:**
~~~
$ git -C nitpick show c970483:meta/specs/BUILD_REFERENCE.md | sed -n '303,313p'
- **The pin is a version, and a version is not a binary** (D-265 ...) ... **The claim that holds across
  machines is the compiler's own emission**, `build/npkc.ll`
# nitpick-time run 36274631237 (its close), job log via `gh api .../jobs/108494860501/logs`:
npkc   CI: 0cb4510d3f0fcb0eebe2f11c8202973e930159c60364b179bfe342624a616f13
npkc   WB: e4d95007018f313e5dabab5c69610b72dc0781eeb0f7b7414a6179b6e287c70e
# nitpick-regex run 36253106675, job 108434722898:
npkc.ll        28188736 bytes  d36a7e23cf02b11471022c596bc60afbe339d0d4a19b04b5c06031c515fe3183   (= PIN.md's row)
npkc            9751848 bytes  0cb4510d…
~~~

Time's CI will never see the two binaries equal: D-265 says they are not expected to be. Its promotion path therefore cannot fire. The one claim that does hold across machines, the emission, is not printed at all.

**Resolve:** port regex's step: print `npkc.ll` and name it as the claim, and drop the binary-equality premise.

**Owner:** `nitpick-time`.

### EC7: `nitpick-sockets` plans a module whose name is a keyword

**Location:** `nitpick-sockets` plans `src/option/raw.npk` in:
- `meta/specs/OPTION_MODEL.md:12`
- `meta/DECISIONS.md:317`
- `meta/specs/TESTING.md:132`
- `meta/roadmap/0.7/README.md:25`
- `meta/roadmap/0.0/0.0.3.md:74`

**Evidence:**
~~~
$ git -C nitpick show c970483:src/frontend/keywords.npk | grep -o '"[a-zA-Z_0-9]*"' | tr -d '"' | grep -x raw
raw
$ printf 'mod:raw;\npub func:f = int64(int64:x) { pass x; };\n' > $SCRATCH/raw.npk; $PIN/npkc raw.npk -o raw.ll
NITPICK-RESOLVE-012 raw.npk:1:1: file `raw.npk` declares `mod:;` first ...     exit=1 ll_written=no
# the same at 3d15ac9 and c3bdae2; control rawopt.npk: exit=0
~~~

`nitpick-regex` hit the same class (`nitpick-regex/meta/roadmap/0.1/0.1.0.md:40,82`: `error.npk` became `pattern_error.npk`). `PLAYBOOK.md` §10 (`:1348-1370`) presents reserved words as local names only, and never says a file's basename cannot be one (grep finds nothing).

**Resolve:**
- `nitpick-sockets`: rename the module, and the check name that cites it.
- `nitpick-libs`: add "a basename cannot be a keyword" to PLAYBOOK §10.

**Owners:** `nitpick-sockets`, `nitpick-libs`.

### EC8: W-17 and W-18 are contradicted by the fuzzer's practice, and no rule records that practice

**Location:** `nitpick-libs/WORKSTREAMS.md:184` (W-17: "Nothing is branched and nothing is merged") and `:187-191` (W-18: "A worker … never builds the compiler").

**Evidence:**
- `BOARD.md`'s tools table, row T1: fuzz sessions work their own branches (`local-m11`, `claude/fuzzing-session-milestones-…`), which this seat reviews and fast-forwards onto `main`. The M0–M4 run "built and commissioned both compilers", with "12 GB of toolchain under the gitignored `nitpick-fuzz/.work/`".
- `grep -c -i fuzz` returns 0 for each of `WORKSTREAMS.md`, `README.md`, `LIBRARIES.md`, `CLAUDE.md`, `skills/orchestrate/SKILL.md` and `skills/worker/SKILL.md`.
- `WORKSTREAMS.md` was last changed on 2026-09-06 (`97f0aad`). The fuzzer was created on 2026-09-25.

**Resolve:** a rule for tool repositories covering: who writes `main`, the branch-and-review merge, the order gate between milestones, and whether a session may build compilers.

**Owner:** `nitpick-libs`.

### EC9: W-18 says re-pins happen between cycles; both re-pins since the pause were taken mid-cycle

**Location:**
- `nitpick-libs/WORKSTREAMS.md:190-191`: "A re-pin happens between cycles".
- `skills/orchestrate/SKILL.md:86` says only "Never re-pin while any claim is in flight".

**Evidence:**
- `c3bdae2` was pinned on 2026-09-25 with `nitpick-time` in cycle 0.1. Its adoption was 0.1.0b.
- `c970483` was pinned on 2026-09-26 03:0x with `nitpick-regex` in cycle 0.0 (adopted at 0.0.4e) and `nitpick-time` in cycle 0.1 (0.1.4c).
- `RECORD.md`'s entries at 6405 and 7456-7480.

**Resolve:** restate W-18 as the practice: the orchestrator re-pins when no claim is in flight, and each repository adopts in an in-cycle subcycle.

**Owner:** `nitpick-libs`.

### EC10: "Q-6" has three meanings, which is the collision the registry already recorded once

**Location:** `nitpick-libs/meta/OPEN_QUESTIONS.md:48`, `RECORD.md:4552`, `BOARD.md:9438`.

**Evidence:**
- Registry Q-6: "work `nitpick-time`'s nine O-N4-unaffected probes, or idle the stream?"
- `RECORD.md:4552` (2026-09-06): "Q-6 — the `nitpick-time` CI pin bump", which is the board's row 6.
- `BOARD.md:9438` (2026-09-25): the row `~~**Q-6**~~`, "What replaces `VERIFICATION.md` P-1?"
- The registry's own lines 34-42 record this failure mode and say that `check_refs` cannot see it: "a re-used number resolves".

**Resolve:** renumber the board's P-1 question from the registry's next free Q number, and note the old label.

**Owner:** `nitpick-libs`.

### EC11: `nitpick-regex`'s check schedule disagrees with its own roadmap for two checks

**Location and evidence:** `nitpick-regex/meta/specs/TESTING.md`:
- `:213` says `check_inst_kinds_total` arrives at "cycle 0.4". `meta/roadmap/0.6/README.md:14,32` has it "live" at 0.6.1, and no 0.4 file names it.
- `:215` says `check_byte_class_partition` arrives at "cycle 0.7". `meta/roadmap/0.4/README.md:50` checklists "`check_byte_class_partition` live".

This was found by diffing every `check_*` name mentioned in the tree against the harness's definitions, the time audit's C3 method applied to regex. The other 13 undefined names are pending with agreeing cycles, or are external (`check_refs`, `check_record`, the compiler's `check_codes_tested`).

**Owner:** `nitpick-regex`.

### EC12: `nitpick-posix`'s control probes are refused at the pin, and its plan predates the floor of six

**Location:** `nitpick-apps/nitpick-posix/meta/roadmap/0.0/0.0.0.md:164-172`, whose §6 records 02b and 02f as "**ACCEPTED**, exit 70". `StackExhausted` and `MachineFault` appear 0 times anywhere in the repository.

**Evidence** (copies of `tests/probe/` in `$SCRATCH`):
~~~
probe02b_failsafe_handwritten: expect 70, npkc exit 1: NITPICK-REACH-002 ...:21:5: `failsafe` does not name `StackExhausted` ... [and `MachineFault`]
probe02f_decl_macro:           expect 70, npkc exit 1: NITPICK-REACH-002 ...:27:9: ... `StackExhausted` ... [and `MachineFault`]
probe02a / 02c / 02d / 02e / 02g: RESOLVE-002 / REACH-001 / REACH-001 / REACH-001 / MACRO-007 — as recorded
~~~

**Impact:** the chain's control, 02b ("so every failure below is attributable"), no longer controls. The generator's "system set" (`meta/specs/SAFETY.md:34-38`, S-2) is from before 1.5.8.

**Resolve:** at this repository's first dispatch, re-measure 0.0.0 §6 at the pin, add the two arms to the probes and to S-2's set, and date the verdicts.

**Owner:** `nitpick-posix`.

---

## Unverified claim

### EU1: `nitpick-posix` names POSIX.1-2017 as "the standard", with no digest behind it

**Location:** six files: `README.md`, `meta/DECISIONS.md`, `meta/roadmap/0.0/0.0.1.md` (×2), `meta/roadmap/0.0/README.md`, `meta/specs/ARGUMENTS.md`.

**Evidence:**
- `git grep -c -E '2024|Issue 8'` returns nothing.
- There is no `CURRENCY.md`.
- The Open Group publishes the next edition: "The Open Group Base Specifications Issue 8" ([pubs.opengroup.org/onlinepubs/9799919799](https://pubs.opengroup.org/onlinepubs/9799919799/)).
- Registry Q-1 (`meta/OPEN_QUESTIONS.md:10-17`) raised this on 2026-09-03 and is still open 23 days later, with no research digest.

**Owner:** `nitpick-posix`, through a PX- decision. The author owns Q-1.

---

## Dormant

### ED1: time's lexer re-read rule (TM-202) has no counterpart in regex, and time's version speaks for regex's file

This is the C1 question the dispatch asked.

**Location:**
- `nitpick-time/meta/DECISIONS.md:5719-5721`: the adoption "re-reads `src/frontend/lexer.npk` at the new pin whatever part E says, and brings `lexical.py` to it **in both libraries**".
- `nitpick-regex/harness/lexical.py:95-98`: case 18 "requires exactly the imports and the code the compiler would see at `c970483`".

**Evidence:**
- Regex has **no** rule to re-read the lexer at a re-pin; `git grep` finds no such rule.
- Case 18's expectations are fixed in Python, the same gap as time's E1.
- Regex's only compiler-side lexer guard is probe 15, which covers one form: the block-string close.
- The code is still identical. A syntax-tree comparison of the two `lexical.py` files with docstrings stripped gives `True`.

**Forecast, read at compiler HEAD `058505d` rather than the pin:** the next re-pin does move `lexer.npk`, through DEF-145. The change is +13/−2 in `lexer_next`, and it changes a character literal's *width* only, not its span. So the mirror survives the next re-pin, but in regex nothing requires anyone to find that out.

**Resolve:**
- `nitpick-regex` takes a rule (or an E2) of its own.
- `nitpick-time` drops "in both libraries": W-7 gives it no write in regex.

**Owners:** `nitpick-regex`, `nitpick-time`.

### ED2: the registry is missing 11 compiler requests that the libraries keep locally

**Location:** these libraries' `meta/OPEN_QUESTIONS.md`:

| Repository | Local ids |
|---|---|
| `nitpick-parse` | O-N2, O-N3, O-N4 |
| `nitpick-sockets` | O-N1, O-N3, O-N4 |
| `nitpick-tui` | O-N3, O-N4 |
| `nitpick-time` | O-N2, O-N3 |
| `nitpick-posix` | O-N7 |

**Evidence:**
- The registry claims to be the single filing place for compiler requests (`nitpick-libs/meta/OPEN_QUESTIONS.md:249-256`).
- `grep -c` over the registry returns 0 for each subject: stack-depth, map/hash, `arena.get`, `IO_REFERENCE`, `OwnedFd`, `sigaction`, `isatty`, timer, wall-clock, "top level of".

Re-verified live at the pin:
- **`nitpick-sockets`' O-N1:** `IO_REFERENCE.md` §10's "Sockets … not specified" is unchanged.
- **`nitpick-sockets`' O-N3:** `src/frontend/types.npk:1705` still says "or cross a spawn".
- **`nitpick-tui`' O-N3:** `io_isatty` is defined nowhere, while `IO_REFERENCE.md:144` says it "remains available".
- **`nitpick-posix`' O-N7:** probe 02e still gets `REACH-001` with no mention of the nested `pick`. Its id also collides with the registry's line 988, "O-N7 — never existed".

**Resolve:** register each, or strike it with a reason. Renumber posix's entry.

**Owners:** `nitpick-libs` (the registry), then each library's cross-reference.

### ED3: regex's CI has met its own condition for asserting the emission digest

**Location:** `nitpick-regex/.github/workflows/ci.yml:194` and `:217`: "The number becomes an expectation on the day somebody holds both sides of it and writes down that they matched."

**Evidence:**
- `nitpick-libs/.internal/toolchain/c970483/PIN.md` now records `npkc.ll d36a7e23…` (added after the sixth audit's N-34).
- Run 36253106675 printed the same digest.
- Regex 0.1.0's verifier recorded the match.
- Nothing schedules the promotion.

**Owner:** `nitpick-regex`.

---

## Stale

- **ES1:** `nitpick-parse`'s own O-N2 (`meta/OPEN_QUESTIONS.md:61-72`: "there is no stack-depth guard … nothing exists today … an **uncontrolled** fault") is false at the pin. D-305 (`DECISIONS.md:19521`) adds a split-stack prologue on every emitted function, trapping `StackExhausted` (4118), since 1.5.8. PA-022 may keep its reason, since a trap is not an error value, but the premise changed. **Owner:** `nitpick-parse`.
- **ES2:** status pages in the workbench are out of date. **Owner:** `nitpick-libs`.
  - `nitpick-libs/LIBRARIES.md:11-15` shows regex and time as "planned — … 0.0 execution-grade". Regex cycle 0.0 closed 2026-09-26 and 0.1 is open; time's 0.0 and 0.1 are closed.
  - `README.md:33-45`'s layout omits `nitpick-fuzz` and `nitpick-apps`.
  - `README.md:26`'s `tools/` line omits `ladder.py` and the canary.
- **ES3:** registry entries that disagree with settled facts. **Owner:** `nitpick-libs`.
  - O-X8 (`meta/OPEN_QUESTIONS.md:209`) says "an **eleventh** `ValueFault` variant". The enum has had 14 variants since 0.1.3, and time's own entry (`:704-705`) says so.
  - Q-4, the default width (`:30-32`), is still open although W-24 (`WORKSTREAMS.md:219`) and `START.md` settle it at 1.
  - PLAYBOOK §3 item 7 (`:360`) says to add `(BadStep)` "and drop it at DEF-95's notice". DEF-95 is carried in `c970483` (`PIN.md`, CARRIES).
- **ES4:** `nitpick-regex` never records O-N32, which its own 0.1.0 planning raised (registry `:285-297`). `git grep -c O-N32` returns 0, and `meta/roadmap/0.1/0.1.0.md:1352-1368` records the `EMIT-002` finding without an id. This is the time audit's C10 shape in regex. **Owner:** `nitpick-regex`.

---

## Cosmetic

- **EK1:** the board's list of owed work names the wrong rule in two repositories, and misses a manifest. **Owner:** `nitpick-libs`.
  - The A′ item (`BOARD.md:9438`) says "each of the six repositories replaces its `VERIFICATION.md` P-1". In `nitpick-sockets` (`VERIFICATION.md:28`) and `nitpick-posix` (`:7`) that rule is called **Z-1**.
  - The F15 adoption list says the two new `[toolchain]` rows go into "each of the five libraries". `nitpick-posix/nitpick.toml` is a sixth manifest with the same block.
  - These are runner pins, not compiler reads: `1b4f0c6`'s message says "the compiler does not parse nitpick.toml".
- **EK2:** regex's CI lacks two steps that time's has. **Owner:** `nitpick-regex`.
  - Time's "Assert the compiler is AT the pinned commit" (`nitpick-time/.github/workflows/ci.yml:224`).
  - Time's assertion of the unqualified summary (TM-125, `:379-388`). Regex's runner accepts `--only`, so a flag added at `ci.yml:286` would weaken the badge silently.
  - Both CIs also run `actions/checkout@v4` and `actions/cache@v4` under GitHub's annotation "Node.js 20 is deprecated … forced to run on Node.js 24" (run 36274631237).
- **EK3:** `check_refs nitpick-apps/nitpick-posix` reports `[unmarked-supersede] PX-010 is declared superseded at meta/roadmap/0.0/0.0.0.md:196, meta/roadmap/0.0/README.md:51 but its heading carries no marker`. This is the only mechanical finding across the nine trees. **Owner:** `nitpick-posix`.

---

## Checked and found clean

- **The pins agree.** Both `ci.yml` files pin `c9704830ea9c738f523bf6646a355f52679b3aee`, which `git rev-parse c970483` confirms, and LLVM 20.1.2. Time's `NPKC_SHA256_WORKBENCH` and `NPKRT_SHA256_WORKBENCH` equal `PIN.md`'s rows. Regex's CI prints `npkc.ll` equal to `PIN.md`.
- **Regex's error budget, at the pin.**
  - Regex's budget check is **not** C2-shaped for a budgeted name declared in two modules: that plant goes red.
  - S-8 holds today. The umbrella's bill at the pin is the floor of 6.
  - Per-module bills match `SAFETY.md`'s table: `core` 11, `vec` 10, `bytes` 10, `cursor` 8, `ast` 11, `api` 6.
  - Time's umbrella bill is 13, including `cal.ETimeValue`.
- **The registry's status agrees with each library.** O-N25, O-N27 and O-N28 match time's and regex's registers.
- **Older registry entries still hold at `c970483`.**
  - O-N1: the runtime has zero `rt_sigprocmask` calls.
  - O-N2: `rootlist_add` is called only from `tests/frontend/resolve_paths.npk`.
  - O-N5 still holds.
- **Signal sets agree with the floor.** `nitpick-tui`'s blocked set (D-15) excludes `SIGUSR1` and the four fault signals the floor handles (D-291, D-307). T-113 and SK-013 remain correct conclusions.
- **Superseded decisions.** No repository cites D-045, D-079 or D-161 as live. `nitpick-fuzz` quotes D-167 only through the compiler's own `OP_REFERENCE.md:70`.
- **Next re-pin, names and decisions.**
  - No unstarted repository cites D-326…D-334.
  - No repository declares or plans `Copy` or `list_get`.
- **Keyword module names.** No planned module basename in parse, tui or posix is a keyword, checked against all 170 keywords.
- **Tree discovery.** The orchestrate skill's listing returns the board's nine trees.
- **`check_refs`** is clean on eight trees.

**Verdict:** the ecosystem is sound where it has been exercised (regex and time). Fix EC1, EC4, EC5 and EC12 before the owning repository's next dispatch, and correct PLAYBOOK §2 and §3 (EC2, EC3) before any new plan is written from them.

## What I did not reach

- `PLAYBOOK.md` §6 (Tooling, `:450-1112`) and §7–§12 were not verified. Only §2's table, §3 and §10 were.
- The `gather_claims.py` sweep over every repository was not run.
- `nitpick-fuzz/KNOWN_DEFECTS.md` was not checked against the registry.
- `RECORD.md` for 2026-09-25/26 was read by headings and cited entries only. W-19, W-20 and W-23 practice was not audited. The worker, plan, check, research and new-repo skills were not audited.
- Only part of `BOARD.md`'s stream tables was read. The rows for `nitpick-parse`, `nitpick-sockets`, `nitpick-tui` and `nitpick-posix` were not compared against their repositories.
- D-328 (`cstring` owning) against `nitpick-posix`'s G-13 (`meta/specs/ARGUMENTS.md:78-81`: "`Args` holds slices into it … `args_value` returns a view"): **a candidate, not probed**. D-329 and D-331 were not swept in the plans.
- Regex's cycle-0.1 plans after 0.1.0, time's 0.2.0, and `nitpick-apps/PLAYBOOK.md` beyond a signal grep were not read.
```
