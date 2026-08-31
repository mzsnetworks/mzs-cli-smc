# LinkedIn — monitoring-bill-scales


Your monitoring bill scales with data. Your understanding doesn't.

Every device you add, every metric you enable, every month of retention you extend — all of it costs more. None of it automatically tells you anything you didn't already know. Those two curves separate quietly, and nobody is assigned to watch the gap.

Most of the growth was never a decision. It's the default polling interval applied to several thousand interfaces because that's what the template did. It's retention set at the maximum on day one, in case. It's debug-level logging switched on during an investigation in 2023 and never switched off. It's a per-host agent that made sense on twelve servers and now runs on workloads that live for nine minutes.

Here's the uncomfortable test. Take any metric you're paying to store and ask when it last changed a decision. Not when it was last displayed — when it last changed what somebody did. For most of what we find, nobody can answer.

What we do about it:

→ Tier retention by the question, not by the source. Thirty days at full resolution answers "what happened last Tuesday." Capacity trends need two years but not per-second granularity.
→ Sample the high-cardinality things instead of storing every instance of them.
→ Turn off any collection nobody has queried in a year. You can always turn it back on, and the fear of needing it is doing more work than the data is.
→ Put a cost figure next to each source, in front of the person who asked for it. This changes behavior faster than any policy.

And the second-order cost is worse than the invoice. More data means more dashboards, more places to look — and longer to find the one thing that mattered. You pay twice: once in storage, once in attention during an incident.

The goal isn't less monitoring. It's monitoring you would defend line by line.

Collecting more is easy. Deciding what not to collect is the engineering.

What's on your monitoring bill that nobody has queried this year?

#Observability #NetworkOperations #NetOps
