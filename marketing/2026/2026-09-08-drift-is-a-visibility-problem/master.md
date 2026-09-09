# Master — drift-is-a-visibility-problem

**Preset:** Marketing (LinkedIn + Instagram) — post from Luis's profile, not the company page; the posts speak in the first person about his own experience
**Date:** 2026-09-08
**Source:** `mzs-marketing` → `work/social/2026-07-08-network-automation-services-linkedin.md`, "Post 3 — Config drift (the "nobody knows what's deployed" post)"
**Drafted:** 2026-07-08. Copied into this repo 2026-09-08; the folder date is the transfer date, not a publish date.
**Thesis:** For most multi-site teams the honest answer is no. Drift is not a discipline problem, it is a visibility problem — which is what Driftguard exists to solve.
**Pillar:** Driftguard product pull-through
**Stats:** the "19 years" is Luis's own experience running production networks, confirmed 2026-09-09 — it is a personal credential, not company tenure (MZS's Florida LLC dates to 2022), so the post says "taught me" and is written to be published from Luis's profile rather than the company page. Other figures ("30 sites", "38 of 40 sites", "a full engineering week") describe a hypothetical reader, not MZS, and are illustrative by design.
**Language:** EN master with a hand-written ES render (`linkedin-es.md`) using the `mzs-brand` glossary — usted register, product names untranslated. ES is a primary selling language, not a translation layer, so re-render it by hand rather than machine-translating the EN.

---

Quick test for multi-site network teams:

Can you say, with confidence, what's actually configured on every device across every site — right now?

Not what the standards doc says. Not what the change tickets say. What's really there.

For most teams the honest answer is no. Configs drift:
— an emergency fix at 3 AM that never got documented
— a site engineer's "temporary" workaround, now two years old
— a template update that reached 38 of 40 sites

Then the audit lands, and compliance validation becomes weeks of manual diffing.

This is why we built Driftguard — continuous detection of configuration drift across sites, so the answer to "what's deployed?" is a dashboard, not an archaeology project.

Drift is not a discipline problem. It's a visibility problem. Fix the visibility.

Book a consultation: mzsnetworks.com
