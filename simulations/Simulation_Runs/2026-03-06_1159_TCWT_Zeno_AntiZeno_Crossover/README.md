# TCWT Simulation Run: 2026-03-06_1159 Quantum Zeno + Anti-Zeno Crossover

**Run Description**  
Shows both the Quantum Zeno effect (weak frequent measurements freeze evolution) and the Anti-Zeno effect (strong frequent measurements accelerate decay).

**Scientific Context**  
In TCWT, measurements add local Ω → de-phase the wave.  
- Weak Ω per measurement → suppresses evolution → Zeno (fidelity stays high).  
- Strong Ω per measurement → over-drives decoherence → Anti-Zeno (fidelity drops faster than free evolution).  
κ = 1.454 derived from hydrogen squeeze leakage ratio.

**Interpretation of the PNG**  
- Green line: Weak measurements → fidelity rises with frequency (Zeno protection).  
- Red line: Strong measurements → fidelity falls faster than free evolution (Anti-Zeno acceleration).  
- White dashed: Free evolution (no measurements).  
- The crossover between Zeno and Anti-Zeno emerges naturally from Ω strength.

**Parameters Used**  
- κ = 1.454 (from hydrogen)  
- Weak Ω/meas = 0.008 × κ  
- Strong Ω/meas = 0.08 × κ  
- Natural decay rate = 0.025 per unit time

**Files in This Folder**  
- tcwt_zeno_antizeno_crossover.py — script  
- zeno_antizeno_crossover.png — fidelity vs frequency plot  
- README.md — document  

**Timestamp**  
2026-03-06 1159
