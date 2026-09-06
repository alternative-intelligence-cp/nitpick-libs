# The board

**Live state.** What each stream is working on, what is claimed, what is
blocked, what is done. The durable plan is
[`WORKSTREAMS.md`](WORKSTREAMS.md); the past is [`RECORD.md`](RECORD.md).

> **The orchestrator owns this file** (W-8). An agent working a stream does not
> edit it — the orchestrator claims before a worker is dispatched and releases
> when the stream leaves the repository. That is what keeps two agents out of
> one repository and removes every merge conflict by construction.

**Last updated:** 2026-09-06 · **Trees:** **8**, all `dirty=0` and `ahead/behind=0/0`, the set **discovered rather than listed** (`PLAYBOOK.md` §7 — it was recorded as 7 for four orchestrators) · **Width:** 1 — stream 2 only, confirmed by the author 2026-09-05 (question 4 answered; the dial turned down for quota, not a change of plan — `parallel-planning-serial-implementation`) ·
**Toolchain:** **`3d15ac9`** · `.internal/toolchain/3d15ac9/` · pinned 2026-09-06 03:40 · **the 1.5.2f close, and the re-pin the board held for since 02:00.** **Both guards cleared before anything was copied:** the binary's mtime is **725 s AFTER** `HEAD`'s commit, which is §3's provenance test, and it was **876 s old**, past the two-minute mid-rebuild floor that has fired twice and been right both times. **Verified here rather than taken on report:** both digests **match** the compiler's six-digest notice (`npkc` 7 351 160 B / `3b7d6aa0…`; `npkrt.o` 55 576 B / `c9ddbcff…`), `sha256sum -c` OK, LLVM 20.1.2, tree clean and level, and `aaffb87` is an ancestor so the pin moves forward. **`npkrt.o` `cmp`-verified byte-identical to the `aaffb87` pin's** rather than assumed (DEF-12). **COMMISSIONED BOTH DIRECTIONS:** `tools/canary.npk` exits 0 emitting **50 482 B / 14 `define`s**; a malformed file exits 1 at `NITPICK-PARSE-001` writing none. **AND THE FLAT PREDICTION HELD** — the same program through both pinned compilers gives `aaffb87` **50 482 B / 14** and `3d15ac9` **50 482 B / 14**, byte- and define-identical, which is what `nitpick-compiler_s0` predicted and forbids any movement. **The canary SOURCE is now committed** (`tools/canary.npk`, `tools/canary.md`) because the previous one lived only in a session scratchpad and is lost — its output survived, its input did not. Full provenance in `.internal/toolchain/3d15ac9/PIN.md`. *Previous pin, kept:* aaffb87 · .internal/toolchain/aaffb87/ · pinned 2026-09-05 22:47 · **tree clean, and the provenance CHECKED rather than inferred** — the 1.5.2d close. `build/npkc` was rebuilt from the pushed main checkout 22:41–22:45, so its mtime (22:45:33) is **500 s after** `HEAD`'s commit (22:37:13), which is §3's provenance test; the same test refused a binary in the morning. Verified here before copying, independently of the landing notice: **7 346 792 B**, sha256 `a3b0dadc…`, `sha256sum -c` OK, LLVM **20.1.2**, `0dfddac` is an ancestor of `aaffb87`. **`npkrt.o` is byte-identical to the 0dfddac pin's** (55 576 B, `c9ddbcff…`) — taken again and `cmp`-verified, not assumed (DEF-12's precedent). **`aaffb87` is docs-only over `0880771`, so the compiler SOURCE is `0880771`'s** — 1.5.2d step 4. **Commissioned before use, both directions:** the canary compiles at exit 0 writing a 50 560 B `.ll`; a malformed file exits 1 at `NITPICK-PARSE-001` writing none. **The mid-rebuild guard fired first and was right** — the binary was 97 s old and §3 said retry, which is the second re-pin running it has caught the orchestrator moving straight off a landing notice. Full provenance and 1.5.2d's five step commits are in `.internal/toolchain/aaffb87/PIN.md`'s `binary` line
**Workbench writer:** `647e6588-8236-4fcc-91a1-0223d220639f`, session `nitpick-libs_s3`, the **eighth** orchestrator — **taken 2026-09-06 04:1x on a briefed handoff from `nitpick-libs_s2`.** *(Freedom established on **three** independent readings before the write, none of them inference: this line read `none` **both locally and on `origin/main`**, which are the same commit `15969bf`, and `git show 15969bf -- BOARD.md` was read so the take is from a state actually seen rather than one assumed — `nitpick-libs_s4` suggested that check and it confirmed the release is genuine; `.internal/` held **only** `toolchain/`, no marker, which hazard 1 says to check because the guard's silence is not evidence; and **both** libs peers answered from commands — `nitpick-libs_s2` returned a verbatim `git status` with "`15969bf` is my last write, everything from here is messages only", and `nitpick-libs_s4` returned "idle, nothing written, nothing queued", volunteering that its whole transcript holds no write and undertaking to message this session before it ever writes here. Hazards 3 and 4 both paid again.)* **My own eight-tree sweep, discovered with `find` and not listed, agrees: 8 trees, all `dirty=0`, all `ahead/behind=0/0`.** **Nothing is in flight; no agent is live; ALL EIGHT TREES ARE CLEAN AND LEVEL** — `nitpick-time` included, now that 0.1.0 is pushed. **THE RE-PIN IS DONE: the pin is `3d15ac9`**, commissioned, both §3 guards clear on the first attempt, digests matched the compiler's notice rather than taken from it, `npkrt.o` `cmp`-verified unchanged, and **the canary's FLAT prediction held** — 50 482 B / 14 `define`s at both `aaffb87` and `3d15ac9`. **`nitpick-time` 0.1.0 is DONE, VERIFIED PASS, PUSHED, and CI-GREEN** at `2589069` (run `34020573741`), so it is confirmed on a second machine with a differently-built compiler. **`nitpick-regex`'s TWO-DAY RED IS NOW DIAGNOSED, REPRODUCED AND BOUNDED — see THE CI PIN MAP below, which has been rewritten.** It was settled by running the harness at `91657eb` against **three kept pins on this machine**, which is what `.internal/toolchain/` is for; the CI log itself is unrecoverable (**HTTP 404, not an empty log** — GitHub has expired it, so no re-read will ever produce one). **The stale pin IS the cause and the diagnosis also refutes the fix that was recommended for it.** **Then: the claim stands at 0.1.1, which has NO subcycle file** — the first decision needed. **Two things are owed and neither is started:** the **re-founded spread** for the compiler side (specified in full below) and **0.1.1's plan**. **The compiler side is now `nitpick-compiler_s1`; `_s0` has stood down.** Marker removed first, then this line. **To take it: this line first, then the marker — AND PUSH.** **Six hazards, each measured rather than inferred; the third was found at the 13:37 handover, the fourth and fifth at the sixth orchestrator's, and the sixth at this one.** (1) The guard permits **any** session while this line reads `none`, so §2.1's refusal never fires and **its absence is not evidence the lock is free** — verify `.internal/` too. (2) **`CLAUDE_SESSION_ID` is EMPTY in a Bash tool call**, so §2.1's marker command writes a 0-byte file; take your id from the `~/.claude/projects/<slug>/<uuid>.jsonl` path, cross-check it against your scratchpad path, and expect **37 bytes**. (3) **A free lock is not the same as a clean tree.** At the 13:37 handover the incoming session asked the outgoing one *"are you done writing?"* instead of reading the `none` and taking it; the outgoing session nearly answered from memory, ran `git status`, and found an **uncommitted deletion it had not made** — the author had moved a tracked file out from under it. Committing on the "lock is free" reading would have swept another session's deletion into this one's commit. **During any handover overlap, ask the outgoing session directly and have it answer from `git status`, not from memory.** **Done again at this handover, and it paid again:** `nitpick-libs_s0` answered from `git status` — all seven trees `dirty=0`, `ahead/behind=0/0` *(seven was the set every session then swept; it is eight — hazard 6)* — and volunteered that its remaining actions are **messages only**, which a tree read cannot tell you. **Asked and answered a third time at the seventh orchestrator's takeover, and it paid a third time:** `nitpick-libs_s1` answered from `git status` and volunteered *"messages only, I have made my last write"*, which is what released this lock. (4) **A `nitpick-libs_sN` PEER YOU WERE NEVER TOLD ABOUT WILL APPEAR, AND ONE MESSAGE SETTLES IT.** At this takeover `ListAgents` showed **`nitpick-libs_s2`, idle, opened within a minute of this session**, while the handoff brief, the record and this board's own roster named only `s0` and `s1`. Orchestrate §2.1 says to stop and ask the author; **asking the peer itself is faster, cheaper and more certain** — it replied *idle, no task, nothing written, and I will message you before I write*, converting a guess into a fact in one message. That is the move the fourth orchestrator recommended for the unidentified `nitpick-e3` and did not take, leaving it open for two days. **The author's practice, confirmed by him at this handover, is a ROLLING POOL:** he pre-opens the next generation, and closes a spent session so it can return as the generation after next — `s0` closes here and comes back as `s3`, succeeding `s2`. **So a higher-numbered libs peer is normally your own parked successor, not a rival writer — but ask it anyway**, because the alternative is inference, which is exactly what two earlier orchestrators rightly refused to rest this lock on. (5) **TAKING THE LOCK IS NOT DONE UNTIL IT IS PUSHED.** The sixth orchestrator committed the writer line and did not push it, so `origin/main` went on advertising `none` while the lock was held locally — caught by the outgoing session, not by any check. **The tell was that `git status` had been run BEFORE the commit and not after**: the verification ran on the wrong side of the write. A peer reading `origin` sees a free lock; a peer reading the local tree sees a held one. **Push, then re-read the line from `origin/main` to confirm it names you.** (6) **THE SWEEP THAT CLEARS THE LOCK COUNTED SEVEN TREES AND THERE ARE EIGHT, AND NO SESSION EVER STATED WHICH SET IT MEANT.** Found at this handover by the incoming session, conceded by the outgoing one: *"it is EIGHT, and `nitpick-apps` has never been in the loop that checks."* **Three different sets are in live use in this repository and all three are correct under their own denominator** — **six repositories** (the five libraries + `nitpick-posix`) is the *work* set and every "all six repositories" claim on this board and in the record is sound; **seven trees** is that six plus this workbench; **eight** is that seven plus **`nitpick-apps` itself**, a tracked repository holding `APPS.md`, `PLAYBOOK.md`, `README.md` and `LICENSE`, which orchestrate §2.2 already puts in the startup *read* set and `CLAUDE.md` already covers under *"a library **or application** repository"*. **It is not a decision to exclude it; it is that every session inherited the same seven-item list.** The tree was clean at this handover, so nothing was lost — **and nothing would have told us if it had not been**, which is the finding. **Discover the set, never list it:** `find . ../nitpick-apps -maxdepth 3 -name .git` and **print the count with the verdict**, so an unstated denominator cannot survive a handover. The durable half is in `PLAYBOOK.md` §7: *a repository that holds only documents is still a repository, and a loop assembled by listing rather than by discovery will miss exactly the one nobody thinks of as code.* One writer here (W-16, P-19).
**THE PEER SESSIONS, AND THEIR NAMES ARE NOW A CONVENTION RATHER THAN A
LABEL.** The author renamed every session on 2026-09-05 to `<project>_s<N>`,
where the project segment names the work area and `N` is the handoff
generation. Earlier boards and briefs warned that *"names are not durable,
`ListAgents` is the address book"* — true of the old machine-assigned labels
(`nitpick-bc`, `nitpick-36`, `nitpick-e3`), and now only half true: **the
project segment and the generation number are stable and worth reading.**
`ListAgents` remains the authority on who is *alive*, and the bracketed `[ref]`
is what disambiguates.

| Session | Was | Role |
|---|---|---|
| `nitpick-libs_s3` | — | **this workbench's orchestrator — the current writer, the eighth** |
| `nitpick-libs_s4` | — | this workbench's **successor — hand off to THIS one, not to the highest number.** Answered "idle, nothing written, nothing queued" at the lock take and undertook to message before it ever writes here |
| `nitpick-libs_s5` | — | the generation **after** `s4`. Parked and unbriefed, opened 04:1x in the terminal `s2` was closed from. **Needs nothing from the current writer** |
| `nitpick-compiler_s0` | `nitpick-bc` | the original compiler session. **Stood down from the role, still alive** |
| `nitpick-compiler_s1` | `nitpick-e3` | **the compiler side TODAY — who to ask about `build/`, the pin, and whether a diagnostic change is deliberate.** Answered question 8 within the hour, with three measured facts and an unasked-for correction of a stale design premise |
| `nitpick-compiler_s2` | — | the compiler's parked successor |
| `claude-skills-devTeam_s0` / `_s1` / `_s2` | — | the `devteam` trio, **idle to conserve quota**. Segment read from `ListAgents` 2026-09-06 04:4x. This board previously said it was spelled `claud-`, "without the final `e`" — **and that was CORRECT WHEN WRITTEN, not a blunder.** The author had misspelled the names when he created the sessions, an earlier orchestrator observed the real spelling and warned others not to reconstruct it, and he then fixed his own typo by renaming. **The note outlived the thing it described.** See the paragraph below: this session first recorded it as a confident error by a predecessor, which was unfair, and the author supplied the correction |

**Two consequences worth acting on.** The unidentified idle peer the fourth
orchestrator declined to rest the lock on — `nitpick-e3` — is
`nitpick-compiler_s1`, the compiler's own waiting successor, confirmed by the
same `ListAgents` ref across the rename. It works another repository and will
not write here. And **an idle peer is parked on purpose, not stalled**: the
author is holding the `devteam` trio idle so the compiler and this workbench do
not run short of quota, so waking one has a cost he is actively managing.

**THE POOL IS THREE TERMINAL TABS IN ONE WINDOW, CYCLED IN A LOOP — described
by the author 2026-09-06, and it settles a question four orchestrators have
guessed at.** He keeps exactly three live sessions for a work area. When the
outgoing one is closed he opens the next generation **in the terminal it
vacated**, so at any moment there is one working session, its briefed
successor, and a fresh unbriefed session behind that. `s2` was closed and `s5`
opened in its tab while `s3` held the lock.

**Two things follow, and both are easy to get backwards.** (1) **Hand off to the
session ONE number above you, never to the highest number** — handing to `s5`
would skip `s4`, which has been parked and waiting for the role and is the one
the author expects to take it. (2) **A brand-new peer two numbers above you
needs nothing from you.** It is not a rival writer, it has not been briefed, and
waking it to tell it what it will learn at its own handoff spends the quota he is
deliberately managing. **Record its existence here, where the next orchestrator
reads it for free, instead of messaging it.** That is the correct answer to
hazard 4 for a peer the author has already identified — hazard 4 is about
resolving an *unexplained* peer, and a direct statement from the author is a
fact, not the inference it warns against.

**HAZARD 7 — AN IDENTIFIER CAN BE CORRECTED UNDER THIS BOARD WHILE NOTHING IS
WATCHING, AND A STALE ONE IS NOT EVIDENCE OF CARELESSNESS. Established
2026-09-06 by the author, unprompted, after this session got it wrong.** The
`devteam` sessions were originally created with the segment misspelled `claud-`.
An earlier orchestrator read that off `ListAgents`, correctly, and wrote a
warning here telling others not to reconstruct the name. The author later
noticed his own typo and renamed the sessions; **because they were idle he
judged it not worth announcing** — a reasonable call that happened to be wrong,
since a document was tracking the name. The warning outlived its subject and
became a confident, load-bearing falsehood that a later session repeated.

**This session then compounded it**, recording the note as a predecessor's
"confidently-stated spelling fix that was itself wrong". **It was right when
written.** The author supplied the real history and has undertaken to relay such
changes in future — *"if you were tracking them then it very much matters."*
Take that as reliable and build no ceremony on top of it.

**The durable rule, which survives his undertaking rather than being replaced by
it: re-derive a peer identifier from `ListAgents` at the moment you use it,
never from this table.** The table is a roster, not an address. And when you find
a stale fact in a document here, **the first hypothesis is that the world moved,
not that the author of the note was sloppy** — this handover has now found four
stale facts and exactly none of them were wrong when they were written.

**Phase:** cycle 0.2's dry run one is under way — `nitpick-time` 0.0 is the
first library cycle to be worked, and the loop is being judged against
[`meta/roadmap/0.2/0.2.7.md`](meta/roadmap/0.2/0.2.7.md) §2's pass mark.
*(This paragraph was accidentally deleted by the orchestrator's 13:40 edit — a
replacement span that ran to the next blank line and swallowed it — and restored
verbatim from `d91d0ca` at 14:10.)*

**~~THE RE-PIN IS DONE~~ — SUPERSEDED 2026-09-05 22:47 by the `aaffb87` re-pin above; kept because its four re-measurements are the before-values that one is measured against. Pinned `0dfddac` at 2026-09-05 15:58 — the 1.5.2c close —
and all four discharged stops were re-measured against it.** The morning's
question (*what is `build/npkc`, and is there a stable point to pin?*) was
settled by one message to `nitpick-compiler_s0` at 13:35 and the pin followed
its landing notice at 15:47. The working out is in `RECORD.md`; what a reader
needs now is below.

**The provenance test added to §3 this afternoon was exercised on both sides
within one day, which is what makes it commissioned rather than merely
written.** It **refused** the morning's binary as `tree unknown` — mtime
2026-09-04 19:42:54, seventeen hours *before* `HEAD` — and **passed** this one
as `tree clean`, mtime 15:56:34, nine minutes *after* `HEAD`'s 15:47:09. Every
number in the landing notice was verified here before copying rather than taken
on report; `94874ce` is an ancestor of `0dfddac`, so the pin moved forward.
`npkrt.o` is byte-identical to the previous pin's and was **taken again and
checked** rather than assumed. Full provenance, the three commits and their
harness numbers are in `.internal/toolchain/0dfddac/PIN.md`'s `binary` line.

**THE FOUR RE-MEASUREMENTS — the reason the pin was not taken this morning.**
All four were facts about `94874ce`; here is what they are against `0dfddac`.

| Stop | Verdict at the new pin |
|---|---|
| **O-N11** | **FIXED.** `case1_no_failsafe` and `case3_arm_contract_evaded` are now `npkc` **exit 1, `NITPICK-REACH-003`, no `.ll`** — where before it was `npkc` exit 0 and `llc` exit 1 on an undefined `@npk_failsafe`. `case2_failsafe_present` still exits 0 and emits. **THE IDENTITY COUNT IS PER PROGRAM, AND THIS BOARD'S "FOUR" WAS ONE CASE'S BILL ASSERTED OF ALL OF THEM. Corrected 2026-09-05 by the 0.0.1 worker and re-measured by the orchestrator directly before the board moved:** `case1` names **4** — `Unreachable, HeapOom, HeapBadRequest, WildLeak` — and `case3` names **6** — `probe11_arms_lib.EProbeZone, Unreachable, HeapOom, HeapBadRequest, WildLeak, IntOverflow`. **Both numbers were always real.** The earlier entry read *"the diagnostic says 4 identities — this board's correction against the six we were told is confirmed by the compiler's own output"*, which took one program's floor as the general answer and then cited the compiler's own mouth for it. **The board contained its own refutation:** checklist item 5 says `case1` has *"no import, no arithmetic and no allocation, so its bill is S-4b's floor of four"* — which is precisely why four is not `case3`'s number, `case3` importing `probe11_arms_lib` (hence `EProbeZone`) and doing arithmetic (hence `IntOverflow`). **A count that a diagnostic computes FROM THE PROGRAM cannot be corrected once for the set**, and "confirmed by the compiler's own output" is what made it feel settled. This is the after-value the two DEF-5 transcripts owe, and each records its own number |
| **O-N10** | **UNCHANGED.** All three `derive_payload_enum` cases behave identically on both pins through the full four-step recipe and match their `expect-exit` headers exactly (0, 121, 107). 1.5.2b's wholesale derive rewrite did **not** move it — which is precisely what had to be measured rather than assumed |
| **O-N9** | **UNCHANGED.** `probe10b` → `NITPICK-BORROW-012`, `probe10c` → `NITPICK-BORROW-001`, identical on both pins. `probe09b` exits 0 on both — *once its precondition is met; see below* |
| **O-N4** | **STILL DISCHARGED, BUT SLOWER.** `probe04` is **2.03–2.06 s at ~119 MB**, was **1.18 s at 74 624 KiB**. Against the original 281 s / 30.9 GiB it is still ~136× better, so nothing reopens |

**THE COMPILER GAINED A FIXED PER-PROGRAM COST, AND IT IS PAID BY PROGRAMS THAT
USE NONE OF THE NEW SURFACE. Measured differentially — both pinned compilers on
disk, same inputs, same machine.** A 14-line program that only does `exit 0i32`
with a `failsafe` (`probe11d_floor_only`):

| | `94874ce` | `0dfddac` | factor |
|---|---|---|---|
| wall | 0.10 s | **0.85 s** | **8.5×** |
| peak RSS | 21 456 KiB | **102 404 KiB** | **4.8×** |
| `.ll` emitted | 456 517 B | **845 282 B** | **+388 765 B** |

**The `.ll` delta is exactly 388 765 B for both the floor program and the
30 000-row one — identical to the byte**, so it is a fixed prelude increase and
not a compile-time regression. Widened across **30 programs** in two libraries
that compile clean under both: **22 of 30 sit at exactly 388 765**, and all 8
that differ are derive or enum programs, where 1.5.2b/1.5.2c genuinely changed
semantics. Almost certainly D-257's price — the prelude implementing the
derivable traits for every scalar. **Impact, W-27: blocks nothing; inconveniences
every harness run in this ecosystem**, because our libraries compile *many small
programs* per run so a fixed per-program cost multiplies by program count rather
than by size — `nitpick-regex` 0.0.3's harness was 63/63 in 37.5 s, and +0.75 s
per program roughly doubles it — and raises per-compile peak ~5×, which matters
if a harness compiles in parallel; **does not touch correctness.** **Raised to
`nitpick-compiler_s0` 2026-09-05**, under the lifted constraint, with no ask
attached beyond confirming whether the price was known.

**`probe09b_environ_view_returned` CANNOT PASS WITHOUT AN ENVIRONMENT VARIABLE
THAT IS WRITTEN DOWN NOWHERE, AND IT FAILS WITH A CODE THAT LOOKS LIKE A REAL
VERDICT.** Its header says `expect-exit: 0`. Run bare it exits **10**, on both
pins. Exit 10 is its own `string_byte_length(hit) != 14i64` — **a substantive
code from the probe's own map**, so the failure reads as a finding about the
language rather than a missing precondition. It needs **`TZ=Europe/Kiev`**
exported; with that it exits 0 on both pins. The string `Europe/Kiev` appears in
the probe file **0 times**, in `0.0.0.md` **0 times**, and `tests/probe/` has no
`README.md`. **Extent established rather than fixed only where found:** three
program-stage probes read state outside the program. `probe08_readlink` exits 0
bare — no hidden precondition. **`probe09_environ_split` is the model and the
contrast**: it documents *"PRECONDITION: run with `TZ=Europe/Kyiv` exported"*
**and exits a dedicated `30` when it is missing, so an unmet precondition
announces itself.** Same author, same afternoon; one probe made its precondition
self-describing and the neighbouring one reused a substantive failure code and
said nothing. **This is stream 2's to fix at `nitpick-time` 0.0.1** — give
`probe09b` a dedicated precondition exit code and a `PRECONDITION:` line, on
`probe09_environ_split`'s pattern. It blocks nothing today because no harness
runs yet; **it will produce a false failure the first time 0.0.2's `program`
stage runs, and the failure will look like a compiler regression.**

**CI MAY PIN THE COMPILER BY COMMIT AND EXPECT THE PINNED BYTES — BUT ONLY
UNDER TWO CONDITIONS, AND `nitpick-time` 0.0.1 STEP 4 MUST WRITE BOTH.** Asked
of `nitpick-compiler_s0` at this handover and answered 2026-09-05, because our
pin is a **binary** we copied while CI would **build** one, and P-10 has CI pin
by commit. Those are the same artefact only if the build reproduces.

**The answer is yes, by decision rather than by luck**, and the mechanism is
worth knowing: **D-204** (1.4.5) makes the toolchain a build input — the
manifest's `[toolchain]` pins LLVM **20.1.2 exactly, patch release included**,
along with the four flag sets every `llc`, `opt` and `ld.lld` call is built
from; the harness's **repro** stage re-runs the same compiler on the same
inputs from a *different working directory* and requires identical bytes on
every full run; its **parity** stage byte-compares the harness's own `npkc`
against `npkg`'s `build/npkc` on every run (**1083 verdicts, byte-identical on
all three 1.5.2c runs**); and **D-236** renders every embedded source path
relative to the manifest root, so the build path cannot leak into the artefact.

**The two conditions CI must satisfy, and neither is optional:**

1. **The same LLVM patch release — 20.1.2, not 20.1.x.** A patch release can
   change instruction selection. That is *why* the pin is to a patch.
2. **The ladder invoked from the tree root** — `npkg build`, or the harness's
   builder. Invoked elsewhere it may not reproduce.

**And the gap this closes.** `nitpick-libs_s0` flagged, correctly, that it
could prove `HEAD` did not move during the 15:52–15:56 build but **could not
prove the tree was clean during it**, and advised writing the weaker claim.
That session then answered it directly: **the tree was clean at 15:47** — `git
status` printed nothing before the push, and the ladder ran after the push from
the tree root. **So the strong claim is now supported and may be written.**

**QUALIFIED 2026-09-06, AND THE QUALIFICATION IS THE ORCHESTRATOR'S TO MAKE
BECAUSE THE OVERSTATEMENT WAS: THAT REPRODUCTION WAS SAME-MACHINE.**
`nitpick-time`'s first CI run measured the other case — **`npkrt.o` is
byte-identical across machines and `npkc` is NOT**: `c9ddbcff…` both sides,
against **`3c05818c…` in CI versus `a3b0dadc…` here**. So *"built from commit
`aaffb87`"* is **behaviourally** equivalent — CI builds the pinned commit and
the whole suite passes — but **not byte-identical across machines**, and this
board and the message that went upstream both said *"exactly as strong a claim
as the pin"* without that caveat. **One data point, deliberately NOT promoted to
an assertion**; the workflow reports the four digests and a later commit may
assert them once more runs agree. The original same-machine measurement stands
and is unaffected: **a fresh detached worktree at `0dfddac`, nothing
uncommitted, run through the same ladder (`npkg build` from the tree root)
reproduced BOTH pinned artefacts byte-for-byte** — `npkc` **7 304 552 B, sha256 `38e48973…`** and `npkrt.o`
sha256 `c9ddbcff…`. **Checked here against our own pinned files rather than
read off their message: `sha256sum` over `.internal/toolchain/0dfddac/` returns
exactly those two digests.** So *"built from commit `0dfddac`"* is now exactly
as strong a claim as the pin itself, and **`nitpick-time` 0.0.1 step 4 may
write it plainly** — provided it also writes the two conditions above, which
are what the reproduction depended on. Had the rebuild differed, CI could not
have pinned by commit at all and P-10 would have needed revisiting; it did not.

**1.5.2d IS PLANNED AND RATIFIED AS D-262** (their `daa5057`, 16:44 — **verified
here as docs-only: four files, all under `meta/`, no `src/` and no `runtime/`,
and not yet pushed**, so **`0dfddac` remains our pin and is still an ancestor of
their `main`**). **Its step 2 moves our canary**, and the landing notice carries
the before and after. Nothing here waits on it.

**O-N17 IS FIXED, AT THE PRIMITIVE, AND OUR EXTENT CORRECTION IS WHY THAT IS
CHEAP.** `nitpick-compiler_s0`, 2026-09-05: `emit_move_out` (`ir_stmt.npk`)
handed `ll_type` the *place's recorded type* and built the vacant helper's
symbol from that raw id; it now builds it from the **element type through the
specialization**, so **our five operations are one fix**. They verified the
pop, the set and the loop-clear shapes link and run to exit 0 under D-151's
leak check, where all three fail under `0dfddac`. **The extent correction was
right and changed nothing about the fix's shape** — which is the good outcome,
and worth reading twice: correcting an understated extent cost us one message
and cost them nothing, while shipping against *"one row"* would have produced a
generic `vec_clear<T>` that silently does not drop. **It is step 4 of 1.5.2d,
under its harness now**; the landing notice names the commit.

**AND THE SILENCE THAT MADE THE WHOLE CLASS POSSIBLE IS CLOSED WITH IT.** The
drop-body emitter **now says `EMIT-002` aloud when a registered type cannot be
lowered, instead of emitting nothing** — *"that silence is why `npkc` said yes
and `llc` said no"*. **That is the general form of O-N11, O-N14 and O-N17**,
which were three instances of one shape: the frontend accepting and the emitter
quietly declining. **Our harness rule does not change** — the `program` stage
still runs all four steps, because `npkc` exit 0 is not well-formedness — but
the gap it guards has narrowed from a class to whatever remains outside the
registered-type path.

**S-39 — AN OWNING `List<T>` LOCAL ALIVE IN `main` AT EXIT 0 IS REPORTED AS
`WildLeak`, EXIT 94, AT OUR PIN TOO.** Told to us unprompted, found while
writing O-N17's test, and recorded for the author on their side. `exit` runs
joins and defers **and no drops, by decision** (D-183's amendment keeps the drop
walk off the shutdown path), and **a `List`'s buffer is the one managed storage
D-151 counts, because the prelude spells it `wild`.** Their working spelling
until the author rules: **keep the list inside a function that returns**, which
is what every `List` test in their tree does. Their recommendation is that the
buffer allocate through the managed heap's untracked entry, as a channel ring
does.

**What it means here, stated because the answer is not obvious:** for the
prelude's `List<T>` this is a surprise. For **our** containers it is the
enforcement we asked for — `Vec<T>`'s block is `wild` by P-23 precisely so that
an unpaired `vec_free` traps at exit under D-151. **So the same mechanism is a
defect there and a feature here, and the difference is whether the type's owner
intended `wild`.** No action for us; do not "fix" a `Vec` that traps at exit.

**O-N18 is their DEF-22**, recorded with our two controls, to be fixed after the
landing. **And the `string ==` / `TYPE_REFERENCE` §3.2 mismatch is accepted as
our item in their doc-sync backlog** — the language's answer is `.eq` (D-250:
comparisons of owning types are calls, not operators) and **the table is what is
wrong**. They asked for no separate item from us.

