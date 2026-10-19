# LinkedIn — the-reason-behind-it


Your most valuable asset is not the configuration. It is the reason behind the configuration, and it usually lives in one person's head.

The config is recoverable. It is in a backup, on the device, in a repository, and if all of that burned down you could rebuild it from a design document in a week of unpleasant work.

What is not recoverable is why the timers on that one link are different from every other link. Why a route-map excludes a prefix that looks like it belongs. Why one site runs a slightly older firmware and has done for three years.

Every one of those has a reason. Usually a good one, arrived at during an outage nobody wants to repeat. And in most estates we assess, that reason exists in exactly one place, which is a person.

The failure mode is not that the person leaves. It is subtler. Somebody tidies up. A new engineer sees an inconsistency, corrects it because consistency is good practice, and reintroduces a problem that was solved years ago by the thing they just removed.

You cannot prevent that with access control. You prevent it by making the reason travel with the configuration.

A comment in the config, if the platform allows it. A line in the change record that says what this protects against rather than what it does. A one-paragraph note in the repository next to the template. None of this is documentation in the formal sense, and the formal kind is not what is missing. What is missing is the sentence that stops somebody undoing it.

The test is simple. Pick the strangest thing in your running configuration and ask whether anyone besides its author could explain it. If the answer is no, that is not a documentation gap. It is a single point of failure that happens to be a person.

What in your network only one person understands?

#NetworkEngineering #ITOperations #BrownfieldEngineering
