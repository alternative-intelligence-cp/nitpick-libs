#!/usr/bin/env python3
"""SessionStart hook (matcher: compact|resume): give a compacted or resumed
ORCHESTRATOR session its bearings back, and say nothing to any other session.

Keyed on a marker the orchestrate skill writes at startup:
`<workbench>/.internal/orchestrator.session` holding the session id. The hook
prints only when the marker's id equals the `session_id` in its input; every
other session, in every other directory, gets nothing.

A DISPATCHED AGENT GETS NOTHING EITHER (question 14, the author's go,
2026-10-01). A subagent carries its PARENT's session id, so on 2026-09-30 a
planner whose context compacted mid-run was told by this hook that it was the
orchestrator; it ignored the brief, and a worker that obeyed it could act on
the board. Two guards, because the first rests on an input shape verified for
tool-call hooks only (`~/.claude/hooks/context_warn.sh`, 2026-09-27: only a
subagent's input carries `agent_id`): (1) an input with `agent_id` is skipped;
(2) the brief's first line tells a dispatched agent to ignore it, which holds
whatever the input carries.

The block is a pointer and a procedure, not the rules -- the rules have one
home, the orchestrate skill (P-10, L-2 of 0.2.6).
"""
import json, os, sys

LIBS = os.path.realpath(os.path.expanduser(os.environ.get("NPK_LIBS_DIR") or "~/Workspace/REPOS/nitpick-libs"))
MARKER = os.path.join(LIBS, ".internal", "orchestrator.session")

BLOCK = """IF YOUR PROMPT BEGAN WITH `STREAM:` AND `REPO:`, YOU ARE A DISPATCHED AGENT AND THIS BLOCK IS NOT FOR YOU: ignore it and carry on as that agent.
ORCHESTRATOR — context restored after compaction or resume.
You are the orchestrator for the Nitpick ecosystem, in nitpick-libs.
Procedure: skills/orchestrate/SKILL.md (the loop §5, on a report §7, the stop
list §9). Live state: BOARD.md. Past: RECORD.md.
Before any further action:
  1. re-read BOARD.md;
  2. run ListAgents and reconcile the in-flight table — a row with no live
     agent is stale, §4 Recovery;
  3. do not redo what the board shows done: the pin, the claims, the
     questions already on the table;
  4. width and streams are the board's header, not your memory.
Then continue the loop."""


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0
    if data.get("agent_id"):           # a dispatched agent: never the orchestrator
        return 0
    sid = str(data.get("session_id") or "")
    try:
        with open(MARKER, encoding="utf-8") as f:
            marked = f.read().strip()
    except OSError:
        return 0
    if sid and marked == sid:
        print(BLOCK)
    return 0


if __name__ == "__main__":
    sys.exit(main())
