## Single post (publish-ready)

Your IaC repo isn't infrastructure-as-code if the network still drifts. It's infrastructure-as-wishes.

Without drift detection, it describes a network that no longer exists — with total confidence. Version-controlled was never the point. True is.

#NetDevOps

---

## Thread option

1/ Your IaC repo isn't infrastructure-as-code if the network still drifts. It's infrastructure-as-wishes. 🧵

2/ The test nobody runs: compare your source of truth — Terraform, NetBox, YAML — line by line to what's running tonight. If they don't match, you don't have IaC. You have a hopeful description of infrastructure, stored in Git.

3/ Networks drift constantly:
• the 3am out-of-band CLI fix that never made it back
• the "quick" console change
• the vendor default that reasserts after a reboot

4/ Without detection, the repo keeps describing a network that no longer exists — with total confidence. You plan against it, and find out it's wrong in production.

5/ Real IaC needs detection + enforcement. Version-controlled was never the point. The repo being true is.

Is yours enforced, or the most confident lie in your toolchain?

#InfrastructureAsCode #NetDevOps
