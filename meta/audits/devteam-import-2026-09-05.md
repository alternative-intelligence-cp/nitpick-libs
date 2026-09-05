# What the `devteam` experiment gives this workbench — the import list

Filed 2026-09-05 by `nitpick-libs-42`, the fourth orchestrator, at the
author's direction. **Not an audit of a repository here** — it is a findings
list imported from an external system, filed in `meta/audits/` because that is
where findings are triaged (`meta/audits/README.md`).

**The source.** `devteam` is this workbench's build system, generalised by the
author into a standalone pipeline and given one experimental end-to-end run.
The run was pared down mid-flight to salvage the most relevant data, because
there was no way to predict how long it would take and tokens are finite. The
author's framing, which is the right one to read the rest of this by:
**"sometimes finding out what not to do is as important as finding out what to
do."** A system derived from ours fails where ours is weak, so its failure
modes are worth more to us than its successes.

- the product: `../claude-skills/plugins/devteam/`
- its lessons: that tree's `DESIGN.md` §§15–21 and `docs/CONSOLIDATION.md`
- the run's own record: `../claude-skills/.internal/scratch/devteam/`
- **all of it is READ-ONLY from here** (`library-sessions-write-scope`)

The third orchestrator read this material on 2026-09-05 and harvested two
findings into `PLAYBOOK.md` §6. This is the second, independent pass the
author asked for; items 1–4 below are landed, 5–11 are open.

---

## Landed 2026-09-05

### 1. The guard names the heredoc limit in its REFUSAL, not only its docstring

**The principle, which is `devteam`'s most reliable design lesson: guidance
goes where the temptation is, not where the documentation is.** A rule in a
docstring is read by whoever edits the file; a rule in a refusal is read by
somebody standing in front of the decision. `devteam` has measured evidence
this works — a verifier that had never seen the finding met such a message and
reported it did not use the workaround *because the message named it*.

Ours stated the limit only in `tools/guard_compiler_tree.py`'s module
docstring. The compiler refusal now also says, in the message itself, that
`python3 - <<PY` is a **known limit and not permission**, that this harness's
standing instruction pushes toward exactly that form, and — the part `devteam`
can say and we cannot — that **nothing here reports the write afterwards**.
`devteam` has `check_scope` as a backstop; we have none, so the refusal is the
only mechanism watching, and the message now says so.

This does not close board question 3. `filesystem.denyWrite` remains the
airtight mechanism and remains the author's call.

### 2. The `git worktree list` false positive is fixed, and now has controls

The guard refused `git worktree list` — a **read** — as "a mutating git
subcommand", because `GIT_WRITE` is keyed on the subcommand and `worktree`
covers both `list` and `add`. Its own docstring warns that *"a guard with
false positives gets disabled, which is worse than no guard"*, so this was the
failure mode it had named for itself.

**Why it survived 73 passing controls: there was no case for it.** Fixed with
`GIT_READ_FORMS`, judged on the token *after* the subcommand, with
`GIT_BARE_READS` for the two whose bare form lists (`tag`, `remote`) — bare
`git stash` **creates** one, so the bare form cannot be inferred. Anything not
named stays a write: the table only ever narrows a refusal.

Thirteen new controls, each read form with its write twin. Verified against
the real compiler path, not only the fixture: `worktree list` ALLOW,
`worktree add` DENY.

**`devteam` has this same defect** — its `GIT_WRITE` also contains `worktree`,
with a comment acknowledging the undifferentiated set. Worth sending back.

### 3. `tools/run_controls.py` — one runner, and it reports the denominator

The controls were four files invoked from a remembered list, and **a list held
in someone's head has no failure mode anyone can see**. The runner finds them
by pattern, so a control that stops being run is not invisible, and — copying
`devteam`'s best detail — **"no controls found" is itself a finding** rather
than a quiet exit 0.

### 4. Every control reports its case count and false-positive share

`devteam` prints `check_refs control: 55 cases (35 of them false-positive
controls, 63%)`. Ours printed `All 7 cases correct`. The share is the number
worth surfacing because **a check whose controls are all planted faults can
only ever get stricter** — nothing fails when it over-refuses, which is
exactly how item 2 survived.

Now: `all 4 controls green — 111 cases, 50 of them false-positive controls
(45%)`.

### And doing item 4 found a live defect of the worst class

Adding false-positive controls to `check_refs` immediately failed two of them.
**`check_refs` read an identifier inside a fenced block, and inside its own
quoted output, as a citation** — reporting `cited-undefined` against a file
that had merely pasted evidence.

This workbench **requires** a worker to paste check output verbatim into its
committed REPORT block. So the check fired on the behaviour the protocol
mandates, which `devteam` names as the worst category: **it puts the correct
response and the safe response in opposite directions, and the lesson it
teaches is to paraphrase the evidence next time.**

Fixed by `prose()`, which strips fenced blocks before the citation scans.
Deliberately **not** applied to the leak scan — a home directory pasted inside
a fence is still leaked, and quoting is exactly how one gets there.

