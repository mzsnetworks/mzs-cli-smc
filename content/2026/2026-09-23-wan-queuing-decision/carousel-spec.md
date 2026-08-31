# Carousel build spec — 2026-09-23-wan-queuing-decision

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
| 01 | cover | Bandwidth is a *purchase*. | Priority is a decision. |
| 02 | body | The circuit has headroom | And the complaint is still real. / Both are true at once. |
| 03 | body | Something has to wait | When the link is momentarily full, one packet goes first. / That's all queuing *is*. |
| 04 | body | If you don't decide, the device does | Its default is roughly first come, first served. |
| 05 | body | The file sync doesn't care | The call does. / They queued *identically*. |
| 06 | body | More bandwidth won't remove the queue | It changes how often it forms. / Traffic expands to fill it. |
| 07 | body | Four or five classes | Not twelve. / Nobody reasons about twelve at *2am*. |
| 08 | body | Shape to the rate you bought | Your router sees a gigabit. / The carrier polices at *200 Mbps*. |
| 09 | cta | What will you let wait? | Bandwidth is a purchase. Priority is a decision. / Only one requires somebody to say what matters least. /  / Follow *@mzsnetworks* |

*Text wrapped in `*asterisks*` renders red (italic in titles).*

## Layout system

- Body slides: title block upper-middle, thin red rule beneath, body below in Lato. Consistent left margin across all slides.
- Cover: largest title, sets the promise.
- CTA: landing line as the title, the follow line last.
- Never accent a colour word in red (an earlier draft set "greener" in red — it reads as a rendering bug).

## Production

Rendered deterministically: `node tools/render-carousel.mjs content/2026/2026-09-23-wan-queuing-decision` → `carousel-01.png … 09.png`.
This spec is the portable fallback (paste into any image tool); the renderer is the production path.
