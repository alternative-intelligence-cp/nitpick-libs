<!-- Filed 2026-10-09 by nitpick-libs_15. Made by the API-credits runner (.internal/credits/run.sh, job ecosystem-early-2026-10-09): headless claude -p on claude-sonnet-5-5, read-only tools, 255 turns, $9.90 of the plan's monthly API credits. EARLY: W-22 asks for one after every third close, and only two cycles have closed since 2026-09-26 (time 0.2, regex 0.1). It was run after the re-pin at the author's go. Spot-checked by the seat before filing: E2-1 (PLAYBOOK.md:74-75), E2-5 (CLAUDE.md:26 against WORKSTREAMS.md:232 and :249), E2-9 (meta/OPEN_QUESTIONS.md:459 O-N34 open, against the compiler's OPEN_DECISIONS.md:3713, DEF-225 FIXED) and E2-12 (BOARD.md:12). The workbench's findings are seat writes, and the repositories' go with each repository's next dispatch by id. One edit for check_refs only: a line naming nitpick-time's own second and third O-N rows is reworded, because the workbench's checker reads a bare id as this registry's. -->

# Ecosystem audit (early), 2026-10-09

**Verdict.** The ecosystem is sound where it has been exercised, and the fixes since 2026-09-26 landed wherever a repository was dispatched. Of the 23 earlier findings, 7 are FIXED, 6 are half-fixed (the workbench half done, the repository half open) and 10 are untouched. The worst leftovers are still `nitpick-posix`'s PX-011 and probe 05 (EC1) and its probes' missing arms (EC12). The new defects are mostly in `PLAYBOOK.md`, the page every plan starts from:
- it keeps a false signal row (§2) beside its correction;
- it has no row for `fixed T[]` (D-350, D-351) and still says `string_bytes` yields a plain `uint8[]`;
- it describes at least six compiler defects and decisions as live that the compiler has since fixed or settled.

The registry still carries 12 or more rows whose compiler DEF or library decision is already settled. No tool was run and no compiler probe was made.

## FINDINGS

**E2-1 · contradiction · owner `nitpick-libs`: `PLAYBOOK.md` §2 keeps the pre-`c3bdae2` signal row live beside its correction.**
- `PLAYBOOK.md:74`: "THE RUNTIME DOES INSTALL SIGNAL ACTIONS … `SIGPIPE` gets a returning handler … `EPIPE`".
- `PLAYBOOK.md:75`: "the runtime installs no signal disposition, for anything … `SIGPIPE` terminates the process", un-struck.
- `PLAYBOOK.md:77-85`: the callout treats row 75 as current.
- `nitpick/runtime/npkrt.ll:2092,2099,2119`: `SIGPIPE (13; DEF-68 …)`, `@npk_pipe_handler`.
- Fix: strike row 75 as `:48`, `:53` and `:54` do. Date the callout at :77-85. Update `skills/plan/SKILL.md:38-41` and `skills/worker/SKILL.md:97-100`, which cite the T-113 episode as a model.

**E2-2 · contradiction (compiler claim) · `nitpick-libs`: no `fixed T[]` rule, and `string_bytes` is still described as plain.** This meets TL-1, PL-1 and SL-1 of the four pin audits of 2026-10-09.
- `PLAYBOOK.md:178` and `:212-214`: `string_bytes` yields "a `uint8[]`"; `grep 'fixed uint8|fixed T\[\]|D-351'` over `PLAYBOOK.md` and `APPS.md` finds nothing.
- `DECISIONS.md:22803`: "D-351 — `string_bytes` RETURNS THE READ-ONLY VIEW, `fixed uint8[]`, ALWAYS". `TYPE_REFERENCE.md:1233-1243` agrees.
- Fix: add a §2 row (a plain slice converts to `fixed`, never back, `TYPE-007`; a write is `TYPE-086`; a reader declares `fixed uint8[]`). Rewrite :176-184 and :212-214.

**E2-3 · stale (fixed or settled items stated as live) · `nitpick-libs`:**
- **O-N9, `PLAYBOOK.md:176-184`**: "NOT for slice views … Until it lands". The registry says DISCHARGED, `BORROW-001` since `94874ce` (`meta/OPEN_QUESTIONS.md:1249`).
- **O-N10, `PLAYBOOK.md:250-253`**: "does not compile … Until it lands". The registry (`:1237`) says DISCHARGED since `94874ce`.
- **`f(g(x))` leak, `PLAYBOOK.md:185-205`**: "every Nitpick program pays it today … proposed as its D-246". `DECISIONS.md:17300`: "D-246 … SETTLED (… landed at step 4, 2026-09-04)".
- **O-N4, `PLAYBOOK.md:511-534`**: "Plan around it". The registry (`:1216`) says linear since `94874ce`.
- **`main` rule, `PLAYBOOK.md:262-267`**: "no pin of ours carries it yet … exposure … zero". The pins `c970483`, `5fbaf4a` and `7e91730` carry it.
- **S-108, `PLAYBOOK.md:56`**: "a prelude marker is the author's S-108 … `Pod`". `DECISIONS.md:21816`: D-327 `Copy`. `nitpick-regex/CLAUDE.md:415-417`: "`Pod` retired into the prelude's `Copy`".
- **Index guards, `PLAYBOOK.md:586-595`**: "THREE type kinds". `ir_expr.npk:10347` also guards `List<T>`, as row 53 says.
- **`PLAYBOOK.md:726`**: cites `src/main.npk`; the file is `src/npkc.npk`.
- Fix: dated notes at each site, or strike with the evidence.

**E2-4 · contradiction (toolchain and manifest) · `nitpick-libs`, with four manifests:**
- `PLAYBOOK.md:1270-1275`: "`[toolchain]` pinned to 20.1.2 with the four flag lists".
- `skills/orchestrate/SKILL.md:108`: "`llvm-config --version  # must print 20.1.2`".
- `skills/new-repo/SKILL.md:55-59`: "pinned … with the four flag lists".
- `BUILD_REFERENCE.md:106-107`: "a library's manifest carries the same two rows as this one" (`triple`, `datalayout`). `TCB.md:53`: LLVM 20.1.8 since D-349.
- Only `nitpick-regex` and `nitpick-time` have the two rows. `nitpick-tui`, `nitpick-parse`, `nitpick-sockets` and `nitpick-posix` do not.
- This widens EK1's "sixth manifest" item.
- Fix: correct all three workbench texts, and add the rows to the four manifests at their adoption.

**E2-5 · contradiction · `nitpick-libs`: `WORKSTREAMS.md` against the closed compiler cycle 1.5.**
- `WORKSTREAMS.md:23`: "1.5.1 – 1.5.4 … Nothing earlier".
- `OPEN_DECISIONS.md:2124`: "cycle 1.5 CLOSED 2026-09-25". `PLAYBOOK.md:57` and `nitpick-regex/CLAUDE.md:305-321` record `limit`, `requires` and `ensures` live.
- `WORKSTREAMS.md:273-286` still lists "each library's cycle 0.0 probes … five afternoons"; regex and time closed 0.0.
- `CLAUDE.md:26` says "W-1…W-26"; `WORKSTREAMS.md:232` and `:249` define W-27 and W-28.
- Fix: restate the gating table, §6 and `CLAUDE.md`. Also move W-14 (:283), which sits out of order after W-28.

**E2-6 · contradiction (across repositories) · owners `nitpick-tui`, `nitpick-regex`, `nitpick-parse`, `nitpick-time`: the dogfood consumer's location.**
- `nitpick-tui/meta/roadmap/ROADMAP.md:208`, "A real program in `examples/`"; `meta/OPEN_QUESTIONS.md:44-46`, Q-5 "in `examples/` in this repository".
- `nitpick-regex/meta/roadmap/ROADMAP.md:333`: "A real program in `examples/` — a `grep`-shaped tool".
- `nitpick-parse/meta/roadmap/ROADMAP.md:184`: "A configuration linter in `examples/`".
- Decisions that say otherwise:
  - tui `DECISIONS.md:768`, T-114: "moves to `nitpick-apps`"
  - regex `DECISIONS.md:484`, RX-101: "lives in `nitpick-posix`"
  - time `DECISIONS.md:541`, TM-103: "in `nitpick-posix`"
  - `APPS.md:19-20` (the linter and log viewer in their own repositories)
- `nitpick-tui/meta/DECISIONS.md:617`, T-104, has no supersede marker.
- Fix: amend each roadmap line and add the marker to T-104.

**E2-7 · contradiction · `nitpick-libs`: the sandbox's `denyWrite`.**
- `PLAYBOOK.md:957-960`: "That mitigation is not deployed. `denyWrite` appears nowhere"; registry Q-3 (`meta/OPEN_QUESTIONS.md:24-29`) is still open.
- `BOARD.md:75`: a sandbox that confines shell writes and in which "`../nitpick` is read-only".
- Fix: re-date the PLAYBOOK paragraph, answer Q-3, and state what the guard still cannot see.

**E2-8 · contradiction · `nitpick-posix`:**
- `README.md:7-9`: "Status: scaffolded … the planning pass has not been run. Nothing is implemented."
- Against `APPS.md:10` ("planned — 11 specs … 0.0 execution-grade") and eleven spec files, 19 decisions and 15 cycle rows.
- `meta/roadmap/ROADMAP.md:3` says "seventeen decisions".
- Fix: update the README status and the ROADMAP intro.

**E2-9 · stale · `nitpick-libs`: registry rows open whose compiler or library answer is final.** `skills/orchestrate/SKILL.md:250-254` says a fix is struck in the commit that records it.
- **Compiler side**, `meta/OPEN_QUESTIONS.md` against `OPEN_DECISIONS.md` at 7e91730:

| Registry row (line) | Compiler status |
|---|---|
| O-N27 (:645) | D-326 landed, `DECISIONS.md:21754` |
| O-N28 (:619) | DEF-116 FIXED, :2495 |
| O-N29 (:599) | DEF-126 FIXED, :2601 |
| O-N30 (:559) | DEF-118…125 FIXED, :2520-2594 |
| O-N31 (:530) | DEF-127…133 FIXED, :2607-2665 |
| O-N32 (:516) | DEF-142 and DEF-143 FIXED, :2736 and :2743 |
| O-N33 (:489) | DEF-144…152 FIXED, :2756-2832; DEF-154 stays open |
| O-N34 (:459) | DEF-225 FIXED, :3713 |
| O-N36 (:398) | DEF-227, 229, 230, 231 FIXED, :3751-3828 |
| O-N38 (:373) | DEF-228 FIXED, :3770 |

- Landings 69-82 are carried by `5fbaf4a`, so the rows through O-N33 are about 12 days overdue. The rest are carried by `7e91730`.
- **Library side**:
  - O-X9 (:229) "Handed to cycle 0.3.1": TM-250.
  - O-X11 (:219): TM-251.
  - O-X12 (:201) "Cycle 0.3.2's planner decides": TM-254.
  - O-Y2 (:258): RX-201. Its recommendation ("do not [ignore], matching Rust") is the reverse of what RX-201 measured.
- **Still open and consistent**: O-N1, O-N2 (`rootlist_add` is defined in `src/frontend/resolve_path.npk:57` and not called), O-N5, O-N35 (DEF-235, DEF-239), O-N40, O-N41.
- Fix: strike each with its evidence.

**E2-10 · stale (counts against sets) · owners as listed:**

| Claim | Set |
|---|---|
| `LIBRARIES.md:11` tui "67 decisions" | 69 `### T-` headings (`DECISIONS.md:28-796`) |
| `LIBRARIES.md:12` parse "43" | 47 PA- headings |
| `LIBRARIES.md:14` sockets "35" | 36 SK- headings |
| `APPS.md:10` posix "17 decisions, 14 cycles" | 19 PX- headings; 15 table rows (`ROADMAP.md:44-58`) |

- `WORKSTREAMS.md:87` "26 cycles" is therefore 27.
- Spec counts follow two conventions. tui 16, parse 13, sockets 14 and posix 11 include the specs README. regex 13 and time 12 exclude it.
- `PLAYBOOK.md:1206-1211` says eight trees; `BOARD.md:12` says nine since `nitpick-fuzz`.
- `nitpick-tui/meta/roadmap/ROADMAP.md:6` has two batches to T-112, but T-115 exists. `nitpick-regex/meta/roadmap/ROADMAP.md:6` says "RX-001 … RX-080" while decisions run to RX-230.
- `nitpick-time/README.md:9`: "its first subcycle, the clocks", while the same paragraph reports 0.3.1 and 0.3.2.
- Fix: derive each count from its set, or drop the number.

**E2-11 · contradiction · `nitpick-libs`:**
- `README.md:102-104`: "the auditor and researcher genuinely cannot write".
- `agents/auditor.md:5` and `agents/verifier.md:5` list `Bash`. `PLAYBOOK.md:943-975` says the guard cannot see an interpreter heredoc.
- Fix: say "by discipline, plus the guard where it can see".

**E2-12 · stale · `nitpick-libs`:**
- `meta/roadmap/README.md:10` and `meta/roadmap/0.2/README.md:3` say cycle 0.2 "planned" and "Status: PLANNED"; `0.2.7.md:1` is "RUNNING (since 2026-09-03, author)".
- `meta/audits/README.md:4` gives the file-name rule `<repo>-<cycle>-<date>.md`, but the four new audits are `…-pin-7e91730-…`.
- `BOARD.md:12` "Last updated: 2026-10-08" against a 2026-10-09 pin; `BOARD.md:17` "READ THIS FIRST" still addresses `_14→_15` while `_15` is the writer.
- `skills/orchestrate/SKILL.md:53-57,137` give the `<project>_s<N>` convention and name `nitpick-compiler_s0`, which no longer matches the board's `nitpick-libs_15` and `nitpick-compiler_33`.

**E2-13 · dormant, with one unverified claim · owners: `nitpick-tui`, `nitpick-parse`, `nitpick-sockets`, `nitpick-posix`, and the workbench:**
- `skills/plan/SKILL.md:64-82` and `PLAYBOOK.md:1610-1612`: every external dependency is a `meta/research/CURRENCY.md` row, and a cycle with unchecked rows "is not ready to start".
- The four planned repositories have no `CURRENCY.md` and no digests (their `meta/research/` holds only a README, plus `.gitkeep` files). Nothing checks this: `check_refs.py` has no such class.
- tui T-100 (`DECISIONS.md:556-561`) names the "latest stable UCD, 15.1.0 floor" with no date, which is an unverified claim under the audit skill §1b.
- The "three mandatory research items" rule (plan skill :76-80) was not run for parse, sockets or posix.
- Fix: either write the rows, or add the check.

**E2-14 · dormant / contradiction · `nitpick-libs`, `nitpick-posix`:**
- `WORKSTREAMS.md:53` draws `PA --> PX11` (awk needs `nparse`) and :98-100 times it. `nitpick-posix/meta/roadmap/ROADMAP.md:55` gates 0.11 on 0.10 only, so W-9 has nothing to check.
- W-9 (:149-150) says "nine ungated cycles"; ROADMAP gates only 0.5 and 0.7 on libraries, with 0.11's gate missing as above.
- `WORKSTREAMS.md:55-57,85-86` name `nitpick-logview` and `nitpick-conflint`, which no registry claims (`APPS.md:17-23` leaves the applications unnamed).

**E2-15 · cosmetic · `nitpick-libs`:**
- `skills/check/SKILL.md:32-39` lists six finding classes. `check_refs.py` also emits `tracked-file-missing` (:150), `no-markdown` (:154) and `unmarked-supersede` (:230).
- Also in `nitpick-tui/CLAUDE.md:5-7` and `nitpick-posix/CLAUDE.md:5-7`, which have an empty "What this is" heading.

## THE 23 OF 2026-09-26

Where only a workbench half is fixed, the line says so.

- **EC1 — STILL OPEN** (workbench half fixed). `LIBRARIES.md:175-183` and `PLAYBOOK.md:74` are corrected (but see E2-1).
  - Not corrected:
    - `APPS.md:79-93` ("the runtime installs none")
    - posix `DECISIONS.md:116-125` (PX-011), `SAFETY.md:136-150` (S-7), `0.0.0.md:119`, `CONTRIBUTING.md:24`, `CLAUDE.md:35`
    - tui `TERMINAL_MODEL.md:280-283` and `DECISIONS.md:725-726`
    - sockets `SAFETY.md:17,48`, `CLAUDE.md:38`, `README.md:25`, `CONTRIBUTING.md:33`, `DECISIONS.md:137`, `ROADMAP.md:40`, `0.0.0.md:154`, `TESTING.md:81`
- **EC2 — STILL OPEN** (workbench half fixed: `PLAYBOOK.md:53`). Remaining:
  - tui `SAFETY.md:24`, `VERIFICATION.md:40`
  - parse `SAFETY.md:22`, `VERIFICATION.md:37`
  - sockets `SAFETY.md:28`, `VERIFICATION.md:40`
  - posix `SAFETY.md:20`, `VERIFICATION.md:16`
  - The `VERIFICATION.md` and posix sites are new to the list.
- **EC3 — STILL OPEN** (workbench half fixed: `PLAYBOOK.md:48,376-382`).
  - The eight sentences the board counts remain: tui `CONTRIBUTING.md:32`, `ROADMAP.md:55`, `SAFETY.md:20`; parse `README.md:36`, `ROADMAP.md:49`, `SAFETY.md:18`; sockets `CONTRIBUTING.md:46`, `SAFETY.md:20`.
  - Six check-shape rows are not counted, all naming "count and names of public `error:`":
    - tui `TESTING.md:58`, `0.0.3.md:63`
    - parse `TESTING.md:57`, `0.0.3.md:63`
    - sockets `TESTING.md:127`, `0.0.3.md:69`
- **EC4 — FIXED.** `nitpick-regex/harness/treecheck.py:91` (`_ERROR_DECL` over the whole blanked text, `pub\s+`) and :277-297 (keyed by module, private counted).
- **EC5 — FIXED.** `treecheck.py:571`, `\.\s*(items|ptr)\s*\[` over blanked text.
- **EC6 — FIXED.** `nitpick-time/.github/workflows/ci.yml:435-480` prints and asserts `npkc.ll` as "the cross-machine claim".
- **EC7 — STILL OPEN** (workbench half fixed: `PLAYBOOK.md:1554-1560`). Sockets still plans `src/option/raw.npk` at `OPTION_MODEL.md:12`, `DECISIONS.md:317`, `TESTING.md:132`, `0.7/README.md:25`, `0.0.3.md:74`. `src/frontend/keywords.npk:38` still has `"raw"` as `KwRaw`.
- **EC8 — STILL OPEN.** `WORKSTREAMS.md:184,187-191` unchanged; no mention of fuzz in `WORKSTREAMS`, `README`, `LIBRARIES`, `CLAUDE`, or the orchestrate and worker skills. `BOARD.md:92` lists it as owed.
- **EC9 — STILL OPEN.** `WORKSTREAMS.md:190-191` "A re-pin happens between cycles". The 7e91730 pin (`BOARD.md:13`) was taken mid-cycle, regex in 0.2 and time in 0.3. `orchestrate/SKILL.md:86` says only "no claim in flight".
- **EC10 — STILL OPEN.** The three Q-6s are unchanged: registry `OPEN_QUESTIONS.md:48`, `RECORD.md:4552`, and `BOARD.md:10203` (now a different line).
- **EC11 — FIXED.** `nitpick-regex/meta/specs/TESTING.md:220,222` give 0.6 and 0.4, matching `0.6/README.md:14` and `0.4/README.md:50`.
- **EC12 — STILL OPEN.** `StackExhausted|MachineFault` has 0 hits in `nitpick-posix`. The pin audit's XL-1 to XL-3 cover other probe changes and not this.
- **EU1 — STILL OPEN.** `2024|Issue 8` has 0 hits in `nitpick-posix`, `2017` hits in 8 files, there is no `CURRENCY.md`, and registry Q-1 (`OPEN_QUESTIONS.md:10-17`) has been open 36 days.
- **ED1 — FIXED (moved).** Regex has its rule (`nitpick-regex/meta/DECISIONS.md:4378`, RX-176, "Every adoption re-reads …"). Time's "in both libraries" is marked superseded by TM-208 (`nitpick-time/meta/DECISIONS.md:5770-5774`).
- **ED2 — STILL OPEN.**
  - The registry has no entry for these local requests:
    - parse (`OPEN_QUESTIONS.md:61,75,85`)
    - sockets (:39,58,68)
    - tui (:77,84)
    - posix O-N7 (:72). It still collides with registry `OPEN_QUESTIONS.md:1228` "O-N7 — never existed".
  - Rows 2 and 3 of `nitpick-time`'s own registry series (its `O-N` rows, not this workbench's) were not re-read.