**THE RE-PIN IS HELD UNTIL 1.5.2f, AT THE COMPILER SESSION'S REQUEST — ~2 HOURS
FROM 2026-09-06 00:3x, WHEN ONE NOTICE CARRIES BOTH.** 1.5.2e landed and pushed
at **`f6e3537`**; we are **NOT** re-pinning on it. **`aaffb87` remains the pin**,
and the 0.0.6 close is running against it, so the hold costs nothing and moving
the pin under a running close would cost something. **Do not re-pin on a landing
notice that asks you to wait.**

**WHAT 1.5.2e ALREADY CONTAINS, both of them ours.** **O-N18 is FIXED** —
`.len` on a fixed-size array lowers to its constant (their DEF-22). And
**S-39 is fixed in exactly the shape this workbench asked for**: the prelude's
`List<T>` stores through `alloc_managed`, the managed heap's untracked entry,
**prelude-only** — `TYPE-054` from any other module — *"because your `Vec`'s
`wild` count is its enforcement and stays"*. **We asked that the fix not become
a general "D-151 stops counting managed storage", and it did not.** A `List`
alive in `main` at exit 0 now exits 0; our `Vec` still traps, which is P-23's
whole point.

**AND D-264 — THE RULE OUR O-N19 FORCED — IS RATIFIED, WITH ITS IMPLEMENTATION
UNDER HARNESS.** *A bare type parameter, and `Self` in a trait's default body,
is move-only in the body that names it.* **Measured on the compiler's own tree
the new rule refused SEVEN sites, every one a stored `T` parameter, and nothing
else** — which is the number that made it safe to ratify.

**WHAT 1.5.2f WILL REQUIRE OF OUR CODE AT THE RE-PIN — read this before 0.1 is
planned, not after:**

- a **copy of a `T` place in a generic body is `TYPE-046`** unless spelled
  `move(...)`, or `.clone()` under a `Clone` bound;
- a **by-value `T:v` parameter stored into an element, a field, a payload or a
  channel wants `move T:v` and `move(v)`**;
- a **lending `pick` cannot bind a `T` payload**;
- **`#[derive(Eq | Ord | PartialOrd | Clone)]` over an enum with a `T` payload
  is `DERIVE-006`** — `Hash`, `ToString` and `Debug` still derive — because the
  generated `pick` was the same copy.

**`vec_pop<T>` already has the spelling**, because 0.0.5 fixed our own bug
rather than working around theirs — **so the library is already written the way
the ratified rule requires**, which is the return on that call. **The rest of
`src/core/` is not yet checked against the four rules above**; that belongs to
the first dispatch after the re-pin, not to the close.

**Left open for the author as their S-41:** a borrowing `pick` binding form,
which would let a generic enum with payloads derive the four again. **That one
touches `nitpick-time`'s `Layout` vector** — a payload-free enum but for
`Literal(uint16)` — so it is worth watching rather than waiting on.

**O-N19 IS ACCEPTED AS A SOUNDNESS HOLE IN THE CHECKER, AND IT GOES TO THE
AUTHOR TODAY AS A DECISION RATHER THAN A PATCH.** `nitpick-compiler_s0`
confirmed our mechanism reading — `require_move_if_owning`
(`type_expr.npk:404`) asks `type_drops`, which answers **false for an
unsubstituted `T`**, so a bare copy of an owning element inside a generic body
is **never refused**. Not a regression, and **not O-N17's**: the hole predates
both, and step 4 only made its consequence *runnable* where it previously
stopped at `llc`.

**Why it is a decision and not a fix.** A generic body is checked **once, as a
template**, and a move-only rule keyed on *ownership* has no answer for `T`.
Their honest rule: **a bare type parameter is move-only in a generic body** — a
copy of a `T` place is spelled `move(...)`, or `.clone()` under a `Clone` bound
— **the same at every instantiation, and costing nothing at a scalar.** That
changes what the checker *accepts*, so it needs the author's word, and they are
**measuring how much existing code it refuses first** (the compiler's own
sources, `npkg`, the tools, the test suite) before recommending.

**And our fix is ratified rather than tolerated: `move(s[i])` is the spelling
the language means at every `T`.** So `src/core/vec.npk` is now written the way
the rule will require, whichever way the author rules — which is the good
outcome from having fixed our own bug rather than routing around theirs.

**THE ALLOWLIST NUMBERS RECONCILE, AND THE RECONCILIATION IS GOING INTO THEIR
DOCS SO IT STOPS TRAVELLING.** Confirmed exactly: the allowlist is **the
object's 111 GLOBAL symbols plus `main` = 112**; the `.ll`'s **57** are its
`define internal` **functions**; the object's other **106** non-global symbols
are locals of every kind. **So 217 and 166 describe different artefacts and
every number is right** — which is precisely the shape that had one of ours
wrong today. It lands in `BUILD_REFERENCE` §4.1 with **DEF-23** (this finding)
in the docs commit after 1.5.2e.

**1.5.2e IS UNDER ITS HARNESSES NOW, AND IT CARRIES BOTH OF OUR REMAINING
ITEMS.** **O-N18 is fixed** — `.len` on a fixed-size array lowers. And **S-39
is fixed in the shape this workbench asked for**: the prelude's `List<T>` stores
through the managed heap's **untracked entry** (D-263, **prelude-only**,
`TYPE-054` elsewhere) — **and `D-151` keeps counting every `wild` block, our
`Vec` included.** That was the one thing we asked not to be generalised away,
and it was not. **Another re-pin follows the landing notice**; re-pin first,
then re-measure, and the 30-program spread goes back to them after it.

**1.5.2d's STEP STATUS, as of 2026-09-05 evening:** step 1 (the frontend's
three scaling defects) **committed and under its harness**; step 2 (the prelude
trim) **implemented and passing both runners' self-checks**, about to go under
its harness; **the allowlist fix (DEF-21, below) is the step after**; then docs
and the landing notice. **We re-pin when it lands, then re-measure — in that
order**, because a number taken against the old pin proves nothing about the
new one.

**DEF-21 — THE ALLOWLIST FINDING WAS ACCEPTED, AND IT WAS NOT KNOWN.** Raised
by this workbench 2026-09-05 under the lifted constraint and taken up the same
evening as the compiler's **DEF-21**, carrying our measurement with
attribution, **with a harness of its own** as a step in 1.5.2d. **The fix is
exactly the model our arithmetic implied: the allowlist is the runtime's
EXPORTS** — the non-internal `define`s plus the `module asm`'s `.globl` names —
**not every `define`.** Both halves move: the **57** internal defines leave the
list, so a program naming one is refused *at scan time by name* as D-206 meant
rather than at `ld.lld`; and the **2** `.globl` names enter it, since
`npk_clone_raw` was **a false refusal of a legal program**, the worse half.
They are checking whether the harness's `check_zero_dependency` builds its list
the same way and fixing it in the same step, and `BUILD_REFERENCE` §4.1's prose
will say *exports*.

**What made it a finding rather than a report, in their words, is the
arithmetic** — 109 + 2 = 111 identified the object as the authority and showed
the list had been built from the wrong side of it. **A measurement that pins
down the mechanism is worth more than a count that only shows something is
off**, and the difference cost one extra command.

**SEPARATE COMPILATION IS AN OPEN OFFER, DELIBERATELY NOT TAKEN UP YET.** That
session confirmed P-16's failure is not a compiler defect — *a program is one
object plus the runtime; a library is consumed as source through the module
graph* — and offered to put **separate compilation of library objects** to the
author as a design decision with its own row, with a recommendation, **if the
libraries need it. This workbench's answer is NOT YET, and the reason is a
number about to change.** The entire cost of the one-object model is that every
program re-emits the whole prelude, and step 2 removes ~94% of exactly that.
**Asking for a design change now would rest the case on a measurement we are
days from invalidating.** Re-pin when 1.5.2d lands, re-measure the 30-program
spread, and decide against real numbers. **If the case survives the trim, raise
it then; the offer is on the record and does not expire.**

**THE RE-PIN CHECKLIST — assembled 2026-09-05 because none existed and the
re-pin was being carried as a one-line instruction.** §3 has the general
procedure; this is what *this* re-pin owes on top of it:

**STATUS 2026-09-05 16:0x — items 1–5 are DISCHARGED; 6, 7 and 8 remain and
belong to the streams.** 1: answered and the `binary` line is written. 2: the
harnesses finished and the pin was taken after them. 3: `npkrt.o` taken again
and checked — byte-identical, verified not assumed. 4: all four re-measured,
results in the table above. 5: the after-value is measured
(`NITPICK-REACH-003`; **four** identities for `case1`, **six** for `case3` — the
count is per program, see the O-N11 row) and the two transcripts can now be
re-recorded — **that write belongs to `nitpick-time`'s stream at its claim
(W-7)**, not to the orchestrator. **6** (the six stale `list.npk` citations,
three files, two streams), **7** (`probe04b`'s rationale as historical) and
**8** (`check_refs` naming each repository) are unchanged and outstanding.

1. ~~**Establish the target commit and the binary's provenance**~~ — **DONE
   2026-09-05 13:35.** The answer is in the block above: `build/npkc` is a
   working-tree intermediate of 1.5.2 step 0, the pin point is the 1.5.2c
   close, and the compiler session sends the identity. **Still owed: write its
   reply into `PIN.md` as a `binary` line when the pin is taken**, as the
   previous pin did.
2. **Do not pin while a harness is running against the tree the binary came
   from**, and do not write into that tree — `library-sessions-write-scope`.
   Three are running as of 13:27; the notice at ~15:30 is the all-clear.
3. **Take `npkrt.o` again and check it.** Do not carry the identical-hash
   measurement above forward as an assumption.
4. **Re-measure O-N10 and O-N11 against the new pin — and note the compiler
   session's steers, which change what "correct" looks like for both.**
   Re-run **O-N4** and **O-N9** too; probe 04 now costs ~1.24 s, which is the
   point of its discharge.
   - **O-N11 is now a COMPILE-TIME refusal, not a runtime verdict.** A root
     with `main` and no `failsafe` is `NITPICK-REACH-003` **at `main`**,
     whatever the exit code (1.5.1b step 1b), and D-256…D-261 do not touch it.
     A verdict phrased as an exit code is measuring the wrong thing now.
   - **O-N10's shape moved with D-258.** A derived body reaches every member
     *through the trait it derives*, so a payload's type must implement that
     trait — asked at the **call** of `eq`/`cmp`/`clone` and refused there as
     `TYPE-017` naming the derive, the parameter and the bound (D-256),
     **never at the declaration**. A `string` PAYLOAD under the four that bind
     it (Eq, Ord, PartialOrd, Clone) is **`DERIVE-006` at the derive** — a
     lending `pick` cannot bind an owning payload — while a `string` FIELD of
     a struct derives fine through the prelude's four (D-257). `Hash` on an
     enum is the tag's; `ToString`/`Debug` render the variant name. Every
     derived diagnostic reports **at the derive's declaration** (D-259), and
     **a path containing `<derived-` in any output is a compiler defect the
     compiler session has asked us to report.**
   - **New surface to probe at the same time (1.5.2c):** a generic enum now
     derives as a generic struct does, so `Opt<T>` under a derive is legal and
     `Opt<Point>` compares only if `Point: Eq`, asked at the call.
5. **Re-record `nitpick-time`'s two DEF-5 transcripts** — an `npkc`
   `NITPICK-REACH-003` refusal replaces the `llc` failure — and note the
   identity count is **per program**: `case1` names **four**, `case3` names
   **six**. This line once read *"four, not six"*, which was true of `case1`
   and became a general claim two paragraphs later; **six was never wrong, it
   was another program's bill.**
6. **Correct the stale comments citing the deleted `src/frontend/list.npk`.
   THE COUNT IS SIX, IN THREE FILES — NOT FIVE IN TWO.** Re-derived
   2026-09-05 with an instrument that can actually see the library checkouts
   (see the sweep-blindness block below); the old list was produced by a sweep
   that could not. **The board's previous list was wrong in both directions.**
   The six real sites, each fixed at its own stream's claim (W-7):

   | # | Site | What it cites |
   |---|---|---|
   | 1 | `nitpick-regex/tests/probe/probe01_pod_inst_array.npk:24` | `src/frontend/list.npk` by path |
   | 2 | **`nitpick-regex/tests/probe/probe04_inherent_generic_impl.npk:18`** | `src/frontend/list.npk` by path — **a file the old sweep never saw at all** |
   | 3 | **`nitpick-regex/tests/probe/probe04_inherent_generic_impl.npk:47`** | `list.npk` by basename — **same unseen file** |
   | 4 | `nitpick-time/tests/probe/probe06_generic_vec.npk:14` | `src/frontend/list.npk` by path |
   | 5 | **`nitpick-time/tests/probe/probe06_generic_vec.npk:92`** | `list.npk` by basename — **missed by the old sweep** |
   | 6 | `nitpick-time/tests/probe/probe06_generic_vec.npk:107` | `list_init`, a function the deleted file defined |

   **And two the old list counted that are NOT findings:**
   `probe06_generic_vec.npk:49` and `:60` reference `List<T>` and D-246/D-247
   semantically and cite **no deleted path**; the board itself calls `:60`
   "exactly right". Leave them.

   **The mechanism of the error is the durable part.** The old sweep searched
   for the token **`List`** while the property is *"cites the deleted
   `list.npk`"*. Those are different sets: it caught `:107` by accident (that
   line says `list_init`, not `List`) and **missed every `list.npk` basename
   citation**. The same board paragraph asserts *"nothing here declares any
   `list_init`"* while its own count includes the line that names `list_init`
   — **the two halves of one paragraph contradict each other**, and neither
   half was re-derived. D-239's substantive conclusion is unchanged and was
   re-verified: no `struct:List`, no `mod:list`, no `list_push`, no
   `list_reserve`, so **no rename is required anywhere**; only the citations
   are stale.
7. **`probe04b_emission_shape.npk` exists as a 300-row stand-in *because probe
   04 cost 281 s*.** That reason is gone. Keep the file; record its rationale as
   historical rather than current.
8. **Run `check_refs.py` naming EACH repository, after the comment corrections
   and before `git add`**, and gate the commit on it — **reading the check's
   own exit status, not a pipeline's.** **It takes one directory and checks
   only that one:** `check_refs.py .` from the root prints `All clean` having
   examined the root alone (it does at least name `nitpick-libs` in its
   output, which is the one thing that keeps it honest). **Ran clean
   2026-09-05 13:33 over a denominator of seven** — the workbench root, the
   five library checkouts, and `../nitpick-apps/nitpick-posix` — all exit 0.
   Two traps live in this item: *if you pipe it, `$?` is the pipe's last
   command*, which let an ungated commit through on 2026-09-05 (use
   `${PIPESTATUS[0]}`); and **`check_refs` reports a `tracked-file-missing`
   finding** as of `7da5c2d`, so an unstaged deletion is a finding rather than
   a crash — which is the state the mandated pre-`git add` order puts it in.

**A CROSS-REPOSITORY SWEEP RUN FROM THE WORKBENCH ROOT SEES NONE OF THE FIVE
LIBRARIES, AND SAYS NOTHING ABOUT IT. BOTH OF THIS ECOSYSTEM'S CANONICAL SWEEP
TOOLS ARE AFFECTED. Measured 2026-09-05 by the fifth orchestrator; this is how
checklist item 6's site list was found to be wrong.**

