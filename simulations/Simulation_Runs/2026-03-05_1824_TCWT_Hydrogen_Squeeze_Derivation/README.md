# TCWT Simulation Run: 2026-03-05_1824 Hydrogen Squeeze & κ Derivation

**Run Description**  
This simulation computes the leakage ratio from the hydrogen atom squeeze and derives the non-commutativity coupling κ used in the LG projector boost.

**Scientific Context**  
In TCWT, the enormous squeeze pressure inside the Snag knot (~2.42×10²⁰ Pa) produces a tiny residual gravitational leakage at the Bohr radius (~10⁻⁴⁴ relative strength).  
The leakage ratio r ≈ 2.35×10⁻⁴⁴ → 1/r ≈ 4.26×10⁴³.  
κ is derived as log₁₀(1/r) / 30 ≈ 1.454 — normalising to the typical Ω transition scale (~30) in simulations.

**Interpretation of the PNG**  
- **Orange curve** — Gravitational leakage pressure suppression vs distance (1/r⁴ fall-off).  
- Vertical dashed line — Bohr radius (where leakage is calculated).  
- Derived κ = 1.454 (printed in console and used in non-commuting phase terms).

**Parameters Used**  
- Squeeze pressure: 2.4219×10²⁰ Pa  
- Bohr radius: 5.2918×10⁻¹¹ m  
- κ = log₁₀(1/r) / 30

**Files in This Folder**  
- tcwt_hydrogen_squeeze_kappa.py — script  
- hydrogen_squeeze_leakage.png — leakage suppression plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-05 1824
