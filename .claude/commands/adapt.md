---
description: Re-render an existing fact-checked master into LinkedIn, Instagram, and X (skips drafting)
argument-hint: <slug or path of an existing idea folder>
---

Re-render an **existing** idea whose `master.md` is already written and fact-checked. Use this when the master changed, a platform render needs rebuilding, or the renders are missing.

Target idea: **$ARGUMENTS**

## Steps

1. **Locate the folder.** Resolve `$ARGUMENTS` to `content/<year>/<YYYY-MM-DD>-<slug>/`. If only a slug was given, find the matching folder under `content/`. Confirm `master.md` exists — if not, stop and tell the user to run `/post` instead.

2. **Confirm the master is clean.** Apply the FACTCHECK agent to `master.md`. If FAIL, stop and report — do not adapt an unverified master.

3. **Platform Adapter** → (re)write `linkedin.md`, `instagram.md`, `x.md` from the master, preserving the spine and the author's voice (`rules/VOICE.md` if present), each at its platform Length Target.

4. **Editor** (per render) → tighten to the platform sweet spot.

5. **Hashtag** (per render) → append per-platform hashtags.

6. **Scorer** (per render) → score and loop until SHIP (≥85).

Always read `rules/SHARED.md`, the platform `rules/*.md` files, and `rules/VOICE.md`. Follow `agents/PIPELINE.md`.

7. **Update the index.** Refresh this idea's row in `content/INDEX.md` — renders, visual, and status (SHIP once all renders scored ≥85).

## When done

Report the folder path, which renders were rewritten, each character count vs its Length Target, and each Scorer verdict.
