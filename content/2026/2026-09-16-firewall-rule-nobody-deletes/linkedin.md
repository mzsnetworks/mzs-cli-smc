# LinkedIn — firewall-rule-nobody-deletes


Nobody has ever been promoted for deleting a firewall rule.

That single fact explains almost every rule base we're handed.

Adding a rule solves a visible problem today. Somebody is unblocked, the ticket closes, and a person says thank you. Deleting a rule solves nothing anyone can see, and carries a small chance of breaking something nobody remembers depends on it. One action has upside. The other has only downside. Rule bases grow the way water runs downhill.

So they become archaeology. You can date the layers.

→ The permit any/any from a migration, added "temporarily"
→ A vendor rule for a product decommissioned two years ago, permitting inbound to nothing
→ Rules referencing a subnet that no longer exists
→ Four near-identical rules written by four different people who each didn't trust the existing three

The real cost isn't clutter. It's that nobody can answer the question the rule base exists to answer: what is actually allowed here? And once nobody can read it, nobody can safely change it — so the next engineer does the only safe thing available: adds another rule.

The fix is not a cleanup project. Those fail because they're one-time, unfunded, and terrifying. What works is making deletion evidenced and boring:

→ Hit counters as a candidate list. Zero hits in ninety days is a question, not a verdict.
→ Disable and watch, rather than delete and hope. A disabled rule can be re-enabled in ten seconds. A deleted one gets rebuilt from memory at 3am.
→ An owner and a review date on every new rule, captured at creation — the only moment anybody knows why.
→ Expiry by default on anything opened during an incident. Temporary should mean temporary in the config, not the intention.

None of that is a product. It's a decision to make removal as normal as addition.

Adding a rule is a ticket. Deleting one is a risk. Until that changes, your rule base only grows.

Which rule in your environment is everyone quietly scared to touch?

#NetworkSecurity #FirewallManagement #NetOps
