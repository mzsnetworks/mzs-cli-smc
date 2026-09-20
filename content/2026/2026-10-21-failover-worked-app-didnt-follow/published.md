# Published — 2026-10-21-failover-worked-app-didnt-follow

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Oct 21 (2026-10-21) at 4:00 PM EDT (`20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `d2b8bff0-ae6c-4f59-b2aa-c522aef316a4` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `b129760b-618c-4943-bf72-576cb7fda4a1` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `b3e7b79d-7ba6-42ea-9c94-e5361c0f9fa2` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `fcd368cb-197f-4ef8-9cc5-3fa89fe6c2ed` | SCHEDULED |

**Verified before publish** with `python3 tools/check-renders.py` — zero failures, zero warnings. First batch written with the checker in the loop; it caught Facebook over the cap on two of three drafts before commit.

**Media.** All ten slides to LinkedIn and Instagram, in order. Each upload returned HTTP 200 and each public URL was then fetched and confirmed to serve PNG bytes. URLs in `carousel-urls.json`. Facebook and X carry the hero from `hero.json` (`smc-1789943745654-1.jpg`).

**`pageId: 94095464`** passed explicitly on the LinkedIn call.
