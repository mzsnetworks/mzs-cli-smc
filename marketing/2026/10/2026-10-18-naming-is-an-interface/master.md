# Master — naming-is-an-interface

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM and EN at 4:00 PM local, on a Monday.
**Date:** 2026-10-18
**Source:** `mzs-marketing` → `work/social/2026-10-18-marketing-batch-3/06-naming-is-an-interface.md` (batch 3)
**Drafted:** 2026-10-18. Copied into this repo 2026-10-18; the folder date is the transfer date, not a publish date.
**Planned:** Mon Feb 15, 2027 — **EST**, so `19:00:00Z` for the ES slot and `21:00:00Z` for the EN slot. Daylight time begins Sun Mar 14, 2027; derive the offset from the date rather than copying it forward.
**Thesis:** Inconsistent hostnames, interface descriptions and site codes are not a tidiness problem; they are the reason every automation needs special cases, and they set a ceiling on what can be automated at all.
**Pillar:** Drift and audit stories
**Sells:** Standards and inventory hygiene as an automation precondition
**CTA:** Talk to an engineer
**Stats:** none. Batch 3 carries no metrics, no client results and no case studies by design — the anonymized-proof pillar is still blocked on a case study. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Written to the ES length band and ratio upstream, so nothing was expanded on transfer.

---

Naming conventions get treated as housekeeping. They are an interface, and automation is the consumer.

Here is where it shows up. Somebody writes a script that acts on every distribution switch. To know which devices those are, it matches on the hostname. The convention held for the first eight sites and then stopped, because a different team built the next twelve, and a merger brought thirty more on a scheme nobody wrote down.

Now the script needs a lookup table of exceptions. The table needs maintaining. The person who maintains it is the only one who understands it.

The same happens with interface descriptions. A monitoring system that tells a customer circuit from a backup link reads the description field, because that is the only place the distinction exists. Where that field is free text, the capability is not available, whatever the platform could do.

What makes this hard to fix is that it is never urgent. Nothing is broken. Every individual inconsistency is small, defensible, and was the obvious choice at the time.

The cost does not arrive as an outage. It arrives as a ceiling. Every automation gets more special cases, each reasonable, until the special cases are the system and nobody will touch it.

The fix is not a renaming project across the estate, which is disruptive and rarely gets approved. It is agreeing the convention now, applying it to everything new, and reconciling the existing estate in the order the automation roadmap actually needs it. Every piece of that roadmap gets cheaper the moment the names mean something.

A machine cannot infer what you meant. It can only read what you wrote.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #InfrastructureAsCode
