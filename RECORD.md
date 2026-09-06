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
- 0.2.6 loud case passed: the author's `/compact` in this session restored
  the context with `SessionStart:compact hook success:` and the block
  verbatim — the hook is registered from the symlink-loaded plugin and the
  id it sees is the marker's. The silent case is next
- finding: `ListAgents` lists peer sessions on this machine by directory
  name and idle/busy state, which the orchestrate skill's takeover step
  (§2.1) said it could not; the step now consults it first — a
  `nitpick-libs-…` peer that is not you is a stop-and-ask, none is the
  takeover path. Landed against 0.2.2; seen in 0.2.6's loud case
- 0.2.6 done: the silent case passed — the author's second `/compact` in
  this session, the marker holding no session's id, restored the context
  with nothing from the hook. Same session, same registration, only the
  marker changed, so the marker check is what keeps the hook silent
  elsewhere. The marker holds this session's id again. Next: 0.2.7 §1's
  preconditions, then dry run one
- finding: the pin procedure (orchestrate §3) recorded no tree state; the
  950bb1d pin, taken at 17:12 from a tree that by 17:49 had eighteen
  modified files and a rebuilt npkc, may not be that commit's own build,
  and nothing can tell afterwards. §3 now writes `tree clean|dirty` into
  PIN.md and onto the `pin` line; the existing pin is marked `tree
  unknown`. Landed against 0.2.2; seen at 0.2.7's precondition check
- question answered (the pin's provenance, asked of the compiler session
  over SendMessage): the tree was dirty at 17:12 with uncommitted 1.5.1
  frontend edits, but build/ had not been rewritten since the 1.5.0 close's
  parity run, so the pinned npkc is 950bb1d's own build. PIN.md says so;
  orchestrate §3 now asks the compiler session when the tree is dirty and
  records a `binary` line. Landed against 0.2.2
- **writer takeover: `0a61670c-03a4-47dd-a063-44fd216c25b5`** by
  `6fb2f48d-250b-4880-879f-083132155bd9` at 18:16, the first orchestrator
  session (`/npk:orchestrate width=1 start=nitpick-time 0.0.0` — 0.2.7 §2's
  invocation verbatim). Grounds: `ListAgents` showed two peers, `nitpick-01`
  and `nitpick-76`, both compiler sessions, and **no `nitpick-libs-…` peer**;
  the predecessor's work was committed and the tree clean at `59821a4`. The
  one departure from orchestrate §2.1's takeover test is that its last entry
  was **three minutes old**, not hours — recorded because the test says hours.
  `ListAgents` lists idle sessions (`nitpick-01` is idle and listed), so an
  idle predecessor would have appeared; and the author starting an
  orchestrator here is itself the handoff. Noted as the one judgement call of
  the startup
