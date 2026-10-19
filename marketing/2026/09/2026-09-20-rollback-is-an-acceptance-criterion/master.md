# Master — rollback-is-an-acceptance-criterion

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM EDT and EN at 4:00 PM, on a Monday.
**Date:** 2026-09-20
**Source:** `mzs-marketing` → `work/social/2026-09-20-marketing-batch-2/10-rollback-is-an-acceptance-criterion.md` (batch 2)
**Drafted:** 2026-09-20. Copied into this repo 2026-09-20; the folder date is the transfer date, not a publish date.
**Planned:** Mon Nov 9, 2026.
**Thesis:** Rollback is usually a paragraph in the change record rather than a tested capability. Treating it as an acceptance criterion changes what gets built.
**Pillar:** Safety practice
**Sells:** Safety practice as method — the differentiator
**Stats:** none. Batch 2 carries no metrics, no client results and no case studies by design. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English.

---

Most change records have a rollback plan. Far fewer have a rollback that has ever been executed.

The usual version reads something like "revert to previous configuration." That is a sentence, not a procedure. It does not say where the previous configuration is stored, whether it is the running or the startup config, what happens to the state that accumulated since, or how long the revert takes on a device that needs a reload to apply it.

Under pressure, at 2 AM, that gap is where the outage gets longer instead of shorter.

And the configuration is rarely the hard part. What makes a revert difficult is the state that accumulated while the change was live: sessions established, entries learned, a neighbor that reconverged around the new topology and will now have to reconverge back. A rollback that restores the config and ignores the state is how an outage outlives the fix that caused it.

We treat rollback as an acceptance criterion rather than documentation. An automated change is not finished until the reverse path has been run — against the model first, then in a lab or a canary site — and the time it takes is a known number rather than an estimate.

This sounds like overhead. It is the thing that makes the rest of it fast, because a change you can reliably undo can be approved on its merits instead of on its blast radius. Teams that can revert in minutes approve more changes, not fewer.

The question worth asking about your last automated change: has anyone run the rollback, or does it just exist on paper?

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #InfrastructureAsCode
