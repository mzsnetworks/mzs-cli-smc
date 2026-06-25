---
name: visual
description: Build a carousel or infographic for a finished post — writes a spec + carousel.json, then renders on-brand PNGs locally (HTML/CSS via headless Chrome). Use when the user says "make a carousel", "design a graphic", "create a visual", "infographic", or wants art for a post. Deterministic render — no AI image generation.
---

# Visual

Run the **VISUAL agent**. Read `agents/VISUAL.md`, `rules/SHARED.md`, `rules/VOICE.md` (brand + identity — the source of truth), and the target post folder under `content/`, then execute:

1. Route the post to a **carousel** or an **infographic**.
2. Build a slide-by-slide brief and **show it for approval — wait for explicit "generate."**
3. Write `carousel-spec.md` (portable, paste-anywhere) AND `carousel.json` (machine-readable slide data — see schema in `agents/VISUAL.md`) into the post folder.
4. Render locally:
   - **Carousel:** write `carousel.json` → `node tools/render-carousel.mjs content/<year>/<date>-<slug>` → `carousel-01.png … NN.png`.
   - **Infographic:** write `infographic.json` → `node tools/render-infographic.mjs content/<year>/<date>-<slug>` → `infographic.png` (one tall canvas).
   Both render at 2× with real fonts + exact brand. QA, iterate on the JSON, re-run.
5. Update the post's row in `content/INDEX.md` (Visual column → `carousel` or `infographic`).

**Deterministic render only — no AI image generation.** Canva's AI generator and image models proved unreliable for exact text and real fonts. Pull all brand values from `rules/VOICE.md` (colors, palette system, fonts, identity, slide mark). Never fabricate brand marks, URLs, handles, or stats. There is no logo image; the `@mzsnetworks` text is the mark. Requires Google Chrome (headless). On-demand only.
