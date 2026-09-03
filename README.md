# nitpick-libs — the library workbench

The shared documents for the **[Nitpick](https://github.com/alternative-intelligence-cp/nitpick)**
library ecosystem. Every library has its own repository; this one holds what
belongs to none of them.

**It tracks the root and nothing else.** Each subdirectory is a library
checkout with its own history and its own remote, and `.gitignore` excludes
every one of them — so a library can never be accidentally embedded here as a
gitlink or a copy. Clone this beside the libraries, not around them.

## What is here

| File | What it is |
|---|---|
| [`PLAYBOOK.md`](PLAYBOOK.md) | **how a Nitpick library is set up and planned** — the language constraints that reach a library, the error-budget rule, the repository and roadmap conventions, the measured state of the tooling, and what a finished plan looks like |
| [`LIBRARIES.md`](LIBRARIES.md) | the registry — every library, its package name, its decision prefix, and its status. Read it before starting a new one, so a name or a prefix is not taken twice |
| [`WORKSTREAMS.md`](WORKSTREAMS.md) | **the dependency graph across every repository, and the three streams it partitions into** — what the compiler actually gates (almost nothing), which work can run at once, and the rules that keep two agents out of one repository |
| [`BOARD.md`](BOARD.md) | the live state: what is claimed, what is blocked, what is done. The orchestrator owns it |
| [`RECORD.md`](RECORD.md) | the orchestrator's execution record — what was dispatched, what came back, what it cost, every question answered. Append-only |
| [`CLAUDE.md`](CLAUDE.md) | who a session here is, and the three write rules |
| [`skills/`](skills/) | the **`npk` plugin** — seven skills: `plan`, `worker`, `orchestrate`, `audit`, `check`, `research` and `new-repo`. §"Using the skills" below |
| [`agents/`](agents/) | the five agent roles the orchestrator dispatches: worker, planner, auditor, verifier, researcher — each preloading its skill, tools explicit |
| [`hooks/`](hooks/) | the plugin's session-start hook that gives a compacted orchestrator its bearings back |
| [`START.md`](START.md) | how to start the orchestrator — one line and its arguments |
| [`tools/`](tools/) | the guard that enforces the three write rules, its fixture-based control, and the compaction hook's script |
| [`meta/`](meta/README.md) | the workbench's own roadmap (the plugin's cycles), open questions, the registry of compiler requests, and filed audits |

## The working layout

```
~/Workspace/REPOS/
├── nitpick/            the compiler — READ ONLY from a library session
├── ARCHIVE/            prototype-era prior art — a behavioural oracle, never precedent
└── nitpick-libs/       this repository
    ├── PLAYBOOK.md
    ├── LIBRARIES.md
    ├── nitpick-tui/    ─┐
    ├── nitpick-parse/   │  each its own repository,
    ├── nitpick-regex/   │  ignored by this one
    ├── nitpick-sockets/ │
    └── nitpick-time/   ─┘
```

**The compiler repository is read-only from a library session.** It runs
verification and parity passes measured in hours, and its own orchestration
rules say not to edit a tree while a harness runs on it. A library that needs
something from the compiler records it as an `O-N` open question and raises it
as a request.

## Adding a library

1. Read [`PLAYBOOK.md`](PLAYBOOK.md).
2. Claim a package name and a decision prefix in
   [`LIBRARIES.md`](LIBRARIES.md), in the same commit that starts the work.
3. Follow the playbook's order: setup, specs, decisions, open questions, the
   cycle map, then cycle 0.0 execution-grade. Code last.

## Licence

Apache 2.0, matching the compiler and every library. See [`LICENSE`](LICENSE).

## Using the skills

This repository is also a Claude Code **plugin**, so one versioned copy of the
working skills, agents and hooks serves all the sibling checkouts instead of
eight drifting ones. It loads in every session from a symlink in the personal
skills directory, with no flag:

```bash
ln -s ~/Workspace/REPOS/nitpick-libs ~/.claude/skills/npk     # once
```

The flag form, `claude --plugin-dir ~/Workspace/REPOS/nitpick-libs`, is the
fallback — never both, or the plugin loads twice.

| Skill | For |
|---|---|
| `/npk:orchestrate` | the loop: pin, claim, dispatch, verify, record, escalate. Reads `width=`, `streams=`, `start=`, `tick`. Writes no code |
| `/npk:worker` | one subcycle of one repository, as dispatched — the inputs, the checks, the discipline, the REPORT block |
| `/npk:plan` | a cycle's or a repository's plan — specs, decisions, open questions, the cycle map, the currency table |
| `/npk:research` | an up-to-date fact from outside the compiler tree, as a dated, sourced digest |
| `/npk:audit` | adversarially diffing documents against what they describe, inside the compiler and out. Reports, never fixes |
| `/npk:check` | the mechanical half: links, citations, duplicates, leaks — and a worker's committed REPORT block |
| `/npk:new-repo` | creating a repository, including the GitHub side, in one pass. Never delegated |

| Agent | Preloads | Cannot |
|---|---|---|
| `worker` | worker | write outside its `REPO` (discipline; the guard enforces the claim) |
| `planner` | plan, research | write code |
| `auditor` | audit | write files — no `Write`, no `Edit` |
| `verifier` | check | write anything; runs on a smaller model |
| `researcher` | research | write files; the requester files the digest |

**What the skills deliberately do not contain.** They carry *procedure and
pointers*, never content. The language constraints live in
[`PLAYBOOK.md`](PLAYBOOK.md), the rules in each repository's `meta/specs/`, the
decisions in its `meta/DECISIONS.md`. A skill that copied any of that would be
a second home for one fact, and this ecosystem's whole discipline is that a
fact has one.

**And what they can and cannot enforce.** A skill's `allowed-tools` only
pre-approves; it never restricts. An agent definition's tool list does
restrict, which is why the auditor and researcher genuinely cannot write. The
orchestrator is the main session, so "the orchestrator writes no code" is a
discipline. The three write rules are enforced by the guard below.

## The guard

`tools/guard_compiler_tree.py` runs as a `PreToolUse` hook on `Bash`, `Write`,
`Edit` and `NotebookEdit`, and enforces three rules by the **target** of a
write, never by what a command mentions:

1. **The compiler tree is read-only** from any session started outside it.
2. **A library or application repository is written only when `BOARD.md`
   shows it claimed** (W-7), unless the session was started inside that
   repository.
3. **The workbench's own files are written only by the session the board's
   `Workbench writer:` line names** (W-16). The board itself is exempt — it
   is the lock, taking it is always possible and always in the history, and
   the session refused afterwards is the one that lost it.

It scopes on the session's project directory, not on the shell's current
directory, because the latter follows `cd`. Install it once, in
`~/.claude/settings.json`:

```json
{ "hooks": { "PreToolUse": [ {
    "matcher": "Bash|Write|Edit|NotebookEdit",
    "hooks": [ { "type": "command",
      "command": "python3 ~/Workspace/REPOS/nitpick-libs/tools/guard_compiler_tree.py" } ]
} ] } }
```

`tools/test_guard.py` is its control. It builds a fixture in a temporary
directory and prints its case count; more than a third of the cases are
false-positive controls, because the first version refused a write to
`START.md` when that file's heredoc body mentioned the compiler, and a guard
with false positives gets disabled — which is worse than no guard.

**The limits, stated:** an interpreter heredoc that writes cannot be classified
from the command text, and a target containing an unexpanded variable cannot be
resolved and is not judged. The airtight mechanism for the first is the
sandbox's `filesystem.denyWrite`.
