# The floor canary

**The smallest program that compiles and exits 0.** It references nothing, so
its emitted IR is the prelude and almost nothing else — which is what makes it
the instrument for measuring a prelude trim, and the one continuous number this
workbench owes the compiler session at every re-pin.

**It is committed here because the previous one was not.** Until 2026-09-06 the
canary lived only in a session scratchpad. The 2026-09-05 measurement's *output*
(`canary.ll`, 50 560 B, 14 defines) survived by accident; **its input did not**,
so the series could not be continued — the same defect as the 30-program
spread's unrecorded set, on the measurement most relied upon. A source that
lives in a scratchpad is a measurement that ends with the session.

## How to take the reading

```bash
$NPKC tools/canary.npk > /tmp/canary.ll ; echo "exit=$?"     # MUST redirect: npkc writes IR to STDOUT
grep -c '^define' /tmp/canary.ll                              # the number that matters
stat -c %s /tmp/canary.ll                                     # path-dependent — see below
```

**Redirect, always.** `npkc` writes the emission to **stdout**, so an
unredirected run in an agent session dumps ~50 000 bytes of IR into the
transcript. Measured 2026-09-06, in this file's own first reading.

## Which number to trust

**The count of `define`s, not the byte count.** The byte count is
**path-dependent** by design — `D-236` puts every site row's source path,
relative to the manifest root, into the emission, so the same source compiled
from a different directory gives a different size. The define count is
path-independent *and* it is what a prelude trim moves, because the trim removes
whole `define`s. Both halves matter: path-independence makes it trustworthy,
whole-define removal makes it sensitive.

**But this canary is a WEAK case for that rule, and the measurement said so
before this file could overclaim.** Compiled from a session scratchpad and again
from `tools/` — different paths, six characters apart — it emits **the same
50 482 bytes** at both pins. The reason is visible in the emission: the site
path table is overwhelmingly the *prelude's* rows, every one of them the fixed
string `prelude.npk`, and a floor program contributes almost no site rows of its
own. **Path dependence is real and it scales with a program's own site count**,
which is why `nitpick-time` 0.0.5 measured 14 bytes between two directories one
character apart — that program had 14 site rows. **The canary has close to
none.**

So: record the path beside every number anyway, because the property holds for
the *spread* even though it barely registers here — and because a number whose
denominator is unstated is how this workbench keeps getting caught.

## The series

| Pin | Compiled from | `.ll` bytes | `define`s |
|---|---|---|---|
| `aaffb87` (1.5.2d) | a session scratchpad, source **lost** | 50 560 | **14** |
| `aaffb87` (1.5.2d) | this session's scratchpad | 50 482 | **14** |
| `3d15ac9` (1.5.2f) | this session's scratchpad | **50 482** | **14** |

**The 78-byte gap between rows one and two is a DIFFERENT PROGRAM, not a
compiler change** — the source of row one no longer exists, so this canary is a
reconstruction from its description rather than the same file. The define count
is 14 in all three, which is the half that carries across the break.

**Rows two and three are the measurement that counts**, because they are the
same program through both pinned compilers on this machine: the differential the
board's method requires. **`nitpick-compiler_s0` predicted the 1.5.2f point
would be FLAT, and it is — byte-identical and define-identical.** A prediction
that forbids all movement is falsified by any movement; this one was not.
