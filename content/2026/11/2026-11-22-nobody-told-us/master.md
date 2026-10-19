# Master — nobody-told-us

**Preset:** Business (LinkedIn company page + Facebook + Instagram + X, all on the MZS account)
**Date:** 2026-11-22
**Thesis:** The outages that look unexplained usually began as a correct change in another team, made without reaching the people whose assumptions depended on the old state. Change processes are built to prove authorization and almost never to guarantee announcement, so the damage lands at the boundary between teams.
**Pillar:** Lessons from Production
**Source:** ideas-2026-08-30 #32
**Stats:** none. The four incidents are composite field patterns, not counted or attributed events, and no figure is stated as a measurement.

---

Four of the worst outages we have been called into had nothing to do with the network.

Every one of them started with a change somebody made without telling anyone who would have to live with it.

A security team pushed a certificate update on a Friday. Correct change, properly tested, entirely within their remit. It replaced a certificate that a monitoring system had been pinning for three years, so every probe started failing at once and the network team spent the evening investigating an outage that was not happening.

A facilities contractor relabelled a patch field during an office move. Nothing electrical changed. But the labels were the only map anyone had, so the next person to trace a circuit traced the wrong one and took down a floor to fix a fault that was somewhere else entirely.

An application team enabled compression on a replication job to be helpful. Traffic volume dropped and the pattern changed completely, which tripped a threshold that had been tuned to the old shape, and the alerting went quiet for the thing it was actually there to catch.

A vendor pushed firmware through a support portal during a routine case, without the maintenance window anybody would have asked for.

None of these people were careless. Each change was reasonable inside the team that made it. The damage happened at the boundary, where one team's correct decision met another team's undocumented assumption.

Which is why we ask, on every assessment, who else finds out when you change something. Not who approves it. Who is told.

Most change processes are built to prove a change was authorized. Very few make sure it was announced.

Your last unexplained outage may not have been unexplained. It may have been somebody else's Tuesday.

Who finds out when you change something?
