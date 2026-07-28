# Facebook — resilience-isnt-redundancy

Resilience isn't redundancy. You can own two of everything and still go down.

Dual supervisors, dual uplinks, dual ISPs — unbreakable on paper. Then the primary fails, and the failover fires for real, for the first time ever, in production.

Redundancy is a purchase. Resilience is a behavior: the standby that drifted for two years, the "diverse" circuits in the same conduit, timers never tuned, nothing ever failed over on purpose.

An untested failover isn't a safety net — it's an unknown. If you've never pulled the primary deliberately, your first test is an outage.

Redundancy is what you buy. Resilience is what you rehearse.

When did your team last fail over on purpose?
