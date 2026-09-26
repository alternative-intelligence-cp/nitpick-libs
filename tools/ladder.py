#!/usr/bin/env python3
r"""Ladder check for a compiler landing notice.   usage: ladder.py BASELINE NOTICE
BASELINE: the six rows of the board's "THE BASELINE NOTICE N MUST QUOTE" block (commas allowed in sizes).
NOTICE: the notice's six rows, pasted as `name  sha256  size B  unchanged` or
        `name  sha256  size B  MOVED +delta B  (was sha256, size B)`.
Passes when both sides have six rows, every unchanged row equals the baseline, and every moved row's
previous value equals the baseline and its delta recomputes. THE CONTROL: the same check with one hex digit
of the first row's compared digest altered (its `was` digest if it moved) must FAIL. Exit 0 only if both hold.

Written by nitpick-libs_s6 on 2026-09-26, whose checks until then ran inline and died with its scratchpad;
committed by nitpick-libs_s7, which re-ran its commissioning cases (RECORD.md, 2026-09-26). Run as `python3 -B`.

To get a BASELINE file, take exactly ONE fenced block, the one under its header:
  python3 -B -c "import sys;b=open('BOARD.md').read();k=b.find(sys.argv[1]);f=b.index('\`\`\`',k);e=b.index('\`\`\`',f+3);print(b[f+3:e].strip())" 'THE BASELINE NOTICE 69 MUST QUOTE'
The compiler seat's notices give the rows in prose: transcribe them into the NOTICE form by hand, and re-read
the transcription against the message. Beside the ladder, every notice gets three read-only git checks in the
compiler's local repository -- never fetch there, it rewrites FETCH_HEAD:
  git -C ../nitpick merge-base --is-ancestor <prev> <new>
  git -C ../nitpick diff --name-only <prev> <new> -- src | wc -l
  git -C ../nitpick diff --name-only <prev> <new> -- runtime bootstrap | wc -l
Then file the entry and write the NEXT baseline block, the notice's new values, in the same commit."""
import re, sys
ROW = re.compile(r'^\s*(\S+)\s+([0-9a-f]{64})\s+([\d,]+) B\b(.*)$')
MOV = re.compile(r'MOVED\s+([+-][\d,]+) B\s+\(was ([0-9a-f]{64}), ([\d,]+) B\)')
num = lambda s: int(s.replace(',', ''))
def baseline(text):
    rows = [m for m in map(ROW.match, text.splitlines()) if m]
    names = [m.group(1) for m in rows]
    if len(names) != len(set(names)):          # two blocks pasted: a later row would silently win
        sys.exit('baseline repeats a row name %s -- paste exactly ONE block' % sorted({n for n in names if names.count(n) > 1}))
    return {m.group(1): (m.group(2), num(m.group(3))) for m in rows}
def check(base, text):
    new, prev, bad = {}, {}, []
    for line in text.splitlines():
        m = ROW.match(line)
        if not m: continue
        n, d, z, rest = m.group(1), m.group(2), num(m.group(3)), m.group(4)
        new[n] = (d, z)
        mv = MOV.search(rest)
        if mv:
            prev[n] = (mv.group(2), num(mv.group(3)))
            if z - prev[n][1] != num(mv.group(1)): bad.append(n + ': delta does not recompute')
        elif 'unchanged' in rest: prev[n] = (d, z)
        else: bad.append(n + ': neither "unchanged" nor "MOVED ... (was ...)"')
    if len(base) != 6 or len(new) != 6: bad.append('rows: baseline %d, notice %d -- both must be 6' % (len(base), len(new)))
    bad += [n + ': previous value != baseline' for n in base if prev.get(n) != base[n]]
    return bad
def control_text(text):
    for line in text.splitlines():
        m = ROW.match(line)
        if not m: continue
        mv = MOV.search(m.group(4)); d = mv.group(2) if mv else m.group(2)
        return text.replace(line, line.replace(d, d[:-1] + ('0' if d[-1] != '0' else '1')), 1)
    return text
base = baseline(open(sys.argv[1]).read()); text = open(sys.argv[2]).read()
bad = check(base, text); ctl = check(base, control_text(text))
print('notice vs baseline:', 'MATCH' if not bad else bad)
print('control (one digit off):', 'FAILS as it must' if ctl else 'PASSES -- THE CHECK IS BROKEN')
sys.exit(0 if (not bad and ctl) else 1)
