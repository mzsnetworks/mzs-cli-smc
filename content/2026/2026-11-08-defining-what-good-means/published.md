# Published — 2026-11-08-defining-what-good-means

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Sun Nov 8 (2026-11-08) at 4:00 PM **EST** (`2026-11-08T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `1e165cce-790e-447a-aa0e-93ff994c6517` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `9421d618-943d-4256-8f62-6b5494d7d3c1` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `ab674ad2-37b5-49a5-bd28-15dba3d7f8b2` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `ee53e5bc-f90b-4270-bc76-4d7944254379` | SCHEDULED |

**EST, not EDT.** Daylight time ended Sun Nov 1, so 4:00 PM local is `21:00:00Z`. Verified after
submission by converting each returned `scheduledAt` back to America/New_York; all four read 4:00 PM EST.

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload was fetched back and compared
byte-for-byte against the local PNG before submission. Facebook and X carry the hero served from its
Zipline URL (`smc-1792369615741-0.jpg`). Zipline expires files after 90 days (≈2027-01-16); the local `hero-*.jpg` is the
durable copy, and Blotato copies media into its own storage at submission time.

**Carousel slide 10 carries the fixed CTA render** — the renderer colored accented words red on a red
band until 2026-10-18, which made the emphasized word invisible.

**`pageId: 94095464`** passed explicitly on the LinkedIn call — omitting it posts to the personal profile.

**Note.** Corrections from here mean editing a live Blotato schedule. `blotato_update_schedule` takes the
**numeric schedule ID**, not the submission IDs above, and it is past the first page of
`blotato_list_schedules` — page with the cursor. To change only the time, omit `post` entirely; a partial
`post` silently drops whatever it leaves out.
