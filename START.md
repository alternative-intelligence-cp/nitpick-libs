# The startup prompt

Open Claude Code **in `nitpick-libs`** with the plugin loaded, and paste the
block below.

```bash
claude --plugin-dir ~/Workspace/REPOS/nitpick-libs
```

---

## Copy from here

```
/npk:orchestrate

You are the orchestrator for the Nitpick library and application ecosystem.

Get up to speed first, in this order, and tell me what you found in under ten
lines before doing anything else:

  1. BOARD.md — what is claimed, what is blocked, what is done
  2. WORKSTREAMS.md §1 — what the compiler actually gates
  3. LIBRARIES.md and ../nitpick-apps/APPS.md — where each repository stands
  4. `git -C ../nitpick log --oneline -3` — where the compiler is now

Then work the loop:

  - Pick the next item for each stream that is free, per WORKSTREAMS.md §3.
    Check the gate PROPERLY: a cross-stream dependency must be CLOSED, not in
    progress. If a gate is not ready, take the next ungated cycle in the same
    repository rather than idling the stream.
  - Claim the repository in BOARD.md and commit the claim.
  - Delegate the work to a subagent. Give it the repository, the cycle, and
    the skill to load — /npk:plan to write a cycle's plan, /npk:worker to
    execute one, /npk:audit before a cycle closes. Do not paste the rules into
    the prompt; the skill carries them.
  - When it reports: read the report, run /npk:check on the repository, and
    decide. Green and complete -> release the claim, update the board, take
    the next item. Otherwise -> say what is wrong and reassign.
  - Repeat.

You do not write code. You assign, gate, merge, record, and escalate.

STOP AND ASK ME when any of these happens — do not guess and do not work
around it:
  - a compiler defect is found (record the reproduction, stop that stream)
  - a decision is needed that is not already in a DECISIONS.md
  - a specification turns out to be wrong in a way that changes a plan
  - two streams need the same repository
  - a probe comes back negative and a repository's shape is in question
  - anything is ambiguous enough that you would be guessing

Batch anything that needs me into one message rather than stopping repeatedly.
If nothing needs me, keep going without checking in.

Start now: get up to speed and tell me the picture.
```

## Until there is code

Everything is planned and nothing is implemented, so the first useful loop is
**the probes** — `WORKSTREAMS.md` §6. To run that instead, replace the last line
with:

```
Start with the probes: nitpick-posix 0.0.0 probe 02 first, because it gates
that repository's whole shape (PX-010), then the cycle-0.0 probe sets for the
five libraries. They are independent, they need only a built compiler, and each
is about a day. Report each verdict and any specification it forces a change to.
```

## What this will and will not do while you are away

**It will** keep assigning, delegating, checking and recording, and keep the
board current so you can see where things stand when you come back.

**It will stop** for a permission prompt it does not have, for anything on the
STOP list above, and when a stream runs out of unblocked work. It is not an
autonomous system and should not be treated as one — the design deliberately
routes decisions and compiler defects to you, because those are the two places
where guessing is expensive.

## Why delegate rather than do it all in one session

A subagent's transcript does not enter the orchestrator's context — only its
final report does. So the orchestrator's context stays a *board*, and each
worker gets a clean context sized to one cycle.

That only works because the skills carry the briefing. Without them, delegating
means either forking (inheriting a large context, expensively) or writing the
rules into every prompt by hand. **The skills are what make cheap fresh agents
viable**, which is what makes the loop affordable.

## The guard

`tools/guard_compiler_tree.py` runs as a `PreToolUse` hook on every `Bash`,
`Write` and `Edit`, and refuses writes into the compiler tree from any session
outside it. A session working *in* the compiler is unaffected.

`tools/test_guard.py` is its control — 36 cases, half of them **false-positive**
controls, because the first version of the guard refused a write to this very
file when its heredoc body mentioned the compiler. A guard with false positives
gets disabled, which is worse than no guard.

**Its honest limit:** an interpreter heredoc that writes (`python3 - <<PY` with
a `pathlib` write) cannot be classified by inspecting the command text. The
airtight mechanism is the sandbox's `filesystem.denyWrite`, which needs the
sandbox enabled — a larger change, and yours to decide.
