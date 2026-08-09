# Published — load-bearing-workaround

**Preset:** Professional (LinkedIn personal + IG @mzsnetworks)
**Scheduled:** 2026-08-08 4:00 PM EDT (`2026-08-08T20:00:00Z`)
**Media:** LinkedIn → **full 8-slide carousel** (reposted 2026-08-09). Instagram → full 8-slide carousel (Blotato public_media PNGs).

| Platform | Account | Submission ID | Status |
|----------|---------|---------------|--------|
| LinkedIn (personal — Luis Mazariegos) | 26694 | `dc534922-2d58-4b4c-a818-58288fa31bd7` | published — https://linkedin.com/feed/update/urn:li:ugcPost:7492309911188684801 |
| Instagram (@mzsnetworks · carousel) | 55865 | `267800b8-fe0c-4353-a939-d22549230b61` | published (Aug 8) |

2026-08-09: original LI post (`13eb71aa…`, cover slide only — the flaw that triggered the LinkedIn-carousel rule change) deleted by user on LinkedIn; reposted with identical text + full 8-slide carousel.

**Notes:**
- CTA slide first render dropped the word "date" — `*date*` red-accent inside the red CTA block rendered red-on-red. Fixed by removing accent markup from the CTA title. Lesson: no `*accent*` in CTA/cover titles that sit on red blocks.
- IG caption: exactly 5 hashtags; signs listed with arrows, no numbered `#N`/"1." prose.

Carousel PNGs regenerable from `carousel.json` (`node tools/render-carousel.mjs content/2026/2026-08-08-load-bearing-workaround`).

Live URLs resolve after the scheduled time — poll via `blotato_get_post_status` with the IDs above.
