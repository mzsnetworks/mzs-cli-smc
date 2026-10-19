# Instagram — binary-search-at-3am


At 3am, binary search beats intuition. 🔍

Reliably, and by more than you'd like.

Intuition is pattern-matching against everything you've seen, and it's genuinely good. During the day it's the fastest tool you own.

At 3am it's running on a tired brain that's lost the ability to notice when the pattern doesn't quite fit. That turns it into guessing with confidence. ⚠️

The tell is familiar. You check the thing you're sure about — fine. Then the next thing you're sure about — fine. Forty minutes later you've tested six things in no order and eliminated almost nothing.

Halving the path is slower per step and faster overall:

→ Find the midpoint between the two ends that disagree
→ Test there
→ Whichever half fails is your new problem. The other half is gone for good
→ Repeat

Eight hops become three tests.

What makes it work isn't cleverness. Every test eliminates half the remaining space whether or not you guessed right.

Intuition pays off when it's correct. Binary search pays off when you're wrong — which at 3am is when you need the help. ⚙️

Two things make it usable: write down the two ends before you start, and test at a real boundary, not a convenient one.

You can still follow a hunch. Give it one test. If it misses, go back to halving.

#NetworkEngineering #NetOps #Troubleshooting #ITOps #Infrastructure
