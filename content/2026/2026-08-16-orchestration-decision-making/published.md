# Published — orchestration-decision-making

**Preset:** Business (all four on the MZS account)
**Scheduled:** 2026-08-16 4:00 PM EDT (`2026-08-16T20:00:00Z`)
**Media:** LinkedIn + Instagram → **8-slide carousel** (Blotato public_media PNGs). Facebook + X → `hero-01.jpg` 16:9 (Zipline `smc-1786306796625-0.jpg`). X = single post.

| Platform | Account | Submission ID | Status |
|----------|---------|---------------|--------|
| LinkedIn (MZS company page · pageId 94095464) | 26694 | `91d976cf-e1d9-4529-8525-d64bb77830f1` | scheduled |
| Facebook (MZS page · 779757178552278) | 38836 | `ff25174c-4637-44a3-aa2e-3710aea07da6` | scheduled |
| Instagram (@mzsnetworks · carousel) | 55865 | `8441d10e-68e2-4597-a869-59f27038dd8c` | scheduled |
| X (@mzsnetworks · single) | 21162 | `960c8637-4414-46bf-b34a-bb2430cb4c5f` | scheduled |

**Scores:** LI 90 · FB 88 · IG 88 · X 88. Factcheck PASS (no statistics in the post).

**Notes:**
- First post published under the revised LinkedIn rule — LI carries the full 8-slide carousel, not a cover slide or hero.
- IG caption: exactly 5 hashtags, list rendered as arrows (no `#N` numbering, which Blotato counts as hashtags).
- CTA slide title carries no `*accent*` markup (red-on-red lesson from `load-bearing-workaround`).

Carousel PNGs regenerable from `carousel.json` (`node tools/render-carousel.mjs content/2026/2026-08-16-orchestration-decision-making`).

Live URLs resolve after the scheduled time — poll via `blotato_get_post_status` with the IDs above.
