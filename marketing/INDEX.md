# Marketing Content Index

Company marketing posts. Distinct from `content/INDEX.md`: those are personal thought-leadership pieces that end on a question, these are brand posts that end on a CTA and name MZS services or products. The **slug** is how you reference one ("/adapt `automation-isnt-the-risk`").

Batch 2 (all twelve `2026-09-20` rows) carries **no metrics, no client results and no case studies** — deliberately, since nothing is documented to cite yet. The illustrative-figure exception below is therefore not invoked by any of them.

Sourced from the `mzs-marketing` repo, which owns the brand voice, the ES glossary, and the strategy these posts serve — specifically `.claude/skills/mzs-brand/SKILL.md` (voice + EN→ES glossary), `.agents/product-marketing.md` (products, positioning, CTA conventions), and `work/strategy/marketing-plan/final_plan.md` (the four-part content spine). Note that "mzs-brand" there is a *skill inside `mzs-marketing`*, not the `mzs-brand` repo — that repo is a UI design-system kit and holds no voice or Spanish content.

Those upstream rules are ported into `rules/MARKETING.md` and `rules/SPANISH.md`, which is what the agents in this repo actually read. Edit the copy here; if the voice or positioning itself needs to change, change it upstream and re-port.

**Track:** Marketing preset — LinkedIn only, Luis's **personal profile**, twice per idea: Spanish at 2:00 PM EDT (`18:00:00Z`) and English at 4:00 PM EDT (`20:00:00Z`), on **Mondays**. No company page, no Facebook, no Instagram, no X.

Ordered by **scheduled publish date**, newest first. The `Date` column is the *transfer* date (see "On dates" below), so it does not sort with the table.

| Date | Slug | Title / Thesis | Renders | Visual | Status |
|------|------|----------------|---------|--------|--------|
| 2026-09-20 | `we-hand-it-back` | The quiet objection isn't "will it work", it's "will we be able to touch it afterwards" — handover as a design constraint | LI · LI-ES | hero | **SHIP** · held for Jan 2027 |
| 2026-09-20 | `three-countries-one-standard` | Multi-country networks fragment across a language boundary and a supplier boundary before they fragment technically | LI · LI-ES | hero | **PUBLISHED** · Mon Dec 14 |
| 2026-09-20 | `one-vendor-isnt-automation` | Vendor-native automation works beautifully until the second vendor arrives, which it always does | LI · LI-ES | hero | **PUBLISHED** · Mon Dec 7 |
| 2026-09-20 | `buying-automation-without-a-team` | Most automation advice assumes you already employ automation engineers — the honest version for a team that doesn't | LI · LI-ES | hero | **PUBLISHED** · Mon Nov 30 |
| 2026-09-20 | `noc-sees-alerts-not-state` | Ask your NOC a question that isn't an alert and watch what happens — events describe what broke, not what is · ITOC Dashboard | LI · LI-ES | hero | **PUBLISHED** · Mon Nov 23 |
| 2026-09-20 | `tools-that-dont-talk` | Every system a routine change touches has an API and almost none are connected — the glue is currently a person · Workflow Engine | LI · LI-ES | hero | **PUBLISHED** · Mon Nov 16 |
| 2026-09-20 | `rollback-is-an-acceptance-criterion` | Most change records have a rollback plan; far fewer have a rollback anyone has run — treat it as an acceptance criterion | LI · LI-ES | hero | **PUBLISHED** · Mon Nov 9 |
| 2026-09-20 | `assessment-what-it-finds` | An assessment is not a sales call with a report attached — what two weeks of actually looking turns up, and why the findings are always ordinary | LI · LI-ES | hero | **PUBLISHED** · Mon Nov 2 |
| 2026-09-20 | `evidence-not-assurances` | Auditors don't ask whether you have a standard, they ask you to prove what was deployed on a date — Driftguard | LI · LI-ES | hero | **PUBLISHED** · Mon Oct 26 |
| 2026-09-20 | `test-before-it-touches-a-device` | Networking is the last place where the test plan is "apply it in production and watch" — Config Modeling | LI · LI-ES | hero | **PUBLISHED** · Mon Oct 19 |
| 2026-09-20 | `cant-hire-your-way-out` | Manual change scales linearly and headcount doesn't — the hiring plan is usually a deferred automation decision | LI · LI-ES | hero | **PUBLISHED** · Mon Oct 12 |
| 2026-09-20 | `first-thirty-days` | The objection isn't price, it's "we tried this before" — so here's the concrete shape of a first month | LI · LI-ES | hero | **PUBLISHED** · Mon Oct 5 |
| 2026-09-08 | `drift-is-a-visibility-problem` | Can you say what's actually configured across every site right now? Drift isn't a discipline problem, it's a visibility problem | LI · LI-ES | hero | **PUBLISHED** · Mon Sep 28 |
| 2026-09-08 | `one-bottleneck-not-a-framework` | You probably don't need a network automation framework — automate one repetitive process and let the quick win pay for the roadmap conversation | LI · LI-ES | hero | **PUBLISHED** · Mon Sep 21 |
| 2026-09-08 | `automation-isnt-the-risk` | Automation isn't the risk, unreviewed change is — manual change only feels safer because a human is watching | LI · LI-ES | hero | **PUBLISHED** · Mon Sep 14 |

