---
name: visual
description: Design a carousel or infographic for a finished post using Canva (Gemini fallback for the hand-drawn whiteboard look). Use when the user says "make a carousel", "design a graphic", "create a visual", "infographic", "image for my post", or wants art to pair with an existing post.
---

# Visual

Run the **VISUAL agent**. Read `agents/VISUAL.md`, `rules/SHARED.md`, `rules/VOICE.md` (if present), and the target post folder under `content/`, then execute:

1. Route the post to a carousel, a clean infographic, or the hand-drawn variant.
2. Build a slide-by-slide (or section) brief and **show it for approval — wait for explicit "generate."**
3. Default engine: **Canva via the Canva MCP** — create the design from the closest brand template, apply per-slide copy, export the PNG/PDF into the post's idea folder. Keep style identical across slides.
4. Only use the Gemini whiteboard image prompt if the user wants the hand-drawn marker look.

After exporting, update the post's row in `content/INDEX.md` — set the **Visual** column to what you produced (carousel / infographic / reel).

On-demand only — never a pipeline gate. Strip creator-vanity footers unless the user wants a CTA slide. No fabricated stats on a slide.
