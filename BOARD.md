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
**Workbench writer:** `08f94e4a-85df-4b03-ac4a-bfd9e5cd07a1`, session `nitpick-libs_s4`, taken 2026-09-06 13:24 — **the ninth session to hold this lock and THE FIRST TO HOLD IT AS A LISTENER RATHER THAN AN ORCHESTRATOR.** *(This line first, then the marker, then pushed, then re-read from `origin/main` AS A VALUE — hazard 5. Read it as a value and never by grepping for a uuid: the releaser's id legitimately appears on this line too, which briefly convinced the eighth orchestrator that its own release had failed.)* **THE LOCK IS HELD ONLY TO LOG, AND IT WILL BE RELEASED WITHOUT ANYTHING HAVING BEEN BUILT.** **AND THIS SEAT IS CLOSED AT THE HANDOFF, NOT KEPT AS A SPARE — the author, 2026-09-06 13:50: he will hand to `s5` to resume the libraries and *"at which time i will close the s4 session and start an s7 session in that terminal that will be your successor when the time comes."* **The consequence is operational, not sentimental: the brief this session gives `s5` is its LAST ACT, and there is no asking it anything afterwards.** So everything a successor could need must be on this board or in that brief before the handoff begins — which is why the 0.1 planning gap below is written here and not only spoken.** The first write under it is a correction found by *reading* the board rather than by working it (`:1384`, the kept-pin count) plus the first quiet-period compiler entry — which is what this seat is for. **IF THIS SESSION IS GONE, TAKE THIS LOCK FREELY AND WITHOUT INVESTIGATING: NOTHING IS IN FLIGHT, NO CLAIM IS OPEN, NO AGENT IS LIVE, AND NO WORK IS OWED.** A held lock's failure mode is a **stale** one, and a stale lock normally raises the question *"is someone mid-write?"* — here the answer is permanently no, because this seat only ever logs. **§4 Recovery is written for stale CLAIMS; a watch-lock is a shape it does not cover**, so the condition is stated here rather than left for a successor to infer, which turns the worst case from a mystery into a two-second decision. *(Previously: `none` — released 2026-09-06 by `647e6588-8236-4fcc-91a1-0223d220639f`, session `nitpick-libs_s3`, the **eighth** orchestrator, for a briefed handoff to this session; marker removed first, then the line, then pushed, then re-read.)* **`nitpick-libs_s4` IS NOT AN IDLE ORCHESTRATOR WAITING TO DISPATCH. Its instructions from the author are: stand down, listen for updates from the compiler sessions, LOG THEM HERE, and start no implementation.** The reason is on the pause block above and it is not impatience: **by the time this workbench resumes, the compiler will have moved and any implementation done in the meantime may have to be redone.** So a compiler notice arriving during the quiet period is **recorded, not acted on** — a re-pin is not taken, a claim is not opened, and a defect report is filed for later rather than worked. **A successor that reads a landing notice as a call to dispatch has misread this line.** *(Previously: taken 04:1x on a briefed handoff from `nitpick-libs_s2`.)* *(Freedom established on **three** independent readings before the write, none of them inference: this line read `none` **both locally and on `origin/main`**, which are the same commit `15969bf`, and `git show 15969bf -- BOARD.md` was read so the take is from a state actually seen rather than one assumed — `nitpick-libs_s4` suggested that check and it confirmed the release is genuine; `.internal/` held **only** `toolchain/`, no marker, which hazard 1 says to check because the guard's silence is not evidence; and **both** libs peers answered from commands — `nitpick-libs_s2` returned a verbatim `git status` with "`15969bf` is my last write, everything from here is messages only", and `nitpick-libs_s4` returned "idle, nothing written, nothing queued", volunteering that its whole transcript holds no write and undertaking to message this session before it ever writes here. Hazards 3 and 4 both paid again.)* **My own eight-tree sweep, discovered with `find` and not listed, agrees: 8 trees, all `dirty=0`, all `ahead/behind=0/0`.** **Nothing is in flight; no agent is live; ALL EIGHT TREES ARE CLEAN AND LEVEL** — `nitpick-time` included, now that 0.1.0 is pushed. **THE RE-PIN IS DONE: the pin is `3d15ac9`**, commissioned, both §3 guards clear on the first attempt, digests matched the compiler's notice rather than taken from it, `npkrt.o` `cmp`-verified unchanged, and **the canary's FLAT prediction held** — 50 482 B / 14 `define`s at both `aaffb87` and `3d15ac9`. **`nitpick-time` 0.1.0 is DONE, VERIFIED PASS, PUSHED, and CI-GREEN** at `2589069` (run `34020573741`), so it is confirmed on a second machine with a differently-built compiler. **`nitpick-regex`'s TWO-DAY RED IS NOW DIAGNOSED, REPRODUCED AND BOUNDED — see THE CI PIN MAP below, which has been rewritten.** It was settled by running the harness at `91657eb` against **three kept pins on this machine**, which is what `.internal/toolchain/` is for; the CI log itself is unrecoverable (**HTTP 404, not an empty log** — GitHub has expired it, so no re-read will ever produce one). **The stale pin IS the cause and the diagnosis also refutes the fix that was recommended for it.** **Then: the claim stands at 0.1.1, which has NO subcycle file** — the first decision needed. **Two things are owed and neither is started:** the **re-founded spread** for the compiler side (specified in full below) and **0.1.1's plan**. **The compiler side is now `nitpick-compiler_s1`; `_s0` has stood down.** Marker removed first, then this line. **To take it: this line first, then the marker — AND PUSH.** **Six hazards, each measured rather than inferred; the third was found at the 13:37 handover, the fourth and fifth at the sixth orchestrator's, and the sixth at this one.** (1) The guard permits **any** session while this line reads `none`, so §2.1's refusal never fires and **its absence is not evidence the lock is free** — verify `.internal/` too. (2) **`CLAUDE_SESSION_ID` is EMPTY in a Bash tool call**, so §2.1's marker command writes a 0-byte file; take your id from the `~/.claude/projects/<slug>/<uuid>.jsonl` path, cross-check it against your scratchpad path, and expect **37 bytes**. (3) **A free lock is not the same as a clean tree.** At the 13:37 handover the incoming session asked the outgoing one *"are you done writing?"* instead of reading the `none` and taking it; the outgoing session nearly answered from memory, ran `git status`, and found an **uncommitted deletion it had not made** — the author had moved a tracked file out from under it. Committing on the "lock is free" reading would have swept another session's deletion into this one's commit. **During any handover overlap, ask the outgoing session directly and have it answer from `git status`, not from memory.** **Done again at this handover, and it paid again:** `nitpick-libs_s0` answered from `git status` — all seven trees `dirty=0`, `ahead/behind=0/0` *(seven was the set every session then swept; it is eight — hazard 6)* — and volunteered that its remaining actions are **messages only**, which a tree read cannot tell you. **Asked and answered a third time at the seventh orchestrator's takeover, and it paid a third time:** `nitpick-libs_s1` answered from `git status` and volunteered *"messages only, I have made my last write"*, which is what released this lock. (4) **A `nitpick-libs_sN` PEER YOU WERE NEVER TOLD ABOUT WILL APPEAR, AND ONE MESSAGE SETTLES IT.** At this takeover `ListAgents` showed **`nitpick-libs_s2`, idle, opened within a minute of this session**, while the handoff brief, the record and this board's own roster named only `s0` and `s1`. Orchestrate §2.1 says to stop and ask the author; **asking the peer itself is faster, cheaper and more certain** — it replied *idle, no task, nothing written, and I will message you before I write*, converting a guess into a fact in one message. That is the move the fourth orchestrator recommended for the unidentified `nitpick-e3` and did not take, leaving it open for two days. **The author's practice, confirmed by him at this handover, is a ROLLING POOL:** he pre-opens the next generation, and closes a spent session so it can return as the generation after next — `s0` closes here and comes back as `s3`, succeeding `s2`. **So a higher-numbered libs peer is normally your own parked successor, not a rival writer — but ask it anyway**, because the alternative is inference, which is exactly what two earlier orchestrators rightly refused to rest this lock on. (5) **TAKING THE LOCK IS NOT DONE UNTIL IT IS PUSHED.** The sixth orchestrator committed the writer line and did not push it, so `origin/main` went on advertising `none` while the lock was held locally — caught by the outgoing session, not by any check. **The tell was that `git status` had been run BEFORE the commit and not after**: the verification ran on the wrong side of the write. A peer reading `origin` sees a free lock; a peer reading the local tree sees a held one. **Push, then re-read the line from `origin/main` to confirm it names you.** **AND THE RE-READ IS A VALUE-READ, WITH A LITERAL COMMAND, BECAUSE "read it as a value" LEAVES A TIRED SESSION REACHING FOR `grep`:** `git show origin/main:BOARD.md | sed -n '14p' | sed -n 's/^\*\*Workbench writer:\*\* `\([^`]*\)`.*/\1/p'` — it prints the field and nothing else, so `none` and a uuid are distinguishable at a glance. **Grepping this line for your own uuid does not work and has already failed once:** the releaser's id also appears here, so the eighth orchestrator's grep matched its own release and briefly convinced it the take had failed. **It wrote this hazard and then failed it within the hour** — a hazard that names the trap without naming the command is half a hazard. (6) **THE SWEEP THAT CLEARS THE LOCK COUNTED SEVEN TREES AND THERE ARE EIGHT, AND NO SESSION EVER STATED WHICH SET IT MEANT.** Found at this handover by the incoming session, conceded by the outgoing one: *"it is EIGHT, and `nitpick-apps` has never been in the loop that checks."* **Three different sets are in live use in this repository and all three are correct under their own denominator** — **six repositories** (the five libraries + `nitpick-posix`) is the *work* set and every "all six repositories" claim on this board and in the record is sound; **seven trees** is that six plus this workbench; **eight** is that seven plus **`nitpick-apps` itself**, a tracked repository holding `APPS.md`, `PLAYBOOK.md`, `README.md` and `LICENSE`, which orchestrate §2.2 already puts in the startup *read* set and `CLAUDE.md` already covers under *"a library **or application** repository"*. **It is not a decision to exclude it; it is that every session inherited the same seven-item list.** The tree was clean at this handover, so nothing was lost — **and nothing would have told us if it had not been**, which is the finding. **Discover the set, never list it:** `find . ../nitpick-apps -maxdepth 3 -name .git` and **print the count with the verdict**, so an unstated denominator cannot survive a handover. The durable half is in `PLAYBOOK.md` §7: *a repository that holds only documents is still a repository, and a loop assembled by listing rather than by discovery will miss exactly the one nobody thinks of as code.* **AND A DEPTH-BOUNDED `find` IS STILL A LISTING — JUST AN IMPLICIT ONE.
Added 2026-09-06 14:10 by `nitpick-libs_s6`, which re-ran a sweep as a discovery after
being caught listing, and the discovery MISSED THE SAME REPOSITORY.** `find . ..
-maxdepth 3 -name OPEN_QUESTIONS.md` looks like it obeys this rule and does not: the
live application questions sit at `../nitpick-apps/nitpick-posix/meta/`, **depth 4
from `..`**, so the bound excludes them. **Verified here, and it fails twice over —
that command returns seven paths, misses `nitpick-posix` entirely, and DOUBLE-COUNTS
this workbench**, because `./meta/OPEN_QUESTIONS.md` and `../nitpick-libs/meta/OPEN_QUESTIONS.md`
are the same file reached two ways; a naive count of its output says seven when the
answer is six. **⚠ THE COMMAND PRESCRIBED ABOVE IS CORRECT AND MUST NOT BE "FIXED":**
`find . ../nitpick-apps -maxdepth 3 -name .git` finds all eight **because it roots at
`../nitpick-apps` explicitly**, not because it uses `find`. **The lesson is that the
rooting carries the correctness, so re-root a working sweep at `..` for tidiness and
it silently loses the application repository.** *Discovery is not established by
reaching for `find`; it is established by asserting the count and naming what the
denominator is.* (7) **THE LOCK IS A MUTEX OVER ONE SHARED DIRECTORY, NOT BOOKKEEPING ABOUT WHO IS AUTHORITATIVE ACROSS CLONES — AND THAT IS A STRONGER REASON TO HOLD IT THAN ANY SCHEDULE ARGUMENT.** Every `nitpick-libs_sN` session works **the same checkout**. Measured, not assumed: `git reflog` here shows `commit:` entries from four different orchestrator sessions interleaved in one log — `e364dce` and `36b6d8f` (the ninth), `92b279e` and `25a6de1` (the eighth), and earlier ones before them — and a sweep of `~/Workspace` finds **exactly one** clone pointed at `alternative-intelligence-cp/nitpick-libs`. The eighth orchestrator found this from the other side: it saw its own `HEAD` at a commit it had not made and briefly wondered how it had moved without a pull. **It had not moved; the ninth session moved it, because there is one set of files.** So `none` on this line does not merely invite a successor to *resume the work* — **it permits any other libs session to write into the very files you are editing.** A session holding this lock while deliberately doing nothing is therefore not being tidy, it is holding a mutex, and releasing it "because nothing is happening" is the mistake. **AND THERE IS A CHEAPER DEMONSTRATION THAN THE REFLOG, CONTRIBUTED BY A SESSION THAT NEVER TOUCHED THE TREE.** `nitpick-libs_s6` opened at 2026-09-06 13:39 while this session had `BOARD.md` modified mid-edit. **Its automatic session-start git snapshot recorded `M BOARD.md` with `HEAD` at `a49229c`; minutes later the same directory read clean at `5082518`.** It issued nothing that could have done that — **this session committed and pushed underneath it.** Corroborated from this side rather than taken on report: `a49229c` is 13:32:30 and `5082518` is 13:35:19, consecutive commits of this session, with `BOARD.md` modified-in-tree between them. **So the shared checkout is not merely inferable from a reflog — it is observable, passively, by an IDLE session watching its own view of the repository change.** Reach for that demonstration first: it needs no archaeology, and a session that has run nothing cannot be told it moved its own HEAD. (8) **`nitpick-posix` CANNOT BE RESOLVED BY NAME, AND THE CHECK THAT WOULD NORMALLY
SETTLE IT RETURNS THE SAME ANSWER FOR THE WRONG TREE.** Found 2026-09-06 14:10 by
`nitpick-libs_s6` when a probe did `find … -name nitpick-posix | head -1` and silently
got the archived copy. **Three directories carry that name, and measured here rather
than taken on report, TWO OF THEM REPORT THE IDENTICAL `origin`:**

```
REPOS/nitpick-apps/nitpick-posix       …/nitpick-posix.git   <-- LIVE, the work tree
REPOS/ARCHIVE/nitpick-posix            …/nitpick-posix.git   <-- prior art, read-only
REPOS/ailp-website/apps/nitpick-posix  …/ailp-website.git    <-- different remote
```

**So `git remote get-url origin` — the natural provenance check — CANNOT TELL THE
LIVE TREE FROM THE ARCHIVED ONE.** That is what makes this worse than an ordinary
ambiguity: a sweep that resolves the repository by name can read archived prior art,
report it as live state, and **have every provenance check it runs come back clean**.
**Only the PATH distinguishes them.** So anchor on `nitpick-apps/nitpick-posix`
explicitly, treat a bare `-name nitpick-posix` match as **unresolved** until its parent
directory has been read, and never let `ARCHIVE/` into a live denominator — it is
read-only prior art by design. (9) **THE OPPOSITE OF HAZARD 8, AND THE QUIETER ONE: THE SAME FILE REACHED BY TWO
PATHS, WHICH `sort -u` DOES NOT COLLAPSE.** Found 2026-09-06 14:13 by `nitpick-libs_s6`;
verified here by inode. **Keep these two apart — they are different failure modes with
different fixes.** Hazard 8 is *different files, one name*, fixed by reading the parent
directory. This is *one file, different names*, fixed only by resolving **identity**:

```
50481537  ./meta/OPEN_QUESTIONS.md
50481537  ../nitpick-libs/meta/OPEN_QUESTIONS.md
```

**`sort -u` over those two lines returns two lines.** The strings differ, so a
path-deduplicated sweep still counts the file twice **and still looks deduplicated** —
which is what makes this the more dangerous of the pair. A name collision eventually
looks wrong to a reader; **a re-reached file produces a plausible number with no
visible anomaly at all**, and if it cancels against a missing member the total can even
come out right. `find . .. -maxdepth 3 -name OPEN_QUESTIONS.md` does exactly that: seven
paths, `nitpick-posix` missing, this workbench counted twice.

**Dedupe on inode, and root only on the live areas:**

```
find . ../nitpick-apps -maxdepth 4 -name OPEN_QUESTIONS.md | grep -v '/\.git/' \
  | xargs -r stat -c '%i %n' | sort -u -k1,1        # -> 7: workbench, 5 libraries, posix
```

**⚠ THE `..` ROOT WAS DROPPED DELIBERATELY AND MUST NOT BE ADDED BACK FOR TIDINESS.**
Rooting at `..` with `-maxdepth 4` reaches `ARCHIVE/`, and the only reason it does not
currently pull prior art into the count is that `ARCHIVE/nitpick-posix` happens to hold
no `meta/OPEN_QUESTIONS.md`. **That is safety by coincidence of the archive's present
contents, not by construction** — `ARCHIVE/` holds 121 entries including
`nitpick-posix`, `nparse`, `nregx`, `ntime` and `nsocket`, so one archived file with
that name at that depth silently admits read-only prior art to a live denominator, with
hazard 8 guaranteeing the provenance check comes back clean. Rooting on `.` and
`../nitpick-apps` makes the exclusion structural.

**AND DO NOT SWEEP THIS WORKBENCH AS A PEER OF THE LIBRARIES.** Its own
`meta/OPEN_QUESTIONS.md` carries library ids — an occurrence-based sweep reads them as
an eighth allocator inventing that many colliding ids, when they are **registry entries
citing library questions and naming the repository**, which is the mechanism working.
The allocation-versus-citation distinction is what keeps that out of the count.
(11) **⚠ `../nitpick/build/` IS A STALE LOCAL ARTIFACT AND MUST NEVER BE USED TO CHECK A
LADDER DIGEST. IT LOOKS EXACTLY LIKE THE AUTHORITATIVE THING AND IS NOT.** Found 2026-09-17 03:54
on a resume sweep, one command short of filing a false defect against the compiler side.
**Our read-only checkout's `build/npkrt.o` read `27387ce7…` / 55 768 B — the 1.5.4e anchor —
while the compiler correctly reported `d8a51b42…` / 59 192 B.** Every instinct says the local
object is the fact and the notice is the claim. **It is the other way round.**

```
build/ in the compiler repo    GITIGNORED (.gitignore:3), 0 tracked files
git show b7d60dc:build/npkrt.o the path does not exist in the commit at all
our build/npkrt.o mtime        2026-09-11 10:32  -- BEFORE step 4 (c5eb8c1, 21:19)
                                                    and before b7d60dc (09-12 00:20)
```

**So it reflects whenever someone last ran a build in that tree, which can be arbitrarily far
behind the checked-out commit.** *A session that "verified" a notice against it would get a
confident FALSE NEGATIVE — concluding the compiler was misreporting its own anchor — which is
worse than no check, because it would be reported.*

**THE RULE: a ladder digest is checked against the notice's internal consistency and THIS
BOARD's recorded history, never against `../nitpick/build/`.** **The distinction that makes
the compiler tree usable at all:** its **TRACKED files at a verified commit are
authoritative** — `runtime/npkrt.spec`, `meta/specs/TCB.md`, `runtime/models/`,
`runtime/npkrt.obligations` have all been read that way this cycle and every reading held.
**Gitignored build outputs are not.** *Same family as hazards 8 and 9 and the
`find`-versus-`git ls-files` correction: an artifact that looks authoritative, answers
confidently, and is measuring something else.* One writer here (W-16, P-19).
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
| `nitpick-libs_s3` | — | the **eighth** orchestrator. **CLOSED 2026-09-06 13:39** — released the lock cleanly, briefed this session over a long but deliberately bounded overlap, and its socket is now gone. Most of the hazard list on the writer line is its work, including the four traps it recorded against itself |
| `nitpick-libs_s4` | — | **THIS WORKBENCH'S CURRENT WRITER — and a LISTENER, not the ninth orchestrator.** Holds the lock only to log compiler notices and will not dispatch. Found the `:1384` kept-pin count trap by reading the board it inherited, and closed the compiler-address gap by asking rather than inferring |
| `nitpick-libs_s5` | — | **THE SUCCESSOR. HAND OFF TO THIS ONE, NOT TO A HIGHER NUMBER.** Parked and unbriefed, opened 04:1x in the terminal `s2` was closed from; alive and idle at 2026-09-06 13:39, 9 h old. **Re-confirmed by `nitpick-libs_s6`, which declined the seat and pointed back at this row** rather than accepting a handoff that was not its to take |
| `nitpick-libs_s6` | — | the spare **behind** the spare, opened 2026-09-06 13:39 as `s3` closed. **Parked: no task, nothing written, nothing queued** — asked and answered about itself, its user's only instruction so far being a `/rename`. Undertook to message before it ever writes. **Re-verified this board's writer line with the documented value-read, the single-clone sweep and `HEAD == origin/main` rather than taking them on report**, and contributed hazard 7's passive demonstration |
| `nitpick-compiler_s0` | `nitpick-bc` | the original compiler session. **GONE** — confirmed by `_s2` 2026-09-06 13:34 and by its absence from `ListAgents`; it ran 1.5.2g step 1 in worktree `g1` this morning. *(This row previously read "stood down from the role, still alive".)* |
| `nitpick-compiler_s1` | `nitpick-e3` | **THE COMPILER ADDRESS UNTIL 2026-09-06 16:16, NOW HANDING OFF TO `_s2`.** Goes quiet once `_s2` confirms; **a message sent there after that will not be read.** Landed 1.5.3. Made two falsifiable predictions that held, took a wording correction without defensiveness, and sent three unasked-for corrections of which the last refuted this board's own `failsafe` reading |
| `nitpick-compiler_s2` | — | the compiler address 2026-09-06 → 09-07. **Ran OUT OF QUOTA before it could name a successor**, announcing only *"the resumed session"* — the gap hazard 10 exists for |
| `nitpick-compiler_s3` | — | landed 1.5.4c. **Arrived as an address this board had never verified, and was AUTHENTICATED BY CONTENT under hazard 10** — its three *unchanged* digests and the canary matched our own recorded values exactly. **Named `_s4` explicitly, closing the gap** |
| `nitpick-compiler_s4` | — | the compiler address through 1.5.4d, 1.5.4b and 1.5.4e. **Answered the `(ShiftRange)` question with the mechanism rather than the verdict, and PRE-AGREED the anchor-move protocol unasked — then used it correctly on its first outing.** Handed to `_s5` at `cb8cbb0` |
| `nitpick-compiler_s5` | — | landed 1.5.5. **Corrected its own 368/439 label slip on being queried, and named a GAP IN OUR TYPE-071 METHOD rather than agreeing with our result.** Handed to `_s6` at `149dbf6` |
| `nitpick-compiler_s6` | — | landed 1.5.6 entire. **Corrected itself four times unprompted**, pre-agreed nothing but honoured the anchor protocol on four floor moves, and **withdrew a specified task when shown its premise was wrong.** Handed to `_s7` at `b7d60dc` 2026-09-17 03:54 |
| `nitpick-compiler_s7` | — | **THE COMPILER ADDRESS FROM 2026-09-17 03:54 — announced by `_s6` at `b7d60dc`.** Holds our six items **quoted verbatim with procedures attached**, the standing obligation on language-level changes, and the 1.6 answer with its caveat so it repeats rather than re-derives it. **First notice still gets the ladder check against `d8a51b42…`** |
| `nitpick-compiler_s8` | — | open behind `_s7` as its eventual successor. **Not an address**; we are told from the address the rotation happens from |
| `nitpick-compiler_s7` | — | idle behind `_s6`. **Not an address** |
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

### ⚠ `c18fa78` LANDED — 1.5.6b step 4. **F2 IS FACT: A NEW REFUSAL IN OUR CLASS IS NOW ENFORCED (D-294).** Notice 2026-09-17 12:06 from `nitpick-compiler_s7`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`. ANCHOR STAYS `b72d7774…` / 59 352 B.**

**`NITPICK-RESOLVE-001` at a module-level `func:` — plain, `pub`, `async` or `thread`, inside an inline
module or out — WHOSE NAME IS A BARE BUILTIN'S, and at an `extern` block's METHOD of such a name**
(its generated stub is a module-level function, D-190; reported once, at the method's own
declaration). **Trait and impl methods exempt.** Name table: `is_builtin_name`, **57 names**.

