#!/usr/bin/env python3
"""Control for reinject_orchestrator.py: prints for the marked session only, and
never for a dispatched agent of that session (question 14, 2026-10-01)."""
import json, os, subprocess, sys, tempfile
from pathlib import Path

SCRIPT = str(Path(__file__).with_name("reinject_orchestrator.py"))
GUARD = "IF YOUR PROMPT BEGAN WITH `STREAM:` AND `REPO:`"


def run(libs, sid, agent_id=None):
    payload = {"hook_event_name": "SessionStart", "session_id": sid, "cwd": libs}
    if agent_id is not None:
        payload["agent_id"] = agent_id
    env = dict(os.environ, NPK_LIBS_DIR=libs)
    return subprocess.run([sys.executable, SCRIPT], input=json.dumps(payload),
                          capture_output=True, text=True, env=env).stdout


def main():
    fails = []
    with tempfile.TemporaryDirectory() as t:
        libs = str(Path(t).resolve())
        cases = [("no marker", None, "sess-A", None, False)]
        os.makedirs(os.path.join(libs, ".internal"))
        cases += [("marker matches", "sess-A", "sess-A", None, True),
                  ("marker differs", "sess-A", "sess-B", None, False),
                  ("empty session id", "sess-A", "", None, False),
                  # a subagent carries its PARENT's session id: the 2026-09-30 case
                  ("subagent of marked", "sess-A", "sess-A", "agent-x", False)]
        for name, marker, sid, agent, should_print in cases:
            if marker is not None:
                Path(libs, ".internal", "orchestrator.session").write_text(marker + "\n")
            out = run(libs, sid, agent)
            printed = "ORCHESTRATOR" in out
            ok = printed == should_print
            if printed and not out.startswith(GUARD):   # the second guard must lead the block
                ok = False
            print(f"  {'ok ' if ok else 'FAIL'} {name:<18} expected {'block' if should_print else 'silence'}, "
                  f"got {'block' if printed else 'silence'}{' (guard line first)' if printed and out.startswith(GUARD) else ''}")
            if not ok:
                fails.append(name)
    print()
    if fails:
        print(f"{len(fails)} FAILURE(S): {', '.join(fails)}")
        return 1
    print(f"All {len(cases)} cases correct "
          f"({sum(1 for c in cases if not c[-1])} of them checking it stays quiet).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
