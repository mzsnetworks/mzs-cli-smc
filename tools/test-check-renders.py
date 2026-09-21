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
    # Business post with no carousel -> instagram-solo (125-220 teaser).
    'clean-business-solo':       None,
    # Professional post: hero-only by design, so the caption carries the
    # argument -> instagram-pro (900-1400), not the image-only band.
    'clean-professional-hero':   None,
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

# fixture -> substring that must appear in at least one WARNING (and no failure)
WARN_CASES = {
    # Inside the FAIL band but above the draft ceiling. Until 2026-09-20 this
    # warning was Facebook-only, which let LinkedIn drift to just under its cap.
    'warn-above-draft-target':   'above the 1600-1850 draft target',
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
    for name, expect in WARN_CASES.items():
        d = os.path.join('tools', 'fixtures', name)
        if not os.path.isdir(d):
            print(f"  MISSING FIXTURE  {name}"); bad += 1; continue
        fails, warns = cr.check_post(d)
        if fails:
            print(f"  FAIL  {name}: expected only a warning, got failures {fails}"); bad += 1
        elif any(expect in w for w in warns):
            print(f"  ok    {name}: warned {expect!r}")
        else:
            print(f"  FAIL  {name}: expected a warning containing {expect!r}, got {warns or 'nothing'}")
            bad += 1

    # diff_render is pure, so it is tested directly rather than through git.
    # The first case is the real 2026-09-20 defect: a hashtag silently swapped
    # on an already-scored render, with the body untouched.
    DIFF_CASES = [
        ("silent hashtag swap",
         "# LinkedIn\n\n\nBody stays identical.\n\n#NetOps #InfrastructureAsCode",
         "# LinkedIn\n\n\nBody stays identical.\n\n#NetOps #NetDevOps",
         dict(changed=True, tags_added=['#NetDevOps'],
              tags_removed=['#InfrastructureAsCode'], text_changed=False)),
        ("body edit, tags untouched",
         "# LinkedIn\n\n\nThe original sentence.\n\n#NetOps",
         "# LinkedIn\n\n\nA rewritten sentence.\n\n#NetOps",
         dict(changed=True, tags_added=[], tags_removed=[], text_changed=True)),
        ("heading-only change is not a change",
         "# LinkedIn — old-slug\n\n\nSame body.\n\n#NetOps",
         "# LinkedIn — new-slug\n\n\nSame body.\n\n#NetOps",
         dict(changed=False, tags_added=[], tags_removed=[], text_changed=False)),
    ]
    for name, old, new, want in DIFF_CASES:
        got = cr.diff_render(old, new)
        if all(got[k] == v for k, v in want.items()):
            print(f"  ok    diff: {name}")
        else:
            print(f"  FAIL  diff: {name} — wanted {want}, got {got}")
            bad += 1
    # Instagram carousel notes live below a --- and must not count as a change.
    ig_old = "# Instagram\n\n\nCaption.\n\n#A #B #C #D #E\n\n---\n\n## Carousel slide ideas\n1. Old idea"
    ig_new = "# Instagram\n\n\nCaption.\n\n#A #B #C #D #E\n\n---\n\n## Carousel slide ideas\n1. New idea"
    if not cr.diff_render(ig_old, ig_new, is_instagram=True)['changed']:
        print("  ok    diff: instagram slide notes ignored")
    else:
        print("  FAIL  diff: instagram slide notes counted as a copy change")
        bad += 1

    # Baseline filter. Fixtures cannot exercise this (it reads git history for
    # content/ and marketing/), so assert against two real posts: one written
    # before the bands changed and one after.
    OLD = 'content/2026/2026-10-03-on-call-makes-careers/'
    NEW = 'content/2026/2026-10-24-bought-and-never-enabled/'
    if os.path.isdir(OLD) and os.path.isdir(NEW):
        skipped = cr.pre_baseline([OLD, NEW])
        if OLD in skipped and NEW not in skipped:
            print("  ok    baseline: pre-baseline post skipped, post-baseline post kept")
        else:
            print(f"  FAIL  baseline: expected only {OLD} skipped, got {skipped}")
            bad += 1
        # An explicitly named post is never filtered -- ask about one post,
        # get the truth about it regardless of age.
        f, _ = cr.check_post(OLD)
        if f:
            print("  ok    baseline: explicit post still reports its failures")
        else:
            print("  FAIL  baseline: explicit pre-baseline post reported clean")
            bad += 1
    else:
        print("  skip  baseline: reference posts not present")

    print(f"\n{len(CASES) + len(WARN_CASES) + 6} case(s) · {bad} failing")
    if bad:
        print("CHECKER IS BROKEN — do not rely on it until this passes")
    else:
        print("checker behaves as specified")
    sys.exit(1 if bad else 0)

if __name__ == '__main__':
    main()
