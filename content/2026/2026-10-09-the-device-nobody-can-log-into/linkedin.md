# LinkedIn — the-device-nobody-can-log-into


Every environment we inherit has one device nobody can log into.

It is never the least important one.

It is the core switch in the oldest building, or the firewall in front of the thing finance uses on the last day of the month. The person who built it left in 2019. The credentials were in a password manager that got migrated once, or in a text file on a laptop that was returned, or in someone's head.

And it works. That is the part that is hardest to explain to a board. It has been forwarding traffic for six years without a complaint, which is exactly why nobody ever had a reason to open it.

Here is what that device actually tells you, and it is not a story about passwords.

It tells you there was a point where operational ownership stopped transferring. Somebody left, the runbook did not exist, and the gap stayed open because nothing broke. Credentials are just the first symptom visible from outside. Underneath it, the same gap usually covers the change history nobody can reconstruct, the config that was never backed up, and the one dependency only that person understood.

Which is why "get into the device" is the wrong goal. It is a ticket, not a fix.

The real work is narrower than an audit and more useful. Find every device where the last known change predates the current team. Confirm you can recover each one from backup onto replacement hardware, because a config you cannot restore is a souvenir. Then write down who owns each system now, by name, and make that list something a leaver's checklist actually touches.

The device nobody can log into is not your risk. It is your notification that the risk exists — and it is the only one that raised its hand.

What would it take to find the other three?

#NetworkEngineering #NetOps #TechnicalDebt
