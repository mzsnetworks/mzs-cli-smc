# Published — 2026-11-27-sold-on-speed

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Fri Nov 27 (2026-11-27) at 4:00 PM **EST** (`2026-11-27T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `ca6ace93-2166-4923-9e8d-6ce7aa2772a6` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `e0093d7e-c236-45a5-96ee-afa99e9e38b3` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `38354ba0-e854-4ac3-93eb-5836a149d068` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `a5545f6f-c232-4336-a4d9-987232f7594a` | SCHEDULED |

**EST, not EDT.** 4:00 PM local is `21:00:00Z` from Nov 1. Verified after submission by converting each
returned `scheduledAt` back to America/New_York.

**Verified before publish** with `tools/check-renders.py` — zero failures, zero warnings. All ten slides
fetched back from storage and compared byte-for-byte with the local PNG before submission. Facebook and X
carry the hero from its Zipline URL (`smc-1792372580809-2.jpg`); the local `hero-01.jpg` is the durable copy.

**`pageId: 94095464`** passed explicitly on the LinkedIn call.

**Note.** Past the first page of `blotato_list_schedules` — page with the cursor to find the numeric
schedule ID. To change only the time, omit `post`; a partial `post` drops whatever it leaves out.
