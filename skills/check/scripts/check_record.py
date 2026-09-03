#!/usr/bin/env python3
"""Verify a subcycle's committed execution record against the tree.

The worker's REPORT block (skills/worker/SKILL.md §9) lives in two places:
the final message and the subcycle file's execution record. This checks the
committed one, mechanically, so that "the loop reads the report and decides"
rests on a defined shape rather than on prose.

Usage:  check_record.py <repo> <cycle>.<sub>
Exit:   0 clean, 1 findings, 2 could not run
"""
import re, subprocess, sys
from pathlib import Path

STATUSES = {"DONE", "READY-TO-CLOSE", "BLOCKED", "STOPPED", "NEEDS-DECISION", "RED"}
DONE_LIKE = {"DONE", "READY-TO-CLOSE"}
KEYS = ["status", "stream", "model", "toolchain", "commits", "harness", "check",
        "record", "next", "findings-for-playbook", "open-questions-raised",
        "for-the-author", "compiler-defect", "tokens-and-time"]
TITLE = re.compile(r"^#\s.*—\s*(PLANNED|RUNNING\s*\(.*\)|DONE\s*\(.*\))\s*$")
KEY = re.compile(r"^([a-z-]+):\s*(.*)$")
HASH = re.compile(r"^[0-9a-f]{7,40}$")


def git(repo, *args):
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return r.returncode, r.stdout.strip()


def parse_report(section):
    """The LAST 'REPORT …' block in the section: (name, id, {key: value})."""
    lines = section.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith("REPORT ")]
    if not starts:
        return None
    i = starts[-1]
    head = lines[i].split()
    name, sid = (head[1], head[2]) if len(head) >= 3 else (None, None)
    fields, cur = {}, None
    for l in lines[i + 1:]:
        if not l.strip():
            break
        m = KEY.match(l)
        if m:
            cur = m.group(1)
            fields[cur] = m.group(2).strip()
        elif cur and l[:1].isspace():
            fields[cur] = (fields[cur] + "\n" + l.strip()).strip()
    return name, sid, fields


def check(repo: Path, sid: str):
    findings = []
    cycle = sid.rsplit(".", 1)[0]
    f = repo / "meta" / "roadmap" / cycle / f"{sid}.md"
    if not f.exists():
        return [("no-file", f"{f.relative_to(repo)} does not exist")]
    text = f.read_text(encoding="utf-8", errors="replace")
    title = text.split("\n", 1)[0]
    m = TITLE.match(title)
    tstatus = m.group(1).split()[0].split("(")[0] if m else None
    if not tstatus:
        findings.append(("bad-status", f"title line is not PLANNED / RUNNING (…) / DONE (…): {title[:80]}"))

    k = text.find("\n## Execution record")
    rep = parse_report(text[k:]) if k >= 0 else None
    if rep is None:
        findings.append(("no-report", "no REPORT block under '## Execution record'"))
        return findings
    name, rid, fields = rep
    if name != repo.name or rid != sid:
        findings.append(("no-report", f"last REPORT names {name} {rid}, expected {repo.name} {sid}"))
        return findings
    for key in KEYS:
        if key not in fields:
            findings.append(("missing-field", f"REPORT lacks '{key}:'"))
    status = fields.get("status", "").split()[0] if fields.get("status") else ""
    if status not in STATUSES:
        findings.append(("bad-report-status", f"status '{status}' is not one of {sorted(STATUSES)}"))
        status = None
    if status and tstatus:
        if status in DONE_LIKE and tstatus != "DONE":
            findings.append(("status-mismatch", f"report {status} but the title says {tstatus}"))
        if status not in DONE_LIKE and tstatus == "DONE":
            findings.append(("status-mismatch", f"report {status} but the title says DONE"))

    for line in fields.get("commits", "").split("\n"):
        line = line.strip().lstrip("-").strip()
        if not line:
            continue
        h = line.split()[0]
        if h == "HEAD":
            continue
        if not HASH.match(h) or git(repo, "cat-file", "-e", f"{h}^{{commit}}")[0] != 0:
            findings.append(("unknown-commit", f"'{h}' is not a commit in this repository"))

    if status in DONE_LIKE:
        rc, subj = git(repo, "log", "-1", "--format=%s")
        if rc != 0 or not subj.startswith(f"cycle {sid}:"):
            findings.append(("head-subject", f"HEAD's subject is '{subj}', expected to begin 'cycle {sid}:'"))

    rc, dirty = git(repo, "status", "--porcelain")
    if rc != 0:
        return findings + [("no-git", "not a git repository")]
    if dirty:
        findings.append(("dirty-tree", f"{len(dirty.splitlines())} uncommitted path(s)"))

    if status == "DONE":
        readme = repo / "meta" / "roadmap" / cycle / "README.md"
        if readme.exists():
            rt = readme.read_text(encoding="utf-8", errors="replace")
            sec = re.search(rf"^###\s+{re.escape(sid)}\b.*?$(.*?)(?=^###\s|^##\s|\Z)", rt, re.S | re.M)
            if sec:
                for item in re.findall(r"^\s*- \[ \] (.*)$", sec.group(1), re.M):
                    if "~~" not in item:
                        findings.append(("unticked", f"README {sid}: '{item[:70]}'"))
    return findings


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    repo = Path(argv[1]).resolve()
    if not repo.is_dir():
        print(f"!! {repo}: not a directory", file=sys.stderr)
        return 2
    fs = check(repo, argv[2])
    if any(k == "no-git" for k, _ in fs):
        print(f"!! {repo}: not a git repository", file=sys.stderr)
        return 2
    if not fs:
        print(f"  {repo.name} {argv[2]}: record clean")
        return 0
    print(f"  {repo.name} {argv[2]}: {len(fs)} finding(s)")
    for kind, msg in fs:
        print(f"      [{kind}] {msg}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
