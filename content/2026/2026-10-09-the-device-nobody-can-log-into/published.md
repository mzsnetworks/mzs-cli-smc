# Published — 2026-10-09-the-device-nobody-can-log-into

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Fri Oct 9 (2026-10-09) at 4:00 PM EDT (`20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `336f3e03-45f2-4be7-a793-e00f5c09ed08` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `0783643a-b83b-4fb5-b184-4e3f2db866f2` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `336ced12-bf2e-4589-b9d4-29aa65ee767e` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `5a8c5533-8123-4d41-be39-3b50a5588ff7` | SCHEDULED |

**Media.** LinkedIn and Instagram carry all ten carousel slides in order — never a lone cover slide. The ten Blotato public URLs are recorded in `carousel-urls.json`; each upload returned HTTP 200 and each URL was then fetched and confirmed to start with the PNG magic bytes `89504e470d0a1a0a`. Facebook and X carry the 16:9 hero from `hero.json` (`smc-1789939536469-2.jpg`), read from the file rather than typed.

**LinkedIn company page.** `pageId: 94095464` was passed explicitly. That subaccount was absent from `blotato_list_accounts` on 2026-09-09 and again on the morning of 2026-09-20, and had returned by that afternoon with nothing reconnected manually — so it is verified per run. Omitting the pageId does not error; it silently posts to Luis's personal profile, which would put company-voice copy on the wrong account.

**No statistics** in any render, so Factcheck passed with no source gate and the marketing illustrative-figure exception is not in play (that exception is `marketing/` only regardless).
