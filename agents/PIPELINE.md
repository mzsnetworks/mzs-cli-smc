# Editorial Pipeline

How to run the agents to take one idea to three published-ready posts.

---

## Sequence

```
[ Research --> Ideation --> Hook ] --> Writer --> Factcheck --> Platform Adapter --> Editor (x3) --> Hashtag (x3) --> Scorer (x3)
                                         ^            |
                                         |  (on FAIL) |
                                         +-----<------+
```

The bracketed front-end is **idea generation** — run it when you don't already have an idea. The core pipeline (Writer onward) is unchanged.

1. **Research** *(optional)* finds dated, cited niche stories via WebSearch (no edits)
2. **Ideation** *(optional)* crosses pillars × formats into a 30+ idea matrix (no edits)
3. **Hook** *(optional)* generates 6 credible hook options for the chosen idea (no edits)
4. **Writer** drafts the master post (edits the master file)
5. **Factcheck** verifies every stat against its source (PASS/FAIL, no edits)
6. **Platform Adapter** renders LinkedIn / Instagram / X versions (writes the three files)
7. **Editor** tightens each rendered version to its platform length (edits files)
8. **Hashtag** applies per-platform hashtag rules (append-only)
9. **Scorer** scores each render and gates publish — SHIP / REVISE / REWORK (no edits)

If Factcheck fails, send back to the Writer — fix or source the claim before adapting. Never adapt an unverified master; a bad stat would propagate to all three platforms. If the Scorer returns REVISE/REWORK, loop back to the Editor (or Writer for structural misses).

### On-demand agents (not in the core sequence)

- **Voice** — run once at setup to build `rules/VOICE.md` (the author profile that feeds Writer/Ideation/Hook). Update when style shifts.
- **Formatter** — impose a named framework (PAS/AIDA/BAB/STAR/SLAY) on a draft when it needs a skeleton.
- **Visual** — design a carousel or infographic in Canva for a finished post; export into the idea folder.
- **Reels** — write a 30–45s video script from a finished idea.

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
| Research | no | Find dated, cited niche stories (optional front-end) |
| Ideation | no | Pillars × formats idea matrix (optional front-end) |
| Hook | no | 6 credible hook options for an idea (optional front-end) |
| Writer | yes | Draft the master post |
| Factcheck | no | Verify stats and claims |
| Platform Adapter | yes | Render per platform |
| Editor | yes | Tighten each version |
| Hashtag | yes (append) | Per-platform hashtags |
| Scorer | no | Score + publish gate (SHIP/REVISE/REWORK) |
| Voice | yes (`rules/VOICE.md`) | Build author voice profile (on-demand, setup) |
| Formatter | yes | Impose a named framework (on-demand) |
| Visual | yes (exports asset) | Canva carousel/infographic (on-demand) |
| Reels | yes (writes script) | Short-form video script (on-demand) |

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

**Step 6 — Scorer (per file)**
```
Read rules/SHARED.md, rules/[PLATFORM].md, and DIR/[platform].md.
Apply the SCORER agent: score 0–100, return SHIP/REVISE/REWORK with
line-level fixes. Do not edit. Loop back to Editor/Writer until SHIP.
```

---

## Ready to Publish When

1. Writer has produced a strong master with a hook, cited data, and a landing
2. Factcheck returns PASS (every stat sourced)
3. Platform Adapter has produced all three platform files with the spine intact
4. Editor has tightened each to platform length
5. Hashtag has applied the correct per-platform tag policy
6. Scorer returns SHIP (≥85) on each render

Visuals (carousel/infographic) and a Reel script are produced on-demand via the Visual and Reels agents when a post calls for them — they are not gates.
