# Master — llm-config-operationally-wrong

**Preset:** Professional (LinkedIn personal + Instagram @mzsnetworks)
**Date:** 2026-09-24 (Thu)
**Source idea:** ideas-2026-08-27 #12
**Thesis:** Reviewing generated config is a different task from reviewing written config. The error is a premise, not a token.
**Note:** distinct from `your-tickets-are-lies` (2026-09-01, what AI learns from) and the reference `ai-makes-us-judges`. This is about the review gate.
**Stats:** none — story/judgment post, no factcheck gate.

---

It passed lint. It passed review. It failed at four hundred devices.

The config was generated, and it was syntactically perfect. Right keywords, right order, valid on every parser I put it through. Nothing about it looked like a mistake, because in the way we normally mean the word, it wasn't one.

It was just wrong about this network.

What I've come to think happened is a calibration problem in me, not a capability problem in the tool. Reviewing generated config is a different task from reviewing config a person wrote, and I was doing the second one.

When a human writes config, the errors are typos, omissions, and half-finished thoughts. You scan for what's missing or malformed, and your eye is trained for it. When a model writes config, the output is complete, internally consistent and confident. There is nothing missing. The error isn't in a token — it's in a premise, sitting underneath the syntax where nobody is looking.

Two things changed after that.

The first is where a generated change lands first. It used to go to a representative device — in practice, a recent one that was easy to reach. Now it goes to the oldest and strangest device in the fleet — the one with the manual fix from years ago, the older software train, the exception everybody works around. If a change survives that, the standard estate is straightforward. If it fails, it fails on one device, at a time I chose.

The second is what I actually review. I ask for the assumptions out loud, before the config: what does this change assume about platform behavior, software version, and existing state. Then I review that list. It's much shorter, and it's where the mistake lives.

I use these tools daily and I'm not going back. But I stopped treating fluency as evidence.

A model can be completely fluent in your syntax and completely ignorant of your network. Review the premises, not the punctuation.

What's the oldest device in your fleet — and would a generated change go there first, or last?
