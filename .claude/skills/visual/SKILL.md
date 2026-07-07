---
name: visual
description: Build a carousel, infographic, or AI hero image for a finished post. Carousels/infographics render deterministically on-brand (HTML/CSS via headless Chrome); text-free hero images generate via the SMC Image Generator n8n webhook (Gemini → Zipline URL). Use when the user says "make a carousel", "design a graphic", "create a visual", "infographic", "hero image", or wants art for a post.
---

# Visual

Run the **VISUAL agent**. Read `agents/VISUAL.md`, `rules/SHARED.md`, `rules/VOICE.md` (brand + identity — the source of truth), and the target post folder under `content/`, then execute:

1. Route the post: **carousel** (multi-point), **infographic** (framework/stats), or **hero image** (illustrative scene, no text in image).
2. Build the brief (slides/sections, or the hero prompt + aspect) and **show it for approval — wait for explicit "generate."**
3. Produce the asset:
   - **Carousel:** write `carousel-spec.md` + `carousel.json` → `node tools/render-carousel.mjs content/<year>/<date>-<slug>` → `carousel-01.png … NN.png`.
   - **Infographic:** write `infographic.json` → `node tools/render-infographic.mjs content/<year>/<date>-<slug>` → `infographic.png`.
   - **Hero:** brand-template prompt → POST to the SMC Image Generator webhook (creds in `.env`; call pattern in `agents/VISUAL.md`) → QA the image with the user → save `hero-NN.<ext>` + `hero.json` (with the Zipline URL) into the folder.
4. QA, iterate, re-run until on-brand.
5. Update the post's row in `content/INDEX.md` (Visual column → `carousel` / `infographic` / `hero`).

**Deterministic render for anything typographic** — AI generation only for text-free hero scenes, only through the webhook, always behind the approval gate. Pull all brand values from `rules/VOICE.md`. Never fabricate brand marks, URLs, handles, or stats. There is no logo image; the `@mzsnetworks` text is the mark. Requires Google Chrome (headless) for local renders. On-demand only.
