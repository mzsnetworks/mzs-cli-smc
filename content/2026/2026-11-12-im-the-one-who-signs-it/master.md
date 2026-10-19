# Master — im-the-one-who-signs-it

**Preset:** Professional — LinkedIn **personal profile** (no pageId) + Instagram @mzsnetworks
**Date:** 2026-11-12
**Thesis:** The argument about model accuracy is unresolvable and beside the point. The operative question is accountability: a change entering production under an engineer's name is answered for by that engineer, and reading it is what makes the output theirs rather than a quality step to optimize away.
**Pillar:** Network Automation
**Source:** ideas-2026-08-27 #11
**Stats:** none. Judgment and personal practice only; no statistic stated as fact.

---

I use AI to write configs most days, and I still read every line. Not because it is usually wrong. Because I am the one who signs it.

That distinction matters more than the accuracy argument, which is the one everybody has instead.

The accuracy argument goes in circles. Somebody says the model gets it wrong, somebody else says so do people, and both are right in a way that settles nothing. Meanwhile the actual question is not how often it is wrong. It is who is accountable when it is.

When a change goes into production under my name, I am the one who answers for it at the review. Not the tool. Not the vendor of the tool. And I cannot answer for something I did not read, which means reading it is not a quality control step I can optimize away. It is the thing that makes the output mine.

What this looks like in practice is less dramatic than it sounds. The model drafts, and it is genuinely faster than typing. Then I read it the way I would read a colleague's change: what does this do, what does it assume, what does it touch that I did not ask about. That last one catches the most. Models are helpful, and helpful sometimes means adding a line you did not request because it usually goes with the thing you did.

The part that surprised me is that this made me better at reviewing people, too. Reading generated config forced me to articulate what I was actually checking for, which I had been doing by instinct and could not have written down.

I am not arguing against the tool. I use it daily and I would not go back.

I am arguing that "the model wrote it" has never once been an acceptable answer to "why is this in production," and it is not going to start being one.

Would you sign a change you had not read?
