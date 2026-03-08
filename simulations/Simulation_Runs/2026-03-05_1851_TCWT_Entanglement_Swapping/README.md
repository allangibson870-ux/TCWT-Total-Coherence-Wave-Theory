# TCWT Simulation Run: 2026-03-05_1851 Entanglement Swapping

**Run Description**  
Simulates entanglement swapping fidelity vs local distortion Ω in TCWT.  
At low Ω (strong resonance with eternal Hum): near-perfect swapping (quantum-like).  
At high Ω (stiffening): fidelity drops to classical limit (~0.5, no entanglement transfer).

**Scientific Context**  
Entanglement swapping is a core quantum protocol: two independent entangled pairs are measured jointly → entanglement is transferred without direct interaction.  
In TCWT, low Ω allows phase coherence and non-commutative effects → high fidelity.  
High Ω damps coherence → swapping fails (classical correlation only).

**Interpretation of the PNG**  
- **Cyan line** — Average swapping fidelity vs Ω.  
- **Lime dotted line** — Perfect quantum swapping (1.0).  
- **Red dashed line** — Classical limit (0.5, no entanglement).  
- Low Ω → fidelity near 1.0 (quantum regime).  
- High Ω → drops to ~0.5 (classical limit).  
κ = 1.454 derived from hydrogen squeeze leakage ratio.

**Parameters Used**  
- Ω range: 0.0 to 5.0 (80 points)  
- κ = 1.454 (from H squeeze)  
- Visibility damping: exp(-0.75·Ω)

**Files in This Folder**  
- tcwt_entanglement_swapping.py — simulation script  
- entanglement_swapping_fidelity.png — fidelity vs Ω plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-05 1851
