#!/usr/bin/env python3
"""PostToolUse hook: validate a render the moment it is written.

Until this existed, a render was only checked when somebody remembered to run
the checker before publishing. That is how markdown emphasis reached three
live Instagram captions in one batch: the ad-hoc check only looked at
LinkedIn. The feedback loop belongs at the edit, not at the publish.

Non-blocking by design. PostToolUse fires after the write has happened, so
there is nothing to block; this just puts the result in front of Claude
immediately, while the edit is still the thing being worked on.
"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RENDERS = {'linkedin.md', 'linkedin-es.md', 'facebook.md', 'instagram.md', 'x.md'}

def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)
    path = (data.get('tool_input') or {}).get('file_path') or ''
    if os.path.basename(path) not in RENDERS:
        sys.exit(0)
    postdir = os.path.dirname(path)
    if not os.path.exists(os.path.join(postdir, 'master.md')):
        sys.exit(0)
    r = subprocess.run([sys.executable, 'tools/check-renders.py', postdir],
                       capture_output=True, text=True, cwd=ROOT, timeout=60)
    # Only the per-render lines matter. The summary line always contains the
    # word "warning(s)", so matching on the raw output reports clean posts.
    out = '\n'.join(l for l in r.stdout.splitlines()
                    if l.startswith('  FAIL') or l.startswith('  warn'))
    if not out:
        sys.exit(0)
    print(json.dumps({"systemMessage":
        f"check-renders.py on {os.path.basename(postdir)}:\n{out}"}))
    sys.exit(0)

if __name__ == '__main__':
    main()