Two independent causes land on the same silence:

- **`grep` on this machine is `ugrep` 7.8.4, installed at `/usr/bin/grep`.**
  `grep --version` says so; `which grep` does not. ugrep honours ignore files
  in recursive mode, and the workbench's own root `.gitignore` opens with
  **`/*/`** — it ignores *every* top-level directory, which is exactly how this
  repository avoids embedding a library as a gitlink. So the ignore rule that
  makes the workbench correct is the rule that makes its sweeps blind.
- **`git grep` from the root cannot see a library either**, and for a
  different reason: each library is a **separate checkout**, so its files are
  not in this repository's index at all. `git grep -l -i derive -- '*.npk'`
  from the root returns **nothing**, correctly and uselessly.

**The measurement, one pattern, five tools, same tree:**

| Invocation | `.npk` files matching `derive` |
|---|---|
| `grep -rl -i derive --include='*.npk' .` (from the root) | **0** |
| `git grep -l -i derive -- '*.npk'` (from the root) | **0** |
| `grep -rl -i derive --include='*.npk' nitpick-time` | 7 |
| `grep -rl -i derive --include='*.npk' --no-ignore-files .` | **14** |
| `find . -name '*.npk' -not -path '*/.git/*' -print0 \| xargs -0 grep -l -i derive` | **14** |

**The instrument was commissioned before it was believed:** the two tools that
see everything were diffed against each other and agree on the same 14 files,
so 14 is a measurement rather than one tool's opinion.

**Why this is the worst instance of `PLAYBOOK.md` §6's shape yet found here —
the sixth — and worse than `check_refs .`'s.** A `check_refs .` run at least
prints the name `nitpick-libs`, so its denominator of one is visible to a
reader who looks. **A sweep that matches nothing prints nothing at all.** There
is no verdict to be sceptical of, no count to ask for the denominator of, and
the output of "swept, no violations" is byte-for-byte the output of "swept
nothing". Every discipline this workbench has built — *a list of files is
produced by `git grep`, never by recall*; *ask for the denominator, not the
verdict* — routes straight through the one failure mode that produces no
number to interrogate.

**And this project has already been bitten by the same `.gitignore` line
once.** That file's own comment says each workbench directory must be
un-ignored by name *"or it vanishes silently — which is exactly what happened
on the first attempt to add the plugin."* The note was written about tracking;
nobody carried it across to searching.

**What it actually invalidated, and what it did not.** Checklist item 6's site
list: **wrong**, three sites missed including two in a whole file
(`nitpick-regex/.../probe04_inherent_generic_impl.npk`) that no previous sweep
had ever seen. D-248's *"swept all six repositories: zero violations"*:
**re-verified and correct** — 0 violations over a stated denominator of **87**
`.npk` files, a denominator the original claim never gave. Every other
cross-repository count on this board was produced before this was known and
**should be re-derived at the sweep that next touches it**, not trusted.

**THE RULE, and it is cheap: a sweep across libraries is run per repository by
name, or with `find … -print0 | xargs -0 grep`, or with `--no-ignore-files`.
Never with a bare `grep -r` or `git grep` from the workbench root.** State the
denominator with every result. A sweep that reports no matches must also report
how many files it opened, or it has reported nothing.

**Why the re-pin was NOT done at this stopping session:** it would leave a fresh
toolchain with **no verified measurement against it**, discarding the one this
session paid for. Everything verified today — O-N4, O-N9, O-N10, O-N11 — was
measured against **`94874ce`**, and that is the pin those verdicts belong to.
~~**The next session re-pins as its first action**~~ — **superseded 2026-09-05:
there is nothing to pin yet.** The re-pin is now *scheduled*, not owed on
sight: wait for the compiler session's 1.5.2c landing notice (expected ~15:30
on 2026-09-05), then run §3 with the checklist above. **Take `npkrt.o` again
and check it rather than assuming it unchanged** — DEF-12 already caught
this ecosystem once assuming the runtime half was identical.

**D-239 — step 5b moved `List<T>` and its functions into the PRELUDE, deleted
`src/frontend/list.npk` and its 46 imports, and a program's own `List` is now
refused by the loader. SWEPT ACROSS ALL FIVE LIBRARIES: NO COLLISION.** Nothing
here declares a `struct:List`, a `mod:list`, or any `list_init` / `list_push` /
`list_reserve` — **re-verified 2026-09-05 over a stated denominator of 87 `.npk`
files, so this conclusion stands and no rename is required anywhere.** ~~Five
occurrences of the token exist~~ — **that count was wrong, and so was the site
list built from it.** The property is *"cites the deleted `list.npk`"*, the old
sweep matched the token *`List`*, and the two sets differ: **six sites in three
files**, one of them a file no earlier sweep had ever seen. The corrected table
is checklist item 6 above; the reason the sweep could not see it is the
sweep-blindness block above. Every one is still **a comment**, so the residue is
stale citations to correct at the re-pin, each at its own stream's claim (W-7).
Note
`probe06_generic_vec.npk:60` already says D-247 makes *the COMPILER's* `List<T>`
owning, which is exactly right and consistent with RX-126.

**CATALOGUE-DON'T-RAISE IS LIFTED. Ruled by the author 2026-09-05: "raise as
found."** Defects met in library work now go to the compiler session **as they
are found, with their measurements**, rather than being held for a batch. The
constraint's original rationale — a closing fix batch on the compiler side —
had expired, and two orchestrators in a row declined to lift it on their own
judgment, which is the right instinct and is also how an expired rule survives
for days. **It was resolved by asking.** The evidence pointed the same way
before the ruling: **~~O-N16~~ was catalogued rather than raised and the
compiler session closed it the same day anyway**, so cataloguing bought nothing
there; and that session has since **asked us explicitly** to report one class on
sight — any output path containing `<derived-`. Raising still means what W-27
made it mean: **state what the defect blocks**, what it merely inconveniences,
and what it does not touch. Sequencing remains the author's.

**~~O-N16~~ — CLOSED UPSTREAM 2026-09-04, same day it was catalogued.** The
compiler session corrected DEF-8's closing sentence in its `OPEN_DECISIONS.md`
§2f to give the reason rather than the false premise — our recipes *do* pass
copyable fields out of locals; a hand-written container never drops, so the old
clear skipped no drop; we are outside the recognition, not outside the shape.
Their commit `8dbef43`, docs only. **Catalogued rather than raised, and closed
anyway** — worth noting for the next session that the catalogue-don't-raise rule
cost nothing here.

**S-38 — RATIFIED BY THE AUTHOR AND IN FLIGHT AS THE COMPILER'S 1.5.2d. NO
LONGER OPEN, AND NOT OURS TO RE-REPORT.** Confirmed to this session by
`nitpick-compiler_s0` on 2026-09-05: they put it to the author directly with the
measurement and the recommendation, and he ratified it — *"lets go with your
recommendation"*. **Do not re-report it.** The previous board carried it as
*"the author decides"*, which was true when written and is now stale; a session
reading only that line would report a settled decision a second time.
**Originally raised by this workbench 2026-09-05 and taken up the same
afternoon** as the compiler's `OPEN_DECISIONS` **S-38** (their `a882188` —
verified here as docs-only, one file, one insertion, no `src/` or `runtime/`,
so **our pin at `0dfddac` is unaffected** and `sha256sum -c` still passes).
**The compiler session explicitly declined to close it as the price of D-257**
and asked that we carry it as open. It confirmed the mechanism: D-257's
generated scalar impls are **348 rows in thirteen families**, and 1.5.2b had
already recorded that *"every prelude impl body is emitted whether reached or
not"* with **+2.2% IR and +14% frontend time** measured on the compiler's own
tree. **What nobody had measured is the fixed per-program cost — which is
exactly what a per-program harness pays, and is why this workbench saw it and
they did not.** Of their three options the author took **(1)** reachability-driven
emission of non-generic prelude bodies via the demand walk the emitter already
runs for generic instances — deterministic, semantics-neutral, and *"worth doing
before 1.5.3 hangs contract obligations on every prelude function"*. But their
option **(2)** — *measure the frontend's share first* — was carried out before
any of it started, **and it changed the answer. That is the part worth reading.**

**THE COST IS NOT THE PRELUDE'S SIZE.** On the floor-only probe the **frontend
holds 0.72 s of the 0.82 s** and emission only **0.10 s**, and a profile names
**three scaling defects** rather than prelude bulk: the bindings analysis
allocating one state slot **per statement of the whole program, for every
function** (**57%** of the run), and the type interner and the string interner
deduplicating by **linear scan** (13%, plus part of the lexer's 12%). Those are
fixed first as ordinary engineering with **no language change**; reachability-
driven emission follows (587 of the probe's 608 emitted functions are prelude
bodies). **Why this lands harder here than the raise assumed:** all three
defects scale with the number of programs compiled, so a harness that compiles
**many small programs pays them repeatedly** — the same structural asymmetry
that let this workbench see the cost when the compiler's own harness could not.
**And the durable lesson is option (2) itself: the obvious cause was measured
before it was believed, and it was wrong.** We had attributed the whole +0.75 s
to D-257's generated impls; five-sixths of it is three unrelated scaling
defects. Our measurement of the *cost* was sound and our inference about its
*cause* was not — and nothing on this board had marked that inference as one.

**We stop measuring this per program.** The two data points and the
22-of-30 constancy argument are what the decision needs, and any fix arrives
with its own before/after. **One canary is kept:
`nitpick-time/tests/probe/probe11d_floor_only.npk`, whose `.ll` is 845 282 B at
`0dfddac`** — that is the number to watch, and a change in it is the signal.

**THE RE-PIN IS DONE — `aaffb87`, 2026-09-05 22:47 — AND THE CANARY LANDED ON
ITS PREDICTION.** 1.5.2d closed and this workbench re-pinned immediately, then
re-measured. **The prediction was a real test and it passed:** the board said
*check the VALUE, not merely that it moved*, expecting ~50 000.

| | `0dfddac` | `aaffb87` | |
|---|---|---|---|
| canary `.ll` | 845 282 B | **50 560 B** | **−94.0%** |
| canary functions | 608 | **14** | predicted 14, **exact** |
| **full harness run** | **240 s** | **41.8 s** | **5.7× faster** |
| harness verdicts | 40 units, 0 fail | **40 units, 0 fail** | **unchanged** |

**The one-byte gap against their predicted 50 561 has a MEASURED cause, and it
is not the one first written here.** This board said *"two different source
files"* — a plausible guess, offered as fact. `nitpick-time` 0.0.5 then measured
the real mechanism: **an emitted `.ll`'s byte count is PATH-DEPENDENT and the
object's is not.** The same source compiled from two directories whose names
differ by **one character** gives `.ll` sizes **14 bytes apart** — one byte per
`npk.site.paths` entry — while the `.o` and the linked binary are
**byte-identical**. So the byte is the path, and the function count matching
exactly is the real signal. **THE RULE: quote the OBJECT, not the `.ll`.** Every
IR byte-count on this board is therefore a measurement of the emitting
directory as much as of the compiler — including the canary itself, which is
why the count of FUNCTIONS is the half worth trusting.

**THE HARNESS IS GREEN AT THE NEW PIN AND NOTHING BROKE**, which was not
guaranteed: the compiler session warned that *"every emitted module holds only
the prelude functions it references, so any probe asserting a prelude symbol in
IR needs a use"*. No probe here did. **40 units, 0 failures, 5 pending — the
same verdicts, in a sixth of the time.**

**ALL FOUR DISCHARGED STOPS RE-MEASURED, and one improved.** **O-N11** —
`case1` names **4** identities and `case3` **6**, unchanged, so today's
per-program correction still holds at the new pin. **O-N4** — `probe04` is now
**1.18 s at 26 336 KiB**, against 2.03–2.06 s at ~119 MB on `0dfddac`: faster
*and* a quarter of the peak, so it stays discharged with room. **O-N9** —
`BORROW-012` and `BORROW-001` unchanged. **O-N10** — covered by the harness's
derive probes, green.

**OUR TWO DEFECTS BOTH LANDED IN THIS PIN.** **O-N17 is FIXED** — all five
cases now link and write objects, including `case1` and `case5`, which produced
`llc` exit 1 and no object at `0dfddac`; their IR also fell from 850 377 B to
55 652 B. **DEF-21, our allowlist finding, is 1.5.2d step 2b** — the allowlist
is now the runtime's **exports**: 112 entries with `main`, both `.globl` names
in, the 57 internal names out. **O-N18 still refuses** (`NITPICK-EMIT-002`),
as expected: it is their DEF-22, scheduled after the landing.

**WHAT CHANGES FOR EVERY LIBRARY AT THIS PIN, and the last one is a trap:**
`vec_pop`, `vec_set`, `vec_clear`, `vec_truncate` and `vec_free` at an owning
`T` link and drop; a program naming one of the **57 internal runtime symbols**
is now refused **at the scan, by name**, instead of at `ld.lld`; `npk_clone_raw`
is allowed, so a legal program that was falsely refused now passes; and
**every emitted module holds only the prelude functions it references, so any
probe asserting a prelude symbol in IR needs a USE.** `nitpick-time` has none;
**the other four repositories must check at their next claim.**

**THE CANARY IS NOW EXPECTED TO MOVE, AND WE KNOW ROUGHLY WHERE TO — WHICH
MAKES IT A REAL TEST RATHER THAN A TRIPWIRE.** `nitpick-compiler_s0` measured
1.5.2d step 2 on the same probe on their side: **845 282 B → about 50 000 B**,
a ~94% cut. So the next session must not read the change as a defect — read it
as the landing — **and must check the VALUE, not merely that it moved.** A drop
to ~50 000 confirms the trim; **a drop to something else, or no drop at all, is
the finding**, and it is one we could not have stated yesterday because we had
no expected value. **An expected number turns a canary into a prediction.** `nitpick-compiler_s0` sends the before/after at that point and has
asked for our 30-program re-measure afterwards, **which we should run**: it is
the only per-program evidence either side has, and re-running a measurement we
already know how to take is the cheapest confirmation available. **Re-pin
before re-measuring**, since a number measured against the old pin proves
nothing about the new one — that is the rule this workbench already paid for
once at the 0dfddac re-pin.

> **AND WE DO NOT, IN FACT, KNOW HOW TO TAKE IT AGAIN — THE 30-PROGRAM SET IS
> RECORDED NOWHERE. Found 2026-09-06 02:4x by the seventh orchestrator while
> waiting for 1.5.2f, roughly forty minutes before it would have bitten.**
> Searched exhaustively: `BOARD.md` (four sites), `RECORD.md:3013`–`3017`,
> every `meta/` document, every `.txt`/`.csv`/`.py`/`.sh` in this workbench
> tracked or not, and the compiler's own `meta/` — **only the RESULT survives.**
> *"30 programs across two libraries, 22 sit at exactly 388 765, all 8
> exceptions are derive or enum programs"* names **no program, no library and
> no selection command.**
>
> **This is the same defect as hazard 6, in a measurement we OWE somebody**: a
> result published over a denominator nobody wrote down. The tree sweep's
> version cost nothing because the answer happened to be clean; this one costs
> the re-measure its comparability, because a differential over a *different*
> 30 programs cannot be checked against *"22 of 30 at exactly 388 765"*.
>
> **What is still sound, and it is not nothing.** The floor program is described
> precisely enough to rebuild — *"a 14-line program that only exits 0"*, **456 517
> B → 845 282 B**, and the 30 000-row program at the identical delta. That pair
> is the whole load-bearing claim (a constant independent of input size is a
> prelude cost, not a compile-time regression) and it survives without the set.
> **The 30 were the widening, not the argument.**
>
> **So the re-measure is re-founded rather than repeated, and it says so out
> loud.** Define the set in a committed file **before** running it, by discovery
> and not by listing (`PLAYBOOK.md` §7): every program under `tests/` that
> compiles clean under both pinned binaries, enumerated by command, **with the
> count printed beside the verdict**. Report it to the compiler session as a
> **new denominator** — the floor pair carried forward as the continuous
> measurement, the spread restated as first-of-its-kind under a stated set.
> Claiming continuity we cannot demonstrate would be the same overstatement this
> board has now caught four times.
>
> **Take the count when NO WORKER IS LIVE.** `nitpick-time` is being written by
> `s2-ntime-0.1.0-0235` as this is written, so any program count taken from it
> now is a moving target — which is how unstable numbers get published in the
> first place.

### 1.5.2h IS LANDED — pin target `c81efa5`, notice 2026-09-06 08:0x. **RE-PIN HELD: A CLAIM IS IN FLIGHT. AND THIS ONE IS NOT BOOKKEEPING.**

**`nitpick-compiler_s1` IS NOW THE COMPILER ADDRESS; `_s0` HAS ENDED.** Update the
roster above when the lock next moves.

**Unlike `0ba21ef`, `src/` MOVED, so the emission moved with it.** `npkrt.o`,
`builder.o` and `builder` are unchanged; `build/npkc.ll` is now
**`af2bf3dd…` at 21 688 240 B**, was `05457db4…` at 21 514 197 B. The canary's
floor-only probe is **unchanged at 50 561 B / 14 defines** — their stated
prediction, *a program with no `pick` is untouched*, held.

**THERE ARE NOW THREE DIGEST TABLES AT THREE COMMITS AND THIS IS THE THIRD TIME
THIS BOARD HAS HAD TO SAY SO. READ THIS BEFORE COMPARING ANYTHING.**

```
0ba21ef / 3d15ac9   build/npkc.ll  05457db4...  21,514,197 B   <-- WHAT OUR CI MUST MATCH
c81efa5             build/npkc.ll  af2bf3dd...  21,688,240 B   <-- newest, and NOT our target
```

**`nitpick-regex`'s CI pins `3d15ac9` (`ci.yml:82`, verified).** Its digest step
therefore prints **`3d15ac9`'s** emission, and the only legitimate comparison is
against **`05457db4…`**. **Comparing it against the newest number would report a
false difference — and under D-265 a difference in `build/npkc.ll` between two
machines IS a compiler defect, so the false report would be a defect report.**
The trap is not hypothetical: the outgoing orchestrator laid an identical one for
itself inside an hour, and this board already carries a warning under the second
table.

**ADJUDICATION (b) IS STRONGER THAN BEFORE, AND THIS BOARD FIRST SAID THE
OPPOSITE. CORRECTED 2026-09-06 08:2x AFTER `nitpick-compiler_s1` PUSHED BACK.**
The cycle-0.0 auditor established that `build/npkc.ll` and
`.internal/quickemit/npkc.ll` were byte-identical at `05457db4…`, which is what
makes our CI's `quickemit` artefact a legitimate stand-in under D-265 §5. When
the compiler rebuilt at `c81efa5`, this board recorded that the evidence was
**"now unreproducible from the tree"**. **That was wrong.** Measured here after
the challenge: both paths now read **`af2bf3dd…` at 21 688 240 B and `cmp`
returns 0** — the two builders agree again, at a second commit, by an independent
measurement.

**THE ERROR WAS CONFLATING A MEASUREMENT'S INSTANCE WITH THE FACT IT
ESTABLISHES.** What legitimises the substitution is not the digest `05457db4…`;
it is the **property** that `npkg`'s ladder and the harness's `quickemit` path
emit identical bytes. A property that re-derives is not lost when one instance of
it is overwritten — **that is what makes it a property.** So the fact now holds
at **two commits by two independent measurements**, which is better evidence than
the single reading this board was mourning.

**And the moral drawn from it was backwards too.** The original note said this
was "the reason to prefer a recorded measurement over a repeatable one". The
opposite is true here: **the repeatable property is the durable thing, and the
recorded number was only load-bearing while the property was wrongly believed
unrepeatable.** Record the number *and* the command that regenerates it; when
they disagree about what survives, the command wins.

**D-266 — S-41 IS RATIFIED, AND IT LIFTS A RESTRICTION EVERY LIBRARY HERE IS
BUILT AGAINST.** A **lending `pick`'s binding is now a read-only VIEW of the
payload in place** — typed as the payload, read by value, no copy at the bind, no
drop of its own — so an owning payload (`string`, `List`, a bare `T`) binds
without consuming. **D-264's four consequences shrink to two:** a copy of a `T`
place still needs `move(...)` or `.clone()`, and a by-value `T:v` stored anywhere
still needs `move T:v + move(v)`. **The two that LIFT are the two that bit us:** a
lending `pick` binds a `T` or `string` payload, and **derive of `Eq`/`Ord`/
`PartialOrd`/`Clone` over a `T` or `string` payload generates again — all seven
do.** **That is the restriction `nitpick-regex`'s derive probes were written
against, and the board's note that `nitpick-time`'s `Layout` vector was "worth
watching rather than waiting on" is now resolved in its favour.** Neither is
actionable until the re-pin; **neither library may assume it before measuring at
`c81efa5`.**

**The view's rules, so a worker does not discover them by being refused:** no
address of it — assignment to it or a part, `@`, `$$i`, `$$m`, a pointer-receiver
call (`Self->` methods; use `pick (move(v))` or a by-value receiver), an operation
of a stateful kind, and binding a view of an arena/lock/guard/atomic/channel/dyn
payload at all are **`NITPICK-TYPE-066`**. The **selector is FROZEN** inside an arm
that binds a name — assignment, `move`, `@`, a pointer-receiver call or a nested
`pick (move(v))` are **`NITPICK-TYPE-067`** — though an arm binding `_` or nothing
may write it. `move` or `pass` of a view is `TYPE-047`; a copy of an owning view is
`TYPE-046`. The consuming form is unchanged, and **a view across an `await` is
sound.**

**DEF-24 also landed, and it is a hole we could have fallen into:** `TYPE-063`
refused `@`/`$$i`/`$$m` on a limited binding but **not the implicit address a
pointer-receiver method call takes**, so a limited struct written through `Self->`
with no trap was accepted. Now refused. They offer a probe worth holding:
`drop p.bump();` with `bump = NIL(Pt->:p)` under a `Rules` on `Pt`. Separately,
`drop` over an already-refused operand no longer adds a second `TYPE-042`
sentence.

**DEF-25 — OUR DEFECT REPORT WAS CONFIRMED, IS BEING FIXED NOW, AND REACHED
FURTHER THAN THE REPORT DID.** `nitpick-compiler_s1` reproduced our shape on
`c81efa5` — **so it is NOT fixed there** — and instrumented it with
`NPK_HEAP_STATS`: at 1 M calls the empty case reads `allocated=16000000
peak_live=16000000 count=1000000` against `allocated=1000000 peak_live=1` for
`("", "a")`. **16 B per call never freed; our 32.2 B/call is that plus the block
header** — two instruments, one phenomenon, and the numbers reconcile rather than
compete. Mechanism confirmed exactly as read.

**TWO CONSEQUENCES BEYOND WHAT WE FILED, AND THEY ARE THE INTERESTING PART.**
(1) The prelude's `impl:string:Clone` **is** `string_concat(self, "")`, so
**`.clone()` of an empty string leaks the same block** — which reaches every
consumer of the language, not only us. (2) `string_concat(x, "")` is the
compiler's own copy idiom, at **234 sites in its `src/`**, so **the compiler has
been leaking in its own build.** *A library audit of a nine-line accessor found a
runtime defect in the compiler's self-hosting.* The fix is the slice's branch in
the concat, landing as **1.5.2i** under a full harness with a cost unit holding
the empty loop's peak to the one-byte loop's.

**THE PREDICTION WAS MADE BEFORE THE FIX AND IT HELD — VERIFIED HERE, ALL SIX
LINES, NOT TAKEN ON REPORT.** They said in advance that `build/npkrt.o` would
move and `build/npkc.ll` would not, because the runtime is assembled beside the
emission rather than compiled into it. **1.5.2i is pushed at `fe42dba` and the
six lines read exactly as predicted:**

```
npkrt.o    67cc8186...  55,648 B     MOVED   (was c9ddbcff... 55,576 B)
builder.o  3b5f868d...  unchanged
builder    fe528b03...  MOVED   (linked with npkrt.o)
npkc.ll    af2bf3dd...  UNCHANGED    <-- THE PREDICTION, CONFIRMED HERE
npkc.o     98606632...  unchanged
npkc       85ef5904...  MOVED   (linked)
```

The two source-derived objects held; the three things linked against the runtime
moved; the emission did not. **A prediction stated before the measurement is what
makes an unchanged reading evidence rather than a shrug** — the canary's flat
prediction across `aaffb87` and `3d15ac9` was the first instance of this and this
is the second. Canary at `fe42dba`: 50 561 B / 14 defines, **IR byte-identical**
to 1.5.2h's close.

**⚠ THE ONE THING THIS CHANGES FOR OUR NEXT RE-PIN, AND IT WILL LOOK LIKE A
DEFECT IF NOBODY READS THIS FIRST. `npkrt.o` HAS MOVED FOR THE FIRST TIME.** This
workbench's pin ritual has `cmp`-verified `npkrt.o` **byte-identical** at every
re-pin since DEF-12 made it a habit — `0dfddac`, `94874ce`, `aaffb87`, `3d15ac9`
all carry the same `c9ddbcff…` / 55 576 B. **At the next re-pin it will be
`67cc8186…` / 55 648 B and that is CORRECT**, because DEF-25's fix is *in the
runtime*. **An orchestrator applying the standing habit will find a difference
where four consecutive readings found none and may report a defect.** It is the
opposite face of the RX-120 trap: there, a pin-dependent measurement was recorded
as permanent; here, **four identical readings hardened into an expectation that
was never a rule.** Verify `npkrt.o` against the *notice*, never against the
previous pin.

**AND THE ARITHMETIC CLOSES THE LOOP EXACTLY.** The compiler's own build now
allocates **17 264 fewer bytes in 1 079 fewer allocations** — and **1 079 × 16 =
17 264**, checked. Every single leaked byte is accounted for as an empty
concatenation, with no residue and nothing hand-waved. **That is what a complete
attribution looks like**, and it is worth more than the fix: it proves the class
was closed rather than merely reduced.

**Their verification of our shape after the fix:** 8 000 000 empty calls under
`ulimit -v 65536` **exit 0** where they exited 92; 200 000 empty calls read
`allocated=0 peak_live=0 count=0` where they read `3200000 / 3200000 / 200000`.
`tests/cost/empty_concat.toml` now holds the empty loop's peak to 4× the
one-byte loop's, so the class cannot silently return. **`BUILTIN_REFERENCE`'s
`string_concat` row now says an empty result allocates nothing, as the slice's
row already did** — the documentation asymmetry closed with the code asymmetry.
**`impl:string:Clone` is unchanged and correct now, and nothing in library code
needs a guard.**

**WHAT THIS DOES TO BL-4's DISPOSITION, so the next worker does not guess.** The
library-side guard is **not to be written** — the root cause is being removed
upstream, and writing it would convert a compiler defect into a permanent library
house rule for no reason. **But BL-4's other half is ours regardless of any
compiler fix:** `bytes.npk:339-342` asserts something false about
`string_concat`, cites a measurement absent from the tree, and cites `exit 0` for
a managed body where this repository's own S-22 says that instrument cannot see
one. **That comment is a library defect and does not wait for 1.5.2i.** The
`Bytes` memory-cap pair is also owed either way, since nothing currently gates
that type the way `Vec` is gated.

**They read our instrument revision and it found something on their side.**
`check_refs.py` at `2b7d123` counts 63 where the previous counted 62; the extra
is a home path in `meta/roadmap/done/1.4/convert_family.py`, **a 1.4 archive
file, recorded in their 1.5.2h record and deliberately not rewritten.** So the
widened leak scan's first cross-repository effect was to surface a real instance
in the compiler, and the owning side judged it and left it — **which is the right
shape: the tool reports, the owner decides.**

---

### 1.5.2g IS CLOSED — pin target `0ba21ef`, notice received 2026-09-06 05:30. **DO NOT RE-PIN YET, AND THERE IS NO REASON TO WANT TO**

**Notice from `nitpick-compiler_s0`, which is closing; `nitpick-compiler_s1` is
the address from here.** The claim is that the compiler's bytes are **UNCHANGED**
from `3d15ac9` — `src/` did not move, only `npkg` and the documents did — so the
re-pin is **bookkeeping, not a re-measure.**

**VERIFIED HERE RATHER THAN TAKEN ON REPORT, by `sha256sum` against this
workbench's own pinned copies, 05:3x:**

```
npkc      3b7d6aa0d86215b37e0b24bf00fc9481cb651057d93e5cad89b2763c6e82c9e7  7351160 B  MATCH
npkrt.o   c9ddbcffd32eccc7787bd71c39ebefd25913170a9fae48de32eb53ca68b2239e    55576 B  MATCH
```

**Both match the `3d15ac9` pin exactly, so the claim stands and the running
worker is unaffected** — `nitpick-regex` 0.0.4 is executing against the identical
compiler under a different name. **A CLAIM IS IN FLIGHT, so orchestrate §2
forbids the re-pin anyway; take it when the claim clears**, and take it as the
cheap bookkeeping it is rather than repeating §3's guards on bytes already
verified.

**D-265 LANDED, AND IT IS THIS WORKBENCH'S OWN CI FINDING RATIFIED (their S-42,
ours).** Its four parts: (1) **the toolchain pin STAYS A VERSION** — a
tool-binary digest would refuse every machine but one; (2) the asymmetry with
z3's digest pin under D-218.1 is **deliberate**, because a solver's output is a
committed *verdict* while a toolchain's is *checked bytes*; (3) **`build/npkc.ll`
is the identity claim that holds across machines** — a difference THERE between
two machines is a compiler defect, to be reported with both files, while the
object's and the binary's identity is per toolchain build; (4) every `npkg`
ladder run now prints **one `sha256` line per intermediate in ladder order**,
held by the harness against an independent digest of the same file (`ec8ee62`
the code and cross-check, `0ba21ef` the docs; both harnesses green, 1099 parity
verdicts, the cross-check silent on its first run). **Pin notices here can quote
those lines verbatim from now on instead of re-deriving them.**

