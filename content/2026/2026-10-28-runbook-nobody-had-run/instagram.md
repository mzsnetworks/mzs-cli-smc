# Instagram — runbook-nobody-had-run


We were asked to automate a site failover runbook. 📄

Version controlled. Reviewed quarterly. Signed off.

What it hadn't been in two years was run.

Tested by reading — which verifies one thing: the document is still readable. 👀

Automating it meant resolving every ambiguity first. Three didn't survive:

→ A step naming a VLAN renumbered 18 months earlier. A person silently corrects that. A script doesn't.
→ Service restarts ordered so the app came up before its database accepted connections.
→ A verification step that checked the interface was up. Not that traffic flowed. Not that the app answered.

⚠️ That last one was the only evidence the runbook asked for.

None of it was found by testing the automation. It was found by writing it.

When did you last run yours, rather than read it?

#NetworkAutomation #NetOps #ITOperations #Infrastructure #DisasterRecovery

---

## Carousel slide ideas

1. Cover — "The runbook nobody had run in *two years*."
2. On paper — Version controlled. Reviewed quarterly. Signed off.
3. The catch — It had been tested by *reading*.
4. What that verifies — That the document is still readable. Nothing else.
5. Why automating it changed things — Every ambiguity has to be resolved before anything runs.
6. Gap 1 — A VLAN renumbered 18 months ago. A person silently corrects it. A script doesn't.
7. Gap 2 — Restarts ordered so the app came up before its database accepted connections.
8. Gap 3 — Verification checked the interface was up. Not that traffic flowed.
9. The point — None of it was found by testing the automation. It was found by *writing* it.
10. CTA — "When did you last *run* yours, rather than read it?"
