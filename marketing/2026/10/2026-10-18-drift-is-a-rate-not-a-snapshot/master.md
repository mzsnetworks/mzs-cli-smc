# Master — drift-is-a-rate-not-a-snapshot

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM and EN at 4:00 PM local, on a Monday.
**Date:** 2026-10-18
**Source:** `mzs-marketing` → `work/social/2026-10-18-marketing-batch-3/02-drift-is-a-rate-not-a-snapshot.md` (batch 3)
**Drafted:** 2026-10-18. Copied into this repo 2026-10-18; the folder date is the transfer date, not a publish date.
**Planned:** Mon Jan 18, 2027 — **EST**, so `19:00:00Z` for the ES slot and `21:00:00Z` for the EN slot. Daylight time begins Sun Mar 14, 2027; derive the offset from the date rather than copying it forward.
**Thesis:** Remediating drift is a project; staying remediated is a property of the system. What matters is the rate at which variation is reintroduced and what causes it, which a one-time cleanup never measures.
**Pillar:** Drift and audit stories
**Sells:** Continuous drift detection · Driftguard
**CTA:** Book a consultation
**Stats:** none. Batch 3 carries no metrics, no client results and no case studies by design — the anonymized-proof pillar is still blocked on a case study. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Written to the ES length band and ratio upstream, so nothing was expanded on transfer.

---

A drift remediation project ends. Drift does not.

The usual shape is a cleanup. Somebody exports the running configuration from every device, compares it against what the standard says, and works through the differences over a few weeks. At the end the estate matches. It is real work and it is worth doing.

Six weeks later it does not match any more, and the second conversation is harder than the first, because now it looks like the cleanup failed.

It did not fail. A cleanup corrects a state, and drift is not a state. It is a rate, and nothing in the cleanup changed the rate.

That rate has specific sources, and they are mostly ordinary. An emergency change at 2 AM that never came back through the standard. A vendor default that reappears after a firmware upgrade. A site built from an older template because that is what the installer had. An exception for one location, copied to four more by somebody reusing a config.

None of those are discipline problems, which is why asking people to be more careful does not move the number.

So the measurement worth having is not how far the estate is from the standard today. It is how fast it moves away, where that movement enters, and which of it was deliberate. Driftguard watches for that continuously rather than at audit time, which turns the question from an annual archaeology exercise into something with a trend line.

Once you can see the rate, the fix stops being more cleanups. It becomes closing the specific paths variation comes in through.

A perfectly remediated estate with an unexamined reintroduction rate is a snapshot. It was accurate on the day it was taken.

Book a consultation: mzsnetworks.com

#ConfigurationDrift #NetworkAutomation #NetOps
