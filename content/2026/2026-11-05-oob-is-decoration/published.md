# Published — 2026-11-05-oob-is-decoration

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Thu Nov 5 (2026-11-05) at 4:00 PM **EST** (`2026-11-05T21:00:00Z`) on both platforms.
**Submitted:** 2026-10-18 via Blotato MCP. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-11-05T21:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `8161650d-81db-4171-a0f6-7c940d3f3555` | SCHEDULED |
| 2026-11-05T21:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `c707f46a-dd0a-4cee-82d6-3b09108ef65f` | SCHEDULED |

**Account check.** This preset posts to the **personal** profile, so `pageId` is deliberately omitted —
passing `94095464` would send it to the MZS company page instead. The workspace holds a second LinkedIn
account (`34721`) with the same display name; `26694` is the correct one.

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn
(`smc-1792374283759-2.jpg`) and 4:5 for Instagram (`smc-1792374283766-3.jpg`), since a 16:9 hero gets cropped in the IG feed.
Both served from their Zipline URLs and verified to return JPEG bytes before submission. Zipline expires
files after 90 days (≈2027-01-16); the local `hero-*.jpg` files are the durable copies.

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1.

**Note.** Corrections from here mean editing a live Blotato schedule. `blotato_update_schedule` takes the
**numeric schedule ID**, not the submission IDs above, and this post is past the first page of
`blotato_list_schedules` — page with the cursor.
