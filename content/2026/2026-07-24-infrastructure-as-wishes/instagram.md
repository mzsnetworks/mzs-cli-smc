Your IaC repo isn't infrastructure-as-code if the network still drifts. It's infrastructure-as-wishes. 🪄

The test nobody runs: compare your source of truth — Terraform, NetBox, YAML — line by line to what's actually running tonight. If they don't match, you don't have IaC. You have a hopeful description of infrastructure, stored in Git.

Networks diverge constantly:
→ the 3am out-of-band CLI fix that never made it back
→ the "quick" console change in a maintenance window
→ the vendor default that reasserts after a reboot

That's drift. And without detection, you never know it happened ⚙️

Your repo keeps describing a network that no longer exists, with total confidence. You plan the next change against it, and find out it's wrong in production.

Real IaC needs two things most setups skip: detection that compares intended vs actual state, and enforcement that reverts the drift or forces it back through the repo.

The repo being version-controlled was never the point. The repo being true is.

Is your IaC enforced — or the most confident lie in your toolchain? 👇

#InfrastructureAsCode #NetDevOps #NetworkAutomation #IaC #Netops
