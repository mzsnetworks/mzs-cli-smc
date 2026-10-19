# Instagram — layer-1-is-the-answer

Layer 1 is still the answer more often than any of us admit. 🔌

I once watched a room of experienced people spend two hours on routing policy.

It was a dirty fiber connector.

Nobody in that room was junior. That's the part worth sitting with.

Here's my honest read on why it happens: the hard problem flatters us. ⚙️

Opening a BGP table says something about who you are.

Asking someone to read a light level does not.

So we skip past the boring layer — and the boring layer sits there being the answer.

The tells, once you know them:

→ errors that follow the port, not the prefix
→ input errors or CRCs on one side only
→ a link that comes up clean and degrades under load
→ interface resets nobody can correlate to anything above
→ anything called "random" that stops being random at the patch panel

And the checks cost minutes:

→ clear the counters, watch them for five
→ read the optic's actual Tx/Rx power against the vendor threshold
→ swap the patch lead
→ move to a different port
→ confirm the optic matches the fiber and the distance

I'm not saying most problems are Layer 1. They aren't.

I'm arguing about order.

Check the layer that's cheapest to rule out — not the one that's most interesting to be right about.

The asymmetry is brutal. Ruling it out costs ten minutes. Skipping it costs the afternoon, and you find it anyway — right after you've explained your routing theory to four people.

Cheap checks first. Interesting checks later. The photons don't care how senior you are.

What's the longest you've chased something that was a cable? 👇

#NetworkEngineering #Troubleshooting #NetOps #Networking #ITInfrastructure
