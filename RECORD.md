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
