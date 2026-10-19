# Instagram — the-mtu-week

The MTU problem took a week. It deserved about an hour. ⏳

What made it expensive wasn't difficulty.

It was the symptom — the worst kind: some things worked and some things hung. ⚙️

→ small requests, fine
→ pings, fine (of course — they're tiny)
→ logins, fine
→ a file transfer stalling at exactly the same point every time
→ a page loading its HTML and never finishing its assets
→ a database connection opening cleanly, then freezing on the first large result set

Every one of those looks like an application problem.

That's the trap.

When "the network is down," nobody argues about where to look.

When the network is up and only some operations hang, the investigation goes to the application team by default — and days pass in a place where the answer isn't.

The tell I now recognize immediately:

small works, large hangs, reproducible at a consistent size.

That combination is a path MTU story until proven otherwise. It takes minutes to check with a ping that sets the do-not-fragment bit and walks the size down until it stops getting through.

Underneath, it's usually one of a short list:

→ a tunnel added encapsulation overhead and nobody adjusted for it
→ a firewall or ACL is dropping the ICMP that path MTU discovery depends on, so the sender never learns to send smaller
→ two ends of a link disagree about jumbo frames

That second one is the cruel one. The mechanism designed to fix this, silently disabled by a rule written years ago for good reasons.

But the real lesson isn't about MTU.

It's that "some things work" is a stronger clue than "nothing works" — and we treat it as a weaker one.

Total failure narrows the search immediately. Partial failure feels ambiguous, so it gets escalated slowly, described vaguely, and handed between teams who each confirm their part is fine.

It was fine. Everybody's part was fine.

The path between them had an opinion about size that nobody had asked about.

Now when somebody says "it's mostly working," I hear a size question. 👇

#Troubleshooting #NetworkEngineering #NetOps #Networking #ITInfrastructure
