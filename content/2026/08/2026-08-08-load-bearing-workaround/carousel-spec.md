# Carousel build spec — load-bearing-workaround

8 slides · 1080×1350 (4:5).

## How to generate (read first — paste this whole file)
Generate as individual images, one per slide, 1080×1350 (4:5). No grid/collage.
One slide at a time; wait for "next". Identical style across slides. Proof all text.

**Brand**
- Colors: navy `#161a45` field · cream `#F4EFE3` text · red `#eb2027` accent (one word/element per slide max)
- Fonts: Cormorant Garamond Medium (titles) · Lato Regular (body)
- Slide mark: `@mzsnetworks` text small in cream (no logo image); CTA adds `mzsnetworks.com`

| # | Type | Title | Body |
|---|------|-------|------|
| 1 | Cover | Your "temporary" workaround is now **load-bearing**. | 6 signs. |
| 2 | Body | 1 — It has a nickname | The moment the team **names** it, it's a system. |
| 3 | Body | 2 — New hires get taught it | Not documented — but it's in **onboarding**. |
| 4 | Body | 3 — Its alert is suppressed | Permanently. Monitoring learned to **look away**. |
| 5 | Body | 4 — Downstream depends on it | "Fixing" it breaks a thing **you can't explain**. |
| 6 | Body | 5 — Nobody remembers why | The original problem is gone. Only the **fear of removal** remains. |
| 7 | Body | 6 — It survived a redesign | The architecture changed. The workaround got **migrated with care**. |
| 8 | CTA | Promote it — or give removal a **date**. | Temporary is intent. Load-bearing is dependency. What's the oldest "temporary" fix in your production path? |

**Layout system:** navy full-bleed; title top-third in Cormorant; body centered-left in Lato; bold = red accent; cover and CTA carry heavier title sizes; @mzsnetworks bottom corner every slide.

Render: `node tools/render-carousel.mjs content/2026/2026-08-08-load-bearing-workaround`
