# Carousel build spec — automate-toil-first

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
| 1 | Cover | The 5 tasks worth automating first are **never the ones people ask for**. | Automate what pages you. |
| 2 | Body | 1 — State capture | Before and after **every change**. "What changed?" becomes one diff, not one hour. |
| 3 | Body | 2 — Config backup + drift alerts | Every device, every day. Notified when running config **drifts**. Boring. Priceless. |
| 4 | Body | 3 — Health checks | The senior engineer's checklist, encoded — same rigor at **2am as 2pm**. |
| 5 | Body | 4 — The restart runbook | What you already restart out of self-defense — identical, **verified**, every time. |
| 6 | Body | 5 — Alert enrichment | State, recent changes, last occurrence — attached **before a human opens it**. |
| 7 | Body | Notice the pattern | None of these change the network. Automation earns trust by being right **before it earns write access**. |
| 8 | CTA | The demo impresses. The discipline pays. | What pages your team most — and is it on anyone's automation list? |

**Layout system:** navy full-bleed; title top-third in Cormorant; body centered-left in Lato; bold = red accent; cover and CTA carry heavier title sizes; @mzsnetworks bottom corner every slide.

Render: `node tools/render-carousel.mjs content/2026/2026-08-07-automate-toil-first`
