# Master — resilience-isnt-redundancy

**Idea:** ideas-2026-07-11 #3 (ENO · Contrarian) — Resilience isn't redundancy. Two of everything and still down, because the failover was never tested.
**Preset:** Business (all four on the MZS account) — company voice "we"
**Publish date:** 2026-08-14
**Stat gate:** none — no numeric claims.

---

Resilience isn't redundancy. You can own two of everything and still go down.

We've walked into plenty of environments with dual supervisors, dual uplinks, dual power, dual ISPs. On paper: unbreakable. Then a primary actually fails — and the failover fires for real, for the first time ever, in production.

That's when the paper meets the network.

Redundancy is a purchase. Resilience is a behavior. Redundancy counts boxes; resilience is what happens in the thirty seconds after something dies — and that depends on things no invoice shows:

Whether the standby's config drifted for two years while nobody looked.
Whether both "diverse" circuits ride the same conduit out of the building.
Whether both power feeds land on the same panel.
Whether the failover timers were ever tuned for your traffic, or left at defaults from the install.
Whether anything — anything at all — has ever actually failed over on purpose.

An untested failover isn't a safety net. It's an unknown. Its failure modes are invisible by design, because the only thing that reveals them is the failure itself. If you've never pulled the primary deliberately, your first test is an outage — scheduled by chance, at the worst possible time, with an audience.

The fix isn't more hardware. It's rehearsal. Fail over on purpose, on a schedule, in a window. Prove independence, not duplication. Measure recovery time, not inventory.

Redundancy is what you buy. Resilience is what you rehearse.

When did your team last fail over on purpose?
