# Master — monitoring-vs-observability

Your monitoring stack is a museum. It shows you what broke — beautifully, in real time, on forty dashboards nobody watches until the pager fires.

Then you're standing in front of the exhibit at 2am, and it tells you nothing you can act on.

Monitoring answers *what*. Observability answers *why*. Most teams bought the first, renamed it the second, and wondered why outages still take three hours to resolve.

Here's the difference that actually matters operationally.

Monitoring is the questions you knew to ask in advance. CPU, interface errors, BGP session up/down, a latency threshold. You defined the check, so the check can only tell you about the failure you already imagined.

Observability is being able to ask a question you *didn't* pre-plan — at 2am, mid-outage, without shipping new code or a new sensor. "Show me every flow that touched this VLAN in the last ten minutes, grouped by the firewall that dropped it." If your tooling can't answer that on the spot, you don't have observability. You have a lot of graphs.

The tell is the war room. If half of it is spent SSH-ing into boxes to gather the context the dashboards didn't capture, the dashboards were monitoring. The green wall told you the components were up while the service was down — because nobody instrumented the *relationship* between them, only the parts.

This isn't a tooling purchase. Adding a fifth pane of glass doesn't get you there; it usually just moves the SSH session to a different tab. It's an instrumentation discipline: capturing enough context — traces, structured events, the *why* behind a state — that the next question is already answerable before you know to ask it.

Monitoring tells you the system is down.
Observability tells you why.
Engineering judgment is knowing which one you actually bought.
