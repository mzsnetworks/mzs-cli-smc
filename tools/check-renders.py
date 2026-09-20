#!/usr/bin/env python3
"""Validate a post's renders against the platform rules before publish.

    python3 tools/check-renders.py <postdir> [<postdir> ...]
    python3 tools/check-renders.py --all

Lane is inferred from the path: content/ expects linkedin, facebook, instagram
and x; marketing/ expects linkedin and linkedin-es. Exits non-zero if anything
fails, so it can gate a publish.

Every rule here exists because it was violated in a real post. See the
FAILURE HISTORY notes on each check.

This checks TEXT ONLY. It cannot look at a carousel slide or a hero image,
and the most expensive visual failure is semantic rather than mechanical —
an image that is well executed and argues the opposite of its post. That
check is human, and it lives in agents/VISUAL.md under QA step (a).
"""
import re, sys, json, glob, os, subprocess

# --- FAILURE HISTORY: markdown emphasis shipped to LinkedIn in the Sep 6-18
# Business batch and again in every Instagram caption in the Oct 11 batch.
# None of these platforms render markdown; the asterisks publish literally.
MARKDOWN = re.compile(r'\*\*?[^*\n]+\*\*?|`[^`\n]+`|(?<!\w)_[^_\n]+_(?!\w)')

# --- FAILURE HISTORY: a suffix pattern (\w*ised) flagged "raised" and "advised"
# as British while missing "cancelled" and "artefacts". Explicit list only.
BRITISH = {
 'organisation','organisations','organisational','organise','organised','organising',
 'centre','centres','programme','programmes','practise','practised','practising',
 'standardise','standardised','standardises','utilise','utilised','prioritise','prioritised',
 'behaviour','behaviours','favour','favourite','colour','colours','neighbour','neighbours',
 'cancelled','cancelling','artefact','artefacts','defence','licence','catalogue',
 'analyse','analysed','analysing','recognise','recognised','optimise','optimised',
 'realise','realised','apologise','travelling','labelled','modelling','signalling','rumour',
}

# FAILURE HISTORY: a word set cannot catch "on holiday" or "whilst" in context.
BRITISH_PHRASES = [
 'on holiday', 'whilst', 'fortnight', 'learnt', 'spelt', 'amongst',
 'in hospital', 'car park', 'have got to', 'different to',
]

CTA_EN = ("Book a consultation: mzsnetworks.com", "Talk to an engineer: mzsnetworks.com")
CTA_ES = ("Reserve una consulta: mzsnetworks.com", "Hable con un ingeniero: mzsnetworks.com")

# name: (min, max, draft_target, fold, tag_min, tag_max)
#
# FAILURE HISTORY / why these numbers. Measured across every render in the repo:
# output clusters 1-5% under whatever number is ENFORCED and never approaches a
# number that is merely stated. Facebook sat at 774-798 against a prose cap of
# 800 for two months; the first batch written against an enforced warn-at-750
# landed at 621-711. LinkedIn has 17 published renders at 2001-2090 against a
# prose "sweet spot" ceiling of 2000. So the max below is deliberately set BELOW
# where the output should land, not at the outer limit of what the platform
# tolerates. Do not "relax" these to match a platform cap -- that is the change
# that caused the overruns.
SPEC = {
 'linkedin.md':    (1300, 1900, '1600-1850', 210, 2, 3),
 'facebook.md':    (400,   760, '550-700',   477, 0, 2),
 # Instagram splits by whether the post carries a carousel. A caption under ten
 # slides needs to carry the argument; a caption under one image does not.
 # rules/INSTAGRAM.md said 125-220 while every post ever written was 650-2000 --
 # the rule and the practice had never agreed. Resolved 2026-09-20.
 'instagram.md':   (0,     900, '600-900',   125, 5, 5),   # carousel-bearing
 'instagram-solo': (100,   400, '125-220',   125, 5, 5),   # image-only post
 # A Professional post is hero-only by design -- no slides. With nothing else
 # carrying the idea on Instagram, its caption IS the post, so the image-only
 # band would delete the format. Its own band instead. Set 2026-09-20 after
 # 26 posts drifted 596 -> 2080 with nothing enforcing a ceiling.
 'instagram-pro':  (600,  1600, '900-1400',   125, 5, 5),   # hero-only, caption carries the argument
 'linkedin-es.md': (1500, 2200, '1700-2000', 210, 2, 3),
}

