# Editorial Pipeline

How to run the agents to take one idea to three published-ready posts.

---

## Sequence

```
Writer --> Factcheck --> Platform Adapter --> Editor (x3) --> Hashtag (x3)
  ^            |
  |  (on FAIL) |
  +-----<------+
```

1. **Writer** drafts the master post (edits the master file)
2. **Factcheck** verifies every stat against its source (PASS/FAIL, no edits)
3. **Platform Adapter** renders LinkedIn / Instagram / X versions (writes the three files)
4. **Editor** tightens each rendered version to its platform length (edits files)
5. **Hashtag** applies per-platform hashtag rules (append-only)

If Factcheck fails, send back to the Writer — fix or source the claim before adapting. Never adapt an unverified master; a bad stat would propagate to all three platforms.

### Where files go

One idea is one dated folder. The Writer creates `master.md`; the Adapter writes the three renders beside it:

```
content/<year>/<YYYY-MM-DD>-<slug>/
  master.md  linkedin.md  instagram.md  x.md
```

`<slug>` is a short kebab-case handle drawn from the idea's landing or thesis.

---

## Agent Roles

| Agent | Edits files? | Job |
|---|---|---|
| Writer | yes | Draft the master post |
| Factcheck | no | Verify stats and claims |
| Platform Adapter | yes | Render per platform |
| Editor | yes | Tighten each version |
| Hashtag | yes (append) | Per-platform hashtags |

---

## Running the Full Pipeline

Let `DIR = content/<year>/<YYYY-MM-DD>-<slug>/` for the idea.

**Step 1 — Writer**
```
Read rules/SHARED.md, rules/LINKEDIN.md, and the draft at DIR/master.md.
Apply the WRITER agent. Edit the file directly.
```

**Step 2 — Factcheck**
```
Read rules/SHARED.md and DIR/master.md.
Apply the FACTCHECK agent. Output PASS/FAIL. Do not edit.
```
Loop with the Writer until PASS.

**Step 3 — Platform Adapter**
```
Read rules/SHARED.md and all rules/ platform files, plus DIR/master.md.
Apply the PLATFORM_ADAPTER agent: write DIR/linkedin.md, DIR/instagram.md,
and DIR/x.md, preserving the spine.
```

**Step 4 — Editor (per file)**
```
Read rules/[PLATFORM].md and DIR/[platform].md. Apply the EDITOR agent:
tighten to platform length, keep hook/CTA/landing. Edit directly.
```

**Step 5 — Hashtag (per file)**
```
Read rules/[PLATFORM].md and DIR/[platform].md. Apply the HASHTAG agent
per that platform's rules. Append only.
```

---

## Ready to Publish When

1. Writer has produced a strong master with a hook, cited data, and a landing
2. Factcheck returns PASS (every stat sourced)
3. Platform Adapter has produced all three platform files with the spine intact
4. Editor has tightened each to platform length
5. Hashtag has applied the correct per-platform tag policy
