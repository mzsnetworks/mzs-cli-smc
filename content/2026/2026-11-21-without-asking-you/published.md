# Published — 2026-11-21-without-asking-you

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Sat 2026-11-21 at 4:00 PM **EST** (`2026-11-21T21:00:00Z`) on both platforms.
**Submitted:** 2026-10-18 via Blotato MCP. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Schedule ID | Status |
|------------|----------|--------|-------|---------------|-------------|--------|
| 2026-11-21T21:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `0e0126dd-1f52-4f43-a932-749a9cba4939` | `5742913` | SCHEDULED |
| 2026-11-21T21:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `53798df8-dddb-4b29-b509-f3e003da54c4` | `5742914` | SCHEDULED |

**Account check.** This preset posts to the **personal** profile, so `pageId` is deliberately omitted —
passing `94095464` would send it to the MZS company page instead. The workspace holds a second LinkedIn
account with the same display name; `26694` is the correct one. Verified after submission with
`blotato_list_schedules`: both rows carry `target: { targetType: "linkedin" }` with no `pageId`.

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn
(`smc-1792376054410-1.jpg`) and 4:5 for Instagram (`smc-1792375986199-5.jpg`), since a 16:9 hero gets cropped in
the IG feed. Both served from their Zipline URLs. Zipline expires files after 90 days (≈2027-01-16); the
local `hero-*.jpg` files are the durable copies.

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1, 2026, and stays that way until Mar 14, 2027.

**Note.** The schedule IDs above are what `blotato_update_schedule` takes — not the submission IDs. To
change only the time, omit `post` entirely; a partial `post` silently drops the fields it leaves out.
This post sits past the first page of `blotato_list_schedules`, so reaching it means paging with the cursor.