**Runway.** Both batches are transferred and every Monday from **Sep 14 through Dec 14** is live in Blotato — 14 posts, 28 submissions, all with art.

`we-hand-it-back` is the only unscheduled post. It was deliberately **held back from Dec 21** (decided 2026-09-20): a handover post landing in Christmas week draws the year's worst engagement, and holding it puts one written post into January rather than starting 2027 empty. Its hero is generated and both renders are SHIP — it needs only a date. **Dec 21 and Dec 28 are dark.**

**After that the lane is empty.** There is no batch 3. Writing one upstream in `mzs-marketing` is the next real work here, and it needs to happen before January 2027.

**Pillar gap.** The four-part spine is drift/audit, safety practice, technical teardowns, and *anonymized proof*. No post in either batch uses the fourth — it is blocked until a real case study exists. When one does, proof-led posts become the strongest available in this lane.

---

**Legend**
- **Renders:** LI = `linkedin.md`, LI-ES = `linkedin-es.md`. These two are the complete set for this lane — an idea is not adapted until both exist.
- **Visual:** `carousel` / `infographic` / `hero` produced in the folder, or `—` if none. The EN post may take a carousel or a hero; the **ES post takes a text-free hero only**, since carousels render typographically in English (`rules/SPANISH.md`). In practice both languages share one 16:9 hero, which carries no type. No 4:5 variant — this lane has no Instagram target.
- **Status:** DRAFT (master only, or renders not yet scored) · ADAPTED (renders written) · SHIP (all renders scored ≥85) · PUBLISHED (scheduled or live via `/publish`; submission IDs and times in the folder's `published.md`)

Path layout: `marketing/<year>/<YYYY-MM-DD>-<slug>/`

**On dates.** For posts originating in `mzs-marketing`, the folder date is the date the post was *transferred* here, not when it was drafted or when it will publish. The master's `Drafted:` line carries the original date; `/publish` records the real schedule in `published.md`.

**On Spanish.** ES is a primary selling market for MZS, not a translation layer. `linkedin-es.md` is written against the EN→ES glossary in **`rules/SPANISH.md`** — usted register, neutral Latin-American Spanish, product and tool names left in English (Driftguard, Config Modeling, ITOC Dashboard, Workflow Engine) — and carries its own Spanish hashtags. Compose it from the master; never machine-translate the EN.

Two measures worth checking on any new ES render. It should land at **~1,500–2,300 characters**, and its ratio to the English render should sit around **1.15–1.25** — Spanish runs longer for the same content, so a ratio near 1.00 means the Spanish is tracking the English sentence-for-sentence rather than breathing. Every one of the twelve batch-2 renders arrived below that ratio and was expanded on transfer.

**Check paragraph parity too.** The two renders must carry the same beats — same hook, same argument, same landing, same CTA position. Expanding one language without mirroring the other breaks this, which happened on four posts during the 2026-09-20 transfer and had to be corrected twice, once before submission and once in a live Blotato schedule. Compare paragraph counts before publishing; they should match exactly. The ~210-character fold does **not** scale, which makes the Spanish hook the tightest constraint in the system.

**On figures.** The marketing lane carries one narrow exception to this repo's fact discipline, adopted 2026-09-09 from upstream doctrine: an uncited number passes when the copy frames it as the *reader's* hypothetical scenario ("a template update that reached 38 of 40 sites"), and fails when it reads as something MZS measured ("we found drift at 38 of 40 client sites"). Credentials and proof points are not covered — the "19 years" is Luis's own, verified, and must never be attributed to the company, whose Florida LLC dates to 2022. Full table in `rules/MARKETING.md`; enforced by `agents/FACTCHECK.md`.
