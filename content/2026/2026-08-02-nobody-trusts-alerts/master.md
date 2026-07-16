# Master — Nobody Trusts the Alerts

**Idea:** ideas-2026-07-11 #4 (ES, Reframe). You don't have an alerting problem — you have a nobody-trusts-the-alerts problem. Alert fatigue is a trust failure.
**Preset:** Business (MZS company voice — "we").
**Spine:** hook (the reframe) → POV (fatigue blames the human; trust blames the system) → data (none — judgment post) → judgment (the informal filter is the real alerting system; alerts must earn pages) → landing (noise/ignore/trust triad + question).

---

You don't have an alerting problem. You have a nobody-trusts-the-alerts problem. Alert fatigue is a trust failure.

"Fatigue" is a convenient word because it blames the human. Too many alerts, poor tired engineer. But engineers don't ignore alerts because they're tired. They ignore them because experience taught them to: that CPU alert always clears itself, that interface flap is "known," that disk warning has fired daily since March. Ignoring became the correct move. That's not fatigue — that's learning.

Every false positive is a withdrawal from a trust account. Every real page that follows one gets paid from whatever balance is left. When the account hits zero, your alerting still runs, dashboards still glow — but the real alerting system is now informal: the muted channel, the mental list of "ones that matter," the engineer who just knows. Unwritten, unaudited, and it leaves when they do.

The fix isn't fewer alerts. It's honest ones. Our rule: an alert must name an action and an owner. If firing doesn't change what someone does in the next ten minutes, it isn't an alert — it's telemetry wearing a pager. Log it, graph it, review it weekly. Just don't page a human with it.

And run the trust audit, not the threshold review. Ask your on-call: "Which alerts would you bet a 2am wake-up on?" The list will be short. Everything outside it is actively training your team to ignore the pager — and one day the page they ignore will be the real one.

Noise trains people to ignore. Ignoring trains incidents to grow. Trust is the only alerting metric that matters.

How many of your alerts would your on-call bet a 2am wake-up on?

---

**Sources**
- None required — judgment/experience post, no statistics.
