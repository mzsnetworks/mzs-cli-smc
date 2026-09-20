---
description: Re-render an existing fact-checked master into its lane's platform posts (skips drafting)
argument-hint: <slug or path of an existing idea folder>
---

Re-render an **existing** idea whose `master.md` is already written and fact-checked. Use this when the master changed, a platform render needs rebuilding, or the renders are missing.

Target idea: **$ARGUMENTS**

## Steps

1. **Locate the folder.** Resolve `$ARGUMENTS` to `<tree>/<year>/<YYYY-MM-DD>-<slug>/`. If only a slug was given, search **both** trees — `content/` and `marketing/` — via their INDEX files. The tree you find it in sets the lane for every step below. Confirm `master.md` exists — if not, stop and tell the user to run `/post` instead.

2. **Confirm the master is clean.** Apply the FACTCHECK agent to `master.md`. If FAIL, stop and report — do not adapt an unverified master.

3. **Platform Adapter** → (re)write the lane's renders from the master: `linkedin.md` + `facebook.md` + `instagram.md` + `x.md` for a `content/` idea, or `linkedin.md` + `linkedin-es.md` for a `marketing/` one. Preserve the spine and the author's voice (`rules/VOICE.md` if present), each at its Length Target. Compose the ES render in Spanish from the master — never translate the English one.

   The user may name a single render ("`/adapt <slug> only for instagram`", "`just the Spanish`") — then rebuild only that one.

4. **Editor** (per render) → tighten to the platform sweet spot.

5. **Hashtag** (per render) → append per-platform hashtags.

6. **Verify** → `python3 tools/check-renders.py <postdir>`; fix every failure.

7. **Scorer** (per render) → score and loop until SHIP (≥85).

Always read `rules/SHARED.md`, the platform `rules/*.md` files, and `rules/VOICE.md`. For a `marketing/` idea also read `rules/MARKETING.md` and `rules/SPANISH.md`. Follow `agents/PIPELINE.md`.

8. **Update the index.** Refresh this idea's row in its own tree's index — `content/INDEX.md` or `marketing/INDEX.md` — renders, visual, and status (SHIP once all renders scored ≥85).

## When done

Report the folder path, which renders were rewritten, each character count vs its Length Target, and each Scorer verdict.
