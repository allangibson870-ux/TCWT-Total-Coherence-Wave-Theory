# TCWT Simulation Run: 2026-03-06_1154 Delayed Entanglement Swapping with Which-Path Ambiguity

**Run Description**  
Tests entanglement swapping with **time delay** between pair creation and swap measurement, plus **partial which-path ambiguity** on one pair.

**Scientific Context**  
In TCWT, entanglement persists as long as phase coherence with the Hum is maintained.  
Delay accumulates phase mismatch (Ω gradient) → fidelity drops.  
Which-path info increases Ω → de-phases one pair → reduces swapped fidelity.  
κ = 1.454 from hydrogen squeeze.

**Interpretation of the PNG**  
- Cyan line: Final swapped fidelity vs delay time.  
- Starts near 1.0 (small delay) → drops with longer delay.  
- Partial which-path (strength=0.6) adds extra suppression.  
- If fidelity stays high for moderate delay → non-local coherence.  
- If drops fast → temporal fragility.

**Parameters Used**  
- κ = 1.454 (from hydrogen)  
- Which-path strength = 0.6 (partial ambiguity)  
- Delay in coherence time units

**Files in This Folder**  
- tcwt_entanglement_swapping_delayed.py — script  
- entanglement_swapping_delayed_fidelity.png — fidelity vs delay plot  
- README.md — document  

**Timestamp**  
2026-03-06 1154
