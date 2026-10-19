# Master — one-vendor-isnt-automation

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM EDT and EN at 4:00 PM, on a Monday.
**Date:** 2026-09-20
**Source:** `mzs-marketing` → `work/social/2026-09-20-marketing-batch-2/06-one-vendor-isnt-automation.md` (batch 2)
**Drafted:** 2026-09-20. Copied into this repo 2026-09-20; the folder date is the transfer date, not a publish date.
**Planned:** Mon Dec 7, 2026.
**Thesis:** Vendor-native automation works beautifully until the second vendor arrives, which it always does. Portability is a design decision made early or paid for later.
**Pillar:** Short technical teardowns
**Sells:** Network automation · technical credibility
**Stats:** none. Batch 2 carries no metrics, no client results and no case studies by design. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English.

---

Every major vendor ships an automation platform, and each one works well — inside its own estate.

Then the acquisition closes, or the branch refresh goes to a different supplier, or the data center standardizes on something the campus never will. Now you have two automation platforms, two sources of truth, two definitions of a compliant configuration, and an engineer who is fluent in one of them.

Multi-vendor is not a hypothetical end state. It is what an enterprise network becomes after any five-year period with more than one procurement decision in it.

This is why our automation work sits above the vendor layer rather than inside it — Python, Ansible, Terraform, and the platform APIs underneath. The intent lives in your repository in a form that outlasts the hardware. The vendor-specific piece becomes what it should have been all along: a driver, not the architecture.

Two things follow. You can adopt a new vendor without restarting the automation program. And your engineers develop a skill that transfers, which matters more for retention than most people account for.

The tradeoff is real and worth naming. A vendor's own platform will always do vendor-specific things faster than an abstraction over it, and an abstraction you maintain is an abstraction you maintain. The question is not which approach is more elegant. It is which one you are still running after the next procurement cycle.

Portability is not free. It is cheaper than the migration you will otherwise run twice.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #InfrastructureAsCode #NetworkEngineering
