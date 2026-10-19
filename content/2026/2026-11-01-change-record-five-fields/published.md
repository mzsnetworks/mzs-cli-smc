# Published — 2026-11-01-change-record-five-fields

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Sun Nov 1 (2026-11-01) at 4:00 PM **EST** (`2026-11-01T21:00:00Z`) on every platform.
**Submitted:** 2026-10-18 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `d0635a45-53f6-4b5b-89c2-9827955554a9` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `0c9c065c-dfa6-43e9-8861-6641c9f49841` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `a9fbe92c-9b5b-467b-a19a-429e59893644` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `ca095813-49eb-4a38-9a6e-b4a764b5f2d8` | SCHEDULED |

**First batch on EST.** US daylight time ends Sun Nov 1, so 4:00 PM local is `21:00:00Z` here, not the
`20:00:00Z` every October post used. Verified after submission by converting each returned
`scheduledAt` back to America/New_York: all four read 4:00 PM EST.

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings. Every
render sits inside its draft target rather than just under the cap.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload was fetched back and compared
byte-for-byte against the local PNG before submission. Facebook and X carry the hero served straight from
its Zipline URL (`smc-1792368096730-0.jpg`), which returned JPEG bytes on check. Zipline expires files after 90 days
(≈2027-01-16); the local `hero-*.jpg` is the durable copy, and Blotato copies media into its own storage
at submission time, so the expiry does not affect these scheduled posts.

**Carousel slide 10 carries the fixed CTA render.** The renderer colored accented words red on a red band
until 2026-10-18, which made the emphasized word invisible; these were rendered after the fix.

**`pageId: 94095464`** passed explicitly on the LinkedIn call — omitting it posts to the personal profile.

**Note.** Any correction from here means editing a live Blotato schedule rather than a file.
`blotato_update_schedule` takes the **numeric schedule ID**, not the submission IDs above — find it by
paging `blotato_list_schedules`. To change only the time, omit `post` entirely; passing a partial `post`
silently drops whatever it leaves out.
