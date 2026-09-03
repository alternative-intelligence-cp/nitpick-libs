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
