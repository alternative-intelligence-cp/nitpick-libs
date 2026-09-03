# Cycle 0.2 — the system made to run

**Plugin `npk` 0.1.0 → 0.2.0. Status: PLANNED.**

Cycle 0.1 wrote the documents and the skills in one planning session. They
were reviewed on 2026-09-03 with one question: *would this run?* The documents
are strong — the board on disk as the source of truth, skills that carry
procedure rather than content, a guard with false-positive controls, mutual
dogfood gates with a slack rule. The joints between the pieces are not: the
worker skill's paths assume a session started inside a library while workers
are subagents started from the workbench; nothing defines what a worker is
told or what it reports; nothing pins the compiler binary; the workbench has
no writer rule; there is no recovery from a dead session; and the loop has
never run end to end. Probe 02 was run by hand in the planning session.

This cycle fixes the joints, adds the research capability the plans already
assume, and runs the system's own probe: one real subcycle, at width one,
with the pass mark written down first.

**Nothing here changes a library's plan.** The only edits outside this
repository are the mechanical ones the toolchain pin needs (0.2.0 step 5).

---

## Why this shape

- **Paper before mechanism.** The rules and the board schema come first
  (0.2.0), because every later subcycle writes a skill or a script *against*
  them. A skill written before its contract is a skill that will be rewritten.
- **Skills before agents.** An agent definition preloads a skill, so the skill
  has to exist first. Research (0.2.3) precedes the agents (0.2.4) for that
  reason.
- **Enforcement after the thing it enforces.** The guard's claim rule (0.2.5)
  parses the board schema 0.2.0 defines.
- **The dry run is the probe.** 0.2.7 runs one real subcycle through the whole
  loop and judges the *system*, not the subcycle. A pass mark decided in
  advance is what makes a bad result a stop rather than an improvisation.

---

## What the plan rests on

Every fact below was either read from the Claude Code documentation on
2026-09-03, or measured here. A fact marked *docs* was verified by a
documentation lookup and can be re-verified the same way; a fact marked
*measured* has its command in the subcycle that uses it.

| Fact | How established | Used by |
|---|---|---|
| `allowed-tools` in a skill **pre-approves** tools for one turn; it never restricts. Skills have no `disallowed-tools` | docs | P-9, 0.2.4 |
| a subagent has the Skill tool; an agent definition's `skills:` preloads full skill content; its `tools:` list is **exclusive** (anything unlisted is gone) | docs | 0.2.4 |
| subagents can spawn subagents, three levels deep by default | docs | P-14 |
| `context: fork` inherits the **entire** parent conversation | docs | P-9 |
| `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_SESSION_ID}`, `$ARGUMENTS` are real substitutions; arguments with no placeholder are appended as `ARGUMENTS: …` | docs | 0.2.2, 0.2.6 |
| a hook's `cwd` **follows the shell's `cd`**; a hook `deny` applies in bypass-permissions mode; hooks fire for subagents' calls; hook input carries no agent identifier | docs + probe: `mkdir -p ../nitpick/meta` refused in bypass mode; a `cd` out of the project root was reset by the harness | P-15, 0.2.5 |
| hook commands receive `CLAUDE_PROJECT_DIR` | docs | 0.2.5 |
| the Bash tool caps at ten minutes and auto-backgrounds most commands at the cap, but **not `git`** | docs | 0.2.1 |
| `/loop` accepts a plugin skill and can self-pace | docs | 0.2.2 |
| WebFetch truncates large pages, reads PDFs in twenty-page ranges, reports but does not follow a cross-host redirect, caches fifteen minutes; there is no domain rule for WebSearch | docs | 0.2.3 |
| a worker's required reading for `nitpick-regex` 0.0.0 is 104 KB, about 26K tokens | measured: `wc -c` over the read order | P-1 |
| `tools/test_guard.py` has 45 cases; `README.md` and `START.md` say 36 | measured | 0.2.5 |
| the compiler's `build/` holds `npkc` and `npkrt.o`; every library's probe command links `../../nitpick/build/npkrt.o` directly | measured | P-4, 0.2.0 |
| `LIBRARIES.md` says implementation "is deliberately serial — one library at a time", contradicting `WORKSTREAMS.md` | measured | 0.2.0 |
| three decisions (`T-100`, `RX-100`, `TM-100`) pin "the latest release at cycle N" and nothing equips a worker to find out what that is | measured: `grep -rn 'latest' */meta/DECISIONS.md` | P-14 |
| `nitpick-posix` names POSIX.1-2017 throughout and never mentions the 2024 edition | measured | Q-1 |
| the compiler already ran the research → decision-grade digest → ratified-decisions pattern (D-210…D-221) | read: `../nitpick/CLAUDE.md` | P-14 |
| `skills/check/SKILL.md` promises a negative control ("known to catch all six classes") and none exists in the tree; an ad-hoc fixture built by the first flagless test session showed all six classes fire | measured by that session, 2026-09-03 | 0.2.1 step 5b |
| two sessions were writing in the workbench at once with nothing on the board saying so; the second stopped by discipline when a commit landed under it | observed 2026-09-03 | 0.2.0 step 2, 0.2.5 |
| `O-N` ids collide across repositories: `O-N2` is the `npkg` gap in three and something else in three; the workbench references four such ids and defined none | measured: `check_refs.py .` once `meta/OPEN_QUESTIONS.md` existed | 0.2.0 step 1b |

