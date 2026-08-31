# X — monitoring-bill-scales

## Single (publish this)

Your monitoring bill scales with data. Your understanding doesn't.

Take any metric you pay to store and ask when it last changed a decision — not when it was last displayed.

Collecting more is easy. Deciding what not to collect is the engineering.

#Observability #NetOps

## Thread (alternate)

1/ Your monitoring bill scales with data. Your understanding doesn't. 🧵

2/ Every device added, every metric enabled, every month of retention extended costs more. None of it automatically tells you anything you didn't know. Those curves separate quietly.

3/ Most of the growth was never a decision: default polling on thousands of interfaces, retention at maximum "in case," debug logging left on after an investigation in 2023, a per-host agent now running on nine-minute workloads.

4/ The uncomfortable test: take any metric you pay to store and ask when it last changed a decision. Not when it was displayed — when it changed what somebody did. Mostly, nobody can answer.

5/ What we do:
• tier retention by the question, not the source
• sample high-cardinality data
• turn off anything unqueried for a year
• put a cost figure next to each source, in front of whoever asked

6/ The second-order cost is worse than the invoice. More data means more dashboards and more places to look — so it takes longer to find the one thing that mattered.

7/ You pay twice. Once in storage, once in attention during an incident.

8/ The goal isn't less monitoring. It's monitoring you'd defend line by line. Collecting more is easy; deciding what not to collect is the engineering. #Observability #NetOps
