# Master — documentation-that-executes

**Preset:** Professional (LinkedIn personal profile + Instagram @mzsnetworks)
**Date:** 2026-10-15
**Thesis:** BGP communities are documentation that executes. Intent recorded in a wiki drifts from the network silently, because nothing enforces the match; intent recorded in a community string cannot drift, because the router is reading the same thing you are.
**Pillar:** Engineering Systems
**Source:** ideas-2026-08-27 #13
**Stats:** none. Judgment and practice only; no statistic stated as fact.

---

BGP communities are documentation that executes.

That is the part people miss about them. A community is not really a routing feature, it is a place to write down why a prefix is the way it is, in a form the router acts on. Same sentence, two audiences.

Which matters because the alternative is a wiki.

Intent in a wiki drifts. Not because anyone is careless, but because nothing connects the page to the behavior. Somebody changes a policy at 2am, the page is not part of the change, and from that moment the document describes a network that no longer exists. Nobody finds out until the next person trusts it.

Intent in a community cannot drift that way. If the tag says this prefix is a customer route that should not leave the region, and the policy acts on that tag, then the description and the behavior are the same object. You cannot update one and forget the other, because there is only one.

The practical shape of this is unglamorous. Tag at the edge, where you still know what something is: which customer, which region, which relationship, which class of route. Then write policy that matches on the tag rather than on a prefix list somebody has to maintain by hand. A prefix list is a wiki that happens to be machine-readable, and it goes stale the same way.

Two rules that keep it honest.

A community nobody matches on is a comment, not documentation, and it will rot like one. If you are tagging routes and no policy reads the tag, you have built an elaborate way of writing notes to yourself.

And publish the scheme. A community whose meaning lives in one engineer's head is worse than no community, because the next person will infer a meaning from what it appears to do, and they will be subtly wrong.

Where does your routing intent actually live: in something the router reads, or in something only people read?
