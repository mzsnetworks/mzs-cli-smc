# Published — first-thirty-days

**Preset:** Marketing — LinkedIn only, Luis Mazariegos' personal profile (Blotato account `26694`, no `pageId`).
**Scheduled:** Mon Oct 5 (2026-10-05). Spanish at 2:00 PM EDT, English at 4:00 PM EDT.
**Submitted:** 2026-09-20 via Blotato MCP, as part of a five-Monday batch (Sep 28 – Oct 26). Both accepted, no failures.

| Time (UTC) | Local (EDT) | Platform | Language | Render | Submission ID | Status |
|------------|-------------|----------|----------|--------|---------------|--------|
| 2026-10-05T18:00:00Z | 2:00 PM | LinkedIn (personal) | ES | `linkedin-es.md` | `43c7451b-1f7e-4d6a-923d-899503354a1c` | SCHEDULED |
| 2026-10-05T20:00:00Z | 4:00 PM | LinkedIn (personal) | EN | `linkedin.md` | `a9ecd0fd-260e-4d58-9f51-07fe5329a91e` | SCHEDULED |

**Media:** both submissions carry the same text-free hero, `hero-01.jpg` → `https://zipline.mzstools.net/raw/smc-1789936810630-1.jpg`. URL read from `hero.json`, never typed, and verified to return JPEG bytes after submission. Zipline expires files after 90 days (≈2026-12-19); the local `hero-01.jpg` is the durable copy.

**Note:** scheduled well ahead of publication. Any correction from here means editing a live Blotato schedule rather than a file — the submission IDs above are the handles for `blotato_update_schedule`.

**Correction — 2026-09-20.** The English render was missing a clause the Spanish carried ("y normalmente está fundada en algo real"). Paragraph 2 ran one sentence in EN against two in ES. English was expanded to match and the live schedule updated: Blotato schedule ID **`4644074`** (not the submission ID above — `blotato_update_schedule` takes the numeric schedule ID, found by paging `blotato_list_schedules`). Time, media and account unchanged; ES untouched. Found by the sentence-count parity check in `tools/check-renders.py`, which the earlier character-ratio check had missed — one extra sentence inside a long paragraph moves the ratio only to 1.16.
