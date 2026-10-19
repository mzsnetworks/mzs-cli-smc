# Marketing Content Index

Company marketing posts. Distinct from `content/INDEX.md`: those are personal thought-leadership pieces that end on a question, these are brand posts that end on a CTA and name MZS services or products. The **slug** is how you reference one ("/adapt `automation-isnt-the-risk`").

Batch 2 (all twelve `2026-09-20` rows) carries **no metrics, no client results and no case studies** — deliberately, since nothing is documented to cite yet. The illustrative-figure exception below is therefore not invoked by any of them.

Sourced from the `mzs-marketing` repo, which owns the brand voice, the ES glossary, and the strategy these posts serve — specifically `.claude/skills/mzs-brand/SKILL.md` (voice + EN→ES glossary), `.agents/product-marketing.md` (products, positioning, CTA conventions), and `work/strategy/marketing-plan/final_plan.md` (the four-part content spine). Note that "mzs-brand" there is a *skill inside `mzs-marketing`*, not the `mzs-brand` repo — that repo is a UI design-system kit and holds no voice or Spanish content.

Those upstream rules are ported into `rules/MARKETING.md` and `rules/SPANISH.md`, which is what the agents in this repo actually read. Edit the copy here; if the voice or positioning itself needs to change, change it upstream and re-port.

**Track:** Marketing preset — LinkedIn only, Luis's **personal profile**, twice per idea: Spanish at 2:00 PM local and English at 4:00 PM local, on **Mondays** — `18:00Z`/`20:00Z` on EDT, `19:00Z`/`21:00Z` on EST. No company page, no Facebook, no Instagram, no X.

Ordered by **scheduled publish date**, newest first. The `Date` column is the *transfer* date (see "On dates" below), so it does not sort with the table.

| Date | Slug | Title / Thesis | Renders | Visual | Status |
|------|------|----------------|---------|--------|--------|
| 2026-10-18 | `one-change-two-teams` | A route and a security group are now the same path, owned by two teams with two change processes and two tools. The outage happens at the boundary, and the fix is one reviewed change across both rather than better coordination between them. | LI · LI-ES | — | **SHIP** · planned Mon Mar 29 2027 |
| 2026-10-18 | `boring-on-purpose` | Choosing Python and Ansible over something more elegant is a decision about who can maintain the work after the engagement ends. Ordinary tools are a hiring pool, a readable artifact, and an exit that does not depend on us. | LI · LI-ES | — | **SHIP** · planned Mon Mar 22 2027 |
| 2026-10-18 | `api-first-is-not-a-feature` | Every platform claims an API; what matters for automation is whether it writes as well as reads, handles bulk operations, returns usable errors, and survives its own rate limits at your estate's size. Those are evaluation criteria, not assumptions. | LI · LI-ES | — | **SHIP** · planned Mon Mar 15 2027 |
| 2026-10-18 | `assembled-by-hand-every-time` | The recurring reporting ask — audit, insurer, board, renewal — gets answered by an engineer assembling the same spreadsheet from the same four systems, every time. The work is not the question, it is that the answer was never made queryable. | LI · LI-ES | — | **SHIP** · planned Mon Mar 8 2027 |
| 2026-10-18 | `when-you-cannot-test-it` | Some changes genuinely cannot be lab-tested — scale effects, vendor-specific behavior, one-of-a-kind hardware. The answer is not to skip testing but to replace it with staged exposure, measured observation and a rehearsed revert, and to say out loud which category a change is in. | LI · LI-ES | — | **SHIP** · planned Mon Mar 1 2027 |
| 2026-10-18 | `blast-radius-before-the-window` | What else does this touch" is the question a change review cannot answer from a diff, because the diff shows the device and the risk lives in the topology. Modeling the change against the intended network answers it in the review rather than at 2 AM. | LI · LI-ES | — | **SHIP** · planned Mon Feb 22 2027 |
| 2026-10-18 | `naming-is-an-interface` | Inconsistent hostnames, interface descriptions and site codes are not a tidiness problem; they are the reason every automation needs special cases, and they set a ceiling on what can be automated at all. | LI · LI-ES | — | **SHIP** · planned Mon Feb 15 2027 |
| 2026-10-18 | `your-side-of-the-engagement` | Automation projects stall on the buyer's side more often than the vendor's — access, decisions and review time are real hours nobody budgets. Naming them before the proposal is what makes the timeline honest. | LI · LI-ES | — | **SHIP** · planned Mon Feb 8 2027 |
| 2026-10-18 | `what-happens-at-step-four` | A script that dies halfway leaves the estate in a state nobody designed, and the difference between a script and an orchestrated workflow is entirely about what happens on partial failure — retries, idempotence, recorded state, and a named person who is told. | LI · LI-ES | — | **SHIP** · planned Mon Feb 1 2027 |
| 2026-10-18 | `a-dry-run-is-not-a-test` | A dry run proves the change is syntactically valid and will be accepted; it says nothing about whether the service survives. The four stages — dry run, model, lab or canary, production with a rehearsed revert — answer different questions, and skipping to the end is how an approved change becomes an outage. | LI · LI-ES | — | **SHIP** · planned Mon Jan 25 2027 |
| 2026-10-18 | `drift-is-a-rate-not-a-snapshot` | Remediating drift is a project; staying remediated is a property of the system. What matters is the rate at which variation is reintroduced and what causes it, which a one-time cleanup never measures. | LI · LI-ES | — | **SHIP** · planned Mon Jan 18 2027 |
| 2026-10-18 | `the-automation-you-inherited` | Most automation engagements start from something somebody already built and nobody trusts, not from a blank page. The first work is deciding what to keep, and inherited automation usually encodes correct decisions whose reasons were never written down. | LI · LI-ES | — | **SHIP** · planned Mon Jan 11 2027 |
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