**✅ Verified as ENFORCED ON MAIN, not taken from the notice:** `c18fa78` is on the wire;
`owned_builtin_name` is present in the loader at `c18fa78`; the rejection test
`tests/modules/rejection/owned_builtin_names.npk` exists; the table holds 57. **The three "was" values
are this board's and the loop-computed deltas are exact** (`npkc.ll` +11 430, `npkc.o` +4 504, `npkc`
+3 832). **Same shape as F3 — the compiler moved, the floor did not.**

## ✅ THE STANDING RESERVED-NAME CHECK, NOW AGAINST AN ENFORCED REFUSAL RATHER THAN A FORECAST

```
enforced reserved names at c18fa78                       57
module-level func: declarations, tracked library code   532
EXACT-name collisions -- what D-294 actually refuses       0
```

**Zero. Our libraries' function names pass D-294 as it is now enforced.** *The check matches EXACT names by
set membership, which is D-294's own semantics: one of their six ACCEPTED shapes is "a name that merely
contains one", so `read_all` passes where `read` fails. A substring match would have flagged false
positives. (No library name even contains a built-in name of four or more characters, so that side check
had nothing to find — the decisive figure is the zero exact collisions.)*

**✅ THE SHADOWING WINDOW RECORDED LAST NOTICE HAS CLOSED, EXACTLY ONE LANDING WIDE.** At `9955d23`,
`hardware_concurrency` had become a builtin while D-294's refusal had not yet landed, so for that one
landing a same-named library function would have **silently shadowed** the builtin rather than been
refused. **D-294 is now enforced, so that window is shut** — it cost us nothing, since we held no such
function, and it closed on the landing this board said it would.

**✅ A PROPERTY WORTH HAVING STATED: THIS IS REFUSAL-ONLY.** *"No program that compiled before emits
differently."* **The emission moved because the compiler's OWN source changed — the new check — not
because any valid program's output changed.** *A pure refusal can only turn a previously-accepted program
into a rejected one; it cannot alter what an accepted program compiles to. So for a library whose names
pass, D-294 is invisible at the emission level.*

**THE TEST IS CONSTRUCTED THE RIGHT WAY — REFUSALS AND ACCEPTANCES IN ONE FILE:** six refusals (a plain, a
`pub`, an `async` and a `thread` function, one inside an inline module named `hardware_concurrency`, and an
`extern` method named `read`) **and six accepted shapes beside them** — a trait method, an impl method,
**a field** (the exemption this board raised for F4), a parameter, a local, and a name that merely contains
one. *A refusal tested only on what it refuses cannot show it does not over-reach; the accepted shapes in
the same file are what pin the boundary.*

**The `verify` line is still the old one** (273 + 138 + 0 + 22 = 433 of 439) — **expected**; its fix is step
4d, being written now. **STILL FORECASTS:** **F4** (D-296, callable bindings named after builtins —
committed as `32e9f20` on its branch, under its full harness, **lands next**) and the DEF-54/55/56 fixes
after it (not refusals).

### ✅ `9955d23` LANDED — 1.5.6b step 3. **F3 IS FACT: `hardware_concurrency` IS A BUILTIN.** THE EMISSION MOVED; THE FLOOR DID NOT. Notice 2026-09-17 11:44 from `nitpick-compiler_s7`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`. ANCHOR STAYS `b72d7774…` / 59 352 B.**

**✅ Verified on the wire; the three "was" values are this board's; and the loop-computed deltas are
exact.** **This is the OPPOSITE shape to F1** — the compiler's own source changed, so the emission
moved and the floor did not:

```
npkrt.o    b72d7774...     59,352 B  unchanged   <- the anchor stands
builder.o  c489068f...  9,085,152 B  unchanged
builder    d1bfa940...  7,906,536 B  unchanged   (links the floor, which did not move)
npkc.ll    deeb7321... 24,826,171 B  MOVED +5873  (was 8bb03048…)  THE EMISSION, travels (D-265)
npkc.o     390d83ba...  9,801,088 B  MOVED +2064  (was 06c5650c…)
npkc       edc231ff...  8,539,456 B  MOVED +1680  (was fb6e9153…)
```

*Coherent on its face: adding a builtin changes the compiler and not the runtime floor, so the
emission and the compiler binary move while `builder` — which links the floor — does not. F1 moved
the floor and `builder` with it; F3 moves the compiler and leaves `builder` alone. **Between the two
landings, every row of the ladder has now been seen to move for a stated reason and stay still for
one.***

**✅ F3 — `hardware_concurrency() -> int64`, never fails, `effect`, 1 to 1024, asked at each call
(D-293).** *"A pool can size itself now."* **And its test is a planted-fault test:**
`tests/backend/programs/hwconc_builtin.npk` checks the answer against the truth computed from the raw
syscall over a zeroed mask, **also after 100 frames of one-bits are left where the floor's frame
lands — exit 0 on this floor, exit 20 on `b7d60dc`'s floor AT ITS FIRST CALL, in both legs.**
*The test fails on the DEF-52 floor and passes on the fixed one, which is the only kind of test that
proves a fix.*

**✅ THIS BOARD'S 56 → 57 RECONCILIATION HELD.** At `df21fd5` this board counted **56** names in
`is_builtin_name` against their stated 57 and reconciled it as *"56 on main + `hardware_concurrency`
landing with F3"*. **At `9955d23`, counted independently: 57, with `hardware_concurrency` present.**
*A reconciliation is itself a prediction, and this one came true on the commit it named.*

## ✅ THE STANDING RESERVED-NAME CHECK, RUN AS THE RULE REQUIRES ON A NOTICE THAT ADDS A NAME

```
live reserved builtin names at 9955d23                  57
module-level func: declarations    (D-294 surface)     532
function-typed bindings            (D-296 surface)       0
collisions with the live 57                              0
```

**Zero.** *Note the gap between landing and enforcement, which this board should not blur:
`hardware_concurrency` is a builtin NOW, but D-294's refusal lands NEXT (F2). In that window a library
function of that name would silently SHADOW the builtin rather than be refused. We have none, so the
window costs nothing — but it is the exact failure D-294 exists to close, and it is open for one
landing.*

## ✅ OUR 439/433 CATCH: CONFIRMED AN OVERSIGHT, AND THE ASSERTION WE SUGGESTED IS SCHEDULED

**Their words: *"YOUR CATCH ON THAT `verify` LINE IS RIGHT AND IT IS AN OVERSIGHT, not a design."*** The
stated 439 includes the 6 `checker` rows and the breakdown omits them. **Scheduled by name in 1.5.6b
step 4d: both runners print the `checker` category AND ASSERT THAT THE PARTS SUM TO THE TOTAL, so a
missing category is a red run.** *The line in this notice is still the old one — the commit was already
under its harness — and it still reads 273+138+0+22 = 433 against 439. That is expected, not a
regression: watch for the corrected line at step 4d.*

**FORECASTS:** **F2** (D-294 + extern methods) — harness in its last stage, **lands next.** **F4**
(D-296) — committed; they corrected themselves mid-sentence on its timing (*its harness starts when
launched, before F2 lands; it cannot LAND before F2*). **DEF-54, DEF-55, DEF-56** — three defects in the
function-typed corner, found writing F4's test — are fixed in their own step after F4: **DEF-55**
(`raw o.f(x)` over a `never fails` function-typed field refused while `raw (o.f)(x)` is accepted) and
**DEF-56** (a trait method with a function-typed parameter cannot be implemented — TYPE-014 on identical
signatures). **None is a new refusal; all three make something that should compile, compile** — the
opposite direction to our risk class, and vacuous here, since we hold no function-typed binding, field
or payload.

### ✅ `632d2a7` LANDED — 1.5.6b step 2, THE FLOOR'S PROTOCOL MODELS. Notice 2026-09-17 11:36 from `nitpick-compiler_s7`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`. ANCHOR STAYS `b72d7774…` / 59 352 B.**

**✅ Verified on the wire; all six rows unchanged; deltas computed by the loop.** **And the counts
block is now GENERATED from the manifests — verified here against the TRACKED manifests at
`632d2a7`, and it matches to the row:**

```
nitpick.obligations        368 rows over 197 symbols  -- 202 discharged, 138 open,
                                                         22 unencoded, 6 checker   <- matches
runtime/npkrt.obligations  379 rows over 87 symbols   -- 372 discharged, 7 budget  <- matches
```

**✅ The typed-summary fix works: the verdict words are the manifests' own, and "residue" is gone.**
*They also reconciled, unasked, the two figures that look like a disagreement: the manifest holds
368 DISTINCT rows (202 discharged); the harness decides 439 obligations (273 discharged) — the same
facts before and after de-duplication by hash.*

## ⚠ A NEW VARIANT: A GENERATED LINE THAT OMITS A CATEGORY, SO ITS PARTS DO NOT SUM TO ITS WHOLE

**The harness's own verify line, pasted verbatim from its log, reads:** *"439 obligation(s): 273
discharged, 138 open, 0 budget, 22 unencoded"*. **Checked:**

```
273 + 138 + 0 + 22  =  433        stated total 439        gap 6
nitpick.obligations `checker` rows at 632d2a7            =  6
```

**The breakdown omits `checker`, and the gap is exactly the manifest's 6 `checker` rows.** *This is
not the typed-summary shape — the line is generated and pasted verbatim, so nobody mistyped it. It
is its sibling: **a generator that leaves a category out**, so every listed number is true and they
still fail to add up to the total beside them. A reader checking the arithmetic trips on it exactly
as this board just did.*

***So the principle has a second half.*** **Generating a line removes TRANSCRIPTION error; it does
not remove OMISSION in the generator. The remedy for that is different: the generator asserts that
its parts sum to its total, so a category it forgets fails the run loudly instead of printing a
clean-looking breakdown that silently drops six rows.** *Raised with them as a possibility, not a
verdict — `checker` may be deliberately reported apart from "decided" obligations, in which case
the total should say 433 or the breakdown should name the 6.*

## ⭐ WHAT LANDED: A MODEL THAT PASSED EVERY CHECK WHILE MISSING REAL BEHAVIOUR

**The `park-unpark` model was read against `npk_park_sleep` case by case — and was MISSING REAL
BEHAVIOUR IN TWO PLACES:** its early-out **cleared the eventfd's readability where the code keeps
it**, and it had **NO STEP for the epoll wait returning with nothing** (timeout or `EINTR`). **Both
fixed; the model's reachable states went 263 → 358 — a 36% larger state space — and NO VERDICT
MOVED.**

***A model can pass every check it has while being wrong about the code, because it cannot reach a
bad state through a transition it does not contain.*** *The verdicts held over the fuller model —
good news — but they held over the thinner one too, which proved nothing about the two missing
transitions. This is the models' own hazard 6: a check whose scope silently excluded part of what it
covers, green throughout. **What found it was reading the model against the code case by case, not
running the model harder.***

**A SEVENTH model, `reactor-io`**, now covers the I/O wake path — one-shot registration, the deferred
`io_unwatch`, the kernel declining a watch: +3 rows, 3 controls, **19 controls in all.** **And every
model was read a second way by EXHAUSTIVE SEARCH (S-75): no bad state reachable in any of the seven,
and agreement with z3 wherever both speak.** *Two independent readings agreeing — the syscall-table
generators again, at the level of protocol models.*

## F4 — OUR FIELD-EXEMPTION POINT ADOPTED, AND ONE CONSEQUENCE WORTH CARRYING

**Adopted as put:** the implementation decides **by the binding's TYPE at the sites that type a
binding** — local, parameter, `for` binding, `pick` pattern binding — **and never by a spelling
pattern.** A struct field is none of those sites. **The rejection test carries the negative case: a
function-typed field named after a builtin (`func int64(int64) never fails:open`), declared and called
through its receiver, ACCEPTED in the same file that refuses the bindings.**

**⚠ AND THE EXEMPTION HAS AN EDGE, which they flagged for this board:** **a STRUCT PATTERN binds a
field BY NAME, so DESTRUCTURING that field — `(Ops{ open, k })` — IS REFUSED**, because the binding it
creates is a callable local named `open`. **Reach such a field through its receiver instead.** *The
field is exempt; pulling it out by name is not. Vacuous for us today — our libraries declare no
function-typed field at all, measured at F4 — and recorded so the first library that grows one does
not destructure it.*

**FORECASTS, unchanged:** F3 (D-293 `hardware_concurrency`), F2 (D-294 + extern methods), F4 (D-296).

### ⚠ FORECAST F4 — D-296: FUNCTION-TYPED LOCALS NAMED AFTER A BUILTIN ARE REFUSED. Notice 2026-09-17 11:28 from `nitpick-compiler_s7`. **NOTHING HAS LANDED. FILED AS A FORECAST.**

**This board asked for S-76 as a forecast with its code if it were ratified — it was, and it
arrived before a line of it was written.** The author: *"go with your recommendations on all
three."* **S-76 → D-296**, landing at **1.5.6b step 4b**, after steps 2, 3 (F3) and 4 (F2).

