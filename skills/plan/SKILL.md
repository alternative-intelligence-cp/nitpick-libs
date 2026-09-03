---
name: plan
description: Write an execution-grade plan for a Nitpick ecosystem cycle or a whole new repository — the specification set, the decision log, the open questions, the cycle map, and cycle 0.0. Use when opening a new cycle folder, when planning a library or application from scratch, or when a cycle's subcycle files need writing ahead of the work.
argument-hint: "[repo] [cycle]"
allowed-tools: Bash(python3 *) Bash(git *) Bash(grep *) Read Write Edit Grep Glob
---

# Planning

## What this role does, and does not

**Does:** a whole repository's plan from scratch (specs → decisions → open
questions → cycle map → cycle 0.0), or a cycle's `README.md` and its subcycle
map.

**Does not:** write the *next* subcycle file at a cycle's close. That belongs to
the worker who just finished, deliberately — the person who has just learned
what a cycle taught is the one best placed to plan the next, and handing it to a
fresh planner throws that away. `/npk:worker`'s close checklist owns it.

## The order, and why it is not negotiable

specs → decisions → open questions → cycle map → cycle 0.0 → **then** code.

The compiler project credits this order with catching most of its design holes,
and its cycle notes record the counter-example: *a construct that parses is not
a construct that works*, found by three cycles that were mostly repair.

## The rule that keeps a plan honest

**Every decision records the alternatives declined, not just the choice.** The
alternatives are what a later reader will propose, and a decision that does not
say why they lost will be re-litigated. This is the single highest-value habit
in the ecosystem's decision logs.

Two more that follow from it:

- **A settled decision's text is never rewritten.** Supersede it with a new
  numbered one that says why. `nitpick-tui`'s T-113 is the worked example: it
  corrects a false claim about signal disposition without erasing the claim,
  because the record of *how the error survived* is itself the lesson.
- **A question that gets answered is struck through with its decision number,
  never deleted.** The question is part of the record of how the answer was
  reached.

## What a plan must contain

- **Specifications** that state numbered, normative **rules** — facts about the
  library, not intentions. Rationale paragraphs carry no obligation and are
  marked as such.
- **A safety document first**, stating what the *language* imposes: the
  `failsafe` contract, the error budget REACH-002 forces, the trapping
  arithmetic, the borrow and ownership rules. Most proposals that look
  reasonable in the abstract die on one of these.
- **An error budget as a number**, with the module decomposition that keeps it
  payable — REACH is import-scoped, so which module declares what is part of the
  budget.
- **A cycle map** where the riskiest thing is early, instruments precede what
  they guard, and **cycle 0.0 is always the language probes**.
- **Open items with a recommendation each**, or a stated reason they stay open:
  it is a measurement, it is data, it is gated, it waits for a consumer. "Open"
  with no reason is "forgotten".

## Probes, spikes, and the difference

- **A probe answers "is this spellable?"** — a small program asking the compiler
  whether a language shape the design depends on actually works. A probe that
  fails changes the design, which costs a day now and a cycle later.
- **A spike answers "how big is this actually?"** — a measurement, with its
  **thresholds decided in advance**, so a bad number produces a stop rather than
  an improvisation.

Both belong in cycle 0.0. Confusing them produces a probe with no pass mark.

## Verify before committing

```bash
python3 ${CLAUDE_SKILL_DIR}/../check/scripts/check_refs.py .
```

A plan whose cross-references do not resolve is a plan somebody will follow into
a dead link. Every decision cited must be defined, and **every decision defined
must be cited** — an uncited decision is usually a specification that states a
rule and forgot to attribute it.

## Do not copy content into the plan

The language constraints live in `../PLAYBOOK.md`; the compiler's decisions live
in its own tree. **Cite them; do not restate them.** A fact with two homes drifts,
and this ecosystem's entire discipline is that a fact has one.
