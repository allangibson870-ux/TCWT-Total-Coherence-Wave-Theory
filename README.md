# TCWT — Total Coherence Wave Theory (v2026.3)

A coherence-based scalar framework where time is a physical wave, knots are stable solitons, and gravity emerges from phase-bleed.

## Core Idea in One Sentence

Time is an eternal oscillating background wave (the TimeWave).  
All matter, gravity, quantum behaviour, dark matter, and dark energy emerge from distortions (knots) and their phase leakage into this wave.

<img width="1024" height="1536" alt="tcwt-visual" src="https://github.com/user-attachments/assets/caaffce8-b447-4825-88bb-a3b0a55d98a2" />


## Four Primitives

- **θ** — unwinding temporal phase  
- **Ω** — temporal drag / informational density  
- **λ = ∇θ** — phase-bleed (gravity analogue)  
- **G** — ghost density (dark-energy analogue)

## Key Equations (high-level)

- Eternal Hum: θ_Hum(t) = A_Hum sin(2π f_Hum t + ψ)  
- Knots (matter): θ_Knot(r,t) ≈ Θ₀(t) e^{-r²/R²}  
- Gravity: a(r) = -χ λ(r) = -χ ∇θ(r)  
- Dark energy: ρ_DE ∝ κ P_leak × (phenomenological scaling)  
- Visibility / decoherence: V = exp(-σ |λ|)  
- Relativistic decoherence: Ω(v) capped at Ω_max ≈ 16.91  
- Quantum commutator: [θ(t₁), θ(t₂)] = i κ Ω (t₂ - t₁)

## Built-in Safeguards

- Energy positivity: M → |M| in Ω  
- Ω cap: Ω ≤ Ω_max = Ω_transition / κ ≈ 16.91  
- Visibility floor: V ≥ 10^{-60}  
- Knot size floor: R_knot ≥ Planck length

These prevent unphysical runaway while preserving all predictions.

## Dark Matter in TCWT: Phase-Opaque Knots

~84 % mass discrepancy = phase-opaque knots (|∇θ| ≥ λ_crit → Ω ≥ Ω_max, V ≤ 0.368).
Trapped in fractal foam (d ≈ 1.585), they form gravitational scaffolding without light emission.

### Why Galaxy Rotation Curves Are Flat (No Dark Matter Needed)

In standard Newtonian gravity, orbital speeds should drop as 1/√r at large radii.  
In TCWT, phase-bleed accumulation is logarithmic and filtered by the fractal foam, making effective gravity stronger at larger scales.

**Illustrative comparison** (normalised at 1 unit distance, e.g. stellar/galactic core scale):

| Coordinate Radius | Standard Pull (1/r²) | TCWT Effective Pull | Extra Pull Factor (TCWT / Standard) |
|-------------------|----------------------|---------------------|--------------------------------------|
| 1 (Normalization) | 1.0                  | 1.0                 | 1.0×                                 |
| 2 (Stellar Scale) | 0.25                 | 0.67                | 2.6×                                 |
| 5 (Galactic Sub-scale) | 0.04            | 0.39                | 9.7×                                 |
| 10 (Galactic Rim) | 0.01                 | 0.26                | 26×                                  |

At small radii TCWT ≈ Newtonian; at galactic scales the pull is much stronger → flat rotation curves without exotic particles.

<img width="390" height="210" alt="tcwt_log" src="https://github.com/user-attachments/assets/798ee528-af1c-4dcd-8015-0c1c0901af70" /><img width="390" height="210" alt="tcwt_linear" src="https://github.com/user-attachments/assets/c1e98799-8b7d-4a72-81b4-429363d9a149" />



See [Lagrangian-Pregeometric.md](docs/TCWT-Lagrangian-Pregeometric.md) for how this emerges from the phase-bleed field and fractal foam.

## Current Status & Roadmap

- Coherence action & Noether currents defined  
- Knot stability derived from effective potential  
- Gravity as phase-bleed field  
- Dark matter as phase-opaque knots in fractal foam  
- Dark energy as collective inductance (scaling still phenomenological)  
- Relativistic decoherence & 21 cm anomaly explained  
- Orbital phase accumulation derived

## Detailed Mathematics

For the full orthodox field-theory formulation (Lagrangian, Noether currents, commutator derivation, visibility, knot stability, phase-opaque dark matter, reionization-locked dark energy, etc.) see:

TCWT Lagrangian https://github.com/allangibson870-ux/TCWT-Total-Coherence-Wave-Theory/blob/main/docs/TCWT_Lagrangian.md

TCWT Pregeometric - https://github.com/allangibson870-ux/TCWT-Total-Coherence-Wave-Theory/blob/main/docs/TCWT-Lagrangian-Pregeometric.md

## Scientific Test Roadmap (2026)

https://github.com/allangibson870-ux/TCWT-Total-Coherence-Wave-Theory/blob/main/docs/Observational%20Tests.md

<img width="577" height="239" alt="image" src="https://github.com/user-attachments/assets/71ed2333-a727-4825-95a1-c2c24df6f851" />

<img width="1000" height="500" alt="entanglement_plot" src="https://github.com/user-attachments/assets/3311bbfe-9529-417c-baa7-7cbdb0e29d32" />




## LICENSE: Apache-2.0
cff-version: 1.2.0
message: "If you use this theory or code, please cite it as below."
authors:
  - family-names: "Gibson"
    given-names: "Allan"
title: "TCWT: Total Coherence Wave Theory"
version: "1.0.0"
date-released: "2024-05-22"
url: "https://github.com"
license: "Apache-2.0"
abstract: "A framework for interpreting quantum decoherence as a function of informational density (Omega) and temporal curvature."

