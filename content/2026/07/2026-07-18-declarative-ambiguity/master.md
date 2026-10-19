# Declarative Models Don't Fix Ambiguity

**Thesis:** Declarative tooling doesn't remove ambiguity — it moves it from the conversation into the model, and then enforces whatever intent got committed, even when that intent is incomplete or wrong.
**Pillars:** Network Automation · Engineering Systems · Brownfield Engineering
**Defended opinion:** Explicit isn't the same as agreed; enforceable isn't the same as right.
**Stats:** none (judgment/experience post) → Factcheck clean.

---

Declarative config was supposed to end the arguments. It just moved them.

The pitch is clean: stop writing steps, write desired state. The model becomes the source of truth — no procedural drift, no "what order did we run those in." Terraform, intent-based networking, desired-state YAML. Describe the what, let the engine handle the how.

But "desired state" is still a human definition. And humans don't agree on it.

Two engineers picture the same network differently. One's desired state includes the management VLAN, strict ACLs, a specific OSPF cost. The other's doesn't. Declarative tooling doesn't reconcile those two pictures — it takes whichever one got committed and makes it the truth. The disagreement wasn't resolved. It got compressed into a file, where nobody notices they read it differently.

The ambiguity didn't leave. It moved from the conversation into the model.

And there's a second gap. Declarative assumes the model maps cleanly to reality. Brownfield doesn't. The model says "desired state"; production has ten years of exceptions the model never captured. When they diverge, the tool doesn't ask which one is right — it enforces the model. Confidently. Even when the model is the thing that's wrong.

That's the part that bites: a declarative engine is only as correct as the intent you fed it. Feed it an ambiguous or incomplete intent and it doesn't surface the ambiguity — it executes it faster and calls the result "converged."

Declarative is a real improvement. It makes intent explicit and enforceable. But explicit isn't the same as agreed, and enforceable isn't the same as right.

A declarative model doesn't remove ambiguity. It just makes you write it down — and then enforces whatever you wrote.

Where does your "desired state" quietly mean something different to each engineer who owns it?

#NetworkAutomation #NetDevOps #InfrastructureAsCode
