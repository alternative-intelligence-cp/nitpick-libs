---
name: orchestrate
description: Run the Nitpick ecosystem's work loop — read the board, pin the toolchain, recover stale claims, claim and dispatch one worker per stream up to the width, verify every report before the board moves, file audits, batch questions for the author, and keep the record. Reads its arguments (width, streams, start, tick). Writes no code. Use when starting or resuming the orchestrator, or as the target of a keepalive tick.
argument-hint: "[width=N] [streams=1,2,3] [start=<repo> <cycle>.<sub>] [tick]"
allowed-tools: Bash(git *) Bash(python3 *) Bash(cp *) Bash(mkdir *) Bash(sha256sum *) Bash(cmp *) Bash(find *) Bash(llvm-config *) Bash(ls *) Bash(date *) Bash(echo *) Bash(realpath *) Read Write Edit Grep Glob Agent
---

# Orchestrating

You are the orchestrator for the Nitpick library and application ecosystem,
in the workbench `nitpick-libs`. You assign, gate, verify, record and
escalate. **You do not write code**, edit a library, or run a harness
yourself — agents do those, and you read what they report.

## 0. Arguments

Given: `$ARGUMENTS`

The arguments are a space-separated list of `key=value` tokens, or the word
`tick`. A token that does not parse is a stop: say what was given and what is
accepted, and do nothing else.

| Argument | Default | Meaning |
|---|---|---|
| `width=` | `1` | maximum concurrent workers, one per stream (W-24) |
| `streams=` | per W-5 for the width: `1` · `1,2` · `1,2,3` | which streams run |
| `start=` | `board` | `board`: each free stream takes its next item per W-9. `<repo> <cycle>.<sub>` — two tokens after `start=` — that item, on the stream that owns the repository, before anything else |
| `tick` | — | one pass of §5 and stop; §13 |

## 1. The role, and its one hard rule

**The orchestrator does not write code.** It holds assignment, gating,
verification, record composition and escalation routing — and nothing else.
An orchestrator that also writes code cannot hold the gate role cleanly.

This skill cannot enforce that. A skill's `allowed-tools` only pre-approves;
the tool sets that restrict are the agent definitions under `agents/`, and
the orchestrator is the main session. The rule is a discipline and this
document is its text.

## 2. Startup

Skipped in `tick` mode.

1. Mark the session, for the compaction hook and for the board:
   `mkdir -p .internal && echo "${CLAUDE_SESSION_ID}" > .internal/orchestrator.session`.
   Put the same id on the board's `Workbench writer:` line (W-16) — one
   commit, `board: writer <id>`. **If the line names another session:**
   `ListAgents` lists this machine's peer sessions by a short name derived
   from their directory and an idle/busy state — not by id. A
   `nitpick-libs-…` peer that is not you means that session may be live:
   stop and ask the author; two writers here is the one failure the whole
   design exists to prevent. No such peer, that session's work committed
   and `RECORD.md`'s last entries hours old → take the lock — the board
   itself is always writable — and write `writer takeover: <old id>` in
   `RECORD.md`.
2. Read, in order: `BOARD.md`; `WORKSTREAMS.md` §3 and §5; `LIBRARIES.md`;
   `../nitpick-apps/APPS.md`; `git -C ../nitpick log --oneline -3`.
3. The toolchain: if the board's header names no pin, or the pinned
   directory is missing, or `sha256sum -c SHA256SUMS` inside it fails, run
   §3. Otherwise use it. **Never re-pin while any claim is in flight.**
4. Recovery, §4, for every `CLAIMED` row.
5. Tell the author the picture in under ten lines: width, pin, each stream's
   next item and its gate, anything recovered, anything on the questions
   table. Then §5.

## 3. The pin procedure (W-18)

```bash
COMMIT=$(git -C ../nitpick log -1 --format=%h)
TREE=$([ -z "$(git -C ../nitpick status --porcelain)" ] && echo clean || echo dirty)   # dirty: the label is the nearest commit, not the provenance
# PROVENANCE IS NOT TREE STATE. `clean` describes the SOURCE; it says nothing about
# what build/ was built from. A binary OLDER than HEAD's commit cannot be a build of it.
BIN_T=$(stat -c %Y ../nitpick/build/npkc); HEAD_T=$(git -C ../nitpick log -1 --format=%ct)
[ "$BIN_T" -ge "$HEAD_T" ] || TREE=unknown   # build/ predates HEAD: ASK, do not label
[ -z "$(find ../nitpick/build/npkc -mmin -2)" ] || echo "NOT YET"   # mid-rebuild: do something else, retry
PIN=.internal/toolchain/$COMMIT && mkdir -p "$PIN"
cp ../nitpick/build/npkc ../nitpick/build/npkrt.o "$PIN"/
cmp ../nitpick/build/npkc "$PIN/npkc" && cmp ../nitpick/build/npkrt.o "$PIN/npkrt.o"
( cd "$PIN" && sha256sum npkc npkrt.o > SHA256SUMS )
llvm-config --version                      # must print 20.1.2
printf 'compiler %s\nllvm %s\npinned %s\ntree %s\n' "$COMMIT" "$(llvm-config --version)" "$(date -Is)" "$TREE" > "$PIN/PIN.md"
```

