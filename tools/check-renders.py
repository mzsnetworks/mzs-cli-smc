#!/usr/bin/env python3
"""Validate a post's renders against the platform rules before publish.

    python3 tools/check-renders.py <postdir> [<postdir> ...]
    python3 tools/check-renders.py --all

Lane is inferred from the path: content/ expects linkedin, facebook, instagram
and x; marketing/ expects linkedin and linkedin-es. Exits non-zero if anything
fails, so it can gate a publish.

Every rule here exists because it was violated in a real post. See the
FAILURE HISTORY notes on each check.
"""
import re, sys, json, glob, os

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

CTA_EN = ("Book a consultation: mzsnetworks.com", "Talk to an engineer: mzsnetworks.com")
CTA_ES = ("Reserve una consulta: mzsnetworks.com", "Hable con un ingeniero: mzsnetworks.com")

# name: (min, max, draft_target, fold, tag_min, tag_max)
SPEC = {
 'linkedin.md':    (1300, 2000, '1500-1800', 210, 2, 3),
 # FAILURE HISTORY: Facebook overran 800 on 6 of 6 Business posts written
 # 2026-09-20, every one needing two trim passes. 800 is the cap; draft to 650.
 'facebook.md':    (400,   800, '550-700',   477, 0, 2),
 'instagram.md':   (0,    2200, '600-900',   125, 5, 5),
 'linkedin-es.md': (1500, 2300, '1700-2000', 210, 2, 3),
}

def body(path, strip_notes=True):
    lines = open(path, encoding='utf-8').read().split('\n')
    while lines and (lines[0].startswith('# ') or not lines[0].strip()):
        lines.pop(0)
    t = '\n'.join(lines).strip()
    if strip_notes and 'instagram' in os.path.basename(path):
        t = t.split('\n---\n')[0].strip()   # drop "carousel slide ideas"
    return t

def check_file(path, lane, fails, warns):
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
        lo, hi, draft, fold, tmin, tmax = SPEC[f]
        b = body(path)
        n = len(b)
        if not lo <= n <= hi:
            fails.append(f"{rel}: {n} chars outside {lo}-{hi} (draft target {draft})")
        elif f == 'facebook.md' and n > 750:
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
    lane = 'marketing' if (d + '/').startswith('marketing/') or '/marketing/' in d + '/' else 'content'
    preset = preset_of(d)
    if preset not in RENDERS:
        # Unlabelled older post: check whatever renders it actually has.
        expect = [f for f in ('linkedin.md','facebook.md','instagram.md','x.md','linkedin-es.md')
                  if os.path.exists(os.path.join(d, f))]
    else:
        expect = RENDERS[preset]
    fails, warns = [], []
    for f in expect:
        p = os.path.join(d, f)
        if not os.path.exists(p):
            fails.append(f"{os.path.basename(d)}/{f}: MISSING — the {lane} lane needs it")
            continue
        check_file(p, lane, fails, warns)

    # FAILURE HISTORY: on 2026-09-20 four marketing ES renders were expanded
    # without mirroring the addition into the English, and two shipped that way.
    if lane == 'marketing' and not fails:
        en, es = body(os.path.join(d, 'linkedin.md')), body(os.path.join(d, 'linkedin-es.md'))
        pe = len([p for p in en.split('\n\n') if p.strip()])
        ps = len([p for p in es.split('\n\n') if p.strip()])
        if pe != ps:
            fails.append(f"{os.path.basename(d)}: EN/ES paragraph parity {pe} vs {ps} — both renders must carry the same beats")
        r = len(es) / len(en)
        if r < 1.05 and len(es) < 1700:
            warns.append(f"{os.path.basename(d)}: ES/EN ratio {r:.2f} and ES only {len(es)} chars — the Spanish is likely tracking the English sentence for sentence rather than breathing")
    return fails, warns

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); sys.exit(2)
    dirs = sorted(glob.glob('content/*/*/') + glob.glob('marketing/*/*/')) if args[0] == '--all' else args
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
    print(f"\n{len(dirs)} post(s) checked · {len(allf)} failure(s) · {len(allw)} warning(s)")
    print("OK — safe to publish" if not allf else "NOT SAFE TO PUBLISH")
    sys.exit(1 if allf else 0)

if __name__ == '__main__':
    main()
