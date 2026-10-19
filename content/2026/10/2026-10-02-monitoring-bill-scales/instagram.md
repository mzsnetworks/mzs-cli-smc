# Instagram — monitoring-bill-scales

Your monitoring bill scales with data. Your understanding doesn't. 📊

Every device you add. Every metric you enable. Every month of retention you extend.

All of it costs more. None of it automatically tells you anything you didn't already know. ⚙️

Those two curves separate quietly, and nobody is assigned to watch the gap.

Most of the growth was never a decision:

→ the default polling interval applied to several thousand interfaces, because that's what the template did
→ retention set at the maximum on day one, in case
→ debug logging switched on during an investigation in 2023 and never switched off
→ a per-host agent that made sense on twelve servers, now running on workloads that live nine minutes

Here's the uncomfortable test.

Take any metric you're paying to store and ask when it last changed a decision.

Not when it was last displayed. When it last changed what somebody did.

For most of what we find, nobody can answer.

What we do about it:

📍 Tier retention by the question, not the source. Thirty days at full resolution answers "what happened last Tuesday." Capacity trends need two years, not per-second detail.

📍 Sample the high-cardinality things instead of storing every instance.

📍 Turn off collection nobody has queried in a year. You can turn it back on — and the fear of needing it is doing more work than the data is.

📍 Put a cost figure next to each source, in front of whoever asked for it. That changes behavior faster than any policy.

And the second-order cost is worse than the invoice. More data means more dashboards and more places to look — so it takes longer to find the one thing that mattered.

You pay twice. Once in storage, once in attention during an incident.

Collecting more is easy. Deciding what not to collect is the engineering.

What has nobody queried this year? 👇

#Observability #NetworkOperations #NetOps #Networking #ITInfrastructure
