# Published — sla-is-not-a-design

**Preset:** Business (all four on the MZS account)
**Scheduled:** 2026-09-02 4:00 PM EDT (`2026-09-02T20:00:00Z`)
**Media:** LinkedIn + Instagram → **9-slide carousel** (Blotato public_media PNGs, in order). Facebook + X → `hero-01.jpg` 16:9 (Zipline `smc-1787804153196-0.jpg`). X = single post.

| Platform | Account | Submission ID | Status |
|----------|---------|---------------|--------|
| LinkedIn (MZS company page · pageId 94095464) | 26694 | `8cfd29d5-c5d8-4cd4-9094-df4c4b04475b` | scheduled |
| Facebook (MZS page · 779757178552278) | 38836 | `971b5089-d8b4-4942-8050-412accf61c09` | scheduled |
| Instagram (@mzsnetworks · carousel) | 55865 | `f1cdadec-8bb7-408a-b78d-10541ac989cc` | scheduled |
| X (@mzsnetworks · single) | 21162 | `30c280f0-e2c4-47ba-b5c4-c73182f249ec` | scheduled |

**Scores:** LI 91 · FB 88 · IG 89 · X 88. Factcheck PASS (no statistics — the 99.99% is quoted as a contract term, not a measured claim).

**Notes:**
- Hero: an underground cutaway beneath a stone bridge, two supposedly diverse fiber paths converging into one duct, red mark on the convergence point. First pass, no rework needed.
- The distinction the post turns on: an SLA transfers risk, it doesn't reduce it. Deliberately avoids re-treading `resilience-isnt-redundancy` (Aug 14), which was about untested failover rather than contract-vs-physical-path.
- X single trimmed to 263 after a first draft landed at exactly 280 — no margin at the hard cap.
- Carousel PNGs regenerable: `node tools/render-carousel.mjs content/2026/2026-09-02-sla-is-not-a-design`.

Live URLs resolve after the scheduled time — poll via `blotato_get_post_status`.
