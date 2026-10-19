# X — failover-worked-app-didnt-follow


## Single (publish this)

The failover worked perfectly and the application never followed.

The network recovered. The connection pool, the cached DNS record, and the licensing server nobody remembers did not.

None of it is a network fault. All of it is your outage.

#NetOps #Resilience

---

## Thread

1/ The failover worked perfectly and the application never followed.

Everyone has seen this once. 🧵

2/ The circuit drops. The secondary path takes over in under a second. The routing table is exactly right.

The service is still down.

The network team can prove they did their job. The business is still offline.

3/ What happened is that the network recovered and the things sitting on top of it did not.

4/ • A connection pool holding sessions to an address that no longer answers, and won't retry for four minutes
• DNS handing out a cached record with a ten-minute TTL
• A health check that only proves the process is alive

5/ • A licensing server nobody remembers, reachable from the primary path and not the secondary

None of that is a network fault.

All of it is your outage.

6/ It keeps happening because failover gets tested at the layer that's easy to test.

Drop a link on a Tuesday evening, watch the routes converge. That's a real test of a real thing. It just isn't what the business is asking about.

7/ Fail the link, then confirm the service — a real transaction, run by someone who'd notice if it were wrong.

Time how long until it works, not until the route appears.

Resilience without dependency mapping is a rehearsal for half the play.

#NetOps #Resilience
