# Carousel build spec — 2026-09-30-8021x-fails-at-the-printer

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
| 01 | cover | 802.1X fails at the *printer*. | Not the laptop. |
| 02 | body | Laptops are 90% of the devices | And about 10% of the work. / Supplicant, domain, certificate, done. |
| 03 | body | Then you meet the rest | Printers. HVAC. Cameras. / The lab instrument whose vendor says *static IP*. |
| 04 | body | Exceptions aren't cleanup | They're the majority of the work — and all of the *political risk*. |
| 05 | body | Decide the fallback first | Restrictive MAB is a decision. / An open VLAN is an *accident*. |
| 06 | body | One owner per class | “Printers” has an owner. / “This printer” has a *ticket*. |
| 07 | body | Expire every exception | Or *temporary* MAB quietly becomes the permanent architecture. |
| 08 | body | Where projects actually die | Nobody willing to say: then it goes in the *restricted segment*. |
| 09 | cta | The laptops are the demo. | The exceptions are the project. / Design the exception process before the policy. /  / Follow *@mzsnetworks* |

*Text wrapped in `*asterisks*` renders red (italic in titles).*

## Layout system

- Body slides: title block upper-middle, thin red rule beneath, body below in Lato. Consistent left margin across all slides.
- Cover: largest title, sets the promise.
- CTA: landing line as the title, the follow line last.
- Never accent a colour word in red (an earlier draft set "greener" in red — it reads as a rendering bug).

## Production

Rendered deterministically: `node tools/render-carousel.mjs content/2026/2026-09-30-8021x-fails-at-the-printer` → `carousel-01.png … 09.png`.
This spec is the portable fallback (paste into any image tool); the renderer is the production path.
