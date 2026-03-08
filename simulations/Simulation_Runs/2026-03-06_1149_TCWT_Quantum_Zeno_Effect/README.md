# TCWT Simulation Run: 2026-03-06_1149 Quantum Zeno Effect

**Run Description**  
Demonstrates the Quantum Zeno effect in TCWT: frequent weak measurements (each adding tiny Ω) suppress wave evolution, preserving the initial state.

**Scientific Context**  
In TCWT, the wave evolves freely at low Ω.  
Each weak measurement increases local Ω slightly → de-phases the evolution → frequent measurements "freeze" the system (fidelity stays near 1.0).  
κ = 1.454 is derived from hydrogen squeeze leakage ratio.

**Interpretation of the PNG**  
- Orange line: Fidelity after fixed time with increasing measurement frequency.  
- Lime dashed: Fidelity without measurements (natural decay).  
- Higher frequency → higher final fidelity (Zeno protection).  
- At very high frequency → fidelity → 1.0 (evolution frozen).

**Parameters Used**  
- κ = 1.454 (from hydrogen)  
- Natural decay rate = 0.02 per unit time  
- Ω per measurement = κ × 0.01 (weak)

**Files in This Folder**  
- tcwt_quantum_zeno.py — simulation script  
- quantum_zeno_fidelity.png — fidelity vs frequency plot  
- README.md — this document  

**Timestamp**  
2026-03-06 1149
