# Social Media Content System (claude-cli-smc)

A multi-platform editorial system for technical social content. **Write one idea once, render it natively for LinkedIn, Instagram, and X** — each with its own voice, length, emoji policy, and hashtag rules. Same message, platform-correct packaging.

The "code" here is markdown: agents and rule files Claude Code follows. There is nothing to install — you run the agents by pointing Claude at the right rule files and content.

- **Niche:** network engineering, infrastructure, automation, AIOps, operations.
- **Audience:** practitioners and technical leaders — but engagement-oriented (reach matters), not a repel-mode personal blog.
- **The one rule that never loosens:** every statistic must trace to a real, citable source. Factcheck enforces it and blocks the pipeline.

---

## The Pipeline

One idea flows through a pipeline and comes out as three platform-native posts.

```
[ Research --> Ideation --> Hook ] --> Writer --> Factcheck --> Platform Adapter --> Editor (x3) --> Hashtag (x3) --> Scorer (x3)
       optional idea front-end            ^            |
                                          |  (on FAIL) |
                                          +-----<------+

On-demand (not gates):  Voice (setup)   Formatter   Visual (Canva)   Reels
```

The **front-end** (Research → Ideation → Hook) runs only when you don't already have an idea. The **core** (Writer → Scorer) takes one idea to three publish-ready posts. **On-demand** agents are run when a post calls for them.

---

## The Agents

| Agent | Stage | Edits files? | Job |
|-------|-------|--------------|-----|
| **Research** | front-end | no | Find dated, cited niche stories via WebSearch (no scraping) |
| **Ideation** | front-end | no | Cross content pillars × formats into a 30+ idea matrix |
| **Hook** | front-end | no | Generate 6 credible (non-clickbait) hook options for an idea |
| **Writer** | core | yes | Draft the master post (LinkedIn-length) in the author's voice |
| **Factcheck** | core | no | Verify every stat against its source — PASS/FAIL (blocking) |
| **Platform Adapter** | core | yes | Render the master into LinkedIn / Instagram / X |
| **Editor** | core | yes | Tighten each render to its platform length target |
| **Hashtag** | core | yes (append) | Apply per-platform hashtag policy |
| **Scorer** | core | no | Score each render 0–100 and gate publish (SHIP/REVISE/REWORK) |
| **Voice** | on-demand | yes (`rules/VOICE.md`) | Build the author voice profile (run once at setup) |
| **Formatter** | on-demand | yes | Impose a named framework (PAS/AIDA/BAB/STAR/SLAY) on a draft |
| **Visual** | on-demand | yes (exports) | Design a carousel/infographic in Canva (Gemini fallback) |
| **Reels** | on-demand | yes (script) | Write a 30–45s short-form video script from an idea |

Each agent file in `agents/` ends with a **Usage** block — the exact prompt to run it. The how-to below stitches them into workflows.

---

## How to Use

There is no CLI to run. You drive the system by telling Claude Code which agent to apply and which files to read. Copy the prompts below.

### One-time setup — build your voice

Run this first, once. It interviews you and writes `rules/VOICE.md`, the author voice profile every writing agent then applies automatically.

```
Apply the VOICE agent: run the interview, then write rules/VOICE.md.
```

Answer the six questions (background, defended opinions, war stories, writers you respect, voice fingerprint, content pillars). Re-run or edit `rules/VOICE.md` whenever your style shifts. If the file doesn't exist, agents fall back to the generic voice in `rules/SHARED.md`.

### Quick start — you already have an idea

Pick a date and a short kebab-case slug, then set `DIR = content/<year>/<YYYY-MM-DD>-<slug>/`. Drop a rough draft or notes into `DIR/master.md` and run the core pipeline:

```
1. Read rules/SHARED.md, rules/LINKEDIN.md, rules/VOICE.md, and DIR/master.md.
   Apply the WRITER agent. Edit the file directly.

2. Read rules/SHARED.md and DIR/master.md.
   Apply the FACTCHECK agent. Output PASS/FAIL. Loop with the Writer until PASS.

3. Read rules/SHARED.md, all rules/ platform files, and rules/VOICE.md, plus DIR/master.md.
   Apply the PLATFORM_ADAPTER agent: write DIR/linkedin.md, DIR/instagram.md, DIR/x.md.

4. For each render: read rules/[PLATFORM].md, rules/VOICE.md, and DIR/[platform].md.
   Apply the EDITOR agent: tighten to the platform Length Target. Edit directly.

5. For each render: read rules/[PLATFORM].md and DIR/[platform].md.
   Apply the HASHTAG agent. Append only.

6. For each render: read rules/SHARED.md, rules/[PLATFORM].md, and DIR/[platform].md.
   Apply the SCORER agent. Loop back to Editor/Writer until SHIP (>=85).
```

When all three renders score **SHIP**, they're publish-ready in `DIR/`.

