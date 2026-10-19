# Published — 2026-11-03-four-questions

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Tue Nov 3 (2026-11-03) at 4:00 PM **EST** (`2026-11-03T21:00:00Z`) on both platforms.
**Submitted:** 2026-10-18 via Blotato MCP. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-11-03T21:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `55ec6026-df2c-41d7-a804-d4cc130e9e8c` | SCHEDULED |
| 2026-11-03T21:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `304b5f5c-239b-47b1-96bf-912f79799eff` | SCHEDULED |

**Account check.** This preset posts to the **personal** profile, so `pageId` is deliberately omitted —
passing `94095464` would send it to the MZS company page instead. The workspace holds a second LinkedIn
account (`34721`) with the same display name; `26694` is the correct one.

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn
(`smc-1792374283748-0.jpg`) and 4:5 for Instagram (`smc-1792374283751-1.jpg`), since a 16:9 hero gets cropped in the IG feed.
Both served from their Zipline URLs and verified to return JPEG bytes before submission. Zipline expires
files after 90 days (≈2027-01-16); the local `hero-*.jpg` files are the durable copies.

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1.

**Note.** Corrections from here mean editing a live Blotato schedule. `blotato_update_schedule` takes the
**numeric schedule ID**, not the submission IDs above, and this post is past the first page of
`blotato_list_schedules` — page with the cursor.
