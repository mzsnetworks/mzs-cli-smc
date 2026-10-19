# Master — four-questions

**Preset:** Professional — LinkedIn **personal profile** (no pageId) + Instagram @mzsnetworks
**Date:** 2026-11-03
**Thesis:** The questions that decide whether automation is safe are contextual, not technical: real frequency, who else runs it, what a partial failure leaves behind, and what check proves the outcome. The third is the one most often skipped and the one that causes the damage.
**Pillar:** Network Automation
**Source:** ideas-2026-08-27 #24
**Stats:** none. Judgment and personal practice only; no statistic stated as fact.

---

Four questions before I automate anything. None of them is "can this be automated."

How often does it actually run? Not how often it feels like it runs. I have built things for a process somebody described as weekly that turned out to happen twice a year, and I have skipped things that happen four times a day because nobody mentioned them. The honest number decides whether this is worth doing at all.

Who else runs it? If the answer is only me, I am not automating a process, I am building a personal tool and calling it automation. That is fine as long as everybody knows, but it changes what I build. Something a colleague will run at 2am needs error messages written for them, not for me.

What happens if it half-finishes? This is the one that gets skipped, and it is the one that hurts. A script that stops two devices into a five-device change leaves the network in a state nobody designed. Either the thing has to be safe to rerun from the start, or it has to tell me precisely where it stopped. Deciding which, before writing it, changes the whole shape of the code.

And how will I know it did what I think it did? Exit code zero means the script finished. It does not mean the change is in place and working. If I cannot name the check that proves the outcome, I have not automated the task, I have automated the typing.

What these have in common is that none of them is technical. They are about the context the script runs in, and that context is what makes automation safe or dangerous.

The scripts I regret are never the ones that were hard to write. They are the ones I wrote before I had answered the third question.

Which of those four do you usually skip?
