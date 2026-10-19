# Master — the-mtu-week

**Preset:** Professional (LinkedIn personal + Instagram @mzsnetworks)
**Date:** 2026-09-29 (Tue)
**Source idea:** ideas-2026-08-27 #26
**Thesis:** MTU problems don't announce themselves. They make some things work and some things hang, which points investigations away from the network.
**Stats:** none — story/craft post, no factcheck gate.

---

The MTU problem took a week, and it deserved about an hour.

What made it expensive wasn't difficulty. It was the symptom, which was the worst kind: some things worked and some things hung.

Small requests were fine. Pings were fine — of course they were, they're tiny. Then a file transfer would stall at exactly the same point every time, or a database connection would open cleanly and freeze on the first large result set.

Every one of those looks like an application problem. That's the trap. When "the network is down," nobody argues about where to look. When the network is up and only some operations hang, the investigation goes to the application team by default, and days pass in a place where the answer isn't.

The tell I now recognize immediately: small works, large hangs, and it's reproducible at a consistent size. That combination is a path MTU story until proven otherwise, and it takes minutes to check: ping with the do-not-fragment bit set, walking the size down until it stops getting through.

Underneath, it's usually one of a short list. A tunnel added encapsulation overhead and nobody adjusted for it. A firewall or an ACL is dropping the ICMP that path MTU discovery depends on, so the sender never learns to send smaller — the mechanism designed to fix this silently disabled by a rule written years ago for good reasons. Or two ends of a link disagree about jumbo frames.

The lesson isn't about MTU. It's that "some things work" is a stronger clue than "nothing works," and we treat it as a weaker one. Total failure narrows the search. Partial failure feels ambiguous — so it gets escalated slowly, described vaguely, and handed between teams who each confirm their part is fine.

It was fine. Everybody's part was fine. The path between them had an opinion about size that nobody had asked about.

Now when somebody says "it's mostly working," I hear a size question before an application question.

What's the longest you've spent on something that turned out to be a number in a header?
