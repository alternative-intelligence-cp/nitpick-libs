#!/usr/bin/env python3
"""Control for reinject_orchestrator.py: prints for the marked session only."""
import json, os, subprocess, sys, tempfile
from pathlib import Path

SCRIPT = str(Path(__file__).with_name("reinject_orchestrator.py"))


def run(libs, sid):
    inp = json.dumps({"hook_event_name": "SessionStart", "session_id": sid, "cwd": libs})
    env = dict(os.environ, NPK_LIBS_DIR=libs)
    return subprocess.run([sys.executable, SCRIPT], input=inp, capture_output=True, text=True, env=env).stdout


def main():
    fails = []
    with tempfile.TemporaryDirectory() as t:
        libs = str(Path(t).resolve())
        cases = [("no marker", None, "sess-A", False)]
        os.makedirs(os.path.join(libs, ".internal"))
        cases += [("marker matches", "sess-A", "sess-A", True),
                  ("marker differs", "sess-A", "sess-B", False),
                  ("empty session id", "sess-A", "", False)]
        for name, marker, sid, should_print in cases:
            if marker is not None:
                Path(libs, ".internal", "orchestrator.session").write_text(marker + "\n")
            out = run(libs, sid)
            printed = "ORCHESTRATOR" in out
            ok = printed == should_print
            print(f"  {'ok ' if ok else 'FAIL'} {name:<18} expected {'block' if should_print else 'silence'}, got {'block' if printed else 'silence'}")
            if not ok:
                fails.append(name)
    print()
    if fails:
        print(f"{len(fails)} FAILURE(S): {', '.join(fails)}")
        return 1
    print("All 4 cases correct.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
