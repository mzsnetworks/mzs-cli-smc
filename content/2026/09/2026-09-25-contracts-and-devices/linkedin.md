# LinkedIn — contracts-and-devices


We counted forty-two support contracts and thirty-one devices.

Nobody had done anything wrong. That's the part worth understanding. No fraud, no incompetent purchasing — six years of ordinary decisions, and nothing in the process that ever forced the two lists to meet.

Here's how the gap opens. A device gets replaced under a refresh, and the new one gets a new contract — while the old contract runs to its renewal date and quietly renews. A spare gets bought with coverage attached, sits in a cupboard, and stays covered. A site closes and the hardware comes back, but the support line item was in a different budget owned by a different person. A three-year term auto-renews on a device that was decommissioned in month twenty.

Every one of those is a reasonable act by somebody doing their job. The failure is structural: procurement tracks contracts, operations tracks devices, nothing reconciles them.

And the direction people always assume is only half of it. Yes, some of those forty-two were paying for hardware that no longer existed. But the reconciliation also found the opposite, and the opposite is the expensive one — production devices with no coverage at all, because the renewal notice went to a purchasing address rather than to anyone who knew what the device did.

Overpaying is a line item. Discovering at 2am that your core switch has no RMA path is an outage with an unbounded length.

What fixes it isn't a system. It's a cadence:

→ Pull contracts from procurement and devices from the network itself, not from a spreadsheet either team maintains
→ Match on serial number — the only field both sides actually share
→ Do it annually, owned by one named person, not a committee
→ Anything unmatched in either direction gets a decision, not a note

It takes a couple of days and it has never once come back clean.

Two lists that were never wrong, and never reconciled, for six years.

When did anyone last compare what you pay for against what you actually run?

#ITAssetManagement #NetworkOperations #NetOps
