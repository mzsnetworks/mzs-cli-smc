# LinkedIn — drift-is-a-rate-not-a-snapshot


A drift remediation project ends. Drift does not.

The usual shape is a cleanup. Somebody exports the running configuration from every device, compares it against what the standard says, and works through the differences over a few weeks. At the end the estate matches. It is real work and it is worth doing.

Six weeks later it does not match any more, and the second conversation is harder than the first, because now it looks like the cleanup failed.

It did not fail. A cleanup corrects a state, and drift is not a state. It is a rate, and nothing in the cleanup changed the rate.

That rate has specific sources, and they are mostly ordinary. An emergency change at 2 AM that never came back through the standard. A vendor default that reappears after a firmware upgrade. A site built from an older template because that is what the installer had. An exception for one location, copied to four more by somebody reusing a config.

None of those are discipline problems, which is why asking people to be more careful does not move the number.

So the measurement worth having is not how far the estate is from the standard today. It is how fast it moves away, where that movement enters, and which of it was deliberate. Driftguard watches for that continuously rather than at audit time, which turns the question from an annual archaeology exercise into something with a trend line.

Once you can see the rate, the fix stops being more cleanups. It becomes closing the specific paths variation comes in through.

A perfectly remediated estate with an unexamined reintroduction rate is a snapshot. It was accurate on the day it was taken.

Book a consultation: mzsnetworks.com

#ConfigurationDrift #NetworkAutomation #NetOps
