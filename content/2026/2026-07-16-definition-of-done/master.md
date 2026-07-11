# Automation Fails When Teams Don't Agree on "It's Done"

**Thesis:** Automation encodes a definition of done. If the team never agreed where the finish line is, the tool doesn't resolve the disagreement — it hardcodes one version and executes the rest as a gap.
**Pillars:** Network Automation · Engineering Systems · Lessons from Production
**Defended opinion:** Automation doesn't create agreement — it executes whatever agreement (or disagreement) you already had.
**Stats:** none (judgment/experience post) → Factcheck clean.

---

Your automation didn't fail. Your team never agreed on what "done" meant.

Ask three engineers when a switch provisioning job is "done." One says: config pushed. One says: ports up and passing traffic. One says: in monitoring, documented, and handed to ops. Same task, three finish lines.

Now automate it. The script picks one definition — whichever the author had in their head — and silently ships the other two as incomplete. It runs green every time. And every time, someone downstream inherits a switch that's "done" by the tool's definition and unfinished by theirs.

The automation worked perfectly. The outcome was still wrong.

This is the part nobody writes a runbook for: automation doesn't just execute steps. It encodes a definition of done. If the humans never agreed on where the finish line is, the tool doesn't resolve the disagreement — it hardcodes one version of it and executes the rest as a gap.

Manual work hid this. A person filling gaps by hand quietly absorbed the ambiguity — noticed the missing monitoring, added the doc, closed the loop. Automation doesn't improvise. It does exactly what "done" was defined as, and nothing past it.

So the fix isn't better code. It's a definition of done the whole team actually signed off on — written down, boring, specific. Ports up. Config in golden. Monitoring live. Docs updated. Ownership transferred. If it's not on the list, the automation won't do it — and now everyone knows that going in.

Automation is only as aligned as the team behind it. It doesn't create agreement. It executes whatever agreement — or disagreement — you already had.

Where does your team's definition of "done" quietly disagree?

#NetworkAutomation #NetDevOps #NetworkEngineering
