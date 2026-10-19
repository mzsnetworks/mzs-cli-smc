# Published — 2026-12-01-why-is-it-still-there

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Tue 2026-12-01 at 4:00 PM **EST** (`2026-12-01T21:00:00Z`) on both platforms.
**Submitted:** 2026-10-18 via Blotato MCP. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Schedule ID | Status |
|------------|----------|--------|-------|---------------|-------------|--------|
| 2026-12-01T21:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `492b3e75-dad3-4e76-92a9-0f45e702aecd` | `5744038` | SCHEDULED |
| 2026-12-01T21:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `969cc2b9-4382-4573-bd05-2c78a2f9ee34` | `5744041` | SCHEDULED |

**Account check.** This preset posts to the **personal** profile, so `pageId` is deliberately omitted —
passing `94095464` would send it to the MZS company page instead. The workspace holds a second LinkedIn
account with the same display name; `26694` is the correct one. Verified after submission with
`blotato_list_schedules`: both rows carry `target: { targetType: "linkedin" }` with no `pageId`.

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn
(`smc-1792378756694-0.jpg`) and 4:5 for Instagram (`smc-1792378756697-1.jpg`), since a 16:9 hero gets cropped in
the IG feed. Both served from their Zipline URLs. Zipline expires files after 90 days (≈2027-01-16); the
local `hero-*.jpg` files are the durable copies. Both approved on the first roll.

**EST, not EDT.** 4:00 PM local is `21:00:00Z` through to Mar 14, 2027, so December carries the same
offset as November. December's own plan (`ideas/schedule-2026-12.md`) states this at the top.

**Note.** The schedule IDs above are what `blotato_update_schedule` takes — not the submission IDs. To
change only the time, omit `post` entirely; a partial `post` silently drops the fields it leaves out.
This post sits past the first page of `blotato_list_schedules`, so reaching it means paging with the cursor.
