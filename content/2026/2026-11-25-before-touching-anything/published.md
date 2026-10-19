# Published — 2026-11-25-before-touching-anything

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Wed Nov 25 (2026-11-25) at 4:00 PM **EST** (`2026-11-25T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `01cc5de4-d3ea-45e7-a3db-f89908765e1c` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `b6a1fdba-02d5-4e0a-896b-a231476b4ce1` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `ab70b362-33af-46db-9997-4b3b1511dde4` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `2f6d19ef-6b69-4795-8a96-a15f79bd8f5d` | SCHEDULED |

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1. Verified after submission by converting each
returned `scheduledAt` back to America/New_York.

**Verified before publish** with `tools/check-renders.py` — zero failures, zero warnings. All ten slides
fetched back from storage and compared byte-for-byte with the local PNG before submission. Facebook and X
carry the hero from its Zipline URL (`smc-1792372580804-1.jpg`); the local `hero-01.jpg` is the durable copy.

**`pageId: 94095464`** passed explicitly on the LinkedIn call.

**Note.** Past the first page of `blotato_list_schedules` — page with the cursor to find the numeric
schedule ID. To change only the time, omit `post`; a partial `post` drops whatever it leaves out.
