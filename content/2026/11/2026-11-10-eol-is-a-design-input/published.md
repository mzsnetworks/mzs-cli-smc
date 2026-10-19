# Published — 2026-11-10-eol-is-a-design-input

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Tue 2026-11-10 at 4:00 PM **EST** (`2026-11-10T21:00:00Z`) on both platforms.
**Submitted:** 2026-10-18 via Blotato MCP. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-11-10T21:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `b1c98f05-ee15-4c26-afce-41405d49eded` | SCHEDULED |
| 2026-11-10T21:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `6fdacd4e-c981-4540-b103-2765fbcc2da0` | SCHEDULED |

**Account check.** This preset posts to the **personal** profile, so `pageId` is deliberately omitted —
passing `94095464` would send it to the MZS company page instead. The workspace holds a second LinkedIn
account with the same display name; `26694` is the correct one. Verified after submission with
`blotato_list_schedules`: both rows carry `target: { targetType: "linkedin" }` with no `pageId`.

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn
(`smc-1792374983655-0.jpg`) and 4:5 for Instagram (`smc-1792374983659-1.jpg`), since a 16:9 hero gets cropped in
the IG feed. Both served from their Zipline URLs. Zipline expires files after 90 days (≈2027-01-16); the
local `hero-*.jpg` files are the durable copies.

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1, 2026. Every slot in this batch was computed from
its own date rather than copied from the October runs, which used `20:00:00Z` correctly for EDT.

**Note.** Corrections from here mean editing a live Blotato schedule. `blotato_update_schedule` takes the
**numeric schedule ID**, not the submission IDs above, and this post is past the first page of
`blotato_list_schedules` — page with the cursor (this batch needed two pages). To change only the time,
omit `post` entirely; a partial `post` silently drops the fields it leaves out.
