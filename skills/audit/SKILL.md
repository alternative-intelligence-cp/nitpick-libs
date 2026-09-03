---
name: audit
description: Adversarially audit a Nitpick ecosystem repository or the whole ecosystem — diff every document against the thing it describes, re-verify every claim about the compiler against its actual source, find dormant rules, stale cross-references and cross-repository contradictions, and REPORT without fixing. Use before a cycle close, before a release, when two documents seem to disagree, or on a schedule.
allowed-tools: Bash(python3 *) Bash(git *) Bash(grep *) Bash(rg *) Read Grep Glob
---

# Auditing

## Why this role exists

The compiler project's most repeated finding, across six cycles:

> **The compiler and the thing that describes it have to be diffed, because
> reading either alone never reveals the gap.** Every hole cycle 0.6 found was
> found that way, and none of them by a test.

An auditor is that discipline, run deliberately rather than hoped for.

## The two rules that make an audit worth having

**A-1 — report, never fix.** An auditor that fixes is an auditor that can hide
what it changed, and its report stops being evidence. Produce findings with
locations and severity; let a worker fix them under the ordinary discipline,
in a commit that says what it is.

**A-2 — be adversarial, not confirmatory.** An audit whose question is "does
this look right" finds that it does. The question is **"what would have to be
true for this to be wrong, and is it?"** Go looking for the contradiction.

## What to audit, in descending order of value

### 1. Claims about the compiler, re-verified against source

**The highest-value class, and the one with a proven catch.** A specification
in this ecosystem once stated that the runtime returned `EPIPE` rather than
raising `SIGPIPE`. It was true of the case being thought about and false in
general, it shipped, and it was found only when somebody grepped
`runtime/npkrt.ll` instead of believing the document.

So: for every claim about the language or its runtime, **find the primary
source and check it**. `REPOS/nitpick/` is read-only and entirely readable.

- a claim about a language rule → `nitpick/meta/specs/`, and the `DECISIONS.md`
  entry it cites
- a claim about the runtime → `nitpick/runtime/npkrt.ll`
- a claim about what the compiler accepts → `nitpick/src/`, and prefer a probe
  program to a reading
- a claim citing `D-nnn` → confirm the decision says what it is cited for, and
  that it has not been superseded

**A claim that cites only another document in this ecosystem is not verified.**
Follow it to the primary source or record it as unverified.

### 2. Cross-repository contradiction

Six repositories describe one language. Where two disagree about a shared
fact, at least one is wrong — and the disagreement is invisible from inside
either.

Known shared facts worth diffing: the signal-disposition positions (three
different answers, all correct, for stated reasons — check the reasons still
hold); the error-budget rule; the version policy; the reserved-word
substitutions; the tooling state.

### 3. Document against document

`/npk:check` automates the mechanical half — links, citations, duplicates,
leaks. Run it first, then audit what it cannot see:

- a **decision declared and never cited** is usually a specification stating a
  rule without attributing it
- a **rule with no decision** is a rule nobody agreed to
- a **superseded decision still cited as live**
- a **cycle number, path or file name that moved** and was not swept

### 4. Dormant rules

**The pattern the compiler found three times.** A specification rule with no
implementation *and* no refusal — it reads as enforced and enforces nothing.

Pre-code, every rule is dormant, so what is auditable now is narrower and still
useful: does every numbered rule have a cycle that will implement it, a
checklist item that will check it, or a decision that struck it? A rule owned
by no cycle will never be built.

### 5. Budget and scope compliance

Error identities against the stated budget. The utility catalogue against the
standard. The public surface against what the specifications describe.

## The report

Group by severity, and be honest about which is which:

| Severity | Means |
|---|---|
| **contradiction** | two documents cannot both be right |
| **unverified claim** | a statement about the compiler with no primary source checked |
| **dormant** | a rule nothing will implement, check or strike |
| **stale** | a reference that no longer resolves or no longer means what it did |
| **cosmetic** | inconsistent phrasing, a missing citation |

Each finding gets a **location**, the **evidence** (a path and a line, not an
impression), and **what would resolve it**. A finding without evidence is an
opinion.

End with what you checked and found clean. An audit that reports only problems
does not say how much ground it covered — and the next auditor cannot tell what
is already known good.

## Helper

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/gather_claims.py [repo ...]
```

Extracts the claims that assert something about the compiler — those citing
`D-nnn`, quoting a compiler path, or naming a runtime symbol — into a checklist
to verify one by one. It **finds candidates; it does not verify them.** The
verification is reading the source.
