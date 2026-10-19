# Carousel build spec — uptime-is-lagging

9 slides · 1080×1350 (4:5).

## How to generate (read first — paste this whole file)

> **How to generate:** Generate these as individual images — one separate image per slide, each portrait 1080x1350 (4:5). Do NOT combine them into a grid, collage, or contact sheet. Generate one slide at a time; wait for "next" between slides. Keep identical style, palette, and fonts across all slides. Proof every slide's text against this spec — especially numbers — before using.

## Brand

- **Base ~60%:** navy `#161a45` fills the canvas.
- **Text ~30%:** cream `#F4EFE3` — headlines and body. Not white.
- **Accent ~10%:** red `#eb2027` — one key word, a thin rule. Never a field.
- **Fonts:** Cormorant Garamond Medium (500) titles ~32pt · Lato Regular (400) body ~18pt.
- **Slide mark:** the text `@mzsnetworks` bottom-left in cream, small. There is no logo image. CTA slide may add `mzsnetworks.com`.
- Slide number bottom-right. Body slides stay navy/cream with minimal red.

## Slides

| # | Type | Title | Body |
|---|------|-------|------|
| 01 | cover | Uptime is a *lagging* indicator. | It tells you what survived. / Not what's about to break. |
| 02 | body | The easiest number to count | Four nines looks like a job well done. / Right up until the quarter it *isn't*. |
| 03 | body | Watch this pair instead | How fast the environment changes — / against how much review those changes *actually* get. |
| 04 | body | Velocity isn't the risk | Per DORA's State of DevOps research, the fastest teams are also the most *stable*. / Throughput and stability rise together. |
| 05 | body | 1 — The “standard change” list keeps growing | Because getting an *exception* is slow. |
| 06 | body | 2 — Approvals in under a minute | Which makes them approvals, / not *readings*. |
| 07 | body | 3 — A rollback nobody has run | A paragraph in the ticket. / *Never executed.* |
| 08 | body | 4 — The approver is the author | The person who understands the change / is the person *approving* it. |
| 09 | cta | Review discipline decides which one you get. | Uptime tells you what survived. / Change velocity tells you what's coming. /  / Follow *@mzsnetworks* |

*Text wrapped in `*asterisks*` renders red (italic in titles).*

## Layout system

- Body slides: title block upper-middle, thin red rule beneath, body below in Lato. Consistent left margin across all slides.
- Cover: largest title, no slide number emphasis, sets the promise.
- CTA: landing line as the title, the follow line last.

## Production

Rendered deterministically: `node tools/render-carousel.mjs content/2026/2026-08-28-uptime-is-lagging` → `carousel-01.png … 09.png`.
This spec is the portable fallback (paste into any image tool); the renderer is the production path.
