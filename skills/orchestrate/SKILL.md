---
name: orchestrate
description: Assign, gate, merge and record work across the Nitpick ecosystem's three streams. Reads the board, checks whether a dependency is actually closed rather than in progress, merges branches and re-runs the gate on the merged set, rebalances the partition against measured pace, and composes the execution record. Use when deciding what to work on next, when a stream finishes, or when integrating parallel work.
allowed-tools: Bash(git *) Bash(python3 *) Read Edit Grep Glob
---

# Orchestrating

## The role, and its one hard rule

**The orchestrator does not write code.** It holds freeze management,
assignment, integration, record composition and escalation routing — and
nothing else. An orchestrator that also writes code cannot hold the merge and
gate roles cleanly.

> **This skill cannot enforce that.** `disallowed-tools` lasts one turn, not a
> session. The rule is a discipline, and if it needs teeth the mechanism is a
> permission rule in `settings.json`, not skill prose. Say so rather than
> pretending the skill prevents it.

## Assigning

1. Read `BOARD.md`. A repository with no claim is nobody's.
2. Pick the next item in that stream's order from `WORKSTREAMS.md` §3.
3. **Check the gate properly.** A cross-stream dependency must be **closed**,
   not in progress. `nitpick-posix` 0.5 needs `nitpick-regex` *finished*.
4. If the gate is not ready, **do not idle the stream** — take the next
   ungated cycle in the same repository. `nitpick-posix` has nine ungated
   cycles and they exist precisely for this.
5. Write `CLAIMED sN` against the **repository**, not the cycle. Commit it —
   the history of that file is the record of who worked what and when.

## Releasing

Only when the worker's close checklist is complete, including the next
subcycle file being written. Then check whether any `BLOCKED` row just became
available.

## Merging

- **Independently green is not green.** The gate is a full run on the *merged*
  set. Two branches that each pass can fail together, and this ecosystem has
  already paid for that lesson once.
- **A red under parallel load is a stop sign, never a retry.** Every
  timing-shaped defect found here looked like flakiness first. Serialise and
  reproduce.
- Where several branches are ready, build cumulative prefixes — branch 1;
  1+2; 1+2+3 — and run one check per prefix concurrently. All green lands the
  set; a red first appearing at prefix *k* names branch *k*, and the bisect has
  already happened.

## Rebalancing

**Cycle counts are a poor proxy** and `WORKSTREAMS.md` W-4 requires
recalibration after each stream's first closed cycle. Compare measured pace
against the estimate and move a repository between streams if one is starving.
Pretending the initial split was right is how a stream idles for a week.

## Escalating

When a stream reports a compiler defect: **freeze the window, do not let it be
worked around.** Record the reproduction, raise it against the compiler
repository, and have every affected stream rebase once it is fixed.

Anything decision-shaped goes to the author, with a recommendation attached —
not a menu.

## The record

Compose the cross-stream picture that no single stream can see: which findings
recurred, which estimates were wrong and by how much, which gates actually
bound. That is the durable output of orchestrating, and it exists only if
somebody keeps it.

## Files

`WORKSTREAMS.md` is the durable plan; `BOARD.md` is the live state and this
role owns it. Agents working a stream do not edit the board — that removes
every merge conflict on it by construction.
