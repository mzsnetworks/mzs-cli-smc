# Instagram — failover-worked-app-didnt-follow


The failover worked perfectly. 🔄 The application never followed.

The circuit drops. The secondary path takes over in under a second. The routing table is exactly right.

The service is still down.

→ A connection pool holding sessions to a dead address
→ DNS serving a cached record
→ A health check that only proves the process is alive
→ A licensing server nobody remembers

⚠️ None of it is a network fault. All of it is your outage.

Failover gets tested at the layer that's easy to test. Drop a link, watch routes converge. Real test — just not the one the business is asking about.

Site resilience without dependency mapping is a rehearsal for half the play. 🎭

When you last tested failover, did anyone try to use the application?

#NetworkEngineering #NetOps #Resilience #Infrastructure #DisasterRecovery

---

## Carousel slide ideas

1. **Cover** — "The failover worked perfectly. The application *never followed*."
2. **What you proved** — Circuit drops. Secondary takes over in under a second. Routing table exactly right.
3. **What was still true** — The service is down.
4. **The connection pool** — Holding sessions to an address that no longer answers. Won't retry for four minutes.
5. **DNS** — Handing out a cached record with a ten-minute TTL.
6. **The health check** — Passes. It only tests whether the process is alive.
7. **The licensing server** — Nobody remembers it. Reachable from the primary path, not the secondary.
8. **The uncomfortable part** — None of it is a network fault. All of it is your outage.
9. **Test the whole path** — Fail the link, then run a real transaction. Time until it *works*, not until the route appears.
10. **CTA** — "Resilience without dependency mapping is a rehearsal for *half the play*."