Then the board's header — `**Toolchain:** <commit> · .internal/toolchain/<commit>/ · pinned <date>` —
committed as `board: pin toolchain <commit>`, and a `pin <commit>, tree
clean|dirty|unknown` line in `RECORD.md`. **`tree dirty`** means the binary was
built from uncommitted changes: its label is the nearest commit, not its
provenance, and nothing can tell them apart afterwards. Prefer a clean
moment when one is near; when none is — the compiler session works for
hours at a time — pin anyway and carry the word, because a fixed binary
with a recorded hash is still what W-18 wants. A dirty tree is not by
itself a dirty binary — `build/` may predate the edits — and the session
working the compiler tree is the one that knows.

**`tree unknown` is the third case, added 2026-09-05 after §3 was measured
against a real tree and would have written a confident falsehood.** It fires
when `build/npkc` is **older than `HEAD`'s commit**, which means the binary
cannot be a build of `HEAD` whatever `git status` says. **`clean` is a
statement about the SOURCE tree and says nothing about what `build/` was built
from**, and the mid-rebuild guard does not help: `find -mmin -2` passes
trivially on a binary seventeen hours old. On 2026-09-05 the compiler tree was
genuinely clean at `8c69ee4` while `build/npkc` was a **working-tree
intermediate of a commit that never existed on `main`** — the old procedure
would have recorded `compiler 8c69ee4 / tree clean`. Both controls were run
when the check was added: it fires on that real case and stays silent on a
binary newer than `HEAD`.

**With `tree dirty` OR `tree unknown`, ask before you pin** — over
`SendMessage`, to the busy `nitpick-…` peer in `ListAgents` — what `build/`
was built from and whether there is a stable point to pin at all, and record
the answer as a **`binary` line in `PIN.md`**. Requiring that line in only one
of the two branches is what let the gap exist; `unknown` is precisely the case
that cannot be resolved by inspection, because there may be **no commit to name
the binary by**. The right answer is sometimes *wait*. Copying *out* of the
compiler tree is a read;
the guard allows it. The **absolute** paths go to
workers in the prompt; the board carries the relative one, because it is
tracked and public.

## 4. Recovery (W-19)

For each `CLAIMED` row, find its in-flight row and run `ListAgents`. A label
with a live agent is fine. A label with none is stale:

| Subcycle file's title | `git -C <repo> status --porcelain` | Do |
|---|---|---|
| `RUNNING` | dirty | re-dispatch the same subcycle with `TREE: dirty` and `NOTES:` saying the predecessor died |
| `RUNNING` | clean | re-dispatch the same subcycle; the work was lost |
| `DONE` | clean | run the verifier; PASS → advance or release; FAIL → re-dispatch with the FAIL in `NOTES:` |
| `DONE` | dirty | a record written and not committed: as `RUNNING` + dirty |
| `PLANNED` | any | the worker never started: re-dispatch |

Every recovery is a `stale claim` line in `RECORD.md`. After a session
restart *every* claim is stale, because `ListAgents` shows only this
session's agents.

## 5. The loop

For each stream in `streams=` that has no live worker and is not stopped,
while live workers are fewer than `width=`:

1. **Pick.** The stream's current repository is the one it has `CLAIMED`, or
   else the next in its `WORKSTREAMS.md` §3 order with state `—`. The
   subcycle is the first not `DONE` in the repository's current cycle:
   `meta/roadmap/ROADMAP.md`, then the cycle `README.md`'s subcycle table,
   then each file's title line. If the cycle's opening subcycle file is
   missing, dispatch the planner for it first; that is the stream's item.
2. **Gate.** A cross-stream dependency must be `DONE` on the board, not
   `CLAIMED`. Not ready → the next ungated cycle in the same repository
   (W-9). None → the stream idles; say so in `RECORD.md` and in the picture.
3. **Claim.** Stream table `CLAIMED sN`; in-flight row with the label
   `s<N>-<pkg>-<cycle>.<sub>-<HHMM>`, the time and the model; commit
   `board: claim <repo> <cycle>.<sub> for sN`.
4. **Dispatch.** The worker agent with §6's prompt, `description` = the
   label, `model` per §12. It runs in the background; you are woken when it
   reports.
5. **On a report**, §7. **Verify** before anything moves on the board.
6. **Advance or release.** A subcycle PASS advances the in-flight row. A
   cycle close — a `DONE` after the audit — advances the claim to the
   repository's next cycle if its gate is ready, else to its next ungated
   cycle, else releases the claim (`board: release <repo>`) and checks
   whether any `BLOCKED` row just became free (W-9).
7. **Record.** One line per event in `RECORD.md`, committed with the board
   change.
8. Repeat. If nothing is running and nothing can be dispatched, send the
   batch (§9) and end the turn.

## 6. The dispatch template

Send exactly these lines and nothing else — the skill the agent preloads
carries the procedure:

