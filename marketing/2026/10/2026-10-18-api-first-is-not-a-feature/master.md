# Master — api-first-is-not-a-feature

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM and EN at 4:00 PM local, on a Monday.
**Date:** 2026-10-18
**Source:** `mzs-marketing` → `work/social/2026-10-18-marketing-batch-3/10-api-first-is-not-a-feature.md` (batch 3)
**Drafted:** 2026-10-18. Copied into this repo 2026-10-18; the folder date is the transfer date, not a publish date.
**Planned:** Mon Mar 15, 2027 — **EDT**, so `18:00:00Z` for the ES slot and `20:00:00Z` for the EN slot. Daylight time begins Sun Mar 14, 2027; derive the offset from the date rather than copying it forward.
**Thesis:** Every platform claims an API; what matters for automation is whether it writes as well as reads, handles bulk operations, returns usable errors, and survives its own rate limits at your estate's size. Those are evaluation criteria, not assumptions.
**Pillar:** Short technical teardowns
**Sells:** Evaluating vendor APIs as an automation surface — orchestration and API integration
**CTA:** Talk to an engineer
**Stats:** none. Batch 3 carries no metrics, no client results and no case studies by design — the anonymized-proof pillar is still blocked on a case study. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Written to the ES length band and ratio upstream, so nothing was expanded on transfer.

---

"It has an API" is on every datasheet and tells you almost nothing about whether you can automate against it.

We find out the real answer during integration work, usually in the first week, and it is worth knowing before the purchase rather than after.

Four things decide it.

Whether it writes, or only reads. A read-only API gives you reporting. It does not give you provisioning, and the difference is the entire business case for a lot of projects. Vendors are rarely explicit about which operations are exposed.

Whether it does bulk. An endpoint that handles one object per call is a different tool than one that takes a batch. At four hundred objects with a rate limit, per-object calls turn a maintenance task into an overnight job, and the retry logic you now have to write is where the bugs live.

Whether the errors are usable. A failure that returns a specific reason can be handled automatically. One that returns a generic failure with a 200 status needs a human to interpret it, which means the automation stops being unattended.

Whether it is versioned, and what happens on upgrade. An API that changes shape without notice turns every platform upgrade into an automation outage you find out about afterwards.

None of this requires a long evaluation. It requires asking for credentials to a test instance and spending two days writing against it in Python before the contract is signed, rather than discovering it in month two of a project that was scoped assuming it would work.

An API is a product surface, and it has a quality. Treat it as something to evaluate, not something to assume.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #APIIntegration
