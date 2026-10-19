# Master — blast-radius-before-the-window

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM and EN at 4:00 PM local, on a Monday.
**Date:** 2026-10-18
**Source:** `mzs-marketing` → `work/social/2026-10-18-marketing-batch-3/07-blast-radius-before-the-window.md` (batch 3)
**Drafted:** 2026-10-18. Copied into this repo 2026-10-18; the folder date is the transfer date, not a publish date.
**Planned:** Mon Feb 22, 2027 — **EST**, so `19:00:00Z` for the ES slot and `21:00:00Z` for the EN slot. Daylight time begins Sun Mar 14, 2027; derive the offset from the date rather than copying it forward.
**Thesis:** What else does this touch" is the question a change review cannot answer from a diff, because the diff shows the device and the risk lives in the topology. Modeling the change against the intended network answers it in the review rather than at 2 AM.
**Pillar:** Short technical teardowns
**Sells:** Pre-change impact analysis against a network model · Config Modeling
**CTA:** Talk to an engineer
**Stats:** none. Batch 3 carries no metrics, no client results and no case studies by design — the anonymized-proof pillar is still blocked on a case study. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Written to the ES length band and ratio upstream, so nothing was expanded on transfer.

---

A change review reads a diff. The risk is almost never in the diff.

The diff is honest about what it shows: these lines on this device become those lines. Reviewers check the syntax, check it matches the standard, and approve. The part they cannot check from that view is what else the change touches, because that lives in the topology rather than in the device.

So the question gets answered by memory. Somebody senior reads the change and says it looks fine, meaning they cannot immediately think of a dependency it breaks. That is genuinely valuable and it is not a method. It scales exactly as far as one person's recall of an estate that changed last Tuesday.

Modeling the change against the intended network is the part that does scale. A prefix removed here stops being advertised there. A policy tightened on one firewall moves traffic onto a path that was sized for failover rather than for steady state. An MTU change on a link affects a tunnel three hops away that nobody in the room is thinking about.

These are not exotic failures. They are the ordinary ones, and what they have in common is that the device-level change was correct. Nothing in a diff was going to reveal them.

Config Modeling answers the blast-radius question before the window opens, as part of the review, rather than leaving it to be discovered by traffic at two in the morning. The output is not a pass or a fail. It is a list of what else is affected, which is what a reviewer needed in order to approve properly in the first place.

An approved change is one somebody decided was safe. A modeled change is one where the question was actually asked.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #ChangeManagement
