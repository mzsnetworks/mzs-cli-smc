# Carousel build spec — change-window-checklist

8 slides · 1080×1350 (4:5).

## How to generate (read first — paste this whole file)
Generate as individual images, one per slide, 1080×1350 (4:5). No grid/collage.
One slide at a time; wait for "next". Identical style across slides. Proof all text.

**Brand**
- Colors: navy `#161a45` field · cream `#F4EFE3` text · red `#eb2027` accent (one word/element per slide max; never accent markup on red CTA/cover blocks)
- Fonts: Cormorant Garamond Medium (titles) · Lato Regular (body)
- Slide mark: `@mzsnetworks` text small in cream (no logo image); CTA adds `mzsnetworks.com`

| # | Type | Title | Body |
|---|------|-------|------|
| 1 | Cover | The change-window checklist that kills the **2am rollback**. | Four lines. |
| 2 | Body | 1 — Pre-checks, captured | Snapshot configs, routes, neighbors, counters — **before** anything changes. Not "looks good." Recorded. |
| 3 | Body | 2 — Blast radius, written down | What can this break, worst case? **"Not sure" means not ready.** |
| 4 | Body | 3 — A back-out that's been run | An untested rollback is a **theory**. Rehearse it. Mark the point of no return. |
| 5 | Body | 4 — One named decision-maker | Proceed or roll back — **one owner**, criteria written at 2pm. Never a group-chat vote. |
| 6 | Body | What the checklist really does | It moves every decision **out of the window**. The window is for execution. |
| 7 | Body | Well-run changes look boring | Boring is the **achievement**. |
| 8 | CTA | Plan at 2pm. Execute at 2am. Never think at 2am. | What's the checklist item that saved your team a night? |

**Layout system:** navy full-bleed; title top-third in Cormorant; body centered-left in Lato; bold = red accent; cover and CTA carry heavier title sizes; @mzsnetworks bottom corner every slide.

Render: `node tools/render-carousel.mjs content/2026/2026-08-12-change-window-checklist`
