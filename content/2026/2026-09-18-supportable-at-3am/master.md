# Master — supportable-at-3am

**Preset:** Business (MZS company account — LI page, FB, IG, X)
**Date:** 2026-09-18 (Fri)
**Source idea:** ideas-2026-08-09 #10 (ES · Listicle)
**Thesis:** Supportability isn't a product. It's five decisions made in daylight that decide how the 3am call goes.
**Note:** item 5 overlaps `outsourcing-isnt-accountability` (2026-09-11) on the word "owner" — scoped here to per-system ops ownership and reachability during an outage, not contractual accountability.
**Stats:** none — judgment/listicle post, no factcheck gate.

---

Five things make a network supportable at 3am. None of them are products.

**1. Consistent naming.**
Not aesthetics — an index. At 3am you type the name before you think. `bld2-idf3-sw01` tells you which building to walk to. `switch-new-2` tells you nothing and costs four minutes on a bridge call while somebody scrolls. Naming is the key that joins monitoring, backups, DNS, and the runbook to the same device.

**2. One source of truth.**
Not five spreadsheets that disagree politely. The real test: when two systems disagree about which VLAN a port is in, which one wins — and does everyone already know the answer? If the answer is "check with Dave," then Dave is your source of truth, and Dave is asleep.

**3. Out-of-band that actually works.**
A console server nobody has touched since installation isn't out-of-band. It's a story about out-of-band. The test is specific: can you reach a device's console while its uplink is down, from home, without transiting the thing that's broken? The most common failure we find is circular — the OOB path runs over production.

**4. Backups someone has restored.**
A green checkmark on a backup job is an unverified claim. Restore one config onto a spare device this quarter and watch what happens. The backup is rarely the problem. The restore is — it wants a license file, a matching version, or a step nobody wrote down.

**5. One named owner per system, reachable another way.**
Not a team alias. A person, and a path to that person that doesn't depend on the system that's down. "Escalate to Network" is a queue, not an owner. An owner is who decides at 3:20am whether we roll back.

That's the list. Every item is unglamorous, none of them appear in a design review, and all five are decided long before the night they matter.

At 3am nobody is clever. You only have what you wrote down while it was daylight.

Which of the five would your environment fail tonight?
