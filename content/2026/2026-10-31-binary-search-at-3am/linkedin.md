# LinkedIn — binary-search-at-3am


At 3am, binary search beats intuition. Reliably, and by more than you would like.

Intuition is pattern-matching against everything you have seen before, and it is genuinely good. During the day it is the fastest tool you own. At 3am it is running on a tired brain that has lost the ability to notice when the pattern does not quite fit, which turns it into guessing with confidence.

The tell is familiar. You check the thing you are sure about, it is fine. You check the next thing you are sure about, it is fine. Forty minutes later you have tested six things in no particular order and eliminated almost nothing.

Halving the path is slower per step and faster overall.

Find the midpoint between the two ends that disagree. Test there. Whichever half fails is your new problem, and the other half is gone for good. Repeat. Eight hops become three tests.

What makes it work is not cleverness. It is that every test eliminates half the remaining space whether or not you guessed right. Intuition only pays off when it is correct. Binary search pays off when you are wrong, which at 3am is when you need the help.

Two things make it usable.

Write down the two ends before you start. The method depends on knowing what is definitely broken and what is definitely fine, and those are worth ten seconds of explicit thought rather than assumption.

And test at a real boundary, not a convenient one. The midpoint of the path, not the device you happen to have a session open to. A convenient test that eliminates nothing is worse than no test, because it feels like progress.

You can still follow a hunch. Give it one test. If it misses, go back to halving, and stop paying interest on a tired guess.

What is your first move when the obvious suspects come back clean?

#NetworkEngineering #NetOps #Troubleshooting
