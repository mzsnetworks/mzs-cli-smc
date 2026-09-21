#!/usr/bin/env python3
"""PreToolUse hook: refuse to publish a render that fails the checker.

FAILURE HISTORY. Publishing is irreversible, and three Instagram captions
went live with literal asterisks because the pre-publish check was run by
hand and only covered LinkedIn. agents/PUBLISH.md step 4 says to run the
checker; this makes it true whether or not anyone remembers.

blotato_create_post carries no path, only the finished text, so the post has
to be located by matching the first line of that text against the renders in
the repo. If no post matches -- a one-off, or text edited after scoring --
the hook allows the call rather than guessing. It fails open on purpose: a
publish gate that blocks work it does not understand gets disabled, and then
it protects nothing.
"""
import json, os, re, subprocess, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RENDERS = ('linkedin.md', 'linkedin-es.md', 'facebook.md', 'instagram.md', 'x.md')

def allow():
    sys.exit(0)

def deny(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason}}))
    sys.exit(0)

def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        allow()
    text = ((data.get('tool_input') or {}).get('text') or '').strip()
    if not text:
        allow()
    first = text.split('\n')[0].strip()
    if len(first) < 25:                      # too generic to match safely
        allow()
    hits = set()
    for f in RENDERS:
        for p in glob.glob(os.path.join(ROOT, 'content', '*', '*', f)) + \
                 glob.glob(os.path.join(ROOT, 'marketing', '*', '*', f)):
            try:
                if first in open(p, encoding='utf-8').read():
                    hits.add(os.path.dirname(p))
            except OSError:
                pass
    if len(hits) != 1:
        allow()                              # cannot identify the post: fail open
    postdir = hits.pop()
    r = subprocess.run([sys.executable, 'tools/check-renders.py',
                        os.path.relpath(postdir, ROOT)],
                       capture_output=True, text=True, cwd=ROOT, timeout=60)
    if r.returncode != 0:
        fails = '\n'.join(l.strip() for l in r.stdout.splitlines() if 'FAIL' in l)
        deny(f"check-renders.py fails on {os.path.basename(postdir)} — publishing "
             f"is irreversible, so fix the render first:\n{fails}")
    allow()

if __name__ == '__main__':
    main()
