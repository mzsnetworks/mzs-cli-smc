# X — supportable-at-3am

## Single (publish this)

At 3am nobody is clever. You only have what you decided in daylight:

• consistent naming
• one source of truth
• out-of-band that actually works
• backups someone has restored
• one named owner per system

None of them are products.

#NetOps #NetworkEngineering

## Thread (alternate)

1/ Five things make a network supportable at 3am. None of them are products. 🧵

2/ Consistent naming. Not aesthetics — an index. bld2-idf3-sw01 tells you which building to walk to. switch-new-2 costs four minutes on a bridge call while somebody scrolls.

3/ One source of truth. When two systems disagree about which VLAN a port is in, which wins — and does everyone already know? If the answer is "check with Dave," Dave is your source of truth. Dave is asleep.

4/ Out-of-band that actually works. A console server nobody has touched since install isn't OOB, it's a story about OOB. Can you reach a console while the uplink is down, without transiting the thing that's broken?

5/ The most common OOB failure we find is circular — the out-of-band path runs over production.

6/ Backups someone has restored. A green checkmark is an unverified claim. The backup is rarely the problem. The restore is — it wants a license file, a matching version, or a step nobody wrote down.

7/ One named owner per system, reachable another way. Not a team alias. "Escalate to Network" is a queue, not an owner. An owner decides at 3:20am whether we roll back.

8/ At 3am nobody is clever. You only have what you wrote down while it was daylight. #NetOps #NetworkEngineering
