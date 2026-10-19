# Instagram — documentation-that-executes


BGP communities are documentation that executes. 🏷️

That's the part people miss. A community isn't really a routing feature — it's a place to write down why a prefix is the way it is, in a form the router acts on.

Same sentence, two audiences.

Which matters, because the alternative is a wiki.

Intent in a wiki drifts. Not through carelessness — nothing connects the page to the behavior. Somebody changes a policy at 2am, the page isn't part of the change, and from that moment the document describes a network that no longer exists. ⚠️

Nobody finds out until the next person trusts it.

Intent in a community can't drift that way. If the tag says this is a customer route that shouldn't leave the region, and the policy acts on that tag, the description and the behavior are the same object.

You can't update one and forget the other. There's only one.

Two rules keep it honest:

→ A community nobody matches on is a comment, not documentation — and it rots like one.

→ Publish the scheme. A community whose meaning lives in one engineer's head is worse than none, because the next person infers a meaning from what it appears to do. ⚙️

Where does your routing intent live — in something the router reads, or something only people read?

#NetworkEngineering #BGP #NetOps #ITOps #Infrastructure
