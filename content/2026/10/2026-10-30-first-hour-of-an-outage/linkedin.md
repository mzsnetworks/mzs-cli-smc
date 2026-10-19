# LinkedIn — first-hour-of-an-outage


The most expensive hour of an outage is the first one.

It is rarely spent diagnosing. It is spent deciding whose problem this is.

The bridge fills up — fourteen people, most of whom do not need to be there. Each team demonstrates in turn that the fault is not theirs. Network shows clean interfaces and adjacencies. The application team shows the service responding on localhost. Storage is green. Every demonstration is honest, competent, and takes about twelve minutes.

At the end of the hour everybody is correct and nothing is fixed.

This is not a skills problem, and it is not defensiveness. It is structural. Nobody can assign the problem, so everybody defends against being assigned it — a rational response to a bridge with no authority on it.

The fix is to separate two questions that get collapsed into one: who owns the problem, and who caused it.

Ownership is a role. It gets assigned at minute zero, before anyone knows the cause, and it can move. Cause is a finding. It arrives later, sometimes days later, and belongs in a postmortem.

Once those are separate, the first hour changes shape. Someone is holding the timeline and assigning work — and that person does not need to be the deepest expert in the room. Arguably should not be: the expert needs their attention on the fault.

The second piece is a default. When ownership is genuinely ambiguous, it resolves to a named team rather than a debate. Getting that wrong occasionally costs minutes. Debating it costs the hour.

None of this requires tooling, and none of it shortens an outage on its own. It moves the expensive hour from arbitration to work.

The first hour is not where you find the cause. It is where you decide whether the next three have an owner.

Who is allowed to assign ownership on your bridge?

#IncidentResponse #NetworkEngineering #ITOperations
