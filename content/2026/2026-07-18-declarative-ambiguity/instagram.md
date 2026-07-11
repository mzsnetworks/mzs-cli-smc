Declarative config was supposed to end the arguments. It just moved them. 📐

The pitch: stop writing steps, write desired state. The model becomes the source of truth.

But "desired state" is still a human definition. And humans don't agree on it.

Two engineers picture the same network differently:
→ one's state has the mgmt VLAN, strict ACLs, a set OSPF cost
→ the other's doesn't

Declarative tooling doesn't reconcile them. It takes whichever got committed and makes it the truth ⚙️

The ambiguity didn't leave. It moved from the conversation into the model.

Second gap: the model assumes it maps cleanly to reality. Brownfield doesn't. Production has ten years of exceptions the model never captured — and the engine enforces the model anyway. Confidently. Even when the model is what's wrong.

A declarative engine is only as correct as the intent you fed it.

Explicit isn't the same as agreed. Enforceable isn't the same as right.

Where does your "desired state" quietly mean something different to each engineer who owns it? 👇

#NetworkAutomation #NetDevOps #InfrastructureAsCode #IaC #Netops
