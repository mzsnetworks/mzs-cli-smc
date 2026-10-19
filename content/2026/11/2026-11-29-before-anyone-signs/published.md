# Published — 2026-11-29-before-anyone-signs

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Sun Nov 29 (2026-11-29) at 4:00 PM **EST** (`2026-11-29T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `58ad0aca-35eb-4829-8270-8063b1821fa6` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `9e6f5a12-a0d9-4345-a962-607deaa5e59b` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `29928a34-45ce-4f4d-b01f-b93f57a68dba` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `1f321f8a-6cc9-4016-a615-48fcbb54f5d3` | SCHEDULED |

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1. Verified after submission by converting each
returned `scheduledAt` back to America/New_York.

**Verified before publish** with `tools/check-renders.py` — zero failures, zero warnings. All ten slides
fetched back from storage and compared byte-for-byte with the local PNG before submission. Facebook and X
carry the hero from its Zipline URL (`smc-1792373404089-0.jpg`); the local `hero-01.jpg` is the durable copy.

**`pageId: 94095464`** passed explicitly on the LinkedIn call.

**Note.** There are now 110 future schedules. This post is **two pages deep** in
`blotato_list_schedules` — page with the cursor twice to find its numeric schedule ID.
`blotato_update_schedule` does not take the submission IDs above. To change only the time, omit `post`.
