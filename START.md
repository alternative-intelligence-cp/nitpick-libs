# Starting the orchestrator

In `nitpick-libs`, with the plugin loaded — it loads from
`~/.claude/skills/npk` without a flag; `claude --plugin-dir ~/Workspace/REPOS/nitpick-libs`
is the fallback, never both:

    /npk:orchestrate width=1

Arguments: `width=1|2|3` (default 1) · `streams=1,2` (default per W-5) ·
`start=<repo> <cycle>.<sub>` · `tick`. Optional keepalive once the loop is
running: `/loop /npk:orchestrate tick`.

The loop, the stop list, the dispatch template, the pin, the recovery and the
escalation rule are all in `skills/orchestrate/SKILL.md`. There is nothing
else to paste.

## What this will and will not do while you are away

**It will** keep claiming, dispatching, verifying and recording, and keep the
board current so you can see where things stand when you come back.

**It will stop a stream** — and only that stream — for anything on the stop
list, and it will stop altogether when no stream can proceed or when a
permission prompt it does not have blocks it. It is not an autonomous system
and should not be treated as one: decisions and compiler defects are routed
to you on purpose, because those are the two places where guessing is
expensive.

## The guard

`tools/guard_compiler_tree.py` runs as a `PreToolUse` hook on every `Bash`,
`Write` and `Edit`. It refuses writes into the compiler tree from any session
outside it, writes into a library or application the board does not show
claimed, and writes into the workbench by any session but the one the board
names as its writer — the board itself excepted, because it is the lock.
`tools/test_guard.py` is its control; it prints its case count, and more than
a third of the cases are false-positive controls, because a guard with false
positives gets disabled — which is worse than no guard.
