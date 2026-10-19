# Instagram — oob-is-decoration


Out-of-band access you've never tested is decoration. 🔌

It looks like insurance on the diagram. It sits in the rack. It costs money every year. Everybody points at it during the design review.

Then the day comes, and you find it depends on the thing that's down. ⚠️

The patterns repeat:

→ The console server is reachable only across the production WAN — the thing that failed
→ The cellular modem has a SIM that was never activated, or got canceled in a procurement tidy-up nobody mentioned
→ The jump host authenticates against the directory on the other side of the outage
→ The credentials live in a password manager that needs the VPN

None of these are design errors in the usual sense. Each was a reasonable decision made in isolation.

The dependency only exists when you look at the whole path under the one condition where you need it — and that's the condition nobody simulates. ⚙️

So the test isn't "can I reach the console server."

It's: take the primary path away, deliberately, then try to get in. From somewhere other than the office. With the person who'd actually be doing it at 3am.

What you find usually isn't that out-of-band is broken. It's that one link quietly assumed the network was up.

An afternoon, once a year.

When did you last reach a device with the primary path deliberately down?

#NetworkEngineering #NetOps #ITOperations #Resilience #Infrastructure
