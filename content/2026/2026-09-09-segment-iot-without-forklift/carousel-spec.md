# Carousel build spec — 2026-09-09-segment-iot-without-forklift

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
| 01 | cover | Segment IoT without a *forklift*. | Thirty days. / The gear you already own. |
| 02 | body | Days 1–10: profile what's talking | DHCP options and MAC OUI give you the vendor. / Flow data gives you *the truth*. |
| 03 | body | Group by class, not vendor | Cameras. Badge readers. HVAC. Printers. Lab gear. / Class is what policy gets *written against*. |
| 04 | body | Days 10–20: one VLAN per class | An ACL that permits everything and logs it. / You're *recording* the truth, not enforcing it. |
| 05 | body | Pick the boring class first | The camera vendor is not who you want as your *opening argument*. |
| 06 | body | Days 20–30: the ACL writes itself | Cameras reach the NVR, NTP and DNS. / Nothing reaches the *user VLAN*. |
| 07 | body | No new platform. No agent. | Routed VLANs and access lists on hardware you *already pay maintenance on*. |
| 08 | triad | Three moves, in order | Find them. / Fence them. / Then let them out *on purpose*. |
| 09 | cta | The hard part isn't technical. | Segmentation forces a conversation about who owns the cameras. / The network can enforce a policy. It can't invent one. /  / Follow *@mzsnetworks* |

*Text wrapped in `*asterisks*` renders red (italic in titles).*

## Layout system

- Body slides: title block upper-middle, thin red rule beneath, body below in Lato. Consistent left margin across all slides.
- Cover: largest title, sets the promise.
- Triad slide: three numbered steps in circles, the last one carrying the accent.
- CTA: landing line as the title, the follow line last.
- Never accent a colour word in red (an earlier draft set "greener" in red — it reads as a rendering bug).

## Production

Rendered deterministically: `node tools/render-carousel.mjs content/2026/2026-09-09-segment-iot-without-forklift` → `carousel-01.png … 09.png`.
This spec is the portable fallback (paste into any image tool); the renderer is the production path.
