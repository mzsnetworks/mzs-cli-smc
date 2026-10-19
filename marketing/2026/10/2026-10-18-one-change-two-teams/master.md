# Master — one-change-two-teams

**Preset:** Marketing — LinkedIn **only**, Luis's personal profile (not the company page), twice: ES at 2:00 PM and EN at 4:00 PM local, on a Monday.
**Date:** 2026-10-18
**Source:** `mzs-marketing` → `work/social/2026-10-18-marketing-batch-3/12-one-change-two-teams.md` (batch 3)
**Drafted:** 2026-10-18. Copied into this repo 2026-10-18; the folder date is the transfer date, not a publish date.
**Planned:** Mon Mar 29, 2027 — **EDT**, so `18:00:00Z` for the ES slot and `20:00:00Z` for the EN slot. Daylight time begins Sun Mar 14, 2027; derive the offset from the date rather than copying it forward.
**Thesis:** A route and a security group are now the same path, owned by two teams with two change processes and two tools. The outage happens at the boundary, and the fix is one reviewed change across both rather than better coordination between them.
**Pillar:** Short technical teardowns
**Sells:** Cloud and network as one change surface — orchestration and API integration
**CTA:** Book a consultation
**Stats:** none. Batch 3 carries no metrics, no client results and no case studies by design — the anonymized-proof pillar is still blocked on a case study. Factcheck needs no source gate and the marketing illustrative-figure exception is not invoked.
**Language:** EN master with an ES render (`linkedin-es.md`) per `rules/SPANISH.md` — usted register, product and tool names left in English. Written to the ES length band and ratio upstream, so nothing was expanded on transfer.

---

A route and a security group are the same path now. They are still owned by two teams, with two change processes and two tools.

That split made sense when the cloud was a project and the network was the business. It stopped making sense when the path a transaction takes crosses both several times before it reaches anything.

What it produces is a specific kind of incident, and it is always the same shape.

Both changes were correct. The network change was reviewed by network people against network standards. The cloud change was reviewed by cloud people against cloud standards. Neither review had the other change in front of it, because the two live in different systems and were raised on different days. The failure is at the boundary, and the boundary has no owner.

Then the troubleshooting takes longer than the fix, because the evidence is split the same way. One team has flow data and no visibility into the security group. The other has a console and no visibility into the routing. The bridge call is forty minutes of establishing a shared picture that neither tool provides.

The usual answer to this is better coordination, which means more meetings and a shared calendar. That helps a little and does not survive a busy quarter.

What works is making the path one thing in the tooling. One change that describes the whole path, reviewed once, applied through both platforms' APIs, with the state recorded in one place. That is ordinary orchestration work, and it is most of what we do.

Your traffic does not know where your org chart divides. Only your change process does.

Book a consultation: mzsnetworks.com

#CloudNetworking #NetworkAutomation #NetOps