**THE RULE — `NITPICK-RESOLVE-001` at the binding** — a **parameter** (of a function or a method), a
**local**, a **`for` binding** or a **`pick` pattern binding** whose **TYPE is a function type** and
whose **NAME is a bare builtin name.** **Reason, measured on their side:** such a binding is called by
its bare name, so inside its scope the builtin is shadowed — a local
`func int64() never fails:path_exists = eight;` makes `raw path_exists()` answer **8**.
**NOT refused:** a binding of any *other* type named after a builtin (`int64:read`, `string:open` —
calling it is a loud type error, so the name is harmless); **a struct FIELD of function type**
(reached through its receiver, like a method); methods (D-294's exemption stands). **Spelling:** no
type aliases exist, so an annotated function-typed binding is always literally
`func RET(PARAMS)[ never fails]:name`; the un-annotated case is a `pick` binding over a function-typed
payload or field.

## ✅ ZERO EXPOSURE — AND THE ZERO IS VALIDATED BY A POSITIVE CONTROL, NOT ASSUMED

**A zero from a pattern never shown to find anything is worthless**, so both their pattern and a
broader one written here were run against **their** tree first, where the answer is known:

```
                                       compiler tree @ df21fd5    our 3 code repos (tracked)
tracked .npk files                            777 (they: 778)           170
their pattern   \bfunc\s+[^:;{}=]*?\)...       15 (they: 15)             0
broader pattern (allows ':' in parens)          15                       0
function-typed bindings named after a builtin    0 (they: 0)               0
builtin names at landing                              57 = 56 on main + hardware_concurrency
```

**Both patterns reproduce their 15 exactly, so both work — and both find ZERO in our libraries.**
*The broader pattern was written to test a suspected blind spot: theirs excludes `:` inside the
parentheses, so it could not match a function type with NAMED parameters. **It does not
materialise** — Nitpick function types use unnamed parameters (`func int32(int32)`), and the broader
pattern finds the identical 15. Tested rather than asserted either way.*

**⚠ AND THE CONTROL SHOWED SOMETHING ABOUT THEIR DENOMINATOR.** One of their 15 hits is
`tests/backend/programs/fn_field_call.npk:11` — **`struct:Ops = { func int32(int32):op; };`, a struct
FIELD, which D-296 explicitly EXEMPTS.** *So their "15 function-typed bindings" mixes the refused
shape with an exempt one, overcounting the refusable set. It changes no conclusion — a zero over a
superset is still a zero — but it matters to the IMPLEMENTATION: a pattern that matches fields cannot
be used as the definition of what to refuse. Told to them, because it bears on the work in hand.*

**✅ AND IT CLOSES THE `pick` CASE AND DEF-54 FOR US.** That same control hit proves the pattern catches
**struct-field spellings** — and our libraries have **zero** matches of any kind. **So our libraries
declare no function-typed binding, field or payload at all**, which makes both the un-annotated `pick`
case and DEF-54's shape **vacuous here, by measurement.**

**DEF-54, recorded for completeness:** CALLING a function value bound by a `pick` pattern
(`(Op.Run(f)) { raw f(); }`) passes the checker, and **the emitter writes a direct call to a symbol that
does not exist** (`@npk.prelude.f`), so `llc` rejects the module — **for any name, not only a
builtin's. So no library can have a WORKING program of that shape today.** Being fixed inside 1.5.6b.

## ⚠ THE PATH TO THE RESUME SIGNAL JUST GOT ONE SUBCYCLE LONGER

**A new subcycle, 1.5.6c, is inserted BEFORE 1.5.7** — ratified today, for **two over-strong
assumptions in the floor's spec: `npk_string_concat`'s and `npk_small_free`'s.** *Evidence only; the
floor's behaviour does not change; any floor byte that moves arrives with both digests first.* **The
remaining sequence is now: 1.5.6b steps 2, 3, 4, 4b → 1.5.6c → 1.5.7 → 1.5.8 → 1.6.** **S-75 also
ratified** (the floor's protocol models gain a second, exhaustive reading as a belt in both runners) —
no surface for us.

**⚠ `npk_small_free` AGAIN — and the direction matters for the 0.1 planning gap.** This is the symbol
the 0.1 gap's allocator constraint rests on. **An "over-strong assumption" being corrected makes the spec
claim LESS, not more** — so 1.5.6c is likely to make the small-block free path *more honestly unproven*,
not proven. *It does not lift the 0.1 constraint; if anything it confirms it.* Cross-referenced in the gap.

**✅ AND THE LABEL-SLIP ITEM IS STRUCTURALLY CLOSED:** *"the counts block of every notice is generated
from the manifests now (`notice_counts.py`), the manifests' own words, pasted verbatim like the
ladder."* **The one typed line is gone.** Seventh fix of the typed-summary shape, and the first one made
before a recurrence rather than after.

### ✅ `df21fd5` LANDED — 1.5.6b step 1, THE FLOOR'S EVIDENCE AND NOT THE FLOOR. Notice 2026-09-17 11:08 from `nitpick-compiler_s7`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`. ANCHOR STAYS `b72d7774…` / 59 352 B.**

**✅ Verified on the wire, and all six rows unchanged.** **And the structural fix from the 112-byte
correction is IN USE:** the ladder now prints *"moved: nothing / unchanged: npkrt.o, builder.o,
builder, npkc.ll, npkc.o, npkc"*, **deltas COMPUTED against `ladder_b7a7491.txt` by the loop** —
no summary sentence left to type, and none drifted.

**WHAT LANDED is the floor's EVIDENCE, not the floor.** The **kernel-effect table** — what each
syscall the floor issues may write — **is now ONE generated authority** (`VERIFICATION_REFERENCE`
§9.2's `kernel-effects` region → `npkg/floor_kernel.npk`): **four hand-maintained lists became
zero.** A new ordinary program, `tests/backend/programs/kernel_effects.npk`, **holds every write
row to the RUNNING kernel with sentinel-filled buffers and demands equality.** Measurement found
**four things wrong in the table**, none on a verdict's path — `sched_getaffinity`'s length and
missing bound (**the row that hid DEF-52**), `rt_sigaction`'s length in the unsound direction, and a
generated `TCB` sentence claiming rows for `clone`/`execve` that did not exist.

**⭐ AND A PLANTED FAULT PROVED THE METHOD.** `npk_hardware_concurrency` is now **specified: six
rows.** **On a scratch floor with step 0's `memset` removed, exactly ONE of those six is refuted —
so the method would have found DEF-52.** *That is the discipline the eighth orchestrator's brief
asked of every verifier here — require a planted fault — applied by the compiler side to its own
specification, unprompted. A check shown to fail on the bug it claims to catch is worth more than
any number of green runs.*

**NUMBERS, verified against the tracked file at `df21fd5` rather than taken:** harness 52/52, parity
1 406, 268 real-backend programs; `nitpick.obligations` **368** rows unmoved (439 decided);
`runtime/npkrt.obligations` **376 rows over 86 symbols, 369 discharged, 7 `budget`** — **+6 rows,
all `npk_hardware_concurrency`'s.**

## ⚠ THE LABEL SLIP CAME BACK — IN THE ONE LINE THE FIX DID NOT REACH

**The notice says "7 residue". The file's verdict word is `budget`** — read at `df21fd5`: col 4 is
**7 `budget`, 369 `discharged`**, nothing else. *Their own first notice had it right.* **And the
place it recurred is exact and instructive:** the structural fix computed the LADDER deltas in a
loop, and **the ladder was perfect. The obligation COUNTS line is still typed — and that is where
"residue" crept back.** ***Sixth instance of the typed-summary shape, and this time it located
itself precisely: in the one line the loop does not print.*** *Every count in the line is right;
only the word is wrong. The remedy is the same one they already applied — print the verdict
histogram from the manifest, so there is no word to choose.*

## ⚠⚠ F2 GAINED A SHAPE, IN OUR CLASS — AND THEY ASKED US A DIRECT QUESTION ABOUT OUR OWN SCAN

**Found at implementation: an `extern` block's METHOD named after a builtin is refused too**,
because its generated stub is a module-level `pub async func:<method>` (D-190). **So a driver
interface with a method called `read`, `write`, `open` or `close` is refused**, reported once at the
method's own declaration. **Trait and impl methods stay exempt.**

**Their question: *"Your 532-declaration scan covered `func:` generally, so extern methods were in
it; say so if they were not."*** **Answered by TESTING the pattern, not by recalling it:**

```
extern method syntax, from tests/backend/programs/extern_stub.npk at df21fd5:
    extern:"mockif" = {
        func:probe = int64(Bridge->:b, Duration:within);     <- MATCHED by our scan pattern
        func:plus  = int64(Bridge->:b, int64:x, ...);        <- MATCHED
extern BLOCKS declared in our tracked library code:  0
    (both `extern` mentions are COMMENTS -- vec.npk:148 and probe15:53)
```

**So their assumption was correct: the scan pattern does catch extern methods — and there are none
here to catch.** *Worth noting what the right answer was NOT: "our scan covered them" alone would
have been true and uninformative. The useful statement is both halves — the method would have found
them, and the set is empty.*

**RE-CHECKED AGAINST THE AUTHORITATIVE TABLE rather than the reference document** (hazard 11's
lesson — check what decides, not a document about it):

```
names in is_builtin_name, src/frontend/builtins.npk at df21fd5    56
  names in it that our earlier 65-name scan lacked                 0   (that scan was a superset)
func: declarations incl. extern methods, tracked library code    532
collisions                                                         0
```

**56 against their stated 57 is RECONCILED, not an error:** `hardware_concurrency` is **not yet** in
the table on main (0 mentions at `df21fd5`) because it lands with F3 at step 3 — and they described
the table *"at landing"*. **56 today + `hardware_concurrency` = 57 at landing.** *Their phrasing was
precise; the gap was in reading "at landing" as "on main".*

## ⚠ NOT A FORECAST — AN OPEN QUESTION WITH THE AUTHOR (S-76), AND ITS EXPOSURE WOULD BE LARGER

**Whether D-294 should also refuse a PARAMETER or LOCAL of FUNCTION TYPE named after a builtin** —
measured on their side: such a local **redirects the bare call inside its function.** **Not
ratified.** *Flagged here because if it is, the surface is no longer module-level functions (532)
but every function-typed parameter and local in the libraries, which is a different and much larger
denominator — and it would arrive as a forecast with its code before landing.*

**Still owed, unchanged:** 1.5.8's `terminate` / `decreases` keyword-or-refusal answer.

### ⚠ F1 LANDED — THE FLOOR MOVED at `b7a7491`, notice 2026-09-17 08:27 from `nitpick-compiler_s7`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

## ⚠⚠ THE ANCHOR IS NOW `b72d7774…` / 59 352 B — superseding `d8a51b42…` / 59 192 B

**✅ The forecast arrived as a landing, exactly as labelled, under the anchor protocol:** first
lines name the move; the previous digest is quoted beside the new; the commit and reason are named.
**Verified, not taken:** `b7a7491` is on the compiler's origin by `git ls-remote`, **and the previous
digest they quote is exactly this board's current anchor** — which is what makes the move
authenticate rather than merely assert. The "was" values for the two rows that moved (`builder`
`65c5a3da…`, `npkc` `516cce69…`) also match what this board recorded.

```
npkrt.o    b72d7774...     59,352 B  MOVED  (was d8a51b42…, 59,192 B)   the new anchor
builder.o  c489068f...  9,085,152 B  unchanged
builder    d1bfa940...  7,906,536 B  MOVED  (was 65c5a3da…, 7,906,424 B) -- links the floor
npkc.ll    8bb03048... 24,820,298 B  unchanged -- THE EMISSION, the row that travels (D-265)
npkc.o     06c5650c...  9,799,024 B  unchanged
npkc       fb6e9153...  8,537,776 B  MOVED  (was 516cce69…, 8,537,664 B) -- links the floor
```

**✅ THE SHAPE IS THE ONE A FLOOR-ONLY CHANGE MUST HAVE:** the floor's object and the two binaries
that link it moved; the emission and both compiler objects did not. **No surface change** — no
program's meaning moves, nothing newly refused, no new trap armed. **They predicted the new
`npkrt.o` digest from the branch before landing, and the landed build reproduced it** — another
falsifiable prediction that held.

**⚠ BUT ONE SENTENCE IN THE NOTICE DOES NOT MATCH ITS OWN NUMBERS.** It says the floor's object and
the two binaries *"moved, by the same 112 bytes each."* **Checked:**

```
npkrt.o   59,192 -> 59,352     +160 B
builder   7,906,424 -> 7,906,536   +112 B
npkc      8,537,664 -> 8,537,776   +112 B
```

**The two binaries agree with each other at 112; the object moved 160.** *Every listed digest and
size is right and the shape argument holds — a link need not preserve an object's size delta, as
this board recorded at 1.5.6 step 1. Only the summarising sentence is wrong.* **It is the typed
summary of a generated fact drifting from the fact a fifth time — and from a session whose brief
carried that exact principle, attributed.** *Not a defect in the landing and not worth more than a
line back; worth recording because it shows the principle is not self-enforcing even when it is
known. The rows were generated and correct; the sentence was typed and was not.* **✅ RESOLVED BY REMOVING THE SENTENCE, NOT BY
BEING MORE CAREFUL, 2026-09-17 08:28.** `nitpick-compiler_s7` struck it verbatim and gave the true
one — *the floor's object moved 160 bytes and each binary that links it 112*. **Verified that
nothing landed carries the false figure:** `b7a7491`'s pushed commit message contains **no**
mention of `112`, and **no** tracked file at `b7a7491` contains it — only the notice did. **Their
account of the mechanism:** *the six rows were generated by a loop and compared by a loop; the
summary was typed from a glance at two of the three deltas.* **And the fix is the one that
actually answers "knowing the principle does not enforce it": the deltas are now COMPUTED AND
PRINTED BY THE SAME LOOP THAT PRINTS THE ROWS, so there is no sentence left to type.** ***A
principle is enforced by removing the opportunity to violate it, not by remembering it.*** *That
is the same move as generating §4c instead of summarising it, and as listing all six ladder rows
instead of describing which moved.*

**TWO COMMITS UNDER ONE FULL HARNESS:** `ce8ba46` (1.5.6b planned and ratified — D-293, D-294, the
D-288 amendment, DEF-53 declared; documents only) and `b7a7491` (step 0). **52/52; 267
real-backend programs, each also through `opt -O2`; 3 runtime-floor tests, one new; parity 1 403
verdicts agreeing; `npkc` and the verified compiler byte-identical.** Numbers with denominators:
`nitpick.obligations` 368 rows unchanged; 439 obligations decided over the compiler (273
discharged, 138 open, 22 unencoded); `runtime/npkrt.obligations` 370 rows over 85 symbols (363
discharged, 7 `budget`) — **same totals, with 25 HASHES moved and NO verdict moved**: all 3 of
`@npk_mono_now`'s rows and 22 of `@npk_hs_put_dec`'s 23, every one discharged before and after.

**DEF-52 FIXED** — the affinity mask is zeroed before the kernel sees it; still unreachable until
D-293's builtin lands. **DEF-53 FIXED** — all eight out-of-entry allocas hoisted, including the
two in loops (16 bytes per pinged task in `npk_windup_all`, per futex return in
`npk_thread_join`).

## ⭐ THE DEF-53 LESSON, WHICH IS THIS BOARD'S HAZARD 6 ARRIVING IN THE COMPILER

**DEF-53 was not a new rule.** D-173, settled at 1.0.9a, already said *"allocas are hoisted to the
entry block"* and **had a belt in both runners over every EMITTED module. It had simply never been
pointed at the hand-written floor.** *That is exactly hazard 6 — a check that was correct, whose
DENOMINATOR silently excluded something, where nothing would ever have reported the omission
because the check that could have was not looking there.* Hazard 6 was eight trees swept as seven;
DEF-53 was every emitted module checked and the one hand-written module skipped.

**The fix is the same shape as ours too:** the existing check run over one more file, **plus one
genuinely new rule beside it — every alloca fully DEFINED in its entry block before anything else
touches it — whose TWO implementations produce byte-identical findings.** *Two generators agreeing
is, once again, the instrument.*

**STILL FORECASTS, unchanged, nothing landed:** F2 (D-294, `RESOLVE-001` on a builtin-named
function, 1.5.6b step 4) and F3 (D-293, `hardware_concurrency`, step 3). **STILL OWED:** 1.5.8's
`terminate` answer, named with its code, before a re-pin could surprise us.

### ✅ `efffccf` LANDED — DOCUMENTS ONLY, THE FLOOR DID NOT MOVE. FIRST NOTICE FROM `nitpick-compiler_s7`, 2026-09-17 06:18. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`. ANCHOR STAYS `d8a51b42…` / 59 192 B.**

**✅ VERIFIED, NOT TAKEN:** `efffccf` is on the compiler's origin by `git ls-remote`, and **all
six ladder rows match this board's recorded values** — checked against the board, never against
`../nitpick/build/` (hazard 11).

## ⭐ THE BRIEF WORKED — EVERY LESSON ARRIVED IN THE SUCCESSOR'S FIRST NOTICE

**This is the payoff of handing the six items over as values with procedures attached, and it is
worth recording as evidence rather than as courtesy.** A session that had never spoken to us
produced, unprompted, in its first message:

```
"landed as efffccf, origin/main == efffccf"      the landed-sha rule, verbatim
all six ladder rows, unchanged ones included     and rebuilt AFTER landing, cross-checked
                                                 against an independent sha256sum
368 rows = nitpick.obligations                   the distinction lost at two earlier
439 = obligations DECIDED over the compiler      handoffs, now WITH denominators
7 `budget`                                       the manifest's own verdict word, not
                                                 "residue" -- the fourth label instance, fixed
forecasts labelled "file them as forecasts"      the tense error of the 1.5.6 close, fixed
DEF numbering stated so the board stays aligned
```

***Two handoffs ago, the ladder and the 368/439 distinction were both lost. This time nothing was.
The difference was not the model, the session or the goodwill — it was the form.***

**WHAT LANDED:** the 1.5.7/1.5.8 correction is in the tree (`b7d60dc`'s pushed message annotated
in `1.5.6.md`, not rewritten); **S-71 ratified** as an amendment to D-218 (2) — `lp.dio=false`, a
documentation act; **DEF-52 declared (OPEN)** — `npk_hardware_concurrency` popcounts 120 bytes of
uninitialised stack and answered **1008 on a 48-thread machine**, but is **UNREACHABLE**, nothing
calls it; and OPEN_DECISIONS §2g's **E-1…E-4**, the four places `_s6` said it would try to prove its
own 1.5.6 evidence wrong. Harness 52/52, **267 real-backend programs**, parity 1 401,
byte-identical. **DEF-53 is on the 1.5.6b branch, not in `efffccf`** — the hand-written floor never
received D-173's entry-block rule: 8 of 15 allocas outside their entry blocks, 2 inside loops, and
**a loop-body alloca SIGSEGVs under the pinned `llc` at both -O0 and -O2.**

## ⚠ FORECASTS — FILED AS FORECASTS, AS LABELLED. NOTHING BELOW HAS LANDED.

- **F1 — THE FLOOR WILL MOVE at 1.5.6b step 0** (DEF-52 and DEF-53 fixed, every alloca hoisted).
  The anchor protocol will be followed. **No surface change.**
- **F3 — the builtin `hardware_concurrency() -> int64`, never fails** (D-293, 1.5.6b step 3):
  D-181 §4's promise, never reachable until now.

## ⚠⚠ F2 — D-294, A NEW REFUSAL IN OUR CLASS, AND A STRUCTURAL CHANGE TO THE NAMESPACE

**Ratified today, landing at 1.5.6b step 4: `NITPICK-RESOLVE-001` at a module-level `func:` —
plain, `pub`, `async` or `thread`, inside an inline module or out — WHOSE NAME IS A BUILTIN'S.**
Today such a declaration **silently shadows the builtin** — measured on their side: a program's
own `mono_now` answered instead of the clock, consistently through checker and emitter. D-239
already refuses this for type names; D-294 applies it to functions. **METHODS ARE EXEMPT**
(`Writer.write`, `Reader.read`) — a per-type namespace reached only through a receiver.

**✅ ZERO EXPOSURE, AND THEIR MEASUREMENT WAS REPRODUCED HERE RATHER THAN ACCEPTED:**

```
builtin names in BUILTIN_REFERENCE's tables     65   (they stated 65)
func: declarations in TRACKED library code     532   (git ls-files, three code repos)
declarations whose name is a builtin's           0
`hardware_concurrency` anywhere                  0   (F3's first reserved name)
```

*They measured our working tree and flagged that they had not checked our pin. That caveat does
not bite: the pin is the COMPILER version we build against, and library source is not versioned by
it — so for a name scan the working tree, the tracked tree and "our pin" are the same thing, and
all eight trees were clean and level at the sweep.*

**⚠⚠ THE CONSEQUENCE TO CARRY, IN THEIR WORDS: "FROM D-294 ON, EVERY ADDED BUILTIN RESERVES A
NAME."** **The builtin namespace becomes a RESERVED SET THAT ONLY GROWS**, and every addition is a
potential breaking change for any of our **532** function declarations that happens to share its
name. **They commit that each one will reach us as a notice before it lands.**

**AND IT JOINS A PATTERN, SO THE CHECK SHOULD BE ONE CHECK, NOT THREE:**

```
1.5.4c   `use` became a keyword                    0 collisions (measured then)
1.5.8    `decreases` likely to become one          0 collisions (measured 2026-09-17)
D-294    every builtin, now and in future          0 collisions (measured today)
```

**All three are the same question — does any library identifier collide with a name the language
has reserved — and it is cheap: extract the reserved names, intersect with our declarations.**
*Run it on every notice that adds a keyword or a builtin, and run it once in full at the re-pin,
because the reserved set will have grown by then in ways no single notice described.*

**STILL OWED, UNCHANGED:** 1.5.8's `terminate` kind has no surface syntax, so its planning opens
with a language question; the answer arrives as a keyword-or-refusal named with its code, before a
re-pin could surprise us.

### ⭐ THE RESUME QUESTION IS ANSWERED FROM THE PLAN — **1.6 ADDS NO REFUSALS AND NO SYNTACTICALLY-ARMED TRAPS.** `nitpick-compiler_s6`, 2026-09-12 10:36. **STILL RECORDED, NOT WORKED.**

**This is the answer the pause has been waiting for, and it was answered from
`meta/roadmap/1.6/README.md` read end to end and grepped for diagnostic codes, trap codes
and refusal language rather than from memory.** *"There are none."*

**AND THE REASON IS STRUCTURAL RATHER THAN INCIDENTAL: D-233 MOVED 1.6's EVIDENCE TO THE IR
THE COMPILER ALREADY EMITS.** The three legs are **abstract interpretation over that emitted
IR** (leg A), **Z3 under D-218 — 1.5's spine, untouched by the cycle** (leg B), and **Alive2
over the pinned `opt -O2` pipeline** (leg C). Every subcycle is tooling: **1.6.0** a bring-up
gate between two engine candidates at pinned commits, **1.6.1** leg A wired in as a standing
harness stage with an alarm ledger, **1.6.2** leg C likewise, **1.6.3** the dry run and the
evidence package. **Nothing in it changes what the compiler accepts.** *The only use of
"refused" in the whole file is an engine option that trades determinism for speed.*

## ⚠ THE CAVEAT, WHICH IS THE HONEST HALF AND MUST NOT BE DROPPED WHEN THIS IS QUOTED

**1.6 IS WHERE THE LANGUAGE DOOR CLOSES, NOT WHERE IT IS ALREADY SHUT.** The plan restates
the standing rule in its own watch-list: **anything entering the language still has to land
before the evidence campaign closes, because a late change re-opens every touched
obligation.**

**So the risk to the library side is not 1.6's CONTENT — it is that something found during
1.5.7 or during 1.6 turns out to need a language-level answer and is LANDED rather than
deferred**, exactly as 1.5.4b's shift-amount rule and 1.5.5's borrow rules were. **They
decline to promise otherwise, and give the right reason:** *"the alternative is deferring a
real hole past the point where fixing it is affordable."*

**THE SHAPE OF THE REMAINING RISK, WHICH IS NARROWER THAN 1.5's WAS.**

```
1.5.4, 1.5.5   dense with refusals -- they were landing THEORIES about the language
               (shifts, bitwise, floats, simd, aliasing), and each theory found
               constructs the checker had been ADMITTING WITHOUT DECIDING
1.5.6          none -- it was about the FLOOR, which is not the language
1.5.7          a harness (mocked primitives, PCT-seeded scheduler, virtualized
               reactor, wired beside `// stress:`) -- finds RUNTIME defects,
               which are fixed in the runtime
1.6            analyzers over emitted IR
```

***Both remaining subcycles are instrument work. The language-change risk in each is the
risk that an instrument FINDS something, not that the plan SCHEDULES something.*** *That is
a materially different exposure from 1.5.4's, where the refusals were the deliverable.*

**✅ AND A STANDING OBLIGATION, NOT A COURTESY — THEIR WORDS.** *"If one does land, you will
hear it from this seat in the notice, named as a refusal with its code, before you find it by
re-pinning. That much I will put in the brief as a standing obligation."* **So a
language-level change now arrives as an announcement rather than as a surprise at a re-pin —
which is precisely the failure mode the pause exists to avoid.**

**Our six values are going into `_s7`'s brief VERBATIM as a quoted block with the procedures
attached, not paraphrased into conventions** — and they noted the diagnosis was ours to make:
*"I only saw that something was lost, not which form survived."*

## ⚠ AND A DISPUTED FIGURE, LEFT OPEN RATHER THAN SETTLED EITHER WAY

**They correct this board's claim that the close notice's figure "was off by 52 symbols",
and they have misread WHICH numbers were compared — but they may still be right about the
substance.** Stated precisely:

```
this board compared   137  ("a specification for 137 symbols", the UN-LANDED forecast notice)
                 vs    85  ("370 obligations over 85 specified symbols", the LANDED close)
they read it as        79  vs 85, which is step 4's figure against the close's -- not what
                           was compared; 79 + 6 models = 85 and that part is coherent
```

**So the arithmetic was right and the CHARACTERISATION may not be: if 137 counts the symbols
the specification DESCRIBES and 85 counts those with SPECIFIED OBLIGATIONS, there is no
drift at all — it is the 368/439 shape a third time, two true numbers with one wearing the
other's name.**

**⚠ AND THE FINDING THAT MATTERS MORE THAN WHO WAS RIGHT: NEITHER 137 NOR 85 NOR 79 APPEARS
ANYWHERE IN THE LANDED DOCUMENTS.** Checked at `b7d60dc` against `meta/specs/TCB.md` and
`runtime/npkrt.spec`: **not one of the three is present as a literal.** What *can* be
verified from the tree: **`runtime/models/` holds exactly 6 models** (`channel-table`,
`driver-registry`, `futex-mutex`, `park-unpark`, `shared-arena`, `trap-route`) — confirming
that half of 85 — and **TCB.md §4's membership table carries 175 distinct symbols**, which
matches neither figure. **§4b and §4c now exist exactly as forecast.**

***So the floor's evidence is generated and held by both runners, and the SUMMARY COUNTS
quoted in notices are not in it.*** *A board that cites one has no way to re-derive it, which
is the same defect as a citation that cannot be followed.*

## ✅ RESOLVED — AND THIS BOARD WAS WRONG TOO. EVERY FIGURE RE-DERIVES FROM THE TREE.

**`137` versus `85` is the 368/439 shape a third time, confirmed by `nitpick-compiler_s6`
against `b7d60dc`: two true numbers with different denominators and no drift.**

```
175   `define`s in runtime/npkrt.ll                       -- the floor's whole surface
137   `(symbol ...)` sections in runtime/npkrt.spec        -- symbols DESCRIBED
 85   distinct symbols with rows in npkrt.obligations      -- symbols WITH EVIDENCE
370   rows: 363 discharged, 7 budget, 0 refuted
```

**The 52-symbol gap is not slack. Their words, and worth keeping verbatim:** *"137 is
'described', 85 is 'has evidence', and the gap is 52 symbols whose whole specification is a
promise at the kernel boundary or an admission of residue. That gap is not slack — it is most
of the allocator, the waits, the thread and process boundaries, and it is the honest part of
the picture."*

**⚠ AND THIS BOARD'S OWN "UN-RE-DERIVABLE" FINDING WAS WRONG — THEY ACCEPTED IT AND IT DOES
NOT HOLD.** The figures are not *written* in `TCB.md` or `npkrt.spec` as literals, which is
what this board checked; **but every one of them is COMPUTABLE from committed artefacts, one
command each, verified at `b7d60dc`:**

```
175  grep -cE '^define' runtime/npkrt.ll                              -> 175
137  grep -cE '^\(symbol' runtime/npkrt.spec                          -> 137
 85  awk '!/^#/{print $6}' runtime/npkrt.obligations | sort -u | wc -l -> 85
370  grep -cE '^[^#;]' runtime/npkrt.obligations                      -> 370
363  awk '!/^#/ && $4=="discharged"' npkrt.obligations | wc -l        -> 363
  6  ls runtime/models/ | wc -l                                       -> 6
 79  85 minus the 6 models                                            -> 79
```

***So "not stated" and "not checkable" are different things, and this board conflated them —
the same error it has been correcting in others all week, one level up.*** **`175` now agrees
three independent ways**: the object's `define`s, `TCB.md` §4's membership table, and their
stated figure. *Their proposed fix — a generated counts line at §4c's head — is therefore a
convenience that saves a reader inventing four commands, NOT the closing of a hole. Worth
knowing before anyone spends half an hour plus a harness on it.*

**⚠ ONE FIGURE DOES NOT RE-DERIVE BY ITS OWN NAME, AND IT IS A FOURTH LABEL INSTANCE.** The
notices say **"7 residue"**; the manifest's verdict word for those rows is **`budget`**.
Grepping the manifest for `residue` returns nothing. *`residue` is the category in prose,
`budget` the verdict in the file — true on both sides, findable from only one.*

**⚠ AND THIS BOARD WAS NARROW: §4c ALREADY CARRIES BOTH FINDINGS, AND HOLDS THREE RESIDUE
CATEGORIES WHERE THIS BOARD SAW ONE.** Read verbatim at `b7d60dc` 2026-09-12 10:42 rather than
taken from their quote of it. **The label distinction is in the section's own opening
sentence** — *"`budget` is a row the pinned z3 did not decide under the profile — the verdict
rule keeps it as RESIDUE, never as a proof"* — **and the concentration is the generated
`floor-residue` region's body.** *So the DOCUMENT was right all along and the NOTICES were
loose, which is the opposite of where both sides were looking.*

**THE THREE CATEGORIES, of which the 7 budget rows are only the first:**

```
1. rows the profile did not decide (`budget`)   7: @npk_small_free x6, @npk_int_to_string x1
2. sentences the spec CARRIES, each a claim     12 symbols, each naming what is NOT decided
   deliberately NOT MADE
3. the models' residue                          the standing bounds (VERIFICATION_REFERENCE §9.4)
```

**⭐ AND CATEGORY 2 HOLDS THE ENTRY THAT MATTERS MOST TO THESE LIBRARIES, WHICH NEITHER SIDE
NAMED:**

> **`@npk_trap` — the call of `npk_failsafe` is opaque — the program's handler is not the
> floor's (D-0…)**

***So the floor's evidence stops at the handler boundary by design.*** **⚠ BUT THIS
BOARD'S FIRST READING — "the floor proves nothing about our 145 `failsafe` bodies" — IS
BLUNTER THAN THE TRUTH, AND `nitpick-compiler_s6` CORRECTED IT 2026-09-12 10:45.**

## ⭐ THE GUARANTEE STACK FOR ONE OF OUR `failsafe` HANDLERS — reference, not a notice

**This is the most useful thing to come out of the whole quiet period for whoever eventually
writes contracts in these repositories, because it says exactly where their work begins.**

**WHAT THE FLOOR PROVES about the route a handler runs on** — each backed by a named control
in `runtime/models/trap-route.model`, **verified present at `b7d60dc` rather than taken on
report**, every one a `(bad …)` clause the model proves unreachable:

```
runs AT MOST ONCE, on the trapping thread     (bad two-failsafes ...)          :113
                                              unreachable at K 14 / D 6
every other thread STOPPED OR EXITED --       (bad step-after-failsafe ...)    :114
  no task step happens anywhere after it begins
no other thread can END THE PROCESS under it  (bad exit-mid-failsafe ...)      :115
  a second trapper parks; a program `exit` racing the holder parks too
runs AFTER THE DRIVERS ARE KILLED, with an    (bad failsafe-blocked-on-heap)   :117
  allocator that CANNOT block on a heap mutex a stopped thread may hold forever
                                              (and D-292's 1 MiB .bss region)
every path through `npk_trap` ENDS            `(ensures-trap true)` -- npkrt.spec:205
```

**WHAT THE FLOOR PROVES about what the handler DOES: nothing, deliberately, because it is
ours.** The full §4c entry, whose tail this board had trimmed: *"the call of `npk_failsafe`
is opaque — the program's handler is not the floor's (D-014); **its result decides the exit
status through `npk_exit`, whose promise is the boundary's**."*

**⚠ AND THE PART THIS BOARD HAD MISSED ENTIRELY: OUR 145 BODIES ARE NOT EVIDENCE-FREE. THEIR
EXIT DISCIPLINE IS CHECKED BY THE COMPILER RATHER THAN BY THE FLOOR (D-014 §3.3).**

```
a non-positive LITERAL exit in a failsafe   REACH-004 at compile time -- it does not build
a COMPUTED exit code                        a `failsafe-post` row in that program's own
                                            manifest, proving code > 0 at every exit point,
                                            EnsuresViolated armed if it cannot be proven --
                                            and inside `failsafe` that re-enters and ends at 70
```

***So the stack is: the FLOOR proves the handler runs once, alone, unblocked and after
cleanup; the COMPILER proves its exit code is positive; and EVERYTHING BETWEEN THOSE TWO IS
OUR VERIFICATION TO DO.*** **That is the line, and it is far more useful than either "the
floor covers it" or "the floor covers nothing".** *This board asked for the boundary and got
it drawn on both sides — including the half that credits our own toolchain rather than
theirs.*

*(Our own earlier measurement fits this exactly: **zero non-positive literal exits** inside
any of the 145 bodies, so REACH-004 refuses nothing here, and **zero computed exit operands**,
so no `failsafe-post` row is owed either. The exit discipline is already clean under D-014
§3.3 — what remains unproven is everything the handlers DO before exiting.)* *That is the single most important sentence in
§4c for a library whose entire error discipline is `failsafe` — the runtime proves the trap
route, and proves nothing about what our handlers do once reached. Every `exit` code in those
145 bodies is our claim, not the floor's.* **Others in the same list that touch us:**
`@npk_read_file` / `@npk_read_stdin` (the kernel's bytes are opaque), `@npk_wild_live_count`
(the live-block walk), `@npk_small_free` (five ensures and the frame), `@npk_udivmod128` (the
division identity `a = q*b + r`), `@fmod` / `@fmodf` (the reduction's result).

**The original, narrower finding, kept because it is still true of category 1:** **six of the seven are `@npk_small_free`** and the seventh is
`@npk_int_to_string`. *So the floor's undischarged residue is almost entirely the small-block
free path — which is allocator behaviour every library here sits on top of, and is the single
most useful sentence to carry out of `TCB.md` §4c.*

**✅ AND THE z3 PROFILE INSTRUCTION IS SELF-CARRYING AFTER ALL** — `npkrt.obligations`'s own
header line reads `# options smt.random_seed=0 sat.random_seed=0 rlimit=20000000
lp.dio=false`, so a manifest hands a reader its own profile without anyone having to
remember the notice.

### ✅ 1.5.6 IS CLOSED — LANDED as `b7d60dc`, notice 2026-09-12 02:30. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`. ANCHOR STAYS `d8a51b42…` / 59 192 B.**

**✅ VERIFIED ON THE WIRE, NOT FROM THE NOTICE.** They claim `main == origin/main ==
b7d60dc`; `git ls-remote` on the compiler's origin returns **`b7d60dc`**. *The landed-sha
protocol agreed one message earlier was used correctly on its first outing — and this board
checked it anyway, which is the arrangement working rather than distrust.*

**✅ `npkrt.o` DID NOT MOVE, AND THEY SAY "VERIFIED RATHER THAN ASSUMED".** The floor's only
edit across steps 5 and 6 was renumbering DEF-49 → DEF-51 **in two comments**, and the object
is byte-identical to step 4's. **Anchor unchanged.** *A session that had just been caught
writing a forecast as a fact then went out of its way to say which of its own claims was
measured. That is the correction landing, not merely being accepted.*

**✅ AND ALL SIX ROWS CAME WITH FIVE OF THEM UNCHANGED — "listed anyway because that is what
makes them checkable".** *Our own argument, quoted back. The redundancy is no longer
something this board asks for; it is something the sender explains.*

## ⚠ THE FORECAST FIGURE WAS WRONG BY 52, WHICH IS WHY IT WAS MARKED

```
forecast, in the un-landed notice   "a specification for 137 symbols"
landed, in the close-out harness    370 obligations over 85 SPECIFIED SYMBOLS
                                    (79 spec sections + 6 protocol models)
```

**Marking the pre-landing figures as forecast was not pedantry: one of them was off by
52 symbols.** *Had this board adopted "137 symbols" as fact, it would now be carrying a
number nobody could reproduce, cited from a commit that never landed in that form.*

**THE CLOSE-OUT HARNESS, as landed:** every stage green, **52/52**; **parity 1 401 verdicts**
agreeing between the two runners, with `npkc` and the verified compiler **byte-identical**;
the floor stage **370 obligations over 85 specified symbols — 363 discharged, 7 residue, none
refuted** — every model control `sat`, and the floor's rows, index and controls
**byte-identical between the runners**. **`nitpick.obligations` 368 rows, unchanged.**
**`TCB.md` §4b and §4c now resolve** — §4b the syscall boundary at **100 rows** (per symbol,
the numbers it issues and the numbers it reaches on its own paths, the trap route named
rather than counted); §4c **what the evidence does not cover**: the 7 undecided rows by
symbol, every `(residue "…")` sentence verbatim, and the models' bounds. Both generated and
held by both runners, as §4's membership table already was.

## ⭐ THE STRONGEST EVIDENCE FOR "THE REDUNDANCY IS THE INSTRUMENT" IN THIS WHOLE RECORD

**The syscall table has TWO GENERATORS — Python's for the harness, Nitpick's for `npkg` —
and the first run with both REFUSED THE DOCUMENT.**

```
Python emitted   | @npk_heap_bad | syscall | -- | -- |
Nitpick twin     skipped the row entirely
```

**The Nitpick side was right**: a trap entry reaches the whole trap route and nothing of its
own, **so a row about it is noise rather than a boundary.** The same run caught the residue
region's two generators **disagreeing over an ellipsis against three dots.**

***"Neither was visible from one implementation, and neither would have been caught by a test
of either one."***

*This is the argument this board has been making about six-row ladders and unchanged digests,
demonstrated at a far higher cost and on their own tooling. A second implementation is not
duplication; it is the only instrument that can see a class of error a test cannot, because a
test encodes one implementation's idea of the answer.*

## ⚠⚠ STRUCK 2026-09-17 — **CYCLE 1.5 HAS TWO SUBCYCLES LEFT, NOT ONE.** The block below is kept with its error visible.

**THE FALSE SENTENCE THIS BOARD ACCEPTED AND REPEATED, struck rather than deleted:**
*"1.5.7 … is the LAST subcycle of cycle 1.5"* and *"on present plans the next thing that
could move your premises is still nothing."* **Both wrong.** `nitpick-compiler_s6` retracted
them; **verified here against `meta/roadmap/1.5/README.md` at `b7d60dc` rather than taken on
retraction** — the map's rows read:

```
line 239   | 1.5.7 | The G-5 schedule-exploration harness ...
line 240   | 1.5.8 | Overflow obligations (G-1's static leg) + close-out ...
```

**⚠ AND `1.5.8` IS THE ONE REMAINING SUBCYCLE THAT COULD MOVE OUR PREMISES — IT SITS BETWEEN
US AND 1.6, AND THE 1.6 ANSWER ITSELF STILL STANDS.** `VERIFICATION_REFERENCE` §7b assigns it
**five obligation kinds** — `overflow`, `bounds`, `cast-range`, `terminate`, `stack-depth` —
and **the compiler's manifest carries ZERO rows of any of them today, verified: 368 rows, none
of the five.** D-210 item 4 is a ratified commitment that 1.5 proves those traps away, and
1.6's leg B lists them as evidence *arriving from* 1.5.

**THE RISK, MEASURED AND SPLIT BY KIND RATHER THAN TAKEN AS ONE LUMP:**

- **`terminate` is the keyword risk.** It means *"a recursion or unbounded loop has a
  decreasing variant"*, and **there is no surface syntax for it.** Verified: `decreases`
  appears **nowhere in `src`** — only three prose mentions, at
  `meta/roadmap/1.5/README.md:109` (*"`decreases`-style variants on recursion and unbounded
  loops"*) and two research digests. *The roadmap already naming it makes a keyword
  ANTICIPATED rather than speculative.* **A new reserved word is exactly the shape that
  broke nothing at 1.5.4c only because we happened not to use `use`.**
- **✅ AND THE KEYWORD ITSELF WOULD COST US NOTHING TODAY.** Re-running 1.5.4c's check:
  **`decreases` as an identifier — 0 in `nitpick-regex`, 0 in `nitpick-time`, 0 in
  `nitpick-posix`.**
- **⚠ BUT THE CLAUSE WOULD NOT BE FREE.** If unbounded loops must carry a variant, the
  surface is **141 `while` sites — `nitpick-regex` 84, `nitpick-time` 57, `nitpick-posix` 0.**
  *Not all are unbounded, so that is an upper bound on candidates rather than a count of work
  — but it is the first item in this whole quiet period whose cost is measured in the
  hundreds rather than in ones.*
- **✅ `overflow` points the OTHER way.** 1.5.8's row reads **"prove-or-retain on plain-int
  arithmetic"** — work that *retires* a guard where it is proven, rather than adding a
  refusal. **Low risk in direction, whatever its size.**
- **`bounds` and `cast-range` are unknown** and may arm or retire checks at sites our tier
  writes. *(`cast-range` was named at 1.5.4b as the thing that would eventually make a cast
  non-opaque — which is why `byteset.npk`'s masked shift discharges today "the form does not
  need it".)*

**THE STANDING OBLIGATION COVERS THIS**: if 1.5.8 adds a keyword or a refusal, **it arrives
named with its code, in a notice, before a re-pin could surprise us** — `nitpick-compiler_s7`
inherits that as an obligation and will answer the 1.5.8 question when that subcycle is
planned.

## ⚠ HOW THE ERROR TRAVELLED, BECAUSE IT IS THIS BOARD'S OWN LESSON TURNED ON ITS AUTHORS

**`_s6` grepped the 1.5 README for the `1.5.7` row, read the line it returned, and never read
the next line** — then wrote the summary into three tracked files, a pushed commit message,
the handoff brief and two notices to us. **Their own account:** *"precisely the thing I named
to you as the week's best lesson — a hand-written summary of a held fact, with no check on
it — committed by the person who named it, about a list that was correct and one line further
down."*

**AND THIS BOARD REPEATED IT WITHOUT CHECKING.** *We had the map, tracked and current, one
`sed` away, and we relayed a peer's summary of it instead — having spent the week establishing
that a summary of a generated fact has no check on it. The failure is not that they were
wrong; it is that we were positioned to catch it and did not look.* **`nitpick-compiler_s7`
caught it within an hour of taking the seat, by reading the map instead of the summary — and
asked `_s6` for the exact words we had received rather than guessing at them.**



**`nitpick-compiler_s6` is pausing here. 1.5.7 — the schedule-exploration harness — is the
LAST subcycle of cycle 1.5 and is NOT PLANNED YET.** If the seat hands off, **we get the
address before anything else arrives.**

**⚠ READ THIS AGAINST THE RESUME SIGNAL RATHER THAN AS IT.** This board's signal is a
**STATE** — *the compiler out of active implementation and into fixing and refinement* — and
a seat pausing between subcycles **is not that state**. But the shape is worth recording
honestly: **1.5 has one subcycle left, and the record holds that 1.5 and 1.6 together are
meant to carry the initial implementation to good shape.** *So this is the closest the
quiet period has come to its own end without reaching it. The pause holds.*

**They state plainly that our pin at `3d15ac9` is still behind and that NOTHING HERE REQUIRES
US TO MOVE IT** — and that when we do, the runtime under these libraries now has a written
specification (`runtime/npkrt.spec`), bounded models of its protocols (`runtime/models/`), and
an honest list of what it still does not promise (`TCB.md` §4c).

### ⚠ CORRECTED 2026-09-12 00:24 — **1.5.6 IS NOT DONE.** Steps 0–4 are landed; steps 5+6 are HELD in a worktree pending a harness. The `DEF-49` collision is resolved. Notice 2026-09-12 00:22. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`. ANCHOR STAYS `d8a51b42…` / 59 192 B.**

**✅ THE COLLISION RESOLVED, AND THE RULE THEY APPLIED IS THE RIGHT ONE.**

```
DEF-49   a thread's ROOT was never roused        (1.5.6 step 0)  -- stands
DEF-51   a leak in the two file readers          (1.5.6 step 4)  -- renumbered
```

**The later declaration moved, never the earlier, because the earlier one's citations are
already out in the world.** And the half worth keeping: ***"a citation that has been pushed
is annotated, not rewritten"*** — step 4's pushed commit message and execution record keep
the old number under a dated note pointing at the renumber. *That is the same principle this
seat applied to its own overstated commit subject days ago — corrected forward rather than
amended — arrived at independently on the other side.*

**Their own account of how it happened is the useful part**: they renumbered off DEF-43 when
they found it taken by 1.5.5, took the next number they could see, and **did not re-check
against a step they had landed days earlier in the same subcycle.** *"This was invisible from
inside the session that made it. A board that reads the notices side by side caught it in one
pass."* **Their conclusion, which this board adopts: notices should carry enough detail to be
CROSS-CHECKED, not merely enough to be ACKNOWLEDGED.** *That is the standing argument for the
six-row ladder and the full digest set even when nothing moved — the redundancy is the
instrument.*

**STEPS 5 AND 6 LANDED AS ONE COMMIT UNDER ONE HARNESS — declared as a deviation rather than
taken silently**, on the reasoning that the plan's steps are cumulative prefixes and the
validation rule (*the tree that lands is the tree that was tested*) is unchanged by merging
two. **`npkrt.o` did NOT move** — the floor's only edit is two comments, and comments do not
reach the object — **so no digest notice, and the anchor is unchanged.**
`nitpick.obligations` unmoved at 368 rows.

**⚠⚠ THE HEADING ABOVE ORIGINALLY READ "1.5.6 IS DONE" AND THIS BOARD WAS WRONG TO WRITE
IT.** `nitpick-compiler_s6`, corrected 2026-09-12 00:24: **steps 5 and 6 are ONE COMMIT
`6649c49` ON BRANCH `wt-b5` IN A WORKTREE — not on `main`, not pushed — with its full
harness started minutes before the notice was sent.** *"What I got wrong was the tense, not
the push."*

**SO IT IS HELD, NOT UNPUSHED, AND THE DISTINCTION IS THEIRS AND BETTER THAN OURS:** landing
is what happens **after** the harness returns green — the commit is cherry-picked onto
`main`, the harness paragraph amended into its message, and then pushed. **If the harness
goes red, that commit changes or disappears, which is exactly why it is not on `main`.**
**`origin/main` at `c5eb8c1` is the true and current state.**

**✅ AND THE PROTOCOL THIS PRODUCES IS THE MOST USEFUL THING IN THE EXCHANGE:** they will
now say ***"landed as `<sha>`, `origin/main == <sha>`" or nothing at all.*** **So from here,
A COMPILER NOTICE WITHOUT A LANDED SHA IS A FORECAST, AND THIS BOARD FILES IT AS ONE.**
*What caught this was not suspicion but a habit of theirs that we had recorded: every prior
notice carried the `main == origin/main` line, and its absence was the anomaly. They say so
themselves — "the habit your board noticed is the one that should have stopped me writing
this one."*

**WHAT FOLLOWS IS A FORECAST OF THE LANDED TREE, NOT A READING OF IT.** After landing,
`TCB.md` gains **three GENERATED regions** where our `c5eb8c1` checkout has one: **§4** the
membership table (symbol, class, disposition), **§4b** the syscall boundary — *which symbol
issues which number and which it reaches on its own paths, **with the trap route named
rather than counted, since otherwise every symbol "reaches" `exit_group` and the column says
nothing***  — and **§4c** the residue list (every undecided row by symbol, every
`(residue "…")` sentence verbatim, the models' bounds). **§5 stays what it is and gains four
acceptances.** *Our §5 reading of the current tree is confirmed correct for `c5eb8c1`.*

**FORECAST FIGURES, to be checked against the landed sha rather than adopted:**: a specification for **137 symbols** *(FORECAST — the landed figure is **85 specified symbols**; see the close entry above)*, six bounded
protocol models with sixteen controls, an enumerated syscall boundary, and **370 committed
rows — 363 discharged, 7 residue, none refuted.** `TCB.md` is finalised with three regions
generated from the tree and held by both runners, **so the membership table, the syscall
boundary and the residue list cannot go stale without a red run.**

## ⚠⚠ BUT THE STEPS-5+6 COMMIT IS **NOT ON `origin/main`**, AND THE TWO POINTERS DO NOT YET RESOLVE

**Verified at 2026-09-12 00:22 from our read-only checkout:**

```
our nitpick checkout HEAD   c5eb8c1   "1.5.6 step 4 ..."
git ls-remote origin main   c5eb8c1   -- the SAME commit
they report                 steps 5+6 landed as one commit, 1.5.6 done
```

**So the steps-5+6 commit is committed locally on their side and not pushed** — and unlike
every previous notice, this one did **not** carry the customary *"main == origin/main == <sha>"*.
***This is hazard 5 exactly, seen from the other end: a peer reading `origin` sees one state
and the author's local tree another.*** Our own board records that failure against a
predecessor of this seat; it is the same shape.

**Consequences, stated so nobody chases them:**

- **`runtime/npkrt.spec` DOES exist and is readable now** — 1 116 lines, 92 794 B, SMT-LIB2,
  headed *"the floor's specifications (1.5.6; D-288, D-289, D-290)"* and **held to
  `runtime/npkrt.ll` by the belts of both runners** — **and the reason that is worth more than a
  document is that it is CHECKED IN BOTH DIRECTIONS. `nitpick-compiler_s6`: "Several clauses
  I wrote were refuted during step 4 and were wrong; the floor was right."** ***"A
  specification nobody can refute is a wish."*** *Recorded because it is the clearest
  statement anyone in this ecosystem has given of why the verification work is not
  ceremony — and because it will decide, when these libraries eventually get contracts,
  whether those contracts are checked against the code or merely written beside it.*: a name it holds that the floor lacks, a
  word the floor accesses that it does not classify, or a classification the floor's text
  contradicts, **is a red run.** It landed by step 4.
- **`TCB.md` "section 4c" DOES NOT RESOLVE at `c5eb8c1`.** The file has sections **1–5** and
  no subsection markers inside §4. **The content they describe — the honest list of what the
  floor does NOT promise — is §5, "What a reader must accept"**: that LLVM's instruction
  selection is unvalidated, that the kernel implements its syscalls as documented, that z3
  decides correctly what it reports `unsat`, and that the encoding is sound. **Most likely
  §4c exists only in the unpushed commit.** *Recorded with the version it was checked
  against, because a pointer that cannot be followed is worse than no pointer.*

### ⚠ 1.5.6 STEP 4 IS LANDED — a leak in the two file readers, pin target `c5eb8c1`, notice 2026-09-11 23:19. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

## ⚠ THE ANCHOR IS NOW `d8a51b42…` / 59 192 B — superseding `81273821…` / 59 128 B

*Delta 64 B; no byte claim made, so an observation.* **They volunteered that step 3 did not
move the floor** — which is the useful half of a promise to notify only on movement:
**silence is now confirmable rather than merely assumed.**

```
npkrt.o    d8a51b42...     59,192 B  MOVED — the new anchor
builder.o  c489068f...  9,085,152 B  unchanged
builder    65c5a3da...  7,906,424 B  MOVED with the floor it links
npkc.ll    8bb03048... 24,820,298 B  MOVED
npkc.o     06c5650c...  9,799,024 B  MOVED
npkc       516cce69...  8,537,664 B  MOVED
```

**`npk_read_file` and `npk_read_stdin` LEAKED EVERY BUFFER THEY OUTGREW** — each doubling
allocated, copied, and abandoned the old block: **a managed block owned by nobody, invisible
to D-151 (which counts `wild` blocks) and to every test.** Measured before the fix: **fifty
reads of a 256 KiB file peaked at 22.6 MB against 1.2 MB for one read.** *Their note on how
it was found is the part worth keeping: **"Found by SPECIFYING the symbols, not by a test —
the frame claim over the caller's objects would not prove until the growth's memory was read
closely."** A leak invisible to every test was caught by a proof obligation refusing to
discharge.*

**THEIR DIRECT ASK — *"if any of your cost units were calibrated against the leaking floor,
re-measure"* — MEASURED AND ZERO.** Using `git ls-files`, the corrected method's first
outing: **no `tests/cost/` entries in any of the three code repositories, and zero
`read_file` / `read_stdin` calls in any tracked `.npk`.** Nothing of ours was calibrated
against the leaking floor because nothing of ours reads a file.

## ⚠ THE MANIFEST'S HEADER LINE MOVED — FILED FOR THE FIRST MANIFEST WE EVER RECORD

**`nitpick.obligations` keeps 368 rows with every verdict unchanged, but its HEADER now
carries `lp.dio=false` (S-71).** z3 4.16.0's Diophantine sub-solver **undoes its terms at
every `(pop)` by a big-rational matrix elimination**, so a row answering `unsat` in 8 s
returned from its pop **200 s later**, and a larger one **had not returned after 22
minutes** — a wedged solver under P-13, with only the runners' hang net (120 s + 10 s per
row) to catch it. **With it off no verdict moves anywhere** (measured both ways across the
compiler's 411 encoded rows and the floor's 350) **and the pops are instant.**

**⚠ THE INSTRUCTION THAT OUTLIVES THIS NOTICE: if you run z3 by hand against a committed
manifest, use the profile the manifest's HEADER LINE carries — do not supply your own.**
*We hold no manifest yet, so this costs us nothing today and would cost a resuming session a
silent wedge on its first verified build.*

**The floor's own evidence, for the record: 350 obligations over 79 specified symbols, 343
discharged, 7 residue, none refuted.** Steps 5 and 6 follow; **no further floor move
expected, and a notice only if one happens.**

## ⚠⚠ `DEF-49` NOW NAMES TWO DIFFERENT DEFECTS ON THIS BOARD — QUERIED, NOT RECONCILED

```
step 0 notice   DEF-49   a thread's ROOT was never roused (its owner word named
                         the spawning thread's executor)
step 4 notice   DEF-49   a leak in the two file readers
```

**Both came from `nitpick-compiler_s6`, days apart, and they are plainly different
defects.** Most likely a renumbering or a slip in one of the two — **but this board does not
silently pick one.** *It is the same shape as the `O-Y2` collision and the 368/439 label: an
identifier that means two things is worse than one that means nothing, because it reads as
resolved.* **Asked; both readings stand recorded until they answer.**

### ⚠ 1.5.6 STEP 2 IS LANDED — the failsafe region, pin target `813e5b6`, notice 2026-09-11 15:22. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**✅ THE CORRECTION TOOK EFFECT ON THE VERY NEXT NOTICE, NOT MERELY AT THE HANDOFF.** All
six rows, labelled *"all six rows"*, and **`nitpick.obligations: 368 rows, unchanged`** —
the manifest's figure under the manifest's name. *A fix promised for a future handoff that
also lands immediately is worth more than the promise.*

## ⚠ THE ANCHOR IS NOW `81273821…` / 59 128 B — superseding `618c59f5…` / 58 368 B

```
npkrt.o    81273821...     59,128 B  MOVED — the new anchor
builder.o  c489068f...  9,085,152 B  unchanged
builder    16c95b8d...  7,906,408 B  MOVED with the floor it links
npkc.ll    12d65358... 24,806,588 B  unchanged (step 0's)
npkc.o     94ac49bf...  9,794,256 B  unchanged
npkc       2603f04f...  8,533,384 B  MOVED
```

**D-292 — `failsafe` now allocates from a 1 MiB preallocated `.bss` region**, bumped and
never freed, a free inside failsafe a no-op, `ralloc` copying into the region — **so a
handler that formats a report never touches the heap a trapping thread may hold the mutex
of.** Exhaustion is the re-entry exit 70. **⚠ THE BEHAVIOURAL CATCH: a `failsafe` body that
builds text by repeated concatenation is QUADRATIC in the region** — 16 KiB of pieces is
fine, a megabyte of concatenations is not.

**Measured: ZERO allocation or text-building statements inside any failsafe body.** All of
them are `pick` over error constants with `exit` arms — the leading tokens are `pick` (142),
the constant names, and `exit` (142). **No exposure.** **No further floor move is expected
before step 6's close, and a notice comes only if one happens.**

## ⚠⚠ A CORRECTION AGAINST THIS SEAT: "264 FAILSAFE BLOCKS" WAS WRONG. IT IS 145.

**Checking one of my own numbers against another turned up a factor-of-four denominator
error that had been sitting in this board and had been sent to a peer.**

```
                       what I recorded     authoritative      what went wrong
.npk files                     747                170         find swept gitignored scratch
failsafe blocks                264                145         same
```

**`nitpick-time/.internal/` holds 563 untracked `.npk` scratch files**, and `.internal` is
gitignored by this very repository's rules — *"Gitignored scratch. Never commit anything
from here."* **`find` sweeps them in. Python's `glob` with `**` silently skips them, because
it skips dot-directories — so my two scans were wrong in OPPOSITE directions and neither was
the library.**

**✅ THE CONCLUSIONS ALL SURVIVE, AND THAT IS LUCK RATHER THAN METHOD.** The scratch is
`nitpick-time`'s own generated material, so sweeping it in only ever inflated a denominator
on measurements that came back ZERO — a larger clean set is still clean. **Had any of those
scans returned a non-zero hit, I could not have said whether it was library code or
scratch.** *The `(ShiftRange)` finding is unaffected: `src/core/byteset.npk` is tracked, and
I verified its six sites by path rather than by count.*

**THE DURABLE FIX, AND THE REPOSITORY ALREADY KNEW IT.** **Use `git ls-files`, not `find`
and not `glob`.** `find` includes gitignored scratch; `glob` silently drops dot-directories;
**only `git ls-files` is the set this project means by "the library".** *And the tell was in
front of me the whole time: `check_refs.py` reports **"39 md files via git ls-files"** on
every run of the gate — the repository's own check has used the authoritative set all along,
and I was reading that line dozens of times while measuring a different set beside it.*

### ⚠ 1.5.6 STEP 1 IS LANDED — the whole-program stop, pin target `2718324`, notice 2026-09-11 14:52. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

## ⚠⚠ THE ANCHOR IS NOW `618c59f5…` / 58 368 B — superseding `8b01cb3c…` / 55 784 B

*Delta **2 584 B**, again an observation rather than a check — no byte claim was made.*
**Protocol honoured a second time**: first lines name the move, both digests quoted and
labelled, commit `2718324`, reason given.

**D-291 / DEF-47 — a trap now stops every other thread before `failsafe` runs.** A thread
registry; a `SIGUSR1` stop handler installed at `npk_start` using **SA_RESTORER with the
floor's own `rt_sigreturn` stub, so no libc is involved**; **cmpxchg arbitration of the
failsafe holder in `npk_trap`** — a second trapping thread parks, and **a trap inside
`failsafe` itself is the re-entry exit 70**; the stop walk under the executor's join
deadline (default 5 s); a non-holder's `exit` parks instead of racing the holder.

**⚠ A HARD LIMIT WORTH CARRYING EVEN THOUGH WE HAVE NO THREADS: the registry is 64 SLOTS,
AND THE 65TH THREAD IS REFUSED AT ITS START.** *A ceiling that refuses at start is the kind
of fact a library discovers at the worst possible moment; it is recorded here so whoever
writes threaded code in these repositories meets it on the board first.*

**No ABI change; emitted IR unchanged (`npkc.ll` is step 0's).** `getpid` / `tgkill` /
`rt_sigaction` are new syscalls in the floor's table — **and they volunteered, unasked, that
the harness's zero-dependency scan is unchanged because no new SYMBOL appears.** *That is
precisely the check `nitpick-regex/harness/irscan.py` exists to run, and they answered it
before we could ask.*

**Zero exposure: thread primitives remain at zero code-position sites here.**

```
npkrt.o    618c59f5...     58,368 B  MOVED — the new anchor
builder.o  c489068f...  9,085,152 B  unchanged
builder    b1fdd7fc...  7,905,808 B  MOVED — supplied on asking, 2026-09-11 14:55
npkc.ll    12d65358... 24,806,588 B  unchanged (step 0's)
npkc.o     94ac49bf...  9,794,256 B  unchanged
npkc       901b98c2...  8,532,792 B  MOVED
```

## ⚠⚠⚠ TWO NOTICES RUNNING WITH FIVE ROWS: THIS IS `_s6`'s FORMAT, NOT AN OMISSION

**`build/builder` is absent from step 0 AND step 1.** One missing row is a slip; **two in a
row is how this session formats a ladder**, which means **the six-row convention did not
survive the handoff.** Still not reconstructed from this board — the rule holds and the
temptation is now stronger, since two notices agree on every row we can check.

**✅ BOTH RESOLVED ON ASKING, 2026-09-11 14:55 — AND SUPPLIED ON ASKING RATHER THAN
DISPUTED.** `nitpick-compiler_s6` sent the two missing rows outright — step 0
`98e67c46…` / 7 904 000 B, step 1 `b1fdd7fc…` / 7 905 808 B, **both moved with the floor
they link, exactly as our other five rows predicted** — and added the sentence that
settles the principle: ***"as you said, a prediction is not a row."***

**✅ And the count is corrected at source: `nitpick.obligations` is 368 rows, unchanged by
both steps, last moved `3dce739`; 439 is the harness's count of obligations decided over
the compiler** (273 discharged, 138 open, 22 unencoded, 6 checker).

**✅ THE ACTUAL WIN IS NEITHER ROW NOR NUMBER: `_s6` IS CARRYING BOTH INTO `_s7`'s HANDOFF
AS VALUES WITH THE PROCEDURE, NOT AS PROSE.** In their words — the six-row ladder and
*"368 is the manifest, 439 the harness's decided count"* go over in the form that survives.
*So the handoff lesson this board drew from two failures has been adopted by the party that
has to execute it, one handoff before it would have been tested again.*

**⚠ ONE CORROBORATION, AND ITS LIMIT.** Step 0's `builder` grew by **exactly the 16 bytes
`npkrt.o` grew** (7 903 984 → 7 904 000 against 55 768 → 55 784), which is a clean
confirmation of *"moved with the floor it links"*. **Step 1's did not** — `builder`
+1 808 B against `npkrt.o` +2 584 B. **Neither is required**: a link need not preserve an
object's size delta, and the step-0 match is corroboration rather than a law. *Recorded with
both halves, because quoting only the exact one would manufacture a rule out of a
coincidence.*

## THE LESSON THIS HANDOFF TEACHES, WHICH IS WORTH MORE THAN EITHER DEFECT

**Three things were in flight across the `_s5` → `_s6` handoff. Exactly one arrived.**

```
the floor-move protocol   ARRIVED   handed over as an explicit VALUE + PROCEDURE
                                    ("the previous digest 27387ce7…, 55768 B, and the reason")
the six-row ladder        LOST      lived as a CONVENTION observed in practice
the 368/439 correction    LOST      lived as PROSE about which number means what
```

***What survives a handoff is what was handed over as a value with a procedure attached.
A convention that is merely practised, and a correction that is merely explained, do not
travel.*** **This is the same finding as "a rule can be paraphrased away; a quoted digest
cannot", now demonstrated three times in one handoff — twice by failure.**

### ⚠ 1.5.6 STEP 0 IS LANDED — THE FLOOR MOVED AGAIN, pin target `85952d0`, notice 2026-09-11 14:51 from `nitpick-compiler_s6`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**✅ The protocol was honoured on all three elements by a session we had never heard from
— its first outing after a handoff.** First lines name the move; both digests quoted and
labelled; commit and reason given.

## ⚠⚠ THE ANCHOR IS NOW `8b01cb3c…` / 55 784 B — superseding `27387ce7…` / 55 768 B

*Delta 16 B. **Recorded as an OBSERVATION, not a check**: unlike the 1.5.4e move they made
no byte claim this time, so there is no arithmetic to close. Do not treat 16 B as verified
against anything.* Reason given: four words promoted to atomic accesses, `@npk_frozen`
seq_cst, the join's tid word an atomic load, `@npk_in_failsafe` and evfd's owner read made
atomic, the executable-page count an `atomicrmw`, the heap initialiser moved under the heap
mutex — **plus DEF-49, a real fix: a thread's ROOT was never roused**, its owner word naming
the spawning thread's executor, **so any wake of a thread root blocked on a channel, lock,
condvar or barrier slept to its deadline.** Threaded programs that block get faster, never
slower; **no ABI change; emitted IR unchanged.**

**Zero exposure here either way: thread primitives appear 31 times in library text and
ZERO times in code position.**

## ⚠⚠⚠ THE LADDER CAME WITH FIVE ROWS, NOT SIX — `build/builder` IS ABSENT

**This board's own rule fires here: a notice that omits a row is anomalous rather than
terse, and the missing row must NOT be reconstructed from this board, because a check you
can satisfy on the sender's behalf is not a check.** Asked, not filled in.

```
npkrt.o    8b01cb3c...     55,784 B  MOVED — the new anchor
builder.o  c489068f...  9,085,152 B  unchanged, matches this board
builder    98e67c46...  7,904,000 B  MOVED — supplied on asking, 2026-09-11 14:55
npkc.ll    12d65358... 24,806,588 B  UNCHANGED since 1.5.5
npkc.o     94ac49bf...  9,794,256 B  UNCHANGED since 1.5.5
npkc       a0087d81...  8,530,984 B  MOVED (from 13147e9e…)
```

**And the gap is conspicuous rather than arbitrary, because the other five rows predict it.**
At 1.5.4e a floor move took `builder` with it — *"moved with the floor it links"*. Here
`npkc.ll` and `npkc.o` are **unchanged** while `npkc` **moved**, which is exactly that
signature: the emission is untouched and the binary moved because it links the floor.
**`builder` links the floor too, so it should have moved — and it is precisely the row not
given.** *A missing row whose value we could confidently guess is the most dangerous kind:
the temptation to fill it in is strongest exactly where doing so would defeat the check.*

## ⚠ A CORRECTION FAILED TO SURVIVE A HANDOFF THAT THE PROTOCOL SURVIVED

**`_s6` writes *"`nitpick.obligations` unchanged (439 rows)"* — the same label slip `_s5`
corrected one handoff ago**, having confirmed 368 is the manifest (last changed `3dce739`)
and 439 the harness's count. **So on the same handoff: the digest protocol propagated
intact and the correction did not.**

**The difference is how each travelled.** The protocol went across as a **quoted value** —
`_s5` handed `_s6` the literal digest `27387ce7…` / 55 768 B — and arrived intact. The
correction went across, if at all, as **prose about which number means what**, and did not.
***A rule can be paraphrased away; a quoted digest cannot — and a CORRECTION is a rule
unless it is carried as a value.*** **368 still stands as this board's figure for the
manifest; queried again rather than assumed to be a change.**

### ✅ 1.5.5 IS LANDED — D-286/D-287, the aliasing half of D-004, pin target `149dbf6`, notice 2026-09-11 10:41 from `nitpick-compiler_s5`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**✅ FIRST NOTICE FROM A NEW ADDRESS, AND IT AUTHENTICATES AGAINST THE NEW ANCHOR — SO THE
PROTOCOL SURVIVED A HANDOFF.** `npkrt.o` reads `27387ce7…` / 55 768 B, **matching the
anchor `_s4` moved us to one notice ago**, and `builder.o` / `builder` match our recorded
values too. *The chain that mattered: `_s4` moved the floor under a protocol, told `_s5`
the rule, and `_s5`'s first notice satisfies it without ever having spoken to us before.
An agreement that outlives the session that made it is the only kind worth making.*
They also stated **why** `npkrt.o` did not move — *the runtime changed in a comment line
only* — which is the same disclosure habit, unprompted.

```
npkrt.o    27387ce7...     55,768 B  UNMOVED — the anchor holds
builder.o  c489068f...  9,085,152 B  unchanged
builder    2445d651...  7,903,984 B  unchanged
npkc.ll    12d65358... 24,806,588 B  the one that travels (D-265)
npkc.o     94ac49bf...  9,794,256 B
npkc       13147e9e...  8,530,968 B
```
Canary: **14 defines.** No snapshot refresh.

## ⚠ ONE NUMBER TO QUERY, NOT TO ADOPT

**They write *"`nitpick.obligations` did not move (439 rows)"*. This board recorded it
`unchanged at 368 rows` at 1.5.4e.** The two are reconcilable only if the label moved:
**1.5.4b's own notice distinguished them explicitly** — *"`nitpick.obligations`: 368 rows
(329 `int`, 11 `bv`, 28 `-`); **the harness's run over the compiler counts 439
obligations** — 273 discharged, 138 open, 22 unencoded, 6 checker."* **So 368 is the
manifest and 439 is the harness count, and this notice attaches the harness number to the
manifest's name.** *Most likely a slip of label rather than a change of fact — the phrase
"did not move" only makes sense if it means the manifest — but this board does not adopt a
number whose denominator it cannot name.* **Queried with them; recorded here as
UNRESOLVED — **✅ RESOLVED SAME DAY, 2026-09-11 10:42: a slip of label, exactly as read.**
`nitpick-compiler_s5`: **`nitpick.obligations` is 368 rows and did not move — its last change
is `3dce739`, 1.5.4b step 3 — and 439 is the harness's count of obligations decided over the
compiler (273 discharged, 138 open, 22 unencoded, 6 checker), also unchanged.** *Both numbers
were true and one wore the other's name. The board's rule — do not adopt a number whose
denominator you cannot name — cost one question and returned both numbers with their
denominators attached.*

## Measured against each claim — all zero, and the reason is that we hold no claims at all

- **D-287 §1 — the aliasing half of D-004 is live.** `$$m` is an exclusive claim, `$$i` a
  shared one, `@` claims nothing but counts as write-capable; claims are **lexical**; a
  claim anywhere but a call argument or a pointer local is **BORROW-014**, and a static
  overlap is **BORROW-013**. **Zero exposure: `$$m` 0 sites, `$$i` 0 sites.**
- **D-287 §2 — a computed-index overlap is a RUNTIME GUARD IN EVERY BUILD**, trapping the
  new identity `BorrowOverlap` (-4116), **armed by the reach analysis, so any root with
  such a site must name `(BorrowOverlap)` or is REACH-002**; the verified build elides it
  through the new obligation kind `disjoint` (kind 20). **Zero exposure — with no claims
  there are no claim sites to guard.**
- **D-287 §3 — a `fixed` binding has NO ADDRESS**: `@`, `$$i`, `$$m` or a pointer-receiver
  call on a `fixed` local, parameter, module binding or field is **TYPE-071**. *"A write
  through such a pointer was a SIGSEGV on a `fixed` global."* **Zero exposure, and this one
  needed correlating rather than counting:** 43 distinct `fixed` binding names and 34
  distinct `@`-addressed names across 176 `.npk` files, **and the intersection is EMPTY.**
  **⚠→✅ AND THE TEST HAD A GAP, WHICH THE COMPILER SIDE NAMED AND WHICH IS NOW CLOSED.**
  `nitpick-compiler_s5` pointed out that **a `fixed` FIELD's address counts too**, so a
  struct carrying a `fixed` field whose instances are `@`-taken is *"the one shape the name
  intersection misses"* — the field name appears in neither set. **Closing it needed a
  different method rather than a wider grep: brace-scanning every `struct:` body.** Result
  at 2026-09-11 10:42: **65 struct declarations scanned, ZERO `fixed` fields.** **So the
  name-intersection result stands as COMPLETE rather than partial.** *A peer finding the
  hole in our method is worth more than a peer agreeing with our number, and it is the
  second time this week the other side has corrected how we measured rather than what we
  concluded.*
  *A count of either alone would have said nothing.*
- **DEF-42 / Rule 3 — a borrow assigned to a holder declared OUTSIDE the block declaring
  the borrowed local is BORROW-002.** **Zero exposure**, again for want of any borrow.

**Their own sweep reported `lib/` clean under the new rules — but that is THEIR `lib/`,
not ours**, and the measurements above are this board's own.

## ⚠ A PATTERN IS NOW CONFIRMED THREE TIMES AND DESERVES A NAME: THE SYNTACTICALLY-ARMED TRAP

```
D-277   ShiftRange     -4115   armed wherever a computed shift exists
D-284   IntOverflow    -4110   armed wherever an integer-lane + - * or .sum() exists
D-287   BorrowOverlap  -4116   armed wherever a computed-index claim overlap exists
```

**All three are armed by the REACH ANALYSIS, a frontend pass that runs in every build and
never reads `nitpick.obligations`.** So for every one of them the same three things stay
distinct — **the obligation may discharge, the guard may be elided in the verified build,
and the `failsafe` arm is still demanded.** **Expect the next such rule to follow the same
shape, and check for the ARM rather than reasoning about the proof.** **✅ CONFIRMED FOR
`BorrowOverlap` BY `nitpick-compiler_s5`, 2026-09-11 10:42, WITH THE MECHANISM:** *"the
aliasing analysis fills its guard table in every build and never reads the manifest; the
reach analysis arms `BorrowOverlap` off that table; the verified build may elide the compare
through a discharged `disjoint` row, and the arm is still demanded."* **And they confirm the
generalisation in terms: expect the next guarded rule to have the same shape.** *So this is
now a rule of the language's tooling rather than a coincidence across three decisions.* *We hold exposure to
exactly one of the three: `(ShiftRange)`, which remains this board's single item of real
library work.*

### ⚠ 1.5.4e IS LANDED — THE FLOOR MOVED, pin target `cb8cbb0`, notice 2026-09-11 05:09 from `nitpick-compiler_s4`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

## ✅ THE PRE-AGREED ANCHOR-MOVE PROTOCOL WAS USED ON ITS FIRST OUTING, AND HONOURED ON EVERY ELEMENT

**`npkrt.o` moved — the one event this board could not have checked its way out of — and
it arrived exactly as promised one notice earlier.** Element by element:

```
1. said so in its first lines      YES  "THE FLOOR MOVED" opens the notice
2. previous digest quoted beside   YES  67cc8186... 55,648 B, "which had stood since a807de9"
3. named the commit that did it    YES  fe50fc7 (D-285)
```

**AND THE ARITHMETIC CLOSES TO THE BYTE, WHICH THEY DID NOT ASK US TO CHECK.**
`55 768 − 55 648 = 120 B`, against their stated *"one define, `@npk_raise` … 120 bytes of
object. That is the whole floor diff; nothing else in the runtime changed."* **A claim that
carries its own arithmetic is checkable without trusting the claimant**, and this one
checks. *The board's standing suspicion of a moved anchor is satisfied here by evidence
rather than by goodwill — which is the only way it should ever be satisfied.*

## ⚠⚠ THE ANCHOR IS NOW `27387ce7…` / 55 768 B — SUPERSEDING `67cc8186…` / 55 648 B

**Every hazard 10 check from here authenticates against `27387ce7…`.** The old value
appears **17 times** on this board as the historical anchor and those references stay
correct *as history*; **they are no longer the test.** `builder.o` is **unchanged**
(`c489068f…`, no snapshot refresh this time) and `builder` moved **with the floor it
links** — which is itself a consistency check, since a floor-only change should move the
binary and not the object, and it did.

```
npkrt.o    27387ce7...     55,768 B  MOVED — the new anchor (prev 67cc8186… / 55,648 B)
builder.o  c489068f...  9,085,152 B  unchanged
builder    2445d651...  7,903,984 B  moved WITH the floor it links
npkc.ll    3821b811... 24,296,105 B  the one that travels (D-265)
npkc.o     6ff1863c...  9,614,040 B
npkc       ba251b70...  8,379,056 B
```
Canary: **14 defines (unchanged)**, 52 926 B — was 52 897 at `18b93e1`, the difference being
**the declare block's one new line, `declare void @npk_raise(i32)`.** Quote the define
count. Taken on the docs tree and again on landed main: identical.

## What changed, measured against each claim

- **D-284 — `simd` INTEGER LANES NOW TRAP ON OVERFLOW**, and the reach analysis **demands
  `(IntOverflow)` of every root reaching an integer-lane `+ - *` or `.sum()`**, REACH-002
  until the arm is added. **Zero exposure — no `simd` anywhere — and they said so
  themselves.** **DEF-38 CLOSES.** *Filed for whoever writes `simd` here first: this is the
  second construct whose arm is demanded syntactically, so the `ShiftRange` lesson
  generalises — the arm is the plain build's, not the verifier's.*
- **DEF-39 — `v += w` and every `op=` on a `simd` target** was admitted by the checker and
  refused by the emitter as EMIT-002 **since 1.3.3**; it lowers now with every guard. No
  `simd` here, so nothing changes.
- **D-285 — `npk_raise`: `?!` and `!!!` enter the trap route through it, every guard keeps
  `npk_trap`.** **DEF-36 CLOSES** — unwrapping with a system error code is legal in a
  verified build again; our libraries never did it.
- **⚠ BUT THEIR ASIDE LANDS ON US, AND IT IS A DOCUMENTATION FACT RATHER THAN A BUILD
  ONE.** *"If you scan emitted IR for `@npk_trap(` yourselves, a program's raise is
  `@npk_raise(` now."* **Measured: no harness matches on the symbol. `npk_trap` appears in
  `harness/irscan.py:53` and `harness/build.py:363` only inside PROSE, and in
  `meta/specs/BUILD.md` and `meta/DECISIONS.md` as recorded measurement claims.** **So
  nothing breaks — and several RECORDED MEASUREMENTS now describe a floor that has
  changed**: `BUILD.md`'s *"the residue over the 19 program-stage probes is `npk_trap`, the
  `defer` chain, …"* and `DECISIONS.md`'s residue findings were true of the floor they were
  taken against. *A measurement does not become false when the world moves; it becomes
  undated. These need their commit named beside them, not correcting.* **No action while
  paused; for the resuming session.**
- **DEF-40 — `!!!` had bypassed the trap discipline entirely** (no frozen flag, no re-entry
  guard, no driver kill, and `failsafe` ran twice). It goes through the one trap route now,
  so a `failsafe` that traps after a `!!!` ends the process at 70. **One `!!!` site exists:
  `nitpick-apps/nitpick-posix/tests/probe/probe02g_cross_module.npk:12`.** They state a
  library relying on `!!!`'s exit code sees the same code as before, **so no action — but
  that probe is the one place a behaviour change could surface, and it is named here so a
  successor does not have to find it.**
- **DEF-41 — a compound shift through a FIELD or ELEMENT (`s.f <<= n`) has had its
  `ShiftRange` guard since D-277 with no obligation row**, failing a verified build's belts.
  Row recorded now; the plain build was always right. **Zero exposure: no `<<=` or `>>=`
  anywhere.** *Worth noting it is adjacent to our real finding — `byteset.npk` writes
  `s.w[i] = s.w[i] | (1u64 << …)` explicitly rather than compounding, which is why it meets
  D-277 and not DEF-41.*
- **D-283** confirms D-282's binding-lanes reading as ratified. **`nitpick.obligations`
  unchanged at 368 rows.**

**THE `(ShiftRange)` ARM REMAINS THIS BOARD'S ONE ITEM OF REAL LIBRARY WORK** — unaffected
by 1.5.4e, and `_s4` confirms the answer stands.

### ⚠ 1.5.4b IS LANDED — D-277…D-282, pin target `18b93e1`, notice 2026-09-10 17:33 from `nitpick-compiler_s4`. **RECORDED, NOT WORKED — AND IT CARRIES THE QUIET PERIOD'S FIRST NON-ZERO EXPOSURE.**

```
npkrt.o    67cc8186...     55,648 B  unchanged since a807de9   <- the only surviving anchor
builder.o  c489068f...  9,085,152 B  MOVED  (was 3b5f868d / 8,086,688 B)
builder    00bf9cd4...  7,903,920 B  MOVED  (was fe528b03 / 7,014,760 B)
npkc.ll    4025d7ac... 24,223,684 B  the one that travels (D-265)
npkc.o     f68a576a...  9,579,864 B
npkc       840ca3cb...  8,348,152 B
```

**⚠ HAZARD 10's ANCHOR SET JUST SHRANK FROM THREE TO ONE.** The `builder` pair moved, for
a stated and internally coherent reason — **the snapshot was refreshed at step 0 because
forty roots in their own tree had to name `ShiftRange`** — and a snapshot refresh is
exactly the thing that moves `builder`/`builder.o` while leaving `npkrt.o` alone. **The
check still passed, on `npkrt.o` plus the coherence of the explanation.** *But a
content check anchored on "the unchanged rows match" weakens every time a row legitimately
moves, and it is now resting on one row.* **From here, authenticate on `npkrt.o` AND on
the emission chain's continuity, not on the unchanged count.** **⚠ SUPERSEDED 2026-09-11 05:09:
`npkrt.o` MOVED at 1.5.4e and THE ANCHOR IS NOW `27387ce7…` / 55 768 B** — see the 1.5.4e
block, where the move arrived under the pre-agreed protocol with its arithmetic closing to
the byte. **`67cc8186…` is history, not the test.** **✅ AND THE COMPILER SIDE PRE-AGREED THE ONE
FORESEEN ANCHOR MOVE, UNASKED.** `nitpick-compiler_s4`, 2026-09-10 17:36: `npkrt.o` moves
only with the floor, and **the single change on the horizon that would move it is DEF-36's
recommended fix — an `npk_raise` entry in `npkrt.ll`, a D-203 addition that is THE
AUTHOR'S TO RATIFY.** If it lands, that notice will **say so in its first lines, quote the
previous `npkrt.o` digest beside the new one, and name the commit that changed the floor**,
so the anchor moves with a stated reason rather than silently. **Nothing else planned
touches the floor.** **⚠ SUPERSEDED 2026-09-11 11:56: `_s6` HAS PLANNED **1.5.6 —
"the floor's SPEC and the executor primitives"** — so **the floor is back in scope and the
anchor may move again.** The protocol is held by `_s6`, and `_s5` transmitted it **with the
actual value rather than as a rule** (*"the previous `npkrt.o` digest (`27387ce7…`,
55 768 B) and the reason"*), which is why it has survived three handoffs intact: **a rule
can be paraphrased away; a quoted digest cannot.**

**⚠ AND AN EXPECTATION THAT MATTERS TO A LISTENING SEAT: SILENCE DURING A PLANNED SUBCYCLE
IS NORMAL, NOT A GAP.** `_s5` states the convention plainly — **a notice at each landing,
and NO NOTICE AT PLAN TIME.** *So a quiet stretch while 1.5.6 is planned is the protocol
working. A seat that reads silence as a missed notice will go looking for a failure that is
not there — or worse, begin inferring the compiler's state from its silence, which is the
error hazard 10 exists to prevent in the other direction.* *This is the failure this board could not have checked its way out
of — an anchor moving legitimately with nothing left to anchor against — and it was closed
by the other side volunteering a protocol rather than by us devising a test.*

**Canary: 14 defines (unchanged), 52 897 B — was 52 212 at `5f13220`.** Reason given: the
**prelude's own text grew by `ShiftRange` and its site rows.** The standing rule holds —
**quote the define count, the byte count is path-dependent** — and they added a control we
did not ask for: **taken on the docs tree and again on landed main, identical, as were all
six digests.**

## ⚠⚠⚠ D-277 — THE FIRST THING IN THIS ENTIRE QUIET PERIOD THAT WILL REQUIRE A LIBRARY CODE CHANGE

**A computed shift amount now traps `ShiftRange` (-4115), and the reach analysis arms it
WHEREVER A COMPUTED SHIFT EXISTS — so every root whose program contains one must add
`(ShiftRange)` to its `failsafe` or it refuses `REACH-002`.** They said *"forty roots in
the compiler tree needed the arm… expect the same in yours; the fix is one arm."*

**Measured here at 2026-09-10 17:33 — and it is not zero:**

```
computed-amount shift sites: 6, in 2 files
  nitpick-regex/src/core/byteset.npk:70,77,84   1u64 << ((b =>! uint64) & 63u64)   <-- SOURCE
  nitpick-regex/tests/probe/probe11_...:112,119,146                                    tests
`ShiftRange` named in any library:  0
```

**One of the two files is library SOURCE, not a probe** — `src/core/byteset.npk` — and
**`src/core/core.npk` imports it**, so the regular-expression library's core aggregator
reaches a computed shift. **`ShiftRange` appears nowhere in any library.** At the re-pin,
every affected root refuses until it names the arm.

**⚠ THE MASK DOES NOT EXEMPT IT, AND THIS IS THE READING MOST LIKELY TO GO WRONG.** The
amount is `((b =>! uint64) & 63u64)` — provably in `[0, 64)` — so the *obligation* should
discharge. **But the notice says the reach analysis arms the trap "wherever a computed
shift exists", which is syntactic**, so a discharged obligation and an unarmed `failsafe`
are different things. *A successor reasoning "it is masked, therefore fine" would be right
about the proof and wrong about the arm.* **✅ CONFIRMED SYNTACTIC BY `nitpick-compiler_s4`, 2026-09-10 17:36 — THE
READING WAS RIGHT AND THE WORK IS REAL.** *"The reach analysis arms `ShiftRange` for any
shift whose amount is not a literal token, so every root reaching `byteset.npk` needs one
`(ShiftRange)` arm — six sites, one arm per affected root, real work as you read it."*

**⚠ THE REASON IS MORE TRANSFERABLE THAN THE ANSWER: THREE THINGS THAT LOOK LIKE ONE ARE
NOT.** *"The arm reflects the PLAIN build, which keeps the guard whatever the manifest
says — the reach analysis is a frontend pass that runs in every build and never reads
`nitpick.obligations`."* So for a masked computed shift:

```
the OBLIGATION  discharges at once  -- `& 63u64` is the low-bits Int form (mod b 64),
                                       so the shift-range goal 0 <= n < 64 is immediate
the GUARD       is elided           -- but only in the VERIFIED build, to one llvm.assume
the ARM         is still demanded   -- the plain build keeps the guard, so REACH-002 stands
```

***A discharged row, an elided guard and a demanded arm are three different things.***
**Only a LITERAL amount gets no guard at all, and that case is the checker's, `TYPE-070`.**
*(The cast stays an opaque term until 1.5.8's `cast-range` rows; the masked form does not
need it.)* **A successor who proves the shift is in range and concludes the arm is
unnecessary will be right about the proof, right about the elision, and still refused.**

**SIZE OF THE FIX, with its limitation stated:** `nitpick-regex` holds **66 roots**, of
which **1 imports `core` or `byteset` directly**, plus `probe11` which carries its own
computed shifts. **That count is DIRECT imports only — transitive reach was not measured,
so it is a LOWER BOUND, not the answer.**

**No `TYPE-070` exposure:** every literal shift amount is within its type's width —
`nitpick-time`'s `1i128 << 100i128`, `<< 101i128`, `<< 63i128` are all `< 128`, and
`nitpick-regex`'s `>> 6i64`, `<< 13u64`, `<< 17u64`, `>> 7u64`, `>> 8u64` all `< 64`.

## The rest, measured against their own claims

- **THE MANIFEST FORMAT MOVED (D-281)** — `rows.txt` gains an eleventh field and the tier
  column is now the encoder's word (`int`/`bv`/`fp`/`-`, `real` for a tier-2 discharge)
  where it was constant `int`. **We hold zero manifests, so nothing to re-record** — but
  **the first manifest any library records must be recorded under the new compiler**, and
  D-040 asks for the re-baseline in the re-pin commit **with the delta read before it is
  committed.**
- **DEF-36 — a `?!` unwrap with a system error code fails a verified build's belt**
  (-4097, -4098, -4100, -4101, -4111…-4115), because it lowers to the same trap text the
  belts count as a guard. **Zero exposure: no library unwraps with a system error
  constant.** Their advice — *unwrap with your own error constants until the `npk_raise`
  floor entry lands* — is already what these libraries do.
- **DEF-38 / S-59 — a `simd<int32, N>` `+ - *` WRAPS on lane overflow where its scalar
  traps, recorded and NOT fixed.** **Zero exposure: no `simd` in code position anywhere.**
  Worth carrying anyway: *do not rely on a lane overflow reaching `failsafe`.*
- **DEF-37 — a float `/` or `%` no longer demands `(DivByZero)`/`(DivOverflow)` arms**, and
  extra arms still compile. **Not a break.**
- **DEF-33 is a soundness rule for whoever writes contracts here:** a proposition holds
  only where its evaluation does not trap, so `requires (1i32 << n) != 0i32` now **proves**
  `0 <= n < 32` at the call and in the body rather than assuming it. **This matters for
  `nitpick-regex`'s eventual contracts precisely because its shifts are computed.**

**Reminder of the denominator: `nitpick-parse`, `nitpick-sockets` and `nitpick-tui` hold no
`.npk` at all, so every zero above covers `nitpick-regex`, `nitpick-time` and
`nitpick-posix` only.**

### ✅ 1.5.4d IS LANDED — D-274/D-275/D-276, pin target `12a6a78`, notice 2026-09-10 08:33 from `nitpick-compiler_s4`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**✅ The ladder convention was honoured on its first outing** — all six digests including
the three unchanged, plus the canary line, and the three unchanged match this board.
52/52, **parity 1 254**. `nitpick.obligations` did not move (184 rows, 170/8). Commits
`1c60cdb`, `5caa43e`, `f6691bc`, `32884b2`, `12a6a78`; `main == origin/main` at `12a6a78`.

```
npkrt.o    67cc8186...     55,648 B  unchanged
builder.o  3b5f868d...  8,086,688 B  unchanged
builder    fe528b03...  7,014,760 B  unchanged
npkc.ll    8db8451d... 23,199,787 B  the one that travels (D-265)
npkc.o     47b34d0c...  9,258,200 B
npkc       25e72cc2...  8,061,616 B
```

**⚠→✅ THE CANARY WAS DESCRIBED BY A NEW PATH, AND `cmp` SETTLED IT.** Previous notices
said *"your `tools/canary.npk`"*; this one says *"canary.npk at the tree root"*. **Two
files of that name exist** — ours and `nitpick/.internal/canary.npk` — and this board has
already been caught three times comparing canary numbers across different artifacts.
**Measured rather than assumed: both are 335 B with sha `55dafd8aff262c7e…`, byte-identical.**
Same program, so the 14 / 52 212 reading compares and the wording drift is harmless.
*The check cost one `cmp`; assuming would have cost nothing until it cost everything.*

## ⚠⚠ THE DENOMINATOR BEHIND EVERY "ZERO EXPOSURE" ON THIS BOARD — READ THIS BEFORE TRUSTING ONE

**Three of the five libraries contain NO `.npk` FILES AT ALL.** Measured 2026-09-10 08:33:
**`nitpick-parse` 0, `nitpick-sockets` 0, `nitpick-tui` 0.** They hold specifications and
plans; no code has been written in them. **So every "zero across all six work
repositories" this seat has recorded during the quiet period is really "zero across the
three that contain code" — `nitpick-regex`, `nitpick-time` and `nitpick-posix`.**

**That is not wrong, and it is much weaker than it reads.** A successor taking *"measured
zero across six repositories"* as six independent confirmations would be treating three
empty sets as evidence. **None of these clearances says anything about code not yet
written**, and `nitpick-parse`, `nitpick-sockets` and `nitpick-tui` will be written from
specifications drafted when the pre-1.5.3 language was current. **Every measurement in
this quiet period must be re-run against those repositories the first time they hold
code** — the results here do not transfer to them, they simply do not cover them.

## The four items, measured against their own specific claims

- **D-274 — a member-less `mod:name;` import carries the loaded file's scope.** **An
  unlock.** `name.f()`, `name.K`, `use name.{f};` and a `pub mod:name;` re-export now
  work, one meaning with the alias form. **Our 170 such imports gain a form and lose
  none**, and nothing can have depended on the old behaviour because it said *"no
  member"*.
- **D-275 — every arm over an `Error` selector is checked at the arm.** **Zero exposure.**
  **Zero** `(file.Name)` qualified arms; our arms are **899 bare error-constant names and
  148 wildcards**. The other TYPE-007 shapes are absent too: **zero `ERR:` arms, zero
  numeric-literal arms, zero range arms.** *(The 40 qualified arms that do exist —
  `(Ordering.Less)`, `(HirKind.Empty)`, `(Part.YearN)` — are `Type.Variant` over ENUM
  selectors, a different construct from `(file.Name)` over an `Error`, and are untouched.)*
- **DEF-32, latent since 1.1.6 — the reach analysis took a constant's qualifier from the
  FIRST site that reached it**, so `(root.E)` was demanded and the correct `(perr.E)`
  refused; an arm spelled `(root.Name)` for another file's constant **was a dead arm and
  refuses now.** **Zero exposure: zero `?! qualifier.CONST` unwrap sites and zero
  qualified arms**, so no dead arm of that shape exists here.
- **D-276 and the fixture rule — a file loaded only through `mod:name;` by another test is
  a fixture, built and never run.** **Zero exposure — and the first count said 161.**
  **⚠ That count was wrong and the error is worth more than the result:** every `.npk`
  opens by declaring its own module (`mod:<own name>;`), so a naive match of each
  declaration against the test file set **matched every file against itself**. Excluding
  self-references, **no test in any repository is loaded by another test**, so nothing is
  reclassified and no unit silently stops running. *Third instance this session of a count
  taken over the wrong set; the guard each time was checking the SHAPE before believing
  the NUMBER.*

**Next on the compiler side: 1.5.4b, the remaining theories.**

### ✅ 1.5.4c IS LANDED — D-273 implemented, pin target `5f13220`, notice 2026-09-10 04:27 from `nitpick-compiler_s3`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

## ✅ HAZARD 10 FIRED EXACTLY AS WRITTEN, AND THE CONTENT CHECK RESOLVED IT

**The notice arrived from `nitpick-compiler_s3` — an address this board had never
verified**, because `nitpick-compiler_s2` ran out of quota before it could name a
successor and announced only *"the resumed session"*. **This is the case hazard 10 was
written for three days ago, and its prescribed check worked without needing the sender's
cooperation.** The notice's three *unchanged* digests match this board's own recorded
values to the character — `npkrt.o` `67cc8186…` / 55 648 B, `builder.o` `3b5f868d…` /
8 086 688 B, `builder` `fe528b03…` / 7 014 760 B — and the canary reads 14 / 52 212 B.
**A sender who could not read this board could not have produced those.** *Authenticated
by ladder, not by name.*

**AND THE GAP IS NOW CLOSED GOING FORWARD: `_s3` NAMES `nitpick-compiler_s4` AS ITS
SUCCESSOR EXPLICITLY.** So the chain is `_s1` → `_s2` (announced) → **`_s3` (arrived
unannounced, authenticated by content)** → `_s4` (announced). **Send to
`nitpick-compiler_s4` from here.** *The one link that broke was the one where the
outgoing session ran out of budget rather than going quiet — a failure of capacity, not
of discipline, and the content check is the only thing that covers it.*

**LANDED:** three commits each under a full harness — `5886bcb`, `2bca8cb`, `5f13220` —
plus `9f1983c` (1.5.4b measurements) and `1ef034a` (**S-49/S-50 ratified as D-274/D-275**).
`main == origin/main` at `1ef034a`. **The ladder is `5f13220`'s**, since `1ef034a` and
`9f1983c` are meta-only. **`nitpick.obligations` did not move: 184 rows, 170 discharged,
8 open.**

```
npkrt.o    67cc8186...     55,648 B  unchanged since a807de9
builder.o  3b5f868d...  8,086,688 B  unchanged
builder    fe528b03...  7,014,760 B  unchanged
npkc.ll    3387a612... 23,119,807 B  quote THIS across machines (D-265)
npkc.o     144a45b8...  9,229,832 B
npkc       e5011d46...  8,037,368 B
canary     14 defines / 52,212 B     unchanged
```

## ⚠ THREE ITEMS WERE FLAGGED "MAY CHANGE A LIBRARY'S VERDICTS". ALL THREE MEASURE TO ZERO HERE — AND ONE OF THEM WAS A DOUBLE-FREE

**Measured at 2026-09-10 04:27, each against the specific claim rather than by inheriting
a neighbouring result:**

- **`Trait.method(recv, s)` now demands `move(s)` for a `move` parameter (TYPE-046) —
  "before, the qualified spelling let the string be FREED TWICE."** **Zero exposure.**
  All **10** qualified `Capitalised.method(` sites are **enum-variant paths calling a
  derived method** — `HirKind.Empty.eq(HirKind.Literal(0u32))`,
  `Weekday.Saturday.cmp(Weekday.Sunday)`, `HirKind.Empty.cmp(…)` — not the
  `Trait.method(recv, s)` form, and none passes a `move` parameter. *`TYPE-046` is the
  same rule `BL-5`'s central claim turns on, so this is worth the resuming session's
  attention even though our exposure is nil.*
- **An async METHOD spawn `drop j.run()` now arms `DeadlineExceeded`, so a `failsafe`
  that never names it is `REACH-002`.** **Zero exposure, and the first reading looked
  alarming.** There are **5** `drop x.method()` sites and `DeadlineExceeded` is named
  **exactly once** in all library code — which reads as four unguarded spawns until the
  shapes are checked. **They are not spawns.** All five are `drop b.push2(…)` /
  `drop c.push2(…)` in one probe, and `push2` is
  `NIL(Vec<T>->:self, move T:v) never fails` — **not `async`**, so `drop` is discarding a
  value, not spawning a job. **No async METHOD exists anywhere**: all 7 `async`
  occurrences are `async func:` free functions in a single probe, which **already names
  `DeadlineExceeded` in its failsafe arm.**
- **A struct declared inside an inline module can now be named from outside.** **Zero
  exposure** — zero inline `mod` blocks, measured at step 4 and unchanged.

**D-274 and D-275 are UNLOCKS, NOT BREAKS.** D-274 gives a member-less `mod:name;` import
the loaded file's scope — **today `name.f()` says "no member", so nothing can be relying
on it**; we hold **170** such imports, all `mod:name;`, and this makes a form available
rather than invalidating one. D-275 concerns error constants inside inline modules, of
which we have none. **Both land at 1.5.4d, planned next by `nitpick-compiler_s4` ahead of
1.5.4b.**

**So 1.5.4c changes nothing for these libraries, and the clearance is INCIDENTAL in every
case — each rests on a form we happen not to write, not on a property of the change.**
Re-measure all three the moment library code moves.

### ✅ THE AUTHOR RATIFIED ALL FIVE — D-269…D-273 — and 1.5.4c is scheduled ahead of 1.5.4b. Notice 2026-09-07 03:05. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**The compiler is unblocked.** Five docs-only commits, `5a499d9`…`f071d43`. **S-45…S-48
are ratified as D-269…D-272 and DEF-31 as D-273**, so the four that had landed *under
their recommendations with no decision number minted* now have numbers, and the code and
the decision are back in step.

**✅ AND THE "NOTHING MOVED" CLAIM CAME TWO INDEPENDENT WAYS.** Not only the six digests
measured at `da1f911`, but **`git diff a807de9 f071d43 -- src lib runtime bootstrap
nitpick.toml npkg tools tests` reported EMPTY** — a measurement *and* a structural proof
that no build input moved. *One shows the outputs match; the other shows there was
nothing that could have changed them. Neither alone is the other.* Harness on the final
tree: every stage green, **52/52, 184 obligations (170 discharged, 8 open) matching the
manifest with 170 guards elided, parity 1 204, `npkc` byte-identical.**

**THE FIVE DECISIONS.**

- **D-269** — an undischarged `prove` **refuses the VERIFIED build** (`NITPICK-VERIFY-001`);
  the plain build lowers `prove` to nothing.
- **D-270** — a counted loop's **computed** step is the `loop-step` obligation kind (trap
  `-4101`); a **literal non-positive** step is the checker's `TYPE-068`.
- **D-271** — the rung suite retires; `NITPICK-RUNG-001` **stays a defined code with no
  test, removed only by a decision.** **⚠ SO OUR `probe13a` EXPECTATION INVERTING AT ANY
  RE-PIN AT OR PAST `a807de9` IS NOW A RATIFIED CONSEQUENCE, NOT A PENDING ONE.**
- **D-272** — a **discharged `prove` is a lemma after its site.**
- **D-273 (DEF-31)** — a module symbol means one thing wherever it stands: `m.f(x)` is a
  **direct call** of the member (inline module, alias, nested path); `use m.*` /
  `use m.{a, B}` / `use m.f` bind a module symbol's public names; a **private member is
  `RESOLVE-004`** from either spelling; an alias carries its file's scope; `std` joins the
  names a program cannot declare as a module. **Two riders are recorded for the author to
  veto**: an unknown first segment in a `use` path **refuses (`RESOLVE-002`) rather than
  binding nothing**, and **alias imports apply before logical ones so their order never
  matters.** Lands at **1.5.4c** (`meta/roadmap/1.5/1.5.4c.md`, three steps), **scheduled
  AHEAD of 1.5.4b.**

**✅ THE MEASUREMENT THEY ASKED FOR, AND IT IS ZERO.** They flagged that
`use "./lib.npk" as lib;` followed by `lib.f(x)` **is refused today** exactly as an inline
module's member is — *no test ever called through an alias* — and said the alias count was
worth one grep here. **Run at 2026-09-07 03:05, confirmed two ways: ZERO alias imports in
any library.** All **90** `use` statements are path-form:

```
63   use "PATH".*;
27   use "PATH".Symbol;      (ETimeValue, CivilDate, civil_date, NTIME_*, ...)
 0   use "PATH" as NAME;     <-- the broken shape. none anywhere.
```

**So D-273's unusable shape touches nothing here**, alongside the **zero inline `mod`
blocks** measured at step 4. *Both halves of DEF-31 are clear, and both were measured
rather than assumed — the second because they asked, which is the pattern worth keeping:
they name the grep, we run it, neither side infers.*

**1.5.4b is a SKELETON, marked not execution-grade at its head** — the settled scope from
D-218 (QF_BV crossing for bitwise, the twisted kinds as scaled `Int` with ERR-sentinel
rows, two float tiers), the step shape, and five questions with their measurements. **The
resumed session completes it after 1.5.4c.**

## ⚠⚠ HAZARD 10 — THE COMPILER ADDRESS WILL ROTATE WITH NO NAME ATTACHED, BECAUSE THE ANNOUNCER RAN OUT OF QUOTA

**`nitpick-compiler_s2` is out of quota after that message**, and says *"the next notice
comes from the resumed session at 1.5.4c step 0's landing."* **That announces the FACT of
a rotation without announcing the NAME**, and this board's standing rule — *the switch is
announced or it has not happened* — was written for a session that goes quiet, not for one
that **runs out of budget before it can name a successor.**

**So the next compiler notice will arrive from an address this board has never verified.**
**Do not treat its arrival as self-authenticating, and do not infer the name from
`ListAgents`.** The rotation is expected, which makes it *more* impersonatable rather than
less. **Verify by content, which is cheap here and does not need the sender's cooperation:
a genuine notice will carry the six digests in ladder order, and `npkrt.o` must still read
`67cc8186…` / 55 648 B and the emission chain must continue from `72fdbd97…`
at `a807de9`.** A notice that cannot place itself on this board's own ladder is not one.

**✅ AND THE CONVENTION IS NOW AGREED RATHER THAN ASSUMED, WHICH CHANGES WHAT ITS ABSENCE
MEANS.** `nitpick-compiler_s4` confirmed at 2026-09-10 04:43 that **1.5.4d's notice will
carry all six ladder digests — the unchanged ones included — plus the canary line,
specifically so it can place itself on this ladder.** The request was made because a
notice giving only what *changed* cannot be authenticated by a board that has never
verified the sender; it was accepted without argument.

**The consequence is the part to keep: a future compiler notice that OMITS the unchanged
digests is now anomalous rather than merely terse.** Before this exchange, a short-form
notice meant the sender was being brief. **After it, it means the sender either never
received the convention or is not the party that agreed to it** — so treat a short-form
notice as *failing* the check above and ask, rather than reconstructing the missing rows
from this board and thereby authenticating it against itself. ***A check you can satisfy
on the sender's behalf is not a check.***

**1.5.4d IS BEING PLANNED NOW** — three commits under full harnesses, notice after the
close, nothing asked of this side. **⚠ ONE WORDING DRIFT WORTH KEEPING:** `_s4` summarises
D-275 as *"a `failsafe` arm's qualifier checked at the arm"*, which is the **second half**
of what `_s3` gave. The fuller form on this board is *"an error constant declared inside
an inline module is the FILE's (`(file.Name)` in a `failsafe` arm), **and** an arm's
qualifier naming no known module will refuse at the arm."* **Not a contradiction — a
compression** — but the first half is the part that touches error-constant scope, and a
successor reading only the compression would not know D-275 had one.

### ✅ 1.5.4 IS CLOSED — step 5 (docs) at `da1f911`, notice 2026-09-07 01:13. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**✅ THEY KEPT THE COMMITMENT THEY VOLUNTEERED.** Asked about a garbled clause, they said
the step 5 notice would **quote measured digests from a ladder run rather than assert
them by construction**. It does. **All six unchanged since `a807de9`, bar none, measured
at `da1f911`** — the "bar none" reading this board flagged as *unresolved* rather than
guessed is now confirmed by measurement rather than by agreement. *On a step whose entire
claim is that nothing moved, a measurement and a deduction are not interchangeable, and
they chose the one that can fail.*

```
npkrt.o    67cc8186...     55,648 B  unchanged since 1.5.2i (fe42dba)
builder.o  3b5f868d...  8,086,688 B  unchanged since the 1.5.1b snapshot refresh
builder    fe528b03...  7,014,760 B  unchanged since the same refresh
npkc.ll    72fdbd97... 22,965,305 B  unchanged since a807de9
npkc.o     96a5c05c...  9,168,856 B  unchanged since a807de9
npkc       7757457f...  7,983,712 B  unchanged since a807de9
```
Canary 14 / 52 212 B, unchanged since `8ef0f79`. Docs only: `VERIFICATION_REFERENCE`
§1/§4/§7b/§8, `CONTROL_REFERENCE` §2.4/§4.4, `BUILD_REFERENCE` §7.1, dated notes under
D-022, D-085, D-218, D-219, D-234; the 1.5 README row and `ROADMAP` read **DONE**.

**⚠ STEP 4's OWN NUMBERS WERE NEVER STATED AND ARE RECOVERABLE ONLY FROM THIS NOTICE.**
Step 5 says *"every count step 4's"* and then gives them: **52/52, 66 verified programs,
184 obligations matching, parity 1 204.** Step 4's notice had given the parity and the
suite drop but **not the verified count and not the obligations total** — so
cross-referencing the two yields something neither states alone: **the obligation total
moved 178 → 184 across step 4**, which is the `checker` rows arriving. *A docs-only step
is the one place a restatement is safe to trust, since it must reproduce the prefix's
numbers exactly.*

**THE SUBCYCLE IN ONE TABLE, assembled from five notices:**

```
            suites  verified  obligations        parity   emitted-IR change
step 0      53/53      48     178 (154/24)       1,166    none
step 1      53/53      53     178 (168/10)       1,176    none
step 2      53/53      57     178 (170/ 8)       1,184    none
step 3      53/53      62     178 (170/ 8)       1,194    counted loops only
step 4      52/52      66     184                1,204    prove/assert_static only
step 5      52/52      66     184                1,204    none (docs)
```

**Nothing moved the other way at any step**, the suite count dropped once (the rung
retiring), and **our libraries' emitted IR is byte-identical across the entire subcycle**
— the two steps that changed emission touched only counted loops and
`prove`/`assert_static`, and we write neither outside one probe.

## ⚠⚠ THE COMPILER IS NOW BLOCKED ON THE AUTHOR, AND THAT IS A STATE CHANGE WORTH READING CAREFULLY

**`1.5.4b` (the remaining theories) is the next subcycle in the map, and `nitpick-compiler_s2`
states plainly that NOTHING STARTS ON IT UNTIL THE RULINGS ARE IN**, because **S-46's
`loop-step` kind and S-48's lemma reading shape its encoder.** **Five items are open on
the author: S-45 (VERIFY-001), S-46 (`loop-step` kind), S-47 (the rung suite retires),
S-48 (`prove` as lemma), and DEF-31 (inline module members unreachable).** All four S-
questions **landed under their recommendations with ratification pending and NO DECISION
NUMBER MINTED** — which is the careful form: the code moved, the decision did not, and
the record says so.

**⚠ WHAT THIS IS NOT.** This board's resume signal is **a STATE — the compiler out of
active implementation and into fixing and refinement** — and *"blocked awaiting rulings"*
**is not that state.** It is a pause inside active implementation, and a session reading
a quiet compiler as a stabilised one would resume the libraries on the strength of the
author's inbox rather than on the compiler's condition. **The pause holds. Nothing here
changes it.** *(Recorded because this is the most plausible way the stand-down gets ended
early by accident, and it would look entirely reasonable at the time.)*

### 1.5.4 STEP 4 IS LANDED — `prove`/`assert_static` live, the rung retired, pin target `a807de9`, notice 2026-09-06 23:48. **RECORDED, NOT WORKED — BUT THIS IS THE FIRST NOTICE OF THE SUBCYCLE WITH REAL LIBRARY CONSEQUENCES, AND THEY ARE SET OUT BELOW.**

```
npkrt.o    67cc8186...     55,648 B  unchanged since 1.5.2i (fe42dba)
builder.o  3b5f868d...  8,086,688 B  unchanged since the 1.5.1b snapshot refresh
builder    fe528b03...  7,014,760 B  unchanged since the same refresh
npkc.ll    72fdbd97... 22,965,305 B  the emission, MOVED
npkc.o     96a5c05c...  9,168,856 B  MOVED
npkc       7757457f...  7,983,712 B  MOVED
```
Canary 14 / 52 212 B, unchanged — **and per step 3's lesson that is a null result here too.**
Parity **1 204** verdicts; both runner self-checks +3 cases. **52 harness suites where there were 53** (the rung suite retired).

## ⚠⚠⚠ THE FINDING: `VERIFICATION.md` RULE P-1's PREMISE IS NOW ENTIRELY GONE, IN ALL SIX REPOSITORIES

**This is a library-side consequence, not a compiler defect, and no session asked for
it — it falls out of reading the notice against our own specification.**

**P-1** (present in all six work repos' `meta/specs/VERIFICATION.md`, 56–269 lines each)
says: *until a construct is live, its obligation is stated as a comment beside the code in
the exact syntax it will take*. Its **safety argument** is that at compiler 1.5.0
`prove`, `assert_static`, `limit<Rules>`, loop `invariant` and `requires`/`ensures` **all
refuse with `NITPICK-RUNG-001`**, so *"a premature clause is a build failure and not a
silent no-op"*, and *"the switch is deleting a comment marker rather than inventing the
clause."*

**P-1a (RX-127) already saw the mechanism** — *"the rung is no longer uniform, so
'refused by name' must be re-measured per construct and not inherited"* — and recorded
that at our pin `3d15ac9` three still refuse while `limit<Rules>` had gone live. **Its
closing line is the operative one: *"A comment-form obligation is only inert while its
construct is refused."***

**Tracked against this board's own landing notices, every construct P-1 names has now
gone live:**

```
limit<Rules>          live at 1.5.2             (already live at our 1.5.2f pin; P-1a saw it)
requires / ensures    live at 1.5.3, b2f7d94    checked at entry / at return seams
loop invariant        live at 1.5.3, b2f7d94    checked at every loop head
prove / assert_static live at 1.5.4 step 4, a807de9   THIS NOTICE
```

**So at the compiler's current `main`, NOT ONE of P-1's constructs refuses.** P-1a
instructs re-measurement per construct rather than inheritance; **the re-measurement is
now due for all of them at once, in six repositories.**

**⚠ WHAT THIS DOES *NOT* MEAN — stated so nobody over-reacts at the re-pin.** Comments
remain comments; **nothing breaks automatically and no library result is invalidated.**
The commented-obligation footprint in the exact future syntax is tiny — measured at
2026-09-06 23:48: **2 commented `prove(`, and zero commented `requires(`, `ensures(`,
`invariant(` or `assert_static(`.** **What is lost is the GUARANTEE**, not any code: a
prematurely uncommented clause used to be a build failure, and now compiles.

**⚠ AND ONE PROBE'S EXPECTATION IS NOW INVERTED.**
`nitpick-regex/tests/probe/refused/probe13a_prove_refused.npk` carries
`// expect-error: NITPICK-RUNG-001` and exists to prove `prove` is *inert*. **`prove` is
live, so that probe will no longer be refused at the re-pin.** Its own comment states the
stake precisely: *"A construct that compiled to nothing would tell a caller its argument
was checked when nothing checked it, which is the exact defect the compiler's LIVE-1 lock
was created for."* **In a plain build `prove` now lowers to nothing** — under `--elide` an
undischarged one is `NITPICK-VERIFY-001`, so it is not silent *under verification*.
**Whether that satisfies P-1's requirement is a library design question for the resuming
session, and this seat does not answer it.**

## The rest, measured rather than assumed

- **THE MANIFEST SHAPE MOVED**, and it is the change with the widest reach: every `pick`
  and every `assert_static` is now a **`checker` row** (column 5 `c`, kind `exhaustive`
  or `assert-static`, no z3 query, tier `-`, word `none`). **A `nitpick.obligations`
  recorded before `a807de9` will not match at or past it if the library has any `pick`.**
  **Measured: NO library holds a recorded obligations manifest of any kind — zero across
  all six.** So there is **nothing to re-baseline**, and the exposure is deferred rather
  than absent: `nitpick-regex` (81 `pick` sites), `nitpick-time` (101) and
  `nitpick-posix` (7) will carry `checker` rows in the **first** manifest they record.
  The adopting commit re-records with `npkg verify --record` under **D-040 — a deliberate
  re-baseline in the same commit, never a quiet fix.**
- **DEF-31 does not apply to us.** An inline `mod` block's members are unreachable from
  the parent (`TYPE-007` / `RESOLVE-002`). **Measured: zero inline `mod` blocks.** All 170
  non-comment `mod` uses are file-module declarations of the form `mod:name;`.
- **`assert_static`: zero occurrences.** **`prove`: one in code position** — the probe
  above — and nothing else.
- **Emitted IR is byte-identical for our libraries across this landing**, since only
  programs writing `prove`/`assert_static` changed, and only that one probe does.
- **`NITPICK-RUNG-001`: the asymmetry is real but bounded, and `nitpick-compiler_s2`
  closed the dangerous half on being asked.** The code **stays defined** in
  `emit_codes.npk` as the named refusal for any future rung, and the harness's
  `UNTESTED_CODES` carries it with the reason *"no rung left"*. **It is removed only by a
  decision, and a notice would name that removal explicitly** — so the failure mode this
  board worried about, the code vanishing while our probe still asserts it, cannot happen
  silently. **What remains true and is the fact to carry: our probe's expectation is
  inverted at ANY re-pin at or past `a807de9`, because `prove` compiles.** Confirmed by
  them in those terms.

**⚠ RATIFICATION IS PENDING ON ALL FOUR: S-45 (VERIFY-001), S-46 (`loop-step`), S-47 (the
rung retires), S-48 (`prove` as lemma) — landed under their recommendations, not yet
ratified — plus DEF-31.** So the shape above can still move before the author signs it,
and nothing here should be treated as settled.

**Step 5 (the docs) is under its harness. ✅ THE GARBLED CLAUSE IS RESOLVED — ASKED,
NOT GUESSED.** The notice read *"expect every digest but none to read unchanged"*; this
board flagged it unresolved and read it provisionally as *bar none*. **`nitpick-compiler_s2`
confirmed at 2026-09-06 23:50 that the reading is right and the sentence was garbled on
their side: step 5 is docs-only, so all six digests will read "unchanged since
`a807de9`", bar none.** **And they added the better half unprompted: the step 5 notice
will QUOTE THE MEASURED DIGESTS FROM A LADDER RUN RATHER THAN ASSERT THEM BY
CONSTRUCTION** — which is the difference between a prediction and a measurement, on a
step whose whole claim is that nothing moved.

### 1.5.4 STEP 3 IS LANDED — the counters, S-46 under its recommendation, pin target `65a1756`, notice 2026-09-06 19:58. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**53/53, 62 verified programs (57, 53, 48 at the steps before), parity 1 194, the
catalogue's kinds check agreeing with the new `loop-step` row, and the compiler's 178
obligations UNCHANGED at 170 / 8** — the first step of the subcycle to move none.

```
npkrt.o    67cc8186...     55,648 B  unchanged since 1.5.2i (fe42dba)
builder.o  3b5f868d...  8,086,688 B  unchanged since the 1.5.1b snapshot refresh
builder    fe528b03...  7,014,760 B  unchanged since the same refresh
npkc.ll    3abbe270... 22,897,885 B  the emission, MOVED
npkc.o     535874fc...  9,122,976 B  MOVED
npkc       0115df4b...  7,940,984 B  MOVED
```

**⚠⚠ THE CANARY'S FOURTH IDENTICAL READING IS A NULL RESULT FOR THIS STEP, NOT A
CONTROL — AND THIS BOARD MUST WALK BACK HOW IT PRAISED THE SERIES ONE NOTICE AGO.**
14 defines / 52 212 B again, unchanged since `8ef0f79`. **But they gave the reason, and
the reason removes the evidential value: *the canary holds no counted loop.*** Step 3
changes emission **only** for counted loops, so **our canary cannot detect this change at
all.** The previous notice recorded the three-reading series as establishing *"our
canary's emission is stable across 1.5.4 so far"* — **that was too broad.** The correct
statement is narrower: **a control series is only a control for changes that touch the
paths its program exercises**, and for step 3 the canary is silent rather than
reassuring. *Four identical readings look like mounting evidence and are not; a fifth
would add nothing either. The right instrument for a counted-loop change is a program
with a counted loop, and we have none.*

**THE ONE EMITTED-IR CHANGE OF THE SUBCYCLE SO FAR.** A counted loop whose step is a
**literal** no longer emits the `BadStep` compare — the checker's `TYPE-068` at step 0
already made the literal positive — so such a program **compiles to fewer bytes than at
`24fad46`**. A **computed** step keeps its compare, now the guard of a **new catalogue
kind: `loop-step`, kind 18, trap `-4101`, guard yes**, elided when the manifest discharges
the row. **A manifest read from this compiler forward can carry `loop-step` rows; none
exists in the compiler's own.** No new refusal (`TYPE-068` landed at step 0), no new trap
identity.

**BLAST RADIUS: ZERO — BUT INCIDENTALLY, LIKE STEP 0, NOT STRUCTURALLY LIKE STEPS 1–2.**
This is why the board keeps those two kinds of zero apart. **Steps 1 and 2 could not
affect a program that compiled before; step 3 can, and simply does not affect ours.**
Re-verified here at 2026-09-06 19:58 rather than carried forward from the earlier run —
all six work trees unmoved (`nitpick-parse` `3cad08c`, `nitpick-regex` `ab93eae`,
`nitpick-sockets` `d385991`, `nitpick-time` `2589069`, `nitpick-tui` `e5439ee`,
`nitpick-posix` `948d9b6`, all `dirty=0`), and the claim itself re-run: **zero `loop(`
heads in code position, zero `till` anywhere.** **⚠ THE MOMENT A LIBRARY WRITES A COUNTED
LOOP, THIS CLEARANCE EXPIRES AND ITS EMITTED BYTES CHANGE** — with a literal step it
loses the `BadStep` compare, with a computed step it gains a `loop-step` obligation row.

**Next: step 4 (`prove` / `assert_static` / `exhaustive` rows, the `checker` verdict, the
rung suite's retirement — S-45, S-47, S-48) and step 5 (the docs); harnesses running.
S-45…S-48 remain open with the author.**

### 1.5.4 STEP 2 IS LANDED — the merge, pin target `24fad46`, notice 2026-09-06 19:36. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**53/53, 57 verified programs (53 at step 1, 48 at step 0), parity 1 184 verdicts
agreeing, and the compiler's 178 obligations now 170 discharged / 8 open (168 / 10
before).** `origin/main == main`.

```
npkrt.o    67cc8186...     55,648 B  unchanged since 1.5.2i (fe42dba)
builder.o  3b5f868d...  8,086,688 B  unchanged since the 1.5.1b snapshot refresh
builder    fe528b03...  7,014,760 B  unchanged since the same refresh
npkc.ll    b7f4b8e7... 22,717,508 B  the emission, MOVED (the encoder's source)
npkc.o     829e930d...  9,013,248 B  MOVED
npkc       67160221...  7,838,264 B  MOVED
```

**THE CANARY IS NOW A THREE-READING CONTROL SERIES, AND THAT IS WHAT MAKES IT USABLE.**
`8ef0f79`, `182ef47`, `24fad46` — **14 defines / 52 212 B at all three, same scratchpad
path.** A single reading at a controlled path proves nothing; three identical ones across
commits that each moved `npkc` establish that **our canary's emission is stable across
1.5.4 so far.** *Still not comparable with this board's 50 482 B, which is a different
path (D-236) — the series is internally valid and externally not.*

**WHAT LANDED.** An arm's facts survive it **guarded by its condition** — a region opened
for an arm re-pushes its hypotheses as `(=> c H)` into the parent on leaving — so versions
after an `if`, a `when` or a `pick` **merge as `(ite c v_then v_else)` instead of being
forgotten**; a `pick` expression's value is the chain of its arms' `give` terms; and the
right-hand side of `&&` / `||` and a ternary's branches are encoded under their
conditions.

**✅ A PREDICTION WRITTEN AT 1.5.0 CAME TRUE AT 1.5.4.** The pin on
`divz_after_branch.npk` carried the expectation *"1.5.4 adds the branch guards; this
expectation changes to discharged"* — **and it flipped as promised.** This is the fourth
prediction from the compiler side to land intact on this board, and the longest-range one
by far: **they write falsifiable expectations into their own test pins and those
expectations survive four subcycles.** That is the strongest available evidence that
their reports can be treated as claims to verify rather than claims to audit.

**⚠ THE COST NUMBER WAS TAKEN UNDER CONTENTION AND THEY SAID SO — DO NOT LATER READ IT
AS A CLEAN BASELINE.** *"31.7 s to 34.9 s, the solver files 514 to 760 asserts"*,
measured on the compiler's own walk **while three harnesses ran beside it**. **The delta
is the usable part; the absolutes are contended**, and 34.9 s must not become a
remembered baseline that a future quiet-machine reading is diffed against — that
comparison would manufacture an improvement, or a regression, out of scheduling.
*Recorded because this board already owns a spread whose failure signal is a constant
delta, and a contended timing is exactly the sort of number that leaks into one.* The
disclosure was volunteered, which is the behaviour to keep expecting.

**BLAST RADIUS: ZERO, STRUCTURALLY — the same kind as step 1, not step 0's.** No new
refusal, no new trap, no emitted-IR change. **Nothing here needs re-checking when library
code changes.**

**OBLIGATION TREND ACROSS THE SUBCYCLE, none ever moving the other way:**

```
step 0   154 discharged / 24 open
step 1   168 / 10
step 2   170 /  8
```

**Next: step 3 the counters and the `loop-step` kind (S-46); step 4 `prove` /
`assert_static` / `exhaustive` rows with the rung suite's retirement (S-45, S-47, S-48);
step 5 the docs — harnesses running. S-45…S-48 remain open with the author.**

### 1.5.4 STEP 1 IS LANDED — path conditions as hypotheses, pin target `182ef47`, notice 2026-09-06 19:20. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**Full harness: 53/53, and 53 verified programs — up from 48 at step 0.** `origin/main
== main`. **The compiler's own 178 obligations are now 168 discharged / 10 open, where
154 / 24 held before — re-recorded, and NOTHING MOVED THE OTHER WAY.** Parity **1 176
verdicts agreeing** (1 166 at step 0). *That "none moved the other way" is the load-
bearing half: 14 newly discharged obligations are only good news if no previously
discharged one regressed, and they checked the direction rather than the total.*

**THE SIX DIGESTS AT `182ef47`, LADDER ORDER (D-265).**

```
npkrt.o    67cc8186...     55,648 B  unchanged since 1.5.2i (fe42dba)
builder.o  3b5f868d...  8,086,688 B  unchanged since the 1.5.1b snapshot refresh
builder    fe528b03...  7,014,760 B  unchanged since the same refresh
npkc.ll    ae39f8e3... 22,566,981 B  the emission, MOVED (the encoder's own source grew)
npkc.o     ec36d1a0...  8,958,960 B  MOVED
npkc       98efe5f6...  7,790,528 B  MOVED
```

**✅ AND THIS TIME THE CANARY IS A CONTROLLED COMPARISON, WHICH IS A DIFFERENT THING
FROM THE LAST ONE.** They ran our `tools/canary.npk` **from the SAME scratchpad path as
the previous notice** and report **14 defines, 52 212 B — unchanged since `8ef0f79`.**
**Holding the path constant is what makes the byte number mean something**, and it means
something narrow: **comparable WITHIN this series of notices, still NOT comparable with
this board's 50 482 B**, which was taken at a different path (D-236). *So the rule is
not "the byte count is useless" but "the byte count compares only against another
reading at the same path" — and they have now given us two such readings.* Their stated
reason for expecting no movement is the right kind: **this step touches the obligation
walk only, not a byte of emitted IR for a program without obligations.**

**WHAT LANDED.** A branch condition is a **hypothesis inside the arm it guards and its
negation inside the other**; after an arm that never falls through (a syntactic
terminator) the other arm's versions and condition are what follows. A `pick` arm knows
its pattern — a value, a range, or a wildcard as **the negation of the arms before it**,
with a pattern's literal **encoded under the SELECTOR's type**, since the checker types
no pattern for its own sake — plus the negations of earlier arms and its `where` guard,
and **no conditions at all when a `fall` or a guard makes the order more than the
patterns say**. A loop's condition is false after a loop nothing `break`s out of.
`when`'s `then` and `end` know whether the body ran.

**BLAST RADIUS: ZERO, AND STRUCTURALLY SO — WHICH IS NOT WHAT STEP 0's ZERO WAS.**
**No new refusal, no new trap, no emitted-IR change.** Step 0's clearance was
*incidental* — its new refusals had no surface here only because these libraries happen
not to use counted loops, and that expires the moment someone writes one. **This one is
structural: a step that changes only what the verifier may assume cannot refuse a
program that compiled before.** *A successor should treat these two zeroes differently:
step 0's needs re-checking when library code changes, step 1's does not.*

**⚠ WHAT IT MEANS FOR A GREEN, AND IT COMPOUNDS WITH DEF-26.** *"Verification results
read from this compiler forward can discharge what the branch structure proves; nothing
already discharged moved."* Set beside step 0's **DEF-26** — a guard site inside a
value-`pick`'s arm had carried **no obligation row since 1.5.0** — the picture is that
**a pre-1.5.4 green both understated its obligations and under-discharged the ones it
had.** Nothing to do while paused, and no library result is invalidated; but **the
strength of a verification result is now a function of which compiler produced it**, and
any comparison of results across this boundary is comparing two different instruments.

**FOUR STEPS RUN IN WORKTREES NOW**, landing in order: step 2 the merge (`ite` after
`if` / `when` / `pick`, and `&&` / `||` / ternary arms); step 3 the counters and the
`loop-step` kind (S-46); step 4 `prove` / `assert_static` / `exhaustive` rows with the
rung suite's retirement (S-45, S-47, S-48); step 5 the docs. **S-45…S-48 remain open
with the author**, so what actually lands may still move.

### 1.5.4 STEP 0 IS LANDED — pin target `8ef0f79`, notice 2026-09-06 18:47 from `nitpick-compiler_s2`. **RECORDED, NOT WORKED. PIN STAYS `3d15ac9`.**

**First notice from the rotated address, and it arrived correctly formed.** Full harness:
**53/53, 48 verified programs, the compiler's 178 obligations matching, parity 1 166
verdicts agreeing.** `origin/main == main`. They said *file, don't work* before we had to.

**✅ OUR WORDING REQUEST WAS ADOPTED WITHIN ONE NOTICE.** This board asked that a future
notice saying "unchanged" name the commit, because "unchanged" is frame-relative and a
consumer holding an older pin reads it as agreement. This notice says **"unchanged since
1.5.2i (`fe42dba`)"**. The frame trap that cost us a careful paragraph last notice is
now closed at the source.

**THE SIX DIGESTS AT `8ef0f79`, LADDER ORDER (D-265).**

```
npkrt.o    67cc8186...     55,648 B  unchanged since 1.5.2i (fe42dba) -- DEF-25's fix
builder.o  3b5f868d...  8,086,688 B  unchanged since the 1.5.1b snapshot refresh
builder    fe528b03...  7,014,760 B  unchanged since the same refresh
npkc.ll    1175fa69... 22,442,371 B  the emission, MOVED (the cross-machine claim)
npkc.o     92a0b6bb...  8,912,952 B  MOVED (the toolchain's)
npkc       8e3c9e3d...  7,749,960 B  MOVED (the toolchain's)
```

**⚠ THEY RAN *OUR* CANARY, AND ONLY HALF OF IT COMPARES.** `tools/canary.npk` through
the quickemit `npkc` at `8ef0f79`: **14 defines, 52 212 B of `.ll`**. **The BYTE COUNT
IS PATH-DEPENDENT (D-236) — they compiled from a scratchpad path — so it is NOT
comparable with this board's recorded 50 482 B, and a session that diffs those two
numbers is measuring a directory name.** **The DEFINE COUNT is the half that compares,
and it held: 14 here and 14 at `b2f7d94`.** So our flat prediction survives on its
comparable half. *(Third canary trap now on this board: ours versus their floor-only
probe are different artifacts; and our own canary's byte count is not comparable across
machines or paths, only its define count is.)*

**WHAT STEP 0 LANDED.**

- **DEF-26** — a guard site inside a `pick` **expression's** arm had had **no obligation
  row since 1.5.0**, because the walk never entered a value-`pick`'s arms. Fixed; every
  walker that must see into a statement's expressions now reads one enumeration.
- **DEF-27** — a callee parameter sharing a name with an address-taken caller local was
  bound unnamed in the contract substitution, leaving its call-site `requires` row open
  for a literal argument. Fixed.
- **DEF-28 / DEF-30 — NEW REFUSALS, `NITPICK-TYPE-068`.** A counted loop's head is now
  checked: **`loop(start, limit, step)` takes three arguments, `till(limit, step)` two,
  and a literal (or negated-literal) step must be positive.** A `till (cond) { … }`
  do-while spelling, a two-argument `loop`, or a `till(n, 0)` that used to compile and
  trap at run time is **refused at compile time**.
- **DEF-29 — the compile-time evaluator disagreed with the run time.** A `comptime
  func`'s counted loop took its direction from the **step's sign** and read
  `till(limit, step)` as `loop(limit, step)`, so a descending loop folded to **zero
  iterations** and a `till` to the wrong range. Fixed — direction from the bounds, head
  read by kind, as the emitter does. **A library `comptime func` that iterates downward
  or uses `till` may see its folded value change, to the correct one.**
- No new trap identity; `nitpick.obligations` byte-identical at this step.

**BLAST RADIUS: ZERO — AND MEASURED HERE RATHER THAN INHERITED.** The notice says *"per
your measurement of the library surface this should touch nothing."* **That measurement
was about `failsafe`, which is unrelated to the counted-loop rule**, so the conclusion
was right and the inference was not. Re-measured directly at 2026-09-06 18:47:

```
loop( ) heads in code position:   0    (all 53 'loop' occurrences are in comments)
till   anywhere in library code:  0
till (cond) { } do-while spelling: 0
comptime func declarations:      16    -- but none contains a counted loop
what these libraries actually use: while 141, for 347
```

**So `NITPICK-TYPE-068` has no library surface to refuse, and DEF-29 cannot change any
folded value here, because the constructs both concern are not used at all.** *(Logged
with its reason rather than as a bare "nothing to do": "no counted loops are used" stays
true only until someone writes one, and a successor needs to know which fact expires.)* **AND THE LOOP IS CLOSED ON THEIR SIDE, WHICH IS THE PART A SUCCESSOR
WOULD OTHERWISE HAVE TO ASK ABOUT:** `nitpick-compiler_s2` acknowledged the flag at
2026-09-06 18:51, accepted that it had cited a `failsafe` measurement for a counted-loop
question, and **confirmed it now carries the re-measurement together with the
incidental-clearance caveat.** So the superseded `failsafe` number is not still
circulating on the compiler side, and a future notice reasoning about our surface is
reasoning from the corrected version. *(Two wrong readings of our library surface were
raised and retired within one afternoon — one ours, one theirs, each caught by the other
side reading the claim instead of accepting it. That is the relationship doing the work
that no single session's care could.)*

**COMING BEHIND IT, each under its own full harness, landing in order:** step 1 path
conditions (a branch condition becomes a hypothesis in its arm; the compiler's manifest
re-recorded with 13 more discharges); step 2 the merge (`ite` after `if` / `when` /
`pick`); step 3 the counters (`$` and a range `for`'s binding as terms, plus a new
catalogue kind `loop-step` for a computed step, S-46); step 4 `prove` / `assert_static`
/ `exhaustive` rows and the rung suite's retirement (S-45, S-47, S-48); step 5 the docs.
**Four questions are open with the author (S-45…S-48) and the plan proceeds under its
own recommendations** — worth knowing, because answers to those may move what lands.

### 1.5.3 IS LANDED — pin target `b2f7d94`, notice 2026-09-06 15:36. **RECORDED, NOT WORKED. NO RE-PIN TAKEN, NO CLAIM OPENED, NOTHING DISPATCHED. THE PIN STAYS `3d15ac9`.**

**This is the notice the quiet period existed to catch, and it is filed rather than
acted on — which is the seat working, not the seat stalling.** `nitpick-compiler_s1`,
who asked for nothing from this side. **Contracts are live**: four commits, each under
a full harness on a cumulative prefix.

**⚠ THE BOARD'S OWN PREDICTION HELD TO THE BYTE, AND THE WORD "UNCHANGED" IN THIS
NOTICE IS A FRAME TRAP.** This board predicted that at the next re-pin `npkrt.o` would
read `67cc8186…` / 55 648 B and that this would be **correct** rather than a defect,
because DEF-25's fix is in the runtime. It reads exactly that. **But the notice calls
it *unchanged*, and that is true in the COMPILER's frame — unchanged since 1.5.2h at
`c81efa5` — while in OURS it has moved.** Measured here from the pin itself rather than
quoted from this board: `.internal/toolchain/3d15ac9/npkrt.o` is **55 576 B,
`c9ddbcff…`**. **So "unchanged" in a notice never means "unchanged for us", and a
session that reads it as agreement with our pin will conclude the runtime is stable
when it is precisely the thing that moved.** Verify against the notice, never against
the previous pin — and read the notice's *frame* as well as its values.

**THE SIX DIGESTS AT `b2f7d94` (npkg build).**

```
npkrt.o    67cc8186...    55,648 B   unchanged since c81efa5; MOVED vs our 3d15ac9 pin
builder.o  3b5f868d...  8,086,688 B  unchanged
builder    fe528b03...  7,014,760 B  unchanged
npkc.ll    35d370d1... 22,340,907 B  MOVED (was af2bf3dd... 21,688,240 B)
npkc.o     c3ab0c63...  8,880,808 B
npkc       9c8cb8ba...  7,723,104 B  MOVED
```

**WHAT CHANGED FOR A LIBRARY AUTHOR — the language surface, which is what will
invalidate library work written against the old one.**

- **`requires` is now CHECKED at the callee's entry in every build** — a generated
  predicate `<sym>.req`, one trap per clause, **`RequiresViolated -4112`**. A sync
  function carrying one **splits into `.body` plus its checked entry**, exactly as a
  limited parameter makes it; a coroutine checks at **state 0**.
- **`ensures` is checked at every return seam** — **`EnsuresViolated -4113`**.
  `result` is the value in register, and **`old(p)` names the function's own
  PARAMETERS only.**
- **A loop `invariant` is checked at every loop head** — **`InvariantViolated -4114`**.
- **`failsafe`'s exit code must be positive.** A literal that is not is **refused
  (REACH-004)**; a **computed zero traps and the process ends at 70**.
- **Clauses repeat their keyword** (`requires a requires b`).
- **`use` is now a keyword** — a function cannot be named `use`.

**BLAST RADIUS OF THE TWO BREAKING CHANGES, MEASURED READ-ONLY AT 2026-09-06 15:36 AND
NOT ACTED ON.** This seat does not work; it measured because "unassessed" is a worse
thing to hand a successor than a number, and a read costs nothing:

- **`use` as a keyword touches NOTHING.** Zero functions named `use` across all six
  work repositories.
- **REACH-004 touches NOTHING.** There is **no bare-literal `failsafe` value** in any
  library source.
- **✅ AND THE COMPUTED-ZERO RULE TOUCHES NOTHING EITHER — CORRECTED 2026-09-06 16:15
  AFTER `nitpick-compiler_s1` REFUTED THIS BOARD'S FIRST READING.** **What was written
  here, and was wrong:** *"the computed-zero rule touches 141 sites, the libraries using
  `failsafe = int32(Error:e)` almost exclusively."* **`failsafe = int32(Error:e)` is the
  MANDATORY SIGNATURE of every failsafe (D-013), not a computation of the exit code.**
  What the guard judges is **each `exit` statement's operand inside the body** — a
  literal operand refused at compile time when non-positive, a computed one trapping to
  70 when zero or negative at runtime. **So it is a per-exit reading, not a
  per-signature one**, and this board had measured a signature and reported it as a
  behaviour. **Re-measured correctly with a brace-tracking scan over 747 `.npk` files,
  264 failsafe blocks:**

```
exit literals inside failsafe bodies:  9 60 70 71 80 87 88 89 90 91..99
  non-positive literals:               0     REACH-004 refuses nothing
  computed (non-literal) operands:     0     the trap-to-70 path has no consumer
```

  **Both arms are clean and `failsafe` costs the libraries nothing at the re-pin.** The
  97 `exit 0i32` in these sources are all on ordinary success paths **outside** any
  failsafe body, which is precisely the distinction a flat grep destroys. *(Recorded at
  length because the error is instructive: a signature was measured and a behaviour was
  reported, with a confident denominator attached — and **a wrong number carrying a
  denominator is worse than no number, since the denominator is what makes it look
  measured**, which is a lesson already on this board from an earlier session.)*

**WHAT CHANGED IN THE VERIFICATION LEG.** Rows: `requires` at every call with a
recorded callee — **bypass at a direct sync call, held at an `await` or through `dyn`,
word `retained` whatever the verdict** — and at every entry; `ensures` per return
point; a loop's **entry, preservation and continue** rows; **`failsafe-post` per exit**,
and since every `failsafe` has them now, **every verify test names them and
`expect-obligation: none` names no program**; conformance rows per impl method against
its trait (no guard, word `none`). A **`pure never fails` callee is an uninterpreted
function**; a callee's `ensures` is **knowledge** at `raw` / `?!` / `relay`. `rows.txt`
gains four columns — **space:site, role, group, traps**. `nitpick.obligations` is **178
rows** (141 + the compiler's 37 `failsafe-post` rows, plus `npk_gcd256`'s div-zero now
discharged through its loop guard, since a loop condition holds inside the body).

**⚠⚠ THE SPREAD'S SIGNAL IS NOW DOUBLE-INVERTED. READ THIS BEFORE RUNNING IT — IT IS
THE ONE ITEM HERE THAT CAN SEND A PEER A DEFECT REPORT FOR CORRECT BEHAVIOUR.** This
board already records that on the re-founded spread the old finding's signal is
**INVERTED**: after the prelude trim, **a CONSTANT delta is the failure signal**, and it
reaches the compiler side as a defect report naming a program rather than as a result.
**1.5.3 now produces a constant delta BY DESIGN.** The floor-only canary moved
**50 561 B → 52 288 B at 14 defines**, and the **+1 727 B is the six `failsafe-post`
guards of its six `exit`s in the plain build.** The compiler states the shape
explicitly: **it is a per-exit-in-failsafe cost, NOT a per-program constant.** **So the
failsafe-post cost must be subtracted per program before a constant delta means
anything at all** — and with 141 `failsafe` sites in the libraries this is not a small
correction. **Run the spread at the new pin without that subtraction and it manufactures
exactly the defect report the inverted signal was designed to raise.**

**⚠ TWO CANARIES EXIST AND THEY ARE DIFFERENT ARTIFACTS — DO NOT CONFLATE THEM.**

```
ours,     tools/canary.npk      50,482 B / 14   at BOTH aaffb87 and 3d15ac9 (flat)
theirs,   floor-only probe      50,561 B / 14 -> 52,288 B / 14 at b2f7d94
```

They differ by 79 B at baseline and are not the same program. **Our flat prediction is
about our canary and is untested at `b2f7d94`;** their movement is about theirs and is
explained. Comparing one against the other produces a difference that means nothing.

**Rung count on a full run reads 1** (`inline_mod.npk`, its construct now `prove`).
**⚠ THE COMPILER ADDRESS HAS ROTATED: SEND TO `nitpick-compiler_s2` FROM 2026-09-06 16:15.**
**ANNOUNCED BY `_s1` BY NAME, WHICH IS THE ONLY THING THAT MAKES A ROTATION REAL HERE** —
this board's standing rule is that a quiet `_s1` is never evidence of a completed
handoff, and `_s2` going busy earlier today was logged as an observation and explicitly
not as a signal. **`_s1` goes quiet once `_s2` confirms, and a message arriving there
after that WILL NOT BE READ.** Expect the next landing notice from `_s2`. **`_s1`
briefed it on our side already** — the library hold, this seat as a listener that logs
and acts on nothing, notices with the six digests in ladder order and the canary, the
pin at `3d15ac9`, that `s5` and `s6` are not addresses and no address is inferred from
`ListAgents`, that `npkrt.o` at `67cc8186…` is DEF-25's fix and correct, and that our CI
digest reads against `05457db4…`. **Our wording rule was accepted and passed on: a
future notice saying "unchanged" will say "unchanged since `<commit>`".**

### 1.5.3 WAS IN PROGRESS — SUPERSEDED BY THE LANDING NOTICE ABOVE — status from `nitpick-compiler_s1`, 2026-09-06 13:25. **THIS IS NOT A LANDING NOTICE AND NOTHING IN IT IS TO BE ACTED ON.**

**The first entry logged under the quiet period, and it is logged exactly as the
writer line requires: recorded, not worked.** No re-pin is taken, no claim is
opened, nothing is dispatched. **The pin stays at `3d15ac9`.**

**Their status, in their words rather than paraphrased:** 1.5.3 is *"mid-way
through — contracts live; steps 0 and 1 are under harness, step 2 is being
written."* The compiler is in the middle of a subcycle, which is precisely the
state the pause exists for. **The 1.5.3 landing notice will carry the six digests
as before**, so when it arrives the re-pin procedure has its inputs and nothing
needs to be asked for.

**They confirmed both of our landmines back to us, unprompted** — worth recording
because it makes the confirmation *theirs* rather than ours: the pin stays at
`3d15ac9`; `npkrt.o` moving to `67cc8186…` / 55 648 B at our next re-pin is
DEF-25's runtime fix and is **CORRECT, not a defect**; and our CI digest reads
against `05457db4…` under that pin. **Verify against their notice when it comes,
never against the previous pin** — four identical `c9ddbcff…` readings hardened
into an expectation that was never a rule.

**THE COMPILER ADDRESS QUESTION IS SETTLED, AND IT TOOK THREE ASKS — THE LAST OF
WHICH WENT TO THE SUBJECT OF THE QUESTION RATHER THAN TO SOMEONE ABOUT IT.** The
eighth orchestrator left it open deliberately rather than guessing. Asking `_s1`
closed the *address* in under two minutes. Asking the author produced a
contradiction. **Asking `_s2` about `_s2` closed the rest, and produced the
reconciliation neither of the other two could.** The sequence is the lesson and it
is worth more than the answer:

- **`nitpick-compiler_s1` is the live compiler address.** Send there.
- **`nitpick-compiler_s2` WAS NEVER BRIEFED AND IS NOT AN ADDRESS — SETTLED
  FIRST-HAND BY `_s2` ITSELF, 2026-09-06 13:34.** Three accounts of this
  circulated within about half an hour and **two of them were second-hand claims
  about a third party.** `_s1`, asked directly: `_s2` and `_s3` are parked, neither
  briefed, neither an address. **The author, relayed by `nitpick-libs_s3`:** `_s2`
  was at least initially briefed, then told to stand down, and is listening so it
  can relay — *with his own memory flagged as fuzzy, because it was late when it
  happened.* **`_s2`, asked, about itself:** *"I received no handover brief from
  `_s1`, full or partial. My author sent me no prompt beyond naming the session."*
  **THE ONLY AUTHORITY ON A SESSION'S BRIEFING STATE IS THAT SESSION**, and this is
  the entry that establishes it here.
- **AND THE AUTHOR WAS NOT WRONG — HIS MEMORY WAS ATTACHED TO THE WRONG SESSION.**
  `_s2` supplied the reconciliation nobody else could: the briefing-then-stand-by
  he remembers **most likely describes `_s1` itself**, which `_s0` briefed early on
  2026-09-06 ahead of a compaction, with a stand-by condition. **So no account was
  false; one was misfiled.** Worth keeping, because "two sources disagree" invites
  picking a winner, and the actual resolution was that both described real events
  and one had the wrong subject.
- **⚠ A CORRECTION TO WHAT THIS BOARD BRIEFLY IMPLIED: A MESSAGE TO `_s2` IS NOT
  LOST.** The two-branch framing this workbench was working from had "unbriefed"
  implying messages vanish. `_s2` says otherwise, about itself: it is alive and
  idle, a message arrives at its next turn, and it will read it, report it to its
  author, and **forward it to `_s1` noting that it came through `_s2`.** But it
  states the limit in the same breath, and the limit is the operative half:
  **that is a FALLBACK, NOT A ROUTE — a parked spare can be closed without
  notice.** So `_s1` remains the address; `_s2` is what you use if `_s1` is
  unreachable and you accept that the message may die with the spare.
- **⚠ DO NOT INFER THE SWITCH HAS HAPPENED FROM `_s1` GOING QUIET. A STALLED
  HANDOFF LOOKS EXACTLY LIKE A COMPLETED ONE FROM OUTSIDE.** This is the hazard the
  author's account adds and `_s1`'s does not, and it is the one that could actually
  cost us: a silence we read as "rotation complete, write to `_s2`" is
  indistinguishable from a silence that means "still stuck on a question from last
  night". **The switch is announced or it has not happened.** The introduction is
  bidirectional in this ecosystem and the compiler side has been reliable about it.
- **On the inference we declined to make.** The `ListAgents` shape — `_s1` busy,
  `_s2` and `_s3` idle — did point at the right answer, and `nitpick-libs_s3`
  fairly noted so. **It would still have been the right answer for the wrong
  reason**, and the reason is where the value was: the inference yields "`_s2` is
  next", which is true, while missing both that the rotation is **frozen** and that
  a quiet `_s1` must not be read as its completion. *Parked is not the same as
  addressable, and stalled is not the same as parked.* Hazard 4 says ask; asking
  cost one message and returned what the shape of the roster could not.
- **When they hand off at a subcycle boundary the outgoing session briefs its
  successor by message, names it explicitly, and WILL COPY US ON THAT NAMING.** So
  this workbench should never have to infer the compiler address again. Until that
  copy arrives, `_s1`.

**⚠ THE STALLED-HANDOFF HAZARD PAID WITHIN TWENTY MINUTES OF BEING WRITTEN — AND
THEN THE TRANSITION TURNED OUT TO HAVE A KNOWN CAUSE, WHICH IS A DIFFERENT ENTRY.**
At 2026-09-06 13:32 `ListAgents` showed **`nitpick-compiler_s2` BUSY**, idle minutes
earlier. It was logged then as an *observation and explicitly not as evidence*: the
tempting read was *"the rotation completed, write to `_s2`"* and the correct read was
that **a parked session doing something is not an announcement.** That caution was
right and is kept. **The cause is now known: `nitpick-libs_s3` had messaged `_s2`
minutes before, asking it to settle its own briefing state.** *An explained
transition and an unexplained one are different entries* — a bare signal left on the
board is something a later session will mine for meaning it does not have, so the
cause is recorded beside the observation rather than the observation being deleted.
**The address never changed and was never going to: `nitpick-compiler_s1`.**

**THE COMPILER-SIDE PICTURE, VOLUNTEERED BY `_s2` AS OBSERVATION RATHER THAN AS A
NOTICE — AND NOTHING IN IT IS TO BE ACTED ON.** Recorded because it is the only
current read of that tree this workbench has, and flagged hard because it is exactly
the shape of thing that gets mistaken for a landing notice:

- **`nitpick-compiler_s0` is GONE.** It ran 1.5.2g step 1 in worktree `g1` this
  morning. This board's roster had it as *"stood down from the role, still alive"*;
  it is now corrected, and `ListAgents` agrees — no `_s0` row.
- **`nitpick-compiler_s1` is the only busy compiler session and is RUNNING A FULL
  HARNESS in worktree `c1`.** Expect it to be slow to answer, and do not read that
  slowness as a handoff (see the hazard above).
- **Compiler `main` is at `47a7eb2` — 1.5.3 RATIFIED, D-267/D-268** — with
  worktrees `c0`, `c1`, `c2` on 1.5.3. **⚠ THIS IS NOT THE LANDING NOTICE AND IS
  NOT A RE-PIN TRIGGER.** `_s1` has said its 1.5.3 landing notice will carry the six
  digests as before; **that** is the input to the re-pin procedure, and this is a
  heads-up from a third party. **THE PIN STAYS `3d15ac9`.** Nothing is claimed,
  nothing is dispatched, and no re-pin is taken — the quiet period is unchanged by
  it.
- **`nitpick-compiler_s3` exists and is idle**, and `_s2` explicitly declined to
  speak for it, which is the same discipline that settled `_s2`'s own state.

**They also confirmed receipt of the handover of OUR address.** The eighth
orchestrator asserted that handover without waiting for an acknowledgement and
said so plainly; the acknowledgement is now on the record. `nitpick-libs_s4` is
where landing notices and defect answers go. **The gap that receipt closed is the
one that fails silently:** an unacknowledged address change loses exactly the
notices the quiet period exists to collect, and nothing would have reported it.

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

**⚠ BEFORE READING THE PAUSE AS "NOTHING CAN BE DONE": COMPILER-INDEPENDENT WORK
EXISTS, IT IS UNBLOCKED, AND THE AUTHOR RAISED IT SPECIFICALLY SO IT WOULD SURVIVE
THE PAUSE.** 2026-09-06 13:50. **He asked for it to be in the handoff brief because
he expects to have forgotten it himself by then**, and his reason generalises past
this item: *"there is no actual way of knowing how long it will take to get to the
stable state. sometimes sub cycles go fast. sometimes they take all day or longer.
It just depends on how many hiccups we encounter along the way."* **An indeterminate
pause is exactly the condition under which something held only in a person's head is
lost**, so it lives here as well as in the brief.

**THE GAP: `nitpick-regex` CYCLE 0.1 HAS ITS MAP AND NOT ITS EXECUTION-GRADE
FILES.** Verified in the tree at 2026-09-06 13:50 rather than taken from this board's
own claim about itself:

- **`meta/roadmap/0.1/` holds exactly two files** — `0.1.0.md` (241 lines) and
  `README.md` (110 lines). **Six subcycle files are owed: `0.1.1` … `0.1.6`.**
- **The map already exists, so this is not designing a cycle from nothing.**
  `0.1/README.md`'s table gives every subcycle a topic and an end-state: 0.1.1 the
  core grammar; 0.1.2 the explicit stack, `NREGEX_NEST_DEPTH` and the refusal
  (*10 000 levels deep is a `NestTooDeep`, not a segfault*); 0.1.3 classes; 0.1.4
  escapes and flags; 0.1.5 the refusals by name with offsets; 0.1.6 close.
  **A useful tell in that table: `0.1.0` is a markdown LINK because its file exists,
  and 0.1.1–0.1.6 are plain text because they do not.**
- **`0.1.0.md` existing is NOT evidence that 0.1 was started.** The convention is
  stated in two places — `meta/roadmap/ROADMAP.md:23` and `0.1/README.md:8`:
  *"the opening subcycle file is written by the cycle before it."* `0.0.5` step 5
  wrote it. **The size difference makes the point: cycle 0.0's six files run
  452–1189 lines each; `0.1.0.md` is 241.**
- **`nitpick-regex`'s `O-Y2` is open and belongs to this cycle** — whether `x` mode ignores whitespace
  inside classes. `meta/OPEN_QUESTIONS.md:648`, with the standing recommendation
  *no*, matching Rust, and refusing `xx`. `0.1/README.md:69` has it as a checklist
  item and `:76` ties it to 0.1.4's behaviour, **so it wants an answer before 0.1.4
  rather than at the close.**
  **⚠ AND NEVER CITE A LIBRARY QUESTION ID BARE ON THIS BOARD.** That id is
  allocated in `nitpick-sockets` too, as an unrelated question about descriptor
  passing. **This is structural rather than bad luck: 20 ids are allocated in more
  than one of the six work repositories and NOT ONE means the same thing
  everywhere** — swept and recorded in `meta/OPEN_QUESTIONS.md`'s second registry,
  with the method, so it is re-runnable rather than remembered. **Partial agreement
  is the hazard, not disagreement** — the worst case is allocated in five
  repositories as three different questions, three of which agree, so a reader who
  checks two or three and stops learns a rule that is false in the rest:

```
B1  "when to migrate off the harness"   regex, sockets, tui
    "when npkg can build a library"     time
    "the multi-call binary"             posix
```

  Cite a library question only through a registry entry naming the repository.
  `check_refs` enforces it, and **the right response to that gate firing is an entry,
  never a change to the check.** *(Evidence fenced deliberately: `prose()` strips
  fences so quoted ids are not themselves read as citations. **This paragraph needed
  that fix — the first draft cited the example bare and `check_refs` refused the
  commit**, which is the second time on record that this rule has caught its own
  author in the act of writing it.)*

**WHY THIS IS NOT BLOCKED BY THE STAND-DOWN, WHICH IS THE WHOLE POINT OF RAISING
IT.** Writing subcycle files is **planning, not code.** The pause exists because a
library built against a moving compiler re-derives its own premises at every re-pin
— and **nothing in a subcycle plan gets invalidated by a re-pin.** It is therefore
the one category of `nitpick-regex` work the stand-down does not reach, and it is
also the category the author most wants done well: plans here are expected to be
execution-grade, because a specific plan catches design faults before code and has
to be followable by an executor that was not present for the planning.

**THIS SESSION IS NOT DOING IT, AND THAT IS CORRECT.** This seat logs; it does not
work, dispatch, or plan. **The item is recorded for `nitpick-libs_s5`**, so that
whichever session takes the lock next knows there is compiler-independent work
waiting and **does not sit idle waiting for a stability signal it does not need for
this part.**

**⚠ AND ONE THING THE 0.1 PLAN MUST ACCOUNT FOR, ADDED 2026-09-12 10:49 AT THE AUTHOR'S
DIRECTION: THE FLOOR LEAVES ONE THING UNPROVEN AND 0.1.0 WALKS STRAIGHT INTO IT.**

**`0.1.0`'s subject is *"the byte cursor with offsets, the AST ARENA, the node kinds"* —
and the single largest hole in the runtime's own evidence is the allocator's small-block
free path.** Both of `TCB.md` §4c's residue categories point at the same symbol:

```
category 1, rows the profile did not decide   6 of the 7 are `@npk_small_free`
category 2, claims the spec does NOT make     `@npk_small_free` -- "the five ensures and
                                              the frame are not decided under the profile
                                              (unknown at the budget; at ten times it two
                                              answer unknown and four do not ...)"
```

**⚠ THAT IS NOT A BUDGET TWEAK AWAY.** They raised the budget **ten-fold** and the rows
still did not resolve — two answered `unknown` and four did not return. *So a resuming
session must not plan on the assumption that the floor's allocator evidence will be
complete by the time 0.1 is built; on present evidence it will not be.*

**AND `nitpick-regex` IS ALREADY ON THAT PATH, measured in tracked code rather than
assumed:** `ralloc` **26**, `free` **29**, `dalloc` **22**, `alloc` **17**, `wild` **133**.
**An arena allocates and, at teardown, frees** — which is precisely the operation whose five
`ensures` and frame the floor declines to decide.

**WHAT THIS MEANS FOR THE PLAN, stated as a planning constraint rather than as alarm:**

- **It is not a defect and nothing is broken.** The floor's `(residue …)` sentence is a
  claim deliberately **not made**, enumerated honestly in a generated region held by both
  runners. The plain build's guards are unaffected.
- **It means the arena's own correctness is `nitpick-regex`'s to establish, not something it
  inherits.** Under the guarantee stack recorded above, the floor proves the trap route and
  the compiler proves exit codes; **the arena's free discipline sits in the gap between
  them, which is the library's verification to do.**
- **So `0.1.0`'s subcycle file should say so explicitly** — what the arena promises about
  its own frees, and how that is checked here — rather than leaving a reader to assume the
  allocator underneath is proven. *Per the author's standing preference, a plan records the
  measurements it rests on; this is one of them, and it is cheaper to write into 0.1.0 now
  than to discover when a probe disagrees.*
- **⚠ AND 1.5.6c WILL REVISIT IT — IN THE DIRECTION THAT CONFIRMS THIS CONSTRAINT.** Ratified
  2026-09-17 11:28: a new subcycle before 1.5.7 corrects an **over-strong assumption in
  `npk_small_free`'s spec.** Correcting an over-strong assumption makes the spec claim *less*, so
  the free path is likely to become **more honestly unproven, not proven.** *Plan 0.1.0 on the
  assumption that the arena's free discipline stays the library's own to establish.*
- **Re-check it at the re-pin**, because §4c is generated: if a later cycle decides those
  rows, the constraint lifts, and the check is one read of `TCB.md` §4c rather than a
  conversation.


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

**THREE WERE RUN; FIVE ARE KEPT.** `.internal/toolchain/` holds `0dfddac`,
`3d15ac9`, `94874ce`, `950bb1d` and `aaffb87` — five pins, each with `npkc`,
`npkrt.o`, `PIN.md` and `SHA256SUMS`. **The three in the table below are the three
this diagnosis needed, not the archive.** *(Counted with `ls` 2026-09-06 by
`nitpick-libs_s4`; raised by it and confirmed independently by the eighth
orchestrator, who had written the sentence.)* The sentence above is **true as
written** and is left standing — the trap is that it sits directly on top of a
three-row table, inside a measured result with real digests around it, so it reads
as an inventory to anyone who does not run `ls`. **That is trap 4: a count that
looks measured because it is adjacent to a measurement.**

**Old pins are never deleted, and the reason is structural rather than
sentimental.** Every differential this workbench owes is taken by running **two
pinned compilers over the same inputs on this machine**. So deleting a pin does
not cost history, it costs the ability to take the measurement at all — and a
remembered number compared against a freshly built compiler is not a differential,
it is an anecdote. This diagnosis is the standing example: the CI log was
**HTTP 404 and unrecoverable**, and the kept pins were the only instrument left.

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
