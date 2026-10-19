# Published — 2026-11-07-ttls-are-a-plan

**Preset:** Professional — LinkedIn **personal profile** (Blotato account `26694`, **no `pageId`**) + Instagram @mzsnetworks (`55865`).
**Scheduled:** Sat Nov 7 (2026-11-07) at 4:00 PM **EST** (`2026-11-07T21:00:00Z`) on both platforms.
**Submitted:** 2026-10-18 via Blotato MCP. Both accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-11-07T21:00:00Z | LinkedIn (personal) | `linkedin.md` | hero 16:9 | `7e135ccd-a421-4cc8-8c7d-9f6c58ddbe6e` | SCHEDULED |
| 2026-11-07T21:00:00Z | Instagram @mzsnetworks | `instagram.md` | hero 4:5 | `7613771c-3908-4582-9808-7662cf2244b4` | SCHEDULED |

**Account check.** This preset posts to the **personal** profile, so `pageId` is deliberately omitted —
passing `94095464` would send it to the MZS company page instead. The workspace holds a second LinkedIn
account (`34721`) with the same display name; `26694` is the correct one.

**Media.** Two separately composed heroes, not one image cropped twice: 16:9 for LinkedIn
(`smc-1792374351989-0.jpg`) and 4:5 for Instagram (`smc-1792374351993-1.jpg`), since a 16:9 hero gets cropped in the IG feed.
Both served from their Zipline URLs and verified to return JPEG bytes before submission. Zipline expires
files after 90 days (≈2027-01-16); the local `hero-*.jpg` files are the durable copies.

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1.

**Corrected after submission.** The LinkedIn render shipped with the British spelling "honour", which
`tools/check-renders.py` did not catch because the word was missing from its BRITISH list. Found by reading
the submitted text back. Fixed in the repo, the word list extended (honour, favour, behaviour, colour,
labour, licence, defence, offence, analyse, catalogue, dialogue and inflections), and the live LinkedIn
schedule corrected in place via `blotato_update_schedule` on numeric id `5742040` — a full `post`
replacement carrying the media URL forward and omitting `pageId`, which this preset must not have. Verified
afterwards with `blotato_get_schedule`: text corrected, media intact, no pageId, time unchanged. The
Instagram render already read "honor" and was untouched.

**Note.** Corrections from here mean editing a live Blotato schedule. `blotato_update_schedule` takes the
**numeric schedule ID**, not the submission IDs above, and this post is past the first page of
`blotato_list_schedules` — page with the cursor.
