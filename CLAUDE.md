# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Repository Purpose

A **multi-platform social media content system** for technical posts. The core workflow: write one idea once, then render it natively for **LinkedIn, Facebook, Instagram, and X**. Same message, platform-correct packaging. Finished posts go live via **`/publish`** (Blotato MCP), always behind an explicit user confirmation.

**Two lanes** share one pipeline. `content/` is thought leadership — ends on a question, asks for nothing. `marketing/` is company marketing — ends on a CTA, names an MZS product or service, and ships **English + Spanish**. The agents and their order are identical; only the render set and a few rule files differ.

Niche: network engineering, infrastructure, automation, AIOps. Audience: practitioners and technical leaders, but **engagement-oriented** (reach matters here, unlike a repel-mode personal blog).

This is an editorial system, not a software project. The "code" is markdown agents and rule files.

## How It Works

One idea flows through a pipeline and comes out as platform-native posts — four for `content/`, two (English + Spanish LinkedIn) for `marketing/`:

```
[ Research --> Ideation --> Hook ] --> Writer --> Factcheck --> Platform Adapter --> Editor (x4) --> Hashtag (x4) --> Scorer (x4) --> [ Publish ]
```

- **Research** *(optional)* finds dated, cited niche stories via WebSearch — no scraping
- **Ideation** *(optional)* crosses content pillars × formats into a 30+ idea matrix
- **Hook** *(optional)* generates credible (non-clickbait) hook options for an idea
- **Writer** drafts the master post (LinkedIn-length source)
- **Factcheck** verifies every stat against a cited source (BLOCKING — never adapt an unverified master)
- **Platform Adapter** renders LinkedIn / Facebook / Instagram / X, preserving the "spine"
- **Editor** tightens each render to its platform length
- **Hashtag** applies per-platform hashtag policy
- **Scorer** scores each render and gates publish (SHIP / REVISE / REWORK)

The bracketed front-end runs only when you don't already have an idea. **On-demand agents** (not pipeline gates): **Voice** (build `rules/VOICE.md` author profile), **Formatter** (PAS/AIDA/BAB/STAR/SLAY skeletons), **Visual** (three tiers: carousel + infographic render deterministically on-brand via `tools/render-*.mjs` — never AI for anything typographic; text-free illustrative **hero images** generate via the SMC Image Generator n8n webhook, creds in `.env`), **Reels** (short-form video script), **Publish** (post SHIP renders live via Blotato — asks platforms/LinkedIn target/timing/X shape every run, shows final text, publishes only on explicit approval, then writes `published.md` and flips the INDEX row to PUBLISHED; media is per-platform — **LinkedIn and Instagram take the full carousel, Facebook and X a single 16:9 hero**, never a lone cover slide). Full mechanics in `agents/PIPELINE.md`.

### How the system is invoked

Three layers, same logic underneath:

