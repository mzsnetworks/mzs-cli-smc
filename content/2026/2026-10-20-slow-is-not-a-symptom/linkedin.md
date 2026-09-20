# LinkedIn — slow-is-not-a-symptom


"It's slow" is not a symptom. It is a feeling, and you cannot troubleshoot a feeling.

That is not a dig at whoever reported it. They are describing the thing accurately from where they sit. But the report has no number, no direction and no boundary, and without those three you cannot tell whether anything you do next helps.

The most expensive version of this is the ticket that stays open for a month because there is no condition under which anyone could call it fixed.

So before touching anything, I try to get three things.

A number. Slow compared to what, measured how. Page load, file copy, query time, a transaction that used to take four seconds and now takes forty. Any number, even a rough one, even a stopwatch. Forty seconds is a fact. "Slow" is not.

A direction. Is it slow in one direction, both, or only on the first request? Upload and download failing differently is a completely different problem from both failing together, and it is the cheapest split available.

A boundary. Who is not affected. One user, one site, one application, one time of day. The edge of the problem tells you more than the center of it, because everything on the working side of that line is eliminated.

Then one more question, and it is not technical: when did this become worth reporting? Sometimes nothing changed in the network and something changed in what the business expects of it. That is still a real problem. It is just not one you fix with a packet capture.

None of this is the investigation. It is what makes an investigation possible, and it takes about ten minutes.

An unmeasured complaint cannot be closed. It can only be outlasted.

How do you get a number out of "it's slow"?

#NetworkEngineering #NetOps #Troubleshooting
