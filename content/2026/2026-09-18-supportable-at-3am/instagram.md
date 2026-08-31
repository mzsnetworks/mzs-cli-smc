# Instagram — supportable-at-3am

Five things make a network supportable at 3am. 🌙

None of them are products.

1️⃣ Consistent naming

Not aesthetics — an index. At 3am you type the name before you think.

bld2-idf3-sw01 tells you which building to walk to. switch-new-2 tells you nothing and costs four minutes while somebody scrolls.

2️⃣ One source of truth

Not five spreadsheets that disagree politely.

The test: when two systems disagree about which VLAN a port is in, which one wins — and does everyone already know?

If the answer is "check with Dave," Dave is your source of truth. And Dave is asleep. ⚙️

3️⃣ Out-of-band that actually works

A console server nobody has touched since install isn't out-of-band. It's a story about out-of-band.

Can you reach a console while its uplink is down, from home, without transiting the thing that's broken?

The most common failure we find is circular — the OOB path runs over production.

4️⃣ Backups someone has restored

A green checkmark is an unverified claim.

Restore one config onto a spare device this quarter. The backup is rarely the problem — the restore is. It wants a license file, a matching version, or a step nobody wrote down.

5️⃣ One named owner per system, reachable another way

Not a team alias. A person, and a path to them that doesn't depend on the system that's down.

"Escalate to Network" is a queue, not an owner.

None of these appear in a design review. All five are decided long before the night they matter.

At 3am nobody is clever. You only have what you wrote down while it was daylight.

Which one would you fail tonight? 👇

#NetworkOperations #NetOps #ITInfrastructure #NetworkEngineering #Networking
