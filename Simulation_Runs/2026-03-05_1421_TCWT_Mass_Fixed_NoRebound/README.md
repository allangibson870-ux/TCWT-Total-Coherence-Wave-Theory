# TCWT Simulation Run: 2026-03-05_1421 Mass/Energy Shift (No Rebound)

**Run Description**  
This run tests Bell-CHSH violation strength (S-value) vs local mass/energy density (M) in TCWT.  
The "Mass-Frequency Link" is now soft-saturated: ratio = 0.9 + (M × 0.5) × exp(-0.35 × M).  
This prevents over-rotation at high M, avoiding artificial S rebound while keeping the quantum-to-classical drop.

**Scientific Context**  
In TCWT, quantum non-locality (S > 2) emerges at low Ω (high resonance with the eternal Hum).  
Increasing local mass/energy density raises Ω → de-tunes frequency ratio → reduces S toward classical limit (S ≤ 2).  
The exponential decay caps excessive phase wrapping at high M, keeping the model realistic.

**Interpretation of the PNG**  
Single plot: S-value vs M:  
- **Orange line** — Simulated S-values with soft saturation.  
- **Green shaded area** — Quantum Zone (S > 2.0, up to ~2.828).  
- **Red dashed line** — Classical limit (S = 2.0).  
At low M → maximal violation (quantum resonance).  
At high M → S falls and stays below 2.0 (classical behaviour, no rebound).

**Parameters Used**  
- Mass range: 0.0 to 3.0 (40 points)  
- Frequency ratio: 0.9 + (M × 0.5) × exp(-0.35 × M)  
- Bell test samples per point: 3000  
- Random seeds: 101 (reproducible)

**Files in This Folder**  
- tcwt_mass_shift_v3_no_rebound.py — simulation script (self-copied)  
- mass_shift_no_rebound.png — Bell violation vs mass plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-05 :??:??
