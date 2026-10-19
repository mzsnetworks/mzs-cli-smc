# Published — four-incidents-taught-me

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Sat Oct 17 (2026-10-17) at 4:00 PM EDT (`2026-10-17T20:00:00Z`) on both platforms.
**Submitted:** 2026-09-20 via Blotato MCP, as part of the Oct 6–24 Professional batch. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-10-17T20:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `1d137f03-b7bf-4a36-9198-356d2889dcdb` | SCHEDULED |
| 2026-10-17T20:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `5dbb1d2d-42ac-43cd-8dab-9321c5c367d2` | SCHEDULED |

**Media.** Two separately composed heroes, not one image cropped twice: a 16:9 for LinkedIn and a 4:5 for Instagram, since a 16:9 hero gets cropped in the IG feed. Both served straight from their Zipline URLs (recorded in `hero.json`) and verified to return JPEG bytes before submission. Zipline expires files after 90 days (≈2026-12-19); the local `hero-01.jpg` and `hero-02-ig.jpg` are the durable copies, and Blotato copies media into its own storage at submission time, so the expiry does not affect these scheduled posts.

**Account check.** `blotato_list_accounts` was called first. This preset posts to the **personal** profile, so `pageId` is deliberately omitted — passing `94095464` would send it to the MZS company page instead. Note the workspace holds a second LinkedIn account (`34721`) with the same display name; `26694` is the correct one.

**Note.** Any correction from here means editing a live Blotato schedule rather than a file. `blotato_update_schedule` takes the **numeric schedule ID**, not the submission IDs above — find it by paging `blotato_list_schedules`.
