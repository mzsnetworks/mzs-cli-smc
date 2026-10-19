# LinkedIn — naming-is-an-interface


Naming conventions get treated as housekeeping. They are an interface, and automation is the consumer.

Here is where it shows up. Somebody writes a script that acts on every distribution switch. To know which devices those are, it matches on the hostname. The convention held for the first eight sites and then stopped, because a different team built the next twelve, and a merger brought thirty more on a scheme nobody wrote down.

Now the script needs a lookup table of exceptions. The table needs maintaining. The person who maintains it is the only one who understands it.

The same happens with interface descriptions. A monitoring system that tells a customer circuit from a backup link reads the description field, because that is the only place the distinction exists. Where that field is free text, the capability is not available, whatever the platform could do.

What makes this hard to fix is that it is never urgent. Nothing is broken. Every individual inconsistency is small, defensible, and was the obvious choice at the time.

The cost does not arrive as an outage. It arrives as a ceiling. Every automation gets more special cases, each reasonable, until the special cases are the system and nobody will touch it.

The fix is not a renaming project across the estate, which is disruptive and rarely gets approved. It is agreeing the convention now, applying it to everything new, and reconciling the existing estate in the order the automation roadmap actually needs it. Every piece of that roadmap gets cheaper the moment the names mean something.

A machine cannot infer what you meant. It can only read what you wrote.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #InfrastructureAsCode
