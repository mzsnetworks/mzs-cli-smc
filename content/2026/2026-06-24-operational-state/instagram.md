Two supervisors. Full redundancy. Every health check green. The ISSU still refused to run. ⚠️

The problem wasn't the procedure. It never is.

Most in-service upgrade failures aren't a skipped step. They're operational state the procedure assumed was clean — and wasn't.

→ Health checks read the running system
→ Redundancy status reads the running system
→ ISSU runs on the accumulated state underneath it 🔍

A previous install attempt had left residue behind. Not in the config. Not in anything a dashboard points to. In the upgrade machinery's own memory of what it already tried.

This is the brownfield tax. 🏗️ A greenfield box has no history to contradict you. A ten-year-old production device carries the residue of every change window — invisible until the one operation that depends on it fails.

The fix wasn't a better procedure. It was clearing what the device still remembered from upgrades that never finished.

⚙️ Configuration = what it should do
📜 Logs = what it did
🧠 Operational state = what it still remembers — and that's the one that fails your upgrade at 2 a.m.

What's the last "healthy" device that lied to you? 👇

---

**Carousel slides**
1. Cover — "Every check was green. The upgrade still failed." (bold)
2. The reframe — "The problem isn't the procedure. It never is."
3. The blind spot — health + redundancy read the *running* system
4. The real cause — ISSU runs on accumulated state, not the running config
5. The brownfield tax — every old box remembers every change window
6. The triad — Config / Logs / Operational state
7. CTA — "What's the last 'healthy' device that lied to you?"

---

#NetworkEngineering #NetworkOperations #NetDevOps #Cisco #NetworkAutomation #ITInfrastructure #DataCenter #NetOps #BrownfieldEngineering #SysAdmin #NetworkEngineer #ITOps #TechFieldNotes #Networking #UptimeMatters
