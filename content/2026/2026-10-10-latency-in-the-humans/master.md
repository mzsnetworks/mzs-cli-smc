# Master — latency-in-the-humans

**Preset:** Professional (LinkedIn personal profile + Instagram @mzsnetworks)
**Date:** 2026-10-10
**Thesis:** We estimate the technical work carefully and the waiting not at all. A four-hour fix becomes three weeks because of six queues nobody put in the plan. Human latency is the estimate, and it is the part you can actually manage.
**Pillar:** Engineering Systems
**Source:** ideas-2026-08-27 #35
**Stats:** none. Judgment and practice only; no statistic stated as fact.

---

Half of this job is waiting, and none of our planning accounts for it.

TAC callback. Maintenance window. RMA in transit. The change board that meets Thursday. Access that needs approval from someone on leave. A vendor confirming a license entitlement.

We estimate the technical work carefully. Four hours. And we are usually right about it. Then the thing takes three weeks, and everyone treats that as an estimating failure when it was an estimate of the wrong quantity.

The four hours was accurate. What nobody counted was six handoffs, each with a queue in front of it.

The queue is not a rounding error. It is most of the duration.

Three things help, and none of them is working faster.

Name the waits in the estimate. Not "four hours of work" but "four hours of work across roughly two weeks, because of the change board and the RMA." That is a different conversation, and it is an honest one. It also makes the queue visible to the person who can shorten it.

Start the clock early on anything with a queue. Raise the access request, open the TAC case, lower the DNS TTL, order the spare, before you need any of them. The wait runs in the background or it runs in the middle of your outage. Same wait, different position.

Run the waits in parallel. Most plans serialize them by accident, because each step is written as though the previous one must finish first. Usually only one or two of them genuinely must.

And waiting is not idle. It is where you write the rollback, stage the config, test it against a model, brief the person taking the next shift. The best engineers I have worked with are not faster at the work. They are doing the next step during the wait for the current one.

The work is fast. The queue is not. Estimate the queue.
