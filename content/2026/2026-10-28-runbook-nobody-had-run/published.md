# Published — runbook-nobody-had-run

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Wed Oct 28 (2026-10-28) at 4:00 PM EDT (`2026-10-28T20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP, as part of the Oct 25–30 Business week. All four accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-10-28T20:00:00Z | LinkedIn (MZS Networks company page `94095464`) | `linkedin.md` | carousel, 10 slides | `0b2b3fab-df6b-4224-87d9-7cdd14fc8149` | SCHEDULED |
| 2026-10-28T20:00:00Z | Instagram @mzsnetworks | `instagram.md` | carousel, 10 slides | `a52eb04e-d5ef-4a2c-b1a6-bed20c365508` | SCHEDULED |
| 2026-10-28T20:00:00Z | Facebook page `779757178552278` | `facebook.md` | hero 16:9 | `4e598a75-c83c-420e-a08b-a88fbe32c055` | SCHEDULED |
| 2026-10-28T20:00:00Z | X @mzsnetworks | `x.md` — Single | hero 16:9 | `abbae104-fac6-4ce8-b33f-7f396ef4af2c` | SCHEDULED |

**Media.** LinkedIn and Instagram carry the full 10-slide carousel, uploaded to Blotato storage via presigned URLs; all thirty were verified to serve PNG bytes after upload. Facebook and X carry the text-free 16:9 hero straight from its Zipline URL (`https://zipline.mzstools.net/raw/smc-1789946551632-1.jpg`), verified to return JPEG bytes. Zipline expires files after 90 days (≈2026-12-19); the local `hero-01.jpg` is the durable copy, and Blotato copies media into its own storage at submission time, so the expiry does not affect these scheduled posts.

**Accounts verified at submission.** `blotato_list_accounts` was called first: the LinkedIn company-page subaccount `94095464` was present. It has gone missing before, and omitting `pageId` silently posts to the personal profile instead.

**Note.** Any correction from here means editing a live Blotato schedule, not a file. `blotato_update_schedule` takes the **numeric schedule ID**, not the submission IDs above — find it by paging `blotato_list_schedules`. Note also that `pageId` lives in `draft.target`, not `draft.content`, so a round-trip that drops it will move the post to the wrong destination.
