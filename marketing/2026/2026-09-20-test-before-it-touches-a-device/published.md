# Published — test-before-it-touches-a-device

**Preset:** Marketing — LinkedIn only, Luis Mazariegos' personal profile (Blotato account `26694`, no `pageId`).
**Scheduled:** Mon Oct 19 (2026-10-19). Spanish at 2:00 PM EDT, English at 4:00 PM EDT.
**Submitted:** 2026-09-20 via Blotato MCP, as part of a five-Monday batch (Sep 28 – Oct 26). Both accepted, no failures.

| Time (UTC) | Local (EDT) | Platform | Language | Render | Submission ID | Status |
|------------|-------------|----------|----------|--------|---------------|--------|
| 2026-10-19T18:00:00Z | 2:00 PM | LinkedIn (personal) | ES | `linkedin-es.md` | `c0e13966-2a1e-4690-b8e1-383eca69230e` | SCHEDULED |
| 2026-10-19T20:00:00Z | 4:00 PM | LinkedIn (personal) | EN | `linkedin.md` | `47236ac0-1ec6-44d2-887c-df405e4dbfc0` | SCHEDULED |

**Media:** both submissions carry the same text-free hero, `hero-01.jpg` → `https://zipline.mzstools.net/raw/smc-1789936810658-3.jpg`. URL read from `hero.json`, never typed, and verified to return JPEG bytes after submission. Zipline expires files after 90 days (≈2026-12-19); the local `hero-01.jpg` is the durable copy.

**Note:** scheduled well ahead of publication. Any correction from here means editing a live Blotato schedule rather than a file — the submission IDs above are the handles for `blotato_update_schedule`.

**Correction — 2026-09-20.** The English render was missing a sentence the Spanish carried ("Nadie lo llamaría una prueba en ningún otro lugar de la organización"). Paragraph 2 ran two sentences in EN against three in ES. English was expanded to match and the live schedule updated: Blotato schedule ID **`4644083`** (not the submission ID above — `blotato_update_schedule` takes the numeric schedule ID, found by paging `blotato_list_schedules`). Time, media and account unchanged; ES untouched. Found by the sentence-count parity check in `tools/check-renders.py`.
