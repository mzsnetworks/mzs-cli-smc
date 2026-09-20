# Spanish (ES) Render Rules

Applies to any `*-es.md` render. Today that is `marketing/<year>/<date>-<slug>/linkedin-es.md`; the rules generalize if a Spanish render is ever added elsewhere.

Layers on `SHARED.md`, `LINKEDIN.md`, and `MARKETING.md`. Where a length or phrasing rule in those files assumes English, this file overrides it.

**Spanish is a primary selling language for MZS, not a translation layer.** The ES render is *written*, not translated. It carries the same argument, the same spine, and the same CTA — in native Spanish, from scratch.

---

## The rule that does not bend

**Never machine-translate the English render.** Not with a translation tool, not by translating line-by-line in your head. Read the master, understand the argument, and write it in Spanish the way a Spanish-speaking network engineer would write it.

The tell for a translated post is idiom that survived word-for-word. "Fix the visibility" becomes "Arregle la visibilidad" — which works — but "the answer is a dashboard, not an archaeology project" needs a Spanish reader to find "un proyecto de arqueología" as natural as an English reader finds the original. Rewrite idioms natively; keep the *effect*, not the words.

## Register

- **usted**, always. This is B2B copy addressed to IT directors and network engineering leaders. Never tú, never vos.
- **Neutral Latin-American Spanish.** LatAm is the market. Avoid Castilian forms (vosotros, "ordenador", peninsular slang) and avoid country-specific idiom that would mark the post as Mexican, Colombian, or Argentine.
- Same voice as the EN lane: practitioner not vendor, calm confidence, no exclamation marks, technically precise.

## Glossary (EN → ES)

Use these mappings. They originate in `mzs-marketing/.claude/skills/mzs-brand/SKILL.md`; this table is what agents in this repo read, and it wins where the two differ (see the note below).

| EN | ES |
|----|-----|
| network automation | automatización de redes |
| Infrastructure as Code (IaC) | infraestructura como código (IaC) |
| configuration drift | desviación de configuración |
| compliance | cumplimiento normativo |
| compliance validation | validación de cumplimiento normativo |
| device provisioning | aprovisionamiento de dispositivos |
| firewall policy updates | actualizaciones de políticas de firewall |
| multi-site deployments | despliegues multi-sitio |
| workflow | flujo de trabajo |
| rollback | reversión (rollback) |
| Book a consultation | Reserve una consulta |
| Talk to an engineer | Hable con un ingeniero |
| engineers who run production | ingenieros que operan producción |

**Corrections made here are local until re-ported upstream.** `compliance → cumplimiento normativo` was corrected by the author on 2026-09-09; `mzs-marketing/.claude/skills/mzs-brand/SKILL.md` still carries the shorter `cumplimiento`. This file wins for anything rendered in this repo.

**When a term is missing from the glossary,** keep the English term and add a short Spanish gloss on first use. Do not coin a translation for an industry term that practitioners say in English.

**Product names stay in English.** Driftguard, Config Modeling, ITOC Dashboard, Workflow Engine — never translated, never glossed. They keep the no-article rule too: "Driftguard detecta…", never "el Driftguard".

Tool names stay in English as well: Python, Ansible, Terraform, API.

## Length targets

`SHARED.md`'s targets are calibrated to English. **Spanish runs roughly 15–25% longer** for the same content — more articles, longer compounds, no noun-stacking. Rendering to the English character count silently cuts an argument.

| | English (`SHARED.md`) | Spanish |
|---|---|---|
| LinkedIn draft target | **1,600–1,850 chars** | **1,700–2,000 chars** |
| Checker fails outside | <1,300 or >1,900 | <1,500 or >2,200 |
| Hard cap | ~3,000 chars | ~3,000 chars (platform limit, unchanged) |
| Fold — hook must land before | ~210 chars | **~210 chars (unchanged)** |

The fold does **not** scale. LinkedIn truncates on characters, not on meaning, so the Spanish hook has ~210 characters exactly like the English one — and Spanish needs more of them to say the same thing. **This is the hardest constraint in the ES render.** Write the Spanish hook first and to the fold; do not write a Spanish sentence and hope it fits.

## Hashtags

2–3, same as the English render, at the very end.

- Spanish tags for Spanish concepts, no accents and no ñ (LinkedIn tags handle them inconsistently): `#AutomatizacionDeRedes`, `#InfraestructuraComoCodigo`, `#IngenieriaDeRedes`, `#CumplimientoNormativo`.
- **Keep the tag in English when the industry says it in English** — `#NetOps`, `#NetDevOps`, `#DevOps`, `#IaC`. A Spanish-speaking network engineer follows `#NetOps`, not a translation of it.
- PascalCase throughout, same as English.

## Structure

Keep the EN structure parallel — same hook shape, same beats, same landing, same CTA position — so the two renders read as one idea in two languages rather than two different posts. The bilingual site depends on this parallelism; so does anyone who follows the profile in both languages.

## Editing an ES render

`EDITOR.md`'s filler list is English (`just`, `really`, `actually`, `basically`, `in order to`). It does not apply. The Spanish equivalents to cut:

- **Empty intensifiers:** *realmente*, *básicamente*, *simplemente*, *de hecho*, *en realidad*
- **Padding constructions:** *con el fin de* / *con el objetivo de* → *para*; *a nivel de* → cut or name the thing; *el hecho de que* → *que*
- **Hedges:** *podría llegar a ser*, *de alguna manera*, *en cierto modo*
- **Corporate filler:** *cabe destacar que*, *es importante mencionar que*, *en el mundo actual*

Spanish tolerates longer sentences than English, so do not chop every sentence to English rhythm — but the short-declarative cadence and the white space before the turn carry over.

## Scoring

Score an ES render against **this file plus `MARKETING.md`**, not against the English reference post. The calibration bar in `LINKEDIN.md` (`content/2026/2026-06-24-ai-makes-us-judges/linkedin.md`) is an English post and does not apply.

The rubric is otherwise unchanged, with one added check inside Platform fit: **does the hook land inside 210 characters, and does the copy read as written-in-Spanish rather than translated?** A render that reads as a translation fails Platform fit regardless of its character count.

## Visuals

**ES posts take a text-free hero image only** — never a carousel or infographic. Those are rendered typographically from `carousel.json` / `infographic.json` in English, and English slides under a Spanish caption is a broken post. Heroes carry no type, so they are language-neutral and the EN post's hero can be reused as-is.

If an idea's EN render uses a carousel, the ES render either reuses that post's hero (when one exists) or ships text-only. Do not render a Spanish carousel; the renderer's `Source:` label and font stack are English-only.