- **ED3 — FIXED.** `nitpick-regex/.github/workflows/ci.yml:321-328` asserts `npkc.ll` equals the pin's row.
- **ES1 — STILL OPEN.** `nitpick-parse/meta/OPEN_QUESTIONS.md:61-65` still says "nothing exists today". The 2026-10-09 parse audit's PL-5 carries it.
- **ES2 — STILL OPEN** (workbench half fixed: `LIBRARIES.md:13,15` show building). `README.md:31-43` still omits `nitpick-fuzz`, `nitpick-apps` and `nitpick-posix`. `README.md:26` still lists only the guard, its control and the hook script, while `tools/` also holds `ladder.py`, `floatscan.py`, `run_controls.py`, `canary.*`.
- **ES3 — STILL OPEN**, all three items:
  - `OPEN_QUESTIONS.md:245` "eleventh `ValueFault`", against `nitpick-time/meta/OPEN_QUESTIONS.md:815` "fifteenth".
  - `OPEN_QUESTIONS.md:30-32` Q-4, against W-24 (`WORKSTREAMS.md:219`).
  - `PLAYBOOK.md:403-405` `(BadStep)` "drop it at DEF-95's notice", while `NOTICES.md` row 54 shows DEF-95 delivered.
- **ES4 — FIXED.** O-N32 is struck at `nitpick-regex/meta/OPEN_QUESTIONS.md:614`.
- **EK1 — STILL OPEN.** `BOARD.md:10203` still says "each of the six repositories replaces its `VERIFICATION.md` P-1". Sockets (`VERIFICATION.md:28`) and posix (:7) call it Z-1. `BOARD.md:1690,92` list it as owed. See E2-4 for the manifest half.
- **EK2 — STILL OPEN** (regex half fixed: `ci.yml:157` pinned-commit assert, `:346-359` unqualified-summary assert). Node 20 actions remain: `actions/checkout@v4` and `actions/cache@v4` at time `ci.yml:330,333,367,402` and regex `ci.yml:143,146,179,213`.
- **EK3 — STILL OPEN.** `nitpick-posix/meta/DECISIONS.md:94` has an unmarked PX-010 heading; the supersede note is in the body (:96).

