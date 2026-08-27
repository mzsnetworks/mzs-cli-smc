# Master — uptime-is-lagging

**Preset:** Business (MZS company account — LI page, FB, IG, X)
**Date:** 2026-08-28 (Fri)
**Source idea:** ideas-2026-07-11 #10 (ENO · Reframe)
**Thesis:** Uptime is a lagging indicator. What predicts the next outage is change velocity measured against review discipline.

---

Uptime is a lagging indicator.

It tells you what already survived. It says nothing about what's about to break.

We report it anyway, because it's the easiest number in the building to count. Four nines looks like a job well done — right up until the quarter it isn't, and nobody saw it coming, because the metric was never built to warn anyone.

Here's the pair we'd watch instead: how fast the environment changes, measured against how much review those changes actually get.

Not velocity on its own. DORA's State of DevOps research has found the same thing year after year — the fastest-moving teams are also the most stable ones. Throughput and stability rise together. They aren't a trade.

So the risk was never change velocity. It's change velocity outrunning review discipline.

That gap is visible long before an outage:

The "standard change" list keeps growing, because getting an exception is slow.

Approvals come back in under a minute — which makes them approvals, not readings.

Rollback is a paragraph in the ticket that nobody has ever executed.

The person who understands the change is also the person approving it.

Every one of those is measurable this week. None of them require an incident first.

An environment with heavy change and real review is safer than one with light change and rubber stamps — even though the second one has better uptime, right up until the day it doesn't.

Uptime tells you what survived. Change velocity tells you what's coming. Review discipline decides which one you get.

What's your ratio — and when did anyone last check it?

## Sources

- DORA (Google Cloud), *State of DevOps Report* — throughput and stability move together; the highest performers lead on both rather than trading one for the other. https://dora.dev/research/
