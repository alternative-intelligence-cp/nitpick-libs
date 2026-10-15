<!-- Filed 2026-10-15 by nitpick-libs_19. Made by the API-credits runner (.internal/credits/run.sh, job ecosystem-2026-10-15): headless claude -p on claude-sonnet-5-5, read-only tools, 236 turns, $7.7755 of the plan's monthly API credits, 13:19:57-13:34:21. W-22's audit after the sixth close (nitpick-time's cycle 0.3, at 1cc801f). Its BOARD.md line numbers are those of 13:19; at 13:23 two lines were added after line 14, so a line it cites past 14 is now two further down (its number plus two). The triage is RECORD.md's entry of this date. Two passages that cite repository-local question ids were changed in form only at filing, so that this workbench's check_refs does not read them as its own registry's ids: ED2's local rows are fenced, and E3-16's id of time's own fourth X question is written "time's own question X-4". -->

# Ecosystem audit, 2026-10-15 (W-22, after the sixth close)

**Verdict.** The workbench's own documents were largely repaired after 2026-10-09: of the 15 early findings, 6 are FIXED outright and 9 are half-fixed (the workbench half done). Of the 16 earlier findings the early audit left open, 1 is FIXED (EK3), 1 MOVED (EU1, to PX-102) and 14 are STILL OPEN. The libraries' own pages are the weak part. tui, parse, sockets and posix still carry the SIGPIPE, index-trap and error-budget claims, and their manifests are still at LLVM 20.1.2 with no `triple`/`datalayout` rows. The worst new defects are cross-repository:

- PLAYBOOK §5 says the language has no stack guard, against its own §3 and the compiler's D-305.
- The `PD-n` label is a bare number that collides across repositories, and no rule states it.
- The worker skill's one-commit and the libraries' push-at-cycle-end rules contradict what the chains do.
- The Team seat's branch-and-merge practice is in no rule.

Read at the compiler's working tree, which is newer than the pin. The tree carries D-359 and landings through 112. D-305, D-350, D-351, DEF-154/225/226/232/233/235/239 and runtime lines were checked there. `runtime/npkrt.ll:2087-2119` has the SIGPIPE handler. No shell, so no tool was run and no probe compiled.

## FINDINGS

**E3-1 · contradiction (compiler claim) · owner `nitpick-libs`, then `nitpick-parse` · "no stack guard" is false at the pin.**
- `PLAYBOOK.md:499`: "parser on `[[[[[…` blows the stack, and the language has no stack guard".
- `PLAYBOOK.md:414-417`: "At `c3bdae2` the floor is six … `StackExhausted` and `MachineFault`".
- `specs/DECISIONS.md:20226` (compiler): "D-305 — A stack overflow is a controlled trap … `StackExhausted` (4118)".
- `nitpick-regex/CLAUDE.md:463-471`: "the reason RX-032 … gave … is false".
- Parse still states it: `README.md:53`, `CLAUDE.md:54-55`, and `meta/OPEN_QUESTIONS.md:61` ("there is no stack-depth guard"). This is ES1 and the parse pin audit's PL-5, which meets this finding.
- Fix: restate the §5 bullet as "a trap, not a segfault; the explicit stack stands because a trap ends the program" (regex RX-191's wording). Strike parse's O-N2 premise.

**E3-2 · contradiction · owner `nitpick-libs`, with `nitpick-time`, `nitpick-regex` · `PD-n` is a plan-local label with no rule, and it has collided.**
- `nitpick-time/meta/DECISIONS.md:6607` "plan's PD-66" and `:6926` "plan's PD-72", against `nitpick-regex/meta/DECISIONS.md:5747` "PD-66" and `:5956` "PD-72". They are different decisions.
- From regex's PD-103 an ecosystem-wide sequence is in use. Examples: `BOARD.md:10668` "PD-129 … PD-148" for parse, `nitpick-time/meta/roadmap/0.4/0.4.0.md:71` "PD-149 … PD-158".
- The scheme is stated in no workbench rule. PLAYBOOK, WORKSTREAMS and the skills only cite old numbers as examples (`PLAYBOOK.md:54,1184,1226,1541,1564`). `check_refs` does not read PD.
- Fix: one paragraph in PLAYBOOK §7 and the plan skill: PD is allocated by the seat, ecosystem-wide, from PD-103; cite it as `<repo> PD-n`; PD-1 … PD-102 are per repository.

**E3-3 · contradiction · owner `nitpick-libs` · one commit per subcycle, and when to push.**
- `skills/worker/SKILL.md:83` "One commit per subcycle", and `:77-78` "the subcycle's one commit".
- `BOARD.md:10666`: time 0.3.4 "six commits". `BOARD.md:10667`: regex 0.2.2 "Five commits on `5161973`".
- `PLAYBOOK.md:1381` "Push each commit as it is made". But `nitpick-regex/meta/roadmap/ROADMAP.md:21`, `nitpick-time/meta/roadmap/ROADMAP.md:58` and `nitpick-tui/meta/roadmap/ROADMAP.md:22` say "Push at the end of every cycle".
- Fix: amend the worker skill to "one commit per plan step, then the record", and state the push rule in one place.

**E3-4 · contradiction / dormant · owner `nitpick-libs` · the Team seat's practice is in no rule (EC8 and EC9, widened).**
- `WORKSTREAMS.md:190-191` "Nothing is branched and nothing is merged"; `skills/orchestrate/SKILL.md:311-315` "There is no merge step … workers commit to `main` (W-17)".
- `BOARD.md:43` "fetch the `team/` branch … fast-forward our clone's `main`"; `:138` "works on `team/<repo>-<item>` branches"; `:10668` "branch `team/parse-0.0-plan`".
- `WORKSTREAMS.md:196-197` "A re-pin happens between cycles"; pins `c970483`, `5fbaf4a` and `7e91730` were taken with regex and time mid-cycle (EC9).
- A search for `fuzz`, `team/`, `Team seat` and `management` finds nothing in `WORKSTREAMS.md`, `README.md`, `LIBRARIES.md`, `CLAUDE.md`, or the orchestrate, worker and plan skills.
- Fix: add W-rules for a branch-and-review domain (who writes `main`, the review and merge, the order gate), for tool repositories, and for the mid-cycle adoption subcycle.

**E3-5 · contradiction · owners `nitpick-apps`, `nitpick-regex` · "arms" against "identities".**
- `nitpick-apps/PLAYBOOK.md:25-26`: "Importing `ntui` costs nine arms, `nparse` two, `ntime` three".
- `nitpick-time/README.md:139-155`: "three … The whole bill is larger … 11 … 13". The same page records that it "counted the identities and not the bill".
- `nitpick-regex/README.md:87-88`: "costs your program's `failsafe` exactly one arm". Against `meta/specs/SAFETY.md:305-325`: floor of six, `core` 9-11. S-8 itself qualifies it at `:321`.
- Fix: say "identities", and point at each library's bill table.

**E3-6 · contradiction · owner `nitpick-posix` · the macro `failsafe` is still the instruction.**
- `CONTRIBUTING.md:14-15`: "Its `failsafe` is the macro (`SAFETY.md` S-2). A hand-written `pick` fails `check_failsafe_macro`".
- `CLAUDE.md:28`: "the answer is a macro", and `:23`. `meta/specs/README.md:19`: "the macro that writes them".
- `meta/specs/TESTING.md:115`: "*Replaced `check_failsafe_macro` under PX-100*". `meta/DECISIONS.md:215`: "PX-100 — `failsafe` is **generated**".
- The posix pin audit's XL-5 covers `UTILITY_MODEL.md` only. Fix: reword all four sites to "generated, `check_failsafe_current`".

**E3-7 · stale (a closed cycle called open) · owner `nitpick-libs`.**
- `LIBRARIES.md:15`: "cycle 0.3 (the host boundary) in progress … 0.3.3 … verified 2026-10-13 … 146 units GREEN … decisions to TM-262".
- `nitpick-time/README.md:9`: "cycle 0.3 … CLOSED on 2026-10-15". `ROADMAP.md:110` agrees, and the board's work verification passed at 13:16 (`BOARD.md:10666`).
- Fix: write the closed row and the 0.4 opening, with a "Was …" note.

**E3-8 · dormant · owner `nitpick-libs` · "claim a prefix in the registry" has no registry for applications.**
- `LIBRARIES.md:4-5` and `:146-147` list five prefixes and `D-`. `skills/new-repo/SKILL.md:19-26` says the registry row is in `APPS.md` for an application.
- `nitpick-apps/APPS.md:8-10` has no package or prefix column. `PX-` is used in `nitpick-posix/meta/DECISIONS.md:15-269` and claimed nowhere.
- `PLAYBOOK.md:1338-1344` also lists five.
- Fix: add the prefix to `APPS.md`'s table, or name posix under "Names taken".

**E3-9 · stale (registry rows) · owner `nitpick-libs`, `nitpick-regex`.**
- Q-1, `meta/OPEN_QUESTIONS.md:10-18`: "The `PX-` decision follows his answer, in nitpick-posix's 0.0.1". But `nitpick-posix/meta/DECISIONS.md:269` "PX-102 — … 2026-10-15, the author's decision". Strike Q-1 with PX-102 (meets the PX-102 and digest scope).
- O-X6, `:297`: "**SETTLED 2026-10-01 by `nitpick-time`'s TM-229**", not struck. Time's own row is struck (`nitpick-time/meta/OPEN_QUESTIONS.md:733`).
- Regex `meta/OPEN_QUESTIONS.md:629` (O-N28) and `:667` (O-N27) are un-struck headings. The registry strikes them (`:620`, `:646`), and their own text records the fix (`:648-651`, `:663-665`).

**E3-10 · stale · owner `nitpick-libs` · `PLAYBOOK.md:280-282`.**
- "`if (r.is_error) { #unreachable(); }` leaves `r.value` tainted at the pin `5fbaf4a` … it holds here until the re-pin that carries that landing". There is no dated note.
- `.internal/toolchain/7e91730/PIN.md:30-31` lists "DEF-225 at 93" among what the pin carries. `nitpick-time/CLAUDE.md:117` says O-N34 is struck.
- Fix: a dated note, as E2-3 did at its eight sites.

**E3-11 · stale · owner `nitpick-libs` · BOARD status lines.**
- `BOARD.md:12` "Last updated: 2026-10-09", while `:14` records a wake on 2026-10-15.
- In-flight rows `:10666-10667` repeat their first cells. s1 has `| s1 | `nitpick-regex` | | s1 | …` four times.
- In the s2 row, "Agent label" is "— (plan verifier next)" and "Since" is "2026-10-09 12:05". The Note cell is 2026-09-06's ("THE FIRST CYCLE CLOSED ANYWHERE IN THIS ECOSYSTEM"). The "Subcycle" cell holds today's close.
- The tools row T1 (`:10443`) is `CLAIMED orchestrator`, against the header's "from 2026-10-15 the fuzzer's M12 is `nitpick-fuzz_2`'s".

**E3-12 · stale · owner `nitpick-libs` · tools.**
- `tools/guard_compiler_tree.py:34-35`: "`filesystem.denyWrite`, which is configured nowhere (BOARD.md question 3)". Registry Q-3 `:25-26` says it was answered and applied 2026-10-01, and `PLAYBOOK.md:982` says the sandbox was deployed.
- `tools/canary.md:54-64` ends at `5fbaf4a` (56 213 B / 16). `PIN.md:41-42` records 56,903 B / 16 for `7e91730`. The file calls this "the one continuous number … at every re-pin" (`:5-6`).

**E3-13 · stale · owner `nitpick-libs` · the plugin's cycle 0.2.**
- `meta/roadmap/0.2/0.2.7.md:1` "RUNNING (since 2026-09-03, author)"; `:17` and `:42-55` have every pass-mark box unticked.
- The orchestrator has run the loop for six weeks and 100+ subcycles. Fix: tick it or write the close.

**E3-14 · unverified claim / stale · owners `nitpick-time`, `nitpick-parse` · pins the 2026-10-09 currency audit found superseded.**
- `meta/audits/currency-2026-10-09.md:11-12`: tzdata 2026c → 2026e; TOML v1.0.0 → v1.1.0.
- `nitpick-time/meta/research/CURRENCY.md:13` still says 2026c and "Whether it is still IANA's latest is not checked here". `roadmap/done/0.3/0.3.2a.md:96` only notes 2026e as "cycle 0.5's".
- `nitpick-parse/meta/specs/FORMATS.md:15,63` still says "TOML v1.0.0". This is main; the Team's branch was not readable.
- Fix: record the superseded fact beside each pin, or re-pin with a dated reason.

**E3-15 · dormant · owner `nitpick-regex` · "quote every hex value in a workflow" (`PLAYBOOK.md:1232-1237`).**
- `nitpick-time/.github/workflows/ci.yml:335-350` quotes them, with a comment saying why.
- `nitpick-regex/.github/workflows/ci.yml:136,141` leaves `NITPICK_COMMIT` and `NPKC_LL_SHA256` bare. Nothing checks it. Both pin `7e91730d19cf…`, LLVM 20.1.8 and the emission row `b79f89c5…`/31 527 001, equal to `PIN.md`.

**E3-16 · dormant · owner `nitpick-time` · O-X8 has no cycle.**
- `nitpick-time/meta/OPEN_QUESTIONS.md:836-838`: "What settles it: … `src/fmt`'s parser at cycle 0.4".
- `meta/roadmap/0.4/README.md:13-18` names only time's own question X-4, and the 0.4.2 checklist (`:81-89`) has no O-X8 item.
- It is read at `0.4.0.md:89`, and nothing owns its decision.

**E3-17 · stale (live status line) · owner `nitpick-libs`.**
- `meta/OPEN_QUESTIONS.md:400` (O-N36): "Each is discharged at the re-pin that carries it, the one after landing 115".
- The author's word of 12:04 is the one re-pin at 118, carrying 104 … 118. The `BOARD.md:10667` regex row has the same "Before the re-pin after 115 (landing 113 …)".
- Everything else I found saying "after 115" is dated and was left alone.

## THE EARLIER FINDINGS

**Early audit, E2-1 … E2-15**
- **E2-1 STILL OPEN.** `PLAYBOOK.md:76` is struck and `:88` dated. But `skills/plan/SKILL.md:38-41`, `skills/worker/SKILL.md:97-100` and `skills/audit/SKILL.md:35-39` still tell the T-113 story undated.
- **E2-2 FIXED.** `PLAYBOOK.md:58` (the `fixed T[]` row), `:188`, `:218`.
- **E2-3 FIXED** at its eight sites: `PLAYBOOK.md:188,210,260,275,554,616`, the S-108 row `:56`, and `:203-204,747`. Residue is E3-10.
- **E2-4 STILL OPEN.**
  - Workbench half FIXED: `PLAYBOOK.md:1322`, `orchestrate:108`, `new-repo:55-58`.
  - The four planned manifests are unchanged: `nitpick-tui/nitpick.toml:40`, parse `:40`, sockets `:40`, posix `:28` all read `20.1.2`. None has `triple` or `datalayout`.
  - The pin audits' TL-4, PL-4 and XL-4 cover the LLVM row only.
- **E2-5 FIXED.** `WORKSTREAMS.md:23,175,285-289`; `CLAUDE.md:26` says W-1…W-28.
- **E2-6 STILL OPEN.**
  - tui: `ROADMAP.md:208-211`; `OPEN_QUESTIONS.md:44-46` (Q-5, "in `examples/`"); `DECISIONS.md:617` (T-104, no supersede marker).
  - parse: `ROADMAP.md:184`.
  - regex is FIXED (`ROADMAP.md:351`).
- **E2-7 FIXED.** `PLAYBOOK.md:978-991`; registry Q-3 struck. Residue is E3-12.
- **E2-8 STILL OPEN.** `nitpick-posix/README.md:7-9` "Status: scaffolded … Nothing is implemented"; `meta/roadmap/ROADMAP.md:3` "seventeen decisions".
- **E2-9 FIXED** for every listed row.
  - Struck in the registry: O-N27 … O-N32 and O-N34 (`:460,517,531,560,600,620,646`), O-X9/X11/X12 (`:202,220,230`), O-Y2 (`:259`).
  - O-N33, O-N35 and O-N36 are correctly open (`OPEN_DECISIONS.md:2850,3927`). New rows are E3-9.
- **E2-10 STILL OPEN.**
  - `LIBRARIES.md:11,12,14` say 67, 43 and 35, against 69, 47 and 36 headings.
  - `APPS.md:10` says "17 decisions, 14 cycles", against 20 `### PX-` headings and 15 table rows.
  - `WORKSTREAMS.md:87` says "26 cycles"; it is 27.
  - `PLAYBOOK.md:1256-1260` says "eight" trees, against nine at `BOARD.md:12`.
  - `nitpick-tui/meta/roadmap/ROADMAP.md:6-8` stops at T-112; T-115 exists.
  - Spec counts still use two conventions: regex and time exclude `README.md`; tui, parse, sockets and posix include it.
  - posix `meta/roadmap/0.0/README.md:28` lists "PX-001 … PX-013, PX-020 … PX-023" and omits PX-014 and PX-100…102.
  - Regex and time are FIXED (`nitpick-regex/meta/roadmap/ROADMAP.md:6-8`, `nitpick-time/README.md:9`).
- **E2-11 STILL OPEN.** `README.md:104` is corrected. `agents/auditor.md:3,8-9` still says "Cannot write files … no file-writing tools" beside `:5` `Bash`.
- **E2-12 FIXED.** `meta/roadmap/README.md:10`, `0.2/README.md:3`, `meta/audits/README.md:4`, `orchestrate:54`. `BOARD.md:12` has gone stale again (E3-11).
- **E2-13 STILL OPEN.**
  - None of tui, parse, sockets or posix has a `CURRENCY.md` (each `meta/research/` holds a README; posix also `.gitkeep`).
  - tui `DECISIONS.md:556` (T-100, "15.1.0 floor") is undated.
  - posix is MOVED to PX-102 (`DECISIONS.md:282` schedules the row).
- **E2-14 STILL OPEN.** `WORKSTREAMS.md:53` (`PA --> PX11`) against posix `ROADMAP.md:55` (0.11 gated on 0.10 only); `:149` "nine ungated cycles"; `:55-61` `nitpick-logview` and `nitpick-conflint`, named in no registry.
- **E2-15 STILL OPEN.** The `check` skill table is FIXED (`SKILL.md:40-42,80`). The empty "What this is" heading (`CLAUDE.md:5-7`) remains in all four planned repositories, tui, parse, sockets and posix. Two more than the early audit listed.

**The 23 of 2026-09-26 that the early audit did not find FIXED**
- **EC1 STILL OPEN.** `LIBRARIES.md:175` and `PLAYBOOK.md:75` carry the correction (runtime check at `runtime/npkrt.ll:2087-2119`). Still uncorrected:
  - `nitpick-apps/APPS.md:79-93`.
  - posix `DECISIONS.md:116-125` (PX-011), `SAFETY.md:136-150`, `0.0.0.md:52,119`, `0.0/README.md:72`, `CONTRIBUTING.md:24`, `CLAUDE.md:35`.
  - tui `TERMINAL_MODEL.md:277-284`, `DECISIONS.md:727-730`.
  - sockets `SAFETY.md:17,50`, `CLAUDE.md:36-38`, `README.md:24-25`, `CONTRIBUTING.md:33`, `DECISIONS.md:137-141`, `ROADMAP.md:40`, `0.0.0.md:154-155`, `TESTING.md:81`.
- **EC2 STILL OPEN.** The same eight sites: tui `SAFETY.md:24`, `VERIFICATION.md:40`; parse `SAFETY.md:22`, `VERIFICATION.md:37`; sockets `SAFETY.md:28`, `VERIFICATION.md:40`; posix `SAFETY.md:20`, `VERIFICATION.md:16`. Also tui `CLAUDE.md:71` and sockets `CLAUDE.md:85` ("indexing traps"), new to the list.
- **EC3 STILL OPEN.**
  - tui `CONTRIBUTING.md:32`, `ROADMAP.md:55`, `SAFETY.md:20`, `TESTING.md:58`, `0.0.3.md:63`.
  - parse `README.md:36`, `ROADMAP.md:49`, `SAFETY.md:18`, `TESTING.md:57`, `0.0.3.md:63`.
  - sockets `CONTRIBUTING.md:46`, `SAFETY.md:20`, `TESTING.md:127`, `0.0.3.md:69`.
- **EC4, EC5, EC11, ED1, ED3, ES4 — previously FIXED, re-checked or unchanged.** Regex `harness/treecheck.py:92` and `:576`, `TESTING.md:239,241`.
- **EC6 — previously FIXED.** Not re-read; time's `ci.yml:491-513` shows the emission asserted.
- **EC7 STILL OPEN.** Sockets plans `src/option/raw.npk`: `OPTION_MODEL.md:12`, `DECISIONS.md:317`, `TESTING.md:132`, `0.7/README.md:3,16,25`, `0.0.3.md:74`, `ROADMAP.md:149`, `1.0/README.md:31`, `src/option/README.md:4`. `src/frontend/keywords.npk:38` still has `"raw"`. The playbook half is FIXED (`PLAYBOOK.md:1620`).
- **EC8, EC9 STILL OPEN.** See E3-4.
- **EC10 STILL OPEN.** Three Q-6s: registry `:49`, `RECORD.md:4552`, `BOARD.md:10965`; plus `PLAYBOOK.md:446` ("The board's Q-6").
- **EC12 STILL OPEN.** `StackExhausted|MachineFault` has 0 hits in `nitpick-posix`. `BOARD.md` schedules two arms for 02a/02d/02e at the pin that carries 109.
- **EU1 MOVED.** To PX-102 (`nitpick-posix/meta/DECISIONS.md:269-286`) and the editions digest. The 2017 mentions and the `CURRENCY.md` row are carried to its 0.0.1. Registry Q-1 is unstruck (E3-9).
- **ED2 STILL OPEN.** The registry has no hit for any of these subjects. Still live at the compiler: `IO_REFERENCE.md:149` (`io_isatty`), `:281-283` (sockets), `types.npk:1733` ("cross a spawn"), `rootlist_add` uncalled in `src/`. Local rows, each in its repository's own registry:

```
tui O-N3, O-N4; sockets O-N1, O-N3, O-N4 (`OPEN_QUESTIONS.md:39,58,68`); parse O-N2 … O-N4 (`:61,75,85`); time O-N2, O-N3 (`:245,254`); posix O-N7 (`:72`), which collides with the registry's "O-N7 — never existed" (`:1229`).
```

- **ES1 STILL OPEN.** See E3-1.
- **ES2 STILL OPEN.** `README.md:31-43` omits `nitpick-fuzz`, `nitpick-apps`, `nitpick-posix`. `:26` omits `ladder.py`, `floatscan.py`, `run_controls.py`, `canary.*`, `guard_domains.py`, `reinject_orchestrator.py`.
- **ES3 STILL OPEN.** All three items:
  - Registry `:246` "eleventh `ValueFault`", against `nitpick-time/meta/OPEN_QUESTIONS.md:815-816` "the sixteenth since cycle 0.2.0".
  - Registry `:31-33` Q-4 is open, against `WORKSTREAMS.md:225` W-24.
  - `PLAYBOOK.md:423` "drop it at DEF-95's notice", against the pin carrying DEF-95.
- **EK1 STILL OPEN.** `BOARD.md:10965` "replaces its `VERIFICATION.md` P-1". Sockets `VERIFICATION.md:28` and posix call it Z-1. The manifest half is under E2-4.
- **EK2 STILL OPEN.** Floating `@v4`: regex `ci.yml:158,161,194,228`; time `ci.yml:362,365,399,434`.
- **EK3 FIXED.** `nitpick-posix/meta/DECISIONS.md:94` "— *superseded by PX-100*". PX-002 (`:33`) is marked too.

## NOT CHECKED

- **No shell.** I could not confirm `../nitpick` HEAD, run `check_refs`, `check_record` or `gather_claims`, or compile a probe. The compiler was read at its working tree, not at `7e91730`, and never `build/`.
- **`NOTICES.md` and DEF-252…254.** The compiler's `NOTICES.md` rows are long lines that did not print. DEF-250…254 are absent from its `OPEN_DECISIONS.md`. I could not confirm the board's landing numbers 113-118 from the compiler's own documents.
- **BOARD.md and RECORD.md.** I read `BOARD.md` lines 1-159, parts of `:10425-10485` and `:10640-10667`, and the two in-flight rows (the regex row was cut off mid-line by the reader). Everything else in the two files was searched, not read.
- **Parse's Team branch.** `team/parse-0.0-plan` is outside main. `tui`, `parse` and `sockets` roadmaps and cycle READMEs were read only for 0.0, or by search. Their CONTRIBUTING files were read for tui, and for sockets only by search. No CI exists in the four planned repositories.
- **Regex and time.** Their `DECISIONS.md` and spec files were read by heading, count and search. Regex `harness/` and `tools/*.py` were read only for their docstrings; time's CLAUDE.md lines 786-1113 only by search.
- **Not read.** `START.md`, `RECORD.md` beyond cited lines, `.internal/credits`, `skills/audit/scripts`, `check_refs.py`, and `reinject_orchestrator.py`. `meta/roadmap/0.2/*.md` I read for headings and `0.2.7.md` only.
- **External facts.** tzdata 2026e and TOML 1.1.0 are taken from `currency-2026-10-09.md`; I fetched nothing. The sandbox's real settings are unreadable, so E2-7 is document against document.