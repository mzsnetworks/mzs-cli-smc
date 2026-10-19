# Master — blast-radius-moved

**Idea:** ideas-2026-07-08 #1 (NA · Contrarian) — "Automation didn't reduce your outages — it changed who causes them. The blast radius moved from a human to a playbook."
**Preset:** Professional (LinkedIn personal + IG @mzsnetworks)
**Publish date:** 2026-08-06
**Stat gate:** none — no numeric claims; scenario numbers kept illustrative/vague, no invented precision.

---

Automation didn't reduce your outages. It changed who causes them.

The blast radius moved from a human to a playbook.

Before automation, mistakes were retail. An engineer fat-fingers a VLAN on one switch. One closet goes down. Someone walks over and fixes it. Painful — and contained.

After automation, mistakes are wholesale. The same wrong decision — encoded once, reviewed by nobody, pushed everywhere — lands on every device in scope, in seconds, with perfect consistency. Nothing "failed." The system did exactly what it was told. At scale.

That's the part teams miss when they measure automation by tickets closed: automation executes decisions. It doesn't improve them. A bad change process at human speed is an outage. The same process at machine speed is an outage everywhere at once.

I'm not arguing against automation. I'm arguing the discipline has to move upstream — into the playbook and the change process, before anything executes:

Dry-run diff before push.
Canary scope before fleet.
A rollback that's been tested, not assumed.
Peer review on playbooks, same as production code — because that's what they are.

The blast radius didn't shrink when we automated. It consolidated. One person's judgment now executes with the reach of the entire fleet.

Automation doesn't take humans out of the loop. It amplifies whichever human wrote the loop.

What's the guardrail you won't let a playbook run without?
