# Published — 2026-11-26-what-survives-you

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Thu 2026-11-26 at 4:00 PM **EST** (`2026-11-26T21:00:00Z`) on both platforms.
**Submitted:** 2026-10-18 via Blotato MCP. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Schedule ID | Status |
|------------|----------|--------|-------|---------------|-------------|--------|
| 2026-11-26T21:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `d7e3d0ab-66fd-4350-86d6-ababe4562d1c` | `5743534` | SCHEDULED |
| 2026-11-26T21:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `76c3e29e-9e7f-4c16-a022-e262377b205a` | `5743537` | SCHEDULED |

**Account check.** This preset posts to the **personal** profile, so `pageId` is deliberately omitted —
passing `94095464` would send it to the MZS company page instead. The workspace holds a second LinkedIn
account with the same display name; `26694` is the correct one. Verified after submission with
`blotato_list_schedules`: both rows carry `target: { targetType: "linkedin" }` with no `pageId`.

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn
(`smc-1792377575227-2.jpg`) and 4:5 for Instagram (`smc-1792377575231-3.jpg`), since a 16:9 hero gets cropped in
the IG feed. Both served from their Zipline URLs. Zipline expires files after 90 days (≈2027-01-16); the
local `hero-*.jpg` files are the durable copies. Both approved on the first roll.

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1, 2026, and stays that way until Mar 14, 2027.

**Note.** The schedule IDs above are what `blotato_update_schedule` takes — not the submission IDs. To
change only the time, omit `post` entirely; a partial `post` silently drops the fields it leaves out.
This post sits past the first page of `blotato_list_schedules`, so reaching it means paging with the cursor.
