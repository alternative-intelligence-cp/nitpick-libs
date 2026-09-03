#!/usr/bin/env python3
"""Negative AND false-positive control for guard_compiler_tree.py.

The false-positive half exists because the first version of the guard failed
it: a heredoc whose BODY mentioned the compiler tree was refused, even though
the write targeted another repository. A guard with false positives gets
disabled, which is worse than no guard -- so both halves are required.
"""
import json, subprocess, sys
from pathlib import Path

GUARD = str(Path(__file__).parent / "guard_compiler_tree.py")
LIBS = "/home/randy/Workspace/REPOS/nitpick-libs"
TUI = LIBS + "/nitpick-tui"
COMP = "/home/randy/Workspace/REPOS/nitpick"

# (tool, cwd, payload, should_block)
CASES = [
    # --- MUST BLOCK: real writes into the compiler tree -------------------
    ("Bash", LIBS, "echo x > ../nitpick/meta/specs/DECISIONS.md", True),
    ("Bash", LIBS, "sed -i 's/a/b/' /home/randy/Workspace/REPOS/nitpick/CLAUDE.md", True),
    ("Bash", LIBS, "rm -rf ../nitpick/build", True),
    ("Bash", LIBS, "cp notes.md ../nitpick/meta/", True),
    ("Bash", LIBS, "git -C ../nitpick commit -am oops", True),
    ("Bash", LIBS, "touch ../nitpick/newfile", True),
    ("Bash", LIBS, "mkdir -p ../nitpick/meta/newdir", True),
    ("Bash", LIBS, "chmod +x ../nitpick/tools/thing.py", True),
    ("Bash", LIBS, "cat foo >> ~/Workspace/REPOS/nitpick/notes.txt", True),
    ("Bash", TUI,  "mv x ../../nitpick/y", True),
    ("Bash", LIBS, "cd ../nitpick && rm -rf build", True),     # cd-shifted target
    ("Bash", LIBS, "dd if=/dev/zero of=../nitpick/x bs=1", True),
    ("Write", LIBS, "../nitpick/meta/specs/DECISIONS.md", True),
    ("Edit",  TUI,  "../../nitpick/src/main.npk", True),
    ("Edit",  LIBS, "/home/randy/Workspace/REPOS/nitpick/CLAUDE.md", True),

    # --- MUST ALLOW: reads and inspection ---------------------------------
    ("Bash", LIBS, 'grep -rn "SIGPIPE" ../nitpick/runtime/npkrt.ll', False),
    ("Bash", LIBS, "cat ../nitpick/meta/specs/DECISIONS.md | head -50", False),
    ("Bash", LIBS, "cd ../nitpick && git log --oneline -3", False),
    ("Bash", TUI,  "git -C ../../nitpick status --short", False),
    ("Bash", LIBS, "ls ../nitpick/src/frontend/", False),
    ("Bash", LIBS, "python3 tools/check_refs.py . nitpick-tui", False),
    ("Bash", LIBS, "find ../nitpick -name '*.npk' | head", False),
    ("Bash", LIBS, "diff ../nitpick/CLAUDE.md /tmp/old.md", False),

    # --- MUST ALLOW: writes elsewhere, incl. ones DESCRIBING the compiler --
    ("Bash", LIBS, "git add -A && git commit -m 'note about ../nitpick'", False),
    ("Bash", LIBS, "sed -i 's/a/b/' nitpick-tui/README.md", False),
    ("Bash", LIBS, "cat > START.md <<'EOF'\nthe compiler at ../nitpick is read-only\nrun: rm -rf ../nitpick/build\nEOF", False),
    ("Bash", LIBS, "echo 'see ../nitpick/meta' > PLAYBOOK.md", False),
    ("Bash", LIBS, "mkdir -p nitpick-tui/meta/roadmap/0.1", False),
    ("Bash", LIBS, "rm -rf nitpick-parse/build", False),
    ("Write", LIBS, "PLAYBOOK.md", False),
    ("Write", LIBS, "../nitpick-apps/APPS.md", False),
    ("Edit",  TUI,  "meta/DECISIONS.md", False),

    # --- MUST ALLOW: the compiler's own session ---------------------------
    ("Bash",  COMP, "sed -i s/a/b/ src/main.npk", False),
    ("Bash",  COMP + "/src", "echo x > frontend/lexer.npk", False),
    ("Bash",  COMP, "git commit -am '1.5.1'", False),
    ("Edit",  COMP, "src/main.npk", False),
]


def run(tool, cwd, payload):
    key = "command" if tool == "Bash" else "file_path"
    inp = json.dumps({"tool_name": tool, "cwd": cwd, "tool_input": {key: payload}})
    out = subprocess.run([sys.executable, GUARD], input=inp,
                         capture_output=True, text=True).stdout.strip()
    return bool(out)


def main():
    fails = []
    for tool, cwd, payload, should in CASES:
        got = run(tool, cwd, payload)
        mark = "ok " if got == should else "FAIL"
        if got != should:
            fails.append((tool, payload, should, got))
        label = "block" if should else "allow"
        one = payload.replace("\n", "\\n")
        print(f"  {mark} [{label}] {tool:<6} {one[:66]}")
    print()
    if fails:
        print(f"{len(fails)} FAILURE(S):")
        for tool, p, should, got in fails:
            print(f"  {tool} {p!r}: expected {'block' if should else 'allow'}, "
                  f"got {'block' if got else 'allow'}")
        return 1
    print(f"All {len(CASES)} cases correct "
          f"({sum(1 for c in CASES if c[3])} block, "
          f"{sum(1 for c in CASES if not c[3])} allow).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
