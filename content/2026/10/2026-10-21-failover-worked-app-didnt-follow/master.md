# Master — failover-worked-app-didnt-follow

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-10-21
**Thesis:** Network failover tests prove the network recovered. They do not prove the service did, because the application's dependencies were never in scope. Resilience is a property of the whole path, and most organizations have only ever tested one layer of it.
**Pillar:** Enterprise Network Operations — resilience
**Source:** ideas-2026-08-30 #5
**Stats:** none. Judgment and field experience only.

---

The failover worked perfectly and the application never followed.

Everyone has seen this once. The circuit drops, the secondary path takes over in under a second, the routing table is exactly right, and the service is still down. The network team can prove they did their job. The business is still offline.

What happened is that the network recovered and the things sitting on top of it did not.

The database connection pool was holding sessions to an address that no longer answers, and it will not retry for another four minutes. DNS is handing out a cached record with a ten-minute TTL. The application's health check passes because it only tests whether the process is alive. A licensing server that nobody remembers is reachable from the primary path and not the secondary.

None of that is a network fault, and all of it is your outage.

The reason it keeps happening is that failover gets tested at the layer that is easy to test. You can drop a link on a Tuesday evening and watch the routes converge, and that is a real test of a real thing. It just is not the thing the business is asking about.

Testing the whole path is harder and more useful. Fail the link and then confirm the service — a real transaction, end to end, by someone who would notice if it were wrong. Time how long until it works, not how long until the route appears. Write down every dependency you discovered on the way, because that list is the actual output of the exercise.

Site resilience without dependency mapping is a rehearsal for half the play. The network knows its lines. Nobody has read the other half.

When you last tested failover, did anyone try to use the application?