**A stated gap, not a closed one.** Verbatim output quoted *inline* (single
backticks) is still miscounted. It is not fixable by stripping inline spans,
because `` `RX-126` `` in backticks is how a real citation is written here — a
control now asserts that genuine form still counts. **The rule this implies is
that verbatim output belongs in a fence**, and a rule is what it needs; a
check guessing which backticks were quotations would be inventing an agreement
nothing requires (see item 5).

Regression-checked across all six repositories: clean.

---

## Open, in the order I would take them

### 5. Audit every check against "name the rule whose two sides it compares"

**If you cannot name a rule requiring the two sides to agree, the check is
*proposing* a rule rather than enforcing one** — and its false positives are
that missing rule showing up, never noise to tune away. `devteam` applied this
to three of its own checks and found all three proposing rules; stating the
rules is what made the checks legitimate.

Two failure modes wanting opposite fixes: **inventing an agreement no rule
requires** (noise — write the rule or withdraw the check, never parse harder),
and **being unable to extract the thing to compare** (silence — a backstop
after the fact, and a refusal naming the limit). The interpreter heredoc is
the second kind. None of our checks has been audited against this test.

### 6. Sweep for pairs of rules that cannot both be satisfied

**A rule a worker must break to do the work right is a defect in the rule.**
`devteam` has nine known instances, every one two rules correct in isolation
with nothing noting the tension, and **every one found by a worker hitting it
from below** — because a reviewer reads rules one at a time and a worker is
the only party required to satisfy all of them at once.

**We have at least one live:** this harness's standing instruction prefers
heredocs and `sed` over `Write`/`Edit`, and the guard can only judge
`Write`/`Edit`. That is not merely a guard limitation, it is a rule pair, and
framing it that way changes what a fix has to do.

The question with the good hit rate: not *"is this rule right?"* but
**"what else must be true at the same moment, and can both hold?"**

### 7. Log every handoff question as a defect in the record

From `devteam`'s manager-rotation design: the incoming manager asks the
outgoing one what it could not determine from the files, and **every question
asked is logged as a defect in the record** — because a record that needed a
conversation to interpret is a record that will fail the next reader, who may
have nobody to ask.

**This session asked five.** They are in `RECORD.md`'s 2026-09-05 entries and
each is a gap the files should have closed: what the re-pin owed, whether the
two standing claims were stale, whether catalogue-don't-raise still held, the
model and width policy, and who the compiler peer now is. Cheap, and it
self-applies immediately.

### 8. "A sentence written to justify a measurement does not itself get measured"

The measurement licenses the paragraph; the paragraph then acquires claims the
measurement never covered, and the borrowing is invisible because it reads as
one thing. `devteam` had three false sentences reach signed text in one night
from an author measuring everything else carefully.

Aimed squarely at how `BOARD.md` is written — dense prose wrapped around real
numbers. **This session committed an instance**: it asserted the workbench's
`check_refs.py` had no controls, while measuring `devteam`'s side properly.
`test_check_refs.py` had existed all along.

### 9. Before widening a rule on a count of workarounds, run the widened rule first

The detector is excellent: **several agents departing the same way,
independently, is a measurement of the rule rather than of the workers**, and
it needs no cleverness — only somebody reading more than one report at a time,
which an orchestrator already does.

But `devteam`'s **first application counted the wrong thing**, claiming three
departures where one existed, and the obvious next move would have produced
eleven false findings. So the second half is not optional: **apply the
candidate rule to the corpus and read what it newly reports** before widening
anything. One command, and it catches both errors.

### 10. The ceremony cost grows with the record and nothing bounds it

`devteam` measured roughly **200,000 tokens per step-unit** of fixed overhead,
rising as the append-only record grows, and names our exact case — *"a
compiler, a library ecosystem, something worked on for a year"* — as where it
eventually dominates. Its manager read 897 KB of task files on one run.

Live for us now that budget is the binding constraint. **`RECORD.md` is 2,600+
lines and `BOARD.md` is dense.** `devteam` deliberately proposes no answer and
warns what each obvious one trades: **summarising** puts a lossy second home
beside the authoritative one and the summary is what gets read; **scoping
decisions by area** hides the cross-cutting contradiction audits exist to
catch; **reading only recent decisions** inverts the value, since the oldest
are the load-bearing ones. Recorded so the first person to feel the cost does
not reach for summarisation without seeing the price.

### 11. "A thing exempted from a check for its own protection is a thing the check cannot see"

Whenever something is carved out, **name what watches it instead — or record
that nothing does**, which is a legitimate answer and a very different one
from "it is safe". We now have one such carve-out by construction: fenced
blocks are invisible to the citation scans (item 4). What watches them is
nothing, and this sentence is the record of that.

---

## One bias to expect

`devteam`'s own report: **everything found so far has made that pipeline
stricter and nothing has made it simpler**, and both simplifications in its
history came from people who **declined to use it**. Its
`docs/REPORTING-PROBLEMS.md` keeps an `unnecessary` category — *it worked, and
buying it was not worth what it cost* — which has **never once been used**.

We should expect the same bias here, and it is worth saying plainly: every
item on this list makes this workbench stricter. None makes it smaller.
