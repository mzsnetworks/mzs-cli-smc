---
description: Publish a SHIP-gated post live via Blotato — LinkedIn, Facebook, Instagram, X, or the marketing lane's LinkedIn EN+ES pair
argument-hint: <slug of a finished idea folder>
---

Publish an existing, **SHIP-gated** idea live through Blotato.

Target idea: **$ARGUMENTS**

Follow `agents/PUBLISH.md` exactly. In short:

1. **Resolve + gate.** Find the folder for `$ARGUMENTS` by searching **both** catalogs — `content/INDEX.md` and `marketing/INDEX.md`. The tree it lives in determines the preset. Status must be SHIP — if not, stop and point the user at `/post` or `/adapt`.

2. **Verify.** Run `python3 tools/check-renders.py <postdir>`. Any failure blocks the publish.

3. **Backfill.** If a render is missing (e.g. `facebook.md` on an older post), run Adapter → Editor → Hashtag → Scorer for that platform to SHIP first.

3. **Ask the run questions** (one round): platforms to publish, LinkedIn personal vs company page, timing (now / next free slot / scheduled), and single-vs-thread for X. A named preset answers the first two; the **Marketing** preset answers all four — LinkedIn personal profile, twice, ES at `18:00:00Z` and EN at `20:00:00Z` on the same Monday — so ask nothing and go straight to the final gate.

4. **Media.** Instagram requires media — use the folder's carousel or infographic; if none exists, run the Visual agent (with its approval gate) first. Upload local PNGs via `blotato_create_presigned_upload_url` + `curl PUT`, then use the public URLs. **Read every media URL out of `hero.json`; never type one from memory.** Marketing ES posts take a text-free hero or nothing — never carousel slides.

5. **Final gate.** Show the exact text per submission — for a marketing post, the Spanish and the English side by side. **Wait for explicit "publish."**

6. **Publish + verify** via `blotato_create_post` / `blotato_get_post_status`. Report live URLs and any failures honestly.

7. **Record.** Write `published.md` in the idea folder (one row per submission, language included for a marketing pair) and set the post's row to PUBLISHED in its own tree's index — `content/INDEX.md` or `marketing/INDEX.md`.

If `$ARGUMENTS` is empty, list SHIP-status posts from both `content/INDEX.md` and `marketing/INDEX.md` and ask which to publish.
