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
| [`skills/`](skills/) | the **`npk` plugin** — five working skills: `worker`, `orchestrate`, `audit`, `check` and `new-repo`. §"Using the skills" below |

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
working skills serves all the sibling checkouts instead of eight drifting ones.

```bash
claude --plugin-dir ~/Workspace/REPOS/nitpick-libs
```

An alias is worth setting, since forgetting the flag silently loses the skills:

```bash
alias nclaude='claude --plugin-dir ~/Workspace/REPOS/nitpick-libs'
```

| Skill | For |
|---|---|
| `/npk:worker` | working one cycle — the claim check, the read order, the discipline, the close checklist |
| `/npk:orchestrate` | assigning, gating, merging, rebalancing, and keeping the record. Writes no code |
| `/npk:audit` | adversarially diffing documents against what they describe, and re-verifying every claim about the compiler at its source. Reports, never fixes |
| `/npk:check` | the mechanical half of that, as a script: links, decision citations, duplicates, leaks |
| `/npk:new-repo` | creating a repository, including the GitHub side, in one pass |

**What the skills deliberately do not contain.** They carry *procedure and
pointers*, never content. The language constraints live in
[`PLAYBOOK.md`](PLAYBOOK.md), the rules in each repository's `meta/specs/`, the
decisions in its `meta/DECISIONS.md`. A skill that copied any of that would be
a second home for one fact, and this ecosystem's whole discipline is that a
fact has one.

**And what they cannot enforce.** A skill's tool restrictions last one turn,
not a session, so "the orchestrator writes no code" is a discipline rather than
a guarantee. Hard constraints — the compiler tree being read-only above all —
belong in `settings.json` permissions or a hook, where they are enforced rather
than requested.
