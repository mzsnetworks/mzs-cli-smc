# LinkedIn — a-dry-run-is-not-a-test


"We dry-ran it" gets said in change reviews as though it settles the question. It does not.

A dry run tells you the change is syntactically valid and that the device will accept it. That is genuinely useful and it is not nothing. It is also the smallest of the questions worth asking, and the one least likely to be the reason a change goes wrong.

The changes that cause outages are usually accepted perfectly. The command was valid. The device took it. What then failed was a dependency nobody modeled, a traffic pattern the test did not generate, or a neighbor that reconverged in a way the diagram did not predict.

So we separate four stages, because each one answers a question the one before it cannot.

A dry run answers whether the syntax is right. A model answers what the change does to the intended topology, including the parts of it you were not thinking about. A lab or a canary site answers how real traffic behaves against it, which is where the surprises actually live. And production with a rehearsed revert answers the only question the business asked, which is whether the service still works.

Teams skip to the last stage because the first three cost time and the change looked simple. That is a defensible call on a change whose blast radius is small and well understood. It is how a Tuesday becomes a long night on anything else.

None of this requires more tooling than most estates already have. It requires agreeing which stage a change has to clear before it enters a window, and writing that down once rather than deciding it under time pressure.

Valid is not the same as safe. A dry run proves the first one.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #ChangeManagement
