# Carousel Spec — kill-config-drift

8 slides · 1080×1350 (4:5).

**Brand:** navy `#161a45` background · cream `#F4EFE3` text · red `#eb2027` accent (words marked *like this*) · Cormorant Garamond Medium titles · Lato Regular body · brand mark = the text `@mzsnetworks` (no logo image).

Generate as individual images, one per slide, 1080×1350 (4:5). No grid/collage.

| # | Type | Title | Body / Steps |
|---|------|-------|--------------|
| 1 | Cover | Kill config drift in *30 minutes*. | Not six months. |
| 2 | Triad | Three pieces | NetBox — the source of truth · Rendered intent — the config you *meant* · The diff — intent vs running |
| 3 | Body | 1 — Source of truth | Intended state in NetBox. What *should* be running — not what is. Can't agree on "should"? That's the finding. |
| 4 | Body | 2 — Render the intent | Python + Jinja pull NetBox and render the config you meant, per device. No push. No orchestration. |
| 5 | Body | 3 — Diff it | Running config vs rendered intent. Every line that shows up is telling you something. |
| 6 | Triad | Every diff line is one of three things | An *undocumented* fix · An *unauthorized* change · Stale intent |
| 7 | Body | The trap: skipping to enforcement | Auto-remediation is month six. Day one is *visibility* — you can't enforce intent you never wrote down. |
| 8 | CTA | Write the intent down. The diff writes itself. | Drift is intent living in someone's head instead of a system. Follow *@mzsnetworks* · mzsnetworks.com |
