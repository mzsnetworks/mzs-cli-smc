# Carousel build spec — 2026-09-18-supportable-at-3am

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
| 01 | cover | Supportable at *3am*. | Five things. / None of them are products. |
| 02 | body | 1. Consistent naming | At 3am you type the name before you think. / Naming is *the index* into everything else. |
| 03 | body | 2. One source of truth | Two systems disagree about a VLAN. Which wins? / If it's “ask Dave,” *Dave is asleep*. |
| 04 | body | 3. Out-of-band that works | Can you reach a console while the uplink is down, without transiting *what's broken*? |
| 05 | body | 4. Backups someone restored | A green checkmark is an unverified claim. / The backup is rarely the problem. *The restore is.* |
| 06 | body | 5. One named owner | Not a team alias. / “Escalate to Network” is a *queue*, not an owner. |
| 07 | body | None of it is a product | Not one of these five appears in a *design review*. |
| 08 | body | At 3am nobody is clever | You only have what you wrote down while it was *daylight*. |
| 09 | cta | Which one would you fail tonight? | Naming. Source of truth. Out-of-band. / Restores. An owner. /  / Follow *@mzsnetworks* |

*Text wrapped in `*asterisks*` renders red (italic in titles).*

## Layout system

- Body slides: title block upper-middle, thin red rule beneath, body below in Lato. Consistent left margin across all slides.
- Cover: largest title, sets the promise.
- Triad slide: three numbered steps in circles, the last one carrying the accent.
- CTA: landing line as the title, the follow line last.
- Never accent a colour word in red (an earlier draft set "greener" in red — it reads as a rendering bug).

## Production

Rendered deterministically: `node tools/render-carousel.mjs content/2026/2026-09-18-supportable-at-3am` → `carousel-01.png … 09.png`.
This spec is the portable fallback (paste into any image tool); the renderer is the production path.
