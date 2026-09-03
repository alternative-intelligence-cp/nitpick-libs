# The record

The orchestrator's execution record (the compiler's R8): what was dispatched,
what came back, what it cost, which estimates were wrong and by how much,
which gates bound, which findings recurred, and every question answered.
Append-only; never rewritten. [`BOARD.md`](BOARD.md) is the present; this is
the past.

Entry vocabulary: `dispatch <label>` · `report <label> <status> <tokens>
<minutes>` · `verify <label> PASS|FAIL` · `advance <repo> <subcycle>` ·
`release <repo>` · `pin <commit>` · `stale claim <repo>: <found>, <done>` ·
`question Q-n answered: <answer>` · `rebalance: <what moved and why>` ·
`audit <repo> <cycle> filed` · `finding: <one line, and where it went>`.

## 2026-09-03

- workbench: cycle 0.2 planned and committed (`3f00d7d`); Q-2 answered by the
  author's flagless session (`5e8f464`); the first flagless `/npk:check` run
  found the check skill's control missing and a second writer in the
  workbench — both folded into the plan (`e6a94a7`)
- 0.2.0 executed in the author's planning session, named on the board as the
  workbench writer. Toolchain edits, one commit per repository:
  `nitpick-tui` e5439ee · `nitpick-parse` 3cad08c · `nitpick-regex` c056ae1 ·
  `nitpick-sockets` d385991 · `nitpick-time` aad6e45 · `nitpick-posix` 948d9b6
- finding: the "Where you are" bullet of every `0.0.0.md` also pointed at the
  compiler's `build/` ("whichever is current"); edited with the §2 command.
  `nitpick-posix/CLAUDE.md` had no build section, so it gained "The toolchain"
- 0.2.1 done: the worker skill rewritten for delegation from the workbench;
  `check_record.py` with an 11-case control; the reference check's promised
  control now exists, 7 cases. Both controls green on first run
- 0.2.2 done: the orchestrate skill carries the loop, the stop list, the
  dispatch template, the pin, recovery and escalation; `START.md` is one line
  plus arguments
- 0.2.3 done: the research skill, the currency table in planning and
  auditing, the first research request written for the POSIX edition (Q-1)