---

## Decisions taken at planning

Each records the alternatives declined, because the alternatives are what a
later reader will propose. The durable ones become `W-` rules in 0.2.0.

- **P-1 — the unit of delegation is the subcycle.** One fresh worker per
  subcycle; the claim covers the repository for the whole cycle; the handoff
  between subcycles is the execution record. *Why:* a cycle can be days of
  work and a context dies; one commit per subcycle already makes the subcycle
  the unit of record. *Declined:* one worker per cycle (context exhaustion;
  uncommitted work lost on death); one long-lived worker fed the next
  subcycle by message (its context grows exactly like one long session).
  *Cost:* about 26K tokens of reading per worker start, measured, and worth
  it because it is also what survives a model swap.
- **P-2 — the workbench repositories have one writer, the orchestrator.**
  Workers, planners, auditors and researchers write nothing under
  `nitpick-libs/` or `nitpick-apps/` roots. Findings for the playbook travel
  in the report. *Why:* W-7, and the compiler's R1 incident, where a second
  writer swept another session's work into its commit. *Declined:* workers
  appending to `PLAYBOOK.md` — three writers in one repository the moment
  width exceeds one.
- **P-3 — workers commit to `main`; nothing is branched, nothing is merged.**
  *Why:* one writer per repository makes a branch redundant, and the
  orchestrate skill's merge section was the compiler's many-writers protocol
  copied into a world with none. *Declined:* a branch per subcycle with an
  orchestrator merge. R3's substance survives as P-7.
- **P-4 — the toolchain is pinned by the orchestrator outside the compiler
  tree, and workers never read `../nitpick/build/`.** *Why:* the guard
  correctly refuses building the compiler from a library session; the compiler
  session rebuilds `build/npkc` under running workers; probe 02 already had to
  copy the binary out. *Declined:* pointing workers at `build/npkc`
  (nondeterministic under a rebuild); building per library (forbidden).
- **P-5 — a claim names the subcycle, the agent label and the time, and a
  claim with no live agent in the current session is stale.** Stale claims are
  recovered by a written procedure before anything is dispatched. *Why:*
  sessions end and contexts compact; the board must carry enough to resume.
  *Declined:* releasing stale claims automatically — it discards the
  dirty-tree evidence a recovery needs.
- **P-6 — a report has one fixed shape and lives in two places:** the
  worker's final message, and the subcycle's execution record, committed.
  `check_record.py` verifies the committed one. *Why:* the loop's decision
  step needs a defined shape; a weaker executor cannot be trusted to
  summarise prose, in either direction. *Declined:* free-form reports; report
  files in the workbench (a worker write into the workbench, P-2).
