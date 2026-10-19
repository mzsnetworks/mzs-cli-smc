# Published — 2026-11-11-post-incident-actions-expire

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Wed Nov 11 (2026-11-11) at 4:00 PM **EST** (`2026-11-11T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `a8c1b982-7486-44dc-a801-ccef725ca499` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `587dd2ac-c565-4af3-ba39-ccaab0cb506a` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `2ae1b69d-5afd-4a6f-8b9c-32951460278f` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `c01e1474-d51a-49c5-ac3c-061d5eb4fe07` | SCHEDULED |

**EST, not EDT.** Daylight time ended Sun Nov 1, so 4:00 PM local is `21:00:00Z`. Verified after
submission by converting each returned `scheduledAt` back to America/New_York; all four read 4:00 PM EST.

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload was fetched back and compared
byte-for-byte against the local PNG before submission. Facebook and X carry the hero served from its
Zipline URL (`smc-1792369562381-1.jpg`). Zipline expires files after 90 days (≈2027-01-16); the local `hero-*.jpg` is the
durable copy, and Blotato copies media into its own storage at submission time.

**Carousel slide 10 carries the fixed CTA render** — the renderer colored accented words red on a red
band until 2026-10-18, which made the emphasized word invisible.

**`pageId: 94095464`** passed explicitly on the LinkedIn call — omitting it posts to the personal profile.

**Note.** Corrections from here mean editing a live Blotato schedule. `blotato_update_schedule` takes the
**numeric schedule ID**, not the submission IDs above, and it is past the first page of
`blotato_list_schedules` — page with the cursor. To change only the time, omit `post` entirely; a partial
`post` silently drops whatever it leaves out.
