# Master — one-bottleneck-not-a-framework

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM EDT and EN at 4:00 PM, on a Monday. First person, about his own experience.
**Date:** 2026-09-08
**Source:** `mzs-marketing` → `work/social/2026-07-08-network-automation-services-linkedin.md`, "Post 2 — The contrarian ("you don't need a big framework")"
**Drafted:** 2026-07-08. Copied into this repo 2026-09-08; the folder date is the transfer date, not a publish date.
**Thesis:** Vendor pitches start with the platform: six months of design and a seven-figure line item. Start with one repetitive process instead — the quick win pays for the roadmap conversation, not the other way around.
**Pillar:** Positioning against big SI firms
**Stats:** the "19 years" is Luis's own experience running production networks, confirmed 2026-09-09 — it is a personal credential, not company tenure (MZS's Florida LLC dates to 2022), so the post says "taught me" and is written to be published from Luis's profile rather than the company page. Other figures ("30 sites", "38 of 40 sites", "a full engineering week") describe a hypothetical reader, not MZS, and are illustrative by design.
**Revised:** 2026-09-09 — transferred draft ran short of this repo's LinkedIn target and stated its claim without the mechanism behind it. Added the reasoning; lengths now in range.

**Language:** EN master with a hand-written ES render (`linkedin-es.md`) using the EN→ES glossary in `rules/SPANISH.md` (ported from the `mzs-brand` skill inside `mzs-marketing`, not the `mzs-brand` repo) — usted register, product names untranslated. ES is a primary selling language, not a translation layer, so re-render it by hand rather than machine-translating the EN.

---

Unpopular opinion from an automation company: you probably don't need a "network automation framework."

Every vendor pitch says start with the platform. Six months of design, a steering committee, a seven-figure line item.

Meanwhile your engineers are still pushing firewall updates by hand across 30 sites.

Here's the problem with starting at the platform. A framework is a bet on which processes will matter in two years, made before you have automated a single one. You are choosing abstractions for work you have not done yet. And the thing that actually kills these programs isn't the technology — it's that eighteen months in, nobody can point at an hour that came back.

Start smaller:
— One repetitive process. The one that eats a full engineering week every month.
— Automate it end to end. Tested, reviewed, rollback-able.
— Measure the hours back. Then pick the next one.

The second process is easier than the first, because now you know what your inventory data is actually like, which devices lie about their state, and where your exceptions live. That knowledge is the real prerequisite for a framework. You buy it by shipping something small.

One of our engagements began as a network refresh — one scoped project, not a program. That work is what led to the roadmap conversation, not the other way around.

Not every engagement requires a large framework. Sometimes it requires one solved bottleneck.

Book a consultation: mzsnetworks.com