- **P-7 — release requires independent verification.** A verifier re-runs
  the reference check, the record check, and the harness or probe commands on
  the committed tree; the orchestrator releases only on PASS. *Why:* "green"
  in a report is a claim, and R3 says independently green is not green.
  *Declined:* trusting the report; the orchestrator running the harness itself
  (it fills the orchestrator's context and blocks the loop for the run).
- **P-8 — the audit runs at READY-TO-CLOSE, before a cycle closes.** The
  auditor writes nothing; the orchestrator files the report under
  `meta/audits/`; the close worker triages every finding. An ecosystem-wide
  audit runs after every third cycle close. *Why:* findings found after the
  close land a cycle late; an auditor that writes is a second writer.
  *Declined:* audit after close; the auditor writing its report into the
  repository.
- **P-9 — roles are plugin agent definitions** with preloaded skills and
  explicit tool lists, and the orchestrator delegates by agent type.
  `context: fork` is not used. *Why:* `allowed-tools` never restricts and
  agent definitions do; preloading removes "load the skill first" from every
  prompt and removes the failure where a worker never loads it. *Declined:*
  fork — it inherits the orchestrator's whole context, the expensive path
  `START.md` already rejected.
- **P-10 — the loop and the stop list have one home, the orchestrate skill.**
  `START.md` becomes a one-line invocation with arguments, and a session-start
  hook re-injects the orchestrator's rules after compaction, keyed on a marker
  file so every other session is untouched. *Declined:* relying on the pasted
  prompt surviving compaction.
- **P-11 — a stop condition stops its stream, not the loop.** Questions are
  batched with a recommendation each; the author is notified when every
  running stream is stopped, when the batch reaches three items, or four
  hours after the first unanswered item. *Declined:* stopping everything
  (idles two streams for one question); asking one at a time.
- **P-12 — width is an argument, default one.** A stream never has more than
  one worker; helper agents — verifier, auditor, researcher, planner — do not
  count against width, and at most one of each runs at a time. *Why:* the
  number of concurrent agents is a dial, and the plan degrades to one.
- **P-13 — attribution is passed verbatim by the orchestrator from its own
  harness notice; a skill never names a model; every report records the model
  that executed.** *Why:* the executing model cannot be guaranteed, and a
  hardcoded name misattributes every commit made by a different one.
- **P-14 — research is a skill plus a researcher agent.** One fetch may be
  inline; more goes to the researcher. The researcher never writes into a
  repository: the requesting writer files the digest under `meta/research/`
  with the date checked, and a decision cites the digest. A security-sensitive
  digest is stale after ninety days. Language facts are never researched on
  the web — the compiler tree is the only source. *Why:* three decisions
  already require a lookup; the agent that has the question should write it,
  and the agent that fetches should not carry the pages back. *Declined:*
  inline research only (fetched pages in the worker's context); the
  researcher writing digests (a second writer in a claimed repository); no
  research.
- **P-15 — the guard self-scopes on the session's project directory, not the
  per-call working directory, and enforces claims:** a write into a library or
  application repository from outside it is refused unless the board shows
  the repository claimed. It stays in `~/.claude/settings.json`, not the
  plugin, so a session started without the plugin is still guarded.
  *Declined:* moving the guard into the plugin's hooks.
- **P-19 — the workbench names its writer on the board.** The board header
  carries `Workbench writer:` — a session id and a time, or `none`. The
  orchestrate skill sets it at startup and clears it at a clean stop; an
  author's session executing a plan sets it by hand. Any other session that
  finds a writer named does not write here. The guard enforces it from 0.2.5
  by comparing the hook's session id. *Why:* the first flagless test session
  found a commit landing under it and had nothing but discipline to go on.
  *Declined:* claiming the workbench in the stream tables (it is not a
  stream's repository).
- **P-16 — three status vocabularies, each defined once.** A subcycle file's
  title line: `PLANNED`, `RUNNING (since <date>, sN)`, `DONE (<date>)`. A
  report: `DONE`, `READY-TO-CLOSE`, `BLOCKED`, `STOPPED`, `NEEDS-DECISION`,
  `RED`. A board row: `—`, `CLAIMED sN`, `BLOCKED on <cycle>`, `DONE`; the
  informal `READY` is dropped. *Why:* the posix probe file says `PLANNED` with
  an empty execution record after it ran.
- **P-17 — models per role.** Worker, planner, auditor and researcher inherit
  the orchestrator's model; the verifier may run on a smaller one; the
  orchestrator may override per dispatch; the report records what ran.
- **P-18 — repository creation is never delegated.** It is outward-facing and
  edits the registry, so the orchestrator or the author runs `/npk:new-repo`.

---

## Subcycles

| # | Topic | Ends with |
|---|---|---|
| [0.2.0](0.2.0.md) | **The rules and the board** — W-15…W-26, the board schema, `RECORD.md`, the toolchain edits in each repository | the contracts every later subcycle is written against |
| [0.2.1](0.2.1.md) | **The worker skill**, rewritten for delegation; `check_record.py` and its control | a worker that can be dispatched from the workbench and a report that can be checked mechanically |
| [0.2.2](0.2.2.md) | **The orchestrate skill** — the loop, the stop list, dispatch, pinning, recovery, escalation; `START.md` as one line | an orchestrator that can start, resume and stop by rule |
| [0.2.3](0.2.3.md) | **Research** — the skill, the request and digest shapes, the currency items in plan and audit | the capability three decisions already assume |
| [0.2.4](0.2.4.md) | **The agent definitions** — worker, planner, auditor, verifier, researcher | delegation by agent type, tools explicit |
| [0.2.5](0.2.5.md) | **The guard** — project-directory scoping, `cd` anywhere, claim enforcement, no home paths | the claim protocol as a mechanism |
| [0.2.6](0.2.6.md) | **Survival** — the compaction hook, the workbench `CLAUDE.md`, flagless loading, the manifest | an orchestrator that outlives its context window |
| [0.2.7](0.2.7.md) | **The dry runs, and close** — width one on one real subcycle, then width two; the findings; 0.2.0 shipped | the system has run, and what it cost is a number |

---

## Checklist

- [x] 0.2.0 — `W-15`…`W-26` in `WORKSTREAMS.md`; `BOARD.md` on the new schema; `RECORD.md` exists; `LIBRARIES.md` no longer says serial; six repositories use `$NPKC`/`$NPKRT`; `check_refs` clean everywhere
- [x] 0.2.1 — worker skill takes `REPO`; every path absolute; every git command `git -C`; the REPORT block defined; `check_record.py` passes its control
- [x] 0.2.2 — orchestrate skill has the loop, the stop list, the dispatch template, the pin procedure, the recovery procedure, the escalation rule, `tick`; `START.md` is one line plus arguments
- [x] 0.2.3 — `skills/research/SKILL.md`; request and digest shapes; currency items in `plan`; external claims in `audit`; the inline threshold in `worker`
- [ ] 0.2.4 — five agent definitions; each preloads its skill; web tools listed where needed; names confirmed in a live session — **files done; live tests pending**
- [x] 0.2.5 — guard scopes on `CLAUDE_PROJECT_DIR`; the `cd`-then-write case blocked; claim enforcement with fixture boards; no `/home/` in a tracked file; docs no longer carry a case count
- [ ] 0.2.6 — `hooks/hooks.json` with the compaction re-injection; `CLAUDE.md` at the workbench root; the plugin loads without `--plugin-dir`; manifest at 0.2.0 — **done but the live compaction test; version bump waits for 0.2.7**
- [ ] 0.2.7 — dry run one passed its pass mark; dry run two passed or its failure is a recorded finding; measurements recorded; cycle closed to `done/`

## Gate

**The cycle is complete when** dry run one (width one, `nitpick-time` 0.0.0)
passes every item of its pass mark as written in [0.2.7](0.2.7.md) §2 *before
the run*; every check script in the repository passes its own control; the
plugin loads in a session started without `--plugin-dir`; and the measured
cost of one subcycle through the loop — wall-clock, worker tokens,
orchestrator context growth — is a number in this repository.

## Watch for

- **`.gitignore`'s `/*/` swallows every new top-level directory.** `meta/`,
  `agents/` and `hooks/` are un-ignored by name already; anything else added
  at the root must be too, or it vanishes silently — which is how the plugin
  was lost on its first commit.
- **An agent definition's `tools:` list is exclusive.** Omit `WebFetch` and
  research silently disappears; omit `Agent` and a worker cannot dispatch a
  researcher; omit `Skill` and it cannot load anything it was not preloaded
  with.
- **The skill name in an agent's `skills:` field may need the plugin
  namespace.** 0.2.4 tests both spellings and records which one works.
- **`git` commands are not auto-backgrounded at the Bash cap.** A long
  `git` operation must be run in the background explicitly.
- **Tracked files may not carry an absolute home path.** The board records
  the pin as a relative path; the worker prompt, which is not tracked,
  carries the absolute one.
- **A heredoc that mentions the compiler tree is data, not a write.** The
  guard strips heredocs; a rewrite of the guard must keep that test green.
- **The harness reset the shell's directory on leaving the project root.**
  That is harness behaviour, not the guard's, and 0.2.5 stops depending on it.

## Execution record

*(appended as subcycles close)*
