# Published — 2026-11-06-done-meant-applied

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Fri Nov 6 (2026-11-06) at 4:00 PM **EST** (`2026-11-06T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `dd1c34dc-5567-4114-91ba-2e111b300e43` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `b38b2c25-5611-42e1-8ac4-be35bc8039c2` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `e52f146b-8c40-416f-893a-b68aa8268b2c` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `9d3c782a-0444-4c62-8e35-acd71c142fb2` | SCHEDULED |

**First batch on EST.** US daylight time ends Sun Nov 1, so 4:00 PM local is `21:00:00Z` here, not the
`20:00:00Z` every October post used. Verified after submission by converting each returned
`scheduledAt` back to America/New_York: all four read 4:00 PM EST.

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings. Every
render sits inside its draft target rather than just under the cap.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload was fetched back and compared
byte-for-byte against the local PNG before submission. Facebook and X carry the hero served straight from
its Zipline URL (`smc-1792368168110-1.jpg`), which returned JPEG bytes on check. Zipline expires files after 90 days
(≈2027-01-16); the local `hero-*.jpg` is the durable copy, and Blotato copies media into its own storage
at submission time, so the expiry does not affect these scheduled posts.

**Carousel slide 10 carries the fixed CTA render.** The renderer colored accented words red on a red band
until 2026-10-18, which made the emphasized word invisible; these were rendered after the fix.

**`pageId: 94095464`** passed explicitly on the LinkedIn call — omitting it posts to the personal profile.

**Note.** Any correction from here means editing a live Blotato schedule rather than a file.
`blotato_update_schedule` takes the **numeric schedule ID**, not the submission IDs above — find it by
paging `blotato_list_schedules`. To change only the time, omit `post` entirely; passing a partial `post`
silently drops whatever it leaves out.
