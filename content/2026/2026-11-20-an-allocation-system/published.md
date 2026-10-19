# Published — 2026-11-20-an-allocation-system

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Fri Nov 20 (2026-11-20) at 4:00 PM **EST** (`2026-11-20T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `650630de-3351-499a-ab25-739215048040` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `3465ee92-6030-4030-b645-b8f70a3b6d6e` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `6a5fa8d2-2451-44f6-a659-2c17ec07945b` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `6dbb3be7-714e-4c96-98fa-dc3003c77ce7` | SCHEDULED |

**EST, not EDT.** Daylight time ended Sun Nov 1, so 4:00 PM local is `21:00:00Z`. Verified after
submission by converting each returned `scheduledAt` back to America/New_York; all four read 4:00 PM EST.

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload was fetched back and compared
byte-for-byte against the local PNG before submission. Facebook and X carry the hero served from its
Zipline URL (`smc-1792371136105-2.jpg`). Zipline expires files after 90 days (≈2027-01-16); the local `hero-*.jpg` is the
durable copy, and Blotato copies media into its own storage at submission time.

**`pageId: 94095464`** passed explicitly on the LinkedIn call — omitting it posts to the personal profile.

**Note.** This post is past the first page of `blotato_list_schedules` — there are now more than fifty
future schedules, so any correction has to page with the cursor to find the **numeric schedule ID**
(`blotato_update_schedule` does not take the submission IDs above). To change only the time, omit `post`
entirely; a partial `post` silently drops whatever it leaves out.
