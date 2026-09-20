# Facebook — failover-worked-app-didnt-follow


The failover worked perfectly and the application never followed.

The circuit drops. The secondary path takes over in under a second. The routing table is exactly right. The service is still down.

The network recovered. The things sitting on top of it did not.

A connection pool holding sessions to an address that no longer answers. DNS serving a cached record. A health check that only proves the process is alive.

None of that is a network fault, and all of it is your outage.

Failover gets tested at the layer that's easy to test — drop a link, watch the routes converge. That isn't the thing the business is asking about.

When you last tested failover, did anyone try to use the application?
