# Published — five-questions-before-wireless

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Sun Oct 25 (2026-10-25) at 4:00 PM EDT (`2026-10-25T20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP, as part of the Oct 25–30 Business week. All four accepted, no failures.

| Time (UTC) | Platform | Render | Media | Submission ID | Status |
|------------|----------|--------|-------|---------------|--------|
| 2026-10-25T20:00:00Z | LinkedIn (MZS Networks company page `94095464`) | `linkedin.md` | carousel, 10 slides | `7104ed89-0261-4146-9f3b-45bff4a1a137` | SCHEDULED |
| 2026-10-25T20:00:00Z | Instagram @mzsnetworks | `instagram.md` | carousel, 10 slides | `59e18266-f297-421d-bf52-f3462187a0aa` | SCHEDULED |
| 2026-10-25T20:00:00Z | Facebook page `779757178552278` | `facebook.md` | hero 16:9 | `b294380e-22fe-4646-9f9d-b8b36a95cfa2` | SCHEDULED |
| 2026-10-25T20:00:00Z | X @mzsnetworks | `x.md` — Single | hero 16:9 | `205dac0c-82fe-4afa-a7f0-69699a996ce1` | SCHEDULED |

**Media.** LinkedIn and Instagram carry the full 10-slide carousel, uploaded to Blotato storage via presigned URLs; all thirty were verified to serve PNG bytes after upload. Facebook and X carry the text-free 16:9 hero straight from its Zipline URL (`https://zipline.mzstools.net/raw/smc-1789946551629-0.jpg`), verified to return JPEG bytes. Zipline expires files after 90 days (≈2026-12-19); the local `hero-01.jpg` is the durable copy, and Blotato copies media into its own storage at submission time, so the expiry does not affect these scheduled posts.

**Accounts verified at submission.** `blotato_list_accounts` was called first: the LinkedIn company-page subaccount `94095464` was present. It has gone missing before, and omitting `pageId` silently posts to the personal profile instead.

**Note.** Any correction from here means editing a live Blotato schedule, not a file. `blotato_update_schedule` takes the **numeric schedule ID**, not the submission IDs above — find it by paging `blotato_list_schedules`. Note also that `pageId` lives in `draft.target`, not `draft.content`, so a round-trip that drops it will move the post to the wrong destination.
