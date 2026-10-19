# Instagram — firewall-rule-nobody-deletes

Nobody has ever been promoted for deleting a firewall rule. 🔒

That one fact explains almost every rule base we're handed.

Adding a rule solves a visible problem today. Somebody is unblocked, the ticket closes, a person says thank you.

Deleting a rule solves nothing anyone can see — and carries a small chance of breaking something nobody remembers depends on it.

One action has upside. The other has only downside.

Rule bases grow for the same reason water runs downhill. ⚙️

So they become archaeology. You can date the layers:

→ the permit any/any from a migration, added "temporarily"
→ a vendor rule for a product decommissioned two years ago
→ rules referencing a subnet that no longer exists
→ four near-identical rules by four people who each didn't trust the other three

The real cost isn't clutter.

It's that nobody can answer the question the rule base exists to answer: what is actually allowed here?

And once nobody can read it, nobody can safely change it — so the next engineer does the only safe thing available and adds another rule.

The fix isn't a cleanup project. Those fail because they're one-time and terrifying.

What works is making deletion boring:

→ hit counters as a candidate list — zero hits in 90 days is a question, not a verdict
→ disable and watch, rather than delete and hope
→ an owner and a review date on every new rule, captured at creation
→ expiry by default on anything opened during an incident

Adding a rule is a ticket. Deleting one is a risk. Until that changes, your rule base only grows.

Which rule is everyone quietly scared to touch? 👇

#NetworkSecurity #FirewallManagement #NetOps #NetworkEngineering #ITInfrastructure
