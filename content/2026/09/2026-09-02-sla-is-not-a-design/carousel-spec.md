# Carousel build spec — sla-is-not-a-design

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
| 01 | cover | An SLA is not a *design*. | Four nines on the contract. / One fiber path in the ground. |
| 02 | body | Diverse on the invoice | Two carriers. One conduit. *One bridge.* / Adjacent in the dirt. |
| 03 | body | Nobody asked the physical question | The contract had already answered a *different one*. |
| 04 | body | An SLA transfers risk | It does *not* reduce it. |
| 05 | body | The credit doesn't run payroll | A fraction of one month's bill, eventually. / It compensates you for the outage — it was never built to *prevent* one. |
| 06 | body | 1 — Where do the paths diverge? | On a *map*. / Not a logical diagram. |
| 07 | body | 2 — Whose conduit is that? | And who else is in it? |
| 08 | body | 3 — What runs when primary is down? | Everything — or the subset somebody chose *three years ago*? |
| 09 | cta | A design tells you whether it breaks. | An SLA tells you what you're owed when it breaks. /  / Follow *@mzsnetworks* |

*Text wrapped in `*asterisks*` renders red (italic in titles).*

## Layout system

- Body slides: title block upper-middle, thin red rule beneath, body below in Lato. Consistent left margin across all slides.
- Cover: largest title, sets the promise.
- CTA: landing line as the title, the follow line last.
- Never accent a colour word in red (an earlier draft set "greener" in red — it reads as a rendering bug).

## Production

Rendered deterministically: `node tools/render-carousel.mjs content/2026/2026-09-02-sla-is-not-a-design` → `carousel-01.png … 09.png`.
This spec is the portable fallback (paste into any image tool); the renderer is the production path.
