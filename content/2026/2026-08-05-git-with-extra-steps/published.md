# Published — git-with-extra-steps

**Preset:** Business (all four on the MZS account)
**Scheduled:** 2026-08-05 4:00 PM EDT (`2026-08-05T20:00:00Z`)
**Media:** LinkedIn/Facebook/X → `hero-01.jpg` 16:9 (Zipline `smc-1784246464915-0.jpg`). Instagram → 8-slide carousel (Blotato public_media PNGs from local `carousel-01…08.png`). X = single post.

| Platform | Account | Submission ID | Status |
|----------|---------|---------------|--------|
| LinkedIn (MZS company page · pageId 94095464) | 26694 | `e1a02bb1-44ad-4d1e-b7ee-bcb356cbb34a` | scheduled |
| Facebook (MZS page · 779757178552278) | 38836 | `4e8df099-ccc8-4431-834b-9b74744695aa` | scheduled |
| Instagram (@mzsnetworks · carousel) | 55865 | `529fdafb-ad76-4ee3-ae73-c82559a79041` | scheduled |
| X (@mzsnetworks · single) | 21162 | `1980de45-2900-44ab-929b-7a4b5ecf5d3f` | scheduled |

**Notes:**
- First IG submission rejected — Blotato's 5-hashtag counter treats inline "#3" in prose as a hashtag. Reworded to "sign 3", republished. Lesson: no `#N` references in IG captions.
- LI/FB/X originally scheduled with the carousel cover slide (submissions `b1d94418…`, `2edacec5…`, `9f992308…`); deleted and re-scheduled with the 16:9 hero per the Business rule: **LI/FB/X always hero; carousel is IG-only** (now in `agents/PUBLISH.md`).

Carousel PNGs regenerable from `carousel.json` (`node tools/render-carousel.mjs content/2026/2026-08-05-git-with-extra-steps`).

Live URLs resolve after the scheduled time — poll via `blotato_get_post_status` with the IDs above.
