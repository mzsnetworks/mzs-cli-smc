# Editorial Pipeline

How to run the agents to take one idea to its publish-ready posts.

**Two lanes share this pipeline.** The agents and their order never change; only the render set and a few rule files differ.

| Lane | Tree | Renders | Preset(s) | Extra rules |
|------|------|---------|-----------|-------------|
| Thought leadership | `content/` | `linkedin.md` `facebook.md` `instagram.md` `x.md` | Professional · Business | — |
| Marketing | `marketing/` | `linkedin.md` `linkedin-es.md` | Marketing | `rules/MARKETING.md` · `rules/SPANISH.md` |

Everything below reads "x4" for the `content/` lane and "x2" for the `marketing/` lane.

---

## Sequence

```
[ Research --> Ideation --> Hook ] --> Writer --> Factcheck --> Platform Adapter --> Editor (x4) --> Hashtag (x4) --> Scorer (x4) --> [ Publish ]
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
6. **Platform Adapter** renders the lane's versions — LinkedIn/Facebook/Instagram/X for `content/`, LinkedIn EN+ES for `marketing/` (writes the files)
7. **Editor** tightens each rendered version to its platform length (edits files)
8. **Hashtag** applies per-platform hashtag rules (append-only)
9. **Scorer** scores each render and gates publish — SHIP / REVISE / REWORK (no edits)
10. **Publish** *(on-demand, `/publish <slug>`)* posts SHIP renders live via Blotato — always behind an explicit per-run user confirmation

If Factcheck fails, send back to the Writer — fix or source the claim before adapting. Never adapt an unverified master; a bad stat would propagate to every render, in every language. If the Scorer returns REVISE/REWORK, loop back to the Editor (or Writer for structural misses).

### On-demand agents (not in the core sequence)

- **Voice** — run once at setup to build `rules/VOICE.md` (the author profile that feeds Writer/Ideation/Hook). Update when style shifts.
- **Formatter** — impose a named framework (PAS/AIDA/BAB/STAR/SLAY) on a draft when it needs a skeleton.
- **Visual** — produce the post's art: carousel/infographic rendered deterministically on-brand (`tools/render-*.mjs`), or a text-free AI hero image via the SMC Image Generator n8n webhook. Approval gate before generating.
- **Reels** — write a 30–45s video script from a finished idea.
- **Publish** — post a SHIP-gated idea live through Blotato (`/publish <slug>`). Asks whatever the preset leaves open — platforms, LinkedIn target, timing, X shape; the Marketing preset fixes all four and asks nothing but the confirmation. Shows final text and waits for explicit approval before anything goes live.

### Where files go

One idea is one dated folder. The Writer creates `master.md`; the Adapter writes the lane's renders beside it:

```
content/<year>/<YYYY-MM-DD>-<slug>/
  master.md  linkedin.md  facebook.md  instagram.md  x.md

marketing/<year>/<YYYY-MM-DD>-<slug>/
  master.md  linkedin.md  linkedin-es.md
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
| Visual | yes (specs + images) | Carousel/infographic (deterministic render) or AI hero image (on-demand) |
| Reels | yes (writes script) | Short-form video script (on-demand) |
| Publish | yes (`published.md`, INDEX) | Post SHIP renders live via Blotato (on-demand, gated) |

---

## Running the Full Pipeline

Let `DIR = <tree>/<year>/<YYYY-MM-DD>-<slug>/` for the idea, where `<tree>` is `content` or `marketing`.

For a `marketing/` idea, every step below also reads `rules/MARKETING.md`, and the ES steps read `rules/SPANISH.md`.

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
Apply the PLATFORM_ADAPTER agent: write DIR/linkedin.md, DIR/facebook.md,
DIR/instagram.md, and DIR/x.md, preserving the spine.
```
*Marketing lane:*
```
Read rules/SHARED.md, rules/LINKEDIN.md, rules/MARKETING.md,
rules/SPANISH.md and DIR/master.md. Apply the PLATFORM_ADAPTER agent:
write DIR/linkedin.md, then compose DIR/linkedin-es.md in Spanish from
the master — never translated from the English render.
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

**Step 5b — Verify (mechanical, all renders at once)**
```
python3 tools/check-renders.py DIR
```
Checks length bands and draft targets, the hook against each platform's fold,
hashtag counts, markdown emphasis (no platform renders it), stray numeric
hashtags, American spelling, and for marketing posts the CTA form and EN/ES
paragraph parity. Exits non-zero on failure. Fix everything it reports before
scoring — the Scorer judges quality, this catches the mechanical faults that
have actually shipped.

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
3. Platform Adapter has produced all of the lane's render files with the spine intact — for marketing, both languages
4. Editor has tightened each to platform length
5. Hashtag has applied the correct per-platform tag policy
6. `python3 tools/check-renders.py DIR` passes with no failures
7. Scorer returns SHIP (≥85) on each render

Visuals (carousel/infographic) and a Reel script are produced on-demand via the Visual and Reels agents when a post calls for them — they are not gates.

Once every render is SHIP, `/publish <slug>` takes it live via the Publish agent — with its own explicit user-confirmation gate on the final text.
