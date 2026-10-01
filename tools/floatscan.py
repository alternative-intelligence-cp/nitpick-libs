#!/usr/bin/env python3
r"""Float exposure scan for the work repositories.   usage: ... | floatscan.py   (one .npk path per line on stdin)
Reports every float TYPE (`flt32`, `flt64`, `flt128`) and every float LITERAL (`1.5`, `2.0f64`, `3f32`, `1e10`)
in CODE, with `//` and `/* */` comments and string and character literals stripped first, so a version number
in a comment or a "2.5" in a string is not a site. Exit 0 always; the count is the result.

THE CONTROL, run before trusting a zero: a file holding `flt64:x = 1.5f64;`, `int64:n = 3e10;` and
`fixed flt32:Y = 3f32;` beside `// version 0.1.3 and 2.5` and `"2.5"` must report 2 types and 3 literals and
nothing from its comment or its string. The repositories, discovered rather than listed:
  { for t in ./nitpick-parse ./nitpick-regex ./nitpick-sockets ./nitpick-time ./nitpick-tui \
      ../nitpick-apps/nitpick-posix .; do git -C "$t" ls-files '*.npk' | sed "s|^|$t/|"; done; } \
    | python3 -B tools/floatscan.py
Written by nitpick-libs_11 on 2026-10-01 for notice 91 (DEF-205), re-measuring F33's scan, which predated
regex's 0.1.3 commits: 280 files, 0 sites, the control 2 + 3. Re-run it when a float notice arrives and
the last count predates the newest library commit."""
import re, sys
TYPE = re.compile(r'\bflt(?:32|64|128)\b')
LIT = re.compile(r'(?<![\w.])\d[\d_]*\.\d[\d_]*(?:[eE][+-]?\d+)?(?:f(?:32|64|128))?(?![\w.])'
                 r'|(?<![\w.])\d[\d_]*(?:[eE][+-]?\d+)?f(?:32|64|128)\b'
                 r'|(?<![\w.])\d[\d_]*[eE][+-]?\d+\b')
def strip(src):
    out, i, n = [], 0, len(src)
    while i < n:
        c = src[i]
        if src.startswith('//', i):
            j = src.find('\n', i); i = n if j < 0 else j; continue
        if src.startswith('/*', i):
            j = src.find('*/', i + 2); i = n if j < 0 else j + 2; continue
        if c in '"\'':
            q, j = c, i + 1
            while j < n and src[j] != q and src[j] != '\n':
                j += 2 if src[j] == '\\' else 1
            out.append(' '); i = j + 1; continue
        out.append(c); i += 1
    return ''.join(out)
def scan(paths):
    hits = []
    for p in paths:
        code = strip(open(p, encoding='utf-8', errors='replace').read())
        for ln, line in enumerate(code.splitlines(), 1):
            for m in TYPE.finditer(line): hits.append((p, ln, 'type', m.group(0)))
            for m in LIT.finditer(line): hits.append((p, ln, 'literal', m.group(0)))
    return hits
if __name__ == '__main__':
    paths = [l.strip() for l in sys.stdin if l.strip()]
    hits = scan(paths)
    print(f'{len(paths)} files scanned, {len(hits)} float site(s)')
    for h in hits[:40]: print('  %s:%d %s %s' % h)
