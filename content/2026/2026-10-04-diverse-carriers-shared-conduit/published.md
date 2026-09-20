# Published — 2026-10-04-diverse-carriers-shared-conduit

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Sun Oct 4 (2026-10-04) at 4:00 PM EDT (`20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `ff7cb456-4fbe-4e86-b348-658be44bde98` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `41f22145-e0bf-481b-a035-7ed36c20a7ee` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `26b0679e-197f-4a55-b509-a79edd439f62` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `3e508180-9925-4701-add0-96abad15cfc3` | SCHEDULED |

**Media.** LinkedIn and Instagram carry all ten carousel slides in order — never a lone cover slide. The ten Blotato public URLs are recorded in `carousel-urls.json`; each upload returned HTTP 200 and each URL was then fetched and confirmed to start with the PNG magic bytes `89504e470d0a1a0a`. Facebook and X carry the 16:9 hero from `hero.json` (`smc-1789939536459-0.jpg`), read from the file rather than typed.

**LinkedIn company page.** `pageId: 94095464` was passed explicitly. That subaccount was absent from `blotato_list_accounts` on 2026-09-09 and again on the morning of 2026-09-20, and had returned by that afternoon with nothing reconnected manually — so it is verified per run. Omitting the pageId does not error; it silently posts to Luis's personal profile, which would put company-voice copy on the wrong account.

**No statistics** in any render, so Factcheck passed with no source gate and the marketing illustrative-figure exception is not in play (that exception is `marketing/` only regardless).
