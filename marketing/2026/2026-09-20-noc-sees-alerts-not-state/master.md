# Master — noc-sees-alerts-not-state

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM EDT and EN at 4:00 PM, on a Monday.
**Date:** 2026-09-20
**Source:** `mzs-marketing` → `work/social/2026-09-20-marketing-batch-2/04-noc-sees-alerts-not-state.md` (batch 2)
**Drafted:** 2026-09-20. Copied into this repo 2026-09-20; the folder date is the transfer date, not a publish date.
**Planned:** Mon Nov 23, 2026.
**Thesis:** Most operations centers are instrumented to report events and cannot answer questions about state. The gap shows up the moment someone asks what is true right now.
**Pillar:** Short technical teardowns
**Sells:** ITOC Dashboard · orchestration
**Stats:** none. Batch 2 carries no metrics, no client results and no case studies by design. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English.

---

Ask your operations center a question that isn't an alert and watch what happens.

"How many sites are running the approved image?"
"Which circuits are we paying for that carry no traffic?"
"What changed in the last 24 hours, and by whom?"

Most NOCs cannot answer these in the moment, and it is not a competence problem. They were instrumented to report events — something crossed a threshold, something stopped responding. Events are necessary. They are also a description of what went wrong, not of what is.

The consequence is subtle. Teams get very good at reacting and stay blind to accumulation: the image versions drifting apart, the circuit nobody canceled, the change that was fine on its own and less fine combined with the other two that week.

Closing this means aggregating state rather than events — inventory, versions, configuration posture, change history — into one view somebody actually opens. That is what we built ITOC Dashboard for, and what most orchestration work ends up producing as a side effect, because you cannot orchestrate across systems without first reconciling what each of them believes.

The test is simple: can someone who is not on the network team get an accurate answer without asking an engineer?

Book a consultation: mzsnetworks.com

#NetOps #NetworkAutomation #NetworkEngineering
