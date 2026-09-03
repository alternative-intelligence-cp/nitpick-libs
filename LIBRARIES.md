# The library registry

Every Nitpick library, its package name, its decision prefix, and where it is.
**Claim a name and a prefix here in the commit that starts the work**, so that
neither is taken twice.

## Libraries

| Repository | Package | Decisions | What it is | State |
|---|---|---|---|---|
| [`nitpick-tui`](https://github.com/alternative-intelligence-cp/nitpick-tui) | `ntui` | `T-` | terminal user interface | **planned** — 16 specs, 66 decisions, 18 cycles mapped, cycle 0.0 execution-grade. No code. |
| [`nitpick-parse`](https://github.com/alternative-intelligence-cp/nitpick-parse) | `nparse` | `PA-` | multi-format parsing over one event stream, with format plugins | planning |
| [`nitpick-regex`](https://github.com/alternative-intelligence-cp/nitpick-regex) | `nregex` | `RX-` | regular expressions | planning |
| [`nitpick-sockets`](https://github.com/alternative-intelligence-cp/nitpick-sockets) | `nsockets` | `SK-` | the BSD socket surface — AF_UNIX, TCP and UDP over IPv4/IPv6 | planning |
| [`nitpick-time`](https://github.com/alternative-intelligence-cp/nitpick-time) | `ntime` | `TM-` | dates, times, durations and zones | planning |

## Why the prefixes are what they are

A decision is cited as `<prefix>-nnn` and must not collide with two other
things:

- **`D-nnn` is always the compiler's**, in `nitpick/meta/specs/DECISIONS.md`.
  Those are language decisions and are never a library's to amend.
- **Single letters are already used as *rule* prefixes inside specification
  documents** — `S-1` in a safety document, `X-1` in a text one, `I-1` in an
  input one, and so on, scoped to the document that defines them. A library
  whose decision prefix were a single letter would collide with its own rules.

Hence two-letter prefixes from here on. `nitpick-tui`'s `T-` predates the
convention and stays as it is, because a settled decision's citation is not
rewritten.

## Names taken

**Packages:** `ntui`, `nparse`, `nregex`, `nsockets`, `ntime`.

**Decision prefixes:** `T-`, `PA-`, `RX-`, `SK-`, `TM-`, and `D-` (the
compiler's, permanently).

**Also in use across the ecosystem**, and not available to a new library: the
compiler's own `lib/` modules — `nbridge`, `nfs`, `nhash`, `nio`, `nproc`,
`nstr`, `nsys`, `ntensor`, `nvec` — several of which are destined for an
`nlibc` sibling repository when the compiler's `meta/LAYOUT.md` moves them.

## Cross-library overlaps, recorded

Dependencies between libraries are **not planned**: `[dependencies]` is empty
everywhere, because the compiler's loader initialises its dependency-root list
empty and never populates it, so a cross-repository import resolves against
nothing (`O-N2`). Where two libraries genuinely overlap, the overlap is
recorded as an open question in **both**, and resolved when resolution lands.

| Overlap | Between | Recorded as |
|---|---|---|
| Unicode tables — character classes, case folding, property lookups | `ntui`, `nregex` | an `O-x` in each |
| datetime scanning — TOML carries four datetime types | `nparse`, `ntime` | an `O-x` in each |

## Prior art

`../ARCHIVE/` holds the prototype-era implementations. They are a **behavioural
oracle** — what the domain needed, what the edge cases were, which tests
existed — and their **dependency choices are not precedent**: most reach C
through an FFI that no longer exists in the language, and several carry defects
recorded in the compiler's own audits.
