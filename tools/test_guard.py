#!/usr/bin/env python3
"""Negative AND false-positive control for guard_compiler_tree.py.

Runs the guard against a FIXTURE built in a temporary directory -- a compiler
tree, a library workbench with two claimed and two unclaimed repositories, an
application workbench -- with the guard's paths and the session's project
directory supplied through the environment, exactly as the harness supplies
them. Every blocking case has an allowing twin, because a guard with false
positives gets disabled, which is worse than no guard.
"""
import json, os, subprocess, sys, tempfile
from pathlib import Path

GUARD = str(Path(__file__).parent / "guard_compiler_tree.py")


def board(writer, claims):
    rows = "\n".join(
        f"| {i} | `{name}` | 0.0 … 1.0 | {'CLAIMED s1' if name in claims else '—'} | |"
        for i, name in enumerate(("nitpick-regex", "nitpick-tui", "nitpick-time", "nitpick-parse", "nitpick-posix"), 1))
    return f"# The board\n\n**Workbench writer:** {writer}\n\n## Stream 1 — text\n\n| # | Repository | Cycles | State | Notes |\n|---|---|---|---|---|\n{rows}\n"


def fixture(tmp: Path):
    comp = tmp / "compiler"
    for d in ("build", "meta/specs", "runtime", "src/frontend", ".internal/quickemit", "tools"):
        (comp / d).mkdir(parents=True)
    for f in ("build/npkc", "build/npkrt.o", "meta/specs/DECISIONS.md", "CLAUDE.md", "runtime/npkrt.ll",
              ".internal/quickemit/npkc", "tools/thing.py", "src/main.npk"):
        (comp / f).write_text("x")
    libs = tmp / "libs"
    for name in ("nitpick-tui", "nitpick-regex", "nitpick-time", "nitpick-parse"):
        (libs / name / ".git").mkdir(parents=True)
        (libs / name / "meta").mkdir()
        (libs / name / "src").mkdir()
        (libs / name / "README.md").write_text("x")
        (libs / name / "meta" / "DECISIONS.md").write_text("x")
    (libs / "tools").mkdir()
    (libs / ".internal/toolchain/abc").mkdir(parents=True)
    for f in ("START.md", "PLAYBOOK.md", "tools/check_refs.py"):
        (libs / f).write_text("x")
    apps = tmp / "apps"
    (apps / "nitpick-posix" / ".git").mkdir(parents=True)
    (apps / "APPS.md").write_text("x")
    return comp, libs, apps


def run(tool, project, cwd, payload, env, session):
    key = "command" if tool == "Bash" else "file_path"
    inp = json.dumps({"tool_name": tool, "cwd": cwd, "session_id": session, "tool_input": {key: payload}})
    e = dict(env, CLAUDE_PROJECT_DIR=project)
    out = subprocess.run([sys.executable, GUARD], input=inp, capture_output=True, text=True, env=e).stdout.strip()
    return bool(out), out


