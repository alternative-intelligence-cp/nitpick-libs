---
name: research
description: Find and record an up-to-date fact about the world outside the compiler tree — a standard's current edition, a release number, a known defect in prior art, current guidance — and return it as a dated, sourced digest. Use when a plan pins an external version, when a worker meets a question the specifications do not answer, when a library is security-sensitive, and at every audit.
allowed-tools: WebSearch WebFetch Read Grep Glob
---

# Research

The compiler tree is the only source for facts about the language, and it is
read, not searched. Everything else a plan rests on — a standard, a data
release, a reference implementation, a defect registry — lives outside it and
moves. This skill is how a fact from outside is found, dated, sourced, and
made citable (W-25).

## 1. When research happens

| When | Who asks | Who runs it |
|---|---|---|
| a repository or cycle is planned — the currency table (§7) | planner | researcher; the planner inline for one fact |
| a decision says "the latest at cycle N" and the cycle arrives | worker | inline for the number; researcher if anything about it is unclear |
| a worker meets a fact the specifications do not settle | worker | inline for one fetch; researcher beyond |
| a library is security-sensitive — before its cycle map, again at hardening | planner, then worker | researcher, always (§8) |
| every audit — external claims re-verified | auditor | inline for one fetch; researcher beyond |

**One fetch may be inline. More is a request** (§3) to the researcher agent,
whose context is disposable. A worker's is not.

## 2. What counts as a source

- **Primary — the only kind a claim may cite:** the standards body
  (`unicode.org`, `iana.org`, `rfc-editor.org`, `pubs.opengroup.org`,
  `toml.io`, `yaml.org`, ECMA for JSON); a defect registry (`cve.org`,
  `nvd.nist.gov`) or the upstream project's own tracker and release notes;
  the reference implementation's repository at a named revision.
- **Secondary — usable with the primary named beside it:** a peer-reviewed
  paper; a vendor's documentation.
- **Leads only, never cited:** blogs, answer sites, aggregators — and this
  ecosystem's own documents. A claim that cites only another document here
  is not verified; that is the audit skill's rule and it applies to research.

## 3. The request

The asker has the context and spends it once, in this shape. It is what
makes the handoff cheap:

```
RESEARCH REQUEST
question: <one sentence, answerable>
feeds: <the rule, decision or checklist item the answer changes>
would-change-the-plan-if: <what answer would force a change>
sources-that-count: <from §2, specifically>
sensitivity: routine | security     (security: two independent primaries; stale after 90 days)
budget: <fetches; default 12>
return-to: <who files the digest, and where>
```

## 4. The procedure

Search to locate the primary. Open the primary, not a summary of it. Record
the exact version, date and the line that answers. For `security`, find a
second independent primary. Stop at the budget and say what is unresolved.
Write the digest. Do not browse past the question.

## 5. The digest

```
# <topic> — research digest

**As of <date>.** Question: <the request's question>.

## Answer
<one paragraph: the version, edition or fact, stated plainly>

## Evidence
- <URL> — retrieved <date> — "<the line that answers, quoted>"

## What would change this
<the request's would-change-the-plan-if, and whether it did>

## Confidence and gaps
<high | medium | low, and why; anything unresolved at the budget>
```

## 6. Filing and citing

The researcher **never writes into a repository**; its final message is the
digest. The requesting writer files it as `meta/research/<topic>.md` and
commits it with the work that used it. A decision that rests on it says
`per meta/research/<topic>.md, as of <date>`. A `security` digest is stale
ninety days after its date; every other digest is re-checked at the
repository's hardening cycle.

## 7. The currency table — `meta/research/CURRENCY.md`

```
| Depends on | Pinned | Checked | Source | Decision |
|---|---|---|---|---|
| tzdata | 2026c | 2026-09-03 | iana.org/time-zones | TM-100 |
```

One row per standard, corpus, data release, algorithm reference and
reference implementation the plan names. A row unchecked for six months is
`stale` to the auditor. **A cycle whose currency rows are unchecked is not
ready to start** — the rule the playbook applies to open questions.

## 8. Security-sensitive libraries

Before the cycle map, three requests are mandatory, and their digests are
cited by the safety specification: known defects in the prior art and in
every reference implementation the plan reads; the standards body's current
guidance for the primitives chosen; the current versions of the test
vectors. All three are re-run at the hardening cycle. Research changes probes
and specifications, not just code: a finding here is a cycle-0.0 probe before
it is anything else.

## 9. Boundaries and limits

Language facts — what the compiler accepts, what the runtime does — are never
researched on the web; nothing about them exists there. Fetching has edges:
a large page is truncated, so fetch the section's own URL; a long PDF is read
in twenty-page ranges; a redirect to another host is reported, not followed —
follow it deliberately; results are cached fifteen minutes, so a "changed"
answer inside that window is the cache. Nothing behind a login.

Search fixes facts, not understanding. The stronger defences stay where the
playbook put them: real conformance corpora as gates, fuzzing with the
findings committed, and differential testing against a reference.
