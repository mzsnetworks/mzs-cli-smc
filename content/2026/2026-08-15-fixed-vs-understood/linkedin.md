# LinkedIn — fixed-vs-understood

We "fixed" it by rebooting. The ticket closed. The problem didn't.

An intermittent issue, users complaining, pressure building. Reboot the device — everything clears. Metrics green, users quiet. Ticket resolved: "rebooted, service restored."

Three weeks later: same symptom, same device, worse timing.

Of course it came back. We hadn't fixed anything. We'd reset the evidence.

Fixed and understood are different states. Fixed means the symptom is gone right now. Understood means you can say why it happened, why the remediation works, and what conditions bring it back. Only the second one prevents the sequel.

And here's the uncomfortable mechanism: the reboot destroyed the crime scene. The leaking process, the exhausted table, the stuck queue — whatever was accumulating toward failure lived in the state we just cleared. We traded the diagnosis for uptime.

Sometimes that's the right trade. Restore service first — that is the job. Users don't wait for root cause.

But "restore first" comes with a debt. Capture before you clear: logs off-box, counters snapshotted, a show tech saved — whatever the platform gives you. And after service is back, the ticket isn't done; it's split. One part closed: service restored. One part open: cause unknown, recurrence expected, capture armed for next time.

A ticket that says "resolved: rebooted" isn't a resolution. It's a scheduled reopening.

Fixed closes tickets. Understood closes causes.

What's the issue in your network that's currently on its third "fix"?

#NetworkEngineering #Troubleshooting #LessonsFromProduction
