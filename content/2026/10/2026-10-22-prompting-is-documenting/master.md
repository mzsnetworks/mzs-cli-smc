# Master — prompting-is-documenting

**Preset:** Professional (LinkedIn personal profile + Instagram @mzsnetworks)
**Date:** 2026-10-22
**Thesis:** Prompting is the new documenting. What separates engineers who get useful output from a model is the ability to state intent, constraints and success conditions precisely — which was always the scarce skill, and was always what good documentation required.
**Pillar:** Network Automation
**Source:** ideas-2026-08-27 #20
**Stats:** none. Judgment and practice only; no statistic stated as fact.

---

Prompting is the new documenting, and I mean that more literally than it sounds.

Watch two engineers use the same model on the same task. One gets something they can use. The other gets something plausible and wrong, and concludes the tool is overrated.

The difference is almost never the phrasing. It is that the first one stated the constraints.

Which platform and which version. What the device already has on it. What must not change. What "correct" looks like when it is finished. Those are not prompt-engineering tricks. That is the same information a competent change record has always required, and the same information that was missing from every wiki page any of us has ever cursed at.

Which is the uncomfortable part. The model is not rewarding a new skill. It is exposing an old one, and it is doing it immediately and in public, because the gap between what you meant and what you said now comes back as output in four seconds rather than as an outage in four months.

We used to be able to hide imprecision. A vague runbook still worked, because a human read it and silently supplied the missing half from context. Models do not supply context you did not give them. They supply something that looks like it.

There is a practical habit in this that pays off regardless of the tool. When you cannot get a useful answer out of a model, the fault is usually not in the request, it is that you have not actually decided something. "Make this safe" means nothing until you say safe against what. The moment you can write that down, you can also write the test, the change record and the rollback, because they are all the same sentence pointed at different audiences.

The engineer who can describe intent precisely gets more out of the model. They were also always the one whose handover you wanted to inherit.

That skill did not appear in 2025. It just stopped being optional.
