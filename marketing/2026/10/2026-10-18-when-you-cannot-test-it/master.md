# Master — when-you-cannot-test-it

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM and EN at 4:00 PM local, on a Monday.
**Date:** 2026-10-18
**Source:** `mzs-marketing` → `work/social/2026-10-18-marketing-batch-3/08-when-you-cannot-test-it.md` (batch 3)
**Drafted:** 2026-10-18. Copied into this repo 2026-10-18; the folder date is the transfer date, not a publish date.
**Planned:** Mon Mar 1, 2027 — **EST**, so `19:00:00Z` for the ES slot and `21:00:00Z` for the EN slot. Daylight time begins Sun Mar 14, 2027; derive the offset from the date rather than copying it forward.
**Thesis:** Some changes genuinely cannot be lab-tested — scale effects, vendor-specific behavior, one-of-a-kind hardware. The answer is not to skip testing but to replace it with staged exposure, measured observation and a rehearsed revert, and to say out loud which category a change is in.
**Pillar:** Safety practice
**Sells:** Method for high-uncertainty change — staged exposure and rehearsed revert
**CTA:** Book a consultation
**Stats:** none. Batch 3 carries no metrics, no client results and no case studies by design — the anonymized-proof pillar is still blocked on a case study. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Written to the ES length band and ratio upstream, so nothing was expanded on transfer.

---

Some changes cannot be tested before you make them, and pretending otherwise is its own risk.

The lab does not have the other vendor's hardware. The behavior only appears above a traffic volume you cannot generate. The platform is one of a kind, with no second unit anywhere. These are not excuses. They are the real conditions in a lot of estates.

What goes wrong is not that the change is risky. It is that the plan pretends it is not. The change record says tested, meaning something adjacent was, and everyone proceeds with a confidence the evidence does not support.

So the first move is to name the category out loud. This change cannot be validated in advance. Once that is said, the conversation becomes about exposure rather than about certainty, and that is a conversation that can actually be managed.

Then the method changes shape. Smallest possible first application, on the site where the consequence is most tolerable. A defined observation period before the second, long enough to cross a real traffic pattern rather than a quiet hour. An explicit list of what you are watching and what reading means stop. And a revert rehearsed until its duration is a known number, because the decision to use it gets made under pressure by somebody tired.

That sequence does not remove the uncertainty. It converts it into something bounded: one site instead of forty, a known window, a known way back.

The failure mode worth avoiding is the confident rollout of an untested change across the estate in one window, because it was approved and the window was booked.

Untestable is a property of the change. Unmanaged is a choice about the plan.

Book a consultation: mzsnetworks.com

#NetOps #NetworkEngineering #ChangeManagement