def sentences(par):
    """Count sentence terminators. Spanish inverted marks open but do not
    terminate, so only . ! ? at a boundary count. Bullet lines are counted as
    one sentence each so a bulleted paragraph does not read as zero."""
    t = re.sub(r'\b(?:Mr|Mrs|Ms|Dr|Sr|Sra|vs|etc|i\.e|e\.g|a\.m|p\.m)\.', 'X', par)
    # Normalize quote-adjacent punctuation before counting. English puts the
    # period inside the quote ("the config parses.") and Spanish puts it
    # outside ("la configuración compila".) -- counting raw produced four
    # false positives on real posts from that convention alone.
    t = re.sub(r'([.!?])["\u2019\u201d\u00bb]', r'\1', t)      # ." -> .
    t = re.sub(r'["\u2019\u201d\u00bb]([.!?])', r'\1', t)      # ". -> .
    n = len(re.findall(r'[.!?](?=\s|$)', t))
    bullets = len([l for l in par.split('\n') if l.lstrip().startswith(('—', '-', '•', '→'))])
    return max(n, bullets)

def body(path, strip_notes=True):
    lines = open(path, encoding='utf-8').read().split('\n')
    while lines and (lines[0].startswith('# ') or not lines[0].strip()):
        lines.pop(0)
    t = '\n'.join(lines).strip()
    if strip_notes and 'instagram' in os.path.basename(path):
        t = t.split('\n---\n')[0].strip()   # drop "carousel slide ideas"
    return t

def check_file(path, lane, fails, warns, carousel=True, preset=None):
    f = os.path.basename(path)
    rel = os.path.join(os.path.basename(os.path.dirname(path)), f)

    if f == 'x.md':
        raw = body(path, strip_notes=False)
        if '## Single' not in raw:
            fails.append(f"{rel}: no '## Single' section"); return
        single = raw.split('## Single', 1)[1]
        single = '\n'.join(single.split('\n')[1:])          # drop the rest of the heading line
        single = re.split(r'\n##\s|\n---\n', single)[0].strip()
        if len(single) > 280:
            fails.append(f"{rel}: single post {len(single)} > 280")
        tags = re.findall(r'(?<!\w)#\w+', single)
        if not 1 <= len(tags) <= 2:
            fails.append(f"{rel}: single has {len(tags)} hashtags, want 1-2")
        if '## Thread' in raw:
            thread = raw.split('## Thread')[1]
            for t in re.findall(r'^\d+/.*?(?=\n\n\d+/|\Z)', thread, re.S | re.M):
                if len(t.strip()) > 280:
                    fails.append(f"{rel}: thread tweet {len(t.strip())} > 280 — {t.strip()[:40]!r}")
        targets = [single]
    else:
        key = f
        if f == 'instagram.md' and not carousel:
            # 'lane' collapses professional and business into 'content', so the
            # preset is what distinguishes a hero-only Professional post (whose
            # caption carries the argument) from a plain image-only one.
            key = 'instagram-pro' if preset == 'professional' else 'instagram-solo'
        lo, hi, draft, fold, tmin, tmax = SPEC[key]
        b = body(path)
        n = len(b)
        if not lo <= n <= hi:
            fails.append(f"{rel}: {n} chars outside {lo}-{hi} (draft target {draft})")
        else:
            # Warn on every platform, not just Facebook. This rule was
            # Facebook-only until 2026-09-20, which is why LinkedIn renders
            # clustered just under the 1900 FAIL line instead of inside the
            # 1600-1850 target: the only number being enforced was the cap.
            draft_hi = int(draft.split('-')[1])
            if n > draft_hi:
                warns.append(f"{rel}: {n} chars — inside the cap but above the {draft} draft target")
        lines = [l for l in b.split('\n') if l.strip()]
        if lines and len(lines[0]) > fold:
            fails.append(f"{rel}: hook {len(lines[0])} chars, fold is {fold}")
        tags = re.findall(r'(?<!\w)#\w+', b)
        if not tmin <= len(tags) <= tmax:
            fails.append(f"{rel}: {len(tags)} hashtags, want {tmin}-{tmax} — {tags}")
        # FAILURE HISTORY: "change window #47" in a Sep 14 post linkified as a
        # hashtag, giving that render a fourth tag nobody intended.
        stray = [t for t in tags if re.fullmatch(r'#\d+\w*', t)]
        if stray:
            fails.append(f"{rel}: {stray} reads as a hashtag — rephrase (\"window 47\", \"the 47th window\")")
        # FAILURE HISTORY: Blotato rejects a 6th IG tag; an inline #3 counts.
        if f == 'instagram.md':
            tagline = [l for l in lines if l.strip().startswith('#')]
            inline = len(tags) - (len(tagline[0].split()) if tagline else 0)
            if inline:
                fails.append(f"{rel}: {inline} hashtag(s) inline in the caption — they count against the cap of 5")
        if lane == 'marketing':
            cta = [l for l in lines if 'mzsnetworks.com' in l]
            want = CTA_ES if f.endswith('-es.md') else CTA_EN
            if not cta:
                fails.append(f"{rel}: marketing post has no CTA")
            elif cta[0].strip() not in want:
                fails.append(f"{rel}: CTA not an approved form — {cta[0].strip()!r}")
            if b.count('!'):
                fails.append(f"{rel}: exclamation mark — rules/MARKETING.md forbids them in body copy")
        targets = [b]

    for t in targets:
        for m in MARKDOWN.findall(t):
            fails.append(f"{rel}: markdown {m!r} — no platform renders it, it publishes literally")
        hit = {w.lower() for w in re.findall(r"[A-Za-z']+", t)} & BRITISH
        if hit:
            fails.append(f"{rel}: British spelling {sorted(hit)} — the corpus is American")
        low = t.lower()
        ph = [x for x in BRITISH_PHRASES if re.search(r'\b' + re.escape(x) + r'\b', low)]
        if ph:
            fails.append(f"{rel}: British usage {ph} — the corpus is American")

