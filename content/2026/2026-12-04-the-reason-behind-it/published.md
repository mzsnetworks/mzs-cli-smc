# Published — 2026-12-04-the-reason-behind-it

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Fri Dec 4 (2026-12-04) at 4:00 PM **EST** (`2026-12-04T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `952a91df-a9b6-4e4a-acb7-e571c5bcf873` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `5a5f3873-3650-440e-a7e1-20d30984eadf` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `b7fda490-241d-428b-9d4d-5865f20c5a27` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `0d407f05-770a-4d0b-8bb9-9ba88dafd5f9` | SCHEDULED |

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1. Verified after submission by converting each
returned `scheduledAt` back to America/New_York.

**Verified before publish** with `tools/check-renders.py` — zero failures, zero warnings. All ten slides
fetched back from storage and compared byte-for-byte with the local PNG before submission. Facebook and X
carry the hero from its Zipline URL (`smc-1792373404102-2.jpg`); the local `hero-01.jpg` is the durable copy.

**`pageId: 94095464`** passed explicitly on the LinkedIn call.

**Note.** There are now 110 future schedules. This post is **two pages deep** in
`blotato_list_schedules` — page with the cursor twice to find its numeric schedule ID.
`blotato_update_schedule` does not take the submission IDs above. To change only the time, omit `post`.
