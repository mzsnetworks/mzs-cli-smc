# Published — 2026-10-16-two-sets-of-assumptions

**Preset:** Business — all four platforms on the MZS account.
**Scheduled:** Oct 16 (2026-10-16) at 4:00 PM EDT (`20:00:00Z`) on every platform.
**Submitted:** 2026-09-20 via Blotato MCP. All four accepted, no failures.

| Platform | Account | Page | Media | Submission ID | Status |
|----------|---------|------|-------|---------------|--------|
| LinkedIn | `26694` | company page `94095464` | full 10-slide carousel | `efa24eff-02ac-4f18-9bc3-03bd97649a94` | SCHEDULED |
| Facebook | `38836` | page `779757178552278` | 16:9 hero | `b6eed02d-0241-42d1-8158-e8ff07a72af3` | SCHEDULED |
| Instagram | `55865` | — | full 10-slide carousel | `385a543a-a1b2-41b5-a203-8820b86e405c` | SCHEDULED |
| X | `21162` | — | 16:9 hero (single, not thread) | `87ac9e96-dec2-4da9-82a7-1863f18b9ac7` | SCHEDULED |

**Media.** All ten carousel slides to LinkedIn and Instagram, in order. Each upload returned HTTP 200 and each public URL was then fetched and confirmed to begin with the PNG magic bytes — a 200 on PUT proves the write was accepted, not that the object serves. URLs recorded in `carousel-urls.json`. Facebook and X carry the hero from `hero.json` (`smc-1789940947146-2.jpg`), read from the file rather than typed.

**`pageId: 94095464`** passed explicitly on the LinkedIn call. Omitting it does not error; it silently posts to the personal profile.

**Correction — 2026-09-20.** `facebook.md` ran over the length band (792 → 705 chars). The Facebook cap moved from 800 to a 760 FAIL line with a 550–700 draft target, and LinkedIn to a 1900 FAIL line, after `tools/check-renders.py` showed output clustering 1–5% under whatever number is actually enforced. Tightened the technical list and the two examples. Hook and landing are unchanged.

Live Blotato schedule updated in place: schedule ID `4645490`. Scheduled time, media and page target (FB page `779757178552278`, LI company page `94095464`) all carried through and verified by re-reading the schedule afterwards. The other renders on this post were not touched.