- finding: orchestrate §2.1 tells the taker to write the marker first and the
  board second, and the guard refuses exactly that — the marker write is a
  redirection into the workbench and the board still named the predecessor.
  The refusal was correct and its message said what to do ("take the lock:
  set the `Workbench writer:` line ... the board itself is always writable").
  **The order in §2.1 is backwards for a takeover**: board first, then
  marker. Landed against 0.2.2; seen at 0.2.7's dry run one. Not a run
  failure — the guard refused nothing the run needed, it refused a
  mis-ordered step and named the fix
- pin: no re-pin. `950bb1d` stands, `SHA256SUMS` verified at startup, the
  compiler still at that commit; W-18's "never re-pin while a claim is in
  flight" and 0.2.7 §8 both point the same way
- dispatch `s2-ntime-0.0.0-1817` — `nitpick-time` 0.0.0, the eleven language
  probes, stream 2, `npk:worker` on `claude-opus-5`, toolchain `950bb1d`,
  tree clean. The first library subcycle in the ecosystem, and 0.2.7 §2's
  dry run one
- dispatch `research-posix-edition` — `npk:researcher` on `claude-opus-5`
  with 0.2.3 §5's request verbatim (Q-1, the POSIX edition). 0.2.7 §4: sent
  after the worker was dispatched and before its report, so the run measures
  a helper running alongside a worker. A helper does not count against
  `width=` (W-24)
- report `research-posix-edition` PASS, 28,571 tokens, 3.4 minutes, 15 tool
  uses. 0.2.7 §4's pass condition met: the skill's shape, eight primary
  sources, a retrieval date on every one
- **question Q-1 answered: yes, POSIX.1-2024 (IEEE Std 1003.1-2024, Issue 8)
  is current** — published 14 June 2024, Active at IEEE SA, freely readable
  without login at `pubs.opengroup.org/onlinepubs/9799919799`. The
  `would-change-the-plan-if` trigger **fired, on one half of two**:
  - the **utility table changed by 19 entries** — seven added (`gettext`,
    `msgfmt`, `ngettext`, `readlink`, `realpath`, `timeout`, `xgettext`),
    twelve removed (`fort77` and the whole eleven-utility Batch Environment
    `q*` set, obsolescent in Issue 7), one renamed (`c99` → `c17`). 160
    utilities in Issue 7, 155 in Issue 8. Derived two independent ways that
    agree: XRAT's own change history and a diff of the two utility indexes
  - the **fourteen Utility Syntax Guidelines did not change** — G3, G5, G8,
    G11, G13, G14 byte-identical across editions, `-W` reservation and all.
    So anything in `nitpick-posix` resting on the guidelines survives the
    edition bump untouched, which is most of `CONFORMANCE.md` K-1
  Two gaps the digest names and did not close, each worth its own request:
  XCU chapter 2's shell-language additions, and per-utility option changes.
  One inference rather than a quotation: the `c99` → `c17` rename. Citation
  advice recorded with the digest — cite the frozen
  `/9799919799.2024edition/` path in a conformance corpus and the rolling
  `/9799919799/` path for "the current standard", because Cor 1 is an active
  IEEE project and will move the rolling one. The full digest is in this
  session's transcript; **the next `nitpick-posix` worker files it at
  `nitpick-posix/meta/research/posix-edition.md`** and amends `SCOPE.md`,
  `CONFORMANCE.md` K-1 and `GLOSSARY.md` from it. Not a stop: no stream is
  on `nitpick-posix`, so this is a fact waiting at the door rather than a
  question
- **the takeover's anomaly, explained by the author.** The predecessor's last
  entry being three minutes old rather than hours had a cause: 0.2.7 §2's
  invocation is printed as a bare fenced command under "Invocation, in the
  workbench", the predecessor handed it over at its close, and the author
  read it as an instruction to run it fresh — **restarting the terminal**,
  which ended that session, and opening this one. So the predecessor was not
  merely absent from `ListAgents`; it was killed, deliberately if not
  knowingly, before this session existed. The takeover was correct and the
  judgement call is discharged
- finding: **a command handed to the author must say which session to run it
  in.** 0.2.7 §2's did not, and cost a live session mid-cycle. Three cases
  and they are not interchangeable — here in this session (say so; do not
  rely on it being obvious), in a second session with this one left running
  (say why it must stay alive), or in a fresh session because this one is
  finished. Landed against 0.2.7 §2; the same fix belongs in any close
  handoff a worker writes
- report `s2-ntime-0.0.0-1817` **STOPPED**, 164,583 tokens, 40.9 minutes, 67
  tool uses. The first library subcycle in the ecosystem, and it stopped the
  stream on a compiler defect — which is W-11 working, not W-11 failing
- **O-N4 raised: `npkc` is quadratic in the size of one declaration.** Three
  independent axes, every point checked at `npkc` exit 0: array-initialiser
  elements (500→30 000 rows: 0.19 s/31 MiB → **281.35 s/30.9 GiB**, a ratio
  near 4 per doubling in both columns), statements in one function body
  (1 000/2 000/4 000 → 0.87/2.27/7.03 s), and bytes in one string literal
  (60 k→480 k → 5.24/22.72/78.11/**308.12 s**, memory flat, so a second
  pathology rather than the first seen through a lexer). Controls locate it
  precisely: an unread table costs the same as a read one, so the cost is in
  the *declaration*; and 4 000 separate `fixed int64` bindings cost 0.61 s
  against 4 000 elements in one array's 4.19 s, so it is the size of **one**
  declaration and not the count of constants. TM-007's tzdb is 26 838 rows.
  Consequence: a 16 GiB machine cannot build `ntime`, CI cannot, and every
  consumer pays it. Q-2 on the board; the reproduction is
  `nitpick-time/tests/probe/defect/`
- verdicts recorded: **probe 01 ACCEPTED** — `#[derive(Ord)]` follows
  declaration order, proven rather than observed by a reversed-field twin
  holding width, alignment, signedness and name constant. TM-011 stands.
  **probe 04 ACCEPTED** on semantics — the table is emitted as
  `constant [30000 x …]` in `.rodata` at 0x75300 = 480 000 B = 30 000 × 16,
  with zero `llvm.global_ctors`, so TM-007, Z-7 and S-19 stand as written.
  Probe 04's *answer* is yes; only its *cost* is the defect
- finding: **a timing without an exit code is not a measurement.** The
  worker's own first pass recorded five "fast" configurations that were
  `NITPICK-PICK-003` and `NITPICK-REACH-002` failures stopping early, and
  drew the wrong conclusion before checking. It caught itself and rebuilt the
  table with exit 0 on every point. Goes to `PLAYBOOK.md` as a measurement
  rule — this will recur in every library that measures anything
- finding: **`failsafe`'s `pick` over `Error` must carry `(*)` AND name every
  reachable identity.** The wildcard discharges PICK-003 exhaustiveness and
  counts for nothing against REACH-002. `PLAYBOOK.md` §3's error-budget
  section states the second half and not the first; the orchestrator lands
  the amendment (W-16)
- Q-4 raised, blocking nothing: `npkc` accepts a root file whose `mod:`
  differs from its basename when a sibling carries that basename, silently
  merges both files into one module, and emits two `define i32 @main` at
  exit 0; `llc` refuses the IR. The resolver's `NITPICK-RESOLVE-005`
  diagnostic for the same rule is exemplary — it simply is not applied when
  the given name resolves to a different file. Costs `ntime` nothing
- check `s2-ntime-0.0.0-1817` **FAIL** — `check_record.py` exit 1,
  `[no-report] no REPORT block under '## Execution record'`. The worker left
  the whole subcycle uncommitted by design, reading the worker skill's §4 as
  wanting a dirty tree for its successor; but W-20 wants the report in the
  tree as well as in the message, and a session loss would have taken both
  probe verdicts, the O-N4 reproduction and the defect README with it. Per
  orchestrate §7 the finding precedes the status: re-dispatched as
  `s2-ntime-0.0.0-1902` to land the record **only**, explicitly barred from
  working another probe or re-running the 30 000-row case
- dispatch `s2-ntime-0.0.0-1902` — the record only, tree dirty. The stream is
  stopped on O-N4 either way; this is W-20, not progress
- **Q-2 routed, not relayed.** O-N4 and Q-4's narrow resolver defect sent to
  peer session `nitpick-76` over `SendMessage` at 19:06 — the compiler
  session, identified as the `nitpick-…` peer that was in `shell` state
  mid-harness at startup and that answered the pin-provenance question at
  18:08. Sent with all three curves, the three locating controls, the
  measurement-discipline warning about PICK-003/REACH-002 early exits, and
  the reproduction path; explicitly asking for no schedule. It is told to say
  so if it is not the session working `npkc`'s frontend. The author's
  standing instruction is to ask the implementing agent rather than route a
  question through him, and W-11's escalation is the orchestrator's to make
- **question Q-3 answered by the author: work the nine.** Probes 02, 03 and
  05–11 proceed against the current `950bb1d` pin; only probe 04's cost waits
  on the re-pin. Width stays 1 — 0.2.7 §5 gates width two on dry run one
  passing, and dry run one is still open, so going wide now would jump its
  own plan. The two alternatives offered were idling stream 2 (buys no
  correctness, costs the calendar, since the nine are genuinely independent
  of a resource defect) and opening stream 1 alongside
- Q-2 and Q-4 leave the author's table by being raised: tracked on the board
  as **O-N4** and **O-N7** under compiler dependencies, where the other
  outstanding compiler requests already live. The questions table is empty
  again
- the nine-probe dispatch waits on `s2-ntime-0.0.0-1902`, which is still
  landing the record. One worker per subcycle and one writer per repository
  (W-7, W-15): a second worker into `nitpick-time` now would be the exact
  collision the board exists to prevent, so the answer is queued rather than
  acted on immediately
- report `s2-ntime-0.0.0-1902` **STOPPED** (unchanged status, the record
  errand only), 66,911 tokens, 5.2 minutes, 25 tool uses. Commit `8066e62`
  on `main`, subject `cycle 0.0.0:`, trailer exactly the attribution passed
  in the dispatch and no model of its own
- check `s2-ntime-0.0.0-1902` **PASS** — `check_record.py nitpick-time 0.0.0`
  exits 0, "record clean". The re-dispatch closed the W-20 gap it was sent
  for and did nothing else: no probe written, no verdict changed, the
  30 000-row case not re-run
- **write scope held.** `git status --porcelain` in `nitpick-parse`,
  `nitpick-regex`, `nitpick-sockets`, `nitpick-tui` and
  `nitpick-apps/nitpick-posix`: zero changes in every one. Every write of
  this subcycle landed under `nitpick-time/`, which is 0.2.7 §2's line and
  the guard's whole purpose
- dispatch `verify-ntime-0.0.0` — the verifier on `8066e62`, six checks.
  Dispatched **after** the record worker rather than beside it: both would
  have been in `nitpick-time` at once, and a verifier that runs `git status`
  while a worker writes gets a spurious FAIL. W-7 costs two minutes here and
  is worth them. Two constraints in the brief that are worth keeping for
  every later verification of this kind: it is **barred** from compiling
  probe 04 (281 s, 30.9 GiB would drive this machine into swap while other
  sessions work on it) and capped at ~2 GiB RSS with `/usr/bin/time` on
  every compile; and it is asked to **regenerate O-N4's curve independently**
  at 1 000/2 000/4 000 rows, because those numbers have already gone to the
  compiler session and a wrong defect report costs that session real time
- **O-N4 and O-N7 accepted by the compiler session**, replying at 19:26. It
  confirms it is the right recipient — the `src/` writer on `npkc`'s frontend
  for 1.5.1 under D-228 R2 — so the routing guess from `ListAgents` state was
  correct. Both are recorded on that side as **DEF-1** and **DEF-2** in
  `meta/roadmap/OPEN_DECISIONS.md` §2f, each with an owner and a
  recommendation: a dedicated subcycle **1.5.1b** immediately after 1.5.1
  closes and before 1.5.2, `src/` work, one commit per defect under a full
  harness, **DEF-1 measured before it is touched so the fix is a number**,
  our `big_fixed_array_cost.npk` as the regression case, and the workbench
  re-pins when it lands. **Provenance caveat, recorded in the same spirit as
  the pin's `tree dirty` line:** that text is in the compiler's working tree
  and not on `main` — its docs commit rides with 1.5.1's close, a few hours
  out, with four prefix harnesses running on 1.5.1's remaining steps now. So
  DEF-1 and DEF-2 are real commitments by a live session but are not yet
  citable at a commit
- the compiler session **declined to guess a cause**, which is the right
  answer and worth recording as the shape of a good defect hand-off. Its
  three suspects, to be measured rather than assumed: an accumulating
  `string_concat` per element or per byte (the shape 1.4.8's process-capture
  bug had), a per-node window copy in the AST scratch pool, and a
  per-statement re-walk in the checker or the obligation walk. It agrees the
  flat-memory string axis is a separate pathology
- **the schedule is the author's**, and that session says it is telling him
  directly rather than through this one — the same standing instruction that
  sent the defect there in the first place. Nothing here waits on it: Q-3's
  answer stands and the nine probes proceed against the current pin
- correction to this board's own O-N4 row: it said "blocks `ntime` 0.0.1
  onward", which was wrong. Cycles 0.0.1–0.0.4 carry no large declaration
  and are unaffected. What O-N4 blocks is **0.0.5**, the tzdb size spike,
  which must compile a real emitted table, and **0.5**, the generator — and
  the library's shipping shape. Fixed on the board; recorded because an
  overstated block is how a stream idles for no reason
- finding, against the orchestrator itself: in the acknowledgement sent to
  the compiler session at 19:31 I wrote that O-N4's curve was "verified
  independently on this side as of now". **It was not** — the verifier was
  dispatched and had not reported. Corrected to that session within the
  minute, before it could cite it, with the instruction not to spend 1.5.1b
  time on DEF-1 if the verification contradicts the curve. This is
  structurally the same error the worker recorded against itself one layer
  down — it timed files that only looked fast because they failed early;
  I reported a result I had not received — and it is worse in one way,
  because it left this repository in a message to another team. The rule the
  system already has covers it and I did not apply it to my own outbound
  claims: **nothing moves before the verifier answers, and that includes a
  sentence.** Goes to `PLAYBOOK.md` alongside the measurement rule
- **O-N4 confirmed independently by the compiler session**, on a different
  build and a different tree — `main`'s `efd6a4d` (1.5.1 step 1) plus 1.5.1
  steps 2–5, on a machine running four harnesses — using our committed
  4 000-row file and three regenerated from its shape, every point checked
  for exit 0: 1 000 rows 0.49 s / 56 MiB · 2 000 1.31 s / 148 MiB · 4 000
  5.88 s / 580 MiB · 8 000 17.49 s / 1.86 GiB. Ratios ×2.7/×4.5/×3.0 in time
  and ×2.6/×3.9/×3.3 in memory. Quadratic, and matching our curve within the
  load noise. **DEF-1 no longer rests on one agent's numbers**, which is what
  my premature "verified" claim had wrongly asserted an hour early and what
  is now actually true, by a better route than the one I claimed
- **the measurement trap caught the compiler session on its first attempt**,
  which is the finding's real evidence. Its regenerated files kept the
  original `mod:` header, so every one "compiled" in 0.04 s at exit 1 —
  `RESOLVE-005`, a *different* diagnostic from the `PICK-003`/`REACH-002`
  that caught our worker, and the identical failure mode. Two independent
  agents, two different diagnostics, one week. That generalises the rule from
  an anecdote about `failsafe` into a rule about measuring anything with
  `npkc`, and it is why it went into `PLAYBOOK.md` §6 as its own paragraph
  rather than as a footnote to the error budget
- `PLAYBOOK.md` amended in three places (W-16, the orchestrator lands these):
  §2's file-name subsection gains O-N8's silent-merge case, so that "a build
  that mysteriously grows a second `main` is this, not your program"; §3's
  error budget gains item 6, that `(*)` and the named arms discharge each
  other's obligation not at all, with the fast-failure consequence spelled
  out; §6 gains O-N4 with its three axes and controls, and the measurement
  rule as a standing paragraph
- **correction: `O-N7` never existed.** I numbered the resolver defect `O-N7`
  on the board and in the playbook before reading this ecosystem's own rule —
  `meta/OPEN_QUESTIONS.md` §"For the compiler" says a new ecosystem-wide
  request takes the next free number **from O-N8 on**. It is **O-N8**. The
  live documents are renumbered; the `O-N7` in the RECORD entries above
  stands, because this file is append-only and is never rewritten, and the
  registry carries a struck `O-N7` entry so the reference still resolves.
  Found by `check_refs.py`, which also caught that O-N4 and O-N8 were cited
  in three documents and defined in none — both now registered. The check has
  now paid for itself twice on the day it went live
- the O-N7 misnumber **never propagated**: the compiler session confirms its
  `OPEN_DECISIONS.md` §2f had only ever cited O-N4, for DEF-1, and DEF-2 now
  carries "their O-N8" as a cross-reference. So the cost of the mistake was
  one message and three renumbered lines, caught inside the hour by
  `check_refs.py` rather than by a reader six weeks later. It also agrees the
  exit-code discipline generalises — two unrelated fast-fail causes under one
  rule — and will cite it when 1.5.1b's measurement stage is written
- verify `s2-ntime-0.0.0` **FAIL**, 138,518 tokens, 17.4 minutes, 32 tool
  uses, on commit `8066e62`. Six checks: 1 tree/commit **confirmed**, 2 both
  reference checks **confirmed**, 3 probe 01 **confirmed**, 4 probe 04's IR
  claims **unverifiable**, 5 O-N4's committed magnitude **falsified**, 6 the
  quadratic shape **independently corroborated**. The FAIL is on two record
  defects; the subcycle's conclusion survives all six
- **check 3, the one that matters most for the library: probe 01 is real.**
  The verifier read the probe rather than trusting its exit code and worked
  out for itself that `Flip`'s reversed twin makes the result unreachable by
  any width-, alignment-, signedness- or name-based ordering, because each of
  those is fixed per field and would pick `a` in *both* structs. Declaration
  order is proven, not merely consistent with. TM-011, S-14 and M-6 stand
- **check 4: probe 04's IR claims are not backed by anything in the tree.**
  The record states `constant [30000 x …]` in `.rodata` and zero
  `llvm.global_ctors` as narrative prose; `git ls-files` shows no `.ll`, no
  `readelf` output, no log anywhere in the repository — and probe 04's own
  header comment promises the record "records what they showed". Row count
  (30 000) and the 16-byte row arithmetic are confirmed by inspection; the
  emission-shape claims are unverifiable without paying 281 s and 30.9 GiB.
  **I repeated those claims to the author as established.** They are not
- **check 5: the committed file does not cost what the record says.** Three
  runs of the exact harness line, exit 0 every time: 6.19 / 5.30 / 5.34 s,
  593 992 / 593 620 / 593 592 KiB — memory reproducible to under 0.1%, so
  this is not the CPU contention the verifier also documented (four
  `builder` processes at ~100%, load 4.6–5.7). The record says 4.19 s /
  473 MiB. The cause is a **conflation**: 4.19 s / 473 MiB is the
  *generic-recipe* 4 000-row point, and the committed file carries the real
  long identifiers. Two different measurements, one number
- **the verifier found something nobody had controlled for: identifier
  length changes the cost.** Same 4 000 rows, diff-confirmed identical row
  data, names alone varying — generic `R`/`T`/`a`/`b` 388.7 MiB; real
  `ZoneTransition`/`TRANSITIONS`/`at_utc`/`type_index` 534–542 MiB; the
  committed file, differing from that only by a nine-character-longer module
  name and two comments, 579.8 MiB. A ~33% swing from names at fixed element
  count. Relayed to the compiler session **explicitly labelled as one
  unreproduced measurement**, not as established, because it fits its
  `string_concat`-per-element suspect and would also explain the third
  axis being quadratic in time with flat memory — same accumulation, nothing
  structural retained. Aiming its measurement stage is worth more than
  waiting to be certain, provided the uncertainty travels with it
- **check 6: the phenomenon is now corroborated three independent ways** —
  our worker, the compiler session on a different build, and this verifier:
  1 000 → 0.37 s / 49 856 KiB · 2 000 → 1.03 s / 121 456 KiB · 4 000 →
  3.95 s / 397 940 KiB, ratios 2.78×/2.44× then 3.83×/3.28×. O-N4 stands.
  What does not stand is any absolute number in our README as a baseline
- the verifier wrote nothing under `REPO` — its reconstructions went to the
  session scratchpad, as its own report says and as `git status` confirms
- dispatch `s2-ntime-0.0.0-2003` — two commits in a fixed order, the record
  corrections before any probe. Ordered rather than split into two dispatches
  because both are the same subcycle (W-15) and a third record-only errand
  would cost a round trip; ordered rather than left to the worker's judgement
  because this run has already shown a worker skipping the record half when
  it had interesting work beside it. The nine probes are commit 2, carrying
  Q-3's answer. The subcycle's status stays STOPPED on O-N4 however the nine
  come out, and a second stop among them is to be reported, not worked through
- report `s2-ntime-0.0.0-2003` **STOPPED** (a second stop, a different one),
  231,505 tokens, 27.4 minutes, 93 tool uses. Commit 1 landed as `4b35886`;
  commit 2 is built and uncommitted
- verify follow-up: the worker **re-measured the committed reproduction
  itself** — 6.11 s / 593 796 KiB, exit 0 — agreeing with the verifier's
  three runs to within 0.1%, so the magnitude correction rests on two
  independent agents rather than on one contradicting another. The 4.19 s /
  473 MiB attribution is corrected in the defect README, the reproduction's
  own header, the execution record and the previous REPORT block, the last
  **marked as corrected rather than silently rewritten**, which is the right
  instinct and is now the house pattern
- **the worker beat its brief on the evidence item.** Told to evidence probe
  04's emission shape at an affordable size, it split the probe's two
  questions — whether 30 000 rows compile needs 30 000 rows; what the
  declaration is *lowered to* does not — and committed
  `probe04b_emission_shape.npk` at 300 rows (0.16 s, 28 MiB) with
  `probe04b_emission_shape.txt`, the whole transcript verbatim, every
  command's exit code included. It shows **more** than the original prose
  claimed: `= constant [300 x …]` with the `global` spelling returning zero
  hits, no `llvm.global_ctors`/`global_dtors`/`appending` globals, `.rodata`
  flagged `A` and not `W`, and — the part the prose never reached — in the
  **linked** program the symbol at `0x200790` inside a LOAD segment mapped
  `R` alone with no `.init_array` anywhere. Symbol size 4800 = 300 × 16
- **and it argued against the finding I had just relayed.** The verifier's
  generic 4 000-row figure (398 036 KiB) does not reconcile with the curve's
  own generic 4 000-row cell (473 MiB); and the committed file differs from
  the middle reconstruction by only a nine-character module name and two
  comment lines yet costs ~8% more. Both point at **total source bytes**
  rather than identifier length — which would make it axis 3 again rather
  than a fourth axis, and would *unify* the three axes instead of adding to
  them. Recorded in the defect README beside the verifier's numbers. Relayed
  to the compiler session, which has the better instruments and whose
  `string_concat` suspect this fits even better
- **probe 02 is a NEGATIVE verdict, and it changes the library.** `=>!` from
  `int128` to `int64` does **not** trap on a value that does not fit — it
  truncates silently, pinned in four shapes including a *positive* `int128`
  narrowing to a *negative* `int64`. And `=>` at a narrowing is not a runtime
  check but a compile error, `NITPICK-TYPE-009`. **There is no checked
  narrowing in the language.** So each of `SPAN_MODEL.md` §5's three `int128`
  sites needs an explicit runtime range check as ordinary library code, which
  is TM-105 plus `SAFETY.md` S-15b and `SPAN_MODEL.md` N-20b. This is 0.2.7
  §2's case exactly: a negative probe verdict is the subcycle doing its job,
  not the dry run failing
- **O-N9 raised — the second stop.** `string_bytes` on a local `string`
  yields a `uint8[]` that returns out of its owning frame with no diagnostic
  and reads freed memory; measured, the caller reading byte 0 gets something
  other than what was written. The same position with an `@`-borrow is
  refused (`NITPICK-BORROW-001`, "a borrow cannot travel up … (D-004 rule
  2)"), and so is a struct literal holding `@local`. So D-004's rule is
  documented, enforced for one form and not the other, and D-186's inventory
  of view-makers does not account for this direction. Registered as **O-N9**
  — checked against the registry's rule this time rather than invented
- `PLAYBOOK.md` §2's "Two facts that only measurement produced" is now
  "Facts…" and carries three more: no checked narrowing exists; D-004 is
  unenforced for slice views, with "a view is a parameter, never a return
  value" as the house rule until O-N9 lands; and `_~argv` marks a parameter
  discarded, `NITPICK-TYPE-007` if read. §6 gains **evidence a claim at the
  size you can afford**, with the rule that a committed verbatim transcript
  is evidence and a prose summary is not — which is what failed here
- **question Q-5-as-numbered (registry Q-8) answered by the author: O-N9 is
  BLOCKING, against this orchestrator's recommendation.** The recommendation
  was that obeying a documented language rule is conformance rather than a
  workaround, so O-N9 need not block. The author ruled otherwise and the
  ground is a good one: a rule enforced only by a harness check the library
  writes for itself is a thin guarantee for a use-after-free, it protects
  only the code that remembers it, and it protects no consumer at all. So
  `src/fmt/` work waits for the compiler, probes 09 and 10 are held, and the
  `SAFETY.md` rule plus `check_no_view_returns` are kept as a **belt, not as
  the guarantee**. Recorded as an override, which is what R8's record is for.
  The ruling was made **before** the compiler session's scheduling message
  arrived, so it was decided on the merits and not on the timeline — and it
  turned out cheap, because DEF-3 lands in 1.5.1b hours out
- **correction, and a worse one than O-N7 because it resolved silently: the
  board's questions Q-2, Q-3 and Q-4 collided with three existing questions.**
  `meta/OPEN_QUESTIONS.md` already held Q-1 (the POSIX edition), Q-2 (the
  plugin symlink, answered), Q-3 (the sandbox's `denyWrite`) and Q-4 (the
  default width). I numbered from the board's empty questions table instead of
  from the registry, so this session's four questions took Q-2, Q-3, Q-4 and
  Q-5, and three of them silently meant something else. They are now **Q-5,
  Q-6, Q-7 and Q-8** in the registry, each struck with its answer and each
  naming the number it briefly carried. `RECORD.md` keeps the wrong numbers
  in the entries above, being append-only
- **finding, against `check_refs.py`: it catches a question referenced and
  never defined, and not a question defined twice.** A re-used number
  resolves, so the collision above passed every run of the check until a
  human — this orchestrator, looking at the registry for an unrelated reason —
  noticed that Q-1 meant the POSIX edition in one file and something else on
  the board. The `O-N` section of that same file already carries a paragraph
  explaining that `O-N` numbers collide across repositories and must be
  registered centrally; the `Q-` section has no such paragraph and needed one.
  A duplicate-declaration check belongs beside the existing
  `[duplicate-decision]` rule, which does exactly this for `D-` numbers.
  Recorded against the check skill (0.2.1) for the workbench's next cycle
- **D-246's scope, answered precisely by the compiler session: the leak is at
  OWNING temporaries only.** A temporary leaks iff its type drops (the
  checker's `type_drops`). It does for a `string` whose body is on the heap —
  `string_concat`, **`string_slice`, an owned copy since D-186**,
  interpolation, `ToString` — and for a `buffer`, a struct or enum with an
  owning field or payload, a `dyn` (it owns its cell), and an `OwnedFd`. It
  does not for a `uint8[]` from `string_bytes`, a `string` from
  `string_from_bytes`, a range-view `arr[lo...hi]`, a plain pointer or any
  scalar. So `f(string_bytes(s))` needs no binding and
  `f(string_concat(a, b))` leaks the whole concatenation. That `string_slice`
  allocates is worth its own attention in a parsing library
- **correction to my own playbook entry, caught by the compiler session: I
  wrote `let a = g(x)` into the Nitpick playbook and there is no `let`.** The
  bound form is `T:a = g(x);`, naming the type. Fixed. It is a small error
  and an instructive one — the playbook exists so that six libraries do not
  each rediscover the language, and an entry that spells a keyword the
  language does not have would have taught the opposite. The general lesson:
  when landing a language fact reported by an agent, the *prose* is the
  agent's but the *syntax* must come from a compiled example or a
  specification, never from the summary
- the caution that came with it, kept in the playbook's wording: binding does
  not help if the bound value is then passed with `move` into something that
  leaks it further — but that is ordinary ownership rather than D-246, and it
  is the library's bug instead of the compiler's
- **peer handoff notice from the author.** The compiler session is handing off
  to a fresh session so an update installed there can be applied; this
  workbench will do the same at a quieter moment, when nothing is running in
  the background. The outgoing compiler session will name its successor to
  this session. Consequence for the record: **`nitpick-76` is a session name,
  not a durable address** — every reference to it above means "the compiler
  session as of 2026-09-03", and a future session must re-identify its peer
  from `ListAgents` and the announcement rather than reusing the name
- 0.2.7's §3 measurements moved out of the session scratchpad and into that
  file's execution record, ahead of either handoff. The scratchpad lives under
  a session-specific path in `/tmp` and a successor would not inherit it —
  the same "finished work left outside the tree" failure this run has already
  recorded three times against workers, and it would have been mine
- **the measurement that should change a plan: one subcycle has cost four
  worker dispatches and is not finished.** W-15's "one fresh worker per
  subcycle" did not survive contact — three of the four were re-dispatches,
  and two of those existed only to make a worker commit work it had already
  done. W-4's recalibration should count dispatches, not subcycles, or it
  will estimate the next repository from a number that was never true here
- **the compiler session handed off: `nitpick-76` → `nitpick-36`.** Every
  reference to `nitpick-76` in this record means "the compiler session as of
  2026-09-03". The successor has this workbench's address and a standing
  instruction to message it at 1.5.1b's landing with the commit, the `build/`
  fact the re-pin needs, and the after-numbers on our own recipes — so the
  re-pin should need no round trip, which is what the fourth rider asked for
- **1.5.1b is planned and ratified by the author**, `meta/roadmap/1.5/1.5.1b.md`
  at the compiler's `4bf3e47`, starting when 1.5.1's last four steps land.
  Five commits: **DEF-2** (our O-N8) first because it is independent, **DEF-3**
  (our O-N9), **DEF-1**'s three backend text builders (our O-N4), then
  **D-246** statement-end temporaries and **D-247** `List<T>` as owning. All
  three of this workbench's defects are in one batch, which is why the
  author's ruling that O-N9 blocks turned out to cost almost nothing
- **D-248 lands with them and touches every library: `mod:<basename>;` becomes
  the mandatory FIRST declaration of every source file, and `main`/`failsafe`
  may be declared only in a program's root file.** Checked the exposure rather
  than assuming it: all seventeen `.npk` files in `nitpick-time` and all eight
  in `nitpick-posix` already lead with `mod:<basename>;`, so the ecosystem
  complies today and the re-pin is free if new files keep to it. The one shape
  D-248 forbids that anybody here has written is `nitpick-posix`'s
  `tests/probe/shared/pxfail.npk` — a macro in a shared module expanding to a
  `failsafe` — and that is a **negative** probe recording `MACRO-007`'s
  refusal rather than live code, already replaced by PX-100's generator. Its
  recorded diagnostic will change after 1.5.1b, which is a note for stream 3
  and not a problem. Landed in `PLAYBOOK.md` §2 as a write-to-it-now rule,
  because complying early costs nothing and not complying breaks every file
  at once
- finding: the worker has meanwhile committed more than its last report
  covered — `tests/probe/defect/view_escape/` now holds six cases, and
  `probe02d_wide_literal_refused.npk` exists. Seen incidentally while sizing
  D-248's exposure. Noted because it means O-N9's reproduction is already in
  the tree at a citable commit, which is what the compiler session asked for;
  the hash goes to `nitpick-36` once the worker reports and the record check
  has run, not before
- `nitpick-36` acknowledges and confirms the sequence: **1.5.1b's order stands
  — DEF-2 step 1, DEF-3 step 2, DEF-1's builders step 3** — so DEF-3 does not
  slip behind DEF-1 and the author's blocking ruling changes nothing about the
  compiler's plan. 1.5.1's four prefix harnesses are at the parity stage. The
  DEF-3 hash goes into `1.5.1b.md` §4 and `OPEN_DECISIONS` §2f verbatim, and
  our six-case contrast set is the shape its planned
  `tests/analysis/rejection/view_escape.npk` will carry — so the reproduction
  becomes the compiler's own regression case, which is the best outcome a
  raised defect has here
- **finding worth feeding into `nitpick-time` 0.0.3, from the compiler's plan
  rather than from our own:** 1.5.1b's step 0 is an `NPK_HEAP_STATS`
  instrument and a **`cost` stage** — a harness stage that measures compile
  cost. This library's harness stage list (`parse`, `accept`, `check`,
  `golden`, `sweep`, `program`, `repro`) has no such stage, and O-N4 was found
  by accident, because one probe happened to be enormous. A `cost` stage
  recording `npkc` wall time and peak RSS per test against a budget would have
  caught it as a *monitored property* instead, and this is a library that will
  compile a 26 838-row generated table on every run. Recorded as a suggestion
  for whoever works 0.0.3, not acted on: the stage list is a plan and the
  orchestrator does not rewrite plans (W-16, and §1 of the orchestrate skill).
  It also wants the author's word, because it adds a stage to a cycle whose
  checklist is already execution-grade
- report `s2-ntime-0.0.0-2035` **STOPPED** (a third stop), 330,666 tokens,
  50.1 minutes, 156 tool uses. Four commits — `ef14210` probes 02/03/07/08 and
  twins plus TM-105, `0667ecb` O-N9 reproduced with the contrast, `eb8d6b4`
  probes 05/06 plus TM-106 and the third stop, `9113487` the execution record.
  `check_record.py` **exit 0**, `check_refs` clean, `nitpick-time` tree clean,
  and every other repository at zero changes — write scope held for the
  fourth dispatch running
- **ten of eleven probes are worked.** 01, 02, 03, 04, 05, 06, 07 and 08
  accepted, several with negative twins that pin a refusal (02c `TYPE-009`,
  02d `LEX-004`+`PARSE-002`, 05b `TYPE-034`). Probes 09 and 10 held on O-N9;
  **probe 11 was not worked and is independent of every open disposition**, so
  it is the next dispatch's first item
- **O-N10 raised, the third stop, and its quiet half is the serious one.**
  `#[derive(Eq)]` on a payload enum does not compile (`NITPICK-TYPE-034`,
  reported inside `<derived-1>`); `#[derive(Ord)]` on the *same declaration*
  compiles and produces a tag-only `cmp`, so `Literal(7).cmp(Literal(9))` is
  **`Equal`**. A refusal is an inconvenience; silently reporting two different
  values as equal is a wrong answer. No file in the compiler's own tree
  derives on a payload enum, so the gap is coverage and the ask includes a
  test there. **Not blocking `nitpick-time`** — one payload enum is exposed
  and no rule needs a derive on it — so no author decision is pending; it
  blocks the first library that wants one. The worker flagged its own id as
  provisional and told me to check the registry, which was the right instinct
  after this session's two numbering errors: `O-N10` was free
- **the finding that contradicts a written gate, and it is in more than one
  plan: freeing a generic container's block does NOT drop its elements, and
  `exit 0` does not notice.** D-151's trap watches `wild` allocations; a
  `string` body is managed. A `Vec<string>` freed without dropping elements
  retained **125 MiB over two million elements and exited 0**, and hit
  `HeapOom` under a 64 MiB cap. Cycle 0.0.4's checklist says "the suite's
  programs exit 0, so a missing `free` on any path is a trap rather than a
  pass (D-151)" — **that is true of `wild` only**, and as written it is a gate
  that cannot fail. Landed in `PLAYBOOK.md`; the plan text itself is the next
  worker's to amend, not mine
- seven more playbook facts landed from this report: the runtime poisons freed
  bytes with `0xAA` (D-183), which is why a dangling-view probe is
  deterministic evidence rather than a flake; `int64`'s **minimum** cannot be
  spelled as a literal (`LEX-004`) though its maximum can, so a bound pair
  written by symmetry is exactly what breaks; `#size_of` must be measured, a
  `string` being 24 bytes and a `uint16`-payload enum 8; and three unhelpful
  diagnostics — the turbofish `f::<int64>(x)`, the qualified `pick` arm
  `(Part.Year4)`, and `NITPICK-TYPE-046` on a lending `pick` binding an owning
  payload
- **verification is OWED and deliberately not run.** W-21 wants a verifier on
  `9113487` before anything advances. Nothing is advancing — the subcycle stays
  `STOPPED` — and a verifier dies with the session that spawned it, so
  starting a twenty-minute run immediately before a planned handoff would
  have thrown the work away. It is the successor's first action and is on the
  board
- **clean stop at 21:31.** `Workbench writer:` set to `none` and
  `.internal/orchestrator.session` removed, per the orchestrate skill §15.
  Done *before* the successor was briefed rather than after, so that an abrupt
  close cannot leave the lock naming a dead session and force the successor
  through the stale-takeover path for no reason. Nothing is in flight; no
  claim has a live agent; `nitpick-time` is `CLAIMED s2` and stays claimed,
  because the subcycle is unfinished and the claim is the thing that says so

### The second orchestrator — `nitpick-libs-88`, from 20:56

- **writer `3e1777c3-c237-4c90-920c-a4a6b9df1e66`** took the lock at 20:56.
  **Not a takeover, and no takeover entry is owed:** the line read `none` after
  the first orchestrator's clean stop, so no session was displaced. Taken board
  line first, then the marker file
- **that finding refined, from the guard's source rather than from the
  handoff.** `writer_allows()` matches `\bnone\b` and returns True *before* it
  ever compares session ids, so while the board says `none` the workbench is
  open to any session, and the marker write is refused only when the board
  names a **different** one. The entry above — "backwards **for a takeover**" —
  is exactly right; the handoff brief's wider phrasing, that the guard refuses
  the §2.1 order as such, is not, and a successor acting on the wider version
  waits for a refusal that never comes. The §2.1 fix is still owed against
  0.2.2
- **the marker command in §2.1 writes an empty file.** `CLAUDE_SESSION_ID` is
  empty in a Bash tool call — the guard does not use it either, reading
  `session_id` from the hook payload instead — so
  `echo "${CLAUDE_SESSION_ID}" > .internal/orchestrator.session` produces a
  blank marker and a silent compaction hook. This session recovered its id from
  the transcript directory (`~/.claude/projects/<slug>/<uuid>.jsonl`, the one
  being written) and cross-checked it against the outgoing session's id, which
  the board named. A second finding against 0.2.2
- **stale claim `nitpick-time`: found `CLAIMED s2` with no live agent, left
  claimed.** Every claim is stale after a session restart (§4), and this one is
  bookkeeping rather than loss — four commits and a full report are in the tree,
  `check_record.py` exits 0, the tree is clean. **Third finding against §4's
  recovery table: it has no row for a subcycle that stopped legitimately.** The
  table keys on the subcycle file's title, which still reads `RUNNING`, while
  the report reads `STOPPED` — so the `RUNNING` + clean row instructs a literal
  successor that "the work was lost" and to re-dispatch, which would redo four
  committed commits. The report is the authority, not the title
- dispatch `s2-ntime-0.0.0-verify-2056` — the verifier W-21 owes on `9113487`,
  and the successor's first action as the board said. Bounded rather than
  trusted: `probe04_big_fixed_table.npk` forbidden by name, and
  `big_fixed_array_cost.npk` with it (no claim in the report rests on either),
  every `npkc`/`llc` under `ulimit -v 4194304` against a measured ceiling of
  37.6 MiB, and no parallelism, because the compiler's four 1.5.1 parity
  harnesses are live on this machine at load ~6
- **a premise in the handoff brief corrected by measurement: this machine is
  157 GiB with NO swap**, 65 GiB free at 20:53. "Re-running probe 04 will drive
  this machine into swap" is not true of this box — there is no swap to drive it
  into, and 30.9 GiB would fit. The exclusion is still right, for two better
  reasons: the report claims no result for probe 04, so re-running it verifies
  nothing; and 281 s of CPU beside four live parity harnesses is a bad
  neighbour. The board's separate claim that a 16 GiB machine and CI cannot
  build the library in its shipping shape is about **consumers'** machines and
  is untouched by this
- the outgoing session's last entries are timestamped ~21:31 against a system
  clock reading 20:47 when it wrote them. Noted only so a successor comparing
  timestamps is not misled; the record is append-only and those entries stand

- **`nitpick-36` → the workbench, relayed by the outgoing session after it had
  released the lock, and landed here by its successor.** Four items:
  - **O-N10 is the compiler's DEF-4**, recorded at our commit `eb8d6b4`, with a
    step proposed in 1.5.1b awaiting the author's ratification. It does **not**
    displace the DEF-2 → DEF-3 → DEF-1 order, so all four of this workbench's
    defects may land in one batch
  - **the instrument that closes the gate we could not close.** 1.5.1b step 0
    builds `NPK_HEAP_STATS`, measuring **managed** memory from the allocator —
    allocated, peak_live, count — because, in their words, "the gate 'exit 0
    proves no leak' cannot be for managed bodies". They have already run it on
    our two container probes: **peak_live 41 321 bytes against 400 101 320
    bytes**, the same pair that both exited 0. That is our finding quantified at
    roughly ten thousand to one, by an instrument rather than by inference.
    Consequence for 0.0.4: its checklist item does not need weakening into
    something vaguer — it needs the right instrument, a `peak_live` assertion,
    once the re-pin lands
  - our container-free finding **is D-247 in library form** (`List<T>` as an
    owning managed structure, already ratified for 1.5.1b), so the library-side
    rule "a container's `free` must drop each element" and the compiler-side fix
    are two halves of one thing. The library rule stays necessary until D-247
    lands
  - case 5's `0xAA` poison assertion goes into their rejection test's companion
    program, so the technique is now shared in both directions
- **Q-9 raised** (registry numbering, not the board's): the compiler side's
  standing rule, heard second-hand, that **a defect a real program finds is
  fixed before planned work**. Every escalation this workbench sent tonight was
  framed "no schedule pressure implied", which under that rule is more
  deferential than the author wants. Recommendation: confirm it, and let the
  workbench state plainly what a defect blocks
- **Q-10 raised**: whether `nitpick-time` 0.0.3 gains a `cost` harness stage,
  now widened by item 2 above to carry `NPK_HEAP_STATS` as well. It adds a stage
  to an execution-grade checklist and amends 0.0.4's gate, so it is a plan
  change and the orchestrator does not make it (W-16, §1)
- **verify `s2-ntime-0.0.0-verify-2056` PASS** on `9113487`, 5.8 minutes,
  99 066 tokens, 53 tool uses. The W-21 debt the handoff carried is discharged.
  It ran both checks against their negative controls *before* trusting them,
  re-compiled all twelve runnable probes and matched every exit code, every
  diagnostic and every memory figure, reproduced both defect transcripts
  verbatim — including case 5's deterministic `exit 170` across four runs — and
  independently re-derived probe04b's emission claims from its own artifacts
  rather than reading the committed `.txt`. It found no unevidenced prose claim,
  and confirmed that the predecessor verifier's one FAIL is corrected in this
  commit. **The `ulimit -v 4194304` cap never bound**, as the 37.6 MiB ceiling
  predicted; the two forbidden files were not compiled
- **`nitpick-libs-02` had already exited** when this session tried to send it
  the two corrections above. They live here instead, which is where they were
  going to matter anyway. Nothing was outstanding from it
- **question Q-9 answered by the author: state what it blocks.** Landed as
  **W-27** in `WORKSTREAMS.md`, refining W-11 and W-23. The compiler side's rule
  is confirmed — *a defect a real program finds is fixed before planned work* —
  so an escalation from here says what is blocked, what is inconvenienced and
  what is unaffected, and drops "no schedule pressure implied". The hedge reads
  as modesty and is really a withheld fact: only the stream that hit the defect
  knows what it cannot do without the fix. O-N9 is the standing evidence — read
  here as conformance rather than a block, overridden by the author, and the
  override cost nothing because the fix batched with three others
- **question Q-10 answered by the author: both, and sweep for the gate.** 0.0.3
  gains the cost-and-heap stage and 0.0.4's gate becomes a `peak_live`
  assertion, both once the re-pin makes `NPK_HEAP_STATS` real
- **the sweep, run read-only the same minute, and it is worse than "more than
  one plan": the unfalsifiable leak gate is in ALL SIX repositories.** The
  claim takes the form *"the suite's programs exit 0, so a missing `free` on any
  path is a trap rather than a pass (D-151)"*, and it is false for every managed
  body — D-151 watches `wild` allocations only. Sites, by repository:
  - **`nitpick-parse` is the worst, 9 sites** — `0.0/README.md:104,135`,
    `0.0/0.0.4.md:20`, **`0.4/README.md:43`**, `specs/SAFETY.md:35,237,283`,
    `specs/VALUE_MODEL.md:214`, `0.0/0.0.0.md:354`. It is a *parsing* library:
    managed bodies are its subject matter, and `string_slice` allocates an owned
    copy since D-186. `0.4/README.md:43` puts the gate on `doc_destroy` — "every
    test exiting 0 so a missed destroy is a trap" — which is precisely an owning
    structure D-151 cannot see. That gate is not weak, it is inert
  - **`nitpick-tui` 5 sites** — `0.0/README.md:125`, `0.0/0.0.4.md:16`,
    `specs/SAFETY.md:27,216`, `0.0/0.0.0.md:353`
  - **`nitpick-sockets` 5 sites** — `0.0/README.md:134`, `0.0/0.0.4.md:14`,
    `specs/SAFETY.md:26`, `specs/VERIFICATION.md:48`, `0.0/0.0.0.md:328`
  - **`nitpick-regex` 4 sites** — `0.0/README.md:130`, `0.0/0.0.4.md:14`,
    `specs/SAFETY.md:25`, `0.0/0.0.0.md:314`
  - **`nitpick-posix` 2 sites** — `0.0/0.0.0.md:37,226`, in `nitpick-apps` and
    outside this workbench's write scope
  - **`nitpick-time` 2 sites and furthest along** — its `specs/SAFETY.md`,
    `meta/DECISIONS.md` and `0.0/0.0.4.md` already carry the correction the
    worker wrote; only `0.0/README.md:100` and `0.0/0.0.0.md:299` lag
- **the one repository that already had it right, and it is the model:**
  `nitpick-sockets`' `ANCILLARY_MODEL.md:67` and `SAFETY.md:221` say the
  ancillary path "takes no `wild` bytes, so it cannot trip D-151 on any exit
  path" — a statement about what the trap *covers*, not a claim that exiting 0
  proves cleanliness. That is the shape the other sites should take.
  **D-188, which `nitpick-sockets` and `nitpick-tui` cite beside D-151, does
  not help:** it is the driver and process registry — a clean exit refuses to
  abandon a live child — and it sees managed heap bodies no better than D-151
- **why this was worth the author's minute rather than the orchestrator's
  judgement.** Every fix is a plan edit in a repository no stream has claimed,
  so W-7 forbids making them now; the sweep is read-only and the notes are on
  the board, so each stream meets its own list at its claim instead of
  rediscovering the defect the way `nitpick-time` did — by writing a two-million
  element probe and noticing 125 MiB that `exit 0` had blessed
- dispatch `s2-ntime-0.0.0-2103` — the fifth into this subcycle. Two items:
  **probe 11**, the `failsafe` arm contract and the last unworked probe; and
  **Q-10's correction applied to the one claimed repository**, amending
  `0.0/README.md:100` and `0.0/0.0.0.md:299` to say what D-151's trap actually
  covers, with `nitpick-sockets`' correctly-scoped wording as the model and a
  hook left for the `peak_live` assertion the re-pin will make possible. The
  NOTES carry all four disciplines this subcycle has paid for — commit as you
  go and before reporting, an exit code beside every timing, the transcript
  verbatim rather than summarised, and the two forbidden files — plus W-27 and
  the standing hold on probes 09 and 10. **W-15's "one fresh worker per
  subcycle" is now five workers on one subcycle**; W-4's recalibration must
  count dispatches, not subcycles
- **`nitpick-36` acknowledges the W-27 escalation.** The four blocking statuses
  are recorded on the compiler side as this workbench stated them, and
  **1.5.1b's full order is confirmed: DEF-2 → DEF-3 → DEF-1 → D-246 → D-247.**
  So the first unhedged escalation cost one message and changed nothing about
  their plan, which is the outcome W-27 predicts: the ordering information was
  already right, and what the hedge had been withholding was merely the
  confirmation of it
- **the D-188 correction is accepted and is being applied on the compiler side
  too** — no document there will pair D-151 with D-188 as a leak guarantee.
  Their formulation is cleaner than ours and is worth carrying verbatim into
  the amendments: **"D-151 counts `wild` blocks, D-188 counts live drivers, and
  neither sees a managed body."** That is the sentence the six repositories'
  sites should be rewritten toward
- **the caution that arrived by accident, and it changes how we should adopt
  the instrument.** 1.5.1b step 0 is being built in a detached worktree, and
  **its first self-build found a defect in the instrument itself** — the
  exit-time report walked a heap-resident environment slice after the
  compiler's wholesale release. Being fixed there. The consequence for Q-10's
  amendment is concrete: `NPK_HEAP_STATS` is new code that has already been
  wrong once, so 0.0.4's `peak_live` gate must be commissioned against a
  **known-leaking and a known-clean control** before it is trusted as a gate —
  exactly the discipline this workbench's own verifier used tonight when it
  ran both checks against their negative controls before believing them. A
  gate that cannot fail is what we are replacing; a gate that fires on a
  buggy instrument would be no better
- 1.5.1's four prefix harnesses are at the parity stage. The landing message,
  with the commit and the `build/` fact the re-pin needs, comes to this session
- report `s2-ntime-0.0.0-2103` **STOPPED** — the fourth stop — 215 321 tokens,
  24.3 minutes, 95 tool uses. Two commits, `b092a9e` probe 11 and the defect,
  `0f86d6e` the record. `check_record.py` exit 0, `check_refs` clean,
  `nitpick-time` tree clean. Six probe-11 programs plus three defect cases and
  a support-module control; probes 01–08 deliberately **not** re-run, being
  settled by the 20:56 verifier, which is the first time this subcycle's
  verification has saved a dispatch work rather than costing it
- **O-N11 confirmed free in the registry** — the worker proposed it as
  provisional and asked, which is now twice in a row that instinct has been
  right. Highest allocated was O-N10. **Held as provisional pending the
  verifier**, and not sent to the compiler: W-21, and the standing rule that
  nothing moves before the verifier answers, including a sentence
- dispatch `s2-ntime-0.0.0-verify-2131`, the second verifier on this subcycle,
  pointed at the four claims that carry weight rather than at all ten lines:
  the defect and its library-vs-executable control, the mechanism claim about
  `reach_settle` (to be confirmed against the compiler's own source, read-only,
  because being wrong about a mechanism in front of the compiler session is
  worse than naming none), the controlled comparison behind the measured import
  cost, and the superset claim. Plus the two amended leak-gate sites and the
  eight inline comments deliberately deferred to 0.0.2
- **what probe 11 reports, pending verification.** The positive contract holds:
  a missing arm is `NITPICK-REACH-002`, so TM-017's error budget is a
  constraint and not a convention, and `SAFETY.md` §2 survives. But three
  findings around it are larger than the probe's own question:
  - **an import charges the consumer for the imported module's ARITHMETIC, not
    only for its error identities.** A module declaring no error at all, but
    dividing, indexing and adding, cost an importing program with no arithmetic
    of its own four arms — DivByZero, DivOverflow, IntOverflow, OutOfBounds —
    measured against a floor twin whose `failsafe` it copies character for
    character. Any published per-import arm table listing identities only
    understates every row that imports arithmetic, and `cal` divides and
    indexes constantly. Landed in the repository as TM-107 / S-4b, S-4c
  - **`npkc` exit 0 does not mean a program is well-formed.** A root file with
    `main` and no `failsafe` compiles at exit 0 and is refused only by `llc`,
    at a generated line naming `@npk_failsafe`. **This is the same class of
    error as "a timing without an exit code is not a measurement", one stage
    further down the pipeline:** a harness that compiles to `.ll` and reads
    `npkc`'s status passes a program with no handler at all. Run all four
    steps, or grep the IR for one `define i32 @npk_failsafe`
  - **and the trap inside the trap — the whole REACH-002 arm contract is
    discharged by DELETING the `failsafe`**, `reach_settle` returning early at
    `failsafe_decl == 0`. So the error budget is enforced against consumers
    that have a handler and asked of nothing that has none. That is the half
    worth raising loudest, exactly as O-N10's quiet half was
  - a **superset** of the required arms compiles: `probe07_negative_div.npk`
    names `(OutOfBounds)`, contains no index expression and exits 0. So
    "exactly these arms and no more" can only ever be a harness assertion, and
    a published arm table that OVERstates would never be caught by a build
  - a `pub error:` **declaration** arms nothing — the set comes from `fail`,
    `?!` and `!!!` sites — so a library may declare an identity before raising
    it at no cost to consumers, and any generator counting declarations
    overstates the bill. The arm is owed by the **import**, not by the call:
    importing a module and calling only its infallible half is still
    REACH-002 for the identity it never touches
- **the playbook edits these imply are HELD until the verifier answers.** Trap
  4 of the handoff: when landing a language fact a worker reports, the prose
  may be the worker's but the syntax must come from a compiled example. The
  verifier is recompiling exactly these
- **verify `s2-ntime-0.0.0-verify-2131` FAIL** on `0f86d6e`, 9.2 minutes,
  149 956 tokens, 42 tool uses — **and read the scope before reading the
  verdict.** All four weight-bearing claims are **CONFIRMED**, three of them
  live and one by reading. The one failure is a miscount in a deferral list
- **what the verifier confirmed, and it is the substance:**
  - **O-N11's defect and its control.** case1 `npkc` exit 0 / `llc` exit 1 on
    `@npk_failsafe`; case2 the contrast; and the support-module control
    emitting **0** `define i32 @main` with **7** calls to an undefined
    `@npk_failsafe`, which is what makes the defect about the missing handler
    rather than about library-versus-executable
  - **the mechanism, read out of the compiler's own source rather than
    inferred** — `../nitpick/src/frontend/analysis/reach.npk`: `failsafe_decl`
    is the sentinel `0i32` at line 88, set only when a function literally named
    `failsafe` is found at line 147, and **`reach_settle` returns early at line
    503**, `if (x.failsafe_decl == 0i32) { pass NIL; }`, *strictly before* the
    named-coverage loop at 529–585 that raises `REACH_UNNAMED`
    (`analysis_codes.npk:273`). The claim this workbench was most exposed on is
    now a citation, which is what the dispatch asked for and why it asked
  - **the import-cost comparison is genuinely controlled** — a `diff` of
    `probe11c`'s and `probe11d`'s `failsafe` blocks is byte-identical, so the
    four extra arms are attributable to the import and nothing else. TM-107 and
    `SAFETY.md` S-4b/S-4c are landed in the same commit, not merely narrated
  - the superset claim, and both amended leak-gate sites in the
    `nitpick-sockets` phrasing, and O-N11 occurring exactly once tree-wide
  - the `ulimit -v` cap did not bind; peak was ~76 MiB, under `llc` rather than
    `npkc`
- **the FAIL: the report says eight deferred inline comments and there are
  nine.** The literal `// D-151: exit 0 additionally asserts that nothing
  leaked.` is in nine `.npk` files. The missing one is
  **`probe04_big_fixed_table.npk`** — almost certainly because it is the file
  nobody ever compiles, being the 281 s / 30.9 GiB one, so it drops out of every
  mental list of "the probes". But `tests/probe/README.md:47` lists it as a
  first-class probe row, not an excluded file the way `support/` and `defect/`
  are. Confirmed here independently: `git grep -l` returns nine
- **why a one-word miscount is worth a dispatch rather than a shrug.** The
  count is not decoration — it is the size of a work item deferred to 0.0.2,
  and a later worker reading "eight" would sweep eight files and leave the
  ninth carrying a comment this ecosystem has just spent a night establishing
  is false. The verifier also checked the deferral's *reasoning* against all
  nine and found it sound — none allocates a leak-risking managed container,
  and it read `probe05_payload_enum.npk` in full because it builds a `Vec<Part>`
  — so only the number is wrong. That is exactly the standard the first
  verifier set on this subcycle and it is being held to
- dispatch `s2-ntime-0.0.0-2141` — the sixth into this subcycle, and the
  smallest: correct eight to nine, name `probe04_big_fixed_table.npk` in the
  deferral list with the reason it was missed so the 0.0.2 worker does not
  repeat the omission, and re-open nothing else. The NOTES enumerate what the
  verifier already confirmed precisely so that none of it is re-run
- **O-N11 sent to `nitpick-36`** with its verification status stated exactly
  rather than rounded: the four claims confirmed, the overall report FAIL named
  as an unrelated miscount now being fixed. Sent rather than held to the
  subcycle's close because it is **kin to an open item on their side** — their
  note that D-014's injected `ensures result > 0` on `failsafe` and its
  non-empty-body check "both currently exist nowhere" is the same missing pass,
  and one walk over the root's declarations answers all three. If they are in
  that code for step 0 anyway the marginal cost is small; if not, it keeps.
  W-27 applied: stated as ordering information, with "blocks nothing of ours"
  said plainly and no reschedule requested
- **the W-4 number, now hard to ignore: six dispatches on one subcycle**, of
  which three were re-dispatches and two of those were caused by a worker's own
  bookkeeping rather than by the work. W-15's "one fresh worker per subcycle"
  has not survived contact once. Recalibration must count **dispatches**, and
  the estimate for the next repository must not be taken from `nitpick-time`
  0.0.0's subcycle count
- **O-N11 accepted as the compiler's DEF-5, and taken into 1.5.1b now rather
  than kept.** The kinship argument was the whole reason: step 1 (D-248) is
  already the whole-graph pass over the root's declarations that makes
  `main`/`failsafe` the root's alone, and this finding is the same pass's
  missing question, so DEF-5 lands as its own commit immediately after it.
  **The ask was granted in full** — a root declaring `main` and no `failsafe`
  is refused *at `main`*, with the diagnostic **listing the error identities**
  the absent handler would have to name; `reach_settle` will report the set it
  currently computes and throws away. A root with **neither** stays legal,
  since a library file checked alone is a partial compile the closed-world link
  never sees as-is; a `failsafe` in any module but the root is refused by
  step 1; and the reach loop's early return survives only for the no-`main`
  case, where there is nothing to settle against. **Raising it immediately
  rather than at the subcycle's close is what put it in this batch**
- **DEF-5's exposure across the ecosystem, measured rather than assumed** —
  the same discipline D-248 got, and it changed the conclusion twice. Files
  declaring `func:main` with no `func:failsafe`, all six repositories:
  **exactly three, and every one is a negative probe.**
  - `nitpick-time`'s `case1_no_failsafe.npk` and `case3_arm_contract_evaded.npk`
    — deliberate, they *are* DEF-5's reproduction. **Their transcripts change
    at the re-pin**: today they record `npkc` exit 0 then `llc` exit 1, and
    afterwards they must record an `npkc` refusal carrying the arm list. That
    is a re-pin task, and it is exactly the kind of thing that gets missed
    because the files still "work"
  - `nitpick-posix`'s `probe02g_cross_module.npk`, and **the first reading of
    it was wrong.** Its header says `// expect-exit: 71` and its `failsafe`
    comes from a macro, which looked like an entire repository's shape resting
    on a macro-generated handler being visible after expansion — a real risk to
    `nitpick-posix` if DEF-5's check ran pre-expansion. It is not: the header
    is the *hypothesis*, and the recorded verdict is **REFUSED
    `NITPICK-MACRO-007`** — a macro is invocable only in the module that
    declares it. That refusal is what killed PX-010, and **PX-100 supersedes
    it: the `failsafe` is GENERATED, so `nitpick-posix`'s real shape writes a
    literal `func:failsafe` into each utility's root**, which is exactly what
    DEF-5 and D-248 want. Its recorded diagnostic may move, like
    `pxfail.npk`'s; nothing else does
  - **so DEF-5 costs this ecosystem nothing in live code.** Every `main` in
    every repository already has a `failsafe` beside it
- **the finding about the finding: `expect-exit:` is a hypothesis header, not a
  verdict**, and reading it as a verdict is how a negative probe gets mistaken
  for a positive one. The verdict lives in the subcycle's results table. This
  workbench came within one message of telling the compiler session that a
  repository's shape was at risk on the strength of a comment. Checking cost
  two reads
- report `s2-ntime-0.0.0-2141` **STOPPED**, 69 220 tokens, 5.2 minutes,
  28 tool uses, one commit `4dcd204`. **It ran no compiler at all** — two
  markdown files, one `git grep`, both checks — which is what a correctly
  scoped FAIL re-dispatch should cost, and is the counter-example to the two
  earlier re-dispatches that existed only to make a worker commit. The count is
  nine and `probe04_big_fixed_table.npk` is now named with its reason in all
  three places the deferral is carried, including `tests/probe/README.md`,
  which is where the 0.0.2 worker will actually meet it
- dispatch `s2-ntime-0.0.0-verify-2152` **on a smaller model, deliberately** —
  §12's case, since every check in it is a command with an exit code: the
  count, the two check scripts, the three carrying sites, and that
  `git show --name-only` lists no `.npk`. The expensive verifier's confirmations
  on `0f86d6e` are explicitly out of scope and must not be re-run. First time
  this workbench has used §12's model override; recorded so the cost comparison
  exists
- **two playbook facts landed from this dispatch (W-16), both about how a claim
  is produced rather than about the language:**
  - **a list of files is produced by `git grep`, never by recall**, and the gap
    is not random — the files that fall out of working memory are exactly the
    ones every dispatch is instructed to skip, so they are absent from every
    transcript and therefore from every list. That is the whole mechanism of
    this FAIL: `probe04_big_fixed_table.npk` is skipped because it costs 281 s
    and 30.9 GiB. A deferral that under-counts leaves work silently undone, and
    the next worker skips the same file for the same reason
  - **a probe's `expect-` header is a hypothesis, not a verdict.** They agree on
    a probe that confirmed its guess and disagree on every probe that found
    something — which is the case a later reader is most likely to be looking
    at. From this session's own near-miss on `probe02g_cross_module.npk`
- **two items the worker scoped OUT and was right to, both now owed to a later
  dispatch here.** (a) There is **no checklist item** for the residue sweep:
  `0.0/README.md`'s 0.0.2 section is what the 0.0.2 worker's read order lands
  on, and the deferral lives only in 0.0.0's record and `tests/probe/README.md`.
  (b) **Nine sites still hedge O-N11 as *(provisional)*** — `specs/SAFETY.md`,
  the repository's own `OPEN_QUESTIONS.md`, `0.0/README.md`,
  two `defect/` READMEs and four places in `0.0.0.md` — though the number is
  allocated and the defect is now the compiler's DEF-5. Both are one-pass jobs
  for the next dispatch that opens those files, and the worker declined to sweep
  half a file and leave it inconsistent, which is the right instinct. Neither
  blocks anything. O-N10's hedges are deliberately excluded: nothing on file
  says that number is allocated
- **verify `s2-ntime-0.0.0-verify-2152` PASS** on `4dcd204` — the count is nine,
  named in all three carrying sites including `tests/probe/README.md`, and
  `git show --name-only` lists two markdown files and zero `.npk`, so the nine
  comments were not swept early. It also disambiguated fifteen `git grep`
  hits for "eight" and confirmed none is a remaining residue claim — the
  legitimate ones are `weight`, the eighth selfcheck case, the eight-row
  isolation and `readlink`'s first eight bytes
- **the §12 override paid off and the numbers are worth keeping.** The smaller
  model cost **71 483 tokens, 2.3 minutes, 12 tool uses**; the full verifier on
  the previous commit cost **149 956 tokens, 9.2 minutes, 42 tool uses**. Half
  the tokens and a quarter of the time, on a task where every check is a
  command with an exit code — and it still did the careful part, the fifteen-hit
  disambiguation nobody asked for by name. The rule this suggests: **the model
  follows the kind of check, not the importance of the commit.** The expensive
  verifier earned its cost on `0f86d6e` because it had to read the compiler's
  source and judge whether a mechanism claim was true; this one had nothing to
  judge
- **question answered by the author: start `nitpick-regex` at width 1.** Stream
  2 stays parked and claimed rather than released — the claim is what records
  that its subcycle is unfinished
- **claim `nitpick-regex` 0.0.0 for s1**, and dispatch `s1-nregex-0.0.0-2205`.
  Tree clean at `c056ae1`, plan PLANNED, fourteen probes, no probe files yet.
  **This is the first dispatch in this ecosystem to start from a full
  playbook**, and the difference is the whole point of having written one:
  - **probe 07 is `string_bytes` at the borrow edges — O-N9's exact territory.**
    Without the playbook this worker would have spent a day rediscovering a
    defect that is already confirmed, already the compiler's DEF-3, and already
    scheduled. It is told instead, and told not to build on the unenforced rule
  - probes 03 and 08 are container work, so the leak finding applies —
    `Vec<int32>`'s elements are POD and need no drop, which is exactly the
    distinction that took `nitpick-time` a two-million-element measurement to
    establish
  - and it inherits the whole syntax ledger: no `let`, the turbofish, the
    qualified `pick` arm, `int64`'s unspellable minimum, `#size_of` measured
    rather than derived
  - its four leak-gate sites are fixed **on this claim**, which is what the
    author's Q-10 answer scheduled and what W-7 requires
- **compiler status, 22:40, sent unprompted at the author's request so this
  board does not rest on a stale picture.** 1.5.1 is CLOSED and pushed
  (`e668f6a`). 1.5.1b runs as cumulative prefixes, each behind a ~3 h harness:
  step 0 committed (21:34), step 1 / DEF-2+D-248 committed (22:05), step 1b /
  DEF-5 committed (22:11), step 2 / DEF-3 written and sweeping the compiler's
  own `src/`. Nothing owed to us changes; the landing message still comes
- **D-248 has a consequence nobody had told us, and it is the kind that breaks
  every file at once: a module name is an IDENTIFIER.** A `.npk` file named
  after a reserved word, or beginning with a digit, refuses. The compiler
  renamed five of its own (`00_minimal.npk` → `c00_minimal.npk`, plus
  `derive`, `arena`, `assoc`, `wildx`). **Swept all six repositories against
  `PLAYBOOK.md` §10's list: zero violations** — and the reason is luck plus one
  earlier catch, `nitpick-regex`'s `d6fb0ce`, "probe filenames cannot begin
  with a digit". The rule now binds every new file and is on the board
- **two shapes DEF-3 distinguishes that our own six cases did not**, and
  `src/fmt/` planning turns on both. A view of a **temporary** —
  `string_bytes(string_concat(a, b))` returned — is refused outright as
  `NITPICK-BORROW-012`; bind the intermediate. It is doubly wrong today, since
  that `string_concat` temporary also leaks under D-246, and the answer to both
  is the same bind. But a view whose root is a **pointer-shaped binding** — a
  wild pointer, a slice, a cstring — is the *pointee's* borrow and not a frame
  borrow, so `string_from_bytes(buf, n)` over an alloc'd block, returned,
  **stays legal**. **Consequence for `nitpick-time`: its house rule "a view is
  a parameter, never a return value" is CONSERVATIVE rather than true.** It was
  written with no way to tell those apart; there now is one, and `src/fmt/`
  should not be built on the stricter reading as though it were the rule.
  Relayed immediately to the live `nitpick-regex` worker, whose probe 07 is
  `string_bytes` at the borrow edges and would otherwise have concluded the
  strong form
- **DEF-4 widened after measurement and is now D-250, step 3b**, inserted
  between the builders and D-246. Our O-N10 was reported as a payload-enum
  defect; it is not only that — a derived `Eq`/`Ord` over a **struct with a
  derived-struct field** fails the same way inside `<derived-1>`. So step 3b
  covers named types in structs and enums alike, and an owning payload will
  refuse the derive **by name** rather than silently generate. Worth noting for
  its own sake: **we reported the narrow case and the compiler's measurement
  found the general one**, which is the same service our sweep did for the leak
  gate in the other direction
- **DEF-5's diagnostic is known before it lands: `NITPICK-REACH-003` at `main`,
  listing every identity the handler owes** — for our own `case1` that is six,
  the four system identities every executable carries plus the user's plus
  `IntOverflow` from a guarded `+`. That is the after-value the two
  `missing_failsafe` transcripts must record at the re-pin, so the re-pin task
  is now fully specified rather than merely flagged
- **three playbook corrections from the same message, two of them numbers we
  had subtly wrong:**
  - the compiler's root file is **`src/npkc.npk`**, renamed from
    `src/main.npk` at step 1; our §2 still spelled the old path
  - **two figures circulate for the compiler's self-build and they measure
    different things** — 11 GiB peak RSS, and 10.39 GiB peak *live* managed
    from the new instrument. Neither supersedes the other, and the playbook now
    says which is which, because a later reader quoting "10.39" as an RSS
    figure would be wrong by the whole difference
  - **the 480 000-byte literal's flat memory is explained: escaping that one
    string requests 107 GiB in total.** The cost is churn rather than
    retention, which is exactly why RSS said nothing about it and wall time
    said everything — and it is a caution about the `cost` stage we are about
    to adopt, since a peak-RSS budget would not have caught this axis at all
  - and **the identifier-length observation is resolved rather than dismissed**:
    not a fourth axis, but a real amplifier, because the builders copy
    accumulated *text* and a longer identifier lengthens every copied prefix.
    Our earlier "did not survive measurement" was right about the axis and
    wrong to leave the 11% unexplained

### Stream 1 — `nitpick-regex` 0.0.0

- report `s1-nregex-0.0.0-2205` **DONE** — the ecosystem's **first completed
  subcycle** — 332 735 tokens, 158 tool uses, six commits, twenty-three probe
  programs, `check_record.py` exit 0, `check_refs` clean, tree clean at
  `9b80d69`. Every one of the twenty-three was re-run fresh from the committed
  tree and matched its `expect-` header, which is the discipline this workbench
  wrote down two hours ago already being followed unprompted
- **correction to the report's own cost figure, and it is not a nitpick: it
  says "wall clock ~9 h" and the six commits span 34 minutes**, with the agent
  running 50. Checked from `git log --date=format:%H:%M:%S` and the harness's
  own duration. **W-4's rebalancing consumes exactly this number**, so a
  nine-hour figure for a fifty-minute subcycle would have mis-sized every
  remaining repository in the partition. Recorded here rather than sent to the
  verifier, since establishing it needed no re-run
- **`stack` is a reserved word and was missing from the playbook.** Confirmed
  against `../nitpick/meta/specs/LEXICAL_REFERENCE.md:52` — a MemoryQualifier
  beside `wild`, `wildx`, `defer` — rather than taken from the report, per the
  rule about landing language facts. **Landed with its failure mode, which is
  the expensive part:** it does not fail where you write it. `PARSE-002` at the
  declaration, then "this `{` is never closed" at `main`'s closing brace, so it
  reads as a brace imbalance dozens of lines away and gets bisected as one. It
  cost this dispatch about an hour and was its single largest cost
- **RX-111, and it is the most serious finding this workbench has produced.**
  The report says D-070's bounds check attaches only to types that **carry a
  length** — a slice `T[]` and a fixed array `T[N]` trap — while a `wild T->`
  block is unchecked raw pointer arithmetic; and that every `Vec<T>` here is a
  `wild T->`, so **no container access in any of these libraries is
  bounds-checked unless the library checks it, and an out-of-range index is a
  silently wrong value rather than a trap.** Under verification now, split into
  the measurement, the mechanism, and — the part everything rests on — whether
  the prelude's `Vec` really is a `wild T->`
- **the exposure, which needed no verifier and is confirmed here directly:
  four repositories' `SAFETY.md` state the opposite as a promise.** This is a
  worse shape than the leak gate: those were gates that could not fail, and
  these are **affirmative safety claims that are false**, two of them about
  adversarial input:
  - **`nitpick-parse:22`** — "Indexing is bounds-checked and traps ... An index
    derived from input is a *crash*, not a smear." A parser's index is
    attacker-influenced by definition. **This is the worst one in the
    ecosystem**
  - **`nitpick-sockets:28`** — "an out-of-range read into a `sockaddr` is a
    *crash*, not a leak of adjacent memory". A claim that there is no
    information disclosure
  - **`nitpick-tui:24`** — "An out-of-range cell index is a *crash*, not a
    smear"
  - **`nitpick-time:21`** — "A zone-table index out of range is a *crash*, not
    a wrong offset"
  - **`nitpick-regex` has already corrected itself** — its `SAFETY.md:20` now
    reads "Indexing **a type that carries a length** is bounds-checked ... **a
    `wild T->` block does not** — and `Vec<T>.items` is one", with Rule S-23 and
    a per-type table at :224. That is the wording the other four should take
- **`O-N` numbering collides INSIDE `nitpick-regex`** — its local
  `meta/OPEN_QUESTIONS.md` carries legacy local `O-N1…O-N4` beside the
  registry's `O-N9…O-N12`, so `O-N9` would mean two different things in one
  file. The worker added a warning block and defined the registry ids locally
  so citations resolve, and did **not** renumber settled entries, which is the
  right instinct. It recommends moving the four legacy ids to a local `O-C`
  prefix and reserving `O-N` for the registry alone. **This is the third
  numbering collision in one day** — Q- on the board, O-N7's misnumber, and now
  this — and the first two were caught by a human reading rather than by
  `check_refs.py`, which finds an undefined reference and not a doubly-defined
  one
- **O-N12 proposed and confirmed free** (highest allocated was O-N11): `>>>`
  and `string_repeat` are documented in the compiler's references and absent
  from the compiler. The worker recommends the **documentation** fix rather
  than the implementation, since `>>` on an unsigned operand is already `lshr`
  — measured at bit 63 — so `>>>` would be a pure synonym. A reader who sees
  `>>` described as `ashr` and `>>>` as `lshr` reaches for the one that does
  not exist, which is exactly what happened here
- **RX-112, an override of a plan instruction, flagged by the worker for
  confirmation rather than buried.** `0.0.0.md` §5 said to stop and re-plan
  `API.md` §2 if probe 06 accepted a slice return. It accepted; the worker did
  not stop, on the ground that the acceptance is O-N9 / DEF-3 — the escape rule
  is known to be unenforced for slice views — rather than evidence that RX-050
  is over-cautious. Under verification as a judgement call. **Flagging it was
  right**: a plan instruction silently not followed is the thing an audit finds
  three cycles later
- **verify `s1-nregex-0.0.0-verify-2257` PASS** on `9b80d69`, 11.1 minutes,
  173 899 tokens, 78 tool uses. It re-ran all 23 probes with every exit code and
  diagnostic matching byte for byte, checked the toolchain's SHA-256 against the
  transcript's declared pin, ran BOTH check scripts' negative controls before
  trusting their clean results, and **wrote its own probes** to reproduce three
  claims rather than re-reading them. **The first subcycle in this ecosystem to
  close.** `advance nitpick-regex 0.0.0 → 0.0.1`
- **RX-111 resolved, and the answer is that it is OURS.** The mechanism is
  confirmed in the compiler's source with citations — `parse_type.npk:14-17`, a
  qualifier is not part of the type so `wild T->:x` is bare `TY_POINTER`; and
  `ir_expr.npk`'s `ExprIndexExpr`, where the `TY_SLICE` branch calls
  `emit_bounds_guard` at ~8667 and `TY_ARRAY` at ~8701 while the `TY_POINTER`
  branch at ~8676-8685 goes straight to `getelementptr`. **That is correct
  behaviour, not a defect**, and I confirmed the compiler's documentation says
  so in as many words: **D-070's own title is "`T[]` is a slice: bounds live in
  the array type, NOT the pointer type"**, and `list.npk` marks `List<T>.items`
  "WILD, DELIBERATELY"
- **so four of our repositories cite D-070 in the direction opposite to its
  title.** That is the finding worth keeping, above the fix itself: the
  citation *resolves*, so `check_refs.py` passes it, and four independent
  authors read a decision by number without reading its scope. It is the same
  failure mode as the Q- collision — a reference check finds what does not
  resolve, never what resolves to the wrong thing
- **the inference has a nuance the verifier was right to flag: there is no
  compiler-prelude `Vec<T>` at all.** `grep -rn "struct:Vec"` over the compiler
  tree is empty. `nitpick-regex`'s RX-006 fixes its `Vec<T>` to the shape of the
  compiler's `List<T>` (D-209, `wild T->:items`), and the other libraries do the
  same **by convention**. So "every `Vec<T>` in this ecosystem is unchecked" is
  true today and is a statement about a shared convention rather than about a
  single enforced type — which means a library that later defines `Vec`
  differently gets a different safety property, silently. Worth a line in each
  `SAFETY.md` alongside the correction
- **O-N12 confirmed from the compiler's tree by this session, not relayed**:
  `TYPE_REFERENCE.md:1799` carries `| >>> | right shift (unsigned) | lshr |`,
  `BUILTIN_REFERENCE.md:166` documents `string_repeat(str, n)`, and
  `string_repeat` appears nowhere in `src/` or `runtime/`. **Sent to
  `nitpick-36` with RX-111's disposition attached** so they do not chase a
  defect that is not theirs — and with the note that four readers here were
  misled by "D-070 guarantees bounds checking" as shorthand, which is
  documentation-legibility feedback even though the document itself is right
- **the author's standing instruction, recorded because it governs timing:**
  when a compiler-end fix is needed we message the compiler session so they can
  roadmap it, and the ecosystem is deliberately collecting every defect found
  so far **before** the compiler moves to 1.5.2, so as not to keep building on
  known bugs. That is why O-N11 went over the moment it was verified rather
  than at the subcycle's close — and it landed as DEF-5 in the open batch,
  which it would not have done a cycle later
- dispatch `s1-nregex-0.0.1-2315` — the skeleton, its gate satisfied by the
  verified close. Carries two 0.0.0 debts that live in files it will have open
  anyway: the record's "five commits" where there are six, and the renumbering
  of the local `O-N1…O-N4` to an `O-C` prefix so they stop colliding with the
  registry inside one file
- dispatch `s2-ntime-0.0.0-2315` — **document-only, compiles nothing**, and the
  reason for its existence is scheduling rather than urgency: `nitpick-time` is
  claimed and idle behind four defects, and four debts against it need no
  re-pin. Clearing them now means the landing-message dispatch is probes 09/10
  and the transcript re-recording **and nothing else**, instead of five
  unrelated chores riding on top of the work that actually needed the compiler.
  RX-111's false promise; the O-N10/O-N11 de-hedging, both being accepted now;
  the missing 0.0.2 checklist line; and the record that the house view rule is
  conservative rather than true. Explicitly forbidden: touching probes 09/10,
  re-recording `missing_failsafe`'s transcripts — **that would destroy the
  before-half of a before-and-after the compiler wants** — and sweeping the nine
  stale comments, which stays deferred
- **width 2 from 23:15**, the author having delegated the next step. Both
  streams own disjoint repositories and neither writes the workbench

- **rebalance measurement, and it is the one the whole partition rests on:
  `nitpick-time` 0.0.0 took SIX dispatches; `nitpick-regex` 0.0.0 took ONE.**
  Same subcycle name, same shape of work, comparable size — 11 probes against
  23 — and the second was the larger. The difference is not the repository and
  not the model. It is that the first one had no playbook and the second
  inherited a full one, including `stack`, the whole syntax ledger, the leak
  rule, the measurement discipline, and a mid-flight relay about DEF-3 that
  changed what it concluded. The first repository paid the discovery cost for
  all six.
  **The consequence for W-4 is concrete and it cuts against the obvious
  reading:** `nitpick-time` 0.0.0's cost is *not* the per-subcycle estimate for
  this ecosystem and must not be used as one — it is the one-off price of going
  first. Nor is `nitpick-regex` 0.0.0 the estimate, because it spent nothing on
  language discovery and later subcycles will spend on other things. **Estimate
  the remaining repositories from the SECOND observation, not the first, and
  count dispatches rather than subcycles** — W-15's "one fresh worker per
  subcycle" held exactly once out of two, and the once it held was the one with
  a playbook
- **O-N12 settled the way this workbench recommended — documents, not
  implementation** — landing inside 1.5.1b step 2's commit, and the compiler's
  fix is better than the ask. We reported an absent operator; they replaced the
  row with the rule that makes the table coherent: **`>>` is arithmetic on a
  SIGNED operand and logical on an UNSIGNED one, the operand's signedness
  decides**, confirmed against the single shift arm in their emitter (`ashr` if
  signed else `lshr`), which also confirms `>>>` would have been a pure synonym.
  And they fixed the trap rather than the instance: `BUILTIN_REFERENCE` §2's
  sentence calling those names "fast compiler intrinsics" — under a header
  saying they are the *planned* surface — now says none resolves without a row
  in a marked table, which repairs every name in the list and not only the one
  we tripped over. Landed in `PLAYBOOK.md` sourced to their emitter rather than
  to our probe, which measured only the unsigned half
- **asked whether to strike `string_repeat`, this workbench said keep it**, on
  two grounds checked rather than assumed: the harm was the intrinsics sentence,
  now fixed for the whole list; and **no library here plans a string-utility
  surface** — grepped all six, and `nitpick-regex` and `nitpick-parse`, the two
  that touch strings hardest, claim no such surface. So "planned library
  surface" is an accurate category and should not imply anyone is building it.
  Striking it would have traded a fixed problem for a lost intention
- **RX-111 sharpened by reading the emitter directly, and my own dispatch was
  too blunt.** I told the `nitpick-time` worker the SAFETY.md bounds line "is
  false"; it is not. `ExprIndexExpr` guards **three** kinds — `TY_SLICE`,
  `TY_ARRAY` and **`TY_SIMD`**, the last being a lane's constant bound that
  nobody here knew about — and not `TY_POINTER`. So "array, slice and buffer
  indexing is bounds-checked" is **true about the types it names, omits SIMD,
  and reaches `buffer` by a route it does not state** (a `buffer` is the managed
  owning byte cell, D-200; indexed through a `uint8[]` view, which is a slice).
  **The defect is what it omits**, not what it asserts. Corrected to the worker
  mid-flight, because "the old line was false" invites a reader to distrust the
  rest of the table, while "it was true and narrow and you read it as broad" is
  the mistake that will actually recur. **`nitpick-regex`'s Rule S-23 table has
  three rows and needs a fourth** — noted for that repository, not edited, since
  another stream holds it
- **three DEF-3 refinements from step 2's first whole-tree sweep**, none of them
  in our six cases and all bearing on `src/fmt/`: a view over `#ptr_add` looks
  through to the pointer; a `for` over a range cannot carry a borrow whatever
  its bound reads; a struct literal is rooted where its field values are
- **the dividend, and it is the strongest evidence this ecosystem has for
  raising defects early rather than at a subcycle's close.** Step 2's sweep
  found that **thirteen files in the compiler's own tree — twelve
  `tests/accept/` roots and one rejection test — had a `main` with no
  `failsafe` from the day they were written**, and every one was passing. That
  is O-N11 exactly. Step 1b's prefix harness was stopped, the thirteen gained
  the handler `REACH-003` dictates, and the prefix is re-running. Our probe 11
  was four lines of Nitpick; the thirteen files were already there and would
  have stayed there. **The defect we raised was worth more to the compiler's
  own test suite than to us**, which is not an argument anyone could have made
  in advance and is worth keeping for the next time a stop looks expensive
- report `s2-ntime-0.0.0-2315` **STOPPED**, 171 166 tokens, 22.7 minutes,
  100 tool uses, two commits, **nothing compiled**. It corrected the
  orchestrator three times, and every correction was checked against the
  compiler's source rather than argued
- **CORRECTION, appended rather than edited above, because this record is
  append-only: `NITPICK-BORROW-012` DOES NOT EXIST.** The entry above citing it
  stands as written and is wrong. The highest allocated borrow code is
  `NITPICK-BORROW-011` (`BORROW_WILD_STORE`, `analysis_codes.npk:106`);
  `BORROW-012` appears nowhere in the compiler's `src/` or `meta/`; and DEF-3's
  own plan adds **no new diagnostic code**, every refusal it introduces being
  `NITPICK-BORROW-001` (`BORROW_RETURNED`, `analysis_codes.npk:24`). Verified
  here directly. **Provenance matters for the lesson:** the number came from
  the compiler session's status message and this orchestrator relayed it into a
  worker dispatch, the board and this record **without checking it** — the
  exact "do not cite a code or decision by number without reading its scope"
  failure the playbook had gained six hours earlier, committed by the session
  that wrote the rule. It reached four files in `nitpick-regex`; its live worker
  has the correction and the site list
- **the `buffer` correction went the OTHER way and ENLARGES the finding.** I
  told the worker a `buffer` is reached through a `uint8[]` view and therefore
  guarded. It is not: `buffer_bytes` is among `TYPE_REFERENCE.md` §23's
  "deliberately NOT landed" items, so **no slice route exists** and a `buffer`
  is indexed as `buf.ptr[i]`, a `uint8->`, on the unguarded pointer branch.
  **So `Bytes` is unchecked exactly as `Vec<T>` is, and every formatter in this
  library goes through a `Bytes`** — and any sibling with a `buffer`-backed sink
  has the same gap. Under verification. I was wrong in the direction that
  understated a safety hole, which is the direction that matters
- **`case1` owes FOUR arms, not six**, and the six was mine — carried onto the
  board from the compiler session's message. `case1` has no import, no
  arithmetic and no allocation, so its bill is S-4b's floor. The worker wrote
  **no count into any document**, recording the diagnostic's shape and leaving
  the numbers to the re-pin, which is right for a number nothing yet depends on
- **my own sweep command was short by one, and the failure mode is now twice
  observed.** I dispatched `git grep -n 'provisional\|PROVISIONAL'`, which is
  case-sensitive and misses `Provisionally` — the most prominent hedge in the
  repository, at `missing_failsafe/README.md:3`. The worker found it with `-i`.
  This is the *same* shape as the eight-versus-nine miscount: a list taken from
  a command that did not cover its subject. The playbook rule "take lists from
  `git grep`" is necessary and not sufficient; **the grep must be
  case-insensitive and its pattern checked against a known member**
- **a record-discipline ruling, and the worker's instinct was right.** It left
  four `(provisional)` occurrences standing inside committed REPORT blocks at
  `0.0.0.md` lines 960, 1237, 1240, 1244, on the ground that rewriting a report
  falsifies the record and the hedge was accurate when written. **Affirmed as
  the rule: a committed REPORT block is history and is not amended in place;
  sites stating current fact are corrected.** It matches `RECORD.md`'s own
  append-only discipline — and this session has just applied the same rule to
  itself, leaving the `BORROW-012` entry above standing with a correction
  appended rather than quietly fixing it. `check_record.py` verifies committed
  reports, so an amendable report is a moving target for the check as well.
  Noted for the author rather than blocking on it
- **TM-108 changes a published safety promise** and `check_raw_index` is now
  load-bearing — on 0.0.3's list rather than built. No code exists yet, so
  nothing is broken; but the gap between "the language checks this" and "we
  check this" is now a named item rather than an assumption
- **CORRECTION TO THE CORRECTION, and the second one is the instructive one:
  `NITPICK-BORROW-012` DOES exist.** The entries above saying it does not stand
  as written and are wrong. DEF-3's **step 2 allocates it**, and it lives only
  in the compiler's unlanded step-2 worktree — entered in `analysis_codes.npk`
  there, with its own case in `view_escape.npk`, a README row and a D-249
  landing note. Our pinned tree at `950bb1d` cannot show it, by construction
- **so the observation was right and the conclusion was wrong**, and the
  difference is the whole lesson. `git grep` over the pin genuinely returned
  nothing; from that this orchestrator concluded "the code does not exist" and
  pushed that into a worker dispatch, a verifier dispatch, the board and this
  record. **The pin is a snapshot of what has LANDED. Absence in it proves "not
  landed", never "not real"** — and while the compiler is mid-cycle, fixing four
  defects this workbench raised, those are wholly different facts. Landed in
  `PLAYBOOK.md` §6 as a rule with the procedure: establish which tree a claim is
  about before checking it; the pin is authoritative for current behaviour and
  silent by construction for a fix in flight; and a document referencing a
  diagnostic the pin lacks is a finding **only if it states it as current fact**
- **why the plan and the message disagreed, which was a real thing to find and
  not a slip.** DEF-3's plan said it adds no new code, and that held for every
  refusal shaped like "as if `@` had been written at that argument" — a view of
  a local returned, held in a literal, laundered through a call, stored through
  a pointer parameter, all `BORROW-001`/`002`. **Writing the rule found one
  shape the `@`-equivalence has no arm for: a view of a TEMPORARY.** `@` of a
  temporary cannot be spelled, so no existing code's text is true of it and
  tracking it would need a root with no name. Hence a new code, and hence §4 of
  their plan gets a dated note at the landing recording that the "no new code"
  sentence held for the `@`-shaped refusals and not for this one
- **the corollary worth keeping: a challenge can be worth making and still be
  wrong.** This query was answered with a distinction the plan had not known and
  a documentation fix on their side. Being wrong out loud, to a peer who can
  check, cost a worker one reverted edit; the silence would have cost the note
- three messages went out to unwind it: the `nitpick-regex` worker told to
  restore all four sites **and to label the code as introduced by step 2 and
  absent from the pin**, which is better than either version this workbench had;
  the running verifier told to drop that check entirely, since neither presence
  nor absence is a fault; and the compiler session told the number checks out
- **the two other corrections HELD and are now independently corroborated.**
  The compiler session confirms the `buffer` finding is right and by design —
  §23's "deliberately NOT landed" is exactly that — so `Bytes` is unchecked as
  `Vec<T>` is. And the "six identities" was its reading of `tests/accept/
  borrows.npk`, not our `case1`: **four stands**, and the count is whatever the
  diagnostic prints at the re-pin, which is why the worker wrote none down
- **a finding from their step 3, relevant because every formatter we ship goes
  through a byte sink:** the compiler's own escaper allocated a one- or
  three-byte `wild` block **per byte of every string literal** and never freed
  it, and its two callers concatenated those onto a growing prefix. Both are
  gone in step 3 — bytes go straight into the module stream — and the axis-3
  recipe measures it. That is the mechanism behind the 480 000-byte literal
  requesting 107 GiB while RSS stayed flat, and it means the after-numbers on
  our own recipes should move a long way, not marginally
- **verify `s2-ntime-0.0.0-verify-2345` PASS** on `5b2e0c8`, 7 minutes,
  108 472 tokens, 45 tool uses. Both check scripts run against their negative
  controls first; `git show --name-only` on both commits confirms markdown only
  and no `.npk`; the nine stale leak comments still nine and unswept; the
  `missing_failsafe` transcripts untouched at `b092a9e`. **Every `nitpick-time`
  debt that does not need the compiler is now cleared**
- **it also caught something about this orchestrator's dispatches, and it is
  the more useful half.** My NOTES cited `ir_expr.npk`'s guards at
  8667/8701/8722 — **taken from the compiler's HEAD, while every worker here
  works against the pinned `950bb1d`, where the same code sits twelve lines
  earlier** because an unrelated 1.5.1 insertion landed in between. The verifier
  checked both trees, found the structure identical and the numbers off, and
  correctly ruled it a property of how the dispatch was sourced rather than a
  defect in the committed record — because **the worker had cited `TY_SLICE`,
  `TY_ARRAY`, `TY_SIMD` and `TY_POINTER` by name and no line numbers at all**,
  which is true at both trees. Landed in `PLAYBOOK.md` beside the pin rule:
  cite the kind, the branch or the symbol; a line number is a convenience beside
  a name, never instead of one. Same family as the `BORROW-012` error — *which
  tree is this claim about* — and it caught me twice in one hour
- **the verifier's own judgement is worth recording as the standard**: it did
  not FAIL a report over line numbers that pointed truly at one tree and not
  another, and it did not wave them through either. It established which tree
  each was right for, said so, and located the defect in the dispatch rather
  than in the repository. That is the difference between checking and
  adjudicating
- **stream 2 parks.** `nitpick-time` stays `CLAIMED s2` with no live agent —
  the claim is the thing recording that its subcycle is unfinished — and there
  is now genuinely nothing left in it that does not need the compiler. A
  structural question is noted for when it next matters, and it is not urgent:
  the rules do not cleanly cover a stream whose repository is blocked on an
  external dependency and which wants to start its *next* repository. W-9 sends
  it to the next ungated cycle in the same repository, and there is none;
  releasing the claim would lose the record that 0.0.0 is unfinished. It did not
  need deciding tonight because stream 1 is still working
- **verify `s2-ntime-0.0.0-verify-2345` PASS, re-confirmed after the
  correction** — and it did the thing this orchestrator failed to do: **it
  verified the relayed fact instead of taking it on trust.** Told by me that
  `BORROW-012` is real after all, it went and found it — the compiler's step-2
  worktree at `.internal/wt/b2`, `pub func:BORROW_VIEW_OF_TEMPORARY` in
  `analysis_codes.npk`, a rejection case with an `// expect-error` header, a
  README row, and D-249 recorded SETTLED by the author. That is the whole
  difference between my failure and its absence of one, on the same fact,
  hours apart
- **and it found a debt the maintenance dispatch itself created.** That commit
  lands the unhedged claim that **DEF-3 introduces no new diagnostic code**,
  which is now false. The verifier deliberately did not score it — the worker
  read DEF-3's plan as it stood, exactly as I read the pin and concluded the
  code was unreal, so it is the same category of gap and not a new error — and
  flagged it because `0.4/README.md`'s planner will meet it. Correct call on
  both counts
- **the verifier said four sites; there are five.** `git grep` here finds a
  fifth at `tests/probe/defect/view_escape/README.md:120`, phrased "and DEF-3
  adds **no new diagnostic code**" where the others say "introduces". **That is
  the third sweep list tonight to be short by one**, after eight-versus-nine and
  the `Provisionally` case-sensitivity miss — three for three, by three
  different agents including a verifier that had just been warned about the
  second one. Landed in `PLAYBOOK.md` as a rule rather than an anecdote: run the
  grep twice with different phrasings, use `-i`, check the count against a known
  member, and treat a list as a claim that needs a command written beside it.
  **The reason it matters most for a deferral is that an undercount there is
  invisible forever** — the later worker sweeps exactly the list it is given
- **the five go to the re-pin dispatch, not to another maintenance pass.** They
  are claims about DEF-3's *landed* behaviour, and the landing is precisely when
  a worker can check them against a real compiler rather than against a
  provisional worktree commit that has not passed its harness. Adding them there
  costs almost nothing beside probes 09/10 and the transcript re-recording,
  which are the same subject
- report `s1-nregex-0.0.1-2315` **DONE** — 330 910 tokens, 120 tool uses, four
  commits, **~1h15m measured from `BOARD.md`'s claim line and `git log` rather
  than estimated**, which is the previous report's wall-clock error corrected
  without being asked twice. Both checks clean, tree clean
- **the worker landed the pin lesson as its own finding before I told it**:
  "a fact about an unlanded compiler commit cannot be checked against the pin,
  and *I grepped the pinned tree and it is not there* is not a refutation… two
  sessions drew the same wrong conclusion from the same correct observation
  within an hour". It also names the fix — mark such a claim
  unverifiable-until-repin — which is what the playbook now says
- **O-N14 raised, and it is the widest finding of the night: there is no
  library object.** `npkc` emits `call i32 @npk_failsafe(...)` into every
  translation unit and never a `declare`, so any module that is not a program
  root compiles at `npkc` exit 0 and is refused by `llc`. **Confirmed at the
  emitter by this orchestrator against the pin** — three `call` sites in
  `ir_func.npk` and `ir_stmt.npk`, no `declare` anywhere in `src/backend/ir/` —
  which is a legitimate use of the pin, the claim being about *current*
  behaviour. **It is every library in this ecosystem**, and
  `BUILD_REFERENCE` §4.1's per-module object model is not achievable at this
  pin. The cheap part: **one emitted `declare i32 @npk_failsafe(i32)` closes it
  and strengthens DEF-5's case**, both being about a root's obligation to
  supply that symbol
- **O-N13 raised: a `pub use` is silently downgraded to a plain `use`** when the
  same path was plain-`use`d earlier in the file — `symtab_bind_import` declines
  a name already bound and returns the prior binding without merging `SYM_PUB`,
  at no severity. The failure appears a file away, in the consumer, as "cannot
  find X in this scope"; the same two lines reversed are correct. **Every
  library with an umbrella module is one redundant `use` from it**, and six are
  planned here. Same family as O-N10's quiet half — the loud failure is the
  inconvenience and the silent wrong answer is the defect
- **the `O-C` prefix I passed on would have recreated the collision it was
  meant to remove**, and the worker caught it: that repository's local `O-C` numbers 1 and 2 already exist
  in that repository as compilation questions, cited in five files. It used
  **`O-G`** ("a Gap in the compiler"), one-for-one and in order, with a row
  added to the prefix table. **Confirmed as orchestrator.** That is the fourth
  numbering collision of the day and **the first caught before it landed** —
  by a worker checking a recommendation instead of applying it
- **the registry edit the worker correctly could not make (W-16) is made**:
  `O-N2`'s entry listed `nitpick-regex`'s local `O-N` number 3; that id is now its local `O-G` number 3
- **confirmed: `meta/roadmap/0.0/0.0.0.md` was right not to be renumbered.** It
  is a verified artifact, two redirect entries keep its citations resolving, and
  the single change made to it is the "Five commits" → "Six commits" correction
  it was directed to make. That is exactly the boundary this workbench affirmed
  hours earlier for committed REPORT blocks, arrived at independently by a
  different worker in a different repository — which is the sign a rule is the
  right one rather than merely stated
- **CI is written and has not run, and the acceptance box is STRUCK rather than
  ticked.** It needs a push, which is the author's, and a compiler build, which
  W-18 refuses from here. Everything checkable was checked — YAML and triggers,
  the pinned commit's presence on the public remote, the LLVM asset name against
  the release API, `quickemit.py`'s output paths read from its source at the
  pin, and the stub run green and red. **A struck box with a reason is the right
  answer; a ticked box for an unrun step would have been a FAIL**
- **`check_refs.py` went red on that entry and it was right.** Four ids —
  another repository's local numbers — were written into `RECORD.md` in the bare
  `O-<letter><digits>` form, which the check reads as a citation of a
  *workbench* question, and the workbench defines none of them. Fixed by
  changing how they are *spelled*, not what they say: "that repository's local
  `O-C` numbers 1 and 2" rather than the bare tokens
- **and the boundary that permits that edit in an append-only file is worth
  stating, because this session refused a similar one an hour ago.**
  **Append-only protects claims, not typography.** Re-spelling a citation so a
  tool can read the file changes no assertion, exactly as fixing a broken
  markdown link would not; that is why it is allowed here. Rewriting
  "`BORROW-012` does not exist" into "does exist" *would* change an assertion,
  which is why that entry still stands above with its correction appended
  instead. The test is whether a reader's belief about what was true, or about
  what this session believed, would differ afterwards
- **finding against the check skill (0.2.1), and it is a real gap rather than a
  nuisance: `check_refs.py` cannot express "another repository's id".** It skips
  `OPEN_QUESTIONS.md` when gathering references, so the registry's own
  cross-repository citations — `nitpick-tui` O-N2, `nitpick-time` O-N1 and the
  rest — are invisible to it and have never been checked. The moment such an id
  appeared **outside** the registry, in `RECORD.md`, it read as a dangling
  workbench question. Both halves are wrong in the same way: a foreign id is
  neither a workbench reference nor nothing. Wanted: a qualified form the check
  understands — a repository-qualified spelling, `<repo>` and a colon before the
  local id — so a foreign citation is checked
  against *that* repository's registry rather than ignored in one file and
  mis-scored in every other. Third finding recorded against the check skill
  today, after the duplicate-question gap and the case-sensitivity of a sweep
- **a process correction on this orchestrator's own commits: three times today
  I have run `check_refs.py` and `git commit` in one shell block, so the commit
  landed whatever the check then said.** Twice it was clean and once it was not,
  and the dangling reference above was committed before I read the output. The
  check must gate the commit, not accompany it
- a small joke at this session's expense, kept because it is the clearest
  possible statement of the gap: **the entry proposing a qualified spelling
  tripped the check by containing an example of the very id it was proposing a
  spelling for.** There is no way to write the wanted syntax in prose without
  writing something that matches `O-[A-Z]\d+`, which is precisely why the check
  needs a form that carries a repository rather than a smarter pattern

### CI, and the first green run

- **the author pushed, and CI ran green.** `nitpick-regex` run `33835762747`,
  conclusion **success**, 8m48s, job `build`. Three repositories went up —
  `nitpick-regex` `c056ae1..c7b8711`, `nitpick-time` `aad6e45..5b2e0c8`, and the
  workbench `02d4f61..6db0370`, 56 commits being the whole of this session's
  record, which until then existed on one disk. `check_refs.py` was run on each
  before publishing, its rule 5 being the machine-specific-path leak check; all
  three clean
- **what the green run proves is small and the workflow says so itself**, which
  is why it is worth trusting: the pinned compiler builds from a clean checkout
  and LLVM is exactly 20.1.2. It proves **nothing about the library**, because
  `harness/run.py` is a toolchain-pin stub until 0.0.2. The value today is that
  **the one unrehearsable step is now rehearsed** — CI builds the compiler, and
  W-18 forbids building it from here, which is exactly why the worker struck
  that acceptance box instead of ticking it. A struck box became a tested fact
  by the only route that could ever have tested it
- one annotation, recorded rather than fixed: `actions/cache@v4` and
  `actions/checkout@v4` target Node.js 20 and are being forced onto Node 24.
  Not a failure. A library whose CI pins its compiler by full SHA and its LLVM
  to three digits should not be surprised by its actions ageing out
- **verify `s1-nregex-0.0.1-verify-0000` FAIL**, 19.6 minutes, 171 866 tokens,
  71 tool uses — **and the scope is one wrong exit code.** `TRANSCRIPT.txt` §A2
  records `npkc --help -> exit 1`; it is **exit 2**, three times for the
  verifier and twice for me against the sha256-verified pinned binary. The
  substantive point that block supports — that `npkc`'s usage line offers no
  library or module mode — is untouched and correct; `--help` is simply not a
  recognised flag
- **everything else passed, and two things passed harder than they were
  reported.** O-N14's **reach was attacked and held**: asked to find a module
  trivial enough to link clean, the verifier found none — `core.npk` is
  `mod:core;` plus comments, zero functions and zero fallible constructs, and it
  fails identically, because **seven `@npk_failsafe` call sites sit inside
  unconditional prelude coroutine-resume scaffolding** (`npk.resume.prelude.sleep`,
  `.io_ready`, `.io_ready2`, `ByteReader:Reader.read`) that `npkc` emits into
  every translation unit whatever the module contains. So it is not "modules
  that can trap" but every module that is not a root. And O-N13's mechanism was
  read out of `symtab_bind_import` in `src/frontend/symbols.npk`: on a name
  already bound with the same origin it executes `pass prior;`, returning the
  pre-existing symbol and **silently discarding the `flags` argument that
  carries `SYM_PUB`**
- **the detail that makes O-N13 worth raising rather than filing: the comment
  above that branch documents it as the intentional *idempotent re-import*
  case.** Idempotence is right for two plain `use`s. It is wrong exactly when
  the second is `pub`, because then the two calls are not the same request. That
  is a deliberate rule with one unconsidered input, not an oversight in a corner
  — and it is the third defect this ecosystem has raised whose quiet half
  matters more than its loud one, after O-N10 and O-N11
- **O-N13 and O-N14 sent to `nitpick-36`** with the verification status stated
  exactly, the FAIL named as unrelated, and O-N14's kinship to DEF-5 argued: one
  emitted `declare i32 @npk_failsafe(i32)` closes it, and the two are the same
  subject from opposite ends — DEF-5 makes a root's obligation to *supply*
  `failsafe` a refusal at `main`, and this makes a non-root's *reference* to it
  well-formed. Today the compiler enforces neither half
- **O-N13 and O-N14 both ACCEPTED and taken into 1.5.1b as step 3c**, after 3b,
  and O-N14's fix is the one this workbench proposed: **a unit that does not
  define `@npk_failsafe` declares it.** They reproduced it on the compiler under
  test — `lib/nsys.npk`, a module with no `main`, seven calls and no `declare`,
  `llc` refusing with our exact line — and confirmed the root does emit
  `define i32 @npk_failsafe(i32 %a0)`, which is what makes "declare it
  elsewhere" the whole of the fix
- **step 3c goes further than the ask, and this is the outcome to want from a
  raised defect: it adds an `object` stage to both runners** (D-238's single
  `[[test]]` table) whose units are non-root modules compiled to objects that
  `llc` must accept — **including a comment-only one, our `core` shape**. So
  `BUILD_REFERENCE` §4.1's per-module-object model stops being documented and
  starts being *measured on every run*. That is the second time today a defect
  we raised became a monitored property in their harness rather than a fixed
  bug, after DEF-5's thirteen files
- O-N13's fix upgrades the prior binding's visibility when a repeated import
  carries `pub`, so the two orders come to mean the same thing, with a positive
  resolve unit shaped on our §E2/§E3 contrast pair
- **a correction aimed at us that turned out not to bite, and the sweep is the
  point.** They warned that a corrected expectation of "321" is above the
  exit-status range — their own step-3b program computed 321 and the process
  reported **65**, which is 321 mod 256 — and asked whether our transcripts
  record anything similar. **Swept: they do not.** No `expect-exit` header and
  no recorded exit claim anywhere in the six repositories exceeds 255, and the
  only `321`s in our trees are a byte figure (`peak_live` 41 321) and a token
  count (215 321), neither an exit status. Three patterns, per the rule that
  every sweep here has been short by one
- **the fact is kept anyway, because it is our trap more than theirs.** An exit
  status is one byte, so any expectation above 255 is silently taken mod 256 —
  and **this ecosystem carries probe results in exit codes**: 170 for a `0xAA`
  poison read, 94 for a bounds trap, 221 and 107 in the derive probes. Landed in
  `PLAYBOOK.md` beside the timing rule, being the same family — a measurement
  channel narrower than the thing measured, failing silently. With the two ways
  out named: compose weights that cannot sum past 255, the way their regression
  pins 121 as Less 100 + Equal 20 + Less 1 so each contribution is readable from
  the total; or print the value and assert on stdout, keeping the status for
  pass/fail alone
- **DEF-4 landed at step 3b as ratified (D-250)**: a payload enum compares tag
  then payload; a named field or payload goes through its own `eq`/`cmp`/
  `partial_cmp`; an owning payload or an array **refuses by name at the
  declaration**, `NITPICK-DERIVE-006` — so O-N10's quiet half, `Literal(7)`
  comparing equal to `Literal(9)`, is gone in both directions
- **one deviation from their plan, recorded there and worth a note here because
  it touches a library shape: a generic parameter field keeps the operator
  form.** The prelude implements `Eq`/`Ord` for no scalar, so `Box<int32>` has
  no method to call; `Eq` over `T` derives and an order over `T` is refused by
  the checker exactly as before. Raised on their side as **S-24** for the
  author: whether the prelude should grow scalar impls so a synthesized bound
  could serve. **Nothing here is blocked** — no library has yet wanted an
  ordering over a generic parameter — but `nitpick-regex`'s probes 03 and 04 are
  the generic-container and generic-impl shapes, so stream 1 is the first that
  would meet it
- report `s1-nregex-0.0.1-0019` **DONE** — 121 958 tokens, 70 tool uses, four
  commits, about three quarters of an hour and "almost all verification rather
  than editing", which is the right ratio for a FAIL re-dispatch. All three
  items done: the exit code corrected, the CI box ticked with run
  `33835762747` cited as evidence, the Node 20 annotation recorded as a dated
  future maintenance item
- **and the one wrong number sat on an ecosystem-wide gap. Nothing documents
  what `npkc`'s exit codes MEAN, while `BUILD.md` rule B-6 orders every harness
  in this ecosystem to assert on exactly those integers.** The alphabet, read
  out of the compiler's source at the pin and confirmed here directly: **0**
  success; **1** REFUSED, with diagnostics, the compiler having judged the
  program; **2** the driver could not proceed and judged **nothing**; **3** a
  `failsafe` trap
- **the dangerous half, and it is reachable through ordinary use rather than a
  malformed command line: a `use` naming a path that is not there exits 2, not
  1.** `graph_load_all` returning `< 0` makes `front_run` `pass 2i32`, and
  `main` passes it through — both confirmed here at the pin. **Every library
  imports by relative path until O-N2 closes**, so a typo'd or moved import is
  exactly this case, and **a harness reading "nonzero means refused" scores a
  MISSING FILE as a passing rejection test** — silently, and for as long as
  nobody looks. All six repositories are about to write that harness; 0.0.2 is
  the cycle that writes the first one. Landed in `PLAYBOOK.md` with the rule:
  assert the specific integer, never `!= 0`, and treat a 2 where 1 was expected
  as a broken fixture rather than a pass
- **"short by one" is now FOUR FOR FOUR, and the fourth is the most
  instructive.** The worker's own enumeration of the `exit 2` sites was short by
  **two**, with one line number off by one — written by a session that had just
  been handed the rule in its own dispatch, and caught only by re-reading the
  source line by line rather than grepping it again. Recorded in the playbook as
  a fourth entry, because a rule with four instances and no counter-example is
  no longer a caution
- **a good refinement of a rule this session made earlier today: a transcript
  that claims to be verbatim must show where it was later touched.** The fix for
  a wrong number is the corrected number **plus a dated note** saying what it
  previously said and how the correction was obtained — never a silent edit,
  which leaves a file asserting it faithfully records a run that reported
  something else. That is the append-only principle applied to evidence rather
  than to the record, arrived at independently by a worker
- **the alphabet is NOT yet raised with the compiler, deliberately.** It is a
  documentation gap of exactly O-N12's shape and the batch is open, so it should
  go — but the enumeration behind it was short by two on its first telling, and
  sending an incomplete alphabet would be the `BORROW-012` failure again in a
  new costume. It goes when the verifier confirms §F is complete. **Waiting
  costs minutes; being wrong in front of the compiler session costs their time
  and our credit**
- one more finding, small and true: **the one thing a pinning workflow forgets
  to pin is its own actions.** `actions/checkout@v4` and `actions/cache@v4` are
  moving tags in a file that pins a compiler by full SHA and LLVM by exact patch
  release — the only floating inputs it has, and the source of the run's only
  annotation. Recommended for the commit that next bumps the compiler pin, so
  one deliberate commit runs the full suite for both
- **verify `s1-nregex-0.0.1-verify-0055` FAIL — on exactly the claim the
  dispatch told it to attack, and it was right.** §F's causal claim, *"a `use`
  naming a path that is not there exits 2, not 1"*, is **false**. A missing
  import exits **1** with `NITPICK-RESOLVE-005: cannot find …`. Reproduced three
  times by the verifier — including on a byte-faithful copy of this
  repository's own `import.npk` with only the path typo'd — and twice more here
  directly. Only a missing **root argument on the command line** reaches
  `pass 2i32`: `npkc no_such_root.npk` prints nothing and exits 2
- **why, and the mechanism is worth recording because the wrong version was
  plausible:** `graph_load_all`'s return is fed **only** by its own direct call
  on the command-line file. Every `use` reached transitively goes through
  `resolve_use`, which does its own existence check, pushes a diagnostic and
  returns not-found — `graph_load` is never called — so the pipeline's generic
  "diagnostics exist" branch produces the ordinary refusal
- **this one is MINE, not the worker's, and it went furthest.** I confirmed
  `pipeline.npk`'s `pass 2i32` and `main.npk`'s pass-through myself, called the
  finding "real", **and landed it in `PLAYBOOK.md`** — the document six
  libraries read — inside an hour of receiving it. The worker wrote it; I
  amplified it and gave it authority
- **the shape of the error, stated plainly because it is the third of the night:
  confirming a code path EXISTS is not confirming that your scenario REACHES
  it.** `BORROW-012` grepped in the pinned tree when the claim was about an
  unlanded one; line numbers taken from the compiler's HEAD and quoted as the
  pin's; and now a `pass 2i32` correctly found and wrongly reached. Each time
  the observation was accurate and the inference was not. **The cure is cheap
  and I did not apply it: produce the behaviour.** One four-line file and one
  command settle it in under a minute — which is exactly what settled it, once
  someone ran it. Landed in `PLAYBOOK.md` as its own rule
- **what survives, and it is most of it.** The verifier independently
  enumerated `src/main.npk` at the pin: **fifteen `exit 2` sites**, matching the
  corrected §F site for site and confirming the "short by two" claim
  numerically; two `exit 0`; three `exit 1`; and **`3` is real rather than
  inferred** — it is npkc's own `failsafe`, 36 named arms plus `(*)` and a
  trailing `exit 3i32`. The alphabet stands and "2 is not a refusal" stands
- **and the corrected hazard is SHARPER than the false one, which is the part
  worth having.** A missing import produces exit **1** — *the very code a
  rejection fixture expects*. So a rejection test whose fixture path is typo'd
  or later moved **passes for the wrong reason**: it wanted a refusal, it got a
  refusal, and the refusal was about the path rather than the thing under test.
  Nothing reports it. The rule is therefore stronger than "assert the specific
  integer": **a rejection fixture asserts the diagnostic CODE as well as the
  exit code**, because exit 1 alone cannot separate "refused for the reason this
  test is about" from "the file was not there". Every library imports by
  relative path until O-N2 closes, so this is the ordinary case
- **the restraint paid for itself exactly as intended.** This alphabet was
  deliberately NOT sent to the compiler while the enumeration was unconfirmed,
  on the ground that shipping an incomplete version would be the `BORROW-012`
  failure in a new costume. The enumeration turned out fine and **the causal
  claim beside it did not** — so the thing withheld was wrong for a reason
  nobody had predicted. Waiting cost forty minutes. It goes over once the
  correction lands and is verified
- report `s1-nregex-0.0.1-0110` **DONE**, 134 592 tokens, 59 tool uses, one
  commit `3679bf8`. The claim is corrected and, more usefully, **measured** —
  a control tree and a typo'd twin differing in one line, the typo'd one exiting
  1 with `RESOLVE-005` three times, and a missing root argument exiting 2 with
  zero bytes on both streams, checked by `wc -c` rather than by eye
- **the worker checked MY list and it was over-long.** The re-dispatch named
  four places the false claim had travelled to; swept in six phrasings with
  `-i`, the tree held **three**, and one site I named — the first REPORT block —
  did not carry it at all. **So sweep lists here have now been wrong five times
  running: short four times and OVER-LONG once**, which retires the shorthand
  "assume yours is short" in favour of "assume yours is wrong". Landed in the
  playbook. It was caught only because a worker checked the list it was handed
  rather than working from it, which is the second time today that habit has
  paid — the first being the `O-C` prefix that would have recreated its own
  collision
- **the two copies it flagged as outside its scope were already corrected**, and
  its flag was a stale read: `BOARD.md`'s only remaining mention of the claim is
  inside the sentence declaring it false, and `RECORD.md`'s is the correction
  entry itself. Flagging them anyway was right — the cost of a redundant flag is
  one check, and the cost of the last surviving copy being the wrong one is
  permanent
- **a rule this session had not thought of, and it is already too late to
  apply: a commit subject names a CHANGE, not a FINDING.** `e478a6a`'s subject
  ends "and one of them bites libraries", which is the false claim in six words.
  It is pushed, CI has run on the tree above it, and every `git log` carries it
  from now on. The file was corrected within the hour; the subject cannot be.
  A subject saying what the commit *did* would have aged into a true sentence.
  Landed in `PLAYBOOK.md`
- **the worker made the same class of error again inside the correction, and
  caught it before committing**: a first draft of §F's note said "five runs
  across two sessions" without counting; it is eight across three. Its own
  formulation is the right one — **an assertion about your own evidence is an
  assertion, and gets checked like one**
- **it also put the measurements in a NEW section §G rather than folding them
  into §F**, on the ground that §F is a *reading of source* and §G is a
  *measurement*, and that a section which says of itself "this is a reading, not
  a measurement" is naming its own failure mode. That is a better instinct than
  the dispatch asked for: it stops a reading borrowing a measurement's authority,
  which is precisely how the false claim acquired its
- **and the finding that shrinks the whole episode: `BUILD.md` rule B-7 (D-237)
  already requires a rejection fixture to assert the diagnostic code.** Under
  verification. If it holds, the ecosystem already had the rule that makes the
  corrected hazard unreachable, and the false claim's real cost was that it
  pointed a harness author at the exit code **alone**, in the one place where
  B-7 is what saves them. Recommended to 0.0.2 as a load-bearing check rather
  than a nicety, and §F now says so addressed to that cycle by name
- **nothing goes to the compiler from this episode.** The exit-1/exit-2 split is
  correct behaviour, not a defect — the earlier claim was a misreading of it.
  The only residue is that the alphabet is undocumented, which is a small
  documentation gap of O-N12's shape, and after being wrong twice on this
  subject in one night this workbench will raise it only once the verifier has
  passed the corrected text, if at all
- **verify `s1-nregex-0.0.1-verify-0140` PASS** on `3679bf8`, 12.3 minutes,
  137 892 tokens, on a **smaller model per §12** — the second use of that
  override, and it reproduced both measurements from a fresh scratch tree with
  **its own fixture name** (`lib_NOPE.npk`, not the worker's `lib_MISSING.npk`),
  ran a control alongside to isolate the single-line change, counted stdout and
  stderr in bytes rather than eyeballing them, swept seven phrasings for the
  false claim, and spot-checked **every** compiler line number the commit cites
  against the pin. `advance nitpick-regex 0.0.1 → 0.0.2`
- **and it settled the open question: `BUILD.md` rule B-7 (D-237) already says
  it.** Verbatim: *"unexpected diagnostics fail a test as surely as missing ones
  … the set of codes a rejection test reports must **equal** the set its
  expectations name."* So the ecosystem already had the rule that makes the
  corrected hazard unreachable, and **the false claim's entire cost was that it
  pointed a harness author at the exit code alone**, in the one place where B-7
  is what saves them. An hour of three sessions' work to end up where a rule
  written at planning already stood — which is an argument for reading the
  specification before measuring, and equally an argument for measuring, since
  nobody had connected B-7 to this until the wrong claim forced the question
- **0.0.1 closed after three re-dispatches and four verifications**, one of them
  a FAIL this orchestrator caused. Its cost is the honest number for W-4: the
  skeleton itself was, in the worker's words, "twenty minutes of typing"
- `advance` — and **0.0.2 is where the night is spent**. It builds
  `harness/run.py`, whose `program` stage judges a test **by its exit code** at
  -O0 and again under `opt -O2`. Every exit-code finding of the last four hours
  lands in that one file: the alphabet, `2` meaning nothing was judged, the
  one-byte ceiling, and B-7's requirement that a rejection fixture assert the
  diagnostic-code *set*. It also carries RX-119, the deferred manifest entry,
  since 0.0.2 owns the runner and can move the seven probe paths and fix
  0.0.0's citations in one commit
- report `s1-nregex-0.0.2-0152` **DONE** — the harness. One commit `e35ba16`,
  295 467 tokens, 111 tool uses, **24/24 units passing in 22.79 s at 80 328 KiB
  peak RSS**. Both checks clean, tree clean. 0.0.3 amended in place rather than
  rewritten. `advance` waits on the verifier
- **the finding that leaves this repository: a differential check is only as
  wide as the thing it diffs.** RX-116's undefined-symbol difference is correct
  and **cannot see a syscall** — measured, a program with `sys(39i64)` in `main`
  has the same 29 undefined symbols as one without, because `npk_sys6` is
  already the prelude's. **Confirmed here that all six repositories plan that
  same scan**, it being in every `meta/specs/BUILD.md`. So five others are on
  course to tick an acceptance item for a check that cannot do what its name
  promises. **Under verification, and deliberately NOT yet landed in
  `PLAYBOOK.md` nor noted on the other streams' rows** — the same restraint that
  paid twice tonight, and no stream is about to start, so waiting costs nothing
- **three more findings, all held pending the same verification**, and all of
  them about instruments rather than about the language:
  - **a check that did not apply reads exactly like one that passed.**
    `reaches_src` answered "no" for every program when handed a relative path,
    silently — the scans would never have run while the suite stayed green.
    **This is the third instance tonight of a gate that cannot fail**, after the
    `exit 0` leak gate and the `SAFETY.md` bounds promise, and the worker's own
    rule is the right one: a predicate that gates a check needs a positive and a
    negative case run against known members, not a reading
  - **measure the instrument before adopting it.** Counting `@npk_sys6` call
    sites is 2/3 at `-O0` and **5/6 after `opt -O2`**, because inlining
    duplicates the floor's own sites — so an IR-shape claim measured only after
    optimisation is a claim about the optimiser
  - **exit 2 arrives with an EMPTY stderr**, so a runner that logs only what the
    compiler said shows no reason at all for a failing test — which is the
    practical half of the exit alphabet and belongs beside it
- **O-N15 raised and its number allocated** (`O-N14` was the highest): `npkg`'s
  `expect_read` accepts an `expect-exit:` above 255 and `run_binary` compares it
  against a one-byte status, so such a test fails forever with a true and
  useless message. Blocks nothing, and this repository's `harness/expect.py`
  already refuses the value, so nothing waits on it
- a clock note, since W-4 consumes these numbers: the worker reports 33 minutes
  measured 01:15 → 01:48 on the clock its checkout sees, while this session's
  `date` read 01:52 when the claim was written and the harness reports
  37.9 minutes elapsed. **`git log` timestamps are the authority** for anything
  that has to be compared across sessions; a worker's local clock is not
- **verify `s1-nregex-0.0.2-verify-0155` PASS** on `e35ba16`, 10.5 minutes,
  136 494 tokens, 80 tool uses — and **every claim was checked by execution
  rather than reading**, which is the discipline this repository spent the night
  learning. It re-ran the harness itself (24/24, 23.0 s, 80 580 KiB, against the
  report's 22.79 s and 80 328 KiB — ordinary variance, stated as such rather
  than flagged); built both halves of the syscall pair and diffed their symbol
  sets; **reconstructed the pre-fix `reaches_src` and ran it against four
  members whose answers were known**, two true and two false, reproducing the
  silent failure and confirming the fix on all four; and **proved B-7
  behaviourally** by building a fixture naming a wrong diagnostic code and
  getting the two failures code-set equality should produce
- **RX-120 confirmed in both halves, and the second half is the useful one.**
  The symbol differential genuinely cannot see a syscall — 29 undefined symbols
  each way, sorted sets differing by nothing. **And the proposed remedy works**:
  the same pair through an IR call-edge scan flags `main` calling `npk_sys6` and
  passes the baseline. A named gap with a working remedy is worth far more than
  a named gap, and the dispatch asked for the second half precisely because a
  remedy that also failed would have been worse than none
- **relayed to the four other library streams on their board rows**, with the
  instruction to treat the acceptance item naming the symbol diff as **unmet**
  rather than merely imprecise. `nitpick-posix` carries it too and is outside
  this workbench's write scope, so it is recorded here and on stream 3's row
- **the three "cannot fail" findings of the night now name a pattern**, and it
  is in `PLAYBOOK.md` as one: the `exit 0` leak gate, the `SAFETY.md` bounds
  promise, and a predicate that silently answered "no" for every program. All
  three are **a check whose NAME describes the property while its MECHANISM
  covers something narrower** — and all three passed every run they were ever
  part of. The rule that follows is the one the worker wrote: a predicate that
  gates a check gets a positive and a negative case against known members
- **a nuance the verifier added and was right to**: the scanned-count guard is
  informational — `run.py` prints which members were scanned but nothing
  hard-fails if that regresses. It noted the report claims only a prescriptive
  lesson and not a regression guard, so nothing overclaims, but flagged that
  **printing is exactly what "green because it never ran" looks like**. Recorded
  as a preference in the playbook: prefer a runner that fails on a regressed
  scan count over one that prints it
- **RX-119 discharged cleanly, and the method is the precedent**: seven files
  moved as **pure renames**, `0.0.0.md` not touched at all — `git diff` against
  the preceding commit is empty — and a dated, marked note in
  `tests/probe/TRANSCRIPT.txt` naming all seven moves, so a verified artifact's
  citations resolve without the artifact being edited. That is the redirect
  pattern 0.0.1 invented, applied a second time by a different subcycle
- **0.0.3 amended in place, and the verifier gave the right reason it is
  allowed**: its status line reads `PLANNED`. An unexecuted plan is amended; a
  verified execution record is not. That distinction is sharper than the rule
  this workbench affirmed earlier — which said "a committed REPORT block is
  history" — and it generalises it: **what may be edited depends on whether the
  document records something that happened**
- **O-N15 verified from the compiler's source and sent.** `expect_read` checks
  only `text_int`'s `is_error` with no upper bound; `run_binary` compares the
  OS-truncated one-byte status against that unbounded value with `!=`. And the
  counter-claim holds by execution: this repository's `harness/expect.py` has
  `EXIT_MAX = 255` and `SIGNAL_MIN = -64`, accepting 255 and −11, refusing 256,
  321 and −65
- `advance nitpick-regex 0.0.2 → 0.0.3`

### A clean pause — 2026-09-04 02:20

- **paused at the author's request with nothing in flight.** No agent of this
  session is live; all six repositories are committed **and pushed**; both
  checks are clean everywhere; the questions table is empty; nothing is owed to
  the compiler session. The writer lock is **held rather than released**,
  because the same session resumes — §15's clean-stop procedure applies at a
  session's end, not at a pause inside one, and releasing it would make a
  successor take a lock nobody had left
- **what is unblocked when work resumes: `nitpick-regex` 0.0.3, and nothing
  else.** Stream 2 is parked on the compiler's landing message. Stream 3 has
  never run
- **what is owed, in one place**, so no successor has to reconstruct it:
  - **at the re-pin, in `nitpick-time`** — probes 09 and 10, held by the
    author's ruling on O-N9; re-recording `missing_failsafe`'s two transcripts
    to `NITPICK-REACH-003`; and correcting the five sites that state *DEF-3 adds
    no new diagnostic code*, which step 2 falsified by allocating
    `NITPICK-BORROW-012`
  - **from the compiler** — the 1.5.1b landing message with the commit, whether
    `build/` was written after it, and the after-numbers on our recipes. Six of
    this workbench's defects are in that batch: O-N4, O-N8, O-N9, O-N10, O-N11,
    plus O-N13 and O-N14 at step 3c, with O-N12 settled in step 2 and O-N15
    filed at low priority
  - **at each stream's next claim** — RX-111's false bounds promise in four
    `SAFETY.md` files, and **RX-120's undefined-symbol scan in all six**, whose
    acceptance item should be read as unmet until an IR call-edge scan stands
    behind it
- **a measurement worth having before it is forgotten: CI's cost collapsed
  after the first run.** 8m48s, then 1m02s, then 1m35s — `actions/cache@v4`
  is doing its job on the compiler build, so a green run costs about a minute
  in the ordinary case and the eight-minute figure is the cold-cache one. That
  matters for how freely this ecosystem can push, and it is the strongest
  practical argument for the Node 20 bump being scheduled rather than urgent:
  the cache action is the one earning its keep every run
- **compiler status: O-N15 taken as a rider on step 5, and step 5 found two
  defects it asked us to check ourselves against.** Both checked, read-only, and
  the answer is small
- **DEF-8 — the `pass` clear cleared the ROOT binding's drop flag for a
  COPYABLE field of an owning local**, latent since 1.2.3 and invisible until
  `List<T>` began to own. `pass xs.count` leaked every list. **Our exposure,
  measured rather than assumed:** `nitpick-regex`'s
  `probe04_inherent_generic_impl.npk:89` does `pass self.count` over a `Vec<T>`
  **by value** — the shape exactly — and `probe08_sparse_set.npk:121` is the
  same family through a nested container. **Neither leaks at this pin**, because
  `Vec<T>` does not own until D-247, which is step 5 — *the same commit that
  fixes DEF-8* — so **no measurement of ours is wrong today** and both simply
  want re-running after the re-pin. Added to stream 1's row
- **and three sites that looked like it and are not**, checked rather than
  waved through: `probe01`'s `pass i.a` is over `Inst`, a pure-POD
  `{ InstKind; uint32; uint32 }`; `probe07`'s `pass src.len + n` is over a
  `uint8[]` **parameter**, which does not own; and `probe03`/`probe06`'s
  `move(v.items[i])` moves an **owning element**, which is the legitimate case
  DEF-8 is not about. Four sites reduced to two by reading the declarations
- **DEF-9 — the session's soft `RLIMIT_NOFILE` of 1 048 576 made every
  descriptor-exhaustion proof pass against a leaking build.** Both runners now
  lower their own soft limit to `nitpick.toml`'s new `[limits] nofile` (1024)
  before spawning. **Our exposure: none.** Swept for `EMFILE`, `ulimit`,
  `nofile`, `rlimit` and descriptor-exhaustion wording across both workbenches —
  no such proof exists anywhere here, and no manifest carries a `[limits]`
  table, which is correct since an absent table means 1024. If a library ever
  writes an "opens until `EMFILE`" proof, `(ulimit -n 1024; ./prog)` is the
  spelling that matches the runners
- **the general lesson from DEF-9 is worth more to us than the defect**, and it
  is the fourth of its kind tonight: **a proof that consumes an environment
  limit is a proof about the environment.** A descriptor-exhaustion test under a
  1M soft limit exhausts nothing and passes; it joins the `exit 0` leak gate,
  the `SAFETY.md` bounds promise and the silent `reaches_src` predicate as a
  check whose name described the property while its mechanism covered something
  narrower — except this one's mechanism was *outside the program entirely*
- step 5's final numbers, recorded for the re-pin comparison: `list_drop` (100
  rounds of 10 000 strings) peaks at 662 515 bytes live against `list_once`'s
  662 515, ratio **1.00** against a bound of 2; the temporaries probe stays
  **×3.0** against a bound of 4; the program sweep is 217 programs, 0 failures.
  Eight cumulative-prefix harnesses (steps 0–4) are running; step 5's follows
- **compiler round 2: step 0 has LANDED on main as `cd8a429`**, the first
  cumulative-prefix run having come back red at step 3 for four fixable causes.
  Steps 1–4 are rebased and running, step 5 behind them. Useful for us: **the
  nine landings after step 0 are fast-forwards of validated prefixes**, so main
  does not move under anything built against it today
- **S-27 / TYPE-062 — the statement after `wild_release_all()` must be `exit`.**
  Three unit tests released the heap and then *returned* from `main`; once
  `List<T>` owned, their scope-exit drops ran over unmapped memory and the
  refusal's own trap route died in a segmentation fault. **Our exposure: none.**
  Swept both workbenches — **nothing here calls `wild_release_all()` at all**,
  which is what the compiler predicted, a library never calling the release
- **S-26 — a `move`/`pass` out of a FIELD or ELEMENT now leaves the canonical
  vacant value and the aggregate stays live.** Before, a field move cleared the
  **whole root's** drop flag, so every sibling leaked; and because a field
  overwrite drops unconditionally, a field moved out and then reassigned was a
  **double free**. **Our exposure, read rather than assumed:** two sites move
  out of an element — `nitpick-regex`'s `probe03_generic_move.npk` `free_owning`
  and `nitpick-time`'s `probe06_generic_vec.npk` `free_names`. **Neither puts an
  element back**, so neither carries the double-free shape at all
- **but the re-pin consequence is larger than DEF-8's, and this is the part to
  carry**: `free_names`'s own comment reads *"Measured above: this is the
  difference between 125 MiB and nothing"* — **it is the remedy half of the leak
  finding**, the function that proved a container's elements must be moved out
  to be dropped. Its semantics change at the re-pin in **two independent ways at
  once**: S-26 alters what a move out of an element does to the aggregate's drop
  flag, and D-247 makes the container own. **So the 125 MiB figure is a
  before-number, and both `free_*` functions must be re-run and READ rather than
  predicted.** Recorded on both streams' rows. This is the strongest re-pin item
  the workbench has, because it is the measurement the leak rule rests on
- **DEF-12 — the main thread's TLS block was an internal heap allocation the
  release unmapped**, so any trap after a release segfaulted; it is a raw
  mapping now, in no table. No action here, since nothing of ours releases
- **and the sweep rule caught me again, in the same minute I invoked it.** My
  first pattern for S-26's sites returned **two**; a second, narrower one
  returned **nothing**, and had I run only the second I would have reported no
  exposure. The count that is right is the one confirmed against a member you
  already know belongs — and I knew probe03 belonged only because an earlier,
  looser grep had shown it

### 1.5.1b lands — and the re-pin does not

- **1.5.1b is on the compiler's main**, ten commits, each a cumulative prefix
  validated by its own full harness (58/58, parity green, `npkc` byte-identical)
  before landing: `cd8a429` step 0, `953fa83` step 1 (D-248), `5da8d24`
  step 1b (REACH-003), `0758b2f` step 2 (D-249), `6dff555` step 3 (the Sink
  builders), `7e0a465` step 3b (D-250), `4521b55` step 3c (library units as
  objects, `pub use` re-export), `281caaf` step 4 (D-246), `39e69cc` step 5
  (D-247 plus the five findings), `94874ce` the docs landing. **All seven of
  this workbench's defects are in it**, and O-N12 and O-N15 with them
- **the re-pin is BLOCKED, and the `build/` question is exactly why it was
  asked.** Their answer was "Yes: build/ was written" followed by the operative
  clause — *the validations built into worktrees that were then removed, and
  main's own `build/` is untouched by the landings.* **Verified here rather than
  read: `build/npkc`'s mtime is 2026-09-03 18:40 and `39e69cc` was committed
  2026-09-04 08:24 — the binary predates the landing by fourteen hours**, and
  its sha256 (`1c3bea4b…`) matches neither our pinned `950bb1d` (`fbb7d022…`)
  nor anything post-landing. It is an intermediate build from yesterday evening
- **so copying it would produce a pin labelled `94874ce` holding a pre-1.5.1b
  binary.** That is worse than the `tree dirty` case §3 already warns about: not
  an imprecise label but a confidently wrong one, and **nothing afterwards can
  tell a stale binary from a fresh one** — which is the entire reason `PIN.md`
  carries a `binary` line. **W-18 forbids building the compiler from here**, so
  the rebuild is the compiler session's or the author's, and has been asked for.
  **Nothing re-pins and no held work resumes until `build/npkc` is from
  `39e69cc`'s `src/`**
- **the pin procedure's `build/` question earned its place tonight.** The
  predecessor orchestrator called it "the one thing our pin procedure cannot
  determine from outside its tree" and made it a standing item on the landing
  message. Had it not been asked, this workbench would have re-pinned from a
  fourteen-hour-old binary and attributed every subsequent measurement to
  1.5.1b — including the after-numbers that decide whether O-N4 still blocks
- **and a second question raised, because their own figures argue against the
  obvious reading.** DEF-1's fix cut the compiler's own build's **allocation** by
  a fifth (14.24 GB → 11.75 GB) while its **peak live memory went UP** (11.16 GB
  → 11.63 GB), for the stated reason that *every table lives until emission ends,
  so drops shorten nothing in one compilation*. **O-N4 blocks `nitpick-time`
  0.0.5 and 0.5 on PEAK, not on churn** — `probe04_big_fixed_table.npk` cost 281 s
  and **30.9 GiB peak**, and a 16 GiB machine and CI still cannot build the
  library in its shipping shape unless that number moved. The landing message
  carried DEF-1's self-numbers rather than the promised after-numbers on our two
  recipes, which is not the same thing. Asked for both, with the note that
  "peak is unchanged by design" is a perfectly good answer — **what cannot be
  done is closing a blocking defect on an inference**
- **`build/` rebuilt and both answers came back as measurements.** The compiler
  session ran `npkg build` from main's root at 08:48 on `94874ce`, and states
  that rebuilding main's `build/` after a landing is theirs to do from now on —
  it had not been done before our check, and they say the check was correct
- **pin 94874ce, tree clean** — and **verified before copying rather than
  after**: `build/npkc` at 5 491 224 bytes and sha256 `0f8c4678…84`, matching
  what that session computed, mtime 08:48:30, against a landing committed at
  08:24:50. `cmp` identical both files, `sha256sum -c` OK, LLVM 20.1.2. **The
  first clean-tree pin this workbench has had**; `950bb1d` was `tree dirty`
- **`npkrt.o` changed too, and asking was worth it.** DEF-12 made the main
  thread's TLS block a raw mapping, so the runtime is not untouched this time —
  its sha differs from the `950bb1d` pin (`c9ddbcff…` against `869c490d…`) and
  its mtime is 08:43, after the landing. The previous pin's `PIN.md` had
  recorded "npkrt.o byte-identical because the runtime is untouched"; that was
  true then and would have been a wrong assumption now. **A re-pin checks both
  halves**
- **§3's mid-rebuild guard fired and was obeyed.** `find -mmin -2` refused the
  first attempt because the binary was ninety seconds old. It was waited out
  rather than overridden — the guard exists for a binary still being written,
  and "we know it finished because someone told us" is exactly the reasoning
  this workbench has been wrong about three times tonight
- **O-N4 REPORTED DISCHARGED ON PEAK, and the numbers are extraordinary.** Our
  two recipes, compiled by that binary under `NPK_HEAP_STATS` and
  `/usr/bin/time`:
  - `defect/big_fixed_array_cost.npk` (4 000 rows): **~6 s and 580 MiB → 0.24 s
    and 28.97 MB max RSS**, peak_live 22.18 MB
  - `probe04_big_fixed_table.npk` (26 838 rows): **281 s and 30.9 GiB → 1.15 s
    and 75.2 MB max RSS**, peak_live 70.30 MB
  About **400× less peak and 240× less time** on the real table's size, and the
  relation between the two sizes is now linear rather than quadratic: 6.7× the
  rows costs 3.2× the peak and 4.8× the time
- **and they explained why their own earlier figure argued the other way, which
  is the part worth keeping.** The compiler-over-itself number was the wrong
  instrument for our question: *its* peak is the retained tables of a 200-file
  compilation, which nothing frees before emission ends, so a drop-shortening
  fix cannot move it. *Our* recipes' peak was the quadratic builder itself —
  transient buffers reallocated per row — and step 3's Sink removed exactly
  that. Two peaks, two different causes, one number quoted for both. **Asking
  the second question was right, and the answer changed a blocking defect's
  disposition**
- **NOT yet acted on: this is reported, not verified here.** O-N4 blocks
  `nitpick-time` 0.0.5 and 0.5, and a blocking defect is discharged on our own
  measurement, not on a correspondent's — however good the correspondent has
  been all night. **The held work stays held** until a verifier re-runs both
  recipes against the new pin. That is the first dispatch when work resumes,
  and it is cheap now: what cost 281 s and 30.9 GiB is claimed to cost 1.15 s
  and 75 MB, so the verification is seconds rather than the hours it would have
  been yesterday

### Handover to `nitpick-libs-44` — 2026-09-04 08:55

- **clean stop and writer release.** `.internal/orchestrator.session` removed
  and the board's writer line set to `none`, naming `nitpick-libs-44` as the
  successor, per orchestrate §15. Done in that order and *before* briefing the
  successor, so an abrupt close cannot leave the lock naming a dead session —
  the same courtesy this session was shown by its predecessor
- **state at the handover.** Pin `94874ce`, **tree clean**, both binaries
  verified by sha before copying. Stream 1 holds `nitpick-regex` with 0.0.0,
  0.0.1 and 0.0.2 all DONE and independently VERIFIED; 0.0.3 is planned,
  unblocked and **not dispatched**. Stream 2 holds `nitpick-time`, parked and
  STOPPED, with its held work still held. Stream 3 has never run. Every
  repository is committed and pushed; both checks clean everywhere; the
  questions table is empty
- **a constraint from the author that changes what a successor does with a
  defect: the compiler session is near its usage limit and is being brought to
  a stopping point. Bugs found from here are CATALOGUED, not raised for a fix,
  until the quota resets.** That inverts the batching rule this session worked
  under all night — the reason to raise a defect immediately was that the batch
  was open, and it is closing. Record them properly against the registry so the
  batch can be reconstructed when it reopens; do not send them one at a time to
  a session that cannot act on them
- **the one thing this session would want its successor to do first: verify
  O-N4's discharge.** It is reported at 400× less peak and not yet measured
  here, it gates `nitpick-time` 0.0.5 and 0.5, and it now costs seconds where
  yesterday it cost 281 s and 30.9 GiB

### O-N4 discharged on our own measurement — 2026-09-04 12:35

`nitpick-libs-44`, the third orchestrator, takes the writer lock and makes the
verification its predecessor named as the first thing to do.

- **the lock.** Taken from a free line (`none`) at a clean stop, **board line
  first, then the marker file**, which is the order the guard enforces and the
  reverse of orchestrate §2.1. Two of §2.1's instructions are wrong and both
  were carried onto the board rather than rediscovered: the guard permits *any*
  session while the writer line reads `none`, so the refusal §2.1 promises never
  fires and **its absence is not evidence the lock was free**; and
  `CLAUDE_SESSION_ID` is **empty in a Bash tool call**, so §2.1's marker command
  writes a 0-byte file. The id was read from this session's own
  `~/.claude/projects/<slug>/<uuid>.jsonl` and **cross-checked against the
  scratchpad path**, which carries the same uuid — two independent sources
  rather than one mtime — and `ListAgents` then confirmed this session is
  `nitpick-libs-44`, the successor the outgoing board line names. Marker is 37
  bytes, not 0
- **O-N4 is DISCHARGED.** Both recipes, three runs each, against pin `94874ce`,
  using the command `tests/probe/defect/README.md:196` records for the
  before-numbers — `/usr/bin/time -f "%e s  %M KiB" "$NPKC" <file> -o <out>.ll`:

  | recipe | rows | before | **measured here** |
  |---|---|---|---|
  | `defect/big_fixed_array_cost.npk` | 4 000 | 5.30–6.19 s · ~593 592–593 992 KiB | **0.24–0.25 s · 28 768–28 960 KiB** |
  | `probe04_big_fixed_table.npk` | 30 000 | 281 s · 30.9 GiB | **1.19–1.32 s · 74 936–74 996 KiB** |

  **~430× less peak and ~227× less time** on the large table, against a reported
  1.15 s / 75.2 MB — reproduced. The relation is no longer quadratic: 7.5× the
  rows costs 5.0× the time and 2.6× the peak, where quadratic would be ~56×
- **the check that would have made this a hollow green, and why it was run.**
  A compiler can be made fast by emitting less, and *`npkc` exit 0 is not
  well-formedness* — O-N11 is exactly that shape, a program that exits 0 while
  emitting calls to an undefined `@npk_failsafe` that only `llc` refuses. So
  exit 0 was paired every run with an `.ll` actually written (2 672 442 B)
  carrying `@"npk.probe04_big_fixed_table.TRANSITIONS" = constant [30000 x …]`
  with **30 000 `i64` rows present**, and then `llc -filetype=obj` was run on it:
  **exit 0**, 0.61 s, a 660 360 B object, with the symbol in **`.rodata`, flags
  `A` and not `W`, size 0x75300 = 480 000 B = 30 000 × 16**. That last line
  independently re-confirms **S-19** — `fixed` module state is read-only, with no
  startup initialisation — as a free by-product of measuring something else
- **the instrument was commissioned before it was trusted**, positive and
  negative: a real tree file (`probe11d_floor_only.npk`) at exit 0 with an `.ll`
  written, and a malformed file at exit 1 with none. The first positive control
  was **hand-written and failed on invented syntax** — `fn main() -> int32` is
  not Nitpick — which is its own small lesson: take a control from the tree,
  where the syntax is known good, rather than composing one from memory
- **and the grep for the table found nothing on its first phrasing.**
  `@[A-Za-z_.]*TRANSITIONS` misses `@"npk.…TRANSITIONS"` because the symbol is
  *quoted*. Had that been the whole check, this entry would record the opposite
  conclusion — the table read as absent, the discharge read as hollow. §6's
  "run it twice with different phrasings" earned its place on a check that was
  about to be believed
- **a citation drift, corrected in form only.** The 281 s / 30.9 GiB figure is
  `probe04`'s **30 000** rows — `[30000 x ZoneTransition]` in the emitted IR —
  not TM-007's tzdb, which is 26 838. `BOARD.md`'s O-N4 row and `RECORD.md:2275`
  had attributed the probe's cost to the tzdb's row count. The board is live
  state and is corrected; **line 2275 is left exactly as it stands**, because it
  records what a correspondent reported and what this workbench believed at the
  time, and that is not a thing a later session rewrites. No conclusion moves
  either way: the probe is the *larger* of the two, so the real table was always
  going to cost less than the number quoted for it
- **still stopped, and deliberately.** O-N9, O-N10 and O-N11 have *landed* at
  this pin but are **not measured here**. They get the same treatment O-N4 just
  got before the work they hold is released — that a defect landed is a
  correspondent's report, and this entry exists because the workbench does not
  discharge blocking defects on those

### The Q-10 sweep's residue — the checkbox, not the prose — 2026-09-04 12:50

Found while assembling stream 1's dispatch, by checking the site list the board
handed over instead of working from it. Two of the four line numbers the board
named for `nitpick-regex` no longer pointed at the leak gate at all — 0.0.2's
landing moved them — which is `PLAYBOOK.md` §6's "cite the kind, not the line
number" arriving as a live inconvenience rather than as a maxim.

- **the finding: seven live sites in five repositories.** Every repository's
  *narrative* text now carries the correct formulation — *D-151 counts `wild`
  blocks, D-188 counts live drivers, and neither sees a managed body*. The
  **acceptance checkbox a worker ticks** still states the unfalsifiable gate.
  `nitpick-regex/…/0.0/README.md:170` is the sharpest: it names **`vec_free`**,
  asserting the gate for exactly the managed case D-151 cannot see, inside the
  cycle that builds `Vec<T>` and `Bytes`. `nitpick-parse/…/0.0/README.md:104` is
  the worst ecosystem-wide: it cites **`(D-151)` in support of** the broad claim
- **why the sweep missed it, which is the part worth keeping.**
  `nitpick-regex/meta/DECISIONS.md:550` records that its site list was *"produced
  by `git grep -n 'D-151'` and not from recall"* — the correct instinct, applied
  honestly, and it still under-counted, because **five of the seven checklist
  lines never cite D-151**. The prose was corrected *because the prose is where
  the citations live*. That repository's note says "four sites stated, and two
  more implied"; the tree holds two more it could not see. **A generating command
  is only as wide as its pattern, and a pattern built from citations finds only
  cited claims**
- **the fifth instance of §6's shape, and the first in acceptance criteria.**
  Prose is read; a checkbox is ticked. This one would have been ticked green in
  five repositories on the case it cannot see
- **the finder's own first sweep was short by one**, and by a mechanism worth
  recording: it filtered out every line mentioning `D-151` on the assumption that
  citing the decision meant being *qualified* by it. Site 6 cites D-151 **as
  support for the false claim**. That is `PLAYBOOK.md` §6's "a wrong citation
  still resolves" met from the other direction — not a checker fooled by a
  resolving reference, but a *sweeper* fooled by one. Three phrasings were
  needed; the third found it
- **and a numbering collision caught before it landed.** This was first written
  onto the board as `RX-121`, which is **already allocated** in
  `nitpick-regex/meta/DECISIONS.md:1113` to an unrelated decision, as is
  `RX-122`. `check_refs.py` returned **clean** on it, exactly as its contract
  says it must — it catches an undefined reference and never a re-used one. The
  finding is recorded as a **Q-10 residue** with no `RX-` number, because `RX-`
  is one repository's namespace and this spans five; each allocates its own when
  its stream fixes it, and `nitpick-regex`'s next free is RX-123
- **routing (W-7).** `nitpick-regex`'s two sites and `nitpick-time`'s one go to
  the dispatches opening now, because those repositories are claimed.
  `nitpick-tui`, `nitpick-parse` (two) and `nitpick-sockets` wait for their own
  streams' claims and are on the board so the next claim inherits them

### Both streams closed, and the board corrected its own premise — 2026-09-04 13:40

Width 2, at the author's direction. Both subcycles DONE and independently
VERIFIED PASS; verifiers run on a smaller model per orchestrate §12, which is
sound because every check they run is a command with an exit code, and was
chosen deliberately to conserve the author's weekly quota.

- **`nitpick-time` 0.0.0 DONE, VERIFIED PASS at `1c43872`.** **All four stops
  are down**, each discharged on this workbench's own measurement rather than on
  a correspondent's report: O-N4 (this orchestrator, then re-confirmed by the
  worker re-running probe 04 whole), O-N9 (TM-110), O-N10 (TM-111), O-N11
  (TM-112). No compiler defect found. **0.0.5 and 0.5 unblocked**
- **`nitpick-regex` 0.0.3 DONE, VERIFIED PASS at `91657eb`**, harness 63/63 in
  37.5 s against the worker's reported 37.6 s
- **THE FINDING OF THE SESSION IS THAT A WORKER CORRECTED THIS BOARD'S PREMISE,
  WHICH THE ORCHESTRATOR HAD PUT IN ITS OWN DISPATCH.** The board said `Vec<T>`
  "does not own **until** D-247". Stream 1 found `decl_is_list`
  (`../nitpick/src/frontend/type_layout.npk`) matches only a struct named
  **exactly `List`**, homed in the compiler's `list` scope, with exactly three
  fields `items` (pointer), `count`, `cap`. **No container in this ecosystem is
  that**, so D-247 changes nothing for any of them: `Vec<T>` does not own, full
  stop. Confirmed by this orchestrator against the pin's source before the board
  moved. **The 125 MiB managed-body leak is therefore not closed and will not
  be** — and stream 2, working a different repository and not looking for this,
  measured `probe06b` at **125 184 KiB three times at this pin**. Two streams,
  opposite directions, same conclusion
- **the consequence is larger than the correction.** `RX-110` and `RX-123` are
  **permanent, not interim**: the `exit 0` leak gate covers the `wild` block
  alone and no compiler fix is coming to widen it. 0.0.4's leak acceptance needs
  a **memory cap for the managed half in every repository**. `nitpick-time`,
  `nitpick-parse` and `nitpick-tui` inherit this at their next claim
- **and the distinction stream 1 drew is the transferable part:** the three
  probes owed at the re-pin **re-ran clean**, which is evidence the shape is
  *outside* DEF-8's scope — **not** evidence the fix is right for it. A less
  careful report would have written the second, and it would have passed
- **how the false premise travelled.** It came off this board, into *both*
  dispatches in the orchestrator's own words, and was caught only because a
  worker checked a premise it had been handed instead of building on it.
  **A dispatch's stated premises are claims, and the worker is the last line
  that can falsify them.** Dispatches should say so explicitly
- **accepted with a known overstatement, recorded rather than re-dispatched.**
  `nitpick-regex`'s mutation-test **transcripts are not committed** — §4 holds a
  per-case attribution summary table, which is what the acceptance criterion
  required and is why this is a PASS — but `harness/README.md` claims "§4 has
  the transcripts" and it does not. `PLAYBOOK.md` §6 says a summary is not
  evidence, and `nitpick-time` 0.0.0 was once FAILED by its own verifier for
  exactly that, so the precedent cuts against the sentence. Carried to 0.0.4
  because the session is stopping, **not** because it is acceptable
- **a residue the verifier's DENOMINATOR exposed**, which is the same lesson
  stream 1 raised independently. `nitpick-time`'s expect-header sweep covered
  **36 of 42** tracked `.npk`. Three uncovered are support libraries and
  correctly headerless; **the other three are the `missing_failsafe`
  reproductions, which carry no `expect-` header at all** — and they are exactly
  the files whose expected behaviour changed today. The strengthened sweep
  cannot see the three files it most needed to
- **two numbering errors by this orchestrator, both caught before they landed.**
  A finding was first written onto the board as `RX-121`, already allocated to
  an unrelated decision; and `RX-127` was cited for a finding nobody had
  numbered. `check_refs.py` passed the first — its contract is undefined
  references, never re-used ones — and caught neither, because both resolved or
  were removed. What did catch the second class was the check firing on a bare
  `O-N16` cited on the board while the workbench registry had no such entry
- **O-N16 registered in the workbench registry**, catalogued and deliberately
  not raised. DEF-8's landing note says the workbench's *"recipes pass values,
  not fields, out of owning locals"*; two probes here `pass` a field out of a
  by-value local, so the premise is false. **The verdict still holds, by the
  route the note does not give** — a library `Vec<T>` never owns, so DEF-8's
  clearing of an owning local's drop flag cannot reach it. Right answer, wrong
  reason, and the wrong reason is the one a later reader would check themselves
  against

### 1.5.1b's landing recorded, and a paragraph restored — 2026-09-04 14:10

Received after this session had already reached its clean stop and released the
writer lock. Recorded rather than acted on, so the next session inherits facts
instead of a notification it has to chase.

- **the lock was briefly re-taken and released inside a single commit**, with the
  board's `Workbench writer:` line reading `none` before and after. Nothing was
  in flight and no peer held it. Recorded here because the net state hides the
  event, and a reader of the board alone would not know a write happened between
  two releases
- **1.5.1b is COMPLETE.** Compiler `main` at `8dbef43` (docs only above
  `25e555c`); `build/npkc` rebuilt at 14:01, 7 014 696 bytes, sha256
  `5af0d06e…f81810`, *larger* than its predecessor because the compiler is now
  built by a builder carrying the step-4 and step-5 machinery
- **the re-pin is OWED and was deliberately not taken here.** Re-pinning at a
  stopping session would leave a fresh toolchain with no verified measurement
  against it and discard the one this session paid for: O-N4, O-N9, O-N10 and
  O-N11 were all measured against `94874ce`, and that is the pin those verdicts
  belong to. **`npkrt.o` must be taken again and checked, not assumed** — DEF-12
  caught this ecosystem once already on that assumption
- **D-239 swept: no collision in any of the five libraries.** Step 5b moved
  `List<T>` into the prelude and a program's own `List` is now refused by the
  loader. Nothing here declares a `struct:List`, a `mod:list`, or any `list_*`
  function; all five occurrences of the token are **comments** naming the
  compiler's type as the shape our containers imitate. The residue is that they
  cite `src/frontend/list.npk`, which no longer exists
- **O-N16 was closed upstream the same day it was catalogued**, by a docs commit
  correcting DEF-8's closing sentence to give the reason instead of the false
  premise. Worth keeping because it prices the author's constraint: cataloguing
  rather than raising cost **nothing** here — the item was registered properly,
  the correspondent read it at its own convenience, and no session was
  interrupted to act on it
- **A PARAGRAPH WAS SILENTLY DELETED BY THIS ORCHESTRATOR AND IS RESTORED.** The
  13:40 clean-stop edit replaced the board's `PAUSED` block with a `STOPPED`
  one using a span that ran to the next blank line — and the `**Phase:**`
  paragraph lived inside that span. It was recovered verbatim from `d91d0ca` and
  put back, with a dated note in place saying so. **The failure mode is worth
  more than the fix:** `check_refs.py` returned **clean** across the deletion,
  because a removed paragraph breaks no reference; the only reason it was caught
  is that a later edit tried to anchor on the very text that had gone. A
  boundary-matched replacement deletes whatever happens to sit inside its span,
  and nothing in this workbench's checks can see it. **Prefer replacing an exact
  known string over replacing a span to the next blank line**, and when a span
  must be used, print what it consumed

### What the `devteam` experiment gives back — 2026-09-05

The author offered the `devteam` pipeline's first-run data, `devteam` having
been derived from this system. Read read-only; nothing outside `nitpick-libs`
was written. Its failure modes are worth more to this workbench than its
successes, because a system derived from ours fails where ours is weak.

- **THE FINDING WORTH THE WHOLE READ: the write guard cannot see an interpreter
  heredoc, and this harness instructs sessions to use one.** Measured directly
  by feeding `tools/guard_compiler_tree.py` PreToolUse payloads on stdin.
  A redirection, a `sed -i`, and a `Write` at the same existing compiler-tree
  file are all **DENIED**; `python3 - <<PY` … `open(<same file>,'w')` … `PY` is
  **ALLOWED, silently**. The guard documents this limit and names the sandbox's
  `filesystem.denyWrite` as its airtight mitigation — **and `denyWrite` is
  configured nowhere.** `permissions.defaultMode` is `auto` and the guard is the
  only hook wired
- **why it is more than a documented limit.** A harness may ship a standing
  instruction preferring `sed`, heredocs and short scripts over `Write`/`Edit`.
  **This one does**, so a session under it writes through the one unjudged form
  by default, for every write, leaving no refusal and no record. `CLAUDE.md`
  says the write rules are "enforced by the guard where they can be" and a
  reader cannot tell which writes those were. **Every board and record edit this
  session made went through the unjudged path.** Nothing improper happened — the
  lock was held and the compiler tree was never targeted — but the mechanism was
  not watching, which is a different fact from the writes being correct
- **the exposure that actually matters** is a library *worker* following the
  same ambient instruction into `../nitpick`, which is what
  `library-sessions-write-scope` exists to prevent and what can invalidate a
  verification run of several hours. **Filed as question 3 for the author and
  deliberately not acted on: it is a permissions change, and no session should
  make one on its own analysis**
- **a retraction that is part of the finding.** The first pass recorded `sed -i`
  as a second gap. It was a bad test — the probe path did not exist, and the
  `sed` branch requires `os.path.exists` precisely so a sed *expression* is not
  read as a filename. That check is correct. **A guard test must use a target
  that exists, or it measures the test rather than the guard**
- **"is compliance visible in the product?"** — `devteam`'s best contribution
  and a test this workbench did not have. A rule asking for care is not a
  mechanism; a rule that puts the command beside the number it produced is,
  because a reader checks it without re-running anything. It is why
  `meta/DECISIONS.md:550` was worth writing even though its list was short
- **"awareness is not immunity", evidenced from our own tree.** `devteam`
  collected five instances of somebody committing a failure *in the artifact
  where they documented it*. This workbench supplied two more on 2026-09-04
  without needing to look: `RX-121` invented minutes after writing the rule that
  numbers come from the registry, and a nonexistent `RX-127` cited in the very
  note recording that collision — plus a **silently deleted `BOARD.md`
  paragraph** that `check_refs.py` passed clean, because a removed paragraph
  breaks no reference. **Nothing here detects deleted content.** All of it is now
  in `PLAYBOOK.md` §6, which is the argument for mechanical checks over written
  rules — including over that section itself

### The handoff, and the landing notice that was already stale — 2026-09-05

`nitpick-libs-42` briefed and onboarded; it asked five questions, verified the
lock free on two sources rather than on the guard's silence, and stood down
without taking it. Answering its fifth question invalidated part of the brief it
had just been given, which is the entry worth keeping.

- **A CORRESPONDENT'S LANDING NOTICE IS A SNAPSHOT, AND IT AGES.** `nitpick-36`'s
  "final landing notice for 1.5.1b" named `25e555c`/`8dbef43` and a `build/npkc`
  of 7 014 696 bytes, sha256 `5af0d06e…`. Checked at the handoff, one day later:
  HEAD is **`8c69ee4`** — **1.5.2 and 1.5.2b have both CLOSED and 1.5.2c is
  planned and ratified** — and `build/npkc` is **7 014 920 bytes, sha256
  `2f786437…`, mtime 19:42**, a different binary five hours after the one
  described. Nothing was wrong when it was written; it was simply believed for a
  day longer than it was true. **This board had carried it forward as the re-pin
  target and would have pinned an unknown binary**
- **`git status --porcelain` was CLEAN on the compiler tree and that was
  misleading**, which is the transferable half. The work is happening in a
  *worktree* (`.internal/wt/q0`), so a clean root tree says nothing about what
  `build/` was built from. A live `harness.py --verdicts` and `quickemit.py` were
  running at the moment the root read clean. **§3's mid-rebuild guard passes too
  and is also insufficient** — it catches a binary still being written, not one
  built from a tree nobody told you about. The remedy is the one §3 already
  prescribes for uncertain provenance and this workbench nearly skipped because
  the tree *looked* clean: **ask the session that owns the tree, and record the
  answer in `PIN.md`**
- **a verdict is a fact about a pin and does not inherit across a re-pin.**
  **DEF-13 landed after `94874ce`** (verified by ancestry) and its symptom is *"a
  zeroed diagnostic and a lost one"* — while **O-N11's verdict is an identity
  COUNT read out of a diagnostic**, measured while that defect was present. And
  **1.5.2b rewrote derives wholesale** while **O-N10 is a derive defect**. Both
  are to be re-measured at the re-pin. The general rule: *when the thing you
  measured with has changed, the measurement is a historical fact rather than a
  current one* — the same shape as the pin proving "not landed" and never "not
  real"
- **A SECOND DEFECT IN THE WRITE GUARD, opposite in sign to the first.** It
  refuses **`git worktree list`** — a read — as "a mutating git subcommand",
  because its `GIT_WRITE` set contains `worktree`, which has both read and write
  subcommands. **It was not worked around**: the command was dropped and the
  information obtained another way, then recorded. The guard's own docstring
  warns that *"a guard with false positives gets disabled, which is worse than no
  guard"*, so this is exactly the failure mode it named for itself. Filed beside
  board question 3, because the two findings pull in opposite directions — one
  write form is unwatched, one read form is refused — and a fix should address
  both or it will trade one for the other

### The fourth orchestrator onboards, and two sessions nearly wrote the same paragraph — 2026-09-05

`nitpick-libs-42` stood up as successor to `nitpick-libs-44` for a handoff, was
told to onboard and stand down without taking the lock, and did stand down —
except for this one bounded commit, taken because the board was carrying an
instruction that had gone dangerous and the outgoing session closed before it
could receive the corrections.

- **THE NEAR-COLLISION IS THE PART WORTH KEEPING.** Both orchestrators
  independently judged that the stale re-pin target had to be corrected, and
  both began editing **the same paragraph of `BOARD.md` at the same time**. The
  outgoing session committed `62ad168`; the incoming session had an uncommitted
  `Edit` to the same block. **Nothing in this workbench detected the overlap** —
  `BOARD.md`'s `Workbench writer:` line read `none` throughout, so the guard
  permitted both, exactly as its known §2.1 defect predicts. What caught it was
  an **editing tool warning that the file had changed on disk**, which is a
  property of the harness and not of the workbench. The incoming session
  discarded its own edit rather than reconcile two versions of one paragraph.
  **The lock's failure mode is not two writers fighting; it is two writers
  agreeing, arriving at the same conclusion, and silently duplicating.** A board
  line reading `none` is an invitation to exactly this whenever a handoff
  overlaps
- **three deltas measured independently and added on top of `62ad168`**, which
  had already recorded the compiler's move to `8c69ee4` and the changed binary:
  - **`build/npkc` cannot have been built from `HEAD`, which is stronger than
    "provenance unknown".** It was written 2026-09-04 19:42:54; `HEAD` was
    committed 2026-09-05 11:54:03, sixteen hours later. The question to put to
    the compiler session changes shape accordingly — not *is this stable to
    pin*, but *what commit is this, and is there a stable point at all*
  - **`npkrt.o` is byte-identical to the pin's**, both 55 576 B and both sha256
    `c9ddbcff…2239e`, measured 2026-09-05. Recorded **with its timestamp**,
    because the standing instruction to take it again and check it is unweakened
    and this is the half someone would now be tempted to skip
  - **`ps -o etime` is `[[DD-]hh:]mm:ss`, so the harness reading `16:41` was 16
    minutes old, not 16 hours.** Both sessions misread it the same way at first.
    The consequence inverts: the compiler tree is unsafe to pin from for hours
    yet, rather than a run being nearly finished. **A unit misread makes a
    number wrong by a factor of sixty while it still looks like a measurement**
- **the re-pin checklist now exists**, eight items on `BOARD.md`, assembled
  because the re-pin had been carried as a one-line instruction across three
  sessions and no session had ever written down what it owed
- **AND WRITING ITEM 8 CAUGHT A NINTH INSTANCE OF §6's SHAPE, THIS TIME IN THIS
  ECOSYSTEM'S OWN REFERENCE CHECKER.** The item said "run `check_refs.py` across
  all six repositories". Asked for its **denominator** rather than its verdict —
  the discipline the outgoing session named as the finding it would most hate to
  see missed — `check_refs.py .` from the workbench root prints
  `nitpick-libs  clean` / **`All clean`** having examined **one** repository.
  It takes a single directory. So the sweep an orchestrator believes it ran
  covers a denominator of one, and the word "All" is doing work the mechanism
  does not support. The checklist item now says to name each repository. **The
  check was run before this commit and is honest for it** — only root files
  changed — but it would have been silently insufficient the moment the D-239
  comment corrections landed in two library trees, which is precisely when item
  8 is meant to fire
- **claims checked rather than assumed**, which is what §4 asks after a session
  restart: `nitpick-regex` at `91657eb` and `nitpick-time` at `1c43872`, both
  trees clean, both level with `origin/main`, both matching the commits the
  board names. `CLAIMED` is *ownership* and persists across a session gap by
  design (W-7); what makes a claim stale for dispatch is an in-flight row with
  no live agent, and both rows already read their next subcycle as `PLANNED`
  and not dispatched. So recovery resolves to "dispatch the next subcycle" with
  nothing to recover
- **width put to the author as question 4**, recommending **1** for the next
  session and a return to 2 when quota recovers — the dial turned down, not a
  change of plan. Workers stay on `claude-opus-5`; verifiers stay on the small
  model
- **the lock was taken and released inside this single commit**, marker written
  and removed, `Workbench writer:` reading `none` before and after — the same
  pattern the third orchestrator used twice on 2026-09-04, and recorded here for
  the same reason: the net state hides the event
- **written through `Edit` rather than a heredoc, deliberately.** This harness's
  standing instruction prefers heredocs and `sed`; board question 3 records that
  the write guard cannot judge an interpreter heredoc. Choosing the judged form
  for a board edit costs nothing and is the only way the guard sees the write at
  all. It is not a fix — the fix is the author's call — but a session need not
  route its own writes through the unwatched path while waiting for one

### The `devteam` import — four mechanisms landed, and one worst-class defect found doing it — 2026-09-05

The author asked for a **second, independent pass** over the `devteam`
experiment that the third orchestrator had already read — *"two heads are
generally better than one"* — and for anything worth bringing over to be
listed. Eleven items; four ported at his direction. The list is
`meta/audits/devteam-import-2026-09-05.md`.

- **THE ITEM THAT PAID FOR THE WHOLE READ, and it was found by porting a
  discipline rather than by looking for a bug.** Adding false-positive controls
  to `check_refs` immediately failed two of them. **`check_refs` read an
  identifier inside a fenced block, and inside its own quoted output, as a
  citation**, reporting `cited-undefined` against a file that had merely pasted
  evidence. This workbench **requires** verbatim check output in a committed
  REPORT block, so the check fired on the behaviour the protocol mandates.
  `devteam` names that the worst category and the reason is not cost: **it puts
  the correct response and the safe response in opposite directions**, and the
  lesson it teaches is to paraphrase the evidence next time. Fixed by
  `prose()`, which strips fences before the citation scans and deliberately
  **not** before the leak scan — a home directory pasted inside a fence is
  still leaked, and quoting is exactly how one gets there
- **the fix stops where the rule stops.** Verbatim output quoted *inline* is
  still miscounted, and stripping inline spans would break genuine citations —
  `` `RX-126` `` in backticks is how this workbench writes them, and a new
  control asserts that form still counts. So the gap is **stated rather than
  closed**: the rule it implies is that verbatim output belongs in a fence, and
  a check that guessed which backticks were quotations would be inventing an
  agreement nothing requires
- **the guard's known heredoc limit now lives in its REFUSAL MESSAGE**, not
  only its docstring. `devteam`'s most reliable design lesson is that
  **guidance goes where the temptation is, not where the documentation is** — a
  docstring is read by whoever edits the file, a refusal by whoever just met
  it — and it has measured evidence: a verifier that had never seen the finding
  met such a message and reported it did not use the workaround *because the
  message named it*. Ours also says the part `devteam` need not: it has
  `check_scope` as a backstop and **we have none**, so the refusal is the only
  mechanism watching
- **`git worktree list` is no longer refused as a write.** Judged on the token
  *after* the subcommand, with bare-form reads named explicitly because bare
  `git stash` **creates** one and the bare form therefore cannot be inferred.
  **Why it survived 73 passing controls: no case covered it** — and that is the
  general lesson rather than the specific bug. A check whose controls are all
  planted faults can only ever get stricter, because nothing ever fails when it
  over-refuses. Thirteen new controls, each read form with its write twin,
  verified against the real compiler path and not only the fixture
- **`tools/run_controls.py`**, and the detail worth copying is its failure
  mode: *"no controls found — that is itself a finding"*. The controls had been
  four files invoked from a remembered list, and **a list held in someone's
  head has no failure mode anyone can see**
- **every control now reports its denominator and false-positive share** —
  `111 cases, 50 of them false-positive controls (45%)`, where before it was
  `All 7 cases correct`
- **AN INSTANCE OF §6 COMMITTED WHILE WRITING THIS UP, AND CAUGHT ONE STEP
  LATER.** This session asserted that the workbench's `check_refs.py` had no
  controls — while measuring `devteam`'s side properly by running its suite.
  `test_check_refs.py` had existed all along. It is exactly `devteam`'s finding
  that **a sentence written to justify a measurement does not itself get
  measured**: the measurement licenses the paragraph, and the paragraph then
  acquires claims the measurement never covered. The tell was that the claim
  was one command away and no command was run
- **seven items left open**, ordered in the list file. The two most valuable
  are structural: audit every check against *name the rule whose two sides it
  compares* (if you cannot name one, the check is proposing a rule rather than
  enforcing one), and sweep for **pairs of rules that cannot both be
  satisfied** — of which this workbench has at least one live, the harness's
  standing preference for heredocs against a guard that can only judge
  `Write`/`Edit`. Framing that as a rule *pair* rather than as a guard
  limitation changes what a fix has to do
- **and one bias to expect, from `devteam`'s own report:** everything found so
  far has made that pipeline stricter and **nothing has made it simpler**; both
  simplifications in its history came from people who declined to use it, and
  its `unnecessary` reporting category has never once been used. Every item on
  our list makes this workbench stricter too. None makes it smaller

### The fifth orchestrator takes the lock; the re-pin is answered, and every cross-repository sweep is found blind — 2026-09-05

**Handover.** `nitpick-libs-c6` (`60371281-2e64-47e7-b208-6a273b2eaff7`) takes
the workbench writer lock at 13:37 from `nitpick-libs-42`, the fourth
orchestrator, on a briefed overlap the author arranged. Board line first, then
the marker (37 bytes, cross-checked against the transcript path, because
`CLAUDE_SESSION_ID` is empty in a Bash call). Freedom verified **two ways** —
the writer line read `none` *and* `.internal/` held only `toolchain/` — because
the guard permits any session while that line reads `none`, so its silence is
not evidence.

**`stale claim`, W-19.** After a session restart every claim is formally stale,
because `ListAgents` shows only the current session's agents. Both `CLAIMED`
rows were checked rather than assumed: `nitpick-time` (s2) and `nitpick-regex`
(s1) each name their next subcycle as PLANNED with **no live agent**, so §4's
table resolves to *"the worker never started: re-dispatch"* with nothing to
recover. Both trees verified **clean and level with `origin/main`** at exactly
the commits the handover named — `nitpick-time` `1c43872`, `nitpick-regex`
`91657eb` — and so were `nitpick-tui` (`e5439ee`), `nitpick-parse` (`3cad08c`),
`nitpick-sockets` (`d385991`) and `../nitpick-apps/nitpick-posix` (`948d9b6`).
The claims stay: `CLAIMED` is **ownership** under W-7 and survives a session
gap by design.

**Asking the outgoing session whether it was done paid for itself in one
message.** The lock read free and the brief said it was free; the incoming
session asked anyway. The outgoing one nearly answered from memory, ran `git
status` instead, and found an **uncommitted deletion it had not made** — the
author had moved a tracked file out from under it. Committing on the "lock is
free" reading would have swept another session's deletion into this session's
commit. **The lock's failure mode is not two writers fighting; it is one writer
inheriting another's dirty tree.** Chasing that also turned up a live crash in
`check_refs.py` on an unstaged deletion — `git ls-files` reads the index, so
the file is listed while `open()` raises — which is *precisely* the pre-`git
add` state the workbench's own rule mandates. Fixed in `7da5c2d` as a
`tracked-file-missing` finding. And the gate that should have caught it read
`check_refs … | tail -2; G=$?`, which is **`tail`'s** status: the gate passed
vacuously.

**The re-pin: answered, and the answer is to wait.** One message to `nitpick-bc`
settled what two sessions could not resolve by inspection. `build/npkc` is an
`npkg` build/parity run from the **main checkout at 19:42 on 2026-09-04**, when
`main` was at `99bbccd` and the working tree carried 1.5.2 step 0's uncommitted
changes (committed at 19:53 as `593c554`). **It is a build of no commit that has
ever been on `main`** — so there was no commit to name it by, and inspection
could never have resolved it. This session's independent measurement placed the
19:42:54 mtime between those two commits before the reply arrived, and the reply
confirmed it exactly. The pin point is the **1.5.2c close**, ~15:30, and that
session sends the identity.

**The pin procedure would have mislabelled it, and that is a defect in §3.**
Run today, §3 yields `COMMIT=8c69ee4` and `TREE=clean` — the tree *is* clean —
and its mid-rebuild guard passes trivially on a seventeen-hour-old binary. It
would have written `compiler 8c69ee4 / tree clean` into `PIN.md`: a confident,
false provenance. **`tree clean` describes the SOURCE tree and says nothing
about what `build/` was built from**, and §3 asks for a `binary` line only in
the `tree dirty` branch — the branch this case does not take. §6's shape, found
in our own pin procedure. The fix is one command: compare `build/npkc`'s mtime
against `HEAD`'s commit date and treat *older* as `tree unknown`.

**THE SESSION'S LARGEST FINDING: a cross-repository sweep run from the
workbench root sees none of the five libraries, and reports that as silence.**
Two independent causes, one result. `grep` here is **`ugrep` 7.8.4 installed at
`/usr/bin/grep`** — `grep --version` says so, `which grep` does not — and it
honours ignore files in recursive mode; the root `.gitignore` opens with
**`/*/`**, ignoring every top-level directory, which is exactly how this
repository avoids embedding a library as a gitlink. Separately, **`git grep`
from the root cannot see a library either**, because each is a separate
checkout and none of its files are in this index. Measured on one pattern:
`grep -r --include='*.npk'` from the root → **0**; `git grep` → **0**; the same
grep pointed at `nitpick-time` → 7; `--no-ignore-files` → **14**;
`find … -print0 | xargs -0 grep` → **14**. The two tools that see everything
were diffed against each other and agree, so 14 is a measurement rather than
one tool's opinion.

**Why it is the worst instance of §6's shape yet found here.** `check_refs .`
at least prints the name `nitpick-libs`, so its denominator of one is visible.
**A sweep that matches nothing prints nothing.** There is no verdict to doubt
and no count to interrogate: "swept, no violations" and "swept nothing" are
byte-identical. Both of this workbench's stated disciplines — *a list of files
is produced by `git grep`, never by recall*, and *ask for the denominator, not
the verdict* — route straight through the one failure that yields no number.
**And the same `.gitignore` line has bitten this project before:** its own
comment records that a directory must be un-ignored by name *"or it vanishes
silently — which is exactly what happened on the first attempt to add the
plugin."* The note was about tracking; nobody carried it across to searching.

**What it invalidated.** Checklist item 6's site list, demonstrably: the stale
citations to the deleted `src/frontend/list.npk` are **six sites in three
files**, not five in two. The old sweep matched the token `List` while the
property is *"cites the deleted `list.npk`"* — so it caught
`probe06_generic_vec.npk:107` by accident (that line says `list_init`, not
`List`), **missed every basename citation**, and never saw
`nitpick-regex/tests/probe/probe04_inherent_generic_impl.npk` at all, which
holds two. It also counted `:49` and `:60`, which cite no deleted path and are
not findings — the board itself calls `:60` "exactly right". **One board
paragraph simultaneously counts the `list_init` line among its `List`
occurrences and asserts that nothing here declares a `list_init`.** Two halves
of one paragraph, contradicting each other, neither re-derived.

**What it did not invalidate, checked rather than assumed.** D-239's
substantive conclusion holds — no `struct:List`, `mod:list`, `list_push` or
`list_reserve` anywhere, so no rename is required. D-248's *"swept all six
repositories: zero violations"* re-verified: **0 violations over a stated
denominator of 87 `.npk` files**, a denominator the original claim never gave.
`check_refs.py` run naming each target: **clean over seven** — the root, the
five library checkouts and `../nitpick-apps/nitpick-posix`. Controls green:
`112 cases, 50 false-positive (44%)`.

**The compiler session's steers, folded into checklist item 4** so the
re-measurement is executable without re-reading this entry. **O-N11 is now a
compile-time refusal, not a runtime verdict** — `NITPICK-REACH-003` at `main`
whatever the exit code — so a verdict phrased as an exit code measures the
wrong thing. **O-N10's shape moved with D-258**: a derived body reaches every
member through the trait it derives, refused at the **call** as `TYPE-017`
naming the derive, the parameter and the bound, never at the declaration; a
`string` payload is `DERIVE-006` at the derive while a `string` field derives
fine. A path containing `<derived-` in any output is a compiler defect that
session has asked us to report.

**No worker dispatched, and the reason is specific rather than caution.** Width
is **1**, confirmed by the author today. `nitpick-time` 0.0.1's gate is
satisfied — 0.0.0 is `DONE` and the probes it names (01, 04, 06) have recorded
verdicts — but **step 4 of that subcycle pins the compiler by commit in CI
(P-10)**. Dispatching before the pin lands would write the stale `94874ce` into
a new CI workflow and guarantee an immediate bump commit, while steps 2 and 5
would accept against a compiler about to be discarded. That is the previous
session's own argument — a measurement belongs to a pin — pointed the other
way.

**Every session renamed to a convention, 2026-09-05.** The author renamed all
live sessions to `<project>_s<N>` — the project segment naming the work area,
`N` the handoff generation — *"to help me keep things in order."* This session
is `nitpick-libs_s0`; it appears above and in earlier entries as
`nitpick-libs-c6`, which was its name for the first hour. **Earlier names in
this record are left as written**, because they were correct on their dates and
this file records what happened.

The rename **answered an inherited open question** rather than merely tidying.
The fourth orchestrator recorded an unidentified idle peer, `nitpick-e3`, noted
that its name shape *weakly* suggested compiler-side, and explicitly declined
to rest the writer lock on that inference — *"that is inference, not evidence."*
After the rename the same `ListAgents` ref, `[0dc3d1]`, reads
**`nitpick-compiler_s1`**: the compiler's own waiting successor, working
another repository, which will not write here. The instinct to refuse the guess
was right, and the convention is what converted it into a fact.

**What the convention changes for a later session.** Earlier boards and briefs
carried *"names are not durable; `ListAgents` is the address book."* That was
true of machine-assigned labels and is now half true: **the project segment and
the generation number are stable and worth reading**, while `ListAgents`
remains the authority on who is alive and the `[ref]` is what disambiguates.
Recorded in `BOARD.md`'s peer roster and in orchestrate §2.1, where the "is
another session live?" check is made.

**And an idle peer is parked on purpose.** The `claud-skills-devTeam_s0`/`_s1`
pair is held idle deliberately, in the author's words *"to conserve on tokens so
we don't run short on the main project (compiler) or this one."* Waking one has
a cost he is actively managing, so idleness there is a decision rather than a
stall.

**pin 0dfddac, tree clean — 2026-09-05 15:58.** The 1.5.2c close, landed and
pushed by `nitpick-compiler_s0` at 15:47 with `build/` rebuilt from the pushed
main checkout 15:52–15:56. **The provenance branch added to orchestrate §3 this
afternoon was exercised on both sides in one day:** it refused the 19:42 binary
as `tree unknown` (mtime seventeen hours *before* `HEAD`) and passed this one as
`tree clean` (mtime 15:56:34, nine minutes *after* `HEAD`'s 15:47:09). A check
that has fired and stayed silent, each on a real case, is commissioned rather
than merely written. Every number in the landing notice was verified here before
copying rather than taken on report: 7 304 552 B, sha256 `38e48973…`,
`sha256sum -c` OK, LLVM 20.1.2, tree clean, level with `origin/main`, and
`94874ce` an ancestor of `0dfddac` so the pin moves forward. `npkrt.o` byte-
identical to the previous pin's, **taken again and checked** — DEF-12 is the
precedent for what assuming that costs. The pinned compiler was then
commissioned positive and negative before any measurement was believed: a real
tree file exits 0 with an 845 282 B `.ll` written, a malformed file exits 1 with
none. The negative control was incidentally refused at `NITPICK-RESOLVE-012`
for a `mod:`/basename mismatch rather than for its syntax, which is **O-N8's
fix (the compiler's DEF-2) observed live** — the defect this workbench raised on
2026-09-03, where a mismatch silently merged two files at exit 0.

### The pin moves to 0dfddac, and the four stops are re-measured — 2026-09-05

**The pin.** `0dfddac`, the 1.5.2c close, taken 15:58 after
`nitpick-compiler_s0`'s landing notice at 15:47 and its ladder run 15:52–15:56.
Recorded above as its own `pin` line. The mid-rebuild guard did its job on the
first attempt — the binary was 96 seconds old and the guard said retry, which is
the one thing that guard is for.

**All four re-measurements, the reason the pin waited.** **O-N11 is FIXED**:
`npkc` now exits 1 with `NITPICK-REACH-003` and no `.ll`, where it previously
exited 0 and left `llc` to refuse an undefined `@npk_failsafe`. **The
diagnostic names four identities — `Unreachable`, `HeapOom`, `HeapBadRequest`,
`WildLeak` — confirming this board's correction against the six the compiler
session had told us**, out of the compiler's own mouth rather than by argument.
**O-N10 is UNCHANGED**: all three `derive_payload_enum` cases run identically on
both pins through the full four-step recipe and match their headers (0, 121,
107), so 1.5.2b's wholesale derive rewrite did not move it — which is exactly
what could not be assumed. **O-N9 unchanged**: `BORROW-012` and `BORROW-001`
identical on both pins. **O-N4 still discharged but slower**: 2.03–2.06 s at
~119 MB against 1.18 s at 74 624 KiB, still ~136× better than the original 281 s.

**A FIXED PER-PROGRAM COST, MEASURED DIFFERENTIALLY BECAUSE BOTH COMPILERS ARE
ON DISK.** Comparing a remembered number against a fresh one would have
confounded compiler version with everything else; running both pinned binaries
on the same inputs does not. A 14-line program that only exits 0 went from
**0.10 s / 21 456 KiB / 456 517 B** to **0.85 s / 102 404 KiB / 845 282 B** —
8.5× the time, 4.8× the peak. **The `.ll` delta is exactly 388 765 bytes for
both that program and the 30 000-row one, identical to the byte**, which is what
turns "the compiler got slower" into "the prelude got bigger": a constant
independent of the input cannot be a compile-time regression. Widened to 30
programs across two libraries, **22 sit at exactly 388 765** and all 8 exceptions
are derive or enum programs where semantics genuinely changed. Raised to the
compiler session the same afternoon under the lifted constraint, with the W-27
statement and no ask beyond confirming the price was known.

**A METHOD ERROR I MADE AND CAUGHT ONE STEP LATER, which is the reason the
numbers above are trustworthy.** The first extent sweep captured exit status as
`${PIPESTATUS[0]}` after `t=$(cmd | tail -1)`. **That is not the compiler's
status** — the pipeline ran inside a command substitution, so the value read
back was `tail`'s, and every program reported `exit=0`. It was the exact trap
the outgoing orchestrator had warned about, committed within the hour, by the
session that had written the warning onto the board. The tell was two *refusal*
probes reporting `exit=0` with no `.ll` written — **a status that disagreed with
an artefact**. Re-run with `/usr/bin/time -o` and no pipeline, both refuse
correctly at exit 1. Nothing above rests on the broken capture.

**AND A FALSE FINDING I ALMOST REPORTED.** `probe09b_environ_view_returned`
exits **10** against a header saying `expect-exit: 0`, on both pins. That reads
as a defect and is not one: exit 10 is its own `string_byte_length(hit) != 14`
and the probe requires **`TZ=Europe/Kiev`** exported. With it, exit 0 on both
pins. **The precondition is written nowhere** — 0 occurrences in the probe, 0 in
`0.0.0.md`, and `tests/probe/` has no `README.md`. **The danger is the code it
chose**: a substantive failure code from its own map, indistinguishable from a
real verdict about the language. Extent established rather than patched where
found: three program-stage probes read outside state; `probe08_readlink` exits 0
bare and is fine; **`probe09_environ_split` is the model** — it states
*"PRECONDITION: run with `TZ=Europe/Kyiv` exported"* **and exits a dedicated
`30`, so an unmet precondition announces itself as one.** Same author, same
afternoon, neighbouring files: one precondition self-describing, one silent.
Given to stream 2 for `nitpick-time` 0.0.1. It blocks nothing now and will
produce a false failure the first time 0.0.2's `program` stage runs it.

**S-38 opened on the compiler side within twenty minutes of the raise —
2026-09-05 16:08.** The prelude-cost measurement went to
`nitpick-compiler_s0` under the just-lifted constraint and came back as their
`OPEN_DECISIONS` **S-38** (`a882188`, verified here docs-only: one file, one
insertion, no `src/` or `runtime/`, our pin unaffected and `sha256sum -c` still
passing). **They explicitly declined to close it as the price of D-257 and
asked us to carry it as open**, which is the right call and not the one we
would have been entitled to make for them. They confirmed the mechanism —
D-257's generated scalar impls are 348 rows in thirteen families — and supplied
the half we could not see: 1.5.2b had already measured *"every prelude impl body
is emitted whether reached or not"* at **+2.2% IR and +14% frontend time on the
compiler's own tree**. **The number nobody had is the fixed per-program cost,
and the reason we found it is structural rather than clever: their harness
compiles a fixed set once per run, ours compiles many small programs, so a
per-program constant is invisible from their side and dominant from ours.**
A measurement's visibility depends on the shape of the thing doing the
measuring.

Their recommendation to the author is reachability-driven emission of
non-generic prelude bodies through the demand walk the emitter already runs for
generic instances — semantics-neutral, and *"worth doing before 1.5.3 hangs
contract obligations on every prelude function"* — with the caveat that the
frontend's share should be measured first, because parsing and typing the
prelude is paid per compile whatever is emitted.

**We stop measuring it per program at their request**, keeping one canary:
`probe11d_floor_only.npk`'s `.ll` at **845 282 B**. Two data points and the
constancy argument are what the decision needs; further sampling is cost without
information.

**The constraint's lifting is now evidenced twice in two days, both pointing the
same way.** O-N16 was catalogued rather than raised and was closed upstream the
same day regardless; S-38 was raised and became a decision item with a
recommendation inside twenty minutes. Neither cost the compiler session anything
it minded, and the second produced work the author now gets to schedule.

### Released at a clean stop for handoff to `nitpick-libs_s1` — 2026-09-05 16:2x

**Released rather than dispatched, by the author's decision.** The re-pin was
done and all four stops re-measured, so `nitpick-time` 0.0.1 was genuinely
dispatchable at width 1 — its gate is satisfied, and the one reason to hold it
(step 4 pins the compiler by commit in CI, and the pin was stale) had just been
removed. It was put to the author with the two facts that made it his call
rather than the orchestrator's: **a subagent dies with the session that spawned
it**, so a worker dispatched into a session about to hand off loses its output;
and quota is a constraint he is actively managing, having parked the
`claud-skills-devTeam` pair for exactly that reason. He chose the clean handoff.
**No worker was dispatched and no claim moved.**

**State at release.** Pin `0dfddac`, `sha256sum -c` passing, `PIN.md` carrying a
full `binary` line. Every repository committed, pushed and level with
`origin/main`; the workbench likewise. Both `CLAIMED` rows stand — W-7 ownership
survives a session gap — with their next subcycles PLANNED and no live agent, so
§4 recovery resolves to "dispatch the next subcycle" with nothing to recover.
Marker removed first, then the writer line set to `none`.

**What `nitpick-libs_s1` inherits as its first item.** `nitpick-time` 0.0.1,
carrying four things that accrued to that repository today and belong to its
stream under W-7: the two DEF-5 transcripts re-recorded against the measured
after-value (`NITPICK-REACH-003`, **four** identities); checklist item 6's three
stale `list.npk` citations in `probe06_generic_vec.npk` (lines 14, 92, 107);
`probe09b`'s undocumented `TZ=Europe/Kiev` precondition, on
`probe09_environ_split`'s self-announcing pattern; and the board's existing
0.0.1 residue — `expect-` headers for the three `missing_failsafe` cases and a
sweep that asserts its denominator. Checklist items 7 and 8 remain; item 6's
other three sites are `nitpick-regex`'s and wait for stream 1's claim.

**One decision sits with the author and is not ours: S-38.** The compiler
session has reported it to him directly as well.

**What this session would tell its successor if it could only say one thing.**
Every finding today came from the same move: **running the command instead of
writing the sentence.** The sweep blindness, the six-not-five citations, the §3
mislabelling, the prelude constant, the `probe09b` precondition, and the one
method error — `${PIPESTATUS[0]}` after a command substitution reading `tail`'s
status — were each one command away, and the ones that were caught were caught
because somebody ran it. **The tell, every time, was a claim standing where no
command had been.**

### The sixth orchestrator takes the lock; `nitpick-time` 0.0.1 closes, and a count is wrong for the fourth time — 2026-09-05

**Handover.** `nitpick-libs_s1` (`00e68bc1-dc6d-4607-b8eb-72f7188a59c1`) takes
the writer lock at 16:4x from `nitpick-libs_s0` on a briefed overlap. Freedom
verified **three** ways rather than the usual two — the line read `none`,
`.internal/` held only `toolchain/`, and the release commit `b992544` was on
`main` with all seven trees clean and level. The outgoing session was asked
directly and **answered from `git status` rather than memory**, and volunteered
what no tree read can show: that its remaining actions were messages only.

**A fourth lock hazard, and it was answered by one message.** `ListAgents`
showed a **`nitpick-libs_s2`, idle, opened within a minute of this session**,
which no brief, record or roster mentioned. Orchestrate §2.1 says to stop and
ask the author; **asking the peer itself was faster and more certain** — it
replied *idle, no task, nothing written, and I will message you before I
write*. That is the move the fourth orchestrator recommended for the
unidentified `nitpick-e3` and did not take, leaving it open two days. The
author confirmed the practice: a **rolling pool**, the next generation
pre-opened and a spent session closed to return as the generation after next
(`s0` closes here and comes back as `s3`). **A higher-numbered libs peer is
normally your own parked successor — ask it anyway.**

**And the lock was taken locally and left invisible on `origin`.** The commit
landed; the push did not. `origin/main`'s writer line still read `none` until
`nitpick-libs_s0` noticed and said so. **The check ran on the wrong side of the
write**: `git status` was verified before committing and not after, and the
session that had just verified "all seven trees committed **and pushed**" as an
inherited state failed to hold its own commit to it.

**`check_refs` AND `gather_claims` BOTH REPORTED OVER A DENOMINATOR THEY NEVER
STATED, AND THE SECOND WAS WORSE.** Both enumerate markdown with `git ls-files`
and fall back to a recursive `rglob` when git is unavailable. From the
workbench root those are **34 files and 334** — the root's own, plus 297 in
five separate checkouts, plus 3 under a gitignored `.internal/`. Measured, not
inferred: with git absent from `PATH`, `check_refs .` reports **exit 1, "57
finding(s)"** against a true answer of clean-over-34, **under the same
repository label**, so all 57 read as this repository's fault when each belongs
to a repository W-7 forbids the session to touch. `gather_claims` gathers
**1449 claims instead of 274**, and its guard was a bare `except Exception`,
swallowing *any* error into the wider path.

**Where it was hiding is the durable part.** `check_refs`'s own docstring warns
that *"quietly narrowing the file set is how a check comes to report 'All
clean' over a denominator it never states"* — **three lines above a fallback
that quietly WIDENED it.** Awareness is not immunity, in the tool this
workbench gates every commit on. Both now print `N files via <how>` on every
line, clean or not. **Two control cases added and commissioned: green with the
fix, red with it reverted, restored byte-identical.** The existing `CASES`
table checked *which faults are found*; nothing checked *what was examined*,
which is exactly why this survived. Controls 112 → 114.

**CI MAY PIN THE COMPILER BY COMMIT, AND IT IS NOW A MEASUREMENT.** Our pin is
a **binary**; CI **builds** one, so P-10 holds only if the build reproduces.
`nitpick-compiler_s0` rebuilt `0dfddac` in a fresh detached worktree with
nothing uncommitted and reproduced **both** artefacts byte for byte — checked
here against `.internal/toolchain/0dfddac/` rather than read off the message.
**Two conditions are load-bearing and are written into the workflow:** LLVM
**20.1.2 exactly**, patch release included, *because a patch release can change
instruction selection*, and **the ladder invoked from the tree root**. The
reason is recorded with the condition, because a condition whose reason is lost
gets relaxed by the next person who finds it inconvenient.

**S-38 IS RATIFIED, AND OUR ATTRIBUTION WAS WRONG.** The author ratified the
compiler session's recommendation and it is in flight as their 1.5.2d (D-262,
verified here as docs-only and unpushed, so `0dfddac` stays the pin). Their
option (2) — *measure the frontend's share before believing the obvious cause*
— was carried out first **and changed the answer. The cost is not the prelude's
size:** the frontend holds **0.72 s of the 0.82 s**, and three scaling defects
account for it, chiefly a bindings analysis allocating one state slot **per
statement of the whole program, for every function** (57%). **We measured the
cost soundly and inferred its cause wrongly, and nothing on the board had
marked that inference as one.** The canary is now *expected* to move at their
step 2; a later session must read that as the landing, not a regression.

**`nitpick-time` 0.0.1 — DISPATCHED, DONE, VERIFIED PASS** at `0c7e156`,
committed and deliberately not pushed. It carried six items, five accrued after
0.0.1 was planned. **Its lasting value is four corrections it made to what it
was told**, three of them to this board:

- **`case3` names SIX identities and `case1` four.** This board said *"the
  diagnostic says four — this board's correction against the six we were told
  is confirmed by the compiler's own output"*, taking one program's floor as
  the general answer and citing the compiler's own mouth for it. **The board
  contained its own refutation**: it records that `case1` has *"no import, no
  arithmetic and no allocation, so its bill is S-4b's floor of four"* — which
  is precisely why four is not `case3`'s number. Re-measured by the
  orchestrator directly before the board moved. **A count a diagnostic computes
  FROM THE PROGRAM cannot be corrected once for the set.**
- **`TZ=Europe/KIEV` exits 34, not 0.** A claim relayed into the dispatch,
  labelled unverified, and measured rather than inherited — which is the only
  reason it did not become a fifth false entry. The spelling that does
  demonstrate the weak assertion is mixed-case `Europe/Kiev`.
- **`tests/probe/` HAS a `README.md`** — 12 KB, with the probe table. Board and
  record both said it had none.
- **TM-114, probably shared:** `BUILD.md` §3 was missing the compiler's default
  `compile` stage and assigned `tests/conformance/` to `accept` — *accepted in
  silence*, the shape O-N11 walks through. **The template was shared**, so each
  sibling checks its own §3 at its next claim.

**THE `list.npk` COUNT HAS NOW BEEN WRONG FOUR TIMES, AND THE REASON IS THAT
NOBODY WAS COUNTING THE RIGHT KIND OF THING.** Five, then six, then seven, then
ten — the last from the verifier, which swept the string and found ten,
including the very records that document the fix. **Every one of those counts
measured a STRING; the property is SEMANTIC** — *"cites the deleted file as
though it still exists"* — and no `grep` decides that, because the same string
appears in a stale citation, in an accurate historical note, and in the proof
that the file is gone. Settled by reading: **zero stale citations remain.** The
four surviving mentions in `probe06_generic_vec.npk` are *"it **was**
`src/frontend/list.npk`"*, *"now prelude functions **rather than**
`list.npk`'s"*, and two naming the new prelude location; lines 49 and 60 were
correctly left untouched. **This workbench's standing rule is "a list of files
is produced by `git grep`, never by recall". This is the counter-case: `git
grep` is not the answer either when the predicate is not lexical**, and four
sessions in a row reached for it because the rule does not say when it stops
applying.

**The worker's own instrument was better than the ones it was given.** It
proved the deleted file gone **at the pin** — `git cat-file -e
0dfddac:src/frontend/list.npk` → exit 128 — rather than in the compiler's
working tree, which by then sat two commits ahead at `daa5057`. That became a
playbook rule the same hour, alongside the restatement of the pipeline trap as
*no pipeline at all when a status is being recorded* — the worker hit that one
twice, once **inside a transcript generator**, where `ls <missing> | sed` wrote
`exit=0` into a file whose entire purpose is verbatim evidence.

**And the playbook paragraph recommending that rule was itself wrong on first
writing** — it said the compiler tree was "four commits" ahead, from memory. It
is two. It was corrected by running the command the paragraph exists to
recommend, and the correction is left in the text.

### `nitpick-time` 0.0.2 — the harness, and a self-checking number that two agents did not check — 2026-09-05

**0.0.2 DONE — VERIFIED PASS** at `e101312`. The harness is green: 27 units, 0
failures, ~63 s. The verifier **rebuilt and re-ran all three negative controls**
rather than accepting them — the symbol scan red on an introduced undefined
symbol, the toolchain pin red on 20.1.3 against 20.1.2, and `repro` red on an
unsorted generator with a sorted control green *through the same code path*,
which is the part that makes it a control rather than a second test.

**P-16 WAS UNEXECUTABLE, AND THE COMPILER WAS RIGHT ALL ALONG.** The plan's
decision to *"compile the library once to an object and link each test program
against it"* cannot work: two `npkc`-produced objects are a duplicate-symbol
error — `ld.lld` exit 1, 121 lines, `npk.prelude.int8:ToString.to_string`
defined twice — because every compile emits the whole reachable graph
**including the prelude**. `tests/conformance/import.npk`, which computes
nothing, emits **845 282 B**: the canary number exactly. **Confirmed here before
anything was concluded from it.**

**And then the reframing, which is the actual lesson.** Read at the pin,
`BUILD_REFERENCE` §4.1 says *"The link line `npkg` builds takes **one program
object** and adds the runtime object; there is no parameter through which a
third input could enter."* **The compiler behaves exactly as documented; our
plan assumed a model it never offered.** The first framing — *"`npkc` has no
separate-compilation mode"* — is true and points at the compiler. The second is
also true and points at us, and only the second is actionable. **A finding that
blames the tool is worth re-reading against the tool's own documentation before
it is raised**, and this one was, which is why what went upstream was the
allowlist finding and an explicit note that separate compilation was *our*
error. P-16 is the natural decision to write, so **the other four libraries'
harness plans probably carry it (TM-117).**

**THE ALLOWLIST IS WRONG IN BOTH DIRECTIONS, AND THE ARITHMETIC PROVES ITSELF.**
`npkg/elf.npk`'s `runtime_allowlist`, read at the pin: on meeting `internal` it
**advances past the keyword and takes the name anyway**, so the allowlist is all
166 `define` names plus `main`. Measured against `runtime/npkrt.ll` at `0dfddac`
and our pinned `npkrt.o`: **166 defines = 57 `internal` + 109 exported**, and
the object exports **111** globals — the 2-symbol gap being exactly the `module
asm` block's `.globl _start` and `.globl npk_clone_raw`. **109 + 2 = 111.** So
the allowlist is **too permissive by 57** (names the object never exports: a
program referencing one passes the scan and fails at `ld.lld`, turning D-206's
named refusal into a link error) and **too narrow by 2** (`npk_clone_raw` is an
intended export no `define` scan can see, so a legal program is falsely
refused — the direction that gets guards disabled). Raised, with impact stated
and no ask beyond whether it was known.

**A NUMBER THAT CHECKED ITSELF PASSED THROUGH TWO AGENTS UNCHECKED.** The worker
reported **56** internal defines; the verifier repeated **56**; the true count
is **57**, confirmed two independent ways — `grep -c '^define internal'` and a
unique-name extraction, both 57. **The number was falsifiable from the other
numbers in the same sentence:** only 57 makes `109 + 2 = 111` come out, and 56
would have required the object to export 112. **Neither agent ran the check
their own figures contained**, and the verifier's phrasing tracked the worker's
closely enough that it plainly carried the number forward rather than
re-deriving it. Everything the verifier actually *tested* it re-ran; this was
the one thing it *reported*. **The distinction is the finding: a verifier
re-runs commands and repeats prose, and a number embedded in prose travels with
the prose.** The orchestrator caught it only because the same figure had been
sent upstream and was worth re-checking for that reason — not by any mechanism.
**Where a report's numbers stand in a fixed relation, state the relation**, so
that carrying one forward without the others is visibly wrong.

**Two board staleness findings, both in the direction nothing here checks.** The
0.0.2 worker checked its inherited NOTES against the files instead of working
from them, and found **RX-111 and two leak-gate sites already discharged** in
`nitpick-time` while the board still listed them as owed. Verifying that turned
up the larger one: **the board cited `specs/SAFETY.md` in all five stream rows,
and the file is `meta/specs/SAFETY.md` in every library** — eight occurrences
across five lines. **The line numbers were right and the prefix was wrong**,
which is why it survived: a line number reads as a thing to re-check and gets
re-checked; a directory prefix reads as part of the file's name and is copied
forward. **A citation is a path AND a line, and this ecosystem has been
re-deriving lines while copying paths.** RX-111 is genuinely discharged in
`nitpick-time` and `nitpick-regex`; **three remain — `nitpick-tui`,
`nitpick-parse`, `nitpick-sockets` — each checked individually.**

**And the general shape of it: every check in this workbench asks whether a
claimed fix is real. Nothing asks whether a claimed debt is still owed.** That
direction costs a whole dispatch, silently, because re-fixing a fixed thing
looks exactly like work and produces a clean diff.

**Incidental, and it is the denominator lesson arriving inside the instrument
used to measure denominators:** `grep -c` reports **5** for the `SAFETY.md`
paths because it counts *lines*, not *matches*; there are **8**.

### `nitpick-time` 0.0.3 — the self-check lands, and the verifier reasons where it should have run — 2026-09-05

**0.0.3 DONE — VERIFIED PASS** at `60e03bf`. The harness is green — 27 units, 0
failures, 5 pending, ~188 s — and this is the subcycle that earns the earlier
greens: **eight self-check cases, each red on its planted fault and green on a
correct twin in the same run; nine tree checks, not the four planned, each red
on a planted violation against ten clean controls.** Case 7 — *a sweep that
silently does not run* — reports **"swept 3 of the 10 its header declares"** and
**"7 case(s) were NOT visited"**, which is this library's most plausible way to
be green and wrong, now caught by name and by number.

**THE VERIFIER RETURNED PASS, AND TWO OF THE NINE PRESSED POINTS HAD NOT BEEN
TESTED. WHICH TWO IS THE FINDING.**

- **V-15's stopping.** Reported as *"a self-check failure **would** block
  subsequent stages"* — read off the code, where the dispatch had asked in
  terms for a planted failure. **Planted at the orchestrator: `run.py` exit 1,
  only `[1/9] self` in the whole output, stages 2 through 9 never ran**, the
  banner *"Nothing below it was run (V-15)"* present, and `harness/selfcheck.py`
  restored byte-identical with `git status --porcelain` and `git diff --stat
  HEAD` both empty.
- **The arm-bill oracle.** Checked against six `src/` placeholders **which all
  owe the floor of four** — a set that cannot distinguish the claim from its
  negation. **The discriminating specimens were re-run here:** `probe11c`, whose
  `failsafe` is the floor-only one character for character, is refused **4×
  `NITPICK-REACH-002`** naming `DivByZero`, `DivOverflow` and two more, so
  `calc_lib` **adds four → 8**; `probe11b` is refused naming
  `probe11_arms_lib.EProbeZone`, so `arms_lib` **adds one → 5**. Both of the
  worker's bills stand.

**The shape both gaps share is worth more than either gap.** Each was a check
that needed **setup** — planting a fault, or choosing a specimen that could
discriminate — and in each the verifier **substituted reading for running**,
reasoning its way to the correct answer. Everything that was a bare command it
re-ran faithfully. **But reasoning from the code is exactly what the worker
already did**, so on precisely the checks that are hardest to fake, the
verification stopped being independent. **A verifier that reads instead of runs
agrees with the worker for the worker's own reasons.**

**This is the second verifier gap today and both point the same way.** The
first carried a **56** that the other two numbers in its own sentence
falsified; this one carried two conclusions that were correct but underived.
**Neither was a wrong answer — that is what makes the pattern hard to see. A
verifier's errors are not wrong verdicts, they are right verdicts reached the
wrong way**, and nothing downstream can tell those apart. **Fix, applied from
the next dispatch: hand the verifier the LITERAL command for any check that
requires construction, or verify that class at the orchestrator and say so.**

**TM-124 — `accept` was DECLINED, not skipped, and the distinction was checked
rather than accepted.** Acceptance asked for five stages and four were built.
The plan listed `accept`; `BUILD.md` B-4b and `TESTING.md` §1 both say this
library does not use it. **The specifications are the authority (TM-002), so
the plan was the wrong document** — and the decision is implemented as an
**active refusal by name with its reason**, distinguished in the schema check
from *"not yet implemented"*, because *"not yet"* invites a later session to
build it and `accept` stops at **"accepted in silence"** — the exact thing this
repository holds the O-N11 reproduction of. Verified live: a manifest naming
`accept` is refused and told what to use instead.

**And the numbers all sum, because the worker was asked to state the identity
rather than the figure.** 50 = 7 `src/` + 42 `tests/probe` + 1 conformance;
42 = 26 + 3 + 13; parse verdicts 50 = 36 clean + 13 refused later + 1
must-not-parse + 0 failed; **what roots each file, 50 = 1 library root + 27
suite roots + 3 reached by `use` + 19 nothing else** — that last one being the
parse stage's whole marginal value, since nineteen files are reached by no
build and would otherwise be checked by nothing. `check_specs_current`:
226 + 15 new = **241** declared rules, 1 575 citations across 119 files, 0
unresolved. **After this morning's `56`, every count in the report carries the
relation that makes it falsifiable.**

**Cost: 187 s, up from 63.8 s** — 78 s of self-check and 40 s of parse, both
**new checks rather than new overhead on old ones**. All of it is TM-117's
floor: ~130 `npkc` invocations at ~0.8 s each for a library that computes
nothing. **Deliberately not chased**, per the dispatch, because 1.5.2d is in
flight to remove ~94% of exactly that. **When it lands, this repository is the
best place in the ecosystem to measure the improvement**, precisely because its
run is an unusually large number of very small compilations — the same
structural fact that let this workbench see the cost when the compiler's own
harness could not.

**The pipeline trap, fourth occurrence, and this one settles what kind of
problem it is.** The worker hit it in its **first measurement**, in a dispatch
whose text warned against it, in the paragraph it was working from:
`$NPKC --help 2>&1 | head -30; echo $?` reports **0**; redirected with the
status on its own line the same command is **2**, re-confirmed here. Four
sessions, four warnings, four violations, each by someone who had just read the
warning. **A rule violated by the person reading it is not under-stated, it is
mis-formed** — appending `| head` to look at output is an older and faster
habit than any instruction and fires before the rule is recalled. `PLAYBOOK.md`
now points at the mechanism instead: **pair every status with the artefact it
should have produced**, because a pipeline's borrowed `0` is falsified the
moment you ask what it wrote. All four were caught that way and none by recall.

### `nitpick-time` 0.0.4 — the first library code, and a defect whose extent was four rows wider than the orchestrator raised — 2026-09-05

**0.0.4 DONE — VERIFIED PASS** at `06f82c0`. `src/core/` exists: `vec.npk`,
`bytes.npk`, `limits.npk`, **35 public names = 10 + 12 + 13**. Harness green at
**40 units, 0 failures, 5 pending, ~240 s**. This is the first subcycle in this
repository to write library code rather than instrument, and the three tree
checks built at 0.0.3 moved from a denominator of zero to a real one on the day
the files landed — `check_constants_named` at 11 bounds / 2 constants,
`check_raw_index` at **0 raw-index sites in the whole library**.

**IT WAS WORKED TWICE. The first worker died mid-run when the session was
killed at ~20:50, and none of its work was lost** — six modified tracked files,
seven new probes and a complete defect reproduction were sitting uncommitted.
§4's table resolved to `RUNNING` + dirty, so the subcycle was **re-dispatched
with `TREE: dirty` and the successor inherited its predecessor's work** rather
than restarting. That is the recovery path working exactly as written, on the
first occasion anything has needed it.

**THE ORCHESTRATOR RAISED A COMPILER DEFECT AS BLOCKING ONE API ROW. IT BLOCKS
FIVE.** O-N17 — a generic function moving out of an indexed element at an
owning `T` calls a `@npk.vacant.<n>` helper the emitter never defines; `npkc`
exit 0 writes the `.ll`, `llc` exit 1 writes no object. **The primitive is
`move(v.items[i])`**, and `vec_pop`, `vec_set`, `vec_clear`, `vec_truncate` and
`vec_free` are all built on it — **a loop is a different caller, not a
different primitive**, which is what the first reading missed. Measured by the
worker with four owning shapes against four scalar controls from the same
source, confirmed here on `case5_generic_drop_loop`, and re-confirmed by the
verifier across all five cases.

**Understating the extent was the dangerous direction, and it would have failed
silently.** *"One row"* is exactly the reading that would have justified
shipping a generic `vec_clear<T>` that **does not drop its elements** — which
passes the `exit 0` leak gate, because D-151 counts `wild` blocks and cannot
see a managed body. **An extent short by four rows would have been discharged by
a green suite.** Overstating an extent costs a message; understating one ships a
silent bug with a passing test beside it. **A defect's extent is a separate
measurement from its existence, and only the second had been taken before it
went upstream.**

**Correcting it cost one message and cost the compiler nothing.** They had
already fixed it — at the primitive rather than the symptom: `emit_move_out`
built the vacant helper's symbol from the place's recorded type's raw id and
now builds it from **the element type through the specialization**, so **our
five operations are one fix**, verified there against the pop, set and
loop-clear shapes. It is 1.5.2d step 4. **The extent correction changed nothing
about the fix's shape**, which is the argument for correcting extents promptly
rather than carefully.

**And the silence that made the whole class possible closed with it.** The
drop-body emitter now says `EMIT-002` **aloud** when a registered type cannot be
lowered, instead of emitting nothing — *"that silence is why `npkc` said yes and
`llc` said no"*. **O-N11, O-N14 and O-N17 were three instances of one shape**,
which this workbench had only ever described case by case. Our `program` stage
still runs all four steps, because `npkc` exit 0 is still not well-formedness,
but the class has gone from open-ended to bounded.

**A SECOND DEFECT, AND THE WORKER DELIBERATELY DID NOT NUMBER IT.** `.len` on a
fixed-size array `T[N]` is accepted by the frontend and refused by the emitter
at `NITPICK-EMIT-002`, whose own text asks to be reported. Registered here as
**O-N18**, accepted upstream as their **DEF-22**. **The worker left it
unnumbered and cited it by path**, because its predecessor had filed O-N17 as
`O-N12` — a number already held by `nitpick-regex`'s settled `>>>` question —
and undoing that took **ten edits in ten files**. **A worker cannot see what the
registry has issued, so it must not assign an id; it names the path and the
orchestrator numbers it.** That rule is now in `PLAYBOOK.md`, and the
repository's own `OPEN_QUESTIONS.md` gained an entry reading *"O-N12 — NOT THIS
REPOSITORY'S"*, which inoculates the next worker who reaches for a number.
**Seven `O-N12` strings remain in the tree on purpose**, annotating the
correction rather than erasing it — the verbatim transcript says the id was
corrected instead of being silently rewritten.

**TM-131 CORRECTED THIS SUBCYCLE'S OWN ACCEPTANCE, AND THE FIGURE HAD BEEN
INHERITED FOR THREE SUBCYCLES.** The acceptance said the non-leaking half
"finishes clean in under 768 KiB of address space". It does not — and neither
does anything else. **`/bin/true` and the probe flip at the same cap, between
2688 and 2816 KiB**, because at that size the dynamic loader fails rather than
the program. **A bound a trivial program also fails is not a statement about
your program.** The gate is now **one shared 64 MiB cap with opposite outcomes**
— `HeapOom` 92 against 0 — plus the peak-RSS pair, 125 184 KiB against 1 660.
**Every repository quoting an address-space bound owes a `/bin/true` control at
the same cap.** It was found only because the dispatch said to re-measure the
figure rather than inherit it.

**THE VERIFIER RAN THE COMMANDS THIS TIME, AND THE FIX WAS IN THE DISPATCH.**
After 0.0.3, where it twice substituted reading for running on checks that
needed setup, this dispatch supplied **the literal commands** for every such
check. It planted the magic constant and watched `check_constants_named`'s
denominator move **11/2 → 11/3**; it ran `/bin/true` at three caps; it compiled
all five O-N17 cases and all four controls. **The failure was never
unwillingness — it was that a check requiring construction has no command to
re-run, and reasoning is what fills that gap.** Supplying the construction
removed the gap.

**S-39, told to us unprompted and worth keeping straight:** an owning `List<T>`
local alive in `main` at exit 0 is reported `WildLeak`, exit 94, at our pin too,
because `exit` runs joins and defers **and no drops, by decision**, and a
`List`'s buffer is the one managed storage D-151 counts. **For the prelude's
`List` that is a surprise; for our containers it is the enforcement P-23 asked
for**, since `Vec<T>` spells its block `wild` precisely so an unpaired
`vec_free` traps at exit. **The same mechanism is a defect there and a feature
here, and the difference is whether the type's owner intended `wild`.** We asked
that the fix not become a general "D-151 stops counting managed storage".

### The pin moves to `aaffb87`, and the canary lands on its prediction — 2026-09-05

**Re-pinned `aaffb87` at 22:47**, the 1.5.2d close, immediately on the landing
notice and before any further work. **Both of this workbench's raised defects
are in this pin**: O-N17 as step 4, and DEF-21 — our allowlist finding — as
step 2b.

**Provenance checked rather than inferred, and §3's test passed honestly this
time.** `build/npkc`'s mtime (22:45:33) is **500 s after** `HEAD`'s commit
(22:37:13), so `tree clean` is a true statement about what the binary was built
from and not merely about the source tree. Every number verified here before
copying: 7 346 792 B, sha256 `a3b0dadc…`, `sha256sum -c` OK, LLVM 20.1.2,
`0dfddac` an ancestor of `aaffb87`. **`npkrt.o` byte-identical to the previous
pin's and `cmp`-verified rather than assumed** — DEF-12 is the precedent for
what assuming that costs. `aaffb87` is **docs-only over `0880771`**, so the
compiler source is `0880771`'s. **Commissioned both directions before any
measurement was believed:** the canary compiles at exit 0 writing a 50 560 B
`.ll`; a malformed file exits 1 at `NITPICK-PARSE-001` writing none.

**The mid-rebuild guard fired first, and was right.** The binary was 97 seconds
old and §3 said retry. **That is the second re-pin running where it has caught
this orchestrator moving straight off a landing notice** — the same 96-second
case occurred at `0dfddac`. Twice is a pattern rather than luck: **the notice
arrives while the ladder is still writing**, so the guard is doing the one thing
it exists for, and the correct response is to spend the wait on something else
rather than to shorten it.

**THE CANARY WAS A PREDICTION AND IT PASSED.** This board had stopped saying
*845 282 — a change is the signal*, which cannot distinguish a fix landing from
something going wrong, and started saying **check the VALUE**, expecting
~50 000 from the compiler session's own measurement.

| | `0dfddac` | `aaffb87` | |
|---|---|---|---|
| canary `.ll` | 845 282 B | **50 560 B** | **−94.0%** |
| canary functions | 608 | **14** | predicted 14, exact |
| full harness | **240 s** | **41.8 s** | **5.7× faster** |
| harness verdicts | 40 units, 0 fail | 40 units, 0 fail | unchanged |

**The one byte between our 50 560 and their predicted 50 561 is two different
source files** — they measured their floor probe and we measured ours — and the
function count matches exactly. **Recorded rather than smoothed over**, because
*"close enough"* is the habit by which a real difference gets absorbed the next
time one appears.

**Nothing broke, and that was not guaranteed.** The landing notice warned that
*"every emitted module holds only the prelude functions it references, so any
probe asserting a prelude symbol in IR needs a use"*. No probe here did — but
**the other four repositories must check at their next claim**, and that is now
on the board with the rest of what changes at this pin.

**All four discharged stops re-measured, and one improved.** **O-N11**: `case1`
names **4** identities and `case3` **6** — unchanged, so the per-program
correction made earlier today survives the pin that could have invalidated it.
**O-N4**: `probe04` is **1.18 s at 26 336 KiB**, against 2.03–2.06 s at ~119 MB
on `0dfddac` — faster *and* a quarter of the peak, so it stays discharged with
more room than before. **O-N9**: `BORROW-012` and `BORROW-001` unchanged.
**O-N10**: covered green by the harness's derive probes.

**O-N17 is fixed and verified here:** all five cases link and write objects,
including `case1` and `case5`, which gave `llc` exit 1 and no object at the old
pin; their IR fell from 850 377 B to 55 652 B alongside. **O-N18 still refuses
at `NITPICK-EMIT-002`**, correctly — it is their DEF-22, scheduled after the
landing.

**The whole S-38 raise is now closed with a number.** It began as a per-program
cost this workbench noticed *because* its harness compiles many small programs
and the compiler's own harness does not — a measurement whose visibility
depended on the shape of the thing measuring. It ends with **our full suite
running in a sixth of the time and the compiler's own build going 242 s to
21 s, 13.7 GB of allocation to 382 MB.** The workbench's contribution was the
per-program constant; the compiler session's option (2) — *measure the
frontend's share before believing the obvious cause* — is what turned it from
a prelude-size story into three scaling defects, and **our inference about the
cause was wrong while our measurement of the cost was right.**

### `nitpick-time` 0.0.5 — the estimate was low by 37%, and a use-after-free that exits 0 — 2026-09-05

**0.0.5 DONE — VERIFIED PASS** at `0c85648`, with one FAIL raised and
**adjudicated in the worker's favour on the orchestrator's own measurement**.
Harness green at 40 units in ~43 s, the first subcycle worked entirely against
the new `aaffb87` pin.

**THE NUMBER.** **475 006 B** for `ZONE_MODEL.md` Z-7's four tables and two
pools; **489 310 B (477.8 KiB)** with `POSIX_RULES` at its real cardinality.
Against a **≈356 119 B** estimate — **low by 37%**. Read off the object with
`nm -S` rather than computed, and that mattered: **two of the three estimated
row widths were wrong** (`ZoneTransition` 12 against **16**, `ZoneEntry` 16
against **28**), in a document that had already been reviewed. **TM-007 stands.**
Margin to the next band is **22 690 B = 1 418 transitions ≈ 4.4%**, now written
into the specification as Z-7b rather than left for a tzdata release to find.
**This is exactly what the subcycle was for**: an estimate sitting under a
decision every specification here rests on, replaced by a measurement *before*
cycle 0.5 could be built on it.

**AND IT FOUND A USE-AFTER-FREE THAT EXITS 0 — O-N19.** `NITPICK-TYPE-046` is
not enforced inside a generic function body: `T:answer = s[i]` at an owning `T`
is accepted, while the identical statement with `string` written out is refused.
The case that drops the first owner and reads the second **compiles, links,
runs, and exits 170 — the allocator's `0xAA` poison.** Reproduced by the
orchestrator end to end before it went upstream. **Accepted there as a soundness
hole in the checker**, not a regression and not O-N17's: the mechanism is
`require_move_if_owning` asking `type_drops`, which answers false for an
unsubstituted `T`, and the hole is present at all four pins this workbench has
used. O-N17's fix only made the consequence **runnable** where it previously
stopped at `llc`. **It goes to the author as a decision rather than a patch**,
because a generic body is checked once as a template and a move-only rule keyed
on ownership has no answer for `T`.

**AND THIS LIBRARY SHIPPED IT.** `vec_pop<T>` at 0.0.4 was the defect's own
`case1` verbatim — **written, reviewed, independently VERIFIED PASS, and
committed.** Every gate this repository owns is a leak gate, and `npkc` accepted
the program, so nothing in the pipeline could see it. **A leak is found by a
gate; this was found by a wrong answer.** Fixed at 0.0.5 with `move(s[…])`,
which the compiler session then ratified as the spelling the language means at
every `T` — so the library is already written the way the rule will require
whichever way the author rules.

**TM-137 IS THE FINDING THIS SUBCYCLE WOULD BE REMEMBERED FOR IF THE NUMBER
WERE NOT ITS POINT.** An exemption list's both-directions diff asks *is every
named file present, and every present file named* — **a question about
membership, while the thing that decays is the reason.** Two entries exempted
for O-N17 stated *in their own text* that they would fail that diff on the day
the defect landed. **It landed. Both files went from stopping at `llc` to
running clean. The suite stayed GREEN at 40 units with both stale entries in
place.** The prediction was written down, was correct about the world, and the
mechanism it named could not see it come true. **Fourth instance of §6's shape
here, and the first found inside a mechanism written to prevent it.** The
remedy — an exemption records the **verdict** it was written against and the
harness re-derives it every run — is now `check_exemptions_live`, and the
verifier drove it red.

**THE ONE FAIL WAS THE DISPATCH'S FAULT, NOT THE WORK'S, AND THE WAY IT HAPPENED
IS INSTRUCTIVE.** The verifier reported 454 files + 153 symlinks = 607 against
the worker's 447 + 153 = 600. **Both numbers are right about different sets:**
454 is every regular file under `zoneinfo`, **447 is the TZif files** — the
difference being exactly seven metadata files (`zone.tab`, `leapseconds`,
`tzdata.zi`, `iso3166.tab`, `zone1970.tab`, `zonenow.tab`,
`leap-seconds.list`), which the orchestrator confirmed by magic bytes. The
worker's own report said *"447 non-symlink **TZif**"*, with TZif doing real
work in the sentence. **The dispatch's literal command dropped it** —
`find … -type f | wc -l` cannot produce a TZif count — and then asserted the
identity against it.

**So the fix for the verifier's 0.0.3 gap produced a failure of its own.**
Supplying literal commands removed the verifier's temptation to reason, and
**moved the error out of its reasoning and into the dispatcher's command.**
That is not an argument against supplying them; it is the reason a FAIL is
adjudicated rather than obeyed. **A verifier's FAIL is evidence, not a verdict**,
and the orchestrator's job is to find out which of the two is wrong before
re-dispatching anybody.

**And it is the third time today two careful parties disagreed on a count while
both were right.** The `56`/`57` internal defines, the allowlist's
`112`/`57`/`113`/`106`, and now `447`/`454`. **When two measurements disagree,
the first question is what SET each one measured, not who miscounted** — and in
all three cases the answer was a denominator nobody had stated.

### Cycle 0.0 CLOSES — the first cycle closed anywhere in this ecosystem — 2026-09-06

**`nitpick-time` cycle 0.0 is CLOSED, VERIFIED PASS, archived at
`meta/roadmap/done/0.0/`, pushed, and CI is GREEN.** Harness green at **62
units, 0 failures, ~62 s**. Seven subcycles: the language probes, the skeleton,
two of harness, `src/core/`, the tzdb spike, and the close.

**All 30 audit findings triaged — 30 of 30 carry a line**, counted rather than
taken on report. Nothing was rejected on disagreement; the single refusal (F8,
a file rename) states its cost instead. **That is what W-22 is for**: the
auditor writes nothing and cannot defend its findings, so a close that drops one
silently is the failure the rule exists to prevent, and the only way to know is
to count.

**CI RAN FOR THE FIRST TIME IN THIS REPOSITORY'S HISTORY, AND ITS FIRST RUN WENT
RED.** Run `34014136095` failed on `f950ae4`; `8081e60` and `93293f2` are green.
Read from GitHub rather than from the report. **The close is three commits
because a CI result cannot live inside the commit that caused it** — an
obvious-once-said structural fact that no plan had anticipated. **The first run
found two defects in eight minutes, and both are in the shared workflow**: a
whole-tree sweep that walks the entire compiler, because **CI checks the pinned
compiler out INSIDE the workspace** where locally it is a sibling directory; and
a capture-then-print step that dies before the print, because **a GitHub `run:`
block already has `-e` on and `set -uo pipefail` does not clear it**. **Treat
the first CI run as an instrument rather than a formality** — it is the only
moment the workflow is tested against a machine that is not yours.

**THE CYCLE SHIPPED TWO USE-AFTER-FREES ON ITS OWN PUBLIC SURFACE AND CAUGHT
BOTH — the second one only because an adversarial reader was sent looking.**
`vec_pop<T>` at 0.0.4 passed review and an independent VERIFIED PASS.
`bytes_view`'s comment, promising a view outlives a growth it does not survive,
passed 0.0.4 and 0.0.5 untouched and was found by the audit. **Both are
invisible to every gate this repository owns, for one structural reason: they
are all leak gates.** D-151 counts `wild` blocks, D-188 counts live drivers, and
neither sees a managed body. **A leak is found by a gate; a use-after-free is
found by a wrong answer — so it is found by a test that reads, and by nothing
else.** That sentence is the most expensive thing this cycle learned.

**The audit's own headline finding was the same shape one level up.**
`check_no_owning_fields` could not parse a single-line struct declaration —
**and both of this repository's structs are single-line**, so neither type's
real fields had ever been examined. The self-check planted the violation
**multi-line**, so the check was red on the fixture its author wrote and silent
on the identical fault in the form the repository actually uses. **A check
commissioned on one spelling is commissioned on none.** Five instances of the
name-versus-mechanism shape landed in this cycle alone (TM-115, TM-137, TM-138,
TM-141, TM-144), **every one found by a reader and none by a run.**

**The harness grew 40 → 62 units, and the 22 are coverage rather than
re-counting**: the defect corpus the audit found asserting nothing — 21
committed `expect-` markers under `tests/probe/defect/`, the entire regression
record for four discharged compiler defects. The inversion the auditor named was
exact: **the three files EXEMPT from carrying an expectation had their verdicts
re-derived every run, and the 21 that CARRIED one did not.**

**~~O-N4~~ struck on this repository's own re-measurement** — 30 000 rows at
**1.17 s / 26 888 KiB** against 281 s / 30.9 GiB, with a **2 266 485 B `.ll`
carrying all 30 000 rows**, so the speed is not bought by emitting less. **Its
heading had read BLOCKING for two subcycles after its gate was passed** — the
same staleness direction the board was caught in earlier: everything here asks
whether a claimed fix is real and nothing asks whether a claimed debt is still
owed.

**AND ONE CORRECTION THE ORCHESTRATOR OWES, BECAUSE THE OVERSTATEMENT WAS
ITS OWN.** After the `0dfddac` rebuild this record and a message upstream both
said *"built from commit X"* is *"exactly as strong a claim as the pin"*. **That
reproduction was same-machine.** CI measured the other case: **`npkrt.o` is
byte-identical across machines and `npkc` is not** — `3c05818c…` in CI against
`a3b0dadc…` here. So a CI build of the pinned commit is **behaviourally**
equivalent, and the suite passing is what carries the weight; **byte-identity
across machines was never measured and is not claimed.** One data point,
deliberately not promoted to an assertion.

**The claim advances to cycle 0.1 — the civil calendar, `src/cal/`** — whose
opening subcycle is written and execution-grade. **The re-pin is held for the
compiler's 1.5.2f close**, which carries D-264, the rule this workbench's O-N19
forced.

### The seventh orchestrator takes the lock; a seven-tree sweep is eight, and the cross-machine digest procedure lands — 2026-09-06

**Handover.** `nitpick-libs_s2` (`7946260a-dc46-4a8d-b254-04e533e4082c`) takes
the writer lock from `nitpick-libs_s1` on a briefed overlap, at `d336e07`.
**Freedom verified on both readings and, for the first time, on the right side
of the write**: the line read `none` in the local tree *and* in `origin/main`
before the take, `.internal/` held only `toolchain/`, and the outgoing session
was asked hazard 3's question outright and **answered from `git status`** — `0`
porcelain lines, no ahead/behind, and *"messages only, I have made my last
write"*. **Third handover running, third time that question produced the
deciding fact**, and the only one of the four checks that no tree read can
supply.

**finding: the sweep that clears this lock has enumerated SEVEN trees since it
was written and there are EIGHT — and this is a denominator, not a count.**
Raised by the incoming session before taking the lock, conceded immediately by
the outgoing one: *"YOU ARE RIGHT AND I AM WRONG. It is EIGHT, and
`nitpick-apps` has never been in the loop that checks."* The eighth is
**`nitpick-apps` itself**, a tracked repository holding `APPS.md`,
`PLAYBOOK.md`, `README.md` and `LICENSE` — already in orchestrate §2.2's
startup *read* set, already covered by `CLAUDE.md`'s *"a library **or
application** repository"*, and never excluded by any decision. Every session
inherited the same seven-item list. Went to `BOARD.md` line 14 as **hazard 6**,
to `PLAYBOOK.md` §7 as the durable rule, and to `skills/orchestrate/SKILL.md`
§2 as a discovery command replacing the list.

**Why four orchestrators missed it, which is the part worth keeping: THREE SETS
ARE IN LIVE USE HERE AND ALL THREE ARE CORRECT UNDER THEIR OWN DENOMINATOR.**

| Phrase | Set | Verdict |
|---|---|---|
| "all six repositories" | the five libraries + `nitpick-posix` — the **work** set | **sound everywhere it appears.** `RECORD.md:907`, `:1061`, `:1176`, `:1784`, `:1833`, `:2004`, `:2095`, `:2699`, `WORKSTREAMS.md:67`, `meta/roadmap/0.2/0.2.0.md:235` and the audit at `meta/audits/devteam-import-2026-09-05.md:115` all measured the right thing |
| "all seven trees" | that six **plus this workbench** | **short by one, and only about its own extent** |
| eight | that seven **plus `nitpick-apps`** | the true set, measured clean and level at this takeover |

So the sweep was never checking a wrong thing; it was checking a smaller thing
than its sentence claimed. **That is why no reader caught it: every neighbouring
count in the same documents was right.** `RECORD.md:2699` had already asked one
of these counts for *"its denominator rather than its verdict"* — the right
question, asked of the one claim that could answer it.

**correction, appended and NOT rewritten, because this file says so in its own
header — *"Append-only; never rewritten"* — and because board question 1's
recommendation draws exactly this line: what may be amended depends on whether
the document records something that *happened*.** Two sentences above are now
known to understate their set and both stand as written:
`RECORD.md:3134` — *"all seven trees clean and level"*, the sixth
orchestrator's own verification at 16:4x — and `RECORD.md:3154` — *"all seven
trees committed **and pushed**"*. **Both were true of the seven they measured
and neither measured `nitpick-apps`.** They are corrected here rather than in
place. The outgoing session asked for the fix "when you take the lock"; the
form it takes is an append, and the disagreement is about mechanism, not fact.

**All eight measured at the take**, `dirty=0` and `ahead/behind=0/0` for each:
`nitpick-libs` `d336e07` · `nitpick-parse` `3cad08c` · `nitpick-regex`
`91657eb` · `nitpick-sockets` `d385991` · `nitpick-time` `93293f2` ·
`nitpick-tui` `e5439ee` · `nitpick-apps` `03c24a7` · `nitpick-posix` `948d9b6`.
**Nothing was lost, and nothing would have reported it if something had been** —
which is the finding rather than the count.

**finding: the incoming session asserted a commit hash it had not run a command
against, in its first message of the session, hours before writing the paragraph
above about running commands.** Telling the outgoing session its tree was clean
"at `b992544`", it named the *previous* handover's release commit; its actual
HEAD was `98d567d`, six commits back. The tree-clean half was measured and true;
the hash was pattern-matched from the shape of the situation. **Retracted
unprompted at the next message.** The outgoing session's reply is the reason it
is recorded here rather than dropped: the hash *"appears exactly once in the
tracked record — `RECORD.md:3133` — and it is my own measurement, not your
confirmation"*, so nothing downstream was wrong; **but retracting cost one
message and a false hash in a record costs forever.** The rule this workbench
keeps re-deriving — *the tell, every time, was a claim standing where no command
had been* — was violated by the session that had just read it.

**question Q1 answered by `nitpick-libs_s1`: it is eight, and `nitpick-apps` was
never excluded by decision.** Recorded above.

**question Q2 answered by `nitpick-libs_s1`: dispatch `nitpick-time` 0.1.0 at
`aaffb87` and do not wait for the re-pin.** Three reasons, and only the first
was the incoming session's own: D-264's four consequences are all about a
generic `T`, and `src/cal/` declares none — `Weekday` and `Month` are
payload-free, so `DERIVE-006` cannot bite either. **0.1.0 was WRITTEN at
`aaffb87`** and its nine binding cases are measured there, so running it at that
pin is running it where it was written rather than despite the hold. And its §1
item 4 **already predicts `check_exemptions_live` firing at the re-pin** — the
close worker thought about this interaction and wrote the answer down.
**Carried: any number 0.1.0 records is an `aaffb87` number and must be labelled
as one**, so the re-pin re-checks rather than inherits it — the discipline that
caught the "under 768 KiB" figure after three subcycles.

**question Q3 answered by `nitpick-libs_s1`: the 30-program spread is a
COMPARISON, and old pins are not deleted, so nothing is perishable and nothing
is being wasted by waiting.** `.internal/toolchain/` holds **four** —
`950bb1d`, `94874ce`, `0dfddac`, `aaffb87` — each with its binary present
(5 265 352 / 5 491 224 / 7 304 552 / 7 346 792 B). The original spread was taken
with *"both pinned compilers on disk, same inputs, same machine"*, which is what
made it a differential rather than a remembered number against a fresh one.
**Take it after the re-pin, both binaries over the same inputs in one pass.**
The incoming session's worry — that the before-half was perishable and idle time
was being wasted — rested on a false premise, and asking dissolved it instead of
producing a wrong measurement.

**question Q4 answered by `nitpick-libs_s1`: KEEP `nitpick-regex`'s `CLAIMED s1`
row, and the disanalogy is the answer.** The incoming session proposed releasing
it on the grounds that a claim no session holds is the same species of untruth
as a writer line advertising `none` while the lock is held. It is not: **the
writer line names a SESSION and a session dies; a `CLAIMED` row names a STREAM
and a stream does not.** W-7 ownership survives a session gap by design, and §4
recovery exists precisely because a claim outlives its agent — such a claim is
*stale*, which is a thing to recover, not a thing that is untrue. Run §4 before
any dispatch and the row resolves honestly. **The 0.0.4 debt stays visibly
attached:** `nitpick-regex/harness/README.md` claims §4 holds the mutation
transcripts and it does not, `nitpick-time` was once FAILED by its own verifier
for exactly that, and it must not pass a third time.

**question Q5 answered by `nitpick-libs_s1`: the address change reached the
compiler side and was confirmed rather than assumed.** `nitpick-compiler_s1`
replied that it relayed to `_s0`, which is landing 1.5.2f itself — *"`nitpick-libs_s2`
is the address for the 1.5.2f close notice."* The notice will carry the pin
commit with both byte counts, both digests and provenance; **`build/npkc.ll`'s
digest beside `npkc`'s from now on**, a change that came out of the
cross-machine finding below; the canary's expected value (50 561 B, 14
functions, *"unless the landing moves it, and whichever it is will be a measured
number"*); D-264's four consequences; and S-41 still open.

**THE CROSS-MACHINE DIGEST PROCEDURE, from `nitpick-compiler_s0`, recorded here
because it arrived after the sixth orchestrator's clean stop and the board did
not carry it.** Six digests, compared **in this order**; the first that differs
names the stage:

| Artifact | Digest | What it is |
|---|---|---|
| `builder.o` | `3b5f868dbab44253…` | the snapshot assembled by `llc` |
| `builder` | `f5c7f5174fc6fa11…` | linked by `ld.lld` |
| `npkrt.o` | `c9ddbcffd32eccc7…` | identical on the runner |
| **`npkc.ll`** | `f0abbfd09ce5ef18…` | **THE EMISSION**, 21 483 280 B |
| `npkc.o` | `a46983645fa690f4…` | |
| `npkc` | `a3b0dadc650421b2…` | |

**`npkc.ll` differing IS a compiler defect and they want the diff.**
`builder`/`builder.o` differing while `npkc.ll` matches is the runner's own LLVM
build. `npkc.o` differing with `npkc.ll` identical is `llc` codegen between two
20.1.2 builds. `npkc` differing with `npkc.o` identical is `ld.lld` layout or a
build-id. **The emission is the cross-machine claim and the binary never was** —
which is why the notices carry `npkc.ll`'s digest beside `npkc`'s from 1.5.2f
on, and which is the concrete form of the correction the previous entry ends on.

**State at the take.** Pin `aaffb87` held, `sha256sum -c` re-run here rather
than read off `PIN.md`: `npkc` 7 346 792 B and `npkrt.o` 55 576 B, both OK.
**The re-pin stays held** for 1.5.2f's single close notice; a landing notice
that asks us to wait is not a re-pin trigger. Width 1, stream 2 only.

- **stale claim `nitpick-time`: found `CLAIMED s2` at cycle 0.1 with no live
  agent, `0.1/0.1.0.md` titled `PLANNED`, tree clean at `93293f2`, done —
  §4's `PLANNED` + any row: the worker never started, so this is a fresh
  dispatch rather than a recovery of lost work.** Every claim is stale after a
  session restart by construction, because `ListAgents` shows only this
  session's agents; recorded so the word is not read as a fault.
- **stale claim `nitpick-regex`: found `CLAIMED s1` at 0.0.4, no live agent,
  `0.0/0.0.4.md` titled `PLANNED`, tree clean at `91657eb`, left claimed** —
  stream 1 idles at width 1 and W-7 ownership survives a session gap by design.
  The claim is kept rather than released: **the writer line names a session and
  a session dies; a `CLAIMED` row names a stream and a stream does not.**
- **finding: `nitpick-regex`'s carried 0.0.4 debt is real and is TWO defects in
  one sentence, not one.** Verified here against the tree rather than taken from
  the handoff: `harness/README.md:69` reads *"`../meta/roadmap/0.0/0.0.3.md` §4
  has the transcripts"*. It does not — that section holds a per-case
  **summary table** (`Mutation | Reddened | Left green`), which is what the
  acceptance criterion actually required and is why 0.0.3 was a PASS. **And the
  citation is ambiguous as well as overstated:** `0.0.3.md` carries **two**
  sections numbered `## 4.` — the plan half and the execution-record half each
  restart at 1 across the `## Execution record` divider — so *"§4"* names both
  "The tree checks" and "The self-check, and the mutation test that is its
  evidence". **0.0.4 must fix both halves**: claim only what is there, and cite
  it unambiguously. The dual numbering is a convention, not a defect, and the
  full extent is two files (`nitpick-regex/…/0.0.3.md`,
  `nitpick-time/…/done/0.0/0.0.4.md`) — measured across all six work
  repositories, not assumed.
- **dispatch `s2-ntime-0.1.0-0235`** — `nitpick-time` 0.1.0, the civil types,
  `claude-opus-5`, at pin `aaffb87` with the re-pin still held. **The author
  confirmed the dispatch rather than the orchestrator assuming it**, because
  quota is the binding constraint the width was turned down for and a worker
  plus a verifier is what it buys. The independence argument is on the board and
  in Q2 above; the one thing carried into `NOTES:` is that **every number it
  records is an `aaffb87` number and must say so.**

- **finding: the 30-program spread we OWE the compiler session at the re-pin
  cannot be re-run, because its program set was never recorded.** Found while
  waiting for 1.5.2f, ~40 minutes before the re-pin would have needed it.
  Searched exhaustively rather than sampled: four `BOARD.md` sites,
  `RECORD.md:3013`–`3017`, every `meta/` document, every `.md`/`.txt`/`.csv`/
  `.py`/`.sh` in this workbench tracked or untracked, and the compiler's own
  `meta/`. **Only the result survives** — *"30 programs across two libraries, 22
  sit at exactly 388 765, all 8 exceptions are derive or enum programs"* — and
  it names **no program, no library and no selection command**. The board's
  standing sentence that *"re-running a measurement we already know how to take
  is the cheapest confirmation available"* is therefore false as written, and
  has been since the day it was written.
- **This is hazard 6's shape a second time in one session, and the third
  instance this week**: a result published over a denominator nobody stated. The
  tree sweep's version cost nothing because the trees happened to be clean; the
  O-N12 citation count cost an understatement the outgoing session caught
  itself. **This one costs the re-measure its comparability**, which is the
  first time the shape has cost something we owe to another party. Recorded as
  evidence that the rule now in `PLAYBOOK.md` §7 — *discover the set, never list
  it, and print the count beside the verdict* — is not a bookkeeping nicety.
- **What survives, stated so the finding is not read as worse than it is.** The
  load-bearing claim never rested on the 30. A 14-line program that only exits 0
  went **456 517 B → 845 282 B**, and the 30 000-row program moved by the
  identical **388 765 B**; a delta independent of input size is a prelude cost
  and not a compile-time regression, and that pair is reproducible from its own
  description. **The 30 were the widening, not the argument.**
- **Decision, taken here and recorded so a later session does not re-litigate
  it: the re-measure is RE-FOUNDED, not repeated, and it will say so to the
  compiler session.** Define the set in a committed file before running it, by
  discovery — every program under `tests/` compiling clean under both pinned
  binaries, enumerated by command, count printed beside the verdict — and report
  the spread as **first-of-its-kind under a stated denominator**, with the floor
  pair carried forward as the one continuous measurement. **Claiming a
  continuity we cannot demonstrate would be the same overstatement this board
  has now caught four times**, and the compiler session is entitled to know
  which of the two numbers it can compare against yesterday's.
- **Sequencing, and it is a rule rather than a preference: `skills/orchestrate/SKILL.md`
  §2 says NEVER RE-PIN WHILE ANY CLAIM IS IN FLIGHT.** `nitpick-time` is claimed
  and `s2-ntime-0.1.0-0235` is live, so 1.5.2f's landing at ~03:20 does **not**
  start the re-pin: the worker must report and the verifier must PASS first.
  §3's mid-rebuild guard then applies on top — a `build/npkc` less than two
  minutes old means retry, and that guard has fired twice and been right both
  times, each time catching an orchestrator moving straight off a landing
  notice. **A landing notice is not a re-pin trigger; a quiet board plus an aged
  binary is.**

- **The re-founded spread is SPECIFIED, agreed with `nitpick-compiler_s0`, and
  it inverts the old finding's signal.** Raising the missing denominator bought
  a better measurement than a repeat would have been, which is the argument for
  raising these rather than quietly working around them. **1.5.2d's trim emits
  only the prelude items a program references**, so the constant that was the
  *finding* — 22 of 30 at exactly 388 765 B, proving a whole-prelude emission —
  is now the **failure signal**: a delta constant across programs means the trim
  did not apply, which is a compiler defect, and they want the program that
  shows it. **A session remembering "22 of 30 at 388 765" as the good number
  would read the new result exactly backwards**, so the inversion leads the
  board block rather than sitting inside it. Their prediction, which makes this
  a test rather than a survey: **the derive and enum programs — the 8 that were
  the exceptions before — should now be at the TOP**, since their impls are what
  they reference. No comparison against "22 of 30" is wanted.
- **finding: the request as received asks for the wrong unit, and this
  workbench's own measurement is what corrects it.** `nitpick-compiler_s0` asked
  for the distribution of **IR bytes** and function counts. `nitpick-time` 0.0.5
  measured that **an emitted `.ll`'s byte count is PATH-DEPENDENT and the
  object's is not** — the same source compiled from two directories whose names
  differ by one character gives `.ll` sizes **14 bytes apart**, one byte per
  `npk.site.paths` entry, while the `.o` and the linked binary are
  byte-identical. **A distribution taken across programs at different paths
  therefore carries a per-program artefact of its own directory name** — a
  confound inside the very statistic meant to expose confounds. Corrected on the
  board: **function counts and object sizes are the primary series**, `.ll`
  bytes reported beside them and labelled path-dependent, or every program
  compiled from one common directory if `.ll` bytes must be comparable. This is
  the board's existing rule — **quote the OBJECT, not the `.ll`** — reaching a
  case nobody had applied it to. Returned to them rather than silently
  substituted, since it is their measurement to accept.
- **finding: the floor pair they asked for is LARGELY ALREADY TAKEN, which
  changes what 1.5.2f buys.** The canary *is* the 14-line floor program, and the
  `0dfddac → aaffb87` pair is on this board: `.ll` **845 282 B → 50 560 B**
  (−94.0%), functions **608 → 14**, with **14 predicted and hit exactly**. So
  1.5.2f yields a **third point in a series** rather than a first comparison,
  and the one-byte gap against their 50 561 was explained by 0.0.5's
  path-dependence measurement — **not** by the "two different source files" this
  board first asserted as fact and later had to correct. That correction is why
  the function count, not the byte count, carried the 1.5.2d prediction.

- **The re-founded spread's specification is SETTLED**, not proposed:
  `nitpick-compiler_s0` accepted the unit correction in full — function counts
  and object sizes as the primary series, `.ll` bytes beside them labelled
  path-dependent, **no common-directory compile needed**. The floor pair stands
  as measured (845 282 → 50 560 B, 608 → 14 functions, the 14 predicted), and
  the 1.5.2f point on that series is what they expect back.
- **finding: they supplied the MECHANISM this workbench only had empirically,
  and it has a decision number — `D-236`.** Our side had *"an `.ll`'s byte count
  is path-dependent, one byte per `npk.site.paths` entry"*, measured by
  `nitpick-time` 0.0.5 and true but unexplained. Theirs: *"every site row
  carries the source path **relative to the manifest root**, so a program's own
  directory name is in its `.ll` and the byte is the path."* **That upgrades a
  measured regularity into a documented design property**, which matters because
  a regularity might change under a re-pin and a ratified design property should
  not. Verified at the pin rather than taken on report: `D-236` is
  *"manifest-root-relative paths in the source manager"*, user-ratified
  2026-09-01, landed at 1.4.8 — `aaffb87:meta/roadmap/OPEN_DECISIONS.md:135` and
  `aaffb87:meta/roadmap/done/1.4/1.4.8.md:125`.
- **And it refines WHICH unit is sharpest, which is not what this workbench had
  concluded.** We had reached "function count, because it is path-independent" —
  a correct conclusion from a weaker reason. Theirs is the real one: **the trim
  removes whole `define`s**, so the function count moves in units of the thing
  being tested rather than in bytes. Path-independence makes it *trustworthy*;
  removing whole defines makes it *sensitive*. Both were needed and we had one.
- **finding: this resolves a seam on our own board that would otherwise read as
  a contradiction, and the dangerous direction is dismissal.** `BOARD.md:137`
  says D-236 *"renders every embedded source path relative to the manifest root,
  so the build path cannot leak into the artefact"*, cited as a reason CI is
  reproducible. `BOARD.md:641` says an `.ll`'s byte count is path-dependent.
  **Both are true and they concern different paths:** D-236 removes the
  **absolute** path above the manifest root — so moving or re-cloning the
  checkout changes nothing, which is what CI's repro stage tests — and leaves
  the **manifest-relative** path in, so two programs at different relative paths
  carry different byte counts, which is what 0.0.5 measured. **A reader taking
  line 137 to mean "paths do not affect the artefact" would use it to dismiss
  the path-dependence finding**, and the two sentences sit ~500 lines apart with
  nothing joining them. The consequence worth carrying: our `.ll` byte counts
  are **portable across machines and checkouts** and **not comparable between
  programs** — different properties, and only the first is what CI tests.

- **report `s2-ntime-0.1.0-0235` DONE**, 399 037 tokens, 49.4 minutes, 177 tool
  uses, one commit `2589069`, tree clean and **1 ahead of origin — deliberately
  not pushed**, workbench and compiler untouched. `check_record` clean; harness
  claimed **GREEN, 67 units, 0 failures, 5 pending**, growing 62 → 67. **Nothing
  moves on the board until the verifier answers**; `s2-ntime-0.1.0-verify-0325`
  dispatched on a small model with **literal commands for every check**,
  including two throwaway-worktree checks — the 62-unit baseline re-derived at
  `93293f2`, and a **planted fault breaking one leap-year condition, which must
  turn the suite RED**. That last is the answer to the failure mode this
  workbench has been caught by twice: *a green suite is evidence only of what it
  is shaped to see*, and `nitpick-time` shipped two use-after-frees under one.
- **finding: 1.5.2f IS CLOSED at `3d15ac9` and the RE-PIN IS STILL GATED, by our
  rule rather than theirs.** Orchestrate §2 forbids re-pinning while any claim is
  in flight and `nitpick-time` is claimed, so the order is verifier PASS →
  advance → §3. Verified read-only before recording: `3d15ac9` is their HEAD,
  tree clean, level with origin, and all three commits exist with matching
  subjects. Their `build/npkc` was **124 seconds old at 03:27**, clearing §3's
  two-minute guard by four seconds — noted because that guard has fired twice
  and been right both times, and this is the closest it has come to firing on a
  notice that was in fact ready.
- **`3d15ac9` carries `S-42`, which is OURS** — recorded by the compiler side
  from this workbench's first CI run: the toolchain pin is a **version** and a
  version is not a binary; the pinned commit's `build/npkc` differs between this
  machine and GitHub's runner while `npkrt.o` is identical; **the property that
  holds across machines is the EMISSION**, and a difference there is a compiler
  defect. It is open with their author, not yet ruled. **A finding this
  workbench filed as a correction of its own overstatement became a compiler
  decision**, which is the return on having recorded the correction rather than
  quietly fixing the sentence.
- **finding, and it is a trap this board LAID FOR ITSELF within one hour: there
  are now TWO six-digest tables on this board at two different commits, and
  comparing them is a category error.** The six digests localise a difference
  **between machines at one commit**; they say nothing across commits. `npkc.ll`
  moved `f0abbfd0…`/21 483 280 B → `05457db4…`/21 514 197 B, **+30 917 B**,
  between `aaffb87` and `3d15ac9` — the expected consequence of shipping D-264,
  **not** the *"`npkc.ll` differs = compiler defect"* rule firing. Three of the
  six are unchanged across the two versions (`builder.o`, `builder`, `npkrt.o`),
  which makes the fourth's movement look like a signal against three controls.
  **A warning now sits directly under the second table.** This is the same shape
  as the spread's inversion, found the same night: a diagnostic whose meaning
  depends on a comparison axis nobody wrote down.
- **The canary prediction for the re-pin is FLAT, and that is stronger than a
  moving one.** Their floor-only probe under `3d15ac9` reads **50 561 B and 14
  `define`s, identical to 1.5.2d's**, so our floor program should hold at
  **50 560 B / 14 functions** and **the 1.5.2f point on the floor series should
  not move. Anything else is a finding.** Third prediction in this series; the
  previous two were hit exactly. **A prediction that forbids all movement is
  falsified by any movement**, which is precisely why it is worth taking rather
  than merely observing the number afterwards.

- **verify `s2-ntime-0.1.0-verify-0325` PASS** on `2589069`, 35 450 tokens, 4.5
  minutes, small model. **All seven checks answered with an observed value
  beside the claimed one, and none substituted reading for running** — which is
  the failure mode the previous orchestrator measured twice and fixed by
  supplying literal commands. Harness re-derived **GREEN 67 units / 0 failures /
  5 pending** at 65.0 s; the 62-unit baseline re-derived **in a throwaway
  worktree at `93293f2`**, so the 62 → 67 growth is measured at both ends rather
  than inferred from a delta.
- **THE PLANTED FAULT IS THE CHECK THAT MATTERED AND IT WORKED.** Breaking the
  400-year leap rule in a throwaway worktree turned the suite **RED — 64 of 67,
  three failures, `tests/unit/leap_rule.npk` exit 10**. This repository shipped
  **two** use-after-frees under a green suite in cycle 0.0, both through review
  and one through an independent VERIFIED PASS, so *"the suite is green"* has a
  measured history of meaning nothing here. **A suite that cannot be shown to
  fail on the thing it claims to test is not evidence**, and this is the first
  subcycle where that was demonstrated rather than assumed.
- **The worker reported a defect against itself and had already fixed it**,
  which the verifier confirmed independently: `BUILD.md` now reads **"83 files =
  66 parse cleanly + 15 parse and are refused later + 2 do not parse"**, matching
  the tree, over the stated denominator *all `.npk` files in the tree*. The
  earlier "64 + 16" came from an intermediate RED run. **Self-reported and
  self-fixed is the outcome this discipline is for**; it is recorded because the
  *class* is durable even though this instance is closed.
- **finding: the gate-after-staging rule added to this workbench at 02:4x caught
  a real defect at 03:1x — within the same session it was written.** `git grep
  -l` reads the index, so the worker's token-correction sweep skipped a file the
  same commit was adding: it reported four corrected and there were five. The
  catch came from running `check_refs` a **second time after `git add`**, the
  rule this board adopted from the outgoing session's trap 5. **`check_refs`
  enumerates with `git ls-files` and has the identical blind spot — one
  index-blind tool caught another, and neither would have caught itself.** Into
  `PLAYBOOK.md` §7 beside the denominator rule, with `git grep --untracked` as
  the fix.
- **advance `nitpick-time` 0.1.0 → 0.1.1.** The claim stays with s2. **`0.1.1.md`
  DOES NOT EXIST** — the convention writes only a cycle's *opening* subcycle file
  — so 0.1.1 needs either a planner dispatch or a ruling that it is worked from
  the cycle README's checklist. **Raised to the author rather than decided here**
  (§9 item 6: anything ambiguous enough that you would be guessing), and the
  worker's own recommendation is on the questions table: **0.1.2's exhaustive
  sweep is the cycle gate and is the one that most wants an execution-grade
  plan.**
- **finding: TWO LANGUAGE FACTS FROM 0.1.0 MAKE EVERY LIBRARY HERE OVERCLAIM,
  and neither was found by a gate.** A `pub struct` has no private fields and
  `opaque struct:Name = { … };` is refused (D-149), so *"cannot be constructed
  invalid"* is a claim the language does not support — a consumer's struct
  literal compiles, links and runs, and the guarantee is only about what the
  library **produces**. And an `error:` identity cannot carry a payload —
  `Result<T>` is `{ T value, tbb32 err }`, so the error half of every return is a
  **code**, and `PLAYBOOK.md` §3's *"put the detail in a rich value the caller
  reads"* names a detail field that does not exist. **Both reach four sibling
  repositories** — a compiled pattern, a validated layout, a parsed address, a
  validated cell — each of which has already written the unsupported claim down.
  Into the board's SHARED FINDINGS block with the per-repository table and into
  `PLAYBOOK.md` §2. **Each repository fixes its own at its next claim (W-7).**
  **The shared cause is worth more than either fact:** every specification here
  was written in the shape of a language that has private fields and
  payload-carrying errors, because that is the shape its authors came from, and
  **nothing in this ecosystem would have reported that until a library tried to
  compile it.**
- **finding: `fails <Identity>` is not a function-signature clause.** The
  contract window is closed — `requires`, `ensures`, `acquires`, `never fails`,
  `joins`, `pure` — and a fallible function simply omits `never fails`. `fails`
  survives as a `VerificationKeyword` only because D-002's FFI contracts used it
  and D-149 removed those. **It read so natural that it was written into a
  REVIEWED plan file and survived to execution**, which is the argument for
  `PLAYBOOK.md` §2's measured-facts list existing at all.

- **finding, and the process error is mine: the orchestrator COMMITTED OVER A
  GATE FINDING, because the gate ran in the same shell script as the commit.**
  `check_refs` reported `undefined-question` on the 0.1.0 close and `e9bf06f`
  landed anyway — the output was printed, and the `git commit` on the next line
  did not read it. **The mandated order is right and the mechanisation defeated
  it:** running the gate and the commit in one non-interactive block makes the
  gate advisory, which is exactly the state the rule exists to prevent. **A gate
  whose result nothing branches on is a log line.** The fix is procedural and
  costs nothing: run the gate, read it, then commit as a separate step.
- **AND THE NEAR-MISS IS WORTH MORE THAN THE ERROR.** The finding was a bare
  `O-X8` cited on the board; `O-X8` is defined in `nitpick-time`'s own registry,
  and `check_refs` resolves questions only against **the repository it is
  scanning**. The orchestrator's first conclusion was that the check's mechanism
  was narrower than its name — the shape found four times already tonight — and
  the intended fix was to teach it to resolve library ids against sibling
  repositories. **That fix would have been actively wrong, and one command
  showed it.** Measured across all six work repositories rather than taken from
  the convention's word — **the letters collide as badly as the numbers**:

```
O-X1   nitpick-regex, nitpick-time, nitpick-tui       THREE different questions
O-X2   nitpick-time, nitpick-tui                      two
O-B1   nitpick-regex, nitpick-sockets, nitpick-time,
       nitpick-tui, nitpick-posix                     FIVE
```

  A sibling-resolving `check_refs` would have named the wrong repository for the
  first of those in two cases out of three — **a false negative dressed as a
  fix, in the one tool this workbench uses to catch false references.**
- **finding: `prose()` DOES NOT STRIP AN INDENTED FENCE, and its docstring does
  not say so.** `FENCE` is `^```.*?^```` under `re.M`, so the opening delimiter
  must sit at **column 0**; a fence nested inside a list item — the natural way
  to attach evidence to a bullet in this file — is invisible to it and its
  contents are read as prose. Found by writing exactly that and watching the
  gate report three ids it should have ignored. **The docstring already states
  one limit of this kind** (verbatim output quoted with *inline* backticks is
  still counted) **and this is a second, undocumented one.** Same shape as the
  night's other findings: a mechanism narrower than its name. **Not fixed here**
  — widening the pattern to allow leading whitespace is a one-line change to a
  gate that everything commits through, it needs its own control case, and it
  is not this subcycle's. **The evidence block above is therefore un-indented
  deliberately**, which is the workaround and reads as a wart until the pattern
  is widened. Raised for the author.
- **That was the third time in ten minutes this gate was right about its
  author.** Naming those ids in prose *cites* them, and citing a colliding
  library id is precisely what the new registry section forbids — so the first
  draft of this very entry tripped `undefined-question` three times, then twice
  more after the fence was added indented. **The rule and its escape hatch were
  both already there; what was missing was the author reading the gate as its
  own step rather than in the same block as the commit.**
- **The lesson, and it is the counterweight to the last three findings rather
  than another instance of them.** Four times tonight the answer was *the check
  is narrower than its name; fix the mechanism*. This time the check was exactly
  as wide as it should be and **the citation was wrong** — and the two cases are
  indistinguishable from the finding alone. **What separated them was measuring
  the premise the convention rests on instead of accepting it.** A check
  reporting a false positive invites being weakened, and **the weakening looks
  like a fix right up until you count.**
- **Resolved by a second registry rather than by a tool change or a rewrite of
  the record.** `meta/OPEN_QUESTIONS.md` gains **"Library questions this board
  cites"**, carrying the collision table and one entry per cited id naming its
  repository. That resolves the reference at workbench scope, keeps `RECORD.md`
  append-only, leaves `check_refs` untouched, and **forces the next citation of
  a colliding id to disambiguate rather than permitting it silently.** Gate clean
  afterwards, and `test_check_refs.py` re-run to prove it cleared by being
  satisfied and not by being weakened: **13 cases, 7 fault classes, 4
  false-positive controls, 2 denominator cases, all correct** — with
  `undefined-question` still firing.

- **pin `3d15ac9`, tree clean** — the re-pin the board had held since 02:00,
  taken 2026-09-06 03:40 once 0.1.0 was verified and nothing was in flight.
  **Both §3 guards cleared before anything was copied**, which is the first
  re-pin where that was true on the first attempt: the binary's mtime is
  **725 s after** `HEAD`'s commit (the provenance test — a binary older than
  `HEAD` cannot be a build of it), and it was **876 s old**, past the
  two-minute mid-rebuild floor. **Digests matched the compiler's notice** rather
  than being taken from it, `npkrt.o` was `cmp`-verified byte-identical to the
  `aaffb87` pin's on DEF-12's precedent, LLVM 20.1.2, and `aaffb87` is an
  ancestor so the pin moves forward.
- **THE FLAT PREDICTION HELD, AND IT WAS A REAL TEST.** `nitpick-compiler_s0`
  predicted the 1.5.2f point on the floor series would not move at all. The same
  program through both pinned compilers on this machine — the differential the
  board's own method requires, and possible only because old pins are kept —
  gives `aaffb87` **50 482 B / 14 `define`s** and `3d15ac9` **50 482 B / 14
  `define`s**. Byte-identical and define-identical. **A prediction that forbids
  all movement is falsified by any movement**, which is what makes a flat one
  worth more than a moving one. Third prediction in this series; all three hit.
- **finding: THE CANARY'S SOURCE WAS NEVER COMMITTED, and it is the measurement
  this workbench relies on most.** Until today it lived in a session scratchpad.
  The 2026-09-05 reading's **output** survived there by accident — `canary.ll`,
  50 560 B, 14 defines — and **its input did not**, so the series could not be
  continued from its own materials. **This is the 30-program spread's defect
  again, found the same night, on the one number the compiler session asks for
  at every re-pin.** Fixed rather than noted: the canary is committed at
  `tools/canary.npk` with `tools/canary.md` carrying the method, the series and
  which number to trust. **The series restarts here**: the 78-byte gap between
  the lost program and this reconstruction is a *different program*, not a
  compiler change, and the define count of 14 is what carries across the break.
- **finding: `npkc` writes the emission to STDOUT.** An unredirected run in an
  agent session dumps ~50 000 bytes of IR into the transcript, which is what
  happened on this canary's first reading and cost real context. **Redirect
  first, always** — `$NPKC prog.npk > out.ll` — and capture the status with
  `; echo "exit=$?"` immediately after, never through a pipeline, because a
  `$(cmd | tail -1)` capture reads `tail`'s status. Into `tools/canary.md`.
- **finding: the canary is a WEAK case for the path-dependence rule, and the
  measurement said so before the document could overclaim.** `tools/canary.md`'s
  first draft asserted that a byte count is comparable only against one taken
  from the same path. Compiled from a session scratchpad and again from
  `tools/` — six characters apart — the canary emits **the same 50 482 bytes**.
  The emission shows why: the site path table is overwhelmingly the *prelude's*
  rows, every one the fixed string `prelude.npk`, and a floor program
  contributes almost none of its own. **Path dependence is real and scales with
  a program's own site count** — `nitpick-time` 0.0.5 measured 14 bytes between
  two directories one character apart because that program had 14 site rows.
  **The rule holds for the spread and barely registers here**, and the document
  now says so. Written down because the draft was corrected by running the
  command against it, which is the only reason it did not ship as fact.

- **`nitpick-compiler_s1` stated D-236's mechanism exactly, and it SHARPENS the
  unit argument rather than softening it.** Their words: *"every site row carries
  the source path relative to the manifest root **the driver finds by walking up
  from the main file**, so the absolute build directory never registers (the
  repro stage measures that), and a program's own rows change only when its path
  WITHIN its manifest tree changes. A spread over programs held at fixed
  relative paths has **stable** byte counts."* **So the per-program artefact is
  DETERMINISTIC, not noise** — same path, same count, every run and every
  machine. That is a better situation than noisy and it **does not** make counts
  comparable between programs, which was the whole of the argument. It also
  settles that `nitpick-time` 0.0.5's 14-byte measurement was **the mechanism
  working, not a leak** — a distinction the workbench had not been able to make
  from its own side.
- **release `nitpick-libs` — the writer lock released 04:0x at a clean stop on
  the author's instruction.** Marker removed first, then the board line, then
  pushed. **State at the stop:** pin `3d15ac9` commissioned and verified;
  `nitpick-time` 0.1.0 DONE and VERIFIED PASS at `2589069`, harness 67 units,
  **1 ahead of origin by design**; `nitpick-regex` still `CLAIMED s1` at 0.0.4
  with its two-part `harness/README.md` debt attached; eight trees swept by
  discovery; nothing in flight; no agent live.
- **What the seventh orchestrator leaves owed, both unstarted and both needing a
  worker:** the **re-founded spread** for the compiler side — specified in full
  on the board, set to be defined and committed *before* it is run, reported as
  function counts and object bytes with `.ll` beside them labelled, and **a
  constant delta anywhere is a compiler defect rather than a result** — and
  **0.1.1's plan**, which does not exist because the convention writes only a
  cycle's opening file. **0.1.2's exhaustive sweep is the cycle gate and is the
  one that most wants an execution-grade plan**, which is the worker's own
  recommendation and the reason this was not guessed at.
- **The session's one-line summary, and it cuts against the night's own grain.**
  Five times the finding was *a check narrower than its name* — the tree sweep,
  the spread's missing set, the two digest tables, the canary's lost source, the
  indented fence. **The sixth time the check was exactly right and the author was
  wrong**, and from the finding alone the two cases were indistinguishable. What
  separated them, every time, was **measuring the premise instead of accepting
  it**: eight trees not seven, one library question id defined in three
  repositories rather than one, 50 482 bytes from two different paths rather
  than two different numbers. **The failure mode is not believing the wrong
  thing; it is not running the command that would tell you which thing you
  believe.**
- **And the gate got the last word, which is the right ending for this record.**
  The paragraph above originally named that colliding id outright — in the
  sentence summarising the lesson about not naming it. `check_refs` reported
  `undefined-question` a fourth time, on the same id, in the entry describing
  the third. **The rule is one session old and its author broke it while writing
  its summary.** What that argues is not a better rule but a better habit:
  **describe a library question, do not spell its id**, and keep any measured
  evidence in a column-0 fence. A rule obeyed only when remembered is a rule
  that needs a check — and this one has one, which is the only reason the
  sentence is right now.

- **`nitpick-time` 0.1.0 PUSHED** at the author's instruction — `2589069` to
  `origin/main`, tree level. CI run **`34020573741`** started immediately. **The
  push is coherent rather than merely permitted, and that was checked before
  pushing:** `nitpick-time`'s CI pins `NITPICK_COMMIT: aaffb87…`, which is
  **exactly the pin 0.1.0 was written and verified at**, so CI judges the code
  against the compiler it was proved against. Pushing after bumping CI's pin
  would have tested 0.1.0 on a compiler it had never been verified on.
- **finding: THE RE-PIN CREATED A DIVERGENCE THAT IS CORRECT TODAY AND BECOMES A
  TRAP AT 0.1.1.** Three compiler pins are now live: the workbench at
  **`3d15ac9`**, `nitpick-time`'s CI at **`aaffb87`**, and `nitpick-regex`'s CI
  at **`950bb1d`**. The first two agree with what has been verified; **the next
  subcycle worked at `3d15ac9` would be verified locally against one compiler
  and judged by CI against another**, and nothing would say so — the run would
  simply be green or red about the wrong thing. `nitpick-time`'s workflow says
  in its own header that bumping the pin *"is a deliberate commit, and this is
  that commit"*, so **the bump belongs BEFORE 0.1.1's work, as its own commit,
  and that commit is what proves `3d15ac9` builds the existing tree.**
- **finding: `nitpick-regex`'s CI HAS BEEN RED AT ITS CURRENT HEAD FOR TWO DAYS
  AND NOBODY LOOKED.** Run `33901134351`, 2026-09-04, on `91657eb` — **the very
  commit this board records as "0.0.3 DONE — VERIFIED PASS … harness 63/63 in
  37.5 s"**. The failing step is `Run the harness`; the compiler and LLVM steps
  were cache hits and passed. **Local harness green, CI harness red, same
  commit, unnoticed for two days.** That is `nitpick-time`'s TM-146 lesson —
  *treat the first CI run as an instrument, not a formality* — reaching a
  sibling where no one was reading the instrument. **The CAUSE is NOT
  established:** `gh run view --log` returns an empty log for that run, so the
  failure text could not be retrieved here, and **it is recorded as an
  unexplained red rather than guessed at.** Its CI also pins `950bb1d`, **57
  compiler commits behind `3d15ac9`** and dated 2026-09-03, so a stale pin is a
  live hypothesis and nothing more.
- **finding: only TWO of the six work repositories have CI at all.**
  `nitpick-parse`, `nitpick-sockets`, `nitpick-tui` and `nitpick-posix` have **no
  `.github/workflows` directory**. So the ecosystem's strongest recent lesson —
  that CI's first run on `nitpick-time` found two defects nothing on this machine
  could reach — currently protects one repository and is broken in the other.
  **Stated with its denominator: 6 work repositories, 2 with a workflow, 1 of
  those green.**
- **CI GREEN on `2589069`** — run `34020573741`, `nitpick-time` 0.1.0, read from
  GitHub rather than assumed. **So 0.1.0 is now confirmed on a second machine
  with a differently-built compiler**, which is the property a local harness
  cannot establish and the whole argument for pushing mid-cycle rather than
  waiting for 0.1.5. The worker recommended it; the author authorised it; it
  cost one push and bought a cross-machine verdict.
- **release `nitpick-libs` — the writer lock released 2026-09-06 04:2x at a
  clean stop, for a briefed handoff to `nitpick-libs_s3`.** Marker first, then
  the line, then pushed, then re-read from `origin/main`. **The retake at 04:1x
  was for one errand and is recorded as such** so the two takes are not read as
  a session that could not decide: released at 04:0x on the author's stop,
  retaken when he asked for the push and the handoff, released again here.
- **writer taken 2026-09-06 05:0x by `647e6588-8236-4fcc-91a1-0223d220639f`,
  session `nitpick-libs_s3`, the eighth orchestrator.** Not a takeover: the lock
  was released cleanly and the release was verified rather than trusted, on
  **three** independent readings — the writer line read `none` both locally and
  on `origin/main` (the same commit, `15969bf`), `.internal/` held only
  `toolchain/`, and **both** libs peers answered from commands. `nitpick-libs_s2`
  returned a verbatim `git status` with *"`15969bf` is my last write, everything
  from here is messages only"*; `nitpick-libs_s4` returned *"idle, nothing
  written, nothing queued"* and undertook to message before it ever writes here.
  Board line first, then the marker (37 bytes), then pushed, then the line
  re-read out of `origin/main`. Own eight-tree sweep, discovered not listed: all
  clean and level.
- **finding: `nitpick-libs_s4` contributed a check worth keeping to the lock
  protocol.** Asked only whether it was idle, it volunteered that the workbench
  `HEAD` had moved under it since it opened and suggested reading
  `git show 15969bf -- BOARD.md` before overwriting the writer line, *"so you are
  taking the lock from a state you have actually read rather than one you
  inferred — the same standard you just applied to me."* Done, and it confirmed
  the release is genuine. **The peer you query for a one-line fact can hand back
  a better procedure than the one you were running.**
- **question Q-5 answered by measurement, not by the author, and CLOSED:
  `nitpick-regex`'s two-day CI red is diagnosed, reproduced and bounded.** One
  tree at `91657eb`, three kept pins, this machine: `950bb1d` (what its CI pins)
  **60/63 in 36.0 s, reproducing the red**; `94874ce` (what 0.0.3 was verified
  at) **63/63 in 37.7 s**; `3d15ac9` (today's pin) **dies at the baseline before
  any suite runs.** The red is three probes 0.0.3 added that need derived
  `Eq`/`Ord` — `NITPICK-TYPE-034`, *"`HirKind` has no built-in `==`"*. `950bb1d`
  predates that support.
- **finding, and the durable half: A CORRECT BRACKET SUPPORTED A WRONG
  INFERENCE, AND TWO SESSIONS DREW IT INDEPENDENTLY.** The outgoing orchestrator
  established — correctly; the readings were re-run and are not in dispute — that
  `NITPICK_COMMIT` is byte-identical at the last green commit and at the red one
  and that `.github/` is untouched between them, and concluded *"the red is
  0.0.3's own content, not the stale pin"*, suspecting `harness/treecheck.py`
  failing on a runner. The incoming orchestrator reached the same conclusion off
  the same bracket and wrote it down before measuring. **Both were wrong and the
  measurement is what separated them from it.** An unchanged pin is not an
  exonerated pin when the tree has come to *require* a newer compiler: the tree
  change is the trigger, the stale pin is the cause, and neither alone explains
  the red. **Holding a variable fixed proves it did not change; it does not prove
  it did not matter.** `treecheck.py` is refuted outright — the red reproduces
  here with no runner involved.
- **finding: the recommended diagnostic was refuted by the OPPOSITE result from
  the one it predicted.** The board had recommended bumping `NITPICK_COMMIT` to
  `3d15ac9` and re-running *as a diagnostic* — *"if the red was the stale pin it
  goes green"*. At `3d15ac9` the harness never reaches the suite: it dies in the
  build step with **23 floor symbols "committed and no longer emitted — THE
  PRELUDE MOVED"** (`__divti3`, `npk_alloc`, `npk_exec`, `npk_sys6`, …), which is
  1.5.2d's prelude trim arriving in the one repository that records a symbol
  floor. **A test that cannot run is not a test that passed**, and a diagnostic
  whose failure mode is "dies earlier, for a third reason" diagnoses nothing.
- **finding: re-recording the baseline surfaces a failure no document
  predicted.** Measured in a **copy**, so the claimed tree was never touched:
  re-record at `3d15ac9` and the suite runs **61/63 in 21.5 s** — the derive
  probes pass, and `probe13b_limit_refused.npk` expects `NITPICK-RUNG-001` and
  gets `NITPICK-REACH-002`, in both the `probe` and the `parse` stage. Raised as
  question 8 **to the compiler side, as a question and not a defect report**,
  because a library cannot distinguish a deliberate diagnostic change from a
  regression. **The expectation is NOT being updated to make the suite green
  before the answer arrives** — that would convert an open question into a
  silently-encoded assumption.
- **finding: the extent was bounded immediately rather than left open.** The
  prelude trim breaks any repository recording a floor-symbol baseline; asked of
  all six work repositories with `git ls-files`, **exactly one has one** —
  `nitpick-regex`. The other five carry none, **so this does not spread**, and
  that is a measurement rather than a hope.
- **finding: the CI log is unrecoverable at the source, which is a different
  fact from "empty".** The previous session reported `gh run view --log` empty;
  the API says `repos/…/actions/jobs/101115219244/logs` returns **HTTP 404** —
  GitHub has expired it. **So re-running the workflow to "regenerate the log"
  buys a log for a different run and never that one.** The kept pins in
  `.internal/toolchain/` were the only available route to a diagnosis, which is
  the first time the never-delete rule has paid for something other than a
  differential.
- **question Q-8 answered by `nitpick-compiler_s1` within the hour, 2026-09-06
  05:2x: DELIBERATE, not a regression — and the answer unblocks `nitpick-regex`
  0.0.4 rather than merely explaining its red.** `limit<Rules>` went **live** in
  1.5.2 (`5d45bb1`…`0fa414b`, 2026-09-04, squarely between `94874ce` and
  `3d15ac9`; D-251…D-255). The `NITPICK-RUNG-001` refusal retired and a limited
  parameter is now **checked in every build**: a generated predicate runs at the
  callee's entry, a violation traps `LimitViolated` (−4111), and REACH arms it
  for any program carrying a limited binding. The probe therefore compiles *past*
  the construct and REACH refuses at its failsafe. **The probe asked "refused, or
  lowered to nothing?" and the answer is a third thing it did not offer:
  enforced.**
- **finding: the cheap fix would have buried two things, not one.** Editing the
  expectation from `RUNG-001` to `REACH-002` turns the suite green in a minute
  and encodes, invisibly, a guess about which of *deliberate* and *regression*
  was true. It would **also** have preserved a stale comment as a live design
  constraint: `probe13b` asserts that a `limit` and `never fails` are mutually
  exclusive (`TYPE-037`), and that has been false since 1.5.1 (D-241,
  2026-09-03) — a never-fails function may carry `limit`, `requires` and
  `ensures`, since the trap route is a channel a never-fails body already admits.
  **That comment is a design input for `src/core/`, which is exactly what 0.0.4
  builds.** Asking cost one message and forty minutes and returned three measured
  facts, a retired language rule, and a design input the red was hiding. **A red
  suite is sometimes the only thing standing between a library and an obsolete
  premise.**
- **finding, against this session's own work: THE FIRST NUMBER IT PUT ON THE
  BOARD WAS WRONG, AND WRONG BY THE MECHANISM THIS WORKBENCH KEEPS NAMING.** It
  wrote "**23** floor symbols committed and no longer emitted", read off a
  `head -45` of the run log. The log holds **3 668** such lines, because the
  self-check re-runs the build; **23 was simply where the truncation fell.**
  Measured by diffing the committed baseline against the re-recorded one:
  `SYMBOLS.txt` **29 → 2, 27 removed, 0 added**; `EDGES.txt` **237 → 2, 235
  removed, 0 added**. **`EDGES.txt` moves by two orders more than the symbols and
  the first account did not mention it at all** — so the re-record is a 237-line
  review, and anyone sizing that commit off the first sentence would have sized
  it wrong. **A count read off a truncated log is not a measurement.** Corrected
  on the board; recorded here rather than rewritten, because this file is
  append-only.
- **finding: the floor-baseline reading was corroborated from the opposite
  direction and it is the strongest form of agreement available.**
  `nitpick-compiler_s1` compiled a floor-only probe at `3d15ac9`, assembled it
  and read its object: **exactly `npk_dalloc` and `npk_ofd_close`** — the same
  pair this workbench's `--record-baseline` produced, from a different input by a
  different route. **Mechanism: D-262** (1.5.2d step 2, 2026-09-05, in `aaffb87`
  and later; the `94874ce` baseline predates it) — a prelude item is emitted only
  if referenced. **Two measurements that could each have been wrong alone agree
  exactly**, which is what makes this a fact rather than a reading.
- **question Q-1 answered by the author 2026-09-06: ratified as recommended, and
  landed as `W-28` in `WORKSTREAMS.md`.** A committed `REPORT` block is
  immutable — it is evidence, not documentation, and editing it in place destroys
  the record of what was believed at the time; corrections go in a later
  `RECORD.md` entry or in the document that supersedes it. **The rule also
  settles the half that actually bit twice, which is bookkeeping rather than
  principle:** a sweep that finds six sites and edits five reads as *incomplete*,
  so W-28 requires the denominator and the exemption stated together. It reached
  the questions table twice with both dispatches leaving it open.
- **questions Q-2, Q-6 and Q-7 confirmed with the author 2026-09-06 and taken off
  his plate.** Q-2 needs no action and is recorded only so a later session does
  not read a type-shaped gap as an omission. Q-6 — the `nitpick-time` CI pin bump
  to `3d15ac9` — is a clear yes as its own commit, and the orchestrator does it
  when that stream moves. Q-7, CI for the four repositories that have none,
  stands as *fix the shape once, then propagate*: a cycle of its own rather than
  work to squeeze in.
- **finding: HALF OF Q-3 HAD ALREADY BEEN FIXED AND THE QUESTIONS TABLE DID NOT
  KNOW.** The row recommended fixing both guard defects *together* — the
  unjudgeable interpreter heredoc, and the false positive refusing
  `git worktree list` as "a mutating git subcommand". **The second landed in
  `80263a2`**: the guard carries a read-forms table (`"worktree": {"list"}`) and
  a `git_is_read()` test, and the suite passes **86 cases, 41 block / 45 allow,
  exit 0**, covering `git worktree list` as an allow and `worktree add`/`remove`
  as blocks. **Established by running the suite rather than by reading the
  code.** So the two halves did not need to be fixed together, and the open
  question is **narrower than the row claimed**: the suite already blocks the
  *visible* form (a heredoc followed by `rm -rf` on a compiler path), so what
  remains is specifically a write inside an **opaque interpreter payload**.
  **And the mechanism is duller and worse than a lost commit.** `80263a2` landed
  **2026-09-05 12:56**, the *same day* Q-3 was raised, and its commit body says so
  in plain words — *"`git worktree list` is no longer refused as a mutating
  subcommand … thirteen controls, each read form with its write twin."* Nothing
  was hidden. **Nobody re-read the row against the tree.** A questions table does
  not update itself, and **a row that recommends work states an INTENT, not a
  STATE**; between raising it and answering it the tree can already have moved.
  **The eighth orchestrator then relayed this row to the author as an open
  question without checking it**, and he approved a recommendation half of which
  was a day stale. **Re-verify a standing question against the tree before
  putting it in front of anyone** — the same discipline this workbench applies to
  a worker's premises, applied to its own table.
- **finding, self-observed and put on the board as live evidence rather than as
  an argument: this session wrote `RECORD.md` twice through exactly the
  unjudgeable form** (`cat >> … <<'ENTRY'`), inside the repository it was
  authorised to write, so nothing went wrong. **That is the point.** The harness's
  own standing instruction prefers heredocs over `Write`/`Edit`, so the unwatched
  path is the *default* path, and it goes unnoticed precisely because it is
  almost always used legitimately.