1. **Plain English** — the user just says what they want ("write a post about X", "give me ideas"). Match the intent to the right agent(s) and run them.
2. **Skills** (`.claude/skills/`) — auto-trigger the standalone capabilities: `build-voice`, `ideate`, `hook`, `niche-research`, `visual`, `reels`. Each skill is a thin trigger that reads its canonical `agents/*.md` and executes it.
3. **Commands** (`.claude/commands/`) — explicit multi-step workflows: **`/post <topic>`** runs the full core pipeline (Writer→Scorer); **`/adapt <slug>`** re-renders an existing master; **`/publish <slug>`** posts a SHIP-gated idea live via Blotato (never publish without the user's explicit per-run confirmation of the final text); **`/schedule`** plans the next publishing cycle — assigns unpublished ideas (per preset, from `ideas/ideas-*.md` and `ideas/marketing-ideas-*.md`) to dates on the standing cadence and writes `ideas/schedule-<YYYY-MM>.md` (per `agents/SCHEDULER.md`; planning only, never publishes).

**Standing cadence — preset locked to weekday.** One post daily at 4:00 PM EDT (`20:00:00Z`); **Professional = Tue/Thu/Sat**, **Business = Wed/Fri/Sun**. Six posting days is even, so daily alternation pins each weekday permanently. **Monday is Marketing** — and carries **two** slots for a single idea: Spanish at 2:00 PM EDT (`18:00:00Z`), English at 4:00 PM. The user batches by week: "**Business for the week of Aug 16**" — week runs Sunday→Saturday, named by its Sunday, three slots per preset (→ Aug 16/19/21; Professional that week → Aug 18/20/22). Marketing yields **one** Monday per week, not three. Resolve those dates directly, no queue-tail detection.

**Before publishing anything, run `python3 tools/check-renders.py <postdir>`.** It validates every render mechanically — length bands and draft targets, the hook against each platform's fold, hashtag counts, markdown emphasis (no platform renders it; `*word*` publishes as an asterisk), stray numeric hashtags like "window #47" that linkify, American spelling, and for marketing posts the CTA form and EN/ES paragraph parity. It exits non-zero and every rule in it exists because it was violated in a real post.

`--all` sweeps both trees, but reports only posts written **after** the length bands were set (2026-09-20). Older posts were written against different numbers; flagging them made `--all` report 185 failures across 68 posts, which is how a checker stops being read. `--all --everything` includes them. A post named explicitly on the command line is never filtered — ask about one post and you get the truth about it, whatever its age.

`agents/*.md` files remain the **source of truth** — skills and commands point to them, never fork the logic. The core pipeline agents (Writer, Factcheck, Adapter, Editor, Hashtag, Scorer) are invoked *through* `/post`, not as individual skills.

## Repository Structure

```
rules/
  SHARED.md        # niche, voice, fact discipline — applies to every platform
  LINKEDIN.md      # 1600-1850 chars (fail >1900), near-zero emoji, 2-3 hashtags, Sources block
  FACEBOOK.md      # 550-700 chars (fail >760), sparing emoji, 0-2 hashtags, inline cites
  INSTAGRAM.md     # caption 600-900 over a carousel / 900-1400 Professional hero-only / 125-220 under one image; exactly 5 hashtags
  X.md             # 280-char single or thread, sparing emoji, 1-2 hashtags
  VOICE.md         # author voice profile (created by the Voice agent; optional)
  MARKETING.md     # marketing lane only: brand voice, products, CTA, the figures exception
  SPANISH.md       # any *-es.md render: usted, glossary, ES length targets, never translate
agents/            # canonical agent logic (source of truth)
  # core pipeline
  WRITER.md  FACTCHECK.md  PLATFORM_ADAPTER.md  EDITOR.md  HASHTAG.md  SCORER.md  PIPELINE.md
  # idea front-end (optional)
  RESEARCH.md  IDEATION.md  HOOK.md
  # on-demand
  VOICE.md  FORMATTER.md  VISUAL.md  REELS.md  PUBLISH.md
.claude/
  commands/        # /post (full pipeline), /adapt (re-render), /publish (go live via Blotato), /schedule (plan cycle)
  skills/          # auto-triggered: build-voice, ideate, hook, niche-research, visual, reels
ideas/             # idea trackers (ideas-<date>.md, marketing-ideas-<date>.md) + forward plans (schedule-<YYYY-MM>.md)
content/           # generated thought-leadership posts (idea-first layout)
marketing/         # generated company marketing posts (same layout, own INDEX.md)
```

## Output Layout (Non-Negotiable)

Posts are **idea-first**. One idea = one dated folder holding all its platform versions. Both trees use the identical layout; only the render set differs:

```
content/<year>/<YYYY-MM-DD>-<slug>/        marketing/<year>/<YYYY-MM-DD>-<slug>/
  master.md      # fact-checked source       master.md       # fact-checked source
  linkedin.md    # LinkedIn render           linkedin.md     # English render
  facebook.md    # Facebook render           linkedin-es.md  # Spanish render
  instagram.md   # Instagram render          published.md    # written by /publish
  x.md           # X render
  published.md   # written by /publish — per-platform live URLs / schedule / status
```

- `<YYYY-MM-DD>` = intended publish/creation date (sorts chronologically)
- `<slug>` = short kebab-case handle from the idea's landing or thesis
- Never scatter the renders across separate trees — they belong to one idea
- The Adapter writes the lane's renders as siblings of `master.md`, in the same folder
- **Each tree has its own catalog** — `content/INDEX.md` and `marketing/INDEX.md` (date, slug, title, renders, visual, status), newest-first. `/post`, `/adapt`, and `/publish` keep them current; the Visual skill updates the visual column. They're the lookup for "what's the slug for that post?" — when resolving a slug, search both.

Reference set: `content/2026/2026-06-24-ai-makes-us-judges/` — the calibration examples for **hook, structure, voice, and landing**.

**Its lengths and hashtag counts are not the bar.** It predates the current bands and fails `tools/check-renders.py` on four counts (LinkedIn 2,831 chars against a 1,900 ceiling; Instagram 15 hashtags against a hard 5; `x.md` missing its `## Single` heading). When the reference set and `rules/SHARED.md` disagree, the rules win — and when the rules and the checker disagree, the checker wins.

## Writing Rules

The one rule that never loosens: **every statistic must trace to a real, citable source.** Vendor forecasts name the firm and the year. Uncited stats get cut or reframed as judgment. Factcheck enforces this and blocks the pipeline.

**The marketing lane carries one narrow exception** (adopted 2026-09-09 from upstream doctrine): an uncited number passes when the copy frames it as the *reader's* hypothetical scenario ("a template update that reached 38 of 40 sites"), and fails when it reads as an MZS measurement ("we found drift at 38 of 40 client sites"). Credentials and proof points are excluded — they are claims. See `rules/MARKETING.md`. This exception does not exist in `content/`.

Otherwise this system is engagement-oriented, NOT repel-mode:
- Emojis allowed per platform (heavy Instagram, sparing X, ~none LinkedIn)
- CTAs and closing questions allowed
- First-person and personal-anecdote openings allowed
- Threads, carousels, and long form where the platform supports them

Every post needs a strong **hook** in line one. The default shape is **hook → POV → cited data → judgment → memorable landing**. Protect the landing (often a triad or a real question). In `marketing/`, the CTA follows the landing on its own line — it never replaces it.

**Spanish is written, never translated.** `linkedin-es.md` is composed from the master against the upstream EN→ES glossary — usted register, neutral Latin-American Spanish, product and tool names left in English. The ES targets run longer than English (draft 1,700–2,000 chars), but the ~210-char fold does *not* scale, which makes the Spanish hook the tightest constraint in the system. See `rules/SPANISH.md`.

## Origin

Adapted from the LinkedIn-LPM editorial system (a strict, repel-mode personal blog). This project kept that system's fact discipline and senior-engineer credibility, but loosened the voice for multi-platform reach and added the Platform Adapter as the core agent.