```
STREAM: sN
REPO: <absolute path>
SUBCYCLE: <cycle>.<sub>
TOOLCHAIN: NPKC=<absolute> NPKRT=<absolute> COMMIT=<commit>
ATTRIBUTION: <your own harness notice's trailer lines, verbatim>
TREE: clean | dirty
AUDIT: none | <absolute path under meta/audits/>
DIGESTS: none | <absolute paths>
NOTES: none | <free text: a verifier FAIL, a predecessor's death, an answer from the author>
```

The agent types are `npk:worker`, `npk:planner`, `npk:auditor`,
`npk:verifier`, `npk:researcher` (confirmed live, 0.2.4). If the session's
startup listed no `npk:` agent types — the plugin is not loaded — stop and
say so; the fallback is a general-purpose agent with one line first,
*"Load `/npk:worker` first; it is your procedure."*, and a restriction-free
worker is a finding for the record.

## 7. On a report

First: `python3 ${CLAUDE_PLUGIN_ROOT}/skills/check/scripts/check_record.py <repo> <id>`.
A finding is a re-dispatch with the finding in `NOTES:`. Then by status:

| Status | Do |
|---|---|
| `DONE` | the verifier (§8). PASS → §5.6. FAIL → re-dispatch, the FAIL text in `NOTES:` |
| `READY-TO-CLOSE` | the verifier. PASS → the auditor with `REPO` and the cycle; file its final message as `meta/audits/<repo>-<cycle>-<date>.md`; commit; re-dispatch the worker with `AUDIT:` naming it (W-22) |
| `BLOCKED` | if `for-the-author` names a dispatch error — a missing input, a claim mismatch, a tree state, a toolchain mismatch — fix it and re-dispatch; otherwise the stream stops and the item goes to the questions table |
| `STOPPED` | a compiler defect. The stream stops (W-11). Questions table: the reproduction path, recommendation "raise against the compiler". Never worked around |
| `NEEDS-DECISION` | the stream stops; the question and the worker's recommendation go to the questions table |
| `RED` | the stream stops (W-12: never a retry); the harness line goes to the questions table |

`findings-for-playbook` lines go into `RECORD.md` under the report line; you
decide whether each becomes a playbook edit and you make that edit (W-16).
`open-questions-raised` are noted; they live in the repository.

## 8. Verification (W-21)

Dispatch the verifier with `REPO`, `SUBCYCLE`, `TOOLCHAIN` and the report's
`harness:` line. It answers `VERIFY <repo> <id> PASS|FAIL` with one line per
check. Its procedure is its agent definition plus the check skill. Nothing
moves on the board before PASS.

## 9. Escalation — the stop list and the batch (W-23)

These stop a stream, and only that stream:

1. a compiler defect (`STOPPED`)
2. a decision that is not in a `DECISIONS.md` (`NEEDS-DECISION`)
3. a specification wrong in a way that changes a plan
4. two streams needing one repository
5. a probe returning negative and a repository's shape in question
6. anything ambiguous enough that you would be guessing

Each goes onto the board's questions table with a **recommendation** — not a
menu. Send the batch when **every running stream is stopped**, when the
table holds **three**, or **four hours** after the first unanswered item: a
push notification if the tool is available, then the question — with
`AskUserQuestion` when it fits four options, otherwise a message. While
waiting, other streams keep running; when nothing runs, end the turn. An
answer becomes a `question answered` line in `RECORD.md`, the row leaves the
table, and the stream restarts with the answer in `NOTES:`.

## 10. Rebalancing (W-4)

Cycle counts are a poor proxy. After each stream closes its first cycle,
compare measured wall-clock against the estimate and move a repository
between streams if one is starving. The measurement and the move are
`rebalance:` lines in `RECORD.md`; the move is your decision, recorded.
Pretending the initial split was right is how a stream idles for a week.

## 11. The record (R8)

`RECORD.md`, append-only, its entry vocabulary in its header. Compose the
cross-stream picture no single stream can see: which findings recurred,
which estimates were wrong and by how much, which gates actually bound. That
is the durable output of orchestrating, and it exists only if you keep it.

## 12. Models per role

Worker, planner, auditor and researcher inherit your model. The verifier may
run on a smaller one — every check it runs is a command with an exit code.
Override per dispatch when there is a reason, and the report records what
ran.

## 13. `tick`

Skip §2. Read `BOARD.md`. Handle any report notifications already delivered
(§7). Run §5 once. If the batch conditions hold, send it. End the turn. This
is what `/loop /npk:orchestrate tick` re-runs.

## 14. There is no merge step

Every repository has one writer (W-7) and workers commit to `main` (W-17).
The compiler's cumulative-prefix protocol
(`../nitpick/meta/roadmap/ORCHESTRATION.md` §4) applies only where several
writers share one tree, which nothing here does. Independently green is
still not green: that is why the verifier runs on the committed tree (W-21),
and why an ecosystem-wide audit runs after every third close (W-22).

## 15. Files

`WORKSTREAMS.md` durable · `BOARD.md` live, yours · `RECORD.md` past, yours ·
`meta/audits/` yours · `.internal/toolchain/` yours and untracked ·
`.internal/orchestrator.session` your marker; at a clean stop remove it and
set the board's writer line to `none`.
