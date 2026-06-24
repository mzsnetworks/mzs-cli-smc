# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Repository Purpose

A **multi-platform social media content system** for technical posts. The core workflow: write one idea once, then render it natively for **LinkedIn, Instagram, and X**. Same message, platform-correct packaging.

Niche: network engineering, infrastructure, automation, AIOps. Audience: practitioners and technical leaders, but **engagement-oriented** (reach matters here, unlike a repel-mode personal blog).

This is an editorial system, not a software project. The "code" is markdown agents and rule files.

## How It Works

One idea flows through a pipeline and comes out as three platform-native posts:

```
[ Research --> Ideation --> Hook ] --> Writer --> Factcheck --> Platform Adapter --> Editor (x3) --> Hashtag (x3) --> Scorer (x3)
```

- **Research** *(optional)* finds dated, cited niche stories via WebSearch — no scraping
- **Ideation** *(optional)* crosses content pillars × formats into a 30+ idea matrix
- **Hook** *(optional)* generates credible (non-clickbait) hook options for an idea
- **Writer** drafts the master post (LinkedIn-length source)
- **Factcheck** verifies every stat against a cited source (BLOCKING — never adapt an unverified master)
- **Platform Adapter** renders LinkedIn / Instagram / X, preserving the "spine"
- **Editor** tightens each render to its platform length
- **Hashtag** applies per-platform hashtag policy
- **Scorer** scores each render and gates publish (SHIP / REVISE / REWORK)

The bracketed front-end runs only when you don't already have an idea. **On-demand agents** (not pipeline gates): **Voice** (build `rules/VOICE.md` author profile), **Formatter** (PAS/AIDA/BAB/STAR/SLAY skeletons), **Visual** (Canva carousel/infographic, Gemini fallback for hand-drawn), **Reels** (short-form video script). Full mechanics in `agents/PIPELINE.md`.

### How the system is invoked

Three layers, same logic underneath:

1. **Plain English** — the user just says what they want ("write a post about X", "give me ideas"). Match the intent to the right agent(s) and run them.
2. **Skills** (`.claude/skills/`) — auto-trigger the standalone capabilities: `build-voice`, `ideate`, `hook`, `niche-research`, `visual`, `reels`. Each skill is a thin trigger that reads its canonical `agents/*.md` and executes it.
3. **Commands** (`.claude/commands/`) — explicit multi-step workflows: **`/post <topic>`** runs the full core pipeline (Writer→Scorer); **`/adapt <slug>`** re-renders an existing master.

`agents/*.md` files remain the **source of truth** — skills and commands point to them, never fork the logic. The core pipeline agents (Writer, Factcheck, Adapter, Editor, Hashtag, Scorer) are invoked *through* `/post`, not as individual skills.

## Repository Structure

```
rules/
  SHARED.md        # niche, voice, fact discipline — applies to every platform
  LINKEDIN.md      # long-form, near-zero emoji, 2-3 hashtags, Sources block
  INSTAGRAM.md     # caption + carousel, purposeful emoji, 10-15 hashtag block
  X.md             # 280-char single or thread, sparing emoji, 1-2 hashtags
  VOICE.md         # author voice profile (created by the Voice agent; optional)
agents/            # canonical agent logic (source of truth)
  # core pipeline
  WRITER.md  FACTCHECK.md  PLATFORM_ADAPTER.md  EDITOR.md  HASHTAG.md  SCORER.md  PIPELINE.md
  # idea front-end (optional)
  RESEARCH.md  IDEATION.md  HOOK.md
  # on-demand
  VOICE.md  FORMATTER.md  VISUAL.md  REELS.md
.claude/
  commands/        # /post (full pipeline), /adapt (re-render an existing master)
  skills/          # auto-triggered: build-voice, ideate, hook, niche-research, visual, reels
content/           # generated posts (idea-first layout)
```

## Output Layout (Non-Negotiable)

Posts are **idea-first**. One idea = one dated folder holding all its platform versions:

```
content/<year>/<YYYY-MM-DD>-<slug>/
  master.md      # fact-checked source (LinkedIn-length, full Sources block)
  linkedin.md    # publish-ready LinkedIn render
  instagram.md   # publish-ready Instagram render
  x.md           # publish-ready X render
```

- `<YYYY-MM-DD>` = intended publish/creation date (sorts chronologically)
- `<slug>` = short kebab-case handle from the idea's landing or thesis
- Never scatter the three renders across separate trees — they belong to one idea
- The Adapter writes the three renders as siblings of `master.md`, in the same folder

Reference set: `content/2026/2026-06-24-ai-makes-us-judges/` — the calibration examples the rules and agents are tuned to.

## Writing Rules

The one rule that never loosens: **every statistic must trace to a real, citable source.** Vendor forecasts name the firm and the year. Uncited stats get cut or reframed as judgment. Factcheck enforces this and blocks the pipeline.

Otherwise this system is engagement-oriented, NOT repel-mode:
- Emojis allowed per platform (heavy Instagram, sparing X, ~none LinkedIn)
- CTAs and closing questions allowed
- First-person and personal-anecdote openings allowed
- Threads, carousels, and long form where the platform supports them

Every post needs a strong **hook** in line one. The default shape is **hook → POV → cited data → judgment → memorable landing**. Protect the landing (often a triad or a real question).

## Origin

Adapted from the LinkedIn-LPM editorial system (a strict, repel-mode personal blog). This project kept that system's fact discipline and senior-engineer credibility, but loosened the voice for multi-platform reach and added the Platform Adapter as the core agent.
