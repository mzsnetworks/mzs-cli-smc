# Carousel build spec — lab-failure-modes

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
| 01 | cover | Your lab doesn't need to match production. It needs to match its *failure modes*. | The spec everyone writes wrong. |
| 02 | body | The digital twin | Same platforms. Same topology. Faithful at scale. / A year later, it proves the *happy path* works. |
| 03 | body | The happy path was never the question | Outages don't come from the topology. / They come from the *seams*. |
| 04 | body | The seams | Failover that breaks only under asymmetric return traffic. / An upgrade that fails on *state left behind*. / A “multicast problem” that was an app design flaw. |
| 05 | body | A replica of a healthy network is healthy | That's the design goal. / It reproduces *none* of it. |
| 06 | body | Write a different spec | Can this lab reproduce / our *last three outages*? |
| 07 | body | Not port count. Not part numbers. | Break the link, watch convergence take the documented path. / Leave stale state behind, run the upgrade again. / Half-apply a change, rehearse the *rollback*. |
| 08 | body | Two switches and a VM | …that reproduce last quarter's incident teach more than a rack that mirrors the DC and has *never been broken on purpose*. |
| 09 | cta | Only one of them gets tested at 2am. | A lab that matches production proves your design. / A lab that matches its failures proves your *operations*. /  / Follow *@mzsnetworks* |

*Text wrapped in `*asterisks*` renders red (italic in titles).*

## Layout system

- Body slides: title block upper-middle, thin red rule beneath, body below in Lato. Consistent left margin across all slides.
- Cover: largest title, no slide number emphasis, sets the promise.
- CTA: landing line as the title, the follow line last.

## Production

Rendered deterministically: `node tools/render-carousel.mjs content/2026/2026-08-30-lab-failure-modes` → `carousel-01.png … 09.png`.
This spec is the portable fallback (paste into any image tool); the renderer is the production path.
