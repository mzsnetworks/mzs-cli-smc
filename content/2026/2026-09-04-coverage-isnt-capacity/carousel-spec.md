# Carousel build spec — coverage-isnt-capacity

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
| 01 | cover | Coverage isn't *capacity*. | Green in every corner. / The complaints keep arriving. |
| 02 | body | Users don't feel dBm | They feel *contention*. |
| 03 | body | A radio is a shared medium | One device talks at a time. / Everyone else *waits their turn*. |
| 04 | body | Forty devices, one conversation | Not forty conversations. / One — taken in turns, very quickly. |
| 05 | body | The slowest client sets the tax | A device at the edge negotiates a low rate and holds the medium *longer* for the same data. / Slow for everyone on that radio. |
| 06 | body | The map answers the wrong question | “Did signal reach here.” / The complaint is *“did I get a turn.”* |
| 07 | body | Look at these instead | Channel utilization. Retry rate. / Clients per radio at *peak*. / The data rates in use. |
| 08 | body | More power makes it worse | Bigger cells → more clients per radio → more overlap. / The heat map gets greener while the experience *degrades*. |
| 09 | cta | Capacity is the design. | Coverage is a design input. / A heat map tells you the signal arrived — not that the user got a turn to speak. /  / Follow *@mzsnetworks* |

*Text wrapped in `*asterisks*` renders red (italic in titles).*

## Layout system

- Body slides: title block upper-middle, thin red rule beneath, body below in Lato. Consistent left margin across all slides.
- Cover: largest title, sets the promise.
- CTA: landing line as the title, the follow line last.
- Never accent a colour word in red (an earlier draft set "greener" in red — it reads as a rendering bug).

## Production

Rendered deterministically: `node tools/render-carousel.mjs content/2026/2026-09-04-coverage-isnt-capacity` → `carousel-01.png … 09.png`.
This spec is the portable fallback (paste into any image tool); the renderer is the production path.
