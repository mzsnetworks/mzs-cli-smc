# LinkedIn — tools-that-dont-talk


Count the systems a single routine change touches at your company.

A ticket gets raised. Someone checks monitoring to confirm the symptom. Someone opens the network platform and makes the change. Someone updates the ticket. Maybe the CMDB gets corrected, maybe it doesn't. Maybe the monitoring threshold gets adjusted for the new state, usually later.

Every one of those systems has an API. Almost none of them are connected to each other.

What fills the gap is a person, moving information between browser tabs. That person is also the failure point: when they are on holiday the process degrades, and when they are busy the CMDB is the step that gets skipped.

This is the least glamorous automation work there is and frequently the highest return, because you are not replacing engineering judgment — you are replacing transcription. Ticket opens, enrichment runs, change executes against the platform, ticket updates itself, inventory reconciles, monitoring adjusts.

We build this as orchestration across whatever you already own, through the APIs those products already ship. Workflow Engine is the piece that sequences it, with the same safety rules as any other change: tested, reviewed, tracked, reversible.

Nobody puts "reduced tab-switching" in a business case. It is still where the hours are.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #InfrastructureAsCode
