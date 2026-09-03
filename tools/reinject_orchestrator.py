#!/usr/bin/env python3
"""SessionStart hook (matcher: compact|resume): give a compacted or resumed
ORCHESTRATOR session its bearings back, and say nothing to any other session.

Keyed on a marker the orchestrate skill writes at startup:
`<workbench>/.internal/orchestrator.session` holding the session id. The hook
prints only when the marker's id equals the `session_id` in its input; every
other session, in every other directory, gets nothing.

The block is a pointer and a procedure, not the rules -- the rules have one
home, the orchestrate skill (P-10, L-2 of 0.2.6).
"""
import json, os, sys

LIBS = os.path.realpath(os.path.expanduser(os.environ.get("NPK_LIBS_DIR") or "~/Workspace/REPOS/nitpick-libs"))
MARKER = os.path.join(LIBS, ".internal", "orchestrator.session")

BLOCK = """ORCHESTRATOR — context restored after compaction or resume.
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
