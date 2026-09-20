# Master — tools-that-dont-talk

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM EDT and EN at 4:00 PM, on a Monday.
**Date:** 2026-09-20
**Source:** `mzs-marketing` → `work/social/2026-09-20-marketing-batch-2/05-tools-that-dont-talk.md` (batch 2)
**Drafted:** 2026-09-20. Copied into this repo 2026-09-20; the folder date is the transfer date, not a publish date.
**Planned:** Mon Nov 16, 2026.
**Thesis:** The integration gap between networking, monitoring and ticketing is not a tooling problem. It is unwritten glue, and the glue is currently a person.
**Pillar:** Short technical teardowns
**Sells:** Orchestration and custom API integration · Workflow Engine
**Stats:** none. Batch 2 carries no metrics, no client results and no case studies by design. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English.

---

Count the systems a single routine change touches at your company.

A ticket gets raised. Someone checks monitoring to confirm the symptom. Someone opens the network platform and makes the change. Someone updates the ticket. Maybe the CMDB gets corrected, maybe it doesn't. Maybe the monitoring threshold gets adjusted for the new state, usually later.

Every one of those systems has an API. Almost none of them are connected to each other.

What fills the gap is a person, moving information between browser tabs. That person is also the failure point: when they are on vacation the process degrades, and when they are busy the CMDB is the step that gets skipped. That role is on nobody's org chart and it exists anyway, and most teams only discover how much depended on it when that person changes jobs.

This is the least glamorous automation work there is and frequently the highest return, because you are not replacing engineering judgment — you are replacing transcription. Ticket opens, enrichment runs, change executes against the platform, ticket updates itself, inventory reconciles, monitoring adjusts.

We build this as orchestration across whatever you already own, through the APIs those products already ship. Workflow Engine is the piece that sequences it, with the same safety rules as any other change: tested, reviewed, tracked, reversible.

Nobody puts "reduced tab-switching" in a business case. It is still where the hours are.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #InfrastructureAsCode
