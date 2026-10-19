# Instagram — ttls-are-a-plan


DNS TTLs are a migration plan. 🕐 Most people treat them as a setting.

The record says 86400 because it always has, and nobody's had a reason to look.

Then a cutover gets scheduled. The change goes in perfectly at 2am. And traffic keeps arriving at the old address all day — because that's what you told the world to do. ⚠️

What makes it frustrating is that nothing failed. Everything worked exactly as configured. The resolvers are doing what you asked.

You just asked a week ago, and your plan assumed you were asking now.

So the TTL change is the first step of the migration, not part of it.

Lower it well before the window — far enough ahead that every cached copy has expired on its own terms. If the record is at a day, you need more than a day: somebody's resolver started its clock before you made the change. ⚙️

Two things worth checking alongside it:

→ Some resolvers don't honor low TTLs the way you expect, especially on consumer and mobile networks. Plan for a tail
→ Applications cache resolution themselves, often for the life of a process. A service running three weeks may not re-resolve until something restarts it

A cutover where you control the timing is a maintenance window.

A cutover where the resolvers control the timing is an afternoon of unexplained traffic.

How far ahead do you drop TTLs?

#NetworkEngineering #NetOps #DNS #ITOperations #Infrastructure
