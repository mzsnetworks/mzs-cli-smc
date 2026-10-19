# Master — test-before-it-touches-a-device

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM EDT and EN at 4:00 PM, on a Monday.
**Date:** 2026-09-20
**Source:** `mzs-marketing` → `work/social/2026-09-20-marketing-batch-2/03-test-before-it-touches-a-device.md` (batch 2)
**Drafted:** 2026-09-20. Copied into this repo 2026-09-20; the folder date is the transfer date, not a publish date.
**Thesis:** Networks are the last place where the standard test procedure is to run the change in production and watch. Modelling the change first is ordinary engineering practice everywhere else.
**Pillar:** Safety practice
**Sells:** Config Modeling
**Stats:** none. Batch 2 carries no metrics, no client results and no case studies by design — there is nothing documented to cite yet, so every post is built from technical judgment, method, or buyer education. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with a hand-written ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Both renders arrived written, not translated.

---

In most disciplines, "we'll run it and see what happens" is not a test plan.

In networking it is still the default. The change gets reviewed by reading it, approved by someone who also read it, and then validated by applying it to production during a window and watching what breaks.

Reading a change tells you it is syntactically fine. It does not tell you that this ACL, on this device, with this routing table, drops the traffic you forgot about.

The alternative is not exotic. Build a model of the network — topology, addressing, policy, adjacencies — and evaluate the change against the model before it reaches a device. What you get back is not "the config parses." It is what the network would do differently, and which of those differences you did not intend.

That is what Config Modeling does, and it is the single practice that moves the most risk out of the change window, because it moves the discovery of a mistake from 2 AM in production to a Tuesday afternoon on a laptop.

A model does not catch everything, and it is worth being clear about that. It will not tell you an optic is degrading, or that the far end has an undocumented policy of its own, or that the vendor's implementation disagrees with the vendor's documentation. What it catches is the class of error that comes from reasoning about a large network inside one person's head. In a multi-site estate, that is most of them.

It also changes the review conversation. Reviewers stop arguing about syntax and start arguing about intent, which is the argument worth having.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #InfrastructureAsCode #NetOps