# --- Baseline -------------------------------------------------------------
# The length bands were tightened in 6f2f5a3 (2026-09-20T19:05-04:00) and the
# Professional Instagram band added in 1605cb7 shortly after. Posts written
# before that were written against different numbers and are not defects --
# reporting them makes --all cry wolf across 68 posts, which is how a checker
# gets ignored. A post is judged against the rules in force when it was
# written: first commit before the baseline means skip it.
#
# Deliberately NOT applied to a post named directly on the command line. If
# you ask about one post you get the truth about it, whatever its age.
BASELINE = '2026-09-20T19:05:38-04:00'

def _first_commit_dates():
    """folder -> ISO timestamp of the commit that first added any file in it."""
    try:
        out = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--format=C%cI', '--name-only',
             '--', 'content', 'marketing'],
            capture_output=True, text=True, timeout=60,
            cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))).stdout
    except (OSError, subprocess.SubprocessError):
        return {}
    first, cur = {}, None
    for line in out.splitlines():
        if line.startswith('C'):
            cur = line[1:]
        elif line.strip() and cur and '/' in line:
            d = os.path.dirname(line)
            if d.count('/') != 2:      # want <tree>/<year>/<slug>, not the file
                continue
            if d not in first or cur < first[d]:
                first[d] = cur
    return first

def pre_baseline(dirs):
    """Subset of dirs first committed before the bands changed."""
    first = _first_commit_dates()
    out = set()
    for d in dirs:
        key = os.path.normpath(d).strip('./')
        t = first.get(key)
        if t and t < BASELINE:
            out.add(d)
    return out

def preset_of(d):
    """Read the preset from master.md. content/ holds two presets with
    different render sets, so the tree alone does not determine them."""
    try:
        head = open(os.path.join(d, 'master.md'), encoding='utf-8').read()[:2000]
    except OSError:
        return 'unknown'
    m = re.search(r'^\*\*Preset:\*\*\s*(\w+)', head, re.M)
    return m.group(1).lower() if m else 'unknown'

RENDERS = {
 'marketing':    ['linkedin.md', 'linkedin-es.md'],
 'professional': ['linkedin.md', 'instagram.md'],
 'business':     ['linkedin.md', 'facebook.md', 'instagram.md', 'x.md'],
}

