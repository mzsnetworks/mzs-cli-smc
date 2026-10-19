# Published — 2026-12-02-first-touch

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Wed Dec 2 (2026-12-02) at 4:00 PM **EST** (`2026-12-02T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `2c68a353-35c6-4c0e-be0c-8eebd460aa8a` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `e1e1e1d9-cb21-44e7-b288-876f747b32d4` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `d6f5be95-749e-436f-a4c8-ab947f2e3672` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `68905cc3-4e12-47bd-ba5d-b85810f4459e` | SCHEDULED |

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1. Verified after submission by converting each
returned `scheduledAt` back to America/New_York.

**Verified before publish** with `tools/check-renders.py` — zero failures, zero warnings. All ten slides
fetched back from storage and compared byte-for-byte with the local PNG before submission. Facebook and X
carry the hero from its Zipline URL (`smc-1792373404094-1.jpg`); the local `hero-01.jpg` is the durable copy.

**`pageId: 94095464`** passed explicitly on the LinkedIn call.

**Note.** There are now 110 future schedules. This post is **two pages deep** in
`blotato_list_schedules` — page with the cursor twice to find its numeric schedule ID.
`blotato_update_schedule` does not take the submission IDs above. To change only the time, omit `post`.
