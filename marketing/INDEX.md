# Marketing Content Index

Company marketing posts, newest first. Distinct from `content/INDEX.md`: those are personal thought-leadership pieces that end on a question, these are brand posts that end on a CTA and name MZS services or products. The **slug** is how you reference one ("/adapt `automation-isnt-the-risk`").

Sourced from the `mzs-marketing` repo, which owns the brand voice, the ES glossary, and the strategy these posts serve — specifically `.claude/skills/mzs-brand/SKILL.md` (voice + EN→ES glossary), `.agents/product-marketing.md` (products, positioning, CTA conventions), and `work/strategy/marketing-plan/final_plan.md` (the four-part content spine). Note that "mzs-brand" there is a *skill inside `mzs-marketing`*, not the `mzs-brand` repo — that repo is a UI design-system kit and holds no voice or Spanish content.

Those upstream rules are ported into `rules/MARKETING.md` and `rules/SPANISH.md`, which is what the agents in this repo actually read. Edit the copy here; if the voice or positioning itself needs to change, change it upstream and re-port.

**Track:** Marketing preset — LinkedIn only, Luis's **personal profile**, twice per idea: Spanish at 2:00 PM EDT (`18:00:00Z`) and English at 4:00 PM EDT (`20:00:00Z`), on **Mondays**. No company page, no Facebook, no Instagram, no X.

| Date | Slug | Title / Thesis | Renders | Visual | Status |
|------|------|----------------|---------|--------|--------|
| 2026-09-08 | `automation-isnt-the-risk` | Automation isn't the risk, unreviewed change is — manual change only feels safer because a human is watching | LI · LI-ES | — | DRAFT |
| 2026-09-08 | `one-bottleneck-not-a-framework` | You probably don't need a network automation framework — automate one repetitive process and let the quick win pay for the roadmap conversation | LI · LI-ES | — | DRAFT |
| 2026-09-08 | `drift-is-a-visibility-problem` | Can you say what's actually configured across every site right now? Drift isn't a discipline problem, it's a visibility problem | LI · LI-ES | — | DRAFT |

---

**Legend**
- **Renders:** LI = `linkedin.md`, LI-ES = `linkedin-es.md`. These two are the complete set for this lane — an idea is not adapted until both exist.
- **Visual:** `carousel` / `infographic` / `hero` / `reel` produced in the folder, or `—` if none
- **Status:** DRAFT (master only, or renders not yet scored) · ADAPTED (renders written) · SHIP (all renders scored ≥85) · PUBLISHED (posted live via `/publish`; details in the folder's `published.md`)

- **Visual:** the EN post may take a carousel or a hero; the **ES post takes a text-free hero only** — carousels render typographically in English (`rules/SPANISH.md`).

Path layout: `marketing/<year>/<YYYY-MM-DD>-<slug>/`

**On dates.** For posts originating in `mzs-marketing`, the folder date is the date the post was *transferred* here, not when it was drafted or when it will publish. The master's `Drafted:` line carries the original date; `/publish` records the real schedule in `published.md`.

**On Spanish.** ES is a primary selling market for MZS, not a translation layer. `linkedin-es.md` is hand-written against the `mzs-brand` glossary — usted register, product names left in English (Driftguard, Config Modeling, ITOC Dashboard, Workflow Engine) — and carries its own Spanish hashtags. Re-render it by hand; do not machine-translate the EN.

**On figures.** The marketing lane carries one narrow exception to this repo's fact discipline, adopted 2026-09-09 from upstream doctrine: an uncited number passes when the copy frames it as the *reader's* hypothetical scenario ("a template update that reached 38 of 40 sites"), and fails when it reads as something MZS measured ("we found drift at 38 of 40 client sites"). Credentials and proof points are not covered — the "19 years" is Luis's own, verified, and must never be attributed to the company, whose Florida LLC dates to 2022. Full table in `rules/MARKETING.md`; enforced by `agents/FACTCHECK.md`.
