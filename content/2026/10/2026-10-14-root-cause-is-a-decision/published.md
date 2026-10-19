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

**Correction — 2026-09-20.** `facebook.md and linkedin.md` ran over the length band (FB 774 → 695, LI 1918 → 1845 chars). The Facebook cap moved from 800 to a 760 FAIL line with a 550–700 draft target, and LinkedIn to a 1900 FAIL line, after `tools/check-renders.py` showed output clustering 1–5% under whatever number is actually enforced. Compressed the five-whys chain in both renders. Hook and landing are unchanged.

Live Blotato schedule updated in place: schedule IDs `4645450` (FB) and `4645443` (LI company page). Scheduled time, media and page target (FB page `779757178552278`, LI company page `94095464`) all carried through and verified by re-reading the schedule afterwards. The other renders on this post were not touched.
