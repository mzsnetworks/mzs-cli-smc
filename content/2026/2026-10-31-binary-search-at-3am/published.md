# Published — binary-search-at-3am

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Sat Oct 31 (2026-10-31) at 4:00 PM EDT (`2026-10-31T20:00:00Z`) on both platforms.
**Submitted:** 2026-09-20 via Blotato MCP, as part of the Oct 27–31 Professional week. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-10-31T20:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `e72c71a0-c4ab-435c-96fc-633447242f8b` | SCHEDULED |
| 2026-10-31T20:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `84f07cf1-b618-4b80-bb43-5c329647874c` | SCHEDULED |

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn, 4:5 for Instagram, since a 16:9 hero gets cropped in the IG feed. Both served from their Zipline URLs (recorded in `hero.json`) and verified to return JPEG bytes immediately before submission. Zipline expires files after 90 days (≈2026-12-19); the local `hero-01.jpg` and `hero-02-ig.jpg` are the durable copies, and Blotato copies media into its own storage at submission time.

**Account check.** `blotato_list_accounts` was called before the batch. This preset posts to the **personal** profile, so `pageId` is deliberately omitted — passing `94095464` would send it to the MZS company page instead. The workspace also holds a second LinkedIn account (`34721`) with the same display name; `26694` is the correct one.

**Note.** Corrections from here mean editing a live Blotato schedule, not a file. `blotato_update_schedule` takes the **numeric schedule ID**, not the submission IDs above — page `blotato_list_schedules` to find it.
