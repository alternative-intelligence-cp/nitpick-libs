# The record

The orchestrator's execution record (the compiler's R8): what was dispatched,
what came back, what it cost, which estimates were wrong and by how much,
which gates bound, which findings recurred, and every question answered.
Append-only; never rewritten. [`BOARD.md`](BOARD.md) is the present; this is
the past.

Entry vocabulary: `dispatch <label>` · `report <label> <status> <tokens>
<minutes>` · `verify <label> PASS|FAIL` · `advance <repo> <subcycle>` ·
`release <repo>` · `pin <commit>` · `stale claim <repo>: <found>, <done>` ·
`question Q-n answered: <answer>` · `rebalance: <what moved and why>` ·
`audit <repo> <cycle> filed` · `finding: <one line, and where it went>`.

## 2026-09-03

- workbench: cycle 0.2 planned and committed (`3f00d7d`); Q-2 answered by the
  author's flagless session (`5e8f464`); the first flagless `/npk:check` run
  found the check skill's control missing and a second writer in the
  workbench — both folded into the plan (`e6a94a7`)
- 0.2.0 executed in the author's planning session, named on the board as the
  workbench writer. Toolchain edits, one commit per repository:
  `nitpick-tui` e5439ee · `nitpick-parse` 3cad08c · `nitpick-regex` c056ae1 ·
  `nitpick-sockets` d385991 · `nitpick-time` aad6e45 · `nitpick-posix` 948d9b6
- finding: the "Where you are" bullet of every `0.0.0.md` also pointed at the
  compiler's `build/` ("whichever is current"); edited with the §2 command.
  `nitpick-posix/CLAUDE.md` had no build section, so it gained "The toolchain"
