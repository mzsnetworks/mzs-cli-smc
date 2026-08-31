# Instagram — llm-config-operationally-wrong

It passed lint. It passed review. It failed at four hundred devices. ⚠️

The config was generated, and it was syntactically perfect.

Right keywords. Right order. Valid on every parser I put it through.

Nothing about it looked like a mistake — because in the way we normally mean the word, it wasn't one.

It was just wrong about this network. ⚙️

What I think happened is a calibration problem in me, not a capability problem in the tool.

Reviewing generated config is a different task from reviewing config a person wrote. I was doing the second one.

→ when a human writes config, the errors are typos, omissions, half-finished thoughts
→ you scan for what's missing or malformed, and your eye is trained for it
→ when a model writes config, the output is complete, internally consistent and confident
→ nothing is missing

The error isn't in a token. It's in a premise, sitting underneath the syntax where nobody is looking.

Two things changed after that.

📍 Where a generated change goes first

It used to go to a representative device — in practice, a recent one that was easy to reach.

Now it goes to the oldest and strangest device in the fleet. The one with the manual fix from years ago, the older software train, the exception everybody works around.

Survive that, and the standard estate is straightforward. Fail, and you fail on one device, at a time you chose.

📍 What I actually review

I ask for the assumptions out loud, before the config: what does this change assume about platform behavior, software version, existing state, and what's already configured.

Then I review that list. It's much shorter — and it's where the mistake lives.

I use these tools daily and I'm not going back. I just stopped treating fluency as evidence.

A model can be fluent in your syntax and ignorant of your network.

Would a generated change hit your oldest device first, or last? 👇

#NetworkAutomation #AI #NetOps #NetworkEngineering #NetDevOps