### Full start — you need an idea first

```
A. Apply the RESEARCH agent: WebSearch the niche for the last 14 days.
   Return dated, linked stories with shareable angles.

B. Read rules/SHARED.md and rules/VOICE.md. Apply the IDEATION agent:
   emit a 30+ row pillar x format matrix plus a Top 5. (Optionally feed it the Research list.)

C. Pick an idea. Read rules/SHARED.md and rules/VOICE.md.
   Apply the HOOK agent to that idea: 6 credible hooks, recommend one.

D. Run the Quick Start pipeline above with the chosen idea + hook.
```

### On-demand recipes

**Add a visual (carousel or infographic):**
```
Read the post at DIR/ and rules/SHARED.md and rules/VOICE.md.
Apply the VISUAL agent: route to carousel/infographic, build a brief, get approval,
then design in Canva via the Canva MCP and export into DIR/.
```
Canva is the design engine. Gemini is only used for the hand-drawn whiteboard look.

**Write a short-form video script:**
```
Read rules/SHARED.md, rules/INSTAGRAM.md, rules/VOICE.md, and DIR/master.md.
Apply the REELS agent: write a 30–45s script with caption, comment trigger, and visual notes.
```

**Force a copywriting framework onto a draft:**
```
Read rules/SHARED.md, rules/LINKEDIN.md, rules/VOICE.md, and the draft.
Apply the FORMATTER agent with framework [PAS/AIDA/BAB/STAR/SLAY].
```

---

## Rules & Voice

Everything an agent does is governed by the files in `rules/`:

- **`SHARED.md`** — niche, audience, voice baseline, **fact discipline**, the spine (hook → POV → data → judgment → landing), and the **per-platform Length Targets** table.
- **`LINKEDIN.md` / `INSTAGRAM.md` / `X.md`** — formatting that layers on top: length sweet spot, the "fold" the hook must clear, emoji policy, hashtag count.
- **`VOICE.md`** — *your* voice (pillars, defended opinions, signature phrasings, word list, war stories). Mandatory for every writing agent when it exists.

**Length Targets** (recommended, enforced by Editor + Scorer):

| Platform | Sweet spot | Hard cap | Fold (hook must land before) |
|----------|-----------|----------|------------------------------|
| LinkedIn | ~1,300–2,000 chars | ~3,000 | ~210 chars (~3 lines) |
| Instagram | ~125–220 chars caption (more if carousel) | ~2,200 | ~125 chars (first line) |
| X — single | ~240–270 chars | 280 | whole post visible |
| X — thread | ≤280/tweet, one idea per tweet | 280/tweet | tweet 1 is the hook |

---

## Output Layout (idea-first, non-negotiable)

One idea = one dated folder holding all its platform versions. Never scatter the renders across separate trees — they belong to one idea.

```
content/<year>/<YYYY-MM-DD>-<slug>/
  master.md      # fact-checked source (LinkedIn-length, full Sources block)
  linkedin.md    # publish-ready LinkedIn render
  instagram.md   # publish-ready Instagram render
  x.md           # publish-ready X render
  (carousel.png / infographic.png / reel-*.md — added on-demand)
```

- `<YYYY-MM-DD>` = intended publish/creation date (sorts chronologically).
- `<slug>` = short kebab-case handle from the idea's landing or thesis.

**Reference sets:**
- `content/2026/2026-06-24-ai-makes-us-judges/` — the original calibration examples the rules and agents are tuned to.
- `content/2026/2026-06-24-operational-state/` — first post written in the author's voice profile end-to-end (all three renders scored SHIP).

---

## Repository Layout

```
rules/
  SHARED.md  LINKEDIN.md  INSTAGRAM.md  X.md  VOICE.md
agents/
  WRITER.md  FACTCHECK.md  PLATFORM_ADAPTER.md  EDITOR.md  HASHTAG.md  SCORER.md   # core
  RESEARCH.md  IDEATION.md  HOOK.md                                                # front-end
  VOICE.md  FORMATTER.md  VISUAL.md  REELS.md                                      # on-demand
  PIPELINE.md                                                                      # run mechanics
content/
  <year>/<YYYY-MM-DD>-<slug>/master.md linkedin.md instagram.md x.md
```

---

## Origin

Adapted from the LinkedIn-LPM editorial system (a strict, repel-mode personal blog). This project kept that system's **fact discipline** and senior-engineer credibility, loosened the voice for multi-platform reach, and added the Platform Adapter as the core agent. The front-end, scoring, voice, and visual agents were adapted from the `charlie947/social-media-skills` repo — retuned to this niche, stripped of creator-vanity and clickbait, and de-coupled from external scraping tools.

**What carries over:** the niche, senior-practitioner credibility, and fact discipline (every stat cited).
**What's loosened:** emojis (per platform), CTAs and closing questions, first-person voice, threads/carousels/long-form where the platform supports them.
