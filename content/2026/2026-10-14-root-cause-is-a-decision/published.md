# Published — 2026-10-14-root-cause-is-a-decision

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Oct 14 (2026-10-14) at 4:00 PM EDT (`20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `3a7e6b21-11b5-4b2a-8f96-5ccc4b36480e` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `6e961ff0-e65a-4861-a35e-89b5034de39f` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `b8594b26-675a-4790-aceb-95804ed418e4` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `e62a6fb7-d984-4143-995d-798f3b1e8f8e` | SCHEDULED |

**Media.** All ten carousel slides to LinkedIn and Instagram, in order. Each upload returned HTTP 200 and each public URL was then fetched and confirmed to begin with the PNG magic bytes — a 200 on PUT proves the write was accepted, not that the object serves. URLs recorded in `carousel-urls.json`. Facebook and X carry the hero from `hero.json` (`smc-1789940947142-1.jpg`), read from the file rather than typed.

**`pageId: 94095464`** passed explicitly on the LinkedIn call. Omitting it does not error; it silently posts to the personal profile.
