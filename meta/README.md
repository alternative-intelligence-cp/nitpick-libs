# `meta/`

The workbench's own planning layer, in the same shape every library uses:
a roadmap of cycles, and the open questions. There is no `specs/` here and no
`DECISIONS.md` — the workbench's rules are the `W-` rules in
[`../WORKSTREAMS.md`](../WORKSTREAMS.md), and a cycle's planning decisions
live in that cycle's `README.md` until they are promoted to a `W-` rule.

| Path | What it is |
|---|---|
| [`roadmap/`](roadmap/README.md) | the workbench's cycles — one per version of the `npk` plugin |
| [`OPEN_QUESTIONS.md`](OPEN_QUESTIONS.md) | what is not settled, each with a recommendation |
| `audits/` | audit reports, filed by the orchestrator (created by cycle 0.2) |

**The workbench has one writer: the orchestrator** (or the author, between
sessions). Nothing under `meta/` is edited by a worker.