def main():
    with tempfile.TemporaryDirectory() as t:
        tmp = Path(t).resolve()
        comp, libs, apps = fixture(tmp)
        C, L, A = str(comp), str(libs), str(apps)
        TUI, TIME = f"{L}/nitpick-tui", f"{L}/nitpick-time"
        env = dict(os.environ, NPK_COMPILER_DIR=C, NPK_LIBS_DIR=L, NPK_APPS_DIR=A)
        DEFAULT = board("none", {"nitpick-tui", "nitpick-regex"})
        NAMED = board("`sess-A` since today", {"nitpick-tui", "nitpick-regex"})

        # (label, board text, session, tool, project, cwd, payload, should_block)
        B, S = DEFAULT, "sess-A"
        CASES = [
            # --- MUST BLOCK: real writes into the compiler tree ---------------
            ("compiler", B, S, "Bash", L, L, "echo x > ../compiler/meta/specs/DECISIONS.md", True),
            ("compiler", B, S, "Bash", L, L, f"sed -i 's/a/b/' {C}/CLAUDE.md", True),
            ("compiler", B, S, "Bash", L, L, "rm -rf ../compiler/build", True),
            ("compiler", B, S, "Bash", L, L, "cp notes.md ../compiler/meta/", True),
            ("compiler", B, S, "Bash", L, L, "git -C ../compiler commit -am oops", True),
            ("compiler", B, S, "Bash", L, L, "touch ../compiler/newfile", True),
            ("compiler", B, S, "Bash", L, L, "mkdir -p ../compiler/meta/newdir", True),
            ("compiler", B, S, "Bash", L, L, "chmod +x ../compiler/tools/thing.py", True),
            ("compiler", B, S, "Bash", L, L, f"cat foo >> {C}/notes.txt", True),
            ("compiler", B, S, "Bash", TUI, TUI, "mv x ../../compiler/y", True),
            ("compiler", B, S, "Bash", L, L, "cd ../compiler && rm -rf build", True),
            ("compiler", B, S, "Bash", L, L, "dd if=/dev/zero of=../compiler/x bs=1", True),
            ("compiler", B, S, "Write", L, L, "../compiler/meta/specs/DECISIONS.md", True),
            ("compiler", B, S, "Edit", TUI, TUI, "../../compiler/src/main.npk", True),
            ("compiler", B, S, "Edit", L, L, f"{C}/CLAUDE.md", True),
            # --- MUST ALLOW: reads and inspection ------------------------------
            ("read", B, S, "Bash", L, L, 'grep -rn "SIGPIPE" ../compiler/runtime/npkrt.ll', False),
            ("read", B, S, "Bash", L, L, "cat ../compiler/meta/specs/DECISIONS.md | head -50", False),
            ("read", B, S, "Bash", L, L, "cd ../compiler && git log --oneline -3", False),
            ("read", B, S, "Bash", TUI, TUI, "git -C ../../compiler status --short", False),
            ("read", B, S, "Bash", L, L, "ls ../compiler/src/frontend/", False),
            ("read", B, S, "Bash", L, L, "python3 tools/check_refs.py . nitpick-tui", False),
            ("read", B, S, "Bash", L, L, "find ../compiler -name '*.npk' | head", False),
            ("read", B, S, "Bash", L, L, "diff ../compiler/CLAUDE.md /tmp/old.md", False),
            # --- MUST ALLOW: writes elsewhere, incl. ones DESCRIBING the compiler
            ("elsewhere", B, S, "Bash", L, L, "git add -A && git commit -m 'note about ../compiler'", False),
            ("elsewhere", B, S, "Bash", L, L, "sed -i 's/a/b/' nitpick-tui/README.md", False),
            ("elsewhere", B, S, "Bash", L, L, "cat > START.md <<'EOF'\nthe compiler at ../compiler is read-only\nrun: rm -rf ../compiler/build\nEOF", False),
            ("elsewhere", B, S, "Bash", L, L, "echo 'see ../compiler/meta' > PLAYBOOK.md", False),
            ("elsewhere", B, S, "Bash", L, L, "mkdir -p nitpick-tui/meta/roadmap/0.1", False),
            ("elsewhere", B, S, "Bash", L, L, "rm -rf nitpick-tui/build", False),
            ("elsewhere", B, S, "Write", L, L, "PLAYBOOK.md", False),
            ("elsewhere", B, S, "Write", L, L, "../apps/APPS.md", False),
            ("elsewhere", B, S, "Edit", TUI, TUI, "meta/DECISIONS.md", False),
            # --- source-vs-destination: reading OUT of the tree is a read ------
            ("source", B, S, "Bash", L, L, "cp ../compiler/.internal/quickemit/npkc /tmp/npkc", False),
            ("source", B, S, "Bash", L, L, "cp ../compiler/runtime/npkrt.ll /tmp/", False),
            ("source", B, S, "Bash", L, L, "rsync -a ../compiler/meta/ /tmp/specs/", False),
            ("source", B, S, "Bash", L, L, "install -m755 ../compiler/build/npkc /tmp/npkc", False),
            ("source", B, S, "Bash", L, L, "ln -s ../compiler/runtime/npkrt.ll /tmp/rt.ll", False),
            ("source", B, S, "Bash", L, L, "cp /tmp/x ../compiler/meta/x", True),
            ("source", B, S, "Bash", L, L, "rsync -a /tmp/specs/ ../compiler/meta/", True),
            ("source", B, S, "Bash", L, L, "mv ../compiler/meta/x /tmp/x", True),
            ("source", B, S, "Bash", L, L, "mv /tmp/x ../compiler/meta/x", True),
            ("source", B, S, "Bash", L, L, "cp ../compiler/build/npkc .internal/toolchain/abc/npkc", False),
            # --- MUST ALLOW: the compiler's own session --------------------------
            ("compiler-session", B, S, "Bash", C, C, "sed -i s/a/b/ src/main.npk", False),
            ("compiler-session", B, S, "Bash", f"{C}/src", f"{C}/src", "echo x > frontend/lexer.npk", False),
            ("compiler-session", B, S, "Bash", C, C, "git commit -am '1.5.1'", False),
            ("compiler-session", B, S, "Edit", C, C, "src/main.npk", False),
            # --- project-directory scoping: the persisted-cd hole ---------------
            ("scoping", B, S, "Bash", L, C, "echo x > meta/x", True),
            ("scoping", B, S, "Bash", C, C, "echo x > meta/x", False),
            ("scoping", B, S, "Bash", L, L, "ls && cd ../compiler && rm -rf build", True),
            ("scoping", B, S, "Bash", L, L, "cd nitpick-regex && cd ../../compiler && touch y", True),
            ("scoping", B, S, "Bash", L, L, "(cd ../compiler && git log) && rm -rf build", False),
            ("scoping", B, S, "Bash", L, L, "(cd ../compiler && rm -rf build)", True),
            ("scoping", B, S, "Bash", L, L, "python3 - <<'PY'\nprint(1)\nPY\nrm -rf ../compiler/build", True),
            # --- the claim rule ---------------------------------------------------
            ("claim", B, S, "Bash", L, L, "echo x > nitpick-regex/src/a.npk", False),
            ("claim", B, S, "Bash", L, L, "echo x > nitpick-time/src/a.npk", True),
            ("claim", B, S, "Bash", L, L, "echo hi\ntouch nitpick-time/x", True),
            ("claim", B, S, "Write", L, L, "nitpick-time/meta/DECISIONS.md", True),
            ("claim", B, S, "Edit", L, L, "nitpick-regex/meta/DECISIONS.md", False),
            ("claim", B, S, "Bash", L, L, "git -C nitpick-time commit -am x", True),
            ("claim", B, S, "Bash", L, L, "git -C nitpick-time log", False),
            ("claim", B, S, "Bash", TIME, TIME, "echo x > src/a.npk", False),
            ("claim", B, S, "Bash", L, L, "echo x > ../apps/nitpick-posix/x", True),
            ("claim", B, S, "Bash", L, L, "rm -rf nitpick-parse/build", True),
            ("claim", B, S, "Bash", L, L, "cat > nitpick-time/notes.md <<'EOF'\nCLAIMED\nEOF", True),
            ("claim", B, S, "Bash", L, L, 'git -C "$REPO" commit -m x', False),
            # --- the workbench-writer rule -------------------------------------
            ("writer", B, S, "Bash", L, L, "echo x > BOARD.md", False),
            ("writer", NAMED, "sess-A", "Bash", L, L, "echo x > PLAYBOOK.md", False),
            ("writer", NAMED, "sess-B", "Bash", L, L, "echo x > PLAYBOOK.md", True),
            ("writer", NAMED, "sess-B", "Write", L, L, "RECORD.md", True),
            ("writer", NAMED, "sess-B", "Bash", L, L, "echo x > BOARD.md", False),
            ("writer", NAMED, "sess-B", "Bash", L, L, "echo x > nitpick-regex/src/a.npk", False),
            ("writer", NAMED, "sess-B", "Bash", L, L, "mkdir -p .internal && touch .internal/x", True),
            ("writer", NAMED, "sess-B", "Bash", L, L, "sed -i 's/a/b/' nitpick-regex/README.md", False),
        ]
        fails, seen_kinds = [], {}
        for label, btext, session, tool, project, cwd, payload, should in CASES:
            (libs / "BOARD.md").write_text(btext)
            got, out = run(tool, project, cwd, payload, env, session)
            mark = "ok " if got == should else "FAIL"
            if got != should:
                fails.append((label, tool, payload, should, got, out[:120]))
            one = payload.replace("\n", "\\n")
            print(f"  {mark} [{'block' if should else 'allow'}] {label:<16} {tool:<5} {one[:60]}")
        print()
        if fails:
            print(f"{len(fails)} FAILURE(S):")
            for label, tool, p, should, got, out in fails:
                print(f"  {label} {tool} {p!r}: expected {'block' if should else 'allow'}, got {'block' if got else 'allow'} {out}")
            return 1
        blocks = sum(1 for c in CASES if c[7])
        print(f"All {len(CASES)} cases correct ({blocks} block, {len(CASES) - blocks} allow).")
        return 0


if __name__ == "__main__":
    sys.exit(main())
