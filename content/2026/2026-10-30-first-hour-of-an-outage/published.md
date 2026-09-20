# Published — first-hour-of-an-outage

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Fri Oct 30 (2026-10-30) at 4:00 PM EDT (`2026-10-30T20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP, as part of the Oct 25–30 Business week. All four accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-10-30T20:00:00Z | LinkedIn (MZS Networks company page `94095464`) | `linkedin.md` | carousel, 10 slides | `d445e0f0-5061-4c9a-9848-5fe78aa5a971` | SCHEDULED |
| 2026-10-30T20:00:00Z | Instagram @mzsnetworks | `instagram.md` | carousel, 10 slides | `ea5ad442-61e7-4cb0-af89-b9768d4e04bc` | SCHEDULED |
| 2026-10-30T20:00:00Z | Facebook page `779757178552278` | `facebook.md` | hero 16:9 | `039abafe-eca3-4a97-a5a4-025f160e2621` | SCHEDULED |
| 2026-10-30T20:00:00Z | X @mzsnetworks | `x.md` — Single | hero 16:9 | `2cd476ed-ba28-4288-a689-98b935bfef18` | SCHEDULED |

**Media.** LinkedIn and Instagram carry the full 10-slide carousel, uploaded to Blotato storage via presigned URLs; all thirty were verified to serve PNG bytes after upload. Facebook and X carry the text-free 16:9 hero straight from its Zipline URL (`https://zipline.mzstools.net/raw/smc-1789946551636-2.jpg`), verified to return JPEG bytes. Zipline expires files after 90 days (≈2026-12-19); the local `hero-01.jpg` is the durable copy, and Blotato copies media into its own storage at submission time, so the expiry does not affect these scheduled posts.

**Accounts verified at submission.** `blotato_list_accounts` was called first: the LinkedIn company-page subaccount `94095464` was present. It has gone missing before, and omitting `pageId` silently posts to the personal profile instead.

**Note.** Any correction from here means editing a live Blotato schedule, not a file. `blotato_update_schedule` takes the **numeric schedule ID**, not the submission IDs above — find it by paging `blotato_list_schedules`. Note also that `pageId` lives in `draft.target`, not `draft.content`, so a round-trip that drops it will move the post to the wrong destination.
