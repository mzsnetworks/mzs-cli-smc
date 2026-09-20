# Published — 2026-10-11-branch-build-two-days

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Oct 11 (2026-10-11) at 4:00 PM EDT (`20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `817cfd28-f4d6-448d-9f30-decb77db8cd8` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `4d577917-24c5-43c5-86a5-d3c44094597e` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `43737fd7-34b1-4aa3-a600-cdd2c381f2f8` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `bea539fc-e1c1-4e92-a888-afcc9ef76c0c` | SCHEDULED |

**Media.** All ten carousel slides to LinkedIn and Instagram, in order. Each upload returned HTTP 200 and each public URL was then fetched and confirmed to begin with the PNG magic bytes — a 200 on PUT proves the write was accepted, not that the object serves. URLs recorded in `carousel-urls.json`. Facebook and X carry the hero from `hero.json` (`smc-1789940947139-0.jpg`), read from the file rather than typed.

**`pageId: 94095464`** passed explicitly on the LinkedIn call. Omitting it does not error; it silently posts to the personal profile.
