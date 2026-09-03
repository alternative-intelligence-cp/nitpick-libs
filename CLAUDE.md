# CLAUDE.md — the library workbench

**What this is.** The shared documents and the working system — the `npk`
plugin — for the Nitpick libraries. Each subdirectory is a library checkout
with its own history and remote; this repository tracks the root only.

**Who you are.**

- Started here with `/npk:orchestrate` → **the orchestrator.** The loop is
  `skills/orchestrate/SKILL.md`; the live state is `BOARD.md`; the past is
  `RECORD.md`. You write here and nowhere else.
- An agent dispatched by the orchestrator → your skill is preloaded and your
  prompt carries your inputs. You write only under your `REPO`.
- The author, or a session here for anything else → read `BOARD.md` first.

**Write rules, enforced by the guard where they can be.**

- The compiler at `../nitpick` is **read-only** from here.
- A library or application repository is written only when `BOARD.md` shows
  it `CLAIMED`, or by a session started inside it.
- This repository has **one writer** (W-16), named on `BOARD.md`'s
  `Workbench writer:` line. If it names a session that is not you, do not
  write here. The board itself is the lock: take it only when that session is
  gone, and record the takeover in `RECORD.md`.

**Read first.** `README.md` (the map) · `WORKSTREAMS.md` (the rules W-1…W-26)
· `PLAYBOOK.md` (what the language imposes). The plan for the system itself
is `meta/roadmap/`.

**If your context was compacted:** re-read `BOARD.md` before acting.
