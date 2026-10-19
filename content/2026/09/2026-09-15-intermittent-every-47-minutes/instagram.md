# Instagram — intermittent-every-47-minutes

The ticket said intermittent. It fired every forty-seven minutes. ⏱️

Three people had already looked at it.

All three did the sensible thing: opened a dashboard, set it to the last 24 hours, saw noise.

Nothing to correlate. Closed with "monitoring." Reopened four days later.

What broke it open wasn't a clever theory. ⚙️

It was a longer window and a different plot.

→ thirty days of syslog instead of twenty-four hours of a graph
→ one row per event, ordered by timestamp
→ the gap between each event and the one before it

I stopped plotting how many events happened and started plotting when.

The gaps clustered. Not perfectly — but unmistakably — around forty-seven minutes.

That's when the problem changes shape completely.

Intermittent means "I have no model."

Periodic means something is running on a schedule. And schedules have owners.

You stop troubleshooting a network and start looking for a timer: a job, a poll, a lease, a re-auth, a cache expiry, a backup that starts when the last one finishes.

Two habits I took from it:

1️⃣ Widen the window before you widen the theory. If the tool's default range is one day, the tool is choosing your conclusion.

2️⃣ Plot the deltas, not the count. Volume tells you how bad. The interval tells you what kind — and only one of those names a suspect.

And a smaller lesson about language: three engineers wrote "intermittent," and each inherited it from the last as a finding.

It was never a finding. It was a description of how long everybody had looked.

Intermittent isn't a property of the fault. It's a confession about the window.

What's the longest period you've had to graph? 👇

#Troubleshooting #NetworkEngineering #NetOps #Networking #ITInfrastructure
