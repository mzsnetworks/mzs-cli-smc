# Master — ttls-are-a-plan

**Preset:** Professional — LinkedIn **personal profile** (no pageId) + Instagram @mzsnetworks
**Date:** 2026-11-07
**Thesis:** A TTL is an instruction issued in the past that governs behavior during the cutover, so lowering it is the first step of a migration rather than part of it. Resolver non-compliance and application-level caching mean the switch has a tail, and the old destination must keep answering until traffic actually stops.
**Pillar:** Engineering Systems
**Source:** ideas-2026-08-27 #22
**Stats:** none. The 86400 is the common default value of a TTL field, not a measurement.

---

DNS TTLs are a migration plan. Most people treat them as a setting.

The record says 86400 because it has always said 86400, and nobody has had a reason to look at it. Then a cutover gets scheduled, the change goes in perfectly at 2am, and traffic keeps arriving at the old address for the rest of the day because that is what you told the world to do.

The thing that makes this frustrating is that it is not a failure. Everything worked exactly as configured. The resolvers are doing what you asked. You just asked a week ago, and your plan assumed you were asking now.

So the TTL change is the first step of the migration, not part of it. Lower it well before the window — far enough ahead that every cached copy of the old value has expired on its own terms. If the record is at a day, you need more than a day of lead time, because the clock on somebody's resolver started before you made the change.

Two things I have learned to check alongside it.

Some resolvers do not honor low TTLs the way you expect, particularly on consumer and mobile networks, so plan for a tail rather than a clean switch. And applications cache resolution themselves, often for the life of a process, which means a service that has been running for three weeks may not re-resolve at all until something restarts it.

The practical version is unglamorous. Lower the TTL a week early, confirm it propagated, do the cutover, and keep the old destination answering until the traffic there actually stops rather than until the TTL says it should have.

A cutover where you control the timing is a maintenance window. A cutover where the resolvers control the timing is an afternoon of unexplained traffic.

How far ahead do you drop TTLs before a cutover?
