#!/usr/bin/env python3
"""Test tools/check-renders.py against tools/fixtures/.

    python3 tools/test-check-renders.py

Exists because the first version of the checker shipped with three bugs that
were found by running it on real posts rather than by testing it: it assumed
content/ meant all four renders (so every Professional post falsely failed),
it mis-parsed x.md files whose thread heading carried a suffix, and its
EN/ES parity check was gated behind `not fails` so any other failure hid a
parity break.

Rule for this repo: no change to check-renders.py lands without a fixture
here that fails before the change and passes after.
"""
import sys, os, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
spec = importlib.util.spec_from_file_location("cr", os.path.join(HERE, "check-renders.py"))
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)

# fixture -> substring that must appear in at least one FAILURE (None = must be clean)
CASES = {
    'clean-business':            None,
    'clean-professional':        None,
    'clean-professional-solo':   None,
    'clean-marketing':           None,
    # EN puts the period inside the quote, ES outside. Identical content,
    # and the sentence-count parity check must not call that a break.
    'clean-marketing-quotes':    None,
    'fail-markdown':             'markdown',
    'fail-numeric-hashtag':      'reads as a hashtag',
    'fail-length-fb':            'chars outside 400-760',
    'fail-hashtag-count':        'hashtags, want 2-3',
    'fail-british':              'British',
    'fail-x-over-280':           '> 280',
    'fail-parity-inparagraph':   'sentence(s) in EN',
    'fail-missing-render':       'MISSING',
}

def main():
    os.chdir(ROOT)
    bad = 0
    for name, expect in CASES.items():
        d = os.path.join('tools', 'fixtures', name)
        if not os.path.isdir(d):
            print(f"  MISSING FIXTURE  {name}"); bad += 1; continue
        fails, warns = cr.check_post(d)
        if expect is None:
            if fails:
                print(f"  FAIL  {name}: expected clean, got {fails}"); bad += 1
            else:
                print(f"  ok    {name}: clean")
        else:
            if any(expect in f for f in fails):
                print(f"  ok    {name}: caught {expect!r}")
            else:
                print(f"  FAIL  {name}: expected a failure containing {expect!r}, got {fails or 'nothing'}")
                bad += 1
    print(f"\n{len(CASES)} case(s) · {bad} failing")
    if bad:
        print("CHECKER IS BROKEN — do not rely on it until this passes")
    else:
        print("checker behaves as specified")
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
