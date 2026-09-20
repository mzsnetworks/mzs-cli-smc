# Published — 2026-10-18-time-to-safe-change

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Oct 18 (2026-10-18) at 4:00 PM EDT (`20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `16b5ca98-eaa0-4db2-ab3f-15adbeb60201` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `e81dbb01-2b74-4879-924d-1fff32b40856` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `94b76a2a-bd40-4725-b9a6-c42026a9e875` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `cabf3338-15ed-422e-b8e4-e0e53f75979a` | SCHEDULED |

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings. First batch written with the checker in the loop; it caught Facebook over the cap on two of three drafts before commit.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload returned HTTP 200 and each public URL was then fetched and confirmed to serve PNG bytes. URLs in `carousel-urls.json`. Facebook and X carry the hero from `hero.json` (`smc-1789943745650-0.jpg`).

**`pageId: 94095464`** passed explicitly on the LinkedIn call.
