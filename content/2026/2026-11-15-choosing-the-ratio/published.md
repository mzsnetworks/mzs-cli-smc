# Published — 2026-11-15-choosing-the-ratio

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Sun Nov 15 (2026-11-15) at 4:00 PM **EST** (`2026-11-15T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `b40e1a1c-33b4-4873-a70e-b14ca133e131` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `ef621969-8d2c-465e-bb30-c8bfbb2ff1e8` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `e8b97e1e-8ebc-41d9-ab07-668726fc47db` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `47442943-77fd-4b56-920a-4f85fb157e4b` | SCHEDULED |

**EST, not EDT.** Daylight time ended Sun Nov 1, so 4:00 PM local is `21:00:00Z`. Verified after
submission by converting each returned `scheduledAt` back to America/New_York; all four read 4:00 PM EST.

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload was fetched back and compared
byte-for-byte against the local PNG before submission. Facebook and X carry the hero served from its
Zipline URL (`smc-1792371231294-0.jpg`). Zipline expires files after 90 days (≈2027-01-16); the local `hero-*.jpg` is the
durable copy, and Blotato copies media into its own storage at submission time.

**`pageId: 94095464`** passed explicitly on the LinkedIn call — omitting it posts to the personal profile.

**Note.** This post is past the first page of `blotato_list_schedules` — there are now more than fifty
future schedules, so any correction has to page with the cursor to find the **numeric schedule ID**
(`blotato_update_schedule` does not take the submission IDs above). To change only the time, omit `post`
entirely; a partial `post` silently drops whatever it leaves out.
