# Published — uptime-is-lagging

**Preset:** Business (all four on the MZS account)
**Scheduled:** 2026-08-28 4:00 PM EDT (`2026-08-28T20:00:00Z`)
**Media:** LinkedIn + Instagram → **9-slide carousel** (Blotato public_media PNGs, in order). Facebook + X → `hero-01.jpg` 16:9 (Zipline `smc-1787801614015-0.jpg`). X = single post.

| Platform | Account | Submission ID | Status |
|----------|---------|---------------|--------|
| LinkedIn (MZS company page · pageId 94095464) | 26694 | `2237cacf-f581-4bcf-89e5-5a30c3941282` | scheduled |
| Facebook (MZS page · 779757178552278) | 38836 | `d69315cd-7330-4d97-bc86-2de3266347a5` | scheduled |
| Instagram (@mzsnetworks · carousel) | 55865 | `d6fd72e9-b146-4d4b-9774-09dc2070601a` | scheduled |
| X (@mzsnetworks · single) | 21162 | `5fc5e8d4-c8b6-410b-bdc4-0a235c84c68c` | scheduled |

**Scores:** LI 90 · FB 88 · IG 88 · X 87. Factcheck PASS.

**Sources:** DORA (Google Cloud), *State of DevOps Report* — throughput and stability rise together; the highest performers lead on both rather than trading one for the other. https://dora.dev/research/

**Notes:**
- The only cited claim in the set. LinkedIn carries it as a plain `Source:` line before the hashtags rather than a markdown Sources block; Facebook and Instagram cite DORA inline; the X single makes no statistical claim.
- Hero metaphor: a corridor where the lit ribbon runs backward and the path ahead is dark, one red line marking the turn nobody can see.
- Carousel PNGs regenerable: `node tools/render-carousel.mjs content/2026/2026-08-28-uptime-is-lagging`.

Live URLs resolve after the scheduled time — poll via `blotato_get_post_status`.
