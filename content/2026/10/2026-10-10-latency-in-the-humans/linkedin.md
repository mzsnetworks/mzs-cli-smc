# LinkedIn — latency-in-the-humans


Half of this job is waiting, and none of our planning accounts for it.

TAC callback. Maintenance window. RMA in transit. The change board that meets Thursday. Access that needs approval from someone on leave. A vendor confirming a license entitlement.

We estimate the technical work carefully. Four hours. And we are usually right about it. Then the thing takes three weeks, and everyone treats that as an estimating failure when it was an estimate of the wrong quantity.

The four hours was accurate. What nobody counted was six handoffs, each with a queue in front of it.

The queue is not a rounding error. It is most of the duration.

Three things help, and none of them is working faster.

Name the waits in the estimate. Not "four hours of work" but "four hours across roughly two weeks, because of the change board and the RMA." That is a different conversation, and an honest one. It also makes the queue visible to whoever can shorten it.

Start the clock early on anything with a queue. Raise the access request, open the TAC case, lower the DNS TTL, order the spare, before you need any of them. The wait runs in the background or it runs in the middle of your outage. Same wait, different position.

Run the waits in parallel. Most plans serialize them by accident, because each step is written as though the one before it must finish first. Usually only one or two genuinely must.

And waiting is not idle. It is where you write the rollback, stage the config, brief whoever takes the next shift. The best engineers I have worked with are not faster at the work. They are doing the next step during the wait for the current one.

The work is fast. The queue is not. Estimate the queue.

What is the longest you have waited on something that took ten minutes to fix?

#NetworkEngineering #EngineeringCulture #ITOperations
