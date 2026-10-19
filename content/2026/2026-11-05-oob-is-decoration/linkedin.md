# LinkedIn — oob-is-decoration


Out-of-band access you have never tested is decoration.

It looks like insurance on the diagram. It sits in the rack, it costs money every year, and everybody points at it during the design review. Then the day comes when you need it, and you discover it depends on the thing that is down.

The patterns repeat. The console server is reachable only across the production WAN, which is the thing that failed. The cellular modem has a SIM that was never activated, or was activated and has since been canceled by a procurement tidy-up nobody told you about. The jump host authenticates against the directory that is on the other side of the outage. The credentials live in a password manager that requires the VPN.

None of these are design errors in the usual sense. Each one was a reasonable decision made in isolation, and the dependency only exists when you look at the whole path under the specific condition where you need it.

That condition is the only one that matters, and it is the one nobody simulates.

So the test is not "can I reach the console server." It is: take the primary path away, deliberately, and then try to get in. Do it from somewhere other than the office. Do it with the person who would actually be doing it at 3am, not the person who built it.

What you find is usually not that out-of-band is broken. It is that one link in the chain quietly assumed the network was up, and until you removed the network nobody could see it.

This is cheap. It takes an afternoon, once a year, and it converts a line item into something you can rely on.

The alternative is finding out during the outage, which is also a test, just an expensive one with an audience.

When did you last reach a device with the primary path deliberately down?

#NetworkEngineering #NetOps #ITOperations
