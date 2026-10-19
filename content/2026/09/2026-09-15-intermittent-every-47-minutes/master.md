# Master — intermittent-every-47-minutes

**Preset:** Professional (LinkedIn personal + Instagram @mzsnetworks)
**Date:** 2026-09-15 (Tue)
**Source idea:** ideas-2026-08-27 #3
**Thesis:** "Intermittent" is a statement about the window you looked at, not about the fault. Plot the timestamps, compute the deltas, find the period.
**Stats:** none — story/craft post, no factcheck gate.

---

The ticket said intermittent. It fired every forty-seven minutes.

Three people had already looked at it. All three had done the sensible thing: pulled up a dashboard, set it to the last twenty-four hours, and seen noise. Nothing to correlate. Closed with "monitoring," reopened four days later.

What broke it open wasn't a clever theory. It was a longer window and a different plot.

I pulled thirty days of syslog for the interface instead of twenty-four hours of a graph. Then — and this is the part that mattered — I stopped plotting how many events happened and started plotting when. One row per event, ordered by timestamp, and the gap between each event and the one before it.

The gaps clustered. Not perfectly, but unmistakably, around forty-seven minutes.

At that moment the problem changes shape completely. Intermittent means "I have no model." Periodic means something is running on a schedule, and schedules have owners. You stop troubleshooting a network and start looking for a timer — a job, a poll, a lease, a re-auth, a cache expiry, a backup that starts when the previous one finishes.

The two habits I took from it:

Widen the window before you widen the theory. A five-minute graph over one day can hide a pattern that thirty days of raw timestamps makes obvious. If the tool's default range is a day, the tool is choosing your conclusion.

Plot the deltas, not the count. Event volume tells you how bad. The interval between events tells you what kind. Those are different questions, and only one of them names a suspect.

And there's a smaller lesson about language. Three engineers wrote "intermittent" in the notes, and each one inherited it as a finding from the one before. It was never a finding. It was a description of how long everybody had looked.

Intermittent isn't a property of the fault. It's a confession about the window.

What's the longest period you've ever had to graph before something finally showed up?
