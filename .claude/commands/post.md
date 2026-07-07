---
description: Take one idea through the full pipeline to four publish-ready posts (LinkedIn, Facebook, Instagram, X)
argument-hint: <topic, one-liner, or pasted notes>
---

Run the **full core editorial pipeline** for this idea, end to end:

> $ARGUMENTS

Follow `agents/PIPELINE.md` exactly. Apply each agent's rules from its file in `agents/`. Always read `rules/SHARED.md`, the relevant `rules/*.md` platform file(s), and `rules/VOICE.md` (if it exists — apply the author's voice).

## Steps

1. **Set up the idea folder.** Pick today's date and a short kebab-case `<slug>` from the idea's thesis or landing. Create `content/<year>/<YYYY-MM-DD>-<slug>/` and seed `master.md` with the topic/notes above.

2. **Writer** → draft `master.md` (LinkedIn-length, author's voice, hook above the fold, spine: hook → POV → cited data → judgment → landing).

3. **Factcheck** → verify every stat against a cited source. Output PASS/FAIL. **If FAIL, loop back to the Writer and fix before going on** — never adapt an unverified master.

4. **Platform Adapter** → write `linkedin.md`, `facebook.md`, `instagram.md`, `x.md` beside the master, preserving the spine and voice, each at its platform Length Target.

5. **Editor** (per render) → tighten to the platform sweet spot, keep hook/CTA/landing.

6. **Hashtag** (per render) → append per-platform hashtags.

7. **Scorer** (per render) → score 0–100. **Loop back to Editor/Writer until every render is SHIP (≥85).**

8. **Update the index.** Add (or update) this idea's row in `content/INDEX.md` — date, slug, title/thesis, which renders exist, visual (— if none yet), and status (SHIP once all renders scored ≥85). Keep it newest-first.

## When done

Report a short summary: the folder path, the five files written, each render's character count vs its Length Target, and each Scorer verdict. Show the LinkedIn render in full. Do not claim SHIP unless the Scorer actually returned ≥85 — show the real scores. Mention that `/publish <slug>` takes it live when ready.

If the user passed no idea (`$ARGUMENTS` is empty), ask them for the topic or notes before starting.
