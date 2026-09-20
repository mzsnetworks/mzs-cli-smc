# Published — tools-that-dont-talk

**Preset:** Marketing — LinkedIn only, Luis Mazariegos' personal profile (Blotato account `26694`, no `pageId`).
**Scheduled:** Mon Nov 16 (2026-11-16). Spanish at 2:00 PM EDT, English at 4:00 PM EDT.
**Submitted:** 2026-09-20 via Blotato MCP, in the Nov 2 – Dec 14 batch. Both accepted, no failures.

| Time (UTC) | Local | Platform | Language | Render | Submission ID | Status |
|------------|-------|----------|----------|--------|---------------|--------|
| 2026-11-16T18:00:00Z | 2:00 PM | LinkedIn (personal) | ES | `linkedin-es.md` | `5b4b9fe4-bddc-4ca9-9266-e26062ef50c4` | SCHEDULED |
| 2026-11-16T20:00:00Z | 4:00 PM | LinkedIn (personal) | EN | `linkedin.md` | `c7793523-11fb-480f-9c8e-773fa467bddd` | SCHEDULED |

**Media:** both submissions carry the same text-free hero, `hero-01.jpg` → `https://zipline.mzstools.net/raw/smc-1789937841245-2.jpg`. URL read from `hero.json`, never typed, and verified to return JPEG bytes after submission. Zipline expires files after 90 days (≈2026-12-19) — **that falls before some of these publish dates**, but Blotato fetched and stored the media at submission time, so the scheduled posts are unaffected. The local file is the durable copy.

**Note:** scheduled months ahead. Corrections from here mean editing a live Blotato schedule; the submission IDs above are the handles for `blotato_update_schedule`.

**Amended 2026-09-20 after scheduling.** The English render was submitted missing the "that role is on nobody's org chart" line, which its Spanish twin carried — a parallelism break introduced when the ES renders were expanded earlier the same day. `rules/SPANISH.md` requires both renders to carry the same beats.

The live schedule was corrected in place via `blotato_update_schedule` on schedule id `4644760` (the EN Nov 16 20:00:00Z entry; distinct from the submission id `c7793523-11fb-480f-9c8e-773fa467bddd` recorded above — the update API keys on schedule id, retrievable only through `blotato_list_schedules`). The existing Blotato-hosted media URL was passed through unchanged so the image was not re-fetched, and the amended text was read back with `blotato_get_schedule` to confirm.

Also worth recording: Blotato copies submitted media into its own storage at submission time, so the Zipline 90-day expiry does not affect already-scheduled posts.
