---
description: Publish a SHIP-gated post live to LinkedIn, Facebook, Instagram, and X via Blotato
argument-hint: <slug of a finished idea folder>
---

Publish an existing, **SHIP-gated** idea live through Blotato.

Target idea: **$ARGUMENTS**

Follow `agents/PUBLISH.md` exactly. In short:

1. **Resolve + gate.** Find the folder for `$ARGUMENTS` via `content/INDEX.md`. Status must be SHIP — if not, stop and point the user at `/post` or `/adapt`.

2. **Backfill.** If a render is missing (e.g. `facebook.md` on an older post), run Adapter → Editor → Hashtag → Scorer for that platform to SHIP first.

3. **Ask the run questions** (one round): platforms to publish, LinkedIn personal vs company page, timing (now / next free slot / scheduled), and single-vs-thread for X.

4. **Media.** Instagram requires media — use the folder's carousel or infographic; if none exists, run the Visual agent (with its approval gate) first. Upload local PNGs via `blotato_create_presigned_upload_url` + `curl PUT`, then use the public URLs.

5. **Final gate.** Show the exact text per platform. **Wait for explicit "publish."**

6. **Publish + verify** via `blotato_create_post` / `blotato_get_post_status`. Report live URLs and any failures honestly.

7. **Record.** Write `published.md` in the idea folder and set the post's `content/INDEX.md` row to PUBLISHED.

If `$ARGUMENTS` is empty, list SHIP-status posts from `content/INDEX.md` and ask which to publish.
