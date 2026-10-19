# LinkedIn — rollback-is-an-acceptance-criterion


Most change records have a rollback plan. Far fewer have a rollback that has ever been executed.

The usual version reads something like "revert to previous configuration." That is a sentence, not a procedure. It does not say where the previous configuration is stored, whether it is the running or the startup config, what happens to the state that accumulated since, or how long the revert takes on a device that needs a reload to apply it.

Under pressure, at 2 AM, that gap is where the outage gets longer instead of shorter.

And the configuration is rarely the hard part. What makes a revert difficult is the state that accumulated while the change was live: sessions established, entries learned, a neighbor that reconverged around the new topology and will now have to reconverge back. A rollback that restores the config and ignores the state is how an outage outlives the fix that caused it.

We treat rollback as an acceptance criterion rather than documentation. An automated change is not finished until the reverse path has been run — against the model first, then in a lab or a canary site — and the time it takes is a known number rather than an estimate.

This sounds like overhead. It is the thing that makes the rest of it fast, because a change you can reliably undo can be approved on its merits instead of on its blast radius. Teams that can revert in minutes approve more changes, not fewer.

The question worth asking about your last automated change: has anyone run the rollback, or does it just exist on paper?

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #InfrastructureAsCode
