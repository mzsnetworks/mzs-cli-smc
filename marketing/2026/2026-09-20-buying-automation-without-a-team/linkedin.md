# LinkedIn — buying-automation-without-a-team


Most network automation advice is written for companies that already employ automation engineers.

If you run a capable network team with no one who writes Python, the standard guidance quietly does not apply. "Start with a small pilot and iterate" assumes someone will maintain the pilot after the enthusiasm fades. "Adopt GitOps for your network" assumes a review culture that exists somewhere in your organization and can be borrowed.

The honest version for a team in that position is narrower.

Pick processes where the automation can be operated without being modified. A well-built provisioning workflow with clear inputs can be run by any engineer on the team; a fragile pipeline that needs its YAML edited for each site cannot. That distinction matters more than which tool gets used.

Insist that the artefacts are ordinary. Python and Ansible over anything bespoke, because you can hire for them and read them.

And be honest about maintenance before you start. Automation that nobody maintains becomes automation debt, and network automation debt fails in a more expensive place than most.

There is real work available for teams with no automation engineers. It just is not the work the conference talks describe.

Talk to an engineer: mzsnetworks.com

#NetworkAutomation #NetOps #NetworkEngineering
