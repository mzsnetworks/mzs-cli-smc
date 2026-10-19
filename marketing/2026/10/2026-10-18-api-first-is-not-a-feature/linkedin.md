# LinkedIn — api-first-is-not-a-feature


"It has an API" is on every datasheet and tells you almost nothing about whether you can automate against it.

We find out the real answer during integration work, usually in the first week, and it is worth knowing before the purchase rather than after.

Four things decide it.

Whether it writes, or only reads. A read-only API gives you reporting. It does not give you provisioning, and the difference is the entire business case for a lot of projects. Vendors are rarely explicit about which operations are exposed.

Whether it does bulk. An endpoint that handles one object per call is a different tool than one that takes a batch. At four hundred objects with a rate limit, per-object calls turn a maintenance task into an overnight job, and the retry logic you now have to write is where the bugs live.

Whether the errors are usable. A failure that returns a specific reason can be handled automatically. One that returns a generic failure with a 200 status needs a human to interpret it, which means the automation stops being unattended.

Whether it is versioned, and what happens on upgrade. An API that changes shape without notice turns every platform upgrade into an automation outage you find out about afterwards.

None of this requires a long evaluation. It requires asking for credentials to a test instance and spending two days writing against it in Python before the contract is signed, rather than discovering it in month two of a project that was scoped assuming it would work.

An API is a product surface, and it has a quality. Treat it as something to evaluate, not something to assume.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #APIIntegration
