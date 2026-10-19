# Master — a-dry-run-is-not-a-test

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM and EN at 4:00 PM local, on a Monday.
**Date:** 2026-10-18
**Source:** `mzs-marketing` → `work/social/2026-10-18-marketing-batch-3/03-a-dry-run-is-not-a-test.md` (batch 3)
**Drafted:** 2026-10-18. Copied into this repo 2026-10-18; the folder date is the transfer date, not a publish date.
**Planned:** Mon Jan 25, 2027 — **EST**, so `19:00:00Z` for the ES slot and `21:00:00Z` for the EN slot. Daylight time begins Sun Mar 14, 2027; derive the offset from the date rather than copying it forward.
**Thesis:** A dry run proves the change is syntactically valid and will be accepted; it says nothing about whether the service survives. The four stages — dry run, model, lab or canary, production with a rehearsed revert — answer different questions, and skipping to the end is how an approved change becomes an outage.
**Pillar:** Safety practice
**Sells:** Staged validation as method — the safety differentiator
**CTA:** Talk to an engineer
**Stats:** none. Batch 3 carries no metrics, no client results and no case studies by design — the anonymized-proof pillar is still blocked on a case study. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Written to the ES length band and ratio upstream, so nothing was expanded on transfer.

---

"We dry-ran it" gets said in change reviews as though it settles the question. It does not.

A dry run tells you the change is syntactically valid and that the device will accept it. That is genuinely useful and it is not nothing. It is also the smallest of the questions worth asking, and the one least likely to be the reason a change goes wrong.

The changes that cause outages are usually accepted perfectly. The command was valid. The device took it. What then failed was a dependency nobody modeled, a traffic pattern the test did not generate, or a neighbor that reconverged in a way the diagram did not predict.

So we separate four stages, because each one answers a question the one before it cannot.

A dry run answers whether the syntax is right. A model answers what the change does to the intended topology, including the parts of it you were not thinking about. A lab or a canary site answers how real traffic behaves against it, which is where the surprises actually live. And production with a rehearsed revert answers the only question the business asked, which is whether the service still works.

Teams skip to the last stage because the first three cost time and the change looked simple. That is a defensible call on a change whose blast radius is small and well understood. It is how a Tuesday becomes a long night on anything else.

None of this requires more tooling than most estates already have. It requires agreeing which stage a change has to clear before it enters a window, and writing that down once rather than deciding it under time pressure.

Valid is not the same as safe. A dry run proves the first one.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #ChangeManagement