def check_post(d):
    d = d.rstrip('/')
    preset = preset_of(d)
    # Lane follows the preset, not the path: the path is wrong for fixtures and
    # for any folder that gets moved, and the preset is what actually decides
    # which rules apply.
    lane = 'marketing' if preset == 'marketing' else 'content'
    if preset not in RENDERS:
        # Unlabelled older post: check whatever renders it actually has.
        expect = [f for f in ('linkedin.md','facebook.md','instagram.md','x.md','linkedin-es.md')
                  if os.path.exists(os.path.join(d, f))]
    else:
        expect = RENDERS[preset]
    fails, warns = [], []
    carousel = bool(glob.glob(os.path.join(d, 'carousel-*.png'))) or \
               os.path.exists(os.path.join(d, 'carousel.json'))
    for f in expect:
        p = os.path.join(d, f)
        if not os.path.exists(p):
            fails.append(f"{os.path.basename(d)}/{f}: MISSING — the {lane} lane needs it")
            continue
        check_file(p, lane, fails, warns, carousel=carousel, preset=preset)

    # FAILURE HISTORY: on 2026-09-20 four marketing ES renders were expanded
    # without mirroring the addition into the English, and two shipped that way.
    # Two bugs in the first version of this check, both found 2026-09-20:
    #   1. it was gated behind `not fails`, so any other failure hid a parity break;
    #   2. it compared paragraph COUNTS, so the break that actually shipped -- a
    #      sentence appended INSIDE an existing paragraph -- passed clean.
    # Parity is now checked per paragraph by length ratio, and always runs.
    both = all(os.path.exists(os.path.join(d, f)) for f in ('linkedin.md', 'linkedin-es.md'))
    if lane == 'marketing' and both:
        en, es = body(os.path.join(d, 'linkedin.md')), body(os.path.join(d, 'linkedin-es.md'))
        pe = [p for p in en.split('\n\n') if p.strip()]
        ps = [p for p in es.split('\n\n') if p.strip()]
        name = os.path.basename(d)
        if len(pe) != len(ps):
            fails.append(f"{name}: EN/ES paragraph parity {len(pe)} vs {len(ps)} — both renders must carry the same beats")
        else:
            for i, (a_, b_) in enumerate(zip(pe, ps), 1):
                if a_.lstrip().startswith('#') or b_.lstrip().startswith('#'):
                    continue            # hashtag block: lengths legitimately differ
                # Sentence COUNT, not length. A sentence appended to a long
                # paragraph moves its length ratio by ~1.1 -- well inside any
                # band loose enough to tolerate Spanish running longer. The
                # count is structural and moves by exactly one.
                ca, cb = sentences(a_), sentences(b_)
                if ca != cb:
                    fails.append(f"{name}: paragraph {i} has {ca} sentence(s) in EN and {cb} in ES — one language carries content the other does not")
                    continue
                r = len(b_) / max(len(a_), 1)
                if not 0.80 <= r <= 1.90:
                    warns.append(f"{name}: paragraph {i} ES/EN length ratio {r:.2f} (EN {len(a_)}, ES {len(b_)})")
        r = len(es) / len(en)
        if r < 1.05 and len(es) < 1700:
            warns.append(f"{name}: overall ES/EN ratio {r:.2f}, ES {len(es)} chars — the Spanish may be tracking the English sentence for sentence")
    return fails, warns

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(2)
    everything = '--everything' in args
    args = [a for a in args if a != '--everything']
    sweep = args and args[0] == '--all'
    dirs = sorted(glob.glob('content/*/*/') + glob.glob('marketing/*/*/')) if sweep else args
    skipped = set()
    if sweep and not everything:
        # Judge a post against the rules in force when it was written. Never
        # applied to a post named explicitly -- ask about one post, get the
        # truth about it.
        skipped = pre_baseline(dirs)
        dirs = [d for d in dirs if d not in skipped]
    allf, allw = [], []
    for d in dirs:
        if not os.path.exists(os.path.join(d.rstrip('/'), 'master.md')):
            continue
        f, w = check_post(d)
        allf += f; allw += w
        if f or w:
            print(f"--- {d.rstrip('/')}")
            for x in f: print(f"  FAIL  {x}")
            for x in w: print(f"  warn  {x}")
    note = ''
    if skipped:
        note = (f" · {len(skipped)} pre-baseline post(s) skipped"
                f" (written before the bands changed; --everything includes them)")
    print(f"\n{len(dirs)} post(s) checked · {len(allf)} failure(s) · {len(allw)} warning(s){note}")
    print("OK — safe to publish" if not allf else "NOT SAFE TO PUBLISH")
    sys.exit(1 if allf else 0)

if __name__ == '__main__':
    main()
