<div align="center">

# 📡 Social Media Content System

### `claude-cli-smc` · by [MZS Networks](https://mzsnetworks.com)

**One idea → four platform-native posts → live.**
_An editorial pipeline for technical social content, run entirely through Claude Code._

![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat&logo=linkedin&logoColor=white)
![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=flat&logo=facebook&logoColor=white)
![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat&logo=instagram&logoColor=white)
![X](https://img.shields.io/badge/X-000000?style=flat&logo=x&logoColor=white)

![License](https://img.shields.io/badge/license-MIT%20%2B%20brand%20notice-eb2027?style=flat)
![Powered by Claude Code](https://img.shields.io/badge/powered%20by-Claude%20Code-D97757?style=flat)
![Publish via Blotato](https://img.shields.io/badge/publish-Blotato-161a45?style=flat)
![Fact discipline](https://img.shields.io/badge/every%20stat-cited%20or%20cut-F4EFE3?style=flat&labelColor=161a45)

</div>

---

A multi-platform editorial system for technical social content. **Write one idea once, render it natively for LinkedIn, Facebook, Instagram, and X** — each with its own voice, length, emoji policy, and hashtag rules. Same message, platform-correct packaging. When it's ready, **`/publish` posts it live** through the connected Blotato accounts.

The "code" here is markdown: agents and rule files Claude Code follows. There is nothing to install — you run the agents by pointing Claude at the right rule files and content.

- **Niche:** network engineering, infrastructure, automation, AIOps, operations.
- **Audience:** practitioners and technical leaders — but engagement-oriented (reach matters), not a repel-mode personal blog.
- **The one rule that never loosens:** every statistic must trace to a real, citable source. Factcheck enforces it and blocks the pipeline.

---

## The Pipeline

One idea flows through a pipeline and comes out as four platform-native posts.

```
[ Research --> Ideation --> Hook ] --> Writer --> Factcheck --> Platform Adapter --> Editor (x4) --> Hashtag (x4) --> Scorer (x4) --> [ Publish ]
       optional idea front-end            ^            |
                                          |  (on FAIL) |
                                          +-----<------+

On-demand (not gates):  Voice (setup)   Formatter   Visual (render carousel)   Reels   Publish (go live)
```

The **front-end** (Research → Ideation → Hook) runs only when you don't already have an idea. The **core** (Writer → Scorer) takes one idea to four publish-ready posts. **On-demand** agents are run when a post calls for them — including **Publish**, which posts SHIP-gated renders live via Blotato behind an explicit confirmation.

---

## The Agents

| Agent | Stage | Edits files? | Job |
|-------|-------|--------------|-----|
| **Research** | front-end | no | Find dated, cited niche stories via WebSearch (no scraping) |
| **Ideation** | front-end | no | Cross content pillars × formats into a 30+ idea matrix |
| **Hook** | front-end | no | Generate 6 credible (non-clickbait) hook options for an idea |
| **Writer** | core | yes | Draft the master post (LinkedIn-length) in the author's voice |
| **Factcheck** | core | no | Verify every stat against its source — PASS/FAIL (blocking) |
| **Platform Adapter** | core | yes | Render the master into LinkedIn / Facebook / Instagram / X |
| **Editor** | core | yes | Tighten each render to its platform length target |
| **Hashtag** | core | yes (append) | Apply per-platform hashtag policy |
| **Scorer** | core | no | Score each render 0–100 and gate publish (SHIP/REVISE/REWORK) |
| **Voice** | on-demand | yes (`rules/VOICE.md`) | Build the author voice profile (run once at setup) |
| **Formatter** | on-demand | yes | Impose a named framework (PAS/AIDA/BAB/STAR/SLAY) on a draft |
| **Visual** | on-demand | yes (spec + images) | Carousel/infographic rendered on-brand locally (HTML→PNG), or a text-free AI hero image via the n8n image webhook |
| **Reels** | on-demand | yes (script) | Write a 30–45s short-form video script from an idea |
| **Publish** | on-demand | yes (`published.md`) | Post SHIP renders live via Blotato — explicit confirmation gate, never automatic |

Each agent file in `agents/` ends with a **Usage** block — the exact prompt to run it. The how-to below stitches them into workflows.

---

## Installation & Setup

For a team standing this up fresh (e.g. a sister/parent company adopting the system). Most of it is markdown — the only real dependencies are Claude Code plus two connected services for visuals and publishing.

### 1. Prerequisites

| Need | For | Notes |
|------|-----|-------|
| **Claude Code** | everything | The agents run *inside* Claude Code. Open this repo folder in it. |
| **Git** | clone + version the content | |
| **Node.js 18+** | carousel/infographic rendering | Only if you produce those visuals. Runs `tools/render-*.mjs`. |
| **Google Chrome** | the renderers (headless) | The deterministic HTML→PNG step drives headless Chrome. |
| **Blotato account** (MCP) | `/publish` | Connect LinkedIn / Facebook / Instagram / X inside Blotato, then connect Blotato as an MCP server in Claude Code. Publishing is optional — the pipeline produces the copy without it. |
| **n8n + image webhook** (MCP/HTTP) | AI **hero** images only | Optional. Carousels/infographics need *no* AI. See step 4. |

There is nothing to `npm install` for the core system — the "code" is the markdown in `agents/`, `rules/`, and `.claude/`. Node is only for the visual renderers.

### 2. Clone

```bash
git clone git@github.com:mzsnetworks/mzs-cli-smc.git
cd mzs-cli-smc
```

Open the folder in Claude Code. It reads `CLAUDE.md` automatically and knows the whole system.

### 3. Make it *your* brand (the rebrand step)

This repo carries MZS Networks' identity. A new company replaces it in **one file plus two configs**:

- **`rules/VOICE.md`** — the single source of truth for voice *and* brand. Edit the **Brand** section: company name, URL, `@handle`, the four hex colors, the palette rule, and the two fonts. The Visual agent reads only this. Then run the **Voice agent** (`build my voice`) to rewrite the author profile — pillars, defended opinions, war stories — for the new team.
- **`content/`** — delete the example posts (or keep `content/2026/2026-06-24-ai-makes-us-judges/` as a calibration reference) and clear `content/INDEX.md` down to its header.
- **`LICENSE`** — update the copyright holder and the reserved-brand NOTICE.

Graphics are **not** stored in git (see `.gitignore`); each team generates its own on-brand assets.

### 4. Secrets — `.env` (never commit)

Only needed for the AI hero-image tier. Copy the template and fill in your own webhook:

```bash
cp .env.example .env    # then edit .env
```

```
SMC_IMAGE_GEN_URL=https://<your-n8n-host>/webhook/<path>
SMC_IMAGE_GEN_HEADER=<auth-header-name>
SMC_IMAGE_GEN_TOKEN=<secret-token>
```

`.env` is gitignored. Never paste the token into chat or commit it. Blotato auth is handled by the Blotato MCP connection, not this file.

### 5. Connect the MCP servers (in Claude Code)

- **Blotato** — for `/publish`. After connecting, the Publish agent calls `blotato_list_accounts` to discover your account IDs (they differ per workspace — the presets in `agents/PUBLISH.md` are MZS-specific; update them).
- **n8n** *(optional)* — only if you want AI hero images. Import an image-generation workflow that takes `{prompt, aspect}` and returns a public image URL, and point `.env` at its webhook.

### 6. Verify

In Claude Code, type: **`give me 5 post ideas`**. If it returns a pillar × format matrix drawn from your new `rules/VOICE.md`, the system is live. Then `write a post about <topic>` runs the full pipeline; `/publish <slug>` takes a SHIP-gated post live once Blotato is connected.

> **No-visual / no-publish mode:** skip steps 4–5 entirely. You still get four fact-checked, platform-native drafts per idea — you just copy them out and post by hand.

---

## How to Use

**You don't run commands. You don't memorize agent names. You open Claude Code in this folder and talk to it in plain English.** Claude reads `CLAUDE.md` and the rule files automatically and knows what to do. The examples below are things you literally type into the chat.

### Step 0 — do this once: teach it your voice

Type this:

> **Build my voice profile.**

Claude asks you six questions (your background, your strong opinions, your war stories, etc.). Answer them in plain text — paste a brain-dump, it's fine. Claude writes `rules/VOICE.md`. From now on every post sounds like *you*. You never have to do this again (unless your style changes).

### Step 1 — write a post (the main thing you'll do)

You have an idea. Type it like you're telling a colleague:

> **I want a post about how most network outages are self-inflicted, not hardware failures. Run it through the full pipeline.**

Claude then, on its own:
1. **Writes** the master post in your voice
2. **Fact-checks** every number (and stops to fix anything it can't source)
3. **Adapts** it into LinkedIn, Facebook, Instagram, and X versions
4. **Tightens** each to the right length
5. **Adds** the right hashtags per platform
6. **Scores** each one and tells you if it's good to ship

You get a new folder like `content/2026/2026-07-01-self-inflicted-outages/` with five files: `master.md`, `linkedin.md`, `facebook.md`, `instagram.md`, `x.md`. Then either copy/paste them yourself — or type **`/publish self-inflicted-outages`** and Claude posts them live through your connected Blotato accounts (it shows you the final text and waits for your explicit "publish" first; nothing ever goes out on its own).

> 💡 You can also paste a messy draft or rough notes instead of one sentence — "here are my bullet points, turn them into a post" works the same way.

### Step 2 — don't have an idea? Ask for some

> **Give me 30 post ideas.**

You get a table of specific angles (not vague topics) crossing your content pillars with proven post formats, plus a "Top 5 to write now." Pick one and go back to Step 1:

> **Write idea #3 from that list through the full pipeline.**

Or hunt for fresh, real stories first:

> **What's trending in network engineering this week?** → gives dated, linked stories you can post about.

### Step 3 — add a carousel spec or a video script (optional)

After a post exists, ask for a carousel:

> **Make a carousel for the self-inflicted-outages post.**

Claude builds a slide-by-slide plan, shows it to you, waits for your "go," then writes `carousel-spec.md` + `carousel.json` and **renders the slides locally** to `carousel-01.png … 08.png` — on-brand (your navy/cream/red, real Cormorant/Lato), exact text, all at once. Deterministic HTML→PNG, no AI image tool. (The `carousel-spec.md` is also portable — paste it into ChatGPT/Canva if you'd rather build there.)

Want atmosphere instead of data? Ask for a **hero image**:

> **Make a hero image for the operational-state post.**

Claude writes a brand-locked prompt (navy/cream/red, no text in the image), shows it for approval, then generates it through the n8n **SMC Image Generator** webhook (Gemini → your Zipline host) and saves it into the post folder with its public URL — ready for `/publish`. AI is used *only* for these text-free scenes; anything with words or numbers stays on the deterministic renderer. For a video:

> **Write me a Reel script from that post.**

### Step 4 — publish it (goes live, so it always asks first)

When every render says SHIP:

> **/publish self-inflicted-outages**   *(or just: "publish the self-inflicted-outages post")*

Claude walks through a fixed script — nothing goes out without you:

1. **Checks the gate.** Status must be SHIP. Missing a render (older posts have no `facebook.md`)? It backfills that render first, scores it, then continues.
2. **Asks you four things**, once per run:
   - *Which platforms?* (default: all four)
   - *LinkedIn: personal profile or the MZS Networks company page?*
   - *When?* now / Blotato's next free slot / a specific time ("tomorrow 9am" is fine — it converts)
   - *X: the single post or the thread?*
3. **Sorts out media.** Instagram can't post text-only — if the folder has a carousel or infographic it uses that; if not, it offers to make one (or a hero image) first. LinkedIn/Facebook/X get the visual attached when one exists.
4. **Shows you the exact final text per platform** and stops. You type **"publish"** — that word is the trigger. Anything else, nothing posts.
5. **Posts via Blotato**, reports each live URL (or failure, honestly), writes a `published.md` receipt into the post folder, and flips the post to **PUBLISHED** in `content/INDEX.md`.

> 💡 Forgot what's ready to go? Ask **"what posts are ready to publish?"** — Claude reads `content/INDEX.md` and lists everything at SHIP.

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
| Make an AI hero image | "Make a hero image for the [slug] post." |
| Make a video script | "Write a Reel script from the [slug] post." |
| Re-shape a rambling draft | "Rewrite this as a PAS post: [paste]." |
| Just one platform | "Write only a LinkedIn post about [topic]." |
| Post it live | "/publish [slug]" — asks where/when, shows final text, waits for your OK |
| Schedule instead of post now | "/publish [slug]" then answer "tomorrow 9am" (or "next free slot") when it asks |
| Add Facebook to an older post | "/publish [slug]" backfills it — or "/adapt [slug]" re-renders all four |
| See what you have | "What posts do I have?" / "What's ready to publish?" (reads `content/INDEX.md`) |
| Re-render after editing the master | "/adapt [slug]" |

You never have to name an agent or edit a rule file. Claude picks the right agents from what you ask.

**Prefer typing a command?** Three shortcuts:
- **`/post <topic>`** — runs the full pipeline (the Step 1 flow above) in one shot.
- **`/adapt <slug>`** — re-renders an existing post's `master.md` into the four platforms.
- **`/publish <slug>`** — posts a SHIP-gated idea live via Blotato (LinkedIn, Facebook, Instagram, X). Asks per run: which platforms, personal vs company page on LinkedIn, now vs scheduled, single vs thread on X. Shows the exact final text and publishes only on your explicit "publish."

And the on-demand capabilities are also installed as **skills** that fire automatically on plain-English phrasing — "build my voice", "give me ideas", "make a carousel", "write a reel", "what's trending". You don't need to learn them; they trigger themselves.

---

### Worked example 1 — writing a post (start to finish)

Here's a real run, exactly as it happened, so you can see the shape of it.

**You type:**
> Write a post about an ISSU upgrade that kept failing even though every health check was green. The real cause was leftover operational state from past install attempts. Run the full pipeline.

**Claude does:**
- Creates `content/2026/2026-06-24-operational-state/master.md` and drafts it in your voice — opening "The problem wasn't the procedure. It never is.", landing on a config/logs/state triad.
- Fact-checks it → **PASS** (no stats to source; it's an experience post).
- Writes `linkedin.md` (1,662 chars), `instagram.md` (caption + 7 carousel slides + 15 hashtags), `x.md` (a 276-char single post **and** a 7-tweet thread).
- Scores them: LinkedIn **97/100 SHIP**, Instagram **92 SHIP**, X **92 SHIP**.

**You get:** ready-to-publish files in one folder. Total effort on your side: one sentence.

> This exact post lives in `content/2026/2026-06-24-operational-state/` — open it to see what "done" looks like. (It predates the Facebook platform — a `/publish` or `/adapt` run adds `facebook.md` automatically.)

### Worked example 2 — publishing (the shape of a run)

**You type:**
> /publish plug-and-play-wifi-myth

**Claude:**
- Reads `content/INDEX.md` → finds the folder, status SHIP, infographic present. Notices `facebook.md` is missing → renders it from the master, scores it (needs ≥85), shows it to you.
- Asks: *platforms?* → you say "all four". *LinkedIn personal or company page?* → "personal". *When?* → "tomorrow 9am". *X: single or thread?* → "single".
- Attaches `infographic.png` to LinkedIn/Facebook/X and uses it for Instagram (IG never posts text-only).
- Shows the final text of all four posts, exactly as they'll appear. Waits.

**You type:**
> publish

**Claude:** schedules all four for 9:00 tomorrow via Blotato, writes `published.md` into the folder (submission IDs + scheduled time), flips the INDEX row to **PUBLISHED**, and reports back. If any platform fails, it says so plainly with the error — no silent retries.

### Worked example 3 — a hero image

**You type:**
> Make a hero image for the operational-state post.

**Claude:**
- Reads the post, drafts a brand-locked prompt — the scene (an engineer facing a rack that "passed every check"), navy `#161a45` dominant, cream highlights, thin red accents, *no text in the image* — and the aspect (16:9 for LinkedIn). Shows it to you and stops.
- On your "generate": calls the n8n SMC Image Generator webhook (Gemini → your Zipline host), pulls the image back, and shows it.
- You approve → it saves `hero-01.jpg` + `hero.json` (with the public URL) into the post folder and sets the INDEX Visual column to `hero`. That URL rides straight into `/publish`.

---

### If something doesn't work

| Symptom | Cause / fix |
|---------|-------------|
| Carousel/infographic render fails | Google Chrome must be installed (the renderer runs it headless). Fonts need network (Google Fonts). |
| Hero image call fails with 401/403 | `.env` missing or wrong — needs `SMC_IMAGE_GEN_URL`, `SMC_IMAGE_GEN_HEADER`, `SMC_IMAGE_GEN_TOKEN` (never committed; see `.gitignore`). |
| Hero image fails with 429 "limit: 0" | The Google AI project behind the n8n Gemini credential lost billing/quota — image models aren't on the free tier. Fix billing in Google AI Studio. |
| `/publish` can't find accounts | Blotato MCP disconnected — reconnect via `/mcp`. |
| Instagram refuses to post | It needs media. Make a carousel, infographic, or hero first (Claude offers this automatically). |
| A hero URL 404s at publish time | Zipline files expire after 90 days. The local `hero-*.jpg` in the post folder is the durable copy — Claude re-uploads it via Blotato automatically. |

---

## Rules & Voice

Everything an agent does is governed by the files in `rules/`:

- **`SHARED.md`** — niche, audience, voice baseline, **fact discipline**, the spine (hook → POV → data → judgment → landing), and the **per-platform Length Targets** table.
- **`LINKEDIN.md` / `FACEBOOK.md` / `INSTAGRAM.md` / `X.md`** — formatting that layers on top: length sweet spot, the "fold" the hook must clear, emoji policy, hashtag count.
- **`VOICE.md`** — *your* voice (pillars, defended opinions, signature phrasings, word list, war stories). Mandatory for every writing agent when it exists.

**Length Targets** (recommended, enforced by Editor + Scorer):

| Platform | Sweet spot | Hard cap | Fold (hook must land before) |
|----------|-----------|----------|------------------------------|
| LinkedIn | ~1,300–2,000 chars | ~3,000 | ~210 chars (~3 lines) |
| Facebook | ~400–800 chars | none (63k) | ~477 chars desktop (~400 mobile) |
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
  facebook.md    # publish-ready Facebook render
  instagram.md   # publish-ready Instagram render
  x.md           # publish-ready X render
  (carousel.png / infographic.png / reel-*.md / published.md — added on-demand)
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
  SHARED.md  LINKEDIN.md  FACEBOOK.md  INSTAGRAM.md  X.md  VOICE.md
agents/
  WRITER.md  FACTCHECK.md  PLATFORM_ADAPTER.md  EDITOR.md  HASHTAG.md  SCORER.md   # core
  RESEARCH.md  IDEATION.md  HOOK.md                                                # front-end
  VOICE.md  FORMATTER.md  VISUAL.md  REELS.md  PUBLISH.md                          # on-demand
  PIPELINE.md                                                                      # run mechanics
content/
  <year>/<YYYY-MM-DD>-<slug>/master.md linkedin.md facebook.md instagram.md x.md
```

---

## Origin

Adapted from the LinkedIn-LPM editorial system (a strict, repel-mode personal blog). This project kept that system's **fact discipline** and senior-engineer credibility, loosened the voice for multi-platform reach, and added the Platform Adapter as the core agent. The front-end, scoring, voice, and visual agents were adapted from the `charlie947/social-media-skills` repo — retuned to this niche, stripped of creator-vanity and clickbait, and de-coupled from external scraping tools.

**What carries over:** the niche, senior-practitioner credibility, and fact discipline (every stat cited).
**What's loosened:** emojis (per platform), CTAs and closing questions, first-person voice, threads/carousels/long-form where the platform supports them.
