# X — firewall-rule-nobody-deletes

## Single (publish this)

Nobody has ever been promoted for deleting a firewall rule.

Adding one closes a ticket. Deleting one risks breaking something nobody remembers.

One action has upside, the other only downside. That's why rule bases only grow.

#NetworkSecurity #NetOps

## Thread (alternate)

1/ Nobody has ever been promoted for deleting a firewall rule. That one fact explains almost every rule base we're handed. 🧵

2/ Adding a rule solves a visible problem today. Somebody is unblocked, the ticket closes, a person says thank you.

3/ Deleting a rule solves nothing anyone can see, and carries a small chance of breaking something nobody remembers depends on it. One action has upside. The other has only downside.

4/ So rule bases become archaeology. You can date the layers:
• the "temporary" any/any from a migration
• a vendor rule for a product decommissioned in 2024
• rules for a subnet that no longer exists
• four near-identical rules by four people

5/ The real cost isn't clutter. It's that nobody can answer what is actually allowed here.

6/ And once nobody can read it, nobody can safely change it — so the next engineer does the only safe thing available and adds another rule.

7/ The fix isn't a cleanup project. Those fail because they're one-time and terrifying. Make deletion boring instead:
• hit counters as a candidate list
• disable and watch, don't delete and hope
• owner + review date at creation
• expiry by default on incident rules

8/ Adding a rule is a ticket. Deleting one is a risk. Until that changes, your rule base only grows. #NetworkSecurity #NetOps
