# Published — automate-toil-first

**Preset:** Business (all four on the MZS account)
**Scheduled:** 2026-08-07 4:00 PM EDT (`2026-08-07T20:00:00Z`)
**Media:** LinkedIn/Facebook/X → `hero-01.jpg` 16:9 (Zipline `smc-1785207032379-0.jpg`) per Business rule (LI/FB/X always hero). Instagram → 8-slide carousel (Blotato public_media PNGs). X = single post.

| Platform | Account | Submission ID | Status |
|----------|---------|---------------|--------|
| LinkedIn (MZS company page · pageId 94095464) | 26694 | `e492795d-1166-4b6f-9cfb-325f8f39c59a` | scheduled |
| Facebook (MZS page · 779757178552278) | 38836 | `b94935cc-4b7b-459a-ae84-a3237b64fbe7` | scheduled |
| Instagram (@mzsnetworks · carousel) | 55865 | `bdc8dad1-b8d2-4005-bee9-8898d211ca93` | scheduled |
| X (@mzsnetworks · single) | 21162 | `99f820e4-53e7-47f4-b67c-dfc8958d9d7a` | scheduled |

IG caption: exactly 5 hashtags, list uses arrows (no `#N`/numbered prose).

Carousel PNGs regenerable from `carousel.json` (`node tools/render-carousel.mjs content/2026/2026-08-07-automate-toil-first`).

Live URLs resolve after the scheduled time — poll via `blotato_get_post_status` with the IDs above.