## NOT CHECKED

- No shell. I could not confirm `../nitpick` HEAD is `7e91730`, run `check_refs`, `check_record`, `gather_claims`, or `git`, or compile a probe. I read the working tree, including `runtime/npkrt.ll`, `src/frontend/keywords.npk` and `src/backend/ir/ir_expr.npk`, and never `build/`.
- Read whole: the workbench top documents and skills, `agents/`, the audit files, `BOARD.md` lines 1-110 and the registry. Also `PLAYBOOK.md`, the two `nitpick-apps` playbooks and `APPS.md`, and the `nitpick-tui` and `nitpick-regex` top documents.
- Read by targeted search only: the remaining library roadmaps, `DECISIONS.md` files and `OPEN_QUESTIONS.md` files, `nitpick-posix`'s `CONTRIBUTING.md`, `RECORD.md`, the rest of `BOARD.md`, and the compiler's `DECISIONS.md`, `OPEN_DECISIONS.md` and `NOTICES.md` (rows by DEF number only).
- Not read: `tools/*.py`, `hooks/hooks.json`, `meta/roadmap/0.2/*.md` beyond headings, `.github` of the four repositories with no CI (none exists), and the board's "shared CI shape" findings (`BOARD.md:94`), which I could not identify.
- Time's own O-N entries against the registry, and the O-N25/27/28 agreement the previous audit found clean, were not re-compared.
- D-305 and the parse O-N2 premise were taken from the parse pin audit's PL-5, not re-read.
- The sandbox's real settings (E2-7) are unreadable from here, so that finding is document against document.