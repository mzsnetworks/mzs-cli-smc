# Marketing Lane Rules

Layers on top of `SHARED.md` and `VOICE.md`. Applies **only** to posts in the `marketing/` tree — never to `content/`.

The two lanes differ in one structural way: a `content/` post ends on a question and asks for nothing. A `marketing/` post ends on a CTA and names an MZS service or product. Everything else — fact discipline, the spine, the hook bar — carries over unchanged.

**Upstream source of truth:** the voice, terminology, and glossary below are ported from `mzs-marketing/.claude/skills/mzs-brand/SKILL.md` (a skill inside the `mzs-marketing` repo — *not* the `mzs-brand` repo, which is a UI design-system kit and holds none of this). Product and positioning facts come from `mzs-marketing/.agents/product-marketing.md`. If the voice or positioning needs to change, change it there and re-port; do not fork it here.

---

## Track shape

- **Platform:** LinkedIn only — Luis Mazariegos' **personal profile**. No company page, no Facebook, no Instagram, no X.
- **Languages:** every idea ships EN and ES. Two posts, same day, same profile.
- **Renders per idea:** `master.md` · `linkedin.md` · `linkedin-es.md`. That is the complete set.
- **Cadence:** Mondays. ES at 2:00 PM EDT (`18:00:00Z`), EN at 4:00 PM EDT (`20:00:00Z`).

Because the posts run from a personal profile, they are written in the **first person** — "what 19 years of running production networks taught me," not "MZS Networks has 19 years of experience." The company is named as the thing the author builds, not as the speaker.

---

## Voice

Inherits `VOICE.md` (Luis's profile) and adds:

- **Practitioner, not vendor.** Written by an engineer who runs production. Show, don't hype.
- **Technically precise.** Name the actual tools — Python, Ansible, Terraform, APIs. Never "cutting-edge solutions."
- **Safety-conscious.** Automation is framed as tested, reviewed, approved, tracked, rollback-able. Address the "is automation safe?" fear directly rather than around it.
- **Right-sized.** One bottleneck or a full framework — no engagement is too small to mention. This is the positioning against big SI firms.
- **Calm confidence.** No exclamation marks in body copy. No superlatives without proof.

| Don't | Do |
|-------|-----|
| "Revolutionary AI-powered networking solutions!" | "Configuration changes tested, reviewed, and rolled back automatically." |
| "We leverage synergies across your stack" | "We connect your monitoring, ticketing, and network platforms through their APIs" |
| "Industry-leading experts" | "Engineers who run production networks" |
| "Contact us" | "Book a consultation" / "Talk to an engineer" |

## Terminology

- **Products are proper nouns and take no article.** "Driftguard detects configuration drift" — never "the Driftguard."
- The four products, and there are no others: **Driftguard** (configuration drift detection) · **Config Modeling** (network configuration modeling) · **ITOC Dashboard** (IT Operations Center visibility) · **Workflow Engine** (automation workflow orchestration). Never invent a fifth.
- Preferred terms: "network automation" (never "network AI"), "Infrastructure as Code" / "IaC", "configuration drift", "orchestration", "multi-site deployments".
- Company name: **MZS Networks** on first mention, **MZS** after. Never "MZS Networks LLC" in copy.
- Location in copy is **Miami** — the term buyers use. "Coral Gables" belongs only in a formal address.
- **No SaaS framing, ever.** Never free trial, signup, self-serve, PLG, MRR, per-seat. The business is consulting engagements and product licensing: consultation, engagement, retainer, demo, licensing.

## The CTA

Every marketing post ends on one. Two approved forms, and only these:

- **"Book a consultation: mzsnetworks.com"**
- **"Talk to an engineer: mzsnetworks.com"**

Never "Contact us", "Get started free", "Sign up", "Try it now", "DM me", or "link in bio". The URL is plain `mzsnetworks.com` in post copy.

The CTA replaces the closing question that `content/` posts use. Keep the landing line — the compressed principle — and put the CTA *after* it, on its own line. The landing still has to earn its place; a CTA is not a substitute for a memorable close.

Ask-to-value ratio is roughly 1:6 against the daily `content/` stream. Do not add a second ask inside the body.

---

## Fact discipline — the one narrow exception

`SHARED.md`'s rule stands: **every statistic stated as fact must trace to a real, citable source.** The marketing lane adds exactly one carve-out, ported from upstream doctrine.

**An uncited number is allowed only when the copy frames it as the reader's hypothetical scenario, never as something MZS measured or observed.**

| Allowed | Blocked |
|---|---|
| "a template update that reached 38 of 40 sites" | "we found drift at 38 of 40 client sites" |
| "imagine 30 branches and one engineer" | "our clients average 30 branches" |
| "a full engineering week every month, gone to manual diffing" | "we save clients a full engineering week every month" |

The test: **could a reader take this number as evidence about MZS?** If yes, it needs a source or it gets cut. If it plainly describes a situation the reader recognizes, it is rhetorical illustration and passes.

Two hard edges that survive the exception:

- **Credentials are claims.** "19 years of running production networks" is verified and is *Luis's own* — MZS Networks' Florida LLC dates to 2022. It must be attributed to the author, never to the company. This is a large part of why the lane posts from a personal profile.
- **Proof points are claims.** Case study results, client outcomes, and savings figures need a real engagement behind them, anonymized by default. Unit economics are unknown upstream and must not be invented — flag the gap instead.

Factcheck applies this table to `marketing/` posts and the unmodified `SHARED.md` rule to `content/` posts.

---

## Content pillars

From `mzs-marketing/work/strategy/marketing-plan/final_plan.md` — the four-part spine, rotated:

1. **Drift and audit stories** — what goes wrong across multi-site networks, and why.
2. **Safety practice** — how a change gets tested, reviewed, approved, tracked, rolled back. The differentiating vocabulary.
3. **Short technical teardowns** — a real Ansible/Terraform/Python pattern, named tools, no vendor pitch.
4. **Anonymized proof** — real engagement outcomes, gated on a finished case study.

Ideation for this lane crosses these four with funnel stage, not the personal pillars in `VOICE.md`.

---

## Length and format

Standard `LINKEDIN.md` rules apply — 1,300–2,000 chars, hook above the ~210-char fold, short paragraphs, near-zero emoji, 2–3 PascalCase hashtags at the end.

Two differences:

- **Sources block is conditional.** `content/` posts always carry one. A marketing post carries one only when it cites a real sourced statistic. A post whose only numbers are hypothetical-reader illustrations has nothing to source, and an empty "Sources" heading reads as a broken template.
- The CTA line sits last, after the hashtags would otherwise go. Order: body → landing → CTA → hashtags.

For the Spanish render, see `rules/SPANISH.md` — its length targets differ, because Spanish runs longer than English.
