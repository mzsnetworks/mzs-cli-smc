---
description: Take one idea through the full pipeline to publish-ready posts (content lane: LinkedIn/Facebook/Instagram/X; marketing lane: LinkedIn EN+ES)
argument-hint: <topic, one-liner, or pasted notes> [marketing]
---

Run the **full core editorial pipeline** for this idea, end to end:

> $ARGUMENTS

Follow `agents/PIPELINE.md` exactly. Apply each agent's rules from its file in `agents/`. Always read `rules/SHARED.md`, the relevant `rules/*.md` platform file(s), and `rules/VOICE.md` (if it exists — apply the author's voice).

**Pick the lane first.** If the request says "marketing" (or names an MZS product, or asks for a post with a CTA), this is a `marketing/` post: additionally read `rules/MARKETING.md` and `rules/SPANISH.md`, and render **LinkedIn EN + ES only**. Otherwise it's a `content/` post and renders all four platforms. When it's genuinely ambiguous, ask — the two lanes have different voices and different endings.

## Steps

1. **Set up the idea folder.** Pick today's date and a short kebab-case `<slug>` from the idea's thesis or landing. Create `<tree>/<year>/<YYYY-MM-DD>-<slug>/` — `<tree>` is `content` or `marketing` per the lane — and seed `master.md` with the topic/notes above. A marketing master also records its Preset, Source, Thesis, Pillar, and how any figures are justified (copy the header shape from an existing `marketing/` master).

2. **Writer** → draft `master.md` (LinkedIn-length, author's voice, hook above the fold, spine: hook → POV → cited data → judgment → landing).

3. **Factcheck** → verify every stat against a cited source. Output PASS/FAIL. **If FAIL, loop back to the Writer and fix before going on** — never adapt an unverified master.

4. **Platform Adapter** → beside the master, write the lane's renders: `linkedin.md` + `facebook.md` + `instagram.md` + `x.md` for `content/`, or `linkedin.md` + `linkedin-es.md` for `marketing/`. Preserve the spine and voice, each at its Length Target. **The ES render is composed in Spanish from the master, never translated from the English render.**

5. **Editor** (per render) → tighten to the platform sweet spot, keep hook/CTA/landing.

6. **Hashtag** (per render) → append per-platform hashtags.

7. **Scorer** (per render) → score 0–100. **Loop back to Editor/Writer until every render is SHIP (≥85).**

8. **Update the index.** Add (or update) this idea's row in the lane's index — `content/INDEX.md` or `marketing/INDEX.md` — date, slug, title/thesis, which renders exist, visual (— if none yet), and status (SHIP once all renders scored ≥85). Keep it newest-first.

## When done

Report a short summary: the folder path, the files written, each render's character count vs its Length Target, and each Scorer verdict. Show the LinkedIn render in full — both languages for a marketing post. Do not claim SHIP unless the Scorer actually returned ≥85 — show the real scores. Mention that `/publish <slug>` takes it live when ready.

If the user passed no idea (`$ARGUMENTS` is empty), ask them for the topic or notes before starting.
