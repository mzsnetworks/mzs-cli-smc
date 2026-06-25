---
name: visual
description: Write a build spec (exact copy + brand) for a carousel or infographic to pair with a finished post. Use when the user says "make a carousel", "design a graphic", "create a visual", "infographic", or wants art for a post. Outputs a spec to build by hand in Canva — it does not generate images.
---

# Visual

Run the **VISUAL agent**. Read `agents/VISUAL.md`, `rules/SHARED.md`, `rules/VOICE.md` (brand + identity — the source of truth), and the target post folder under `content/`, then execute:

1. Route the post to a **carousel** or an **infographic**.
2. Build a slide-by-slide (or section) brief and **show it for approval — wait for explicit "generate the spec."**
3. Write the spec file (`carousel-spec.md` or `infographic-spec.md`) into the post's idea folder: exact per-slide copy, brand colors + palette system, fonts, identity, `@handle` slide mark, layout system.
4. Hand off — the user builds it in Canva on their brand kit, applying the real fonts and the `@handle` text mark.

**This skill does not generate images.** Canva's AI generator and image models proved unreliable for exact text and real fonts, so the agent outputs a precise build spec instead. Pull all brand values from `rules/VOICE.md` (colors, palette system, fonts, identity, slide mark) — never fabricate brand marks, URLs, handles, or stats. There is no logo image; the `@mzsnetworks` text is the mark. On-demand only.
