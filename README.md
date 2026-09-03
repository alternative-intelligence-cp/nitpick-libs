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
