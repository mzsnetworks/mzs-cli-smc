# LinkedIn — handoff-that-survives


Incidents die at handoff more often than they die at diagnosis.

Not because the incoming engineer is worse. Because what gets transferred is almost always the wrong thing: a narrative of what happened, delivered by somebody who has been awake too long, to somebody who wasn't there.

The narrative feels like the important part. It isn't. It's the least portable thing in the room.

Three things carry. I've stopped handing over anything else first.

Current state. Not the history — what is true right now. What's up, what's down, what's degraded, what's been changed since this started and not changed back. If you fail over something at 2am and hand off at 6am without saying so, the next person is troubleshooting a system that isn't the one in their head.

What's been ruled out, and how. Not "we checked DNS" — "DNS resolves correctly from the affected subnet, tested at 03:40 from two hosts." The difference matters: the first gets silently re-checked, the second doesn't. Every re-check is time you already spent, spent again.

What you'd try next, and why. Even when you're wrong. Especially when you're wrong — a stated hypothesis is something the next person can disagree with, and disagreement is fast. A blank space just gets refilled with their own first instinct, which is usually the same instinct you started with four hours ago.

Everything else — the timeline, the false starts, who said what — belongs in the write-up afterwards. Useful there. Dead weight at 6am.

The other half is the receiving side — the half I got wrong for years. Read it back, out loud, in your own words, before the other person leaves. Every handoff I've seen fail had a moment where both people believed the same words meant the same thing. Sixty seconds of read-back catches it while somebody who knows is still in the room.

An incident doesn't get harder overnight. It gets harder at the seam.

Current state. What's ruled out. What you'd try next. What's in your handoff that doesn't survive the trip?

#IncidentResponse #NetOps #NetworkEngineering