**THE MEASUREMENT D-265 §5 ASKS OF THIS SIDE, AND IT IS NOW THE SHARPEST THING
THIS WORKBENCH OWES.** The first **cross-machine** comparison of
`build/npkc.ll`: our runner's digest against theirs —
**`05457db4e98b18a97033eac8bfbe1cfbcddf72f6cf5373dbb99d3693ce94d367`,
21 514 197 B**. **Equal** means the toolchain build explains the earlier `npkc`
difference between machines and **no compiler item exists**; **different** is a
defect report they explicitly want, with both files. **This is a CI job, not a
local one** — the library workflows already check out the pinned compiler and
build it, so the digest is captured on a genuinely different machine. It cannot
be taken here, and taking it locally would answer a different question.

**Their canary reads 50 561 B / 14 defines, flat since 1.5.2d.** Ours is a
**different program** — `tools/canary.npk`, 50 482 B — so **the byte counts are
not comparable and must never be compared**; the **14 defines** is the shared,
path-independent number, and they expect 14 at `0ba21ef` as we measured at
`aaffb87` and `3d15ac9`.

---

### 1.5.2f IS CLOSED — pin target `3d15ac9`, notice received 2026-09-06 03:2x, RE-PIN TAKEN

**Verified against the compiler tree read-only before being written here, not
taken on report:** `3d15ac9` is real and is their `HEAD`, tree clean, level with
origin, and all three claimed commits exist with matching subjects — `94af975`
(D-264 step 1), `1ed4934` (step 2, the docs, *"1.5.2f CLOSES"*), `3d15ac9`
(**S-42, recorded from THIS workbench's first CI run**). Their harnesses: ok 56;
223 programs at `-O0` and under `opt -O2`; 81 type and 10 derive rejection
files; verify 141 obligations with 116 discharged, unchanged; parity 1099
verdicts agreeing with `npkc` byte-identical between two runners; **prelude-trim
101 prelude functions kept, all referenced**.

**THE RE-PIN IS GATED AND THE GATE IS OURS, NOT THEIRS.** Orchestrate §2 —
**never re-pin while any claim is in flight** — and `nitpick-time` is claimed
with 0.1.0 awaiting verification. So the order is: **verifier PASS → advance the
board → then §3's pin procedure**, whose two-minute binary-age guard then gets
its turn. At 03:27 their `build/npkc` was **124 seconds old**, which clears that
guard by four seconds; it will be comfortably aged by the time the gate opens.
**A landing notice is not a re-pin trigger.**

**The six digests at `3d15ac9`:**

| Artifact | Digest | Bytes | |
|---|---|---|---|
| `builder.o` | `3b5f868dbab44253…` | 8 086 688 | unchanged from `aaffb87` |
| `builder` | `f5c7f5174fc6fa11…` | 7 014 696 | unchanged |
| `npkrt.o` | `c9ddbcffd32eccc7…` | 55 576 | **unchanged — `cmp`-verify at the re-pin rather than assume (DEF-12)** |
| **`npkc.ll`** | `05457db4e98b18a9…` | 21 514 197 | **THE EMISSION** |
| `npkc.o` | `3cd6ba4bfb914987…` | 8 469 288 | |
| `npkc` | `3b7d6aa0d86215b3…` | 7 351 160 | |

> **DO NOT COMPARE THIS TABLE AGAINST THE `aaffb87` TABLE ABOVE. There are now
> two digest tables on this board at two different commits, and comparing them
> is a category error waiting to happen.** The six digests localise a difference
> **BETWEEN MACHINES AT ONE COMMIT**; they say nothing across commits. `npkc.ll`
> moved `f0abbfd0…`/21 483 280 B → `05457db4…`/21 514 197 B, **+30 917 B**,
> between `aaffb87` and `3d15ac9` — that is a different compiler, and the change
> is the expected consequence of shipping D-264, **not** the "`npkc.ll` differs
> = compiler defect" rule firing. That rule is about one commit built in two
> places. **Three of the six being unchanged across versions is a convenience,
> not the invariant.**

**THE CANARY PREDICTION IS FLAT, WHICH IS A STRONGER TEST THAN A MOVING ONE.**
Their floor-only probe under `3d15ac9` reads **50 561 B of `.ll` and 14
`define`s — identical to 1.5.2d's**. So our 14-line floor program should land at
**50 560 B and 14 functions** (the byte is the path, D-236), and **the 1.5.2f
point on our floor series should be FLAT. Anything else is a finding.** This is
the third prediction in this series and the previous two were hit exactly; a
prediction that forbids all movement can be falsified by any movement, which is
what makes it worth taking.

**D-264, AS IT BINDS LIBRARY CODE — the four rules, in their words.** A copy of
a `T` place is `TYPE-046` unless spelled `move(...)` (a plain copy at a scalar;
**the source is spent at ANY type**, `MOVE-001` on a later read) or `.clone()`
under a `Clone` bound. A by-value `T:v` stored into an element, field, payload
or channel is spelled **`move T:v` in the signature and `move(v)` at the
store**. A lending `pick` cannot bind a `T` payload. `#[derive]` of `Eq`, `Ord`,
`PartialOrd` or `Clone` over an enum with a `T` payload is `DERIVE-006` —
**`Hash`, `ToString` and `Debug` still generate, and a `T` FIELD in a struct
derives all seven**. `vec_pop<T>` already has the required shape. **The rest of
`src/core/` is unchecked against this and the stored by-value `T:v` is the one
to hunt** — a shape a library writes without thinking, with no diagnostic before
now to have taught us otherwise.

**Open with the author on their side:** **S-41** (a borrowing `pick` binding
form, which would give generic enums with payloads the four derives back) and
**S-42** (ours: the pin is a version and a version is not a binary; `npkg build`
to print the six digests; the emission's digest in every pin notice) — recorded
with recommendations, **not yet ruled**.

**THE COMPILER SIDE IS ROTATING.** `nitpick-compiler_s1` holds this notice's
contents and **is the address once `_s0` closes**.

---

### THE RE-FOUNDED SPREAD — the specification, agreed with `nitpick-compiler_s0` 2026-09-06 02:5x

**Read the inversion first, because a session that remembers the old number
will read the new result exactly backwards.**

| | Before 1.5.2d | After the trim |
|---|---|---|
| **22 of 30 at exactly 388 765 B** | **the FINDING** — a constant delta independent of the program proved the prelude was emitted whole into every program | **the FAILURE SIGNAL** — 1.5.2d keeps only the prelude items a program *references*, so a delta that is constant across programs means **the trim did not apply** |
| a spread that VARIES per program | would have been the anomaly | **is the expected, healthy shape** |

**`nitpick-compiler_s0`'s words, so this is not paraphrase drift:** *"the shape I
want to see is a spread that VARIES with what each program uses, with no
constant delta anywhere. A constant delta reappearing under a stated denominator
would be the trim failing to apply, a compiler defect, and I would want the
program that shows it."* **So if a constant turns up, do not report it as
agreement with the earlier measurement — report it as a defect and name the
program.** No comparison against "22 of 30" is needed or wanted.

**Their prediction, which makes this a test rather than a survey:** the **derive
and enum programs** — the 8 that were the *exceptions* before — are expected at
the **top** of the distribution now, because their impls are what they
reference. A different set at the top is itself a finding.

**Deliverable 1 — the floor pair, the one continuous number. LARGELY ALREADY
TAKEN, and this changes what 1.5.2f buys.** The canary *is* the 14-line floor
program, and the `0dfddac → aaffb87` pair is measured and on this board: `.ll`
**845 282 B → 50 560 B** (−94.0%), functions **608 → 14**, where **14 was
predicted and hit exactly**. So 1.5.2f yields a **third point in a series**, not
a first comparison. Their floor-only probe reads **50 561 B / 14 functions after
1.5.2d**; the one-byte gap is **already explained and is not two different
source files** — see the path-dependence rule below.

**Deliverable 2 — the spread, over a stated denominator.**

- [ ] Define the set in a **committed file before running anything**, by
      **discovery, not by listing** (`PLAYBOOK.md` §7): every program under
      `tests/` that compiles clean under **both** pinned binaries.
- [ ] **Print the count beside the verdict.** "All N" is two claims and the
      second is the one nobody checks.
- [ ] Report the **distribution**: min, median, max — plus **the names of the
      largest**, which is the half they can act on.
- [ ] Report it as **first-of-its-kind under a stated set**, not as a repeat.
- [ ] A constant delta anywhere → **stop, name the program, raise it as a
      compiler defect** (W-11: never worked around).

**THE UNIT IS THE OBJECT AND THE FUNCTION COUNT — NOT THE `.ll` BYTE. Proposed
here from this workbench's own measurement, ACCEPTED BY `nitpick-compiler_s0`
2026-09-06 03:0x, and no common-directory compile is needed.** Their acceptance
supplied the mechanism our side only had empirically — **it is `D-236`, by
design**: every site row carries the source path **relative to the manifest
root**, so a program's own directory name is in its `.ll` and **the byte is the
path**. Their reading of the three units, now settled: *"the object is what the
trim's effect should be read from, and the **function count is the sharpest
signal of all, since the trim removes whole defines**."* So the function count is
the primary instrument rather than a tie-breaker.

> **AND THIS RESOLVES A SEAM ON THIS BOARD THAT WOULD OTHERWISE READ AS A
> CONTRADICTION.** Line 137 says **D-236** *"renders every embedded source path
> relative to the manifest root, **so the build path cannot leak into the
> artefact**"* — cited as a reason CI is reproducible. Line 641 says an `.ll`'s
> byte count is **path-dependent**. **Both are true, and they are about
> different paths:** D-236 removes the **absolute** path above the manifest root
> (so moving or re-cloning the checkout changes nothing, which is what CI
> needs), and leaves the **manifest-relative** path in (so two programs at
> different relative paths carry different byte counts, which is what 0.0.5
> measured). **A reader taking line 137 to mean "paths do not affect the
> artefact" would use it to dismiss the path-dependence finding**, which is why
> the distinction is written here rather than left to be re-derived.
>
> **The consequence that matters for this measurement:** our `.ll` byte counts
> are **portable across machines and checkouts** and **not comparable between
> programs**. Those are different properties and only the first is what CI's
> repro stage tests.
>
> **`nitpick-compiler_s1` stated the mechanism exactly, 2026-09-06 03:5x, and it
> sharpens the rule rather than softening it:** *"every site row carries the
> source path relative to the manifest root **the driver finds by walking up
> from the main file**, so the absolute build directory never registers (the
> repro stage measures that), and a program's own rows change only when **its
> path WITHIN its manifest tree** changes. A spread over programs held at fixed
> relative paths has **stable** byte counts. The prelude's rows are the fixed
> string `prelude.npk`, which is why a floor program barely registers."* **So
> the per-program artefact is DETERMINISTIC, not noise** — a program at a fixed
> relative path gives the same byte count every run and on every machine. That
> is a better situation than "noisy" and **it does not make the counts
> comparable between programs**, which is the whole of the unit argument. It
> also confirms the 0.0.5 measurement was **the mechanism working, not a leak**.

**The measurement this rests on:**
`nitpick-compiler_s0` asked for the distribution of *IR bytes* and function
counts. But `nitpick-time` 0.0.5 measured that **an emitted `.ll`'s byte count
is PATH-DEPENDENT and the object's is not**: the same source compiled from two
directories whose names differ by one character gives `.ll` sizes **14 bytes
apart**, one byte per `npk.site.paths` entry, while the `.o` and the linked
binary are **byte-identical**. **A distribution taken across programs sitting at
different paths therefore carries a per-program artefact of its own directory
name**, which is precisely the confound a distribution is supposed to expose.
So: **function counts and object sizes are the primary series**, `.ll` bytes are
reported beside them and **labelled path-dependent**, and if `.ll` bytes are
wanted comparably, every program is compiled **from one common directory**.
This board's standing rule — **quote the OBJECT, not the `.ll`** — is not a
style preference; it is why the canary's *function* count is the half that
carried the 1.5.2d prediction.

**Gate:** re-pin first (and the re-pin waits for the live claim to close —
orchestrate §2 — then for §3's two-minute binary-age guard). **Every number
above that predates the re-pin is an `aaffb87` number and says so.**

**Why this is worth reading twice: it is the second time in two days that
raising cost nothing and bought something.** O-N16 was catalogued rather than
raised and was closed upstream the same day anyway; S-38 was raised under the
lifted constraint and became a decision item with a recommendation within
twenty minutes. Both point the same way, and the constraint is now lifted.

**Awaiting the author on the COMPILER side** (their `OPEN_DECISIONS.md` §7),
none of it blocking us, two being semantics this ecosystem already builds
against: **S-24** derived comparisons over a generic parameter; **S-25**
`List<T>` in the prelude as struct and functions, implemented in step 5b;
**S-26** a partial move leaves the vacant value; **S-27** `exit` after
`wild_release_all()`, `TYPE-062`.

**THE `devteam` IMPORT — FOUR MECHANISMS LANDED 2026-09-05, SEVEN MORE LISTED.**
The full list, with what each costs and why it matters here, is
[`meta/audits/devteam-import-2026-09-05.md`](meta/audits/devteam-import-2026-09-05.md).
Landed: the guard now names the interpreter-heredoc limit **in its refusal
message** rather than only in its docstring (guidance goes where the temptation
is — `devteam` measured this changing an agent's behaviour); **`git worktree
list` is no longer refused as a write**, with thirteen new controls covering
each read form and its write twin; `tools/run_controls.py` finds and runs every
control and treats *"no controls found"* as a finding; and every control now
reports its **case count and false-positive share** — `111 cases, 50 of them
false-positive controls (45%)`.

**Doing that found a live defect of the worst class, now fixed.** `check_refs`
read an identifier inside a fenced block, and inside its own quoted output, as a
citation — so it reported `cited-undefined` against a file that had pasted
evidence, **which this workbench requires a worker to do**. A check that fires
on mandated behaviour puts the correct response and the safe response in
opposite directions. `prose()` now strips fences before the citation scans
(deliberately **not** before the leak scan). **Stated gap, not closed:**
verbatim output quoted *inline* is still miscounted, and cannot be fixed by
stripping inline spans because `` `RX-126` `` is how a real citation is written
here. The rule that implies — verbatim output belongs in a fence — is item 5's
business, not a check's.

**STOPPED 2026-09-04 13:40 at the author's request, at a clean stop**, to conserve a weekly quota being spread across several sessions. Both streams closed their subcycles and both were independently VERIFIED PASS. **Resume points:** s1 `nitpick-regex` **0.0.4** (`src/core/`), s2 `nitpick-time` **0.0.1** (the skeleton) — both planned, unblocked, and NOT dispatched. Stream 3 has still never run. **UPDATED 2026-09-05 by the fifth orchestrator: the re-pin question that stood in front of both resume points is ANSWERED and the answer is to wait until ~15:30** (see the block at the top). Width is **1**, so one stream runs; the board recommends **s2 `nitpick-time` 0.0.1**, whose gate is satisfied — 0.0.0 is `DONE` and the probes it names (01, 04, 06) have recorded verdicts — **but it is deliberately NOT dispatched before the pin lands**, because step 4 of that subcycle *pins the compiler by commit in CI* (P-10). Dispatching now would write the stale `94874ce` into a new CI workflow and guarantee an immediate bump commit, and steps 2 and 5 accept against a compiler we are about to discard. That is the same argument the previous session used for not re-pinning at a stopping point — a measurement belongs to a pin — pointed the other way. The questions table has **four** entries; question 4 (width) is answered, three stand.

---

## Legend

| State | Means |
|---|---|
| `—` | not started, not claimed, nothing blocking it |
| `CLAIMED sN` | stream N owns this repository; the in-flight table says what it is doing |
| `BLOCKED on <repo> <cycle>` | cannot start until that cycle is DONE; the reason is always a named cycle, never "waiting" |
| `DONE` | every cycle closed and archived to `done/` |

---

## ⏸ CYCLE 0.0 IS PAUSED — the author's decision, 2026-09-06, and the reason is strategic rather than a problem with the work

**`nitpick-regex` stays `CLAIMED s1` so no other stream takes it, and NOTHING IS
IN FLIGHT — no agent is live and the row below is history, not a dispatch.**
Cycle 0.0 is **not closed and not abandoned**: three audits refused the close,
all four subcycle commits are **VERIFIED PASS individually and now PUSHED**
(`7eb8e53..ab93eae`), and `ROADMAP.md` in that repository already records the
refusal in its own words rather than reverting to silence.

**THE AUTHOR'S REASONING, RECORDED BECAUSE A SUCCESSOR WOULD OTHERWISE READ A
PAUSE AS A STALL AND RESUME IT.** In his words: *"nitpick-libs has already been a
tremendous success in helping find bugs in the compiler so far and we already
have a slight backlog of those to get done. building on top of it is still
shifting sand right now but hopefully not for much longer."*

**So the libraries' highest-value output today is NOT library code — it is
compiler defects**, and that is measured rather than asserted. In one session
this workbench raised **DEF-25** from a nine-line accessor, and the compiler side
found the class reached **`impl:string:Clone`** and **234 sites of its own copy
idiom** — *the compiler had been leaking in its own build.* Three audits of one
cycle produced seven `src/core/` defects and a chain in which **the fix for each
finding was where the next one lived**. That is a bug-finding instrument working
well, on a foundation that is still moving.

**WHY RESUMING IS CHEAP LATER AND EXPENSIVE NOW.** Every blocking finding here is
pin-dependent in some direction: `RX-120` expired under a re-pin mid-session,
`BL-4`'s root cause was fixed upstream within the hour, and `BL-5`'s central
claim is about a diagnostic (`TYPE-046`) whose behaviour is a compiler fact. **A
library built against a compiler in active implementation re-derives its own
premises every re-pin**, and this cycle spent most of its cost on exactly that.

**THE COMPILER'S ROADMAP, AS THE AUTHOR STATES IT** — the sequence a successor
needs to know before proposing a resume date:

```
1.5  in progress; the compiler is at 1.5.3 today
1.6  the last cycle on the roadmap so far
     -> together these are meant to carry the INITIAL IMPLEMENTATION to
        good shape
then the STDLIB that ships with the compiler -- filled in and improved
then loads of TESTING, FIXES and REFINEMENT across all of it
then as much FORMAL VERIFICATION as can be done
```

**The resume signal is therefore not a date, it is a state:** the compiler out of
active implementation and into fixing and refinement, at which point a re-pin
stops moving the ground under a library's own measurements. **Until then the
work that pays is the work that finds compiler defects.**

**WHAT A SUCCESSOR SHOULD READ FIRST WHEN 0.0 RESUMES.** The three audits, in
order, at `meta/audits/nitpick-regex-0.0-2026-09-06{,-second,-third}.md`. The
open blocking set is `BL-5` and `BL-6`, both specified with their remedies and
both measured. **`BL-6` is the one to fix first regardless of anything else** —
the `pending-until` marker can move an ordinary red out of a green run's
denominator with one comment line, so every subsequent green in that repository
is worth slightly less until it is controlled.

---

## In flight

| Stream | Repository | Subcycle | Agent label | Since | Model | Note |
|---|---|---|---|---|---|---|
| s2 | `nitpick-time` | **0.1.0 — the civil types — DONE, VERIFIED PASS, PUSHED, CI GREEN** at `2589069`, harness **GREEN 67 units / 0 failures / 5 pending**, grown 62 → 67; CI run **`34020573741`** green, read from GitHub. **Pushed mid-cycle on the author's instruction and the push was CHECKED FOR COHERENCE FIRST:** this repository's CI pins `aaffb87`, which is exactly the pin 0.1.0 was written and verified at, so CI judged the code against the compiler it was proved against. **Bumping that pin to `3d15ac9` first would have tested 0.1.0 on a compiler it had never been verified on** — see the CI PIN MAP. Next: **0.1.1 — Hinnant's algorithms** (`date_to_days`, `days_to_date`), **NOT DISPATCHED and `0.1.1.md` DOES NOT EXIST** — the convention writes only a cycle's *opening* file, so 0.1.1 needs either a planner dispatch or a decision to work it from the cycle README's checklist | *(no live agent)* | verified 2026-09-06 03:30 | `claude-opus-5` worker, small-model verifier | **DISPATCHED UNDER A HELD RE-PIN, DELIBERATELY, AND THE REASON IS ON THE RECORD.** D-264's four consequences are all about a **generic `T`** — a copied `T` place, a stored by-value `T:v`, a lending `pick` on a `T` payload, a derive over a `T` payload — and **`src/cal/` declares no generic at all**; `Weekday` and `Month` are payload-free, so `DERIVE-006` cannot bite either. **0.1.0 was WRITTEN at `aaffb87` and its nine binding cases are measured there**, so running it at this pin is running it where it was written rather than despite the hold, and its §1 item 4 **already predicts `check_exemptions_live` firing at the re-pin**. **EVERY NUMBER IT RECORDS IS AN `aaffb87` NUMBER AND MUST BE LABELLED AS ONE** so the re-pin re-checks rather than inherits it — the discipline that caught the "under 768 KiB" figure after three subcycles. Author confirmed the dispatch 2026-09-06 02:3x. | **THE FIRST CYCLE CLOSED ANYWHERE IN THIS ECOSYSTEM.** **All 30 audit findings triaged — 30 of 30 carry a line**, verified by counting rather than by report; nothing rejected on disagreement, one refusal (F8, a rename) stating its cost instead. **Both use-after-frees are fixed**, and the second one — `bytes_view`'s comment promising a view outlives a growth — now has a test **with its control**, because a test showing only the failing half proves the failure and not the rule. **CI RAN FOR THE FIRST TIME IN THIS REPOSITORY'S HISTORY AND ITS FIRST RUN WENT RED — WHICH IS THE POINT.** Run `34014136095` failed on `f950ae4`, then green on `8081e60` and `93293f2`; read from GitHub, not from the report. **The close is three commits because a CI result cannot live inside the commit that caused it.** **TREAT THE FIRST CI RUN AS AN INSTRUMENT, NOT A FORMALITY** — it found two defects in its first eight minutes. **TWO OF THOSE AFFECT EVERY SIBLING AND ARE IN THE SHARED CI SHAPE — see the SHARED FINDINGS block.** **The harness grew 40 → 62 units**, and the 22 are exactly the defect corpus the audit found asserting nothing (24 = 3 exempt + 21 now asserted, 13 run + 8 refusal) — so the growth is coverage rather than re-counting. **~~O-N4~~ struck on this repository's own re-measurement** — 30 000 rows at **1.17 s / 26 888 KiB** against 281 s / 30.9 GiB, with a 2 266 485 B `.ll` carrying all 30 000 rows, **so the speed is not bought by emitting less**; its heading had read BLOCKING for two subcycles after its gate was passed |
| s1 | `nitpick-regex` | **0.0.4 — `src/core/` — DONE, VERIFIED PASS 2026-09-06 05:5x, harness GREEN 98/98 in 31.7 s, grown 63 → 98.** Seven commits, `52dfa2d`…`7eb8e53`, tree clean, `check_record` and `check_refs` both clean, `compiler-defect: none`, no retries. **NOT PUSHED — 7 ahead of `origin`.** **THE PASS RESTS ON A PLANTED FAULT, NOT ON THE GREEN.** The verifier copied the tree, deleted **one** line — `vec.npk:186`, the `i >= v.count` upper-bound check inside `vec_get<T>` — and the suite went **97/98 with exactly `vec_oob_get_at_count.npk` failing** (exit 50, expected 94), the single unit built to catch that check, failing the way its own comment predicts. Copy destroyed, real tree confirmed clean. **This repository has shipped two use-after-frees under a green suite, one through an independent VERIFIED PASS, so a suite is not evidence until it has been shown to go red.** **The three-step entry cost was paid in the first three commits** and produced **four of the eight playbook findings** — re-record the floor baseline (`SYMBOLS.txt` 29 → 2 and `EDGES.txt` 237 → 2, both landing exactly as predicted, `npk_dalloc` and `npk_ofd_close` surviving), reshape `probe13b`, bump CI to `3d15ac9` (`ci.yml:69` now reads `3d15ac92d51…`, verified). **PUSHED at 05:5x** — `91657eb..7eb8e53`, and CI run **`34025780292`** started at the new pin. **Expect it to be SLOW and do not read slowness as trouble:** the workflow caches the built compiler by commit, so bumping `NITPICK_COMMIT` to `3d15ac9` is a deliberate cache miss and this run builds the compiler from source. **Now: 0.0.5 — the cycle close — DISPATCHED 05:51 as `s1-nregex-0.0.5-0551`.** *(Correcting this row's own earlier claim that "the auditor runs first": it does not. §7's `READY-TO-CLOSE` path is a **worker report status** — the worker works the close, reports `READY-TO-CLOSE`, the verifier passes it, THEN the auditor runs, and only then is the worker re-dispatched with `AUDIT:` naming the filed report. `meta/audits/` does not yet exist in this repository, so that will be its first.)* **0.0.5 REPORTED `READY-TO-CLOSE` AND VERIFIED PASS on eight checks — and THE AUDIT SAYS DO NOT ACCEPT.** Filed as `meta/audits/nitpick-regex-0.0-2026-09-06.md`, the first audit in this ecosystem. **Two BLOCKING findings, both in `src/core/`, the cycle's headline deliverable, both measured with running programs rather than argued.** **BL-1 — `bytes_take_string` RETURNS A BORROWED VIEW** (`npk_string_from_bytes` sets cap 0; the compiler's own runtime comment says *"cap 0 is the not-mine bit"*) **while three documents call it owning and "the only shape that may leave the frame".** Both halves are false at the pin: returning it from the frame that *owns* the `Bytes` is REFUSED `NITPICK-BORROW-001`, and any growth frees the body underneath a taken string — probe A returns a wrong answer at exit 20, probe B returns **exit 170 = `0xAA`, the D-183 free poison**. **THE SHIPPED SUITE ALREADY CONSTRUCTS THE STALE ALIAS AND DECLINES TO READ IT:** `tests/unit/bytes_unit.npk:55` takes `out`, line 63 reallocates, and `out` is never read again — **one added line turns the green run into exit 46.** **This is the THIRD use-after-free this repository has shipped under a green suite and the SECOND to survive an independent VERIFIED PASS.** **BL-2 — `vec_reserve` DOES NOT TERMINATE on a `Vec` with `cap == 0`**, which is exactly `vec_free`'s deliberate poison postcondition; the sibling `bytes_reserve` carries the `if (nc < 1i64) { nc = 1i64; }` guard written in the same subcycle and `vec_reserve` does not. Measured: `timeout 6 ./vfree` → **exit 124**. `vec_push` and `vec_insert` go one step further and `ralloc(<dangling>, 0)` then write. **That is a denial of service in the container every engine is built on, reached with no backtracking at all — against `CLAUDE.md`'s first non-negotiable rule.** **NINE non-blocking findings carry into 0.1.** **Re-dispatched for triage as `s1-nregex-0.0.5-audit-0637` with `AUDIT:` naming the report (W-22).** **Predecessor state: 0.0.3 DONE — VERIFIED PASS at `91657eb`, harness 63/63 in 37.5 s, but that is a `94874ce` number and the CI at `950bb1d` is RED on it** — diagnosed, not inherited blind | `s1-nregex-0.0.4-0437` | 2026-09-06 04:37 | `claude-opus-5` worker, small-model verifier | **RX-126 is this subcycle's most valuable output and it corrected THIS BOARD** — see its block above. O-N10 also discharged here (RX-125), on thirteen measured properties, **two of which `nitpick-time` cannot test** (its enum has one payload field per variant), so O-N10's verification is still owed there. RX-123 (both leak checkboxes), RX-124 (`parse` no longer depends on a compiler-repository tool) landed. O-N16 raised, numbered from `meta/OPEN_QUESTIONS.md:355`. **ACCEPTED WITH A KNOWN OVERSTATEMENT, carried to 0.0.4 rather than re-dispatched at a stopping session:** the verifier found that the mutation-test **transcripts are NOT committed** — `meta/roadmap/0.0/0.0.3.md` §4 holds a per-case attribution *summary table*, which is what the acceptance criterion actually required and is why this is a PASS — but **`harness/README.md` claims "§4 has the transcripts", and it does not**. `PLAYBOOK.md` §6 says a summary is not evidence, and `nitpick-time` 0.0.0 was once FAILED by its own verifier for exactly this, so the precedent cuts against letting the sentence stand. **0.0.4 must either commit the raw mutation runs with their exit codes, or correct that sentence to claim only what is there.** Do not let it pass a third time

## THE CI PIN MAP — read this before dispatching anything at `3d15ac9`

**Found 2026-09-06 04:2x, immediately after the re-pin, by asking which compiler
each repository's CI actually pins. Three different answers.**

```
workbench          3d15ac9   1.5.2f, re-pinned 04:0x
nitpick-time  CI   aaffb87   1.5.2d -- MATCHES what 0.1.0 was verified at
nitpick-regex CI   950bb1d   2026-09-03 -- 57 compiler commits behind
nitpick-parse      (no .github/workflows at all)
nitpick-sockets    (no .github/workflows at all)
nitpick-tui        (no .github/workflows at all)
nitpick-posix      (no .github/workflows at all)
```

**Denominator stated: 6 work repositories, 2 with a workflow, 1 of those green.**

**(1) The `nitpick-time` divergence is CORRECT TODAY AND BECOMES A TRAP AT
0.1.1.** 0.1.0 was written and verified at `aaffb87` and CI judges it at
`aaffb87`, which is why the push was coherent and why it was checked *before*
pushing. But **0.1.1 worked at `3d15ac9` would be verified locally against one
compiler and judged by CI against another, and nothing would say so** — the run
would simply be green or red about the wrong thing. That workflow's own header
says bumping the pin *"is a deliberate commit, and this is that commit"*. **So
bump `NITPICK_COMMIT` to `3d15ac9` as its own commit BEFORE 0.1.1's work; that
commit is what proves the new compiler builds the existing tree.**

**THE TWO BUMPS ARE NOT THE SAME SIZE OF JOB, AND ONE OF THEM HAS A PREREQUISITE.
Confirmed from both sides 2026-09-06 04:1x.** `nitpick-time`'s bump is a one-line
commit. **`nitpick-regex`'s is not**: at `3d15ac9` its harness dies at the
baseline before the suite runs, so **the floor baseline must be re-recorded in
the same pass** or the bump lands a red that says nothing. Treating them as one
kind of task is how the second one gets committed unrun.

**AND THE RULE THAT CAME OUT OF DOING IT: measure a re-pin's blast radius in a
COPY, never in the claimed tree.** Establishing what is on the far side of the
baseline failure meant *running* `--record-baseline`, which rewrites committed
files; done in a scratch copy, the claimed repository was never touched and the
result is just as good. **This is now the rule for any re-pin probe that has to
write to find out**, not a courtesy of the session that happened to do it first.

**`nitpick-time` HAS ITS OWN RE-PIN EXPOSURE, OF A DIFFERENT SHAPE, AND IT IS
PREDICTED RATHER THAN LATENT.** Its check list carries `check_exemptions_live`,
and **0.1.0's plan file §1 item 4 already predicts that check firing at the
re-pin** — the close worker foresaw the interaction and wrote the answer down
before anyone re-pinned. So expect a fire there and **read it as the prediction
landing, not as a new defect.** It is the same class as `nitpick-regex`'s — *a
committed expectation about compiler output meeting a compiler that changed* —
and the difference that matters is that this one was foreseen. **The class is now
the thing to look for at every future re-pin**, in every repository, rather than
the two instances of it.

**(2) `nitpick-regex`'s TWO-DAY RED IS DIAGNOSED, REPRODUCED AND BOUNDED —
2026-09-06 04:1x by the eighth orchestrator.** Run `33901134351`, 2026-09-04, on
**`91657eb`** — *the very commit this board records as "0.0.3 DONE — VERIFIED
PASS … harness 63/63 in 37.5 s"*. Failing step: **`Run the harness`**. **Local
green, CI red, same commit, unnoticed for two days** — TM-146's lesson reaching a
sibling where nobody was reading the instrument.

**THE CI LOG IS UNRECOVERABLE AND THAT IS A FACT, NOT A RETRY.** The previous
orchestrator reported `gh run view --log` "empty"; the API says why —
`repos/…/actions/jobs/101115219244/logs` returns **HTTP 404**. GitHub has
expired it. **No re-read will ever produce that log**, so "re-run the workflow to
regenerate one" buys a log for a *different* run, not the one that failed. The
diagnosis therefore had to come from **the pins kept on this machine**, which is
precisely what `.internal/toolchain/` is for and why it is never cleaned.

**The measurement: one tree at `91657eb`, three kept compilers, this machine.**

```
pin        what it is                          result
950bb1d    what nitpick-regex CI PINS          60/63 in 36.0 s  -- REPRODUCES THE RED
94874ce    what 0.0.3 was VERIFIED at          63/63 in 37.7 s  -- green, the board's number
3d15ac9    today's pin, the proposed bump      DIES AT THE BASELINE, no suite runs

the three failures at 950bb1d, which ARE the CI red:
  probe/tests/probe/probe02b_derive_eq.npk   expected IR, got REFUSAL NITPICK-TYPE-034
  probe/tests/probe/probe02c_derive_ord.npk  exited 20, expected 0 (REAL backend)
  parse/tests/probe/probe02b_derive_eq.npk   expected IR, got REFUSAL NITPICK-TYPE-034
  NITPICK-TYPE-034 <derived-1>:2:82: `HirKind` has no built-in `==`:
                                     derive or implement `Eq` and compare with `a.eq(b)`
```

**THE CAUSE.** 0.0.3 added probes that exercise **derived `Eq` and `Ord`**.
`950bb1d` predates that support and refuses them. The tree change is the
**trigger**; the 57-commit-stale pin is the **cause**; and *neither alone
explains it*, which is why the bracket misled.

**A CORRECT BRACKET SUPPORTED A WRONG INFERENCE, AND THIS IS THE DURABLE PART.**
The previous orchestrator established — correctly, and the readings are not in
dispute — that `NITPICK_COMMIT` is byte-identical at the last green commit and at
the red one, and that `.github/` is untouched between them. From that it
concluded *"the red is 0.0.3's own content, **not** the stale pin"*, and
suspected `harness/treecheck.py` failing on a runner. **The conclusion does not
follow.** An unchanged pin is not an exonerated pin: what changed is a tree that
now *requires* a compiler newer than the pin, so the constant is the cause and
the variable is only the trigger. **`treecheck.py` is refuted outright** — the
red reproduces on this machine with no runner involved, and the failures are
three named derive probes. **Holding a variable fixed proves it did not change;
it does not prove it did not matter.**

**AND THE RECOMMENDED FIX IS REFUTED — BY THE OPPOSITE RESULT FROM THE ONE
PREDICTED.** This board recommended bumping `NITPICK_COMMIT` to `3d15ac9` and
re-running as a *diagnostic*. The outgoing session then withdrew that on the
bracket, predicting it "will not go green". **Bumping does not go green, and not
for that reason.** At `3d15ac9` the harness never reaches the suite: it dies in
the build step on symbols **"committed and no longer emitted — THE PRELUDE
MOVED"** (`__divti3`, `npk_alloc`, `npk_exec`, `npk_sys6`, …). That is 1.5.2d's
prelude trim arriving in a repository that records a symbol floor.

**THE SIZE OF THAT MOVE, COUNTED RATHER THAN EYEBALLED — AND THE FIRST NUMBER
THIS SESSION PUT ON THIS BOARD WAS WRONG.** It read "23 floor symbols", taken
from a `head -45` of the run log; the log carries 3 668 such lines because the
self-check re-runs the build, and 23 was simply where the truncation fell.
**Measured properly, by diffing the committed baseline against the re-recorded
one:**

```
SYMBOLS.txt    29 -> 2     27 removed, 0 added   (npk_dalloc, npk_ofd_close remain)
EDGES.txt     237 -> 2    235 removed, 0 added
unique "no longer emitted" symbols in the log:  27   (not 23)
```

**`EDGES.txt` moves too, and by two orders more than the symbols — this board's
first account of the failure did not mention it at all.** So the re-record is a
**237-line review**, not a 23-line one, and anyone sizing that commit off the
earlier sentence would have sized it wrong. **A count read off a truncated log is
not a measurement**, and the fix is the rule this workbench already has: print
the count beside the verdict, from a command that counts.

**CORROBORATED FROM THE COMPILER SIDE, FROM THE OPPOSITE DIRECTION, 04:2x.**
`nitpick-compiler_s1` compiled a floor-only probe at `3d15ac9`, assembled it, and
read its object: **exactly two undefined symbols, `npk_dalloc` and
`npk_ofd_close`** — none of `__divti3`, `npk_alloc`, `npk_exec`, `npk_sys6`. That
is the same pair this workbench's re-record produced, reached by a different
route on a different input. **The mechanism is D-262** (1.5.2d step 2,
2026-09-05, present in `aaffb87` and later; the `94874ce` baseline predates it):
a prelude item is emitted **only if referenced**, and a reference to a runtime
symbol — or an `i128` division for `llc` to mint `__divti3` from — is what used to
drag the carrying prelude body in. **They confirm re-recording as the library's
own commit is the right move.**

**What is on the other side of it, measured in a COPY so the claimed tree was
never touched:** re-record the baseline at `3d15ac9` and the suite runs
**61/63 in 21.5 s**. The derive probes pass. **Two NEW failures appear that no
document predicts:**

```
probe-refused/tests/probe/refused/probe13b_limit_refused.npk
parse/tests/probe/refused/probe13b_limit_refused.npk
    expected NITPICK-RUNG-001, got NITPICK-REACH-002
    "reported NITPICK-REACH-002, which no expectation names -- an unexpected
     diagnostic fails a test as surely as a missing one (BUILD.md B-7, D-237)"
```

**EXTENT, ESTABLISHED IMMEDIATELY AND BOUNDED RATHER THAN ASSUMED.** The prelude
trim breaks any repository that records a floor-symbol baseline. Asked of all six
work repositories with `git ls-files`, **exactly one has one**: `nitpick-regex`
(`harness/baseline/SYMBOLS.txt`, `EDGES.txt`, `baseline.npk`). `nitpick-parse`,
`nitpick-sockets`, `nitpick-time`, `nitpick-tui` and `nitpick-posix` carry none,
**so this does not spread** — the one place it bites is the one place it was
found, and that is now a measurement rather than a hope.

**WHAT 0.0.4 COSTS TO ENTER, in this order — ALL THREE NOW SPECIFIED, NONE OF
THEM OPEN.** (a) **Re-record the floor baseline as its own commit** naming the
compiler commit that moved; the harness prints that instruction itself — *"this
is a deliberate act, commit it on its own, so a reviewer sees the diff"* — and
**size it as a 237-line review, not a 27-line one**, because `EDGES.txt` moves
further than `SYMBOLS.txt`. The expected landing state is **2 symbols and 2
edges**, corroborated from both sides. (b) **Reshape `probe13b`** per the answer
to question 8, below. (c) **Bump CI's `NITPICK_COMMIT` to `3d15ac9`** in the same
pass as (a), since without the re-record the bump lands a red that says nothing.
**`nitpick-regex` is CLAIMED and is stream 1's next item — and as of 04:2x it is
DISPATCHABLE**, which it was not two hours ago.

**THE THREE FACTS `nitpick-compiler_s1` MEASURED SO 0.0.4 CAN ENCODE RATHER THAN
GUESS.** Taken on their `build/npkc` at `3d15ac9` with the pinned `llc`/`ld.lld`
flags and `npkrt.o` `c9ddbcff…` — the same runtime object this workbench has
`cmp`-verified — so the numbers are commensurable with ours rather than merely
adjacent:

```
1.  probe13b + a (LimitViolated) arm in failsafe, bounded(3i32)
        compiles, exits 0
2.  the same with bounded(0i32)
        exits THROUGH the LimitViolated arm (31 in their copy)
        at -O0 AND under opt -O2 + llc -O2   <- both optimisation levels
3.  func:bounded = int32(limit<r_pos> int32:x) never fails { pass x; }
        compiles and runs, exit 0
```

**Fact 3 is the one that reaches beyond the probe, and it is a DESIGN INPUT for
`src/core/` — the very package 0.0.4 builds.** That probe carries a comment
asserting that a `limit` and `never fails` are **mutually exclusive**
(`TYPE-037`). **That has been stale since 1.5.1** (D-241, 2026-09-03): a
never-fails function may carry `limit`, `requires` and `ensures`, because the
trap route is a channel a never-fails body already admits. **So a comment written
as a constraint on the design is now a false constraint, in the cycle that acts
on it.** 0.0.4 must not inherit it.

**Their recommended reshape, and this workbench's view of it.** Retire `probe13b`
as a *refusal* probe; keep it as **two positive probes** — accepted-and-checked,
and the trap reaching failsafe — and expect `NITPICK-REACH-002` only in a probe
whose failsafe **deliberately** omits the arm. **The recommendation is sound and
the library still owns the decision** (W-7): it is stream 1's to take at its
claim, with the reasoning recorded, not something this board imposes from the
compiler's side of the fence.

**THE PROCEDURAL FINDING, WHICH IS WORTH MORE THAN THE ANSWER.** The cheap move
was available and wrong: edit one expectation from `RUNG-001` to `REACH-002` and
the suite goes green in a minute. That would have encoded, invisibly, a guess
about which of *deliberate* and *regression* was true — and it would have
silently preserved the stale `never fails` comment as a live design constraint
for `src/core/`. **Asking instead cost one message and forty minutes, and
returned three measured facts, a retired language rule, and a design input the
red was hiding.** A red suite is sometimes the only thing standing between a
library and an obsolete premise.

**(3) Four of six repositories have no CI.** The ecosystem's strongest recent
lesson protects one repository and is broken in the other.

---

## Questions for the author

| # | Stream | Raised | Question | Recommendation |
|---|---|---|---|---|
| ~~5~~ | s2 | 2026-09-06 | ~~**`nitpick-regex`'s CI is red at `91657eb`, cause unknown**~~ — **ANSWERED BY MEASUREMENT 04:1x, not by the author; no ruling needed and none should be waited for** | **CLOSED.** Diagnosed, reproduced and bounded against the three kept pins — see the CI PIN MAP item (2). The stale pin is the cause, 0.0.3's derive probes are the trigger, the CI log is gone at the source (HTTP 404, expired), and the recommendation this row carried — bump and re-run *as a diagnostic* — **was refuted by the opposite result from the one it predicted**. It is superseded by the three-step entry cost recorded there. **Nothing here is the author's to decide** |
| ~~8~~ | s3 | 2026-09-06 | ~~**Is `NITPICK-RUNG-001` → `NITPICK-REACH-002` deliberate or a regression?**~~ — **ANSWERED BY `nitpick-compiler_s1` WITHIN THE HOUR, 04:2x. DELIBERATE, and the probe's premise is now obsolete in two separate ways** | **CLOSED, and it UNBLOCKS 0.0.4 rather than merely explaining it.** `limit<Rules>` went **live** in 1.5.2 (`5d45bb1`…`0fa414b`, 2026-09-04 — squarely between `94874ce` and `3d15ac9`; D-251…D-255). The `NITPICK-RUNG-001` refusal for it **retired**, and a limited parameter is now **checked in every build**: a generated predicate runs at the callee's entry and a violation traps `LimitViolated` (−4111), which REACH arms for any program carrying a limited binding. So the probe compiles *past* the construct and REACH then refuses at its failsafe — `NITPICK-REACH-002 …:43:5: failsafe does not name LimitViolated, which can reach it (D-179): add the arm — (*) counts for nothing here`. **The probe asked "refused, or lowered to nothing?" and the answer is now a third thing it did not offer: enforced.** See the block below for the three measured facts and the recommended reshape — **asking rather than editing the expectation green is what turned a red into a design input** |
| 6 | s2 | 2026-09-06 | **Should the CI pin bump to `3d15ac9` happen before 0.1.1?** The workflow's header says bumping is a deliberate commit and that commit runs the full suite | **Yes, as its own commit, before any 0.1.1 work.** Otherwise 0.1.1 is verified locally at `3d15ac9` and judged by CI at `aaffb87`, and neither result means what it appears to |
| 7 | s2 | 2026-09-06 | **Four of six work repositories have no CI at all** — `nitpick-parse`, `nitpick-sockets`, `nitpick-tui`, `nitpick-posix` | **Not urgent, and not free.** `nitpick-time`'s CI found two defects in its first eight minutes that nothing local could reach, so the value is measured rather than assumed; but each workflow is real work and the shared CI shape already has two known findings against it (prune nested repositories by shape; `set +e` before a capture-then-print step). **Fix the shape once, then propagate** |
| ~~1~~ | s2 | 2026-09-04 | ~~**Is a committed `REPORT` block immutable?**~~ — **ANSWERED BY THE AUTHOR 2026-09-06: yes, ratified as recommended** | **CLOSED — landed as `W-28` in `WORKSTREAMS.md`.** A REPORT block is evidence, not documentation; correcting it in place destroys the record of what was believed at the time, so a wrong statement inside one is corrected in a later `RECORD.md` entry or in the document that supersedes it. **W-28 also settles the half that actually bit twice — the bookkeeping.** A sweep that finds six sites and edits five reads as *incomplete*; the rule requires the denominator and the exemption stated together — *"six sites, five edited, one inside a committed REPORT block and corrected at `RECORD.md` <date> under W-28"* — because a count that does not name its exemptions is the same defect as a check whose name is wider than its mechanism. **It reached this table twice and both dispatches left it open; it will not reach a third** |
| 3 | — | 2026-09-05 | **Should `filesystem.denyWrite` be configured?** The write guard cannot judge an interpreter heredoc (`python3 - <<PY` … `open(path,'w')` …) — measured, four controls, the other three forms refuse correctly. The guard's own docstring names the sandbox's `filesystem.denyWrite` as the airtight mechanism for exactly this, and **it is configured nowhere**. Meanwhile this harness ships a standing instruction preferring heredocs and `sed` over `Write`/`Edit`, so a session writes through the unjudged form *by default*. The real exposure is a library worker reaching `../nitpick` and invalidating a multi-hour verification run | **The author's call, and deliberately not acted on here** — this is a permissions/settings change and no session should make one on its own analysis. Options: configure `denyWrite` for `../nitpick`; or teach the guard to refuse `python3`/`perl`/`node` invocations that carry a heredoc at all when a compiler path appears anywhere in the payload (cruder, more false positives, and a guard with false positives gets disabled — the guard's own docstring warns of this); or accept it and say so in `CLAUDE.md`, which today claims enforcement "where they can be" without saying where those are . **THE SECOND, OPPOSITE DEFECT IS ALREADY FIXED — VERIFIED 2026-09-06 04:3x, AND THIS ROW HAD GONE STALE.** It read that the guard *"refuses `git worktree list`, which is a READ"*, and recommended fixing both halves together. **That half landed in `80263a2`**: the guard now carries a read-forms table (`"worktree": {"list"}`) and a `git_is_read()` test, and its suite is **86 cases, all correct, 41 block / 45 allow, exit 0** — covering `git worktree list` as an allow and `worktree add`/`remove` as blocks. **Checked by running it, not by reading the code.** So the two halves did *not* need to be fixed together and only one remains. **WHAT IS STILL OPEN IS NARROWER THAN THIS ROW CLAIMED AND SHOULD BE JUDGED ON ITS OWN:** a write performed *inside* an interpreter payload (`python3 - <<PY` … `open(path,'w')` … `PY`), which the guard cannot see into. The suite already blocks the visible form — a heredoc followed by `rm -rf ../compiler/build` — so the exposure is specifically the opaque payload, and `filesystem.denyWrite` remains the only airtight mechanism for it. **LIVE EVIDENCE, AND THE FIRST ACCOUNT OF IT ON THIS BOARD WAS ITSELF WRONG.** This row first claimed the session had written `RECORD.md` "through exactly that form twice". **It had not.** Those were `cat >> FILE <<'EOF'` — plain shell redirects, which the guard reads and judges correctly; naming them as the unjudgeable form overstated the exposure and would have sent the author a false example. **The genuine instance came later and is worse:** at 05:5x this session rewrote **`BOARD.md` itself** — this file, the one carrying the writer lock — via `python3 - <<'PY'` … `open(path,'w')`, the precise construct the guard cannot classify, in the same session that documented the hazard. **Nothing refused it and nothing recorded it; it is visible only because the session chose to say so.** That is the argument for `filesystem.denyWrite` in one line: the unwatched path is not exotic, it is what a capable session reaches for when an edit gets fiddly |
| 2 | s1 | 2026-09-04 | **O-N10's verification is complete for `nitpick-regex` and cannot be completed for `nitpick-time`.** Two of the thirteen properties measured need an enum with more than one payload field per variant, which `nitpick-time`'s does not have | **No action needed now**, recorded so a later session does not read `nitpick-time`'s partial verification as an omission. The gap is a property of that library's types, not of the work |
| 4 | — | 2026-09-05 | **What width should the next session run?** The board carries **width 2**, confirmed by you on 2026-09-04, and both streams have a planned, undispatched subcycle ready (`nitpick-regex` 0.0.4, `nitpick-time` 0.0.1). Since that confirmation the binding constraint changed: the weekly quota is low and an experiment overspent it. Stream 3 has still never run | **Width 1 for the next session, then back to 2 when quota recovers** — this is `parallel-planning-serial-implementation`'s dial turned down, not a change of plan. The arithmetic is the argument: width 2 is two workers plus two verifiers, so **four dispatches before anything is verified**, and the re-pin has to be settled with the compiler session before either stream can be trusted anyway. Width 1 also puts the whole re-pin on one stream rather than duplicating it. **Model split, unchanged and working:** workers on `claude-opus-5` (stream 1's worker produced RX-126 by reading compiler source and drawing a distinction nobody asked for), verifiers on the small model per orchestrate §12 — both of 2026-09-04's verifiers returned PASS with real substance and one caught an overstatement the orchestrator would have let through |

**Q-9 — answered 2026-09-03 by the author: state what it blocks.** Landed as
**W-27** in `WORKSTREAMS.md`. The compiler side's rule is confirmed — *a defect
a real program finds is fixed before planned work* — so this workbench now says
plainly what a defect blocks, what it merely inconveniences and what it does not
touch, and drops "no schedule pressure implied", which reads as modesty and is
really a withheld fact. Sequencing stays the author's. O-N9 is the evidence the
hedge costs something: recommended here as conformance rather than a block,
overridden by the author, and the override cost nothing because the fix batched
with three others.

**Q-10 — answered 2026-09-03 by the author: both, and sweep for the gate.**
0.0.3 gains the cost-and-heap stage and 0.0.4's gate becomes a `peak_live`
assertion, both once the re-pin makes `NPK_HEAP_STATS` real. The read-only sweep
ran immediately, and **the unfalsifiable gate is in all five repositories** —
the site list is in `RECORD.md` and the per-repository notes are in the stream
tables below. Each fix waits for its own stream's claim (W-7); `nitpick-time`'s
two lagging sites go to the worker now, because that repository is claimed.

**RX-126 — D-247 DOES NOT MAKE A LIBRARY'S CONTAINER OWN, AND THIS BOARD SAID
IT DID. Found by stream 1, 2026-09-04; confirmed by the orchestrator against the
pin's own source before the board moved.** `decl_is_list`
(`../nitpick/src/frontend/type_layout.npk`, the `list_scope` / name / field
walk) recognises a `List` only when **all** of these hold: the declaration is
homed in the compiler's own `list` scope; it is a struct named **exactly
`List`**; and it has **exactly three fields, in order, named `items` (of pointer
type), `count`, `cap`**. D-247's owning behaviour keys on that predicate.

**No library here has such a type.** Every container in this ecosystem is
hand-written, differently named and differently scoped, so **D-247 changes
nothing for any of them.**

**What this board asserted and what is actually true:**

| The board said | The pin says |
|---|---|
| "`Vec<T>` does not own **until** D-247" | `Vec<T>` does not own, **full stop**. D-247 is not a date after which it does |
| "S-26 changes the drop flag and **D-247 makes the container own**, both in the same re-pin" | S-26's half stands; D-247's half never applied to us |
| the 125 MiB managed-body leak is a **before-number** that the re-pin moves | **it is not closed, and it is not going to be.** Stream 2 measured `probe06b` at **125 184 KiB, three times, at this pin** — independently corroborating stream 1's reading from the other direction |

**Impact, stated plainly.** The managed-body gap is permanent for
hand-written containers until a library closes it itself. **`RX-110` and
`RX-123` therefore stand at FULL strength** — the `exit 0` leak gate covers the
`wild` block alone, and the acceptance checkbox correction is not a temporary
measure pending a compiler fix. **0.0.4's leak acceptance needs a MEMORY CAP for
the managed half in every repository**, not just in `nitpick-regex` where it has
now been added. `nitpick-time`, `nitpick-parse` and `nitpick-tui` all carry
hand-written containers of the same shape and **all three inherit this
correction at their next claim.**

**And the three probes owed at the re-pin re-ran CLEAN — which is evidence the
shape is OUTSIDE DEF-8's scope, not evidence the fix is right for it.** Those
are different conclusions and only the first is supported. This distinction is
the finding; the clean result on its own would have read as the second.

**How it got here, which is the durable part.** The premise came off this board,
went into *both* of today's dispatches in the orchestrator's own words, and was
caught only because a worker checked a premise it had been handed instead of
building on it. **A dispatch's stated premises are claims, and a worker is the
last line that can falsify them.**

**Q-10 RESIDUE — THE SWEEP CORRECTED THE PROSE AND LEFT THE ACCEPTANCE
CHECKLISTS.** *(Deliberately NOT given an `RX-` number here: `RX-121` and
`RX-122` are already allocated in `nitpick-regex/meta/DECISIONS.md` and this
board nearly took one of them. `RX-` is one repository's namespace and this
finding spans five, so each repository allocates its own number when its stream
fixes it — `nitpick-regex`'s next free is **RX-123**. `check_refs.py` returned
clean on the collision, because it catches an undefined reference and never a
re-used one.)* Found 2026-09-04 by `nitpick-libs-44`; seven live sites in five
repositories.** Every repository's narrative text now carries the correct
formulation — *D-151 counts `wild` blocks, D-188 counts live drivers, and
neither sees a managed body*. But the **checkbox a worker actually ticks** still
states the unfalsifiable gate, in all five:

| # | Site | Note |
|---|---|---|
| ~~1~~ | ~~`nitpick-regex/…/0.0.4.md:113`~~ | **DISCHARGED at 0.0.4, and the citation was WRONG.** Verifier read the line: it is the harness module list, not the gate |
| ~~2~~ | ~~`nitpick-regex/…/README.md:170`~~ | **DISCHARGED.** That line is about compiler frontend files. The `vec_free` note this row carried does not live there |
| ~~3~~ | ~~`nitpick-time/…/0.0/0.0.4.md:122`~~ | **PATH BROKEN BY ARCHIVAL, not a live site.** `nitpick-time` closed cycle 0.0 and the file is now `meta/roadmap/done/0.0/0.0.4.md`. The phrasing appears **nowhere** in that repository, archive included |
| 4 | `nitpick-tui/meta/roadmap/0.0/0.0.4.md:103` | **LIVE — confirmed by content 2026-09-06.** `- [ ] the leak tests exit 0, so a missing free is a trap and not a pass`. Stream 1's claim (W-7) |
| 5 | `nitpick-parse/meta/roadmap/0.0/0.0.4.md:110` | **LIVE — confirmed by content.** Same wording. Stream 2's claim (W-7) |
| 6 | `nitpick-parse/meta/roadmap/0.0/README.md:104` | **LIVE — confirmed by content**, and still the worst instance: `- [ ] every suite program exits 0, so a leak on any path is a trap (D-151)` cites D-151 in SUPPORT of the broad claim |
| 7 | `nitpick-sockets/meta/roadmap/0.0/0.0.4.md:91` | **LIVE — confirmed by content.** Same wording. Stream 3's claim (W-7) |

**Not findings, checked:** `nitpick-regex/meta/DECISIONS.md:539` quotes the false
form and immediately corrects it; `nitpick-time/…/0.0/README.md:83` is about
probe comments; `nitpick-tui/…/0.13/README.md:48` is a different sense of "leak".

**Why the sweep missed them, which is the durable part.** `nitpick-regex`'s
`meta/DECISIONS.md:550` records that its site list was *"produced by `git grep -n
'D-151'` and not from recall"* — the right instinct, and it still under-counted,
because **five of these seven checklist lines do not cite D-151 at all**. That
repository's own correction note says "four sites stated, and two more implied";
the tree holds two more it never saw. A generating command is only as wide as
its pattern, and the prose was corrected *because* the prose is where the
citations live.

**This is the fifth instance of the shape** `PLAYBOOK.md` §6 names — a check
whose NAME describes the property while its MECHANISM covers something
narrower — and the first found in **acceptance criteria** rather than in prose,
which is the worse place for it: prose is read, a checkbox is ticked.
**And the finder's own first sweep was short by one** (site 6), by filtering out
every line that mentioned D-151 on the assumption that citing it meant being
qualified. Three phrasings were needed. **Fix each at its own stream's claim
(W-7); do not fix another stream's repository.**

**Q-8 — answered 2026-09-03 by the author: O-N9 is BLOCKING**, like O-N4 —
**against the recommendation on this board**, which read it as conformance
rather than a block. Recorded as an override because that is what this table
is for. The reason it is defensible: a rule enforced only by a harness check
the library writes for itself is a thin guarantee for a use-after-free, and it
protects no consumer. So `src/fmt/` work waits for the compiler, probes 09 and
10 are held, and the `SAFETY.md` rule and `check_no_view_returns` are kept as
a belt rather than as the guarantee. **Cheaper than it looked when decided:**
the compiler session has since scheduled the fix as DEF-3 in 1.5.1b, in the
same batch as O-N4's, hours out.

---

## Claim protocol

1. The orchestrator writes `CLAIMED sN` against the **repository** in its
   stream table — a stream owns the whole repository while it works on it
   (W-7) — and a row in the in-flight table naming the subcycle, the agent
   label (`s<N>-<pkg>-<cycle>.<sub>-<HHMM>`), the time and the model. One
   commit: `board: claim <repo> <cycle>.<sub> for sN`.
2. One worker works that subcycle (W-15). When it reports, the verifier runs
   (W-21).
3. On PASS the in-flight row advances to the next subcycle. At a cycle's
   close the claim advances to the repository's next cycle if its gate is
   ready, else to its next ungated cycle (W-9), else it is released and the
   row removed: `board: release <repo>`. Then check whether any `BLOCKED`
   row just became free.
4. A claim with no live agent in the current session is stale — the
   orchestrate skill's recovery procedure runs before any dispatch (W-19).

**A claim is a commit.** The history of this file is the record of who worked
what and when, which is the thing the compiler's R8 says the orchestrator owns.

---

**EVERY `SAFETY.md` PATH IN THE STREAM TABLES BELOW WAS WRONG, IN ALL FIVE
ROWS, AND THE LINE NUMBERS WERE RIGHT — WHICH IS WHY NOBODY CAUGHT IT.**
Corrected 2026-09-05. The board said `specs/SAFETY.md:NN`; the file is
`meta/specs/SAFETY.md:NN` in **all five libraries**, checked one at a time
rather than inferred from the first. Eight occurrences across five lines — and
note `grep -c` reports **5**, because it counts *lines* and not *matches*,
which is the denominator lesson arriving in the instrument used to measure the
denominator.

**Why it survived: the wrong half was the half nobody verifies.** A line number
is obviously a thing to re-check and gets re-checked; a directory prefix reads
as part of the file's name and is copied forward. A worker following one of
these would have found no file at all — the *lucky* failure, since the
unlucky one is a path that resolves to something else. **A citation is a path
AND a line, and this ecosystem has been re-deriving line numbers while
copying paths.**

**AND TWO ITEMS WERE LISTED AS OWED AFTER THE TREE HAD ALREADY DISCHARGED
THEM** — `nitpick-time`'s RX-111 and its two lagging leak-gate sites, both
found by the 0.0.2 worker checking its inherited NOTES against the files
instead of working from them. **This is the opposite staleness from the kind
this board guards against.** Every check here asks *"is a claimed fix real?"*;
nothing asks *"is a claimed debt still owed?"* — and that direction costs a
whole dispatch, silently, because re-fixing a fixed thing looks exactly like
work. `nitpick-regex`'s RX-111 is likewise discharged. **Three genuinely
remain: `nitpick-tui`, `nitpick-parse`, `nitpick-sockets`.**

---

## SHARED FINDINGS — what `nitpick-time` learned that the siblings probably inherit

### THE 0.1.0 PAIR — TWO LANGUAGE FACTS THAT MAKE EVERY LIBRARY HERE OVERCLAIM, verified 2026-09-06

**Both measured at `aaffb87` by `s2-ntime-0.1.0-0235` and carried on a VERIFIED
PASS. They are not `nitpick-time`'s to fix and they are not defects — they are
what the language is, reaching claims that four other repositories have already
written down.**

**(1) A `pub struct` HAS NO PRIVATE FIELDS, so "cannot be constructed invalid"
is a claim the language does not support.** `opaque struct:Name = { … };` is
refused — the bodyless form is the extern-driver declaration (D-149). So a
validating constructor's guarantee is about the values **a library PRODUCES**,
never about the type: **a consumer's struct literal compiles, links and runs.**

| Repository | The type making the claim |
|---|---|
| `nitpick-regex` | a compiled pattern |
| `nitpick-parse` | a validated layout |
| `nitpick-sockets` | a parsed address |
| `nitpick-tui` | a validated cell/geometry |
| `nitpick-time` | `CivilDate` — **found here, and the reason the others are listed** |

**The enforceable half is a tree check over the library's own `src/`** — which
is exactly the shape both of this repository's shipped use-after-frees came
from, so it is a real instrument and not a consolation. **Each repository states
the honest claim at its next claim (W-7); do not fix another stream's
repository.** The honest form: *this library never returns an invalid X, and a
caller building one by struct literal has opted out.*

**(2) An `error:` IDENTITY CANNOT CARRY A PAYLOAD — the error half of every
return in this language is a CODE.** `pub error:E(Detail);` is
`NITPICK-PARSE-001`, exit 1, no `.ll`; a `Result<T>` is `{ T value, tbb32 err }`,
so there is nowhere for a payload to live. **`PLAYBOOK.md` §3's rule — *declare
ONE identity and put the detail in a rich value the caller reads* — therefore
contains an unanswered question**, because the natural reading of *"rides as a
detail field"* names a field that does not exist. **Every library needs an
explicit answer for how the detail reaches the caller.** `nitpick-time`'s is
open as **O-X8** with a recommendation (a `never fails` companion classifier);
the four siblings have not yet been asked the question.

**Why this pair is worth reading twice.** Neither was found by a gate. Both were
found by a worker writing a type and discovering the language would not let it
say what the specification said. **The specifications were written in the shape
of a language that has private fields and payload-carrying errors** — the shape
every author here came from — and nothing in this ecosystem would have reported
that until a library tried to compile it.

---

**Four things, found in three consecutive subcycles, and the reason they are
shared is the same in every case: these repositories were scaffolded from one
template, so a defect in the template is a defect in five trees.** Stated once
here with its evidence rather than pasted into five rows — this board already
carries `RX-120` verbatim four times, and text copied five ways is text that
drifts. **Each is carried into that repository's next dispatch by the
orchestrator; none is fixed in another stream's repository (W-7).**

**None of these blocks anything today.** Every one of them is a plan or a
document that will fail *when executed*, which is precisely why they are worth
carrying now rather than meeting one at a time.

| # | Finding | Who it hits | What to check, in one command |
|---|---|---|---|
| **1** | **TM-114 — `BUILD.md` §3's stage table is incomplete.** It was missing the compiler's **default `compile` stage** and assigned `tests/conformance/` to **`accept`** — *"accepted in silence"*, which is the O-N11 shape: a root with `main` and no `failsafe` is accepted at `npkc` exit 0 and refused only later | **all four siblings**, template-shared | Does your §3 carry a `compile` row, and what stage is `tests/conformance/` on? |
| **2** | **TM-117 — separate compilation DOES NOT EXIST, and this is the documented model rather than a defect.** Two `npkc`-produced objects are a duplicate-symbol error (`ld.lld` exit 1, 121 lines) because every compile emits the whole reachable graph **including the prelude**. `BUILD_REFERENCE` §4.1 at the pin: *"takes one program object and adds the runtime object; there is no parameter through which a third input could enter"* | **any sibling whose harness plan says "compile the library once, link each program against it"** — it is the natural decision to write, and `nitpick-time`'s P-16 said exactly that | `grep -n 'once' meta/roadmap/0.0/0.0.2.md` — a plan naming one library object cannot be executed as written |
| **3** | **The compiler's frontend tools are `.npk` SOURCE, not binaries.** `tools/parse_check.npk` imports twenty frontend modules and `tools/check.npk` the whole driver pipeline, so *"build the compiler's tools once per run from the pinned checkout"* means **building the compiler**, from a tree routinely ahead of our pin | **any sibling naming `tools/parse_check` or `tools/check` in a harness plan** | `git grep -n 'parse_check\|tools/check' -- 'meta/'` |
| **4** | **`NITPICK-REACH-003` LISTS THE IDENTITIES OWED — an OPPORTUNITY, not a defect.** Compile a program importing one module with no `failsafe` and the refusal names **every arm a consumer of that module will owe** | **every library with an error budget** — all five | Verified in `nitpick-time` both directions on three specimens: floor **4**, `arms_lib` **5**, `calc_lib` **8** |

**TWO MORE, ADDED 2026-09-06 FROM `nitpick-time`'s FIRST-EVER CI RUN — and
these are in the shared CI workflow, so every sibling that copied it has them
until it looks.**

| # | Finding | Who it hits | What to check |
|---|---|---|---|
| **5** | **A whole-tree sweep must PRUNE NESTED REPOSITORIES and say what it pruned.** CI checks the pinned compiler out **inside the workspace**, so a library's sweep walks the **whole compiler** on its first CI run — locally invisible, because the compiler is a sibling directory rather than a child. **Prune by SHAPE — a directory containing `.git` — not by name**, which is the version that survives someone checking out something else. `nitpick-time` reports `1 nested repository pruned: .nitpick` | **every sibling with a whole-tree sweep** | Run the sweep with a repository checked out inside the workspace and see whether the denominator explodes |
| **6** | **A GitHub `run:` block ALREADY HAS `-e` ON.** The default shell is `/usr/bin/bash -e {0}`, and **`set -uo pipefail` does not clear it** — so any step that captures a log and prints it on failure dies before the print, and the operator sees a bare exit code where the diagnosis was. Needs an explicit **`set +e`** (TM-146) | **any sibling that copied this workflow** | `grep -n 'set -' .github/workflows/ci.yml` — look for a capture-then-print step with no `set +e` |

**`nitpick-regex` has already run CI green**, so it either solved these differently or has a sweep small enough not to notice — **worth a check before its next close rather than an assumption either way.**

**On #2, the framing matters more than the fact.** *"`npkc` has no separate
compilation"* is true and points at the compiler. *"Our plan assumed a model
the compiler never offered"* is also true, points at the plan, and is the only
one of the two that can be acted on. The compiler session confirmed it is not
a defect and **offered to put separate compilation to the author as a design
row if the libraries need it** — this workbench answered **not yet**, because
1.5.2d's step 2 removes ~94% of the cost that would motivate the ask. Re-pin,
re-measure, then decide. The offer is on the record and does not expire.

**On #4, the trap inside the opportunity:** the identity count is **per
program** — the same diagnostic names **four** identities for one fixture and
**six** for another, differing by an import and some arithmetic. This board
once generalised one program's floor to the set and cited the compiler's own
output for it. Read each program's own bill.

**And the substitute for #3 is better than the thing it replaces.** `npkc` has
no parse-only mode, but **a diagnostic's CODE FAMILY answers the question**:
LEX and PARSE are the parse phase and every other family is later, so **a file
refused at TYPE, BORROW or REACH necessarily parsed.** No extra tool, no build,
and it reads the compiler's own classification instead of reimplementing it.

**`nitpick-posix` IS A SIXTH TREE AND IS NOT EXEMPT — it is only out of
reach.** It lives in `../nitpick-apps/`, outside this workbench's write scope,
so nothing here may touch it; but it was scaffolded the same way, so **findings
1 and 3 plausibly apply to it and finding 4 certainly does** (it consumes three
of these libraries, so it owes their arms). **Say so at stream 3's claim rather
than letting the five-row table imply it was checked.** The table above lists
five because five is what this workbench can write to, and a scope boundary is
not a clean bill of health — which is exactly the *"a check whose name
describes the property while its mechanism covers something narrower"* shape
this ecosystem keeps meeting, arriving this time in a table's row count.

**Still outstanding from earlier sweeps, unrelated to the four above but owed
by the same three repositories:** `RX-111`'s false bounds promise remains in
**`nitpick-tui`** (`meta/specs/SAFETY.md:24`), **`nitpick-parse`** (`:22` — the
worst instance, since a parser's index is attacker-influenced) and
**`nitpick-sockets`** (`:28`). `nitpick-time` and `nitpick-regex` are
discharged, verified by reading.

---

## THE CONSUMER MAP — the applications are the libraries' test bed, and it is ALREADY SHAPING THEIR DESIGNS

**Confirmed by the author 2026-09-06 and then read out of
`nitpick-apps/nitpick-posix/README.md:47` rather than taken from the
conversation.** The applications are not a separate work area: they are *"the
consumers of some of the libraries we made here as a way to test them while
making useful things"*. A library exercised only by its own harness is tested by
the people who wrote it; a library exercised by a real program is not. **This is
the same argument as the planted fault, one level up.**

```
grep   ->  nregex   ("and a stated conformance departure")
date   ->  ntime    ("POSIX +%Y formatting is parsed HERE and mapped onto
                      ntime's typed layout; the library has NO format-specifier
                      language and DOES NOT NEED ONE")
```

**TWO THINGS THAT CHANGE PLANNING, NOT JUST CONTEXT.**

**(1) `nitpick-time`'s scope boundary is already decided, and stream 2's next
cycle is where it bites.** The format-specifier language lives in **`date`**, not
in `ntime`. A planner opening 0.1.1 who assumes the library owes a `strftime`-
shaped formatter would build a feature the consumer's own README says it must not
have. **Carry this into 0.1.1's dispatch.**

**(2) `nregex` has no back-references BY DECISION, and `grep` — the program most
likely in the whole set to be pointed at hostile input — refuses one by name,
with the reason and the byte offset.** Not silently accepted, never quietly
reinterpreted; a documented conformance departure, the same choice `ripgrep`
makes. **That is the same rule the cycle-0.0 audit invoked to make BL-2's
non-terminating loop a BLOCKING finding** — catastrophic backtracking is a denial
of service, and the language has no cancellation to survive one. The library's
safety property and the application's conformance departure are one decision
seen from two sides.

**⚠ CORRECTION, 2026-09-06: THIS BOARD SAID "2 OF 5 LIBRARIES HAVE A NAMED
CONSUMER" AND THAT WAS WRONG. ALL FIVE DO.** The claim was made from
`nitpick-posix/README.md`'s table, which says **"Known so far"** and whose very
next line points at **`../APPS.md`** as *"the summary"* — a pointer this session
grepped straight past. **Stating a wrong number WITH a denominator is worse than
stating it without one, because the denominator is what makes it look
measured**, and this session had spent the day insisting on exactly that.

**The real map, assembled from the three documents that hold it:**

```
nregex     grep                                        posix README + APPS.md
ntime      date, crontab, at                           APPS.md
nparse     a configuration linter, OWN REPOSITORY      APPS.md (PA-103) + nparse ROADMAP 0.12
ntui       a log viewer, OWN REPOSITORY                APPS.md (T-104/114/115) + ntui ROADMAP 0.15
nsockets   a TCP proxy with an AF_UNIX admin socket    nsockets ROADMAP 0.9 -- and it lives in examples/
```

**SO THE ACTUAL FINDING IS NOT A MISSING CONSUMER, IT IS A MISSING MAP.** The
information is spread across `nitpick-posix/README.md` (2 rows, scoped and
honest about it), `nitpick-apps/APPS.md` (the linter, the log viewer, `vi`,
`make`) and **each library's own `ROADMAP.md`** (`nsockets` names its dogfood
application at 0.9 and nothing outside that file knows). **No single document
holds all five** — which is the fifth instance in two days of *a fact written in
the document that discovered it and never carried to the document that owns it*.
The workbench-side map now lives in `LIBRARIES.md`, mirroring `APPS.md` from the
library side.

**AND ONE ASYMMETRY THAT IS A REAL RECOMMENDATION RATHER THAN AN ARTEFACT OF THE
SEARCH.** `nparse`'s and `ntui`'s consumers are **their own repositories**;
`nsockets`'s is **`examples/` inside the library itself**. The author has
confirmed that a consumer need not be a POSIX utility — **anything that is not
one simply lives in the parent `nitpick-apps` folder** — so the in-repo placement
is not forced by the layout. **The whole argument for the arrangement is that a
library exercised only by its own harness is tested by the people who wrote it,
and an `examples/` program is written by exactly those people.** The proxy is a
well-chosen program — streams, Unix sockets, descriptor passing, the bounded
accept loop, half-close and `poll_set` in one thing with a purpose — and the
recommendation is only about **where it lives**, not what it is.

---

## Stream 1 — text

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-regex` | 0.0 … 1.0 (16) | `CLAIMED s1` | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent; nothing gates it. **RX-111 found and already corrected here — its `SAFETY.md:20` and Rule S-23's per-type table are the wording the other four take.** **~~Q-10 sweep — the leak gate that cannot fail:~~ DISCHARGED at 0.0.4, AND THE LIST WAS WRONG IN BOTH DIRECTIONS.** It named 4 sites — `0.0/README.md:130`, `0.0/0.0.4.md:14`, `meta/specs/SAFETY.md:25`, `0.0/0.0.0.md:314` — and the verifier read all four: **two are MISCITATIONS to unrelated content** (`README.md:130` is the harness module list; `0.0.0.md:314` is reserved-word syntax notes) and **two already carried the correction inline** (`0.0.4.md:14` is qualified by its very next line; `SAFETY.md:25` states the corrected form in full). **So none of the four ever stated the bald claim, and the worker's own three-way sweep of 126 tracked files found 13 candidates, 12 correct or exempt, and ONE GENUINE SITE THAT WAS NOT ON THE LIST AT ALL.** A list that is simultaneously stale and short is worse than no list, because it is actioned. **RE-DERIVE PER REPOSITORY BEFORE DISPATCHING IT AGAIN — never carry this list forward by copying it** |
| 2 | `nitpick-tui` | 0.0 … 1.0 (18) | — | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent. **RX-120 HAS EXPIRED AT PIN `3d15ac9` — THIS ROW CARRIED THE OPPOSITE OF THE TRUTH, IN FOUR REPOSITORIES AT ONCE.** It read: *the undefined-symbol scan CANNOT SEE A SYSCALL* — 29 symbols each way, diff empty, because `npk_sys6` is already the prelude's. **True at `950bb1d`, FALSE at `3d15ac9`.** D-262's prelude trim stopped emitting `npk_sys6` into a program that does not use it, so the scan now **can** see one: **floor 2, syscaller 3, difference exactly `{npk_sys6}`**. **A PIN-DEPENDENT MEASUREMENT WAS RECORDED AS A PERMANENT PROPERTY** — the same shape as the `never fails` / TYPE-037 claim `nitpick-regex` also shipped as permanent and has now retracted. **STILL REPLACE IT WITH THE IR CALL-EDGE SCAN, for a better reason than before:** the call-edge scan is strictly stronger *and* pin-independent, while the symbol layer is now a **residue diff** — a reviewed list with a reason per line — rather than an emptiness claim, and a residue diff moves whenever the prelude does. **Do not mark the symbol-diff acceptance item met just because the numbers work now; they work at this pin.** *(Honest limit, from the verifier: the 2-vs-3 reading is recorded in three places — `harness/build.py:292`, `meta/DECISIONS.md:1679`, `0.0.4.md:300` — but is **asserted, not mechanically reproduced**; there is no committed transcript, unlike the original `950bb1d`-era table. And `harness/selfcheck.py:230`'s docstring still reads "the undefined-symbol sets are identical, 29 each way", stale against the very subcycle that found this.)*  Inherits stream 1's Unicode approach from `nregex`. **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `meta/specs/SAFETY.md:24`, "An out-of-range cell index is a *crash*, not a smear". **Q-10 sweep — the leak gate that cannot fail:** 5 sites — `0.0/README.md:125`, `0.0/0.0.4.md:16`, `meta/specs/SAFETY.md:27,216`, `0.0/0.0.0.md:353`. Fix at this stream's claim |
| 3 | `nitpick-logview` | — | `BLOCKED on nitpick-tui 0.14` | repository not created; created at `ntui` 0.15's open (T-115) |

## Stream 2 — data

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-time` | 0.0 … 1.0 (10) | `CLAIMED s2` | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent. **RX-120 HAS EXPIRED AT PIN `3d15ac9` — THIS ROW CARRIED THE OPPOSITE OF THE TRUTH, IN FOUR REPOSITORIES AT ONCE.** It read: *the undefined-symbol scan CANNOT SEE A SYSCALL* — 29 symbols each way, diff empty, because `npk_sys6` is already the prelude's. **True at `950bb1d`, FALSE at `3d15ac9`.** D-262's prelude trim stopped emitting `npk_sys6` into a program that does not use it, so the scan now **can** see one: **floor 2, syscaller 3, difference exactly `{npk_sys6}`**. **A PIN-DEPENDENT MEASUREMENT WAS RECORDED AS A PERMANENT PROPERTY** — the same shape as the `never fails` / TYPE-037 claim `nitpick-regex` also shipped as permanent and has now retracted. **STILL REPLACE IT WITH THE IR CALL-EDGE SCAN, for a better reason than before:** the call-edge scan is strictly stronger *and* pin-independent, while the symbol layer is now a **residue diff** — a reviewed list with a reason per line — rather than an emptiness claim, and a residue diff moves whenever the prelude does. **Do not mark the symbol-diff acceptance item met just because the numbers work now; they work at this pin.** *(Honest limit, from the verifier: the 2-vs-3 reading is recorded in three places — `harness/build.py:292`, `meta/DECISIONS.md:1679`, `0.0.4.md:300` — but is **asserted, not mechanically reproduced**; there is no committed transcript, unlike the original `950bb1d`-era table. And `harness/selfcheck.py:230`'s docstring still reads "the undefined-symbol sets are identical, 29 each way", stale against the very subcycle that found this.)*  **~~RX-111~~ — DISCHARGED HERE, verified by reading 2026-09-05.** `meta/specs/SAFETY.md:315` now reads *"An out-of-range read is **a wrong value**, not a crash"* and `:332` *"**An unchecked index is a WRONG ANSWER, not a crash**"*. The board carried it as outstanding after it had been fixed, and would have dispatched it a second time. **`nitpick-regex` is likewise discharged** (`:269`). **Three remain: `nitpick-tui`, `nitpick-parse`, `nitpick-sockets`** — checked individually, not inferred from this one. Smallest first item; finishes early and can take slack. **Q-10 sweep — the leak gate that cannot fail:** **DISCHARGED IN FULL, verified by reading 2026-09-05** — the specs, `DECISIONS.md` and `0.0.4.md` already carried it, and the two that were listed as lagging (`0.0/README.md:100`, `0.0/0.0.0.md:299`) **do carry the correction too**: `0.0.0.md` now reads *"Exit 0 means 'no `wild` allocation is live' (D-151) — that, and nothing more"*. **Nothing outstanding here.** Both this and RX-111 above were listed as owed after the tree had discharged them, found by the 0.0.2 worker checking its inherited NOTES against the files rather than working from them — **a board that is stale in the "still owed" direction costs a whole dispatch, and nothing in this ecosystem checks for it** |
| 2 | `nitpick-parse` | 0.0 … 1.0 (15) | — | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent. **RX-120 HAS EXPIRED AT PIN `3d15ac9` — THIS ROW CARRIED THE OPPOSITE OF THE TRUTH, IN FOUR REPOSITORIES AT ONCE.** It read: *the undefined-symbol scan CANNOT SEE A SYSCALL* — 29 symbols each way, diff empty, because `npk_sys6` is already the prelude's. **True at `950bb1d`, FALSE at `3d15ac9`.** D-262's prelude trim stopped emitting `npk_sys6` into a program that does not use it, so the scan now **can** see one: **floor 2, syscaller 3, difference exactly `{npk_sys6}`**. **A PIN-DEPENDENT MEASUREMENT WAS RECORDED AS A PERMANENT PROPERTY** — the same shape as the `never fails` / TYPE-037 claim `nitpick-regex` also shipped as permanent and has now retracted. **STILL REPLACE IT WITH THE IR CALL-EDGE SCAN, for a better reason than before:** the call-edge scan is strictly stronger *and* pin-independent, while the symbol layer is now a **residue diff** — a reviewed list with a reason per line — rather than an emptiness claim, and a residue diff moves whenever the prelude does. **Do not mark the symbol-diff acceptance item met just because the numbers work now; they work at this pin.** *(Honest limit, from the verifier: the 2-vs-3 reading is recorded in three places — `harness/build.py:292`, `meta/DECISIONS.md:1679`, `0.0.4.md:300` — but is **asserted, not mechanically reproduced**; there is no committed transcript, unlike the original `950bb1d`-era table. And `harness/selfcheck.py:230`'s docstring still reads "the undefined-symbol sets are identical, 29 each way", stale against the very subcycle that found this.)*  **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `meta/specs/SAFETY.md:22` says "Indexing is bounds-checked and traps ... An index derived from input is a *crash*, not a smear". **The worst instance in the ecosystem** — a parser's index is attacker-influenced by definition, so this is a security claim and it is wrong. **Q-10 sweep — the leak gate that cannot fail:** **the worst case, 9 sites** — `0.0/README.md:104,135`, `0.0/0.0.4.md:20`, **`0.4/README.md:43`**, `meta/specs/SAFETY.md:35,237,283`, `specs/VALUE_MODEL.md:214`, `0.0/0.0.0.md:354`. It is a parsing library, so managed bodies are everywhere and `string_slice` allocates (D-186); `0.4/README.md:43` puts the false gate on `doc_destroy`, which is exactly an owning structure D-151 cannot see. Fix at this stream's claim |
| 3 | `nitpick-conflint` | — | `BLOCKED on nitpick-parse 0.11` | repository not created; created at `nparse` 0.12's open (PA-103) |

## Stream 3 — system

| # | Repository | Cycles | State | Notes |
|---|---|---|---|---|
| 1 | `nitpick-sockets` | 0.0 … 1.0 (12) | — | **SHARED FINDINGS above apply here — carry them into this repository's next dispatch.** independent. **RX-120 HAS EXPIRED AT PIN `3d15ac9` — THIS ROW CARRIED THE OPPOSITE OF THE TRUTH, IN FOUR REPOSITORIES AT ONCE.** It read: *the undefined-symbol scan CANNOT SEE A SYSCALL* — 29 symbols each way, diff empty, because `npk_sys6` is already the prelude's. **True at `950bb1d`, FALSE at `3d15ac9`.** D-262's prelude trim stopped emitting `npk_sys6` into a program that does not use it, so the scan now **can** see one: **floor 2, syscaller 3, difference exactly `{npk_sys6}`**. **A PIN-DEPENDENT MEASUREMENT WAS RECORDED AS A PERMANENT PROPERTY** — the same shape as the `never fails` / TYPE-037 claim `nitpick-regex` also shipped as permanent and has now retracted. **STILL REPLACE IT WITH THE IR CALL-EDGE SCAN, for a better reason than before:** the call-edge scan is strictly stronger *and* pin-independent, while the symbol layer is now a **residue diff** — a reviewed list with a reason per line — rather than an emptiness claim, and a residue diff moves whenever the prelude does. **Do not mark the symbol-diff acceptance item met just because the numbers work now; they work at this pin.** *(Honest limit, from the verifier: the 2-vs-3 reading is recorded in three places — `harness/build.py:292`, `meta/DECISIONS.md:1679`, `0.0.4.md:300` — but is **asserted, not mechanically reproduced**; there is no committed transcript, unlike the original `950bb1d`-era table. And `harness/selfcheck.py:230`'s docstring still reads "the undefined-symbol sets are identical, 29 each way", stale against the very subcycle that found this.)*  **RX-111 — the `SAFETY.md` bounds promise is FALSE and must be corrected at this stream's claim:** `meta/specs/SAFETY.md:28` says an out-of-range `sockaddr` read is "a *crash*, not a leak of adjacent memory" — a claim that there is no information disclosure, and it is wrong. **Q-10 sweep — the leak gate that cannot fail:** 5 sites — `0.0/README.md:134`, `0.0/0.0.4.md:14`, `meta/specs/SAFETY.md:26`, `specs/VERIFICATION.md:48`, `0.0/0.0.0.md:328`. Its `ANCILLARY_MODEL.md:67` and `SAFETY.md:221` are correctly scoped already ("takes no `wild` bytes") and are the model for the rest. D-188 covers the driver/process registry, not managed bodies. Fix at this stream's claim |
| 2 | `nitpick-posix` | 0.0 … 1.0 (14) | — | **Q-10 sweep — the leak gate that cannot fail:** 2 sites, both in `0.0/0.0.0.md:37,226` (`nitpick-apps/nitpick-posix`, outside this workbench's write scope). **O-N6 answered 2026-09-03 by probe 02** — negatively, and the repository absorbed it (PX-100: `failsafe` is generated). W-1 is discharged. Nine of its cycles are ungated and are the slack this stream uses when a gate is not ready. **Q-1 answered 2026-09-03:** POSIX.1-2024 (Issue 8) is current and its utility table moved by 19 entries — the first worker here files the digest and amends `SCOPE.md`, `CONFORMANCE.md` K-1 and `GLOSSARY.md`; the syntax guidelines are unchanged |

---

## The cross-stream gates

Each is mutual (W-3): the utility needs the library finished, and the library's
dogfood cycle needs the utility written **and used**.

| Gate | Needs | Blocks | Expected around |
|---|---|---|---|
| `nitpick-posix` 0.5 — `grep` | `nitpick-regex` closed | `nitpick-regex` 0.14 | s1 unit 16 ↔ s3 unit 17 |
| `nitpick-posix` 0.7 — `date`, `crontab` | `nitpick-time` closed | `nitpick-time` 0.7 | s2 unit 10 ↔ s3 unit 19 |
| `nitpick-posix` 0.11 — `awk` | `nitpick-parse` **and** `nitpick-regex` closed | — | s2 unit 25 ↔ s3 unit 23 — **tight; see below** |
| `nitpick-logview` | `nitpick-tui` closed, `nitpick-regex` closed | `nitpick-tui` 0.15 | s1, internal |
| `nitpick-conflint` | `nitpick-parse` closed | `nitpick-parse` 0.12 | s2, internal |

**The one tight gate.** `awk` wants `nparse` at about the moment stream 2 is
still finishing it. If stream 3 arrives first it takes `nitpick-posix` 0.12
(terminal, archive, compare) out of order — it is ungated — and returns to
`awk` after. W-9 is the rule; this is the case it was written for.

---

## The cross-machine digest procedure — run it when 1.5.2f lands

**From `nitpick-compiler_s0`, and on the board because it arrived after the
sixth orchestrator's clean stop and no earlier board carried it.** Six digests
for localising a cross-machine `npkc` difference. **Compare in this order; the
first that differs names the stage**, and stop there.

| # | Artifact | Digest at `aaffb87` | What it is |
|---|---|---|---|
| 1 | `builder.o` | `3b5f868dbab44253…` | the snapshot assembled by `llc` |
| 2 | `builder` | `f5c7f5174fc6fa11…` | linked by `ld.lld` |
| 3 | `npkrt.o` | `c9ddbcffd32eccc7…` | identical on the runner |
| 4 | **`npkc.ll`** | `f0abbfd09ce5ef18…` | **THE EMISSION**, 21 483 280 B |
| 5 | `npkc.o` | `a46983645fa690f4…` | |
| 6 | `npkc` | `a3b0dadc650421b2…` | |

**How to read the first difference:**

- **`npkc.ll` differs → a COMPILER DEFECT, and they want the diff.** This is
  the only outcome that is ours to escalate.
- `builder` or `builder.o` differs while `npkc.ll` matches → the runner's own
  LLVM build. Not a defect.
- `npkc.o` differs with `npkc.ll` identical → `llc` codegen between two 20.1.2
  builds. Not a defect.
- `npkc` differs with `npkc.o` identical → `ld.lld` layout or a build-id. Not a
  defect.

**Why the order is the procedure and not a convenience.** The emission is the
cross-machine claim and **the binary never was** — CI already measured the case
that proves it: `npkrt.o` is byte-identical across machines and `npkc` is not
(`3c05818c…` in CI against `a3b0dadc…` here). A build of the pinned commit is
**behaviourally** equivalent and the suite passing is what carries the weight;
byte-identity across machines was never measured and is not claimed. **From
1.5.2f's notice on, the compiler side carries `npkc.ll`'s digest beside
`npkc`'s** for exactly this reason, and that change came out of this finding.

---

## Compiler dependencies

Nothing here blocks implementation. Recorded so that a stream reaching its
hardening cycle knows what it is waiting for. The ids are the workbench
registry's ([`meta/OPEN_QUESTIONS.md`](meta/OPEN_QUESTIONS.md) §"For the
compiler"), because `O-N` numbers are per repository and collide.

| Compiler | Needed by | State |
|---|---|---|
| 1.5.1 – 1.5.4 (verification surface) | every library's hardening cycle | compiler at 1.5.0 |
| **1.5.1b — the workbench's three defects** | `nitpick-time` 0.0.5, 0.5 and all `src/fmt/` work | **PLANNED AND RATIFIED 2026-09-03**, `meta/roadmap/1.5/1.5.1b.md` at the compiler's `4bf3e47`. Five commits: DEF-2 (our O-N8) first because it is independent, DEF-3 (our O-N9), DEF-1's three backend text builders (our O-N4), then **D-246** statement-end temporaries and **D-247** `List<T>` as owning — plus a **step 0** that builds `NPK_HEAP_STATS`, an allocator-level instrument for **managed** memory (allocated, peak_live, count), and a `cost` harness stage. Step 0 is the instrument this workbench's 0.0.4 gate needs and does not have (Q-10): run on our own two container probes it reports **peak_live 41 321 bytes against 400 101 320**, the pair that both exited 0. Starts when 1.5.1's last four steps land. **IN FLIGHT 2026-09-03 22:40. 1.5.1 is CLOSED and pushed (compiler `main` `e668f6a`).** 1.5.1b runs as cumulative prefixes, each in its own worktree behind a full ~3 h harness that must be green before it lands: **step 0** (the instrument, the `cost` stage, DEF-1's recipes and the baseline) committed, harness from 21:34; **step 1** (DEF-2, D-248) committed, harness from 22:05; **step 1b** (DEF-5) committed, harness from 22:11; **step 2** (DEF-3, D-249) written, its checker sweeping the compiler's own `src/` now. Steps 3 (the builders), **3b (DEF-4, now D-250)**, 4 (D-246) and 5 (D-247) follow, then the snapshot refresh and the landing message. Order confirmed: DEF-2 → DEF-3 → DEF-1 → D-246 → D-247, with 3b inserted between the builders and D-246. 1.5.1's four prefix harnesses are at the parity stage; step 0 is being built in a detached worktree, and **its first self-build found a defect in the instrument itself** (the exit-time report walked a heap-resident environment slice after the compiler's wholesale release), being fixed there — so 0.0.4's `peak_live` gate must be commissioned against a known-leaking and a known-clean control before it is trusted (Q-10). The compiler session messages this workbench at the landing with the commit, whether `build/` was written after it, and the after-numbers on our own recipes |
| **D-248** (`mod:` header mandatory and first; `main`/`failsafe` root-only) | every library, at the re-pin | **RATIFIED**, lands in 1.5.1b. **Re-checked 2026-09-03 against a consequence we had not been told: a module name is an IDENTIFIER**, so a `.npk` file named after a reserved word, or beginning with a digit, refuses under D-248 — the compiler renamed five of its own files for this. **Swept all six repositories: zero violations**, because `nitpick-regex` had already fixed its leading-digit case at `d6fb0ce`. Any NEW file must clear `PLAYBOOK.md` §10's list. **Costs this ecosystem nothing if we keep writing as we do** — all 17 `.npk` in `nitpick-time` and all 8 in `nitpick-posix` already comply. See `PLAYBOOK.md` §2 |
| **D-249** (the `Views` column) | the fix behind DEF-3 / O-N9 | **RATIFIED**, lands in 1.5.1b |
| **O-N12** (`>>>` and `string_repeat` documented and absent) | nobody — W-27: blocks nothing, both have substitutes | **SETTLED 2026-09-03 the way this workbench recommended — documents, not implementation** — landing inside 1.5.1b step 2's commit. The `>>>` row is gone and the `>>` row now states the rule that makes the table make sense: *arithmetic on a SIGNED operand, logical on an UNSIGNED one; the operand's signedness decides*, confirmed against the single shift arm in their emitter. `BUILTIN_REFERENCE` §2's "fast compiler intrinsics" sentence — the actual trap — now says none of those names resolves without a row in a marked table. `string_repeat` stays listed as planned library surface at this workbench's recommendation: the harm was the intrinsics sentence, and **no library here plans a string-utility surface**, so nobody is on it |
| O-N2 (`npkg` builds a library) | retiring six Python harnesses | **not on the compiler's 1.5 or 1.6 map** — a request, not a date |
| O-N1 (`clone_exec` signal mask) | `ntui` 0.1.6, cosmetically | request raised |
| O-N5 (`npkg` multi-artifact) | `nitpick-posix`'s build | request raised |
| ~~O-N6~~ (macro splices a `pick`) | `nitpick-posix`'s **shape** | **ANSWERED 2026-09-03: no.** Probe 02, seven programs. A macro is not shareable across modules at all (`MACRO-007`); `failsafe` is generated instead (PX-100). Shape changed, schedule did not |
| ~~**O-N4**~~ (`npkc` quadratic in one declaration's size) — **DISCHARGED, verified here** | **blocks nothing now.** It did block `nitpick-time` **0.0.5** (the tzdb size spike must compile a real emitted table) and **0.5** (the generator). TM-007's tzdb is 26 838 rows and the measured 281 s / 30.9 GiB is `probe04`'s **30 000** (`[30000 x ZoneTransition]` in the emitted IR) — the two counts had been conflated here and in `RECORD.md:2275`; the probe is the larger, so no conclusion moves, so a 16 GiB machine and CI cannot build the library in its shipping shape, and every consumer pays it. It does **not** block 0.0.1–0.0.4, which carry no large declaration | **DISCHARGED — VERIFIED HERE 2026-09-04 12:27, on this workbench's own measurement against pin `94874ce`, not on the correspondent's report.** Both recipes, three runs each, `/usr/bin/time -f "%e s  %M KiB" $NPKC <file> -o <out>.ll` — the command `tests/probe/defect/README.md:196` records for the before-numbers. `big_fixed_array_cost.npk` (4 000 rows): **0.24–0.25 s at 28 768–28 960 KiB**, was 5.30–6.19 s at ~593 592–593 992 KiB. `probe04_big_fixed_table.npk` (30 000 rows): **1.19–1.32 s at 74 936–74 996 KiB**, was 281 s and 30.9 GiB — **~430× less peak and ~227× less time**, against a reported 1.15 s / 75.2 MB, which this reproduces. The relation is no longer quadratic: 7.5× the rows costs 5.0× the time and 2.6× the peak (quadratic would be ~56×). **And the speed is not bought by emitting less** — the check that would have made this a hollow green. `npkc` exit 0 was paired every run with an `.ll` actually written (2 672 442 bytes), carrying `@"npk.probe04_big_fixed_table.TRANSITIONS" = constant [30000 x …]` with **30 000 `i64` rows present**; `llc -filetype=obj` then **accepts** it (exit 0, 0.61 s, 660 360 B), and the symbol lands in **`.rodata`, flags `A` and not `W`, size 0x75300 = 480 000 B = 30 000 × 16** — which independently re-confirms **S-19** (`fixed` module state is read-only, no startup initialisation). The `llc` leg was run because *`npkc` exit 0 is not well-formedness* — O-N11 is precisely that shape — so a discharge measured on `npkc` alone would not have been one. Instrument commissioned first, positive and negative: a real tree file (`probe11d_floor_only.npk`) exit 0 with an `.ll`, and a malformed file exit 1 with none. **`nitpick-time` 0.0.5 and 0.5 are UNBLOCKED.** History: | **BISECTED 2026-09-03** — the frontend is *linear* on all three axes; the quadratic is three text builders in `src/backend/` that re-concatenate an accumulator per element, per trap site and per byte, compounded by D-183's never-dropped owning temporaries. Neither of the workbench's two relayed hypotheses (identifier length, then total source bytes) survived measurement. Scheduled in **1.5.1b**. **ACCEPTED 2026-09-03** by the compiler session, which owns `npkc`'s frontend. Recorded there as **DEF-1** (`meta/roadmap/OPEN_DECISIONS.md` §2f) with our numbers, controls and the exit-0 discipline. Proposed: a dedicated subcycle **1.5.1b** after 1.5.1 closes and before 1.5.2, one commit per defect under a full harness, **measured before it is touched so the fix is a number**, `big_fixed_array_cost.npk` as the regression case. Cause not yet confirmed and deliberately not guessed. **The schedule is the author's call.** That session messages us when 1.5.1b opens and again with the re-pin commit |
| **O-N14** (no library object: `@npk_failsafe` called, never declared) · **O-N13** (a `pub use` silently downgraded) | **O-N14 blocks** per-module objects and separate compilation as `BUILD_REFERENCE` §4.1 documents them, **for every library here**; inconveniences 0.0.2's harness and one symbol scan. **O-N13 blocks nothing** but costs each person who meets it, and six umbrella modules are planned | **BOTH ACCEPTED 2026-09-04 and taken into 1.5.1b as step 3c**, after 3b. Verified on the compiler under test there: a non-root module carries seven `call i32 @npk_failsafe(...)` and no `declare`, and the root defines it — **so the fix is the one this workbench proposed: a unit that does not define it declares it.** Better than the ask, step 3c also adds an **`object` stage to both runners** whose units are non-root modules compiled to objects that `llc` must accept, **including a comment-only one — our `core` shape** — so §4.1's model is *measured on every run* instead of documented. O-N13's fix upgrades the prior binding's visibility when a repeated import carries `pub`, so the two orders mean the same thing, with a positive resolve unit shaped on our §E2/§E3 contrast |
| **O-N11** (`main` without `failsafe` compiles at exit 0; the arm contract is discharged by deleting the handler) | **nobody — W-27: blocks nothing here.** Every program this library ships has a handler, and `llc` catches a missing one in the next step of the same recipe. It **inconveniences** cycle 0.0.3's harness, which must stop reading `npkc` exit 0 as "well-formed" and gains an eighth selfcheck case. It does **not** touch the arm contract where a handler exists | **ACCEPTED 2026-09-03 as the compiler's DEF-5, committed at step 1b, harness running from 22:11. The diagnostic is `NITPICK-REACH-003` at `main`, listing every identity the handler owes** — **the count is NOT six.** This board carried six from the compiler session's message; `case1` has no import, no arithmetic and no allocation, so its bill is S-4b's floor of **four** — `Unreachable`, `HeapOom`, `HeapBadRequest`, `WildLeak`. Under verification, and deliberately written into no repository document: the worker recorded the diagnostic's shape and left the numbers to the re-pin, which is right for a number nothing yet depends on. That is the after-value our two transcripts must record at the re-pin., at our `b092a9e`, and taken into 1.5.1b immediately after step 1 (D-248), whose whole-graph pass over the root's declarations this is the missing question of. **The ask was granted in full:** the refusal lands at `main` and the diagnostic LISTS the identities the absent handler would owe. A root with neither `main` nor `failsafe` stays legal; a `failsafe` outside the root is refused by step 1. **Exposure measured across all six repositories: three files, every one a negative probe, no live code** — `nitpick-time`'s two DEF-5 reproductions, whose transcripts must be re-recorded at the re-pin (an `npkc` refusal replaces today's `llc` failure), and `nitpick-posix`'s `probe02g`, already refused at `MACRO-007`. Independently verified before it was sent. `npkc` accepts a root file with `main` and no `failsafe` at exit 0, emitting IR whose trap paths call an undefined `@npk_failsafe`; only `llc` refuses it, against the compiler's own D-013. **The quiet half is the serious one:** `reach_settle` returns early at `failsafe_decl == 0`, so the whole REACH-002 contract is enforced against programs that HAVE a handler and asked of nothing that has none — the same shape as O-N10, where the silent half mattered more than the refusal. The ask includes the diagnostic naming the arms the absent handler would owe, which `reach_settle` has just computed at the line where it returns early |
| **O-N10** (`derive` on a payload enum: refused, or silently tag-only) | nobody yet — `nitpick-time` exposes one payload enum and no rule needs a derive on it. **Blocks the first library that wants one** | **ACCEPTED as DEF-4, then WIDENED after measurement: ratified as D-250, step 3b.** It is not only payload enums — a derived `Eq`/`Ord` over a **struct with a derived-struct field** fails the same way inside `<derived-1>`, so step 3b covers named types in structs and enums alike, and an owning payload will refuse the derive **by name** rather than silently generate. **RAISED 2026-09-03, and ACCEPTED as the compiler's DEF-4** at our commit `eb8d6b4`, with a step proposed in 1.5.1b awaiting the author's ratification; it does **not** displace the DEF-2 → DEF-3 → DEF-1 order, so all four of this workbench's defects may land in one batch. `#[derive(Eq)]` is `NITPICK-TYPE-034`; `#[derive(Ord)]` compiles and reports `Literal(7)` equal to `Literal(9)`. The quiet half is the serious one. No file in the compiler's tree derives on a payload enum, so the gap is coverage; the ask includes a test there. Not blocking, so no author decision is pending |
| **O-N9** (D-004's escape rule unenforced for slice views) | `nitpick-time` in principle — every `src/fmt/` parser takes a `uint8[]` — and **BLOCKING by the author's ruling** — `src/fmt/` work and probes 09/10 wait for the compiler; the house rule "a view is a parameter, never a return value" is kept as a belt, not as the guarantee | **RAISED 2026-09-03.** `string_bytes(local)` returns a view that outlives its owner at exit 0 and reads freed memory; `@`-borrows in the same position are refused, so the rule is documented and under-enforced for one type. **Q-8: the author ruled it BLOCKING.** Accepted by the compiler as **DEF-3**, second of 1.5.1b's five commits — the borrow walk learns that a view-maker's result borrows its operand. The analyses currently name neither `string_bytes` nor `string_from_bytes`; the only view they know is the range-view `arr[lo...hi]`. **Two shapes DEF-3 distinguishes that our own six cases did not, and `src/fmt/` planning turns on them:** a view of a **temporary** — `string_bytes(string_concat(a, b))` returned — is refused outright as **`NITPICK-BORROW-012`** — **real, but NOT in the pinned toolchain**: DEF-3's step 2 allocates it and it lives only in the compiler's unlanded step-2 worktree, so grepping `950bb1d` for it finds nothing. This board briefly said the code did not exist, on exactly that grep; the pin proves "not landed", never "not real" (`PLAYBOOK.md` §6). **Why it needed a new code at all, which the plan had not known:** DEF-3's other refusals are all shaped like "as if `@` had been written at that argument" and are `BORROW-001`/`002`, but `@` of a temporary cannot be spelled, so no existing code's text is true of it and tracking it would need a root with no name — bind the intermediate first, after which the view is an ordinary borrow of that binding (and note it is doubly wrong today, since the `string_concat` temporary also leaks under D-246); but a view whose root is a **pointer-shaped binding** (a wild pointer, a slice, a cstring) is the *pointee's* borrow rather than a frame borrow — **and note which rule is which: TODAY's live mechanism is `borrows_only_param_rooted` (`escape.npk:507`), rooted at a PARAMETER, so "views are never returned" is already stricter than the language before DEF-3 lands; the pointer-shaped-root formulation is what DEF-3 introduces**, so `string_from_bytes(buf, n)` over an alloc'd block, returned, **stays legal**. So `nitpick-time`'s house rule "a view is a parameter, never a return value" is CONSERVATIVE, not the truth: it was written with no way to tell those apart. **Three further refinements from step 2's first whole-tree sweep, which found eight sites and refined the rule three times:** a view over `#ptr_add` **looks through to the pointer**; a `for` over a range **cannot carry a borrow whatever its bound reads**; and a struct literal is **rooted where its field values are**. The rooting checks now share one walk with the classifier. All three bear on `src/fmt/` and none is in our six cases |
| **O-N8** (`mod:`/basename mismatch merges two files) | nobody — raised for correctness | **ACCEPTED 2026-09-03** as the compiler's **DEF-2**, same §2f, same owner and same 1.5.1b slot. Emits two `define i32 @main` at exit 0 and `llc` refuses the IR; the `NITPICK-RESOLVE-005` diagnostic for the same rule already exists and simply is not applied here. Costs `ntime` nothing |

---

## Ready to start now

Independent of everything, roughly a day each, and each converts an unknown
into a fact (W-14):

- [x] `nitpick-posix` 0.0.0 **probe 02** — gated a fourteen-cycle repository; ran 2026-09-03, negative, absorbed
- [ ] `nitpick-regex` 0.0.0 probes
- [~] `nitpick-time` 0.0.0 probes — **nine worked, two held; four stops (~~O-N4~~ **discharged and verified here 2026-09-04**; O-N9, O-N10, O-N11 landed at the pin, not yet measured here).** 01–08 accepted with twins and verified PASS at `9113487`; **11 worked** — six programs, three defect cases and a support-module control — and produced the fourth stop; **09 and 10 held for 1.5.1b** by the author's ruling on O-N9, so the subcycle cannot close until the re-pin
- [ ] `nitpick-sockets` 0.0.0 probes
- [ ] `nitpick-parse` 0.0.0 probes
- [ ] `nitpick-tui` 0.0.0 probes
