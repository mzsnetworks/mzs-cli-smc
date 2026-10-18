# Published — 2026-10-23-definition-of-normal

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Oct 23 (2026-10-23) at 4:00 PM EDT (`20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `45c6619c-e013-47e7-b407-18f6268dbbff` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `fb75c22c-c63c-4e40-8d6f-5f6897ff06a3` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `de45618c-2b41-49ad-b017-422c78bd4dff` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `d020f78a-481e-44d4-8419-2616f7b6b7e9` | SCHEDULED |

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings. First batch written with the checker in the loop; it caught Facebook over the cap on two of three drafts before commit.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload returned HTTP 200 and each public URL was then fetched and confirmed to serve PNG bytes. URLs in `carousel-urls.json`. Facebook and X carry the hero from `hero.json` (`smc-1789943888872-0.jpg`).

**`pageId: 94095464`** passed explicitly on the LinkedIn call.

**Slide 10 corrected 2026-10-18, before this post fired.** The carousel renderer colored an
accented word red, and the CTA title sits on a red band, so the emphasized word rendered
invisible — this post's final slide read with "changed" missing from the sentence. Fixed in
`tools/render-carousel.mjs` (the CTA title now passes navy to `rich()`), slide 10 re-rendered and
re-uploaded, and both carousel schedules updated via `blotato_update_schedule` (LinkedIn `4646378`,
Instagram `4646381`). The other nine slides, the caption, the scheduled time and the LinkedIn
`pageId` were all carried forward unchanged and verified afterwards. Blotato re-hosts and
downscales uploaded media, so the live URL differs from the one uploaded; the served image was
fetched back and confirmed to be the corrected art.
