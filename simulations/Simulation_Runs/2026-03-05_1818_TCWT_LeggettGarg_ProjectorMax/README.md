# TCWT Simulation Run: 2026-03-05_1818 Leggett-Garg with Projector Boost (Saturating Bound)

**Run Description**  
This simulation demonstrates the Leggett-Garg inequality in TCWT with a projector boost term that saturates the quantum bound (~2.828) at Ω = 0.  
The coupling κ = 1.454 is **derived** from the hydrogen atom squeeze leakage ratio (1 in ~4.26×10⁴³).  
Visibility damping recovers classical behaviour at high Ω.

**Scientific Context**  
At low Ω (strong resonance with the eternal Hum), non-commuting phase effects produce maximal LG violation.  
Higher Ω stiffens the manifold → classical bound restored.  
κ is calculated directly from the same squeeze-to-leakage ratio that explains gravitational weakness.

**Interpretation of the PNG**  
- **Orange line** — LG value vs Ω.  
- At Ω ≈ 0 → reaches ~2.828 (quantum maximum violation).  
- Drops smoothly below 2.0 (classical limit) around Ω ≈ 1.0–1.5.  
- Stays low at high Ω — no rebound.

**Parameters Used**  
- Ω range: 0.0 to 5.0 (80 points)  
- Projector boost: κ = 1.454 (from H leakage)  
- Visibility damping: exp(-0.75·Ω)  
- Angles: optimal LG configuration

**Files in This Folder**  
- tcwt_leggett_garg_projector_max.py — simulation script  
- leggett_garg_projector_max.png — LG vs Ω plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-05 1818