- 0.2.4 in progress: five agent definitions written; their live tests
  (names, skill preload, web tools, the auditor's inability to write, nesting,
  and 0.2.2's dry read) wait for a fresh session in the workbench
- 0.2.5 done: the guard scopes on the project directory, follows `cd`
  anywhere, enforces claims and the workbench writer; 73 cases, 29 ms a call.
  Two design findings: the board is the lock and must stay writable, and the
  hook's session id is the UUID, not the cloud id. The board's writer line
  was rewritten once through the interpreter hole to recover from the
  lockout the first rule caused — recorded here so it is never a precedent
- 0.2.6 in progress: the compaction hook with a 4-case control, the workbench
  `CLAUDE.md`, the README current; the live compaction test waits for the
  author's session. Remaining for the cycle: the live tests of 0.2.4 and
  0.2.6, then 0.2.7's dry runs
- writer takeover: `19afbe0e-419e-49e5-86db-c4d8260e417a` → `0a61670c-03a4-47dd-a063-44fd216c25b5`
  at 17:11. The planning session ended with everything committed (`02d4f61`);
  this session, started in the workbench with the plugin loaded from the
  symlink, continues 0.2.4's live tests, 0.2.6's compaction test and 0.2.7.
  Taken by the orchestrate skill's §2 procedure: the board is the lock
- pin 950bb1d: compiler 1.5.0 closed (`950bb1d`), LLVM 20.1.2,
  `.internal/toolchain/950bb1d/`, `sha256sum -c` OK. Made at 17:12 by the
  orchestrate skill's startup, run as 0.2.4's test 6 (the dry read): the
  startup ran through the picture and stopped before dispatch, because
  0.2.7 §1 wants 0.2.4 and 0.2.6 closed before the first worker
- 0.2.4 done: the six live tests ran from this session as agents, not as
  pastes — the five `npk:` types listed; the bare `skills:` spelling
  resolves; the researcher fetched three primaries; the auditor declined
  the write under A-1 and `probe.txt` does not exist; a worker relayed a
  nested researcher's digest; the orchestrate startup ran through the
  picture and the pin and stopped before dispatch by this session's
  judgement (0.2.7 §1). Tokens / seconds: worker-print 17,425 / 3;
  researcher 30,686 / 239; auditor 20,294 / 60; worker→researcher
  35,334 / 136 (the inner researcher about 13K / 46). Details in
  `meta/roadmap/0.2/0.2.4.md`
- finding: `$ARGUMENTS` sat in the orchestrate skill's prose as well as its
  table, so the substituted text misread; §0 now leads with "Given: …".
  Landed against 0.2.2
- question Q-1 digest, first entry (0.2.4 test 3, `budget: 3`; 0.2.7 §4 runs
  the request at its full budget). The next `nitpick-posix` worker files it
  under `meta/research/posix-edition.md`; the decision it feeds is a `PX-`,
  taken in that repository. Verbatim:

  ```text
  # POSIX edition — research digest

  **As of 2026-09-03.** Question: Is POSIX.1-2024 (IEEE Std 1003.1-2024, Issue 8) the current edition, is its XCU volume freely readable online, and what does it change in the utility set relative to POSIX.1-2017?

  ## Answer

  Yes on all three counts. IEEE Std 1003.1-2024 — simultaneously The Open Group Base Specifications Issue 8 and ISO/IEC/IEEE 9945 — is the current edition: IEEE SA lists it as an Active Standard, board-approved 2024-05-20, published 2024-06-14, superseding IEEE Std 1003.1-2017. A corrigendum (P1003.1-2024/Cor 1) is in progress, so a Technical Corrigendum 1 will eventually amend it; nothing has superseded it. The whole edition, XCU volume included, is served without login as HTML at `https://pubs.opengroup.org/onlinepubs/9799919799/` (utilities at `.../utilities/`, rationale at `.../xrat/`); a parallel path `9799919799.2024edition/` also exists, which by the pattern of the previous edition (`9699919799` vs `9699919799.2016edition`) is the frozen 2024 text while the unsuffixed path will track later corrigenda — pin whichever the plan wants. In the utility set, Issue 8 adds seven utilities (gettext, msgfmt, ngettext, readlink, realpath, timeout, xgettext — the internationalisation and path utilities from "Additional APIs for the Base Specifications Issue 8, Part 2") and removes twelve (fort77 and the entire Batch Environment Services family: qalter, qdel, qhold, qmove, qmsg, qrerun, qrls, qselect, qsig, qstat, qsub). The UUCP utilities (uucp, uustat, uux) are not on the removed list. The shell command language gains at least the `$'...'` dollar-single-quotes quoting mechanism (Austin Group Defect 249). The Utility Syntax Guidelines (XBD 12.2) remain fourteen guidelines with the same substance as 2017's; whether any wording changed could not be confirmed within budget (see gaps).

  ## Evidence

  - https://standards.ieee.org/ieee/1003.1/7700/ — retrieved 2026-09-03 — "IEEE/Open Group Standard for Information Technology--Portable Operating System Interface (POSIX™) Base Specifications, Issue 8"; Status: "Active Standard"; Board Approval Date "2024-05-20"; Publication Date "2024-06-14"; Supersedes "IEEE Std 1003.1-2017"; "POSIX.1-2024 defines a standard operating system interface and environment, including a command interpreter (or "shell"), and common utility programs to support applications portability at the source code level."; corrigendum in progress "P1003.1-2024/Cor 1" addressing "changes to correct accidental deviations from other existing standards and widespread existing industry practice."
  - https://pubs.opengroup.org/onlinepubs/9799919799/xrat/V4_xcu_chap01.html (XRAT Appendix C, Rationale for Shell and Utilities; fetched unauthenticated) — retrieved 2026-09-03 — header "The Open Group Base Specifications Issue 8 / IEEE Std 1003.1-2024"; "The Open Group Standard, 2022, Additional APIs for the Base Specifications Issue 8, Part 2 is incorporated."; "The utilities first introduced in Issue 8 (over the Issue 7 base document) are as follows: gettext msgfmt ngettext readlink realpath timeout xgettext"; "The utilities removed in Issue 8 (from the Issue 7 base document) are as follows: fort77 qalter qdel qhold qmove qmsg qrerun qrls qselect qsig qstat qsub"; "Austin Group Defect 249 is applied, adding the dollar-single-quotes quoting mechanism".
  - https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html (XBD Chapter 12, Utility Conventions; fetched unauthenticated) — retrieved 2026-09-03 — header "The Open Group Base Specifications Issue 8, IEEE Std 1003.1-2024"; Guidelines 1 through 14 present, e.g. "Guideline 3: Each option name should be a single alphanumeric character from the portable character set. The -W option shall be reserved for vendor options." and "Guideline 10: The first -- argument should be accepted as a delimiter indicating the end of options." (the fetch tool condensed the guideline text despite a verbatim request; treat these as substance, not exact wording).
  - Lead, not fetched: http://www.opengroup.org/austin/docs/austin_1435.pdf — Austin Group PAR "P1003.1-2024/Cor 1 Type of Project: Corrigendum to IEEE Standard 1003.1-2024" (title from search results only).
  - Lead, not fetched: https://pubs.opengroup.org/onlinepubs/9799919799.2024edition/idx/utilities.html — the Issue 8 utilities index, the right primary for rebuilding the full utility table.

  ## What would change this

  The request's condition — "the 2024 edition is current and its utility table or syntax guidelines differ from 2017's" — is met on the utility-table half: Issue 8 is current and the utility set differs by +7/−12. So the plan does change: nitpick-posix SCOPE.md's utility table must be built against Issue 8 (drop fort77 and the eleven q* batch utilities; add gettext, msgfmt, ngettext, readlink, realpath, timeout, xgettext), GLOSSARY.md "the standard" should name IEEE Std 1003.1-2024 / Issue 8 with the pinned URL, and CONFORMANCE.md K-1 should cite the 2024 edition and note that Cor 1 is pending. The syntax-guidelines half is not met as far as verified: fourteen guidelines, same substance as 2017's; no confirmed wording change.

  ## Confidence and gaps

  **High** that Issue 8 is current, freely readable, and adds/removes exactly the utilities listed (verbatim from the rationale volume, corroborated by the IEEE SA record). **Medium** on the shell-language changes: only the `$'...'` item was surfaced from the rationale page; other Issue 8 shell changes I recall but did not verify here (notably `set -o pipefail`) should be checked against the XCU `set` page before the plan cites them. **Unresolved at the budget (3 fetches used):**

  1. The CHANGE HISTORY of XBD Chapter 12 was not surfaced by the fetch, so whether Issue 8 reworded any Utility Syntax Guideline is unverified; one fetch of the same page's tail (or the XRAT A.12 rationale) settles it.
  2. The C compiler utility name: neither `c99` (removed list) nor `c17` (added list) appears in the retrieved lists, yet my unverified recollection is that Issue 8 provides `c17` in place of `c99`. If a rename is treated as neither an addition nor a removal, the lists above would not show it. One fetch of the utilities index resolves this; it matters for the utility table.
  3. A search snippet of the XRAT page states that `realpath` was added "in preference to a -f option found in some implementations of the readlink utility" — consistent with the fetched lists but not itself fetched; verify before citing.
  ```

- research digest for TM-100 (0.2.4 test 5, `budget: 2`, relayed through a
  worker). The next `nitpick-time` worker files it under
  `meta/research/tzdata.md` with the currency row it proposes. Verbatim:

  ```text
  # tzdata current release — research digest

  **As of 2026-09-03.** Question: What is the current tzdata release?

  ## Answer
  The current IANA Time Zone Database release is **2026c**, released **2026-07-08** (timestamp `2026-07-08 10:23:58 -0700`). Its changes: Alberta moved to permanent -06 on 2026-06-18; Morocco moves to permanent +00 on 2026-09-20 (a transition still in the future as of today, already encoded in this release); further integer-overflow fixes in `zic`. The prior release was 2026b (2026-04-22). Pin: `tzdata 2026c`.

  ## Evidence
  - https://www.iana.org/time-zones — retrieved 2026-09-03 — latest-version box: "2026c" / "Released 2026-07-08"; notes "Alberta moved to permanent -06 on 2026-06-18." / "Morocco moves to permanent +00 on 2026-09-20." / "More integer overflow bugs have been fixed in zic."
  - https://data.iana.org/time-zones/tzdb/NEWS — retrieved 2026-09-03 — first heading: "Release 2026c - 2026-07-08 10:23:58 -0700"; the next heading below it: "Release 2026b - 2026-04-22 23:06:43 -0700"

  ## What would change this
  The request said n/a; nothing to change. Suggested currency row for `meta/research/CURRENCY.md`:

  `| tzdata | 2026c | 2026-09-03 | iana.org/time-zones | TM-100 |`

  ## Confidence and gaps
  **High.** Two iana.org primaries fetched today agree on the version and date: the landing page and the release's own NEWS file (whose first entry is the current release). Budget of 2 fetches exhausted; the tarball directory listing at `data.iana.org/time-zones/releases/` was not opened, but the NEWS file is served from the current release's unpacked contents, so the artifact's existence is not in doubt. Note for TM-100: tzdata releases are frequent (2026a/b/c already this year) and Morocco's 2026-09-20 change may prompt a 2026d; this digest is routine, so it is re-checked at the repository's hardening cycle per §6, not on a 90-day clock.
  ```
- 0.2.6 pre-check: the marker holds this session's id, written by the
  orchestrate startup through substitution and equal to the transcript's
  name; the hook script prints the block for this id and nothing for
  another, by hand. The live test — the author's `/compact` in this
  session, loud with the marker and silent with it changed — is next;
  its procedure is in `meta/roadmap/0.2/0.2.6.md`
