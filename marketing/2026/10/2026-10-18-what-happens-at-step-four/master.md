# Master — what-happens-at-step-four

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM and EN at 4:00 PM local, on a Monday.
**Date:** 2026-10-18
**Source:** `mzs-marketing` → `work/social/2026-10-18-marketing-batch-3/04-what-happens-at-step-four.md` (batch 3)
**Drafted:** 2026-10-18. Copied into this repo 2026-10-18; the folder date is the transfer date, not a publish date.
**Planned:** Mon Feb 1, 2027 — **EST**, so `19:00:00Z` for the ES slot and `21:00:00Z` for the EN slot. Daylight time begins Sun Mar 14, 2027; derive the offset from the date rather than copying it forward.
**Thesis:** A script that dies halfway leaves the estate in a state nobody designed, and the difference between a script and an orchestrated workflow is entirely about what happens on partial failure — retries, idempotence, recorded state, and a named person who is told.
**Pillar:** Short technical teardowns
**Sells:** Orchestration with state and partial-failure handling · Workflow Engine
**CTA:** Talk to an engineer
**Stats:** none. Batch 3 carries no metrics, no client results and no case studies by design — the anonymized-proof pillar is still blocked on a case study. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Written to the ES length band and ratio upstream, so nothing was expanded on transfer.

---

An automation that fails at step four is worse than one that never ran at all.

Never ran is a known state. You are where you started, nothing is half-applied, and the worst outcome is somebody doing it by hand. Failed at step four is a state nobody designed: four changes applied, two not, and no record of which.

This is the real line between a script and a workflow, and it is not about language or tooling. A script executes steps. A workflow knows where it is.

Three things make that difference concrete.

It records state as it goes, so a failure leaves behind an account of what completed rather than a scrollback buffer somebody has to read. It is idempotent, so the fix is to run it again rather than to work out by hand which steps to skip. And it tells a named person, with enough context that they can act, instead of exiting non-zero into a log nobody is watching at 2 AM.

What makes this urgent is scale rather than complexity. A six-step job against one device is recoverable by reading the terminal. The same job across two hundred sites, failing on eleven of them for three different reasons, is not. That is where ad-hoc scripting stops being thrift and starts being the risk.

We build this with Workflow Engine over the APIs you already have, so the sequencing, the retries and the record live in one place rather than inside each script. The ordinary artifacts stay ordinary: Python and Ansible underneath, because you have to be able to hire for it and read it.

The question to ask about any automation you depend on is not whether it works. It is what it leaves behind when it stops halfway.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #Orchestration
