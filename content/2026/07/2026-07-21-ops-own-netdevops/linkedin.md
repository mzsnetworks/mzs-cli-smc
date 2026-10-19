NetDevOps doesn't fail because the tooling is bad. It fails because the wrong people own it.

The common pattern: a separate automation team — or a platform team, or one keen engineer — builds the pipelines. They're good at code. They write the playbooks, the desired-state models, the CI. Then they hand it to operations to run.

And it slowly rots.

Not because ops is resistant. Because the people who wrote the automation don't carry its consequences. They don't get the 3am page when it does the wrong thing. They didn't know about the exception on the third floor, the vendor quirk, the "temporary" workaround that's load-bearing. They encoded the network they were told about — not the one operations actually runs.

Automation written by people who don't operate the network is a set of assumptions someone else has to live with.

NetDevOps works when the operations team owns the automation. Not "is consulted." Owns it. Writes it, breaks it, fixes it, carries the pager for it. Because the moment the author and the operator are the same people, the whole thing aligns: the definition of done matches reality, the edge cases are already known, and trust isn't a handoff problem — it's self-interest. Nobody ships fragile automation they personally have to babysit at 3am.

This is why the org chart matters more than the tool choice. You can buy the best platform on the market and it still rots if it lives outside the team that runs the network. A team that owns its own automation will make even mediocre tooling work — because they feel every gap immediately.

NetDevOps isn't a tooling transformation. It's an ownership one. The tools were never the hard part. Who carries the consequences always was.

Give the automation to the people who get paged. That's the whole strategy.

Who owns your automation — the people who wrote it, or the people who live with it?

#NetDevOps #NetworkAutomation #NetworkOperations
