# Master — automation-isnt-the-risk

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM EDT and EN at 4:00 PM, on a Monday. First person, about his own experience.
**Date:** 2026-09-08
**Source:** `mzs-marketing` → `work/social/2026-07-08-network-automation-services-linkedin.md`, "Post 1 — The fear hook ("is automation safe?")"
**Drafted:** 2026-07-08. Copied into this repo 2026-09-08; the folder date is the transfer date, not a publish date.
**Thesis:** Manual change feels safer because a human is watching. The human watching at 2 AM on change window #47 is the risk. Automation done right is tested, peer-reviewed, tracked, and rollback-able.
**Pillar:** Trust / safety — objection handling
**Stats:** the "19 years" is Luis's own experience running production networks, confirmed 2026-09-09 — it is a personal credential, not company tenure (MZS's Florida LLC dates to 2022), so the post says "taught me" and is written to be published from Luis's profile rather than the company page. Other figures ("30 sites", "38 of 40 sites", "a full engineering week") describe a hypothetical reader, not MZS, and are illustrative by design.
**Revised:** 2026-09-09 — transferred draft ran short of this repo's LinkedIn target and stated its claim without the mechanism behind it. Added the reasoning; lengths now in range.

**Language:** EN master with a hand-written ES render (`linkedin-es.md`) using the EN→ES glossary in `rules/SPANISH.md` (ported from the `mzs-brand` skill inside `mzs-marketing`, not the `mzs-brand` repo) — usted register, product names untranslated. ES is a primary selling language, not a translation layer, so re-render it by hand rather than machine-translating the EN.

---

"What if the script breaks production?"

That's the first question every network team asks us. It's the right question.

Manual changes feel safer because a human is watching. But here's what 19 years of running production networks taught me: the human watching at 2 AM on change window #47 is the risk.

Not because they're careless. Because a manual change leaves nothing behind to check. No diff to read before it runs. No record of what was actually typed versus what the ticket said. No way to guarantee that site 40 got what site 1 got.

The fear underneath the question is blast radius — one script, forty sites, one mistake. That fear is fair. But the engineer fat-fingering a VLAN at 2 AM has a blast radius too. You just don't find out what it was until something breaks the following Tuesday.

Automation done right isn't a script someone runs and hopes.

It's a change that is:
— tested against a model of your network before it touches a device
— peer-reviewed like code, because it is code
— approved, tracked, and logged
— rolled back in minutes, not rebuilt from memory

That's how we build automation at MZS Networks. Python, Ansible, Terraform — with the safety practices of engineers who carry the pager for what they ship.

Automation isn't the risk. Unreviewed change is.

Talk to an engineer: mzsnetworks.com
