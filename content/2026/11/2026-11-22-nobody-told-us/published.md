# Published — 2026-11-22-nobody-told-us

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Sun Nov 22 (2026-11-22) at 4:00 PM **EST** (`2026-11-22T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `7c8c826a-be8c-417a-afa8-44ae092d82d5` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `0c54003c-6492-4ee1-a8e9-9cbe52d402dd` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `7a37849a-c8f0-4495-b324-e6b65d36925b` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `a161455e-3919-4575-a4bc-9c866a5cb75b` | SCHEDULED |

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1. Verified after submission by converting each
returned `scheduledAt` back to America/New_York.

**Verified before publish** with `tools/check-renders.py` — zero failures, zero warnings. All ten slides
fetched back from storage and compared byte-for-byte with the local PNG before submission. Facebook and X
carry the hero from its Zipline URL (`smc-1792372580800-0.jpg`); the local `hero-01.jpg` is the durable copy.

**`pageId: 94095464`** passed explicitly on the LinkedIn call.

**Note.** Past the first page of `blotato_list_schedules` — page with the cursor to find the numeric
schedule ID. To change only the time, omit `post`; a partial `post` drops whatever it leaves out.
