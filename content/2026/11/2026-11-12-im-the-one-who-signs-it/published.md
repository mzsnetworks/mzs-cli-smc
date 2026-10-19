# Published — 2026-11-12-im-the-one-who-signs-it

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Thu 2026-11-12 at 4:00 PM **EST** (`2026-11-12T21:00:00Z`) on both platforms.
**Submitted:** 2026-10-18 via Blotato MCP. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-11-12T21:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `33279552-8c88-4853-bd76-73bea18ac441` | SCHEDULED |
| 2026-11-12T21:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `488f0ead-5e58-4a61-b540-0c1a6f9579a4` | SCHEDULED |

**Account check.** This preset posts to the **personal** profile, so `pageId` is deliberately omitted —
passing `94095464` would send it to the MZS company page instead. The workspace holds a second LinkedIn
account with the same display name; `26694` is the correct one. Verified after submission with
`blotato_list_schedules`: both rows carry `target: { targetType: "linkedin" }` with no `pageId`.

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn
(`smc-1792374983671-2.jpg`) and 4:5 for Instagram (`smc-1792374983680-3.jpg`), since a 16:9 hero gets cropped in
the IG feed. Both served from their Zipline URLs. Zipline expires files after 90 days (≈2027-01-16); the
local `hero-*.jpg` files are the durable copies.

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1, 2026. Every slot in this batch was computed from
its own date rather than copied from the October runs, which used `20:00:00Z` correctly for EDT.

**Note.** Corrections from here mean editing a live Blotato schedule. `blotato_update_schedule` takes the
**numeric schedule ID**, not the submission IDs above, and this post is past the first page of
`blotato_list_schedules` — page with the cursor (this batch needed two pages). To change only the time,
omit `post` entirely; a partial `post` silently drops the fields it leaves out.