**Runway.** Batches 1 and 2 are live in Blotato — every Monday **Sep 14 through Dec 14**, 14 posts, 28 submissions, all with art. **Batch 3 transferred 2026-10-18**: 12 posts for Mondays **Jan 11 – Mar 29, 2027**, written but not yet arted or scheduled.

`we-hand-it-back` is the only unscheduled post. It was deliberately **held back from Dec 21** (decided 2026-09-20): a handover post landing in Christmas week draws the year's worst engagement, and holding it puts one written post into January rather than starting 2027 empty. Its hero is generated and both renders are SHIP — it needs only a date. **Dec 21 and Dec 28 are dark.**

**The lane now runs to Mar 29, 2027.** Batch 3 lives in `mzs-marketing` at `work/social/2026-10-18-marketing-batch-3/` and is the source of record for its copy. Each post needs a hero and a `/publish` run; nothing is scheduled yet.

**Daylight time begins Sun Mar 14, 2027.** Jan 11 – Mar 8 publish at `19:00Z` / `21:00Z`; Mar 15, 22 and 29 at `18:00Z` / `20:00Z`. Each master records its own offset — derive it from the date rather than copying one forward, which is what put fourteen live schedules an hour early in October 2026.

**Batch 3 was written to the length rules rather than fixed on transfer.** All twelve land EN 1,679–1,738, ES 1,944–1,999, ratio 1.15–1.21, with paragraph and sentence parity intact — `tools/check-renders.py` reports zero failures and zero warnings across the set. Batch 2 arrived under ratio on all twelve and broke parity on four. `mzs-marketing/tools/check-batch.py` checks all four properties at the source now.

**Pillar gap.** The four-part spine is drift/audit, safety practice, technical teardowns, and *anonymized proof*. No post in either batch uses the fourth — it is blocked until a real case study exists. When one does, proof-led posts become the strongest available in this lane.

---

**Legend**
- **Renders:** LI = `linkedin.md`, LI-ES = `linkedin-es.md`. These two are the complete set for this lane — an idea is not adapted until both exist.
- **Visual:** `carousel` / `infographic` / `hero` produced in the folder, or `—` if none. The EN post may take a carousel or a hero; the **ES post takes a text-free hero only**, since carousels render typographically in English (`rules/SPANISH.md`). In practice both languages share one 16:9 hero, which carries no type. No 4:5 variant — this lane has no Instagram target.
- **Status:** DRAFT (master only, or renders not yet scored) · ADAPTED (renders written) · SHIP (all renders scored ≥85) · PUBLISHED (scheduled or live via `/publish`; submission IDs and times in the folder's `published.md`)

Path layout: `marketing/<year>/<month>/<YYYY-MM-DD>-<slug>/`

**On dates.** For posts originating in `mzs-marketing`, the folder date is the date the post was *transferred* here, not when it was drafted or when it will publish. The master's `Drafted:` line carries the original date; `/publish` records the real schedule in `published.md`.

**On Spanish.** ES is a primary selling market for MZS, not a translation layer. `linkedin-es.md` is written against the EN→ES glossary in **`rules/SPANISH.md`** — usted register, neutral Latin-American Spanish, product and tool names left in English (Driftguard, Config Modeling, ITOC Dashboard, Workflow Engine) — and carries its own Spanish hashtags. Compose it from the master; never machine-translate the EN.

Two measures worth checking on any new ES render. It should land at **~1,500–2,300 characters**, and its ratio to the English render should sit around **1.15–1.25** — Spanish runs longer for the same content, so a ratio near 1.00 means the Spanish is tracking the English sentence-for-sentence rather than breathing. Every one of the twelve batch-2 renders arrived below that ratio and was expanded on transfer.

**Check paragraph parity too.** The two renders must carry the same beats — same hook, same argument, same landing, same CTA position. Expanding one language without mirroring the other breaks this, which happened on four posts during the 2026-09-20 transfer and had to be corrected twice, once before submission and once in a live Blotato schedule. Compare paragraph counts before publishing; they should match exactly. The ~210-character fold does **not** scale, which makes the Spanish hook the tightest constraint in the system.

**On figures.** The marketing lane carries one narrow exception to this repo's fact discipline, adopted 2026-09-09 from upstream doctrine: an uncited number passes when the copy frames it as the *reader's* hypothetical scenario ("a template update that reached 38 of 40 sites"), and fails when it reads as something MZS measured ("we found drift at 38 of 40 client sites"). Credentials and proof points are not covered — the "19 years" is Luis's own, verified, and must never be attributed to the company, whose Florida LLC dates to 2022. Full table in `rules/MARKETING.md`; enforced by `agents/FACTCHECK.md`.
