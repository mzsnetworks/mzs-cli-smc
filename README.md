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

**You don't run commands. You don't memorize agent names. You open Claude Code in this folder and talk to it in plain English.** Claude reads `CLAUDE.md` and the rule files automatically and knows what to do. The examples below are things you literally type into the chat.

### Step 0 — do this once: teach it your voice

Type this:

> **Build my voice profile.**

Claude asks you six questions (your background, your strong opinions, your war stories, etc.). Answer them in plain text — paste a brain-dump, it's fine. Claude writes `rules/VOICE.md`. From now on every post sounds like *you*. You never have to do this again (unless your style changes).

### Step 1 — write a post (the main thing you'll do)

You have an idea. Type it like you're telling a colleague:

> **I want a post about how most network outages are self-inflicted, not hardware failures. Run it through the full pipeline for LinkedIn, Instagram, and X.**

Claude then, on its own:
1. **Writes** the master post in your voice
2. **Fact-checks** every number (and stops to fix anything it can't source)
3. **Adapts** it into LinkedIn, Instagram, and X versions
4. **Tightens** each to the right length
5. **Adds** the right hashtags per platform
6. **Scores** each one and tells you if it's good to ship

You get a new folder like `content/2026/2026-07-01-self-inflicted-outages/` with four files: `master.md`, `linkedin.md`, `instagram.md`, `x.md`. Open them, copy, paste, publish.

> 💡 You can also paste a messy draft or rough notes instead of one sentence — "here are my bullet points, turn them into a post" works the same way.

### Step 2 — don't have an idea? Ask for some

> **Give me 30 post ideas.**

You get a table of specific angles (not vague topics) crossing your content pillars with proven post formats, plus a "Top 5 to write now." Pick one and go back to Step 1:

> **Write idea #3 from that list through the full pipeline.**

Or hunt for fresh, real stories first:

> **What's trending in network engineering this week?** → gives dated, linked stories you can post about.

### Step 3 — add a graphic, a carousel, or a video script (optional)

After a post exists, ask for art (uses your Canva):

> **Make a carousel for the self-inflicted-outages post.**

Claude builds a slide-by-slide plan, shows it to you, waits for your "go," then designs it in Canva and saves the export into the post's folder. For a video:

> **Write me a Reel script from that post.**

### That's the whole thing

| What you want | What you type |
|---------------|---------------|
| Set up your voice (once) | "Build my voice profile." |
| Write a post | "Write a post about [topic]. Run the full pipeline." |
| Turn rough notes into a post | "Here are my notes: [paste]. Make a post out of this." |
| Get ideas | "Give me 30 post ideas." |
| Find trending stories | "What's trending in [niche] this week?" |
| Punch up a weak opener | "Give me 6 hook options for [topic]." |
| Make a carousel/graphic | "Make a carousel for the [slug] post." |
| Make a video script | "Write a Reel script from the [slug] post." |
| Re-shape a rambling draft | "Rewrite this as a PAS post: [paste]." |
| Just one platform | "Write only a LinkedIn post about [topic]." |

You never have to name an agent or edit a rule file. Claude picks the right agents from what you ask.

**Prefer typing a command?** Two shortcuts do the same thing:
- **`/post <topic>`** — runs the full pipeline (the Step 1 flow above) in one shot.
- **`/adapt <slug>`** — re-renders an existing post's `master.md` into the three platforms.

And the on-demand capabilities are also installed as **skills** that fire automatically on plain-English phrasing — "build my voice", "give me ideas", "make a carousel", "write a reel", "what's trending". You don't need to learn them; they trigger themselves.

---

### Worked example (start to finish)

Here's a real run, exactly as it happened, so you can see the shape of it.

**You type:**
> Write a post about an ISSU upgrade that kept failing even though every health check was green. The real cause was leftover operational state from past install attempts. Run the full pipeline.

**Claude does:**
- Creates `content/2026/2026-06-24-operational-state/master.md` and drafts it in your voice — opening "The problem wasn't the procedure. It never is.", landing on a config/logs/state triad.
- Fact-checks it → **PASS** (no stats to source; it's an experience post).
- Writes `linkedin.md` (1,662 chars), `instagram.md` (caption + 7 carousel slides + 15 hashtags), `x.md` (a 276-char single post **and** a 7-tweet thread).
- Scores them: LinkedIn **97/100 SHIP**, Instagram **92 SHIP**, X **92 SHIP**.

**You get:** four ready-to-publish files in one folder. Total effort on your side: one sentence.

> This exact post lives in `content/2026/2026-06-24-operational-state/` — open it to see what "done" looks like.

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
- `content/INDEX.md` catalogs every post (date, slug, title, renders, visual, status), newest-first. `/post` and `/adapt` keep it current — it's how you look up a post's slug ("make a carousel for `plug-and-play-wifi-myth`").

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
