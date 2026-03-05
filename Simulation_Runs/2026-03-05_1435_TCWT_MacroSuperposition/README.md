# TCWT Simulation Run: 2026-03-05_1435 Macroscopic Superposition Decoherence

**Run Description**  
Shows rapid loss of superposition visibility for macroscopic objects in TCWT. Ω spikes quickly due to high internal degrees of freedom → decoherence before superposition can be observed.

**Scientific Context**  
In TCWT, macroscopic systems (e.g. cat ~10^27 particles) have unavoidable local squeeze/leakage → Ω rises quadratically → exponential decay of coherence. No external environment needed — the object decoheres itself.

**Interpretation of the PNG**  
- **Orange line** — Superposition visibility drops to near-zero in microseconds.  
Demonstrates why we don't see cat superpositions: internal Ω spike suppresses resonance almost instantly.

**Parameters Used**  
- Time scale: 0 to 1 μs  
- Ω growth: 10¹⁰ × t²  
- Visibility: exp(-Ω)

**Files in This Folder**  
- tcwt_macro_decoherence.py — script  
- macro_decoherence.png — plot  
- README.md — document  

**Timestamp**  
Generated on: 2026-03-05 1435
