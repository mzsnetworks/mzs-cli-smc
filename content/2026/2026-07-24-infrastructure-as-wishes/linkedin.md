Your IaC repo isn't infrastructure-as-code if the network still drifts. It's infrastructure-as-wishes.

Here's the test nobody wants to run. Go to your source of truth — the Terraform, the NetBox, the YAML — and compare it, line by line, to what's actually running in production tonight. If they don't match, you don't have infrastructure-as-code. You have a hopeful description of infrastructure, stored in Git.

The repo isn't the source of truth because you named the folder that way. It's the source of truth only if the network can't diverge from it without being caught and corrected.

And networks diverge constantly. The 3am out-of-band CLI fix that saved the outage and never made it back to the repo. The "quick" console change during a maintenance window. The vendor default that quietly reasserts itself after a reboot. Every one of those is drift — a place where reality and the repo disagree, and reality wins.

Without drift detection, you never even know it happened. Your repo keeps describing a network that no longer exists, with total confidence. You plan the next change against it, the plan is wrong, and you find out in production. The IaC didn't prevent that outage. It caused it, by lying to you convincingly.

Real infrastructure-as-code needs two things most "IaC" setups skip: detection that continuously compares intended state to actual state, and enforcement that either reverts the drift or forces it back through the repo. If someone can change the network and the repo doesn't notice, the repo is documentation — and documentation drifts.

The repo being version-controlled was never the point. The repo being true is the point. Enforcement is what makes it true.

Until then, you don't have infrastructure-as-code. You have a wish list with good syntax highlighting.

Is your IaC repo enforced — or is it just the most confident lie in your toolchain?

#InfrastructureAsCode #NetDevOps #NetworkAutomation
