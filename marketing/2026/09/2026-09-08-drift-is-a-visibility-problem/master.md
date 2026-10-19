# Master — drift-is-a-visibility-problem

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM EDT and EN at 4:00 PM, on a Monday. First person, about his own experience.
**Date:** 2026-09-08
**Source:** `mzs-marketing` → `work/social/2026-07-08-network-automation-services-linkedin.md`, "Post 3 — Config drift (the "nobody knows what's deployed" post)"
**Drafted:** 2026-07-08. Copied into this repo 2026-09-08; the folder date is the transfer date, not a publish date.
**Thesis:** For most multi-site teams the honest answer is no. Drift is not a discipline problem, it is a visibility problem — which is what Driftguard exists to solve.
**Pillar:** Driftguard product pull-through
**Stats:** the "19 years" is Luis's own experience running production networks, confirmed 2026-09-09 — it is a personal credential, not company tenure (MZS's Florida LLC dates to 2022), so the post says "taught me" and is written to be published from Luis's profile rather than the company page. Other figures ("30 sites", "38 of 40 sites", "a full engineering week") describe a hypothetical reader, not MZS, and are illustrative by design.
**Revised:** 2026-09-09 — the transferred draft ran 868 chars against this repo's 1,300–2,000 LinkedIn target and asserted the discipline-vs-visibility reframe without explaining it. Added the mechanism (every drift event was individually rational; process with no read-back can't report its own failure), which is also the author's signature move. EN 868 → 1,562; ES 1,069 → 1,868.

**Language:** EN master with a hand-written ES render (`linkedin-es.md`) using the EN→ES glossary in `rules/SPANISH.md` (ported from the `mzs-brand` skill inside `mzs-marketing`, not the `mzs-brand` repo) — usted register, product names untranslated. ES is a primary selling language, not a translation layer, so re-render it by hand rather than machine-translating the EN.

---

Quick test for multi-site network teams:

Can you say, with confidence, what's actually configured on every device across every site — right now?

Not what the standards doc says. Not what the change tickets say. What's really there.

For most teams the honest answer is no. Configs drift:
— an emergency fix at 3 AM that never got documented
— a site engineer's "temporary" workaround, now two years old
— a template update that reached 38 of 40 sites

Here's the part that usually gets misdiagnosed. Every one of those was a reasonable call by a competent engineer. The 3 AM fix restored service. The workaround unblocked a project that was already late. The template push hit two devices that were unreachable that night, Ansible logged the failures, and the run moved on.

Nobody was careless. Drift is not what happens when people stop following the process. It's what happens when the process has no way to tell you it didn't finish.

Which is why more discipline doesn't fix it. Stricter change control and longer checklists govern what you intend to deploy. None of it reads the running config back and tells you what is actually there.

Then the audit lands, and compliance validation becomes weeks of manual diffing.

This is why we built Driftguard — continuous detection of configuration drift across sites, so the answer to "what's deployed?" is a dashboard, not an archaeology project.

Drift is not a discipline problem. It's a visibility problem. Fix the visibility.

Book a consultation: mzsnetworks.com
