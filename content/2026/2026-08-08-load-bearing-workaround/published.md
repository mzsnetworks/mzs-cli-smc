# Published — load-bearing-workaround

**Preset:** Professional (LinkedIn personal + IG @mzsnetworks)
**Scheduled:** 2026-08-08 4:00 PM EDT (`2026-08-08T20:00:00Z`)
**Media:** LinkedIn → carousel cover slide (Professional precedent — Business hero rule N/A). Instagram → full 8-slide carousel (Blotato public_media PNGs).

| Platform | Account | Submission ID | Status |
|----------|---------|---------------|--------|
| LinkedIn (personal — Luis Mazariegos) | 26694 | `13eb71aa-6a0c-405e-9a6a-d4376e3c95eb` | scheduled |
| Instagram (@mzsnetworks · carousel) | 55865 | `267800b8-fe0c-4353-a939-d22549230b61` | scheduled |

**Notes:**
- CTA slide first render dropped the word "date" — `*date*` red-accent inside the red CTA block rendered red-on-red. Fixed by removing accent markup from the CTA title. Lesson: no `*accent*` in CTA/cover titles that sit on red blocks.
- IG caption: exactly 5 hashtags; signs listed with arrows, no numbered `#N`/"1." prose.

Carousel PNGs regenerable from `carousel.json` (`node tools/render-carousel.mjs content/2026/2026-08-08-load-bearing-workaround`).

Live URLs resolve after the scheduled time — poll via `blotato_get_post_status` with the IDs above.
