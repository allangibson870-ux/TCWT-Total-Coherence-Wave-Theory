# TCWT — Total Coherence Wave Theory (v2026.3)


**TCWT Preprint (Primary Citation)**  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19134583.svg)](https://doi.org/10.5281/zenodo.19134583)

**TCWT Software Release (GitHub-linked)**  
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19075414.svg)](https://doi.org/10.5281/zenodo.19075414)


**Summary**  
Total Coherence Wave Theory (TCWT) proposes that spacetime, matter, and the dark sector emerge from distortions in a global coherent oscillatory background — the Hum. Version 1.1.0 introduces the **Saturated Field Equation**, which mathematically resolves gravitational singularities by imposing a physical upper bound on phase-gradient stiffness via the Ω-Cap potential.

## Call for Collaborators

TCWT has reached the point where the core framework is defined, but several mathematical components now require expertise beyond my skillset. I’m looking for collaborators with strong backgrounds in theoretical or mathematical physics to help formalise the stability analysis, perturbation structure, and scale‑dependent dispersion sector. If you’re interested in contributing to the development of the theory, feel free to open an issue or get in touch.


**Key Advancements**  
- The **Saturated Field Equation** expresses emergent spacetime curvature (R_μν) as the energy-momentum response of the phase field θ(x,t), regulated by the Ω-Cap to prevent infinite densities. This yields finite Gaussian Phase-Knots as the fundamental structure of matter.  
- **Non-Singular Gravity**: At the knot core (r < R_crit), the phase gradient |∇θ| saturates and drops effectively to zero, eliminating infinite gravitational pull. The classical "event horizon" is replaced by a physical **Saturation Boundary** (r_sat), a finite-gradient surface.  
- **Observed Phenomena**:  
  - **Planetary / strong-field scale**: Recovers the Einstein / Newtonian limit for high-acceleration systems (e.g., L 98-59 d).  
  - **Galactic scale**: Produces MOND-like flat rotation curves through nonlinear gradient amplification — no dark matter particles required.  
  - **Extreme near-horizon scale**: Predicts **~15% excess periastron precession** for S-stars orbiting Sgr A* due to "Hum-Drag" against the saturated vacuum (consistent with observed deviations from pure GR).  
- **Cosmological fate**: Expansion is reinterpreted as **Ghost-Leakage Relaxation** (∂ₜG ≈ ∇²θ), driving the universe toward eventual return to a state of Total Coherence — 

TCWT offers a unified scalar-field alternative to General Relativity + dark matter/energy, with testable signatures across scales and no requirement for additional particles or higher-curvature terms.

## Core Idea in One Sentence

Time is an eternal oscillating background wave (the TimeWave).  
All matter, gravity, quantum behaviour, dark matter, and dark energy emerge from distortions (knots) and their phase leakage into this wave.


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

# TCWT Mathematical Architecture (v2026.9)

| Component | Mathematical Definition / Lagrangian Term | Physical Interpretation |
| :--- | :--- | :--- |
| **Total Action** ($S$) | $S = \int d^4x \sqrt{-g} \left[ \frac{R}{16\pi G} + \mathcal{L}_{TCWT} \right]$ | Unified Einstein-Hilbert and Phase-Field coupling [1]. |
| **Hum Sector** | $C_0(D_t \theta - \Omega)^2 - \kappa a_0^2 F\left( \frac{\lvert\nabla\theta\rvert^2}{a_0^2} \right)$ | Drives MONDian rotation curves and mass-knot stability [1, 85]. |
| **Ghost Sector** | $-\alpha(D_t G - \Delta \theta)^2$ | Drives late-time expansion and high-$z$ "thawing" [31, 35]. |
| **$\Omega$-Cap Potential** | $V_\Omega(\Omega) = \frac{\lambda_\Omega}{4}(\Omega^2 - \Omega_{max}^2)^2$ | Prevents singularities by capping the maximum gradient density [1]. |
| **MOND Limit** | $F(x) = x + \frac{2}{3}x^{3/2} \implies \mu(x) = 1 + \sqrt{x}$ | Bridges Newtonian ($x \gg 1$) and MOND ($x \ll 1$) regimes [1, 81]. |

## Correspondence & Field Limits

| Physical Regime | TCWT Limit | Standard Physics Mapping |
| :--- | :--- | :--- |
| **Strong Field** | $\lvert\nabla\theta\rvert \gg a_0 \implies \mu(x) \to 1$ | Newtonian Inverse Square Law [1]. |
| **Weak Field** | $\lvert\nabla\theta\rvert \ll a_0 \implies \mu(x) \to \sqrt{x}$ | Milgromian Dynamics (MOND) [81, 82]. |
| **Cosmological** | $\alpha > 0 \implies \omega^2 = c_s^2 k^2 + \beta k^4$ | Dark Energy Expansion + Small-Scale Damping [31]. |
| **Quantum** | $[ \delta\theta(x), \pi(y) ] = i \delta^3(x-y)$ | Renormalizable Effective Field Theory (EFT) [46, 47]. |


At small radii TCWT ≈ Newtonian; at galactic scales the pull is much stronger → flat rotation curves without exotic particles.

<img width="390" height="210" alt="tcwt_log" src="https://github.com/user-attachments/assets/798ee528-af1c-4dcd-8015-0c1c0901af70" /><img width="390" height="210" alt="tcwt_linear" src="https://github.com/user-attachments/assets/c1e98799-8b7d-4a72-81b4-429363d9a149" />
<img width="1500" height="1200" alt="image" src="https://github.com/user-attachments/assets/1cc479a5-97a2-4f27-921c-ee65084f19e2" />




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

## Citation

If you use TCWT in your research, please cite:

@article{gibson_tcwt_preprint_2026,
  author       = {Gibson, Allan},
  title        = {Total Coherence Wave Theory: A Unified Phase-Field Framework for Matter, Gravity, and Cosmic Structure},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19134583},
  url          = {https://doi.org/10.5281/zenodo.19134583}
}






