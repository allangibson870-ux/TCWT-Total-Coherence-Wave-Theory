# TCWT Lagrangian (Orthodox Field-Theory Form)

**Version**: 2026.3  
**Author**: A. Gibson  
**Purpose**: This document reformulates the core ideas of Total Coherence Wave Theory (TCWT) — coherence, phase-bleed gravity, ghost density, and decoherence — in a form compatible with standard scalar-field theory.  
It is inspired by but does not claim equivalence to conventional GR or QFT.

## 1. Field Content

- **θ(x)** — real scalar field representing the temporal phase  
- **G(x)** — real scalar field representing ghost density (dark-energy analogue)  
- **Ω(x)** — auxiliary field encoding temporal drag / informational density  

Phase-bleed field:

$$
\lambda_\mu = \partial_\mu \theta
$$

acts as the gravitational analogue.

## 2. Lagrangian Density

$$
\begin{aligned}
\mathcal{L} ={}& -\frac{1}{2} Z_\theta(\Omega) \, g^{\mu\nu} \partial_\mu \theta \partial_\nu \theta - \frac{1}{2} m_\theta^2 \theta^2 \\
& -\frac{1}{2} Z_G \, g^{\mu\nu} \partial_\mu G \partial_\nu G - \frac{1}{2} m_G^2 G^2 \\
& - \gamma \, \partial_\mu G \partial^\mu \theta \\
& - \lambda_1 \theta^2 G - \lambda_2 G^2 \\
& + \frac{1}{2} (\partial_\mu \Omega)^2 - V(\Omega) - \Lambda_G
\end{aligned}
$$

with constraint/cap potential for Ω:

$$
V(\Omega) = \frac{\mu}{2} \left( \Omega - \kappa |\nabla \theta| \right)^2 + \frac{\lambda}{4} \left( \max(\Omega, \Omega_{\max})^2 - \Omega_{\max}^2 \right)^2
$$

Ω_max ≈ 16.91.

This is a minimal extension: two interacting scalars with Ω-dependent kinetic term for θ and a dynamical auxiliary field Ω.

## 3. Interpretation of Key Terms

### 3.1 Coherence and Drag (Ω)
Kinetic prefactor:

$$
Z_\theta(\Omega) = 1 + \beta \left( \frac{\Omega}{\Omega_{\max}} \right)^2
$$

Ω is enforced variationally:

$$
\Omega = \kappa |\nabla \theta|
$$

Full form with velocity:

$$
\Omega = \kappa \left( |\nabla \theta| + \frac{K_{\text{tc}} v}{\sqrt{1 - v^2/c^2}} \right)
$$

### 3.2 Phase-Bleed and Gravity Analogue
λ_μ = ∂_μ θ couples to G:

$$
\mathcal{L}_{\text{coupling}} = - \gamma \, \partial_\mu G \partial^\mu \theta
$$

Reproduces ∇·λ ∼ ∂_t G.

### 3.3 Dark Energy as Reionization-Locked Inductive Scaling
Dark energy is the residual collective inductance of the knot hierarchy, locked at reionization (z ≈ 6.1).  
Inductive exponent α(z) transitions from 0.5 (pre-reionization) to 0.4 (post-reionization).

This fixes late-time dominance. Scaling remains phenomenological; pure internal attempts are under refinement.

### 3.4 Knot Stability Energy
From Gaussian soliton θ(r) = θ₀ e^{-r²/(2R²)}:

$$
E(R) = a R + \frac{b}{R} + c R^3
$$

- a R = Hum tension  
- b/R = surface energy  
- c R³ = volume potential

Coefficients fixed by knot squeeze pressure and transition scale.

### 3.5 21 cm Anomaly: Phase-Viscosity
Deep absorption at z ≈ 17–20 (EDGES) from phase-viscosity during α(z) descent.  
Grinding produces decoherence heat (~1–10 K), preventing adiabatic cooling.  
Effect occurs pre-stellar, from hierarchical pump.

### 3.6 Dark Matter as Phase-Opaque Knots
~84 % mass discrepancy = phase-opaque knots (|∇θ| ≥ λ_crit → Ω ≥ Ω_max, V ≤ 0.368).  
Trapped in fractal foam (d ≈ 1.585), they form gravitational scaffolding without light emission.

### Scale-Dependent Gravity in TCWT vs Standard Gravity

In standard gravity, acceleration falls as 1/r².  
In TCWT, phase-bleed accumulation is **logarithmic** (θ(r) ∝ ln(r)) and filtered by fractal foam (d ≈ 1.585), producing **slower fall-off** at large scales — mimicking dark-matter-like effects without extra mass.

**Illustrative comparison** (normalised at 1 unit distance):

| Distance | Standard Gravity (1/r²) | Fractal TCWT (effective) | Ratio (TCWT / Standard) |
|----------|--------------------------|---------------------------|--------------------------|
| 1 unit   | 1.0                      | 1.0                       | 1×                       |
| 10 units | 0.01                     | ~0.26                     | ~26× stronger            |
| 100 units| 0.0001                   | ~0.067–0.14               | ~670–1400× stronger      |

**Interpretation**  
- At small scales (near knots): TCWT matches Newtonian gravity (phase-bleed ≈ 1/r²)  
- At large scales (galactic/cluster/cosmic): logarithmic accumulation + fractal filtering strengthens effective gravity → explains rotation curves, cluster dynamics, and cosmic acceleration without dark matter or modified G  

The exact ratio depends on the hierarchical resonance exponent α ≈ 0.4–0.5 and fractal foam dimension d ≈ 1.585.  
This is a direct consequence of the phase-bleed field λ = ∇θ and the decoherence shadow.

See the pregeometric Lagrangian for the derivation of the logarithmic θ(r) and emergent metric.

## 4. Relation to Original TCWT Constructs

| TCWT Concept                | Orthodox Interpretation                                      |
|-----------------------------|---------------------------------------------------------------|
| Coherence action            | Non-canonical kinetic term Z_θ(Ω)                             |
| Phase-bleed λ               | Gradient of θ                                                 |
| Ghost density G             | Second scalar field with shallow potential                    |
| Decoherence cliff           | Ω-dependent kinetic suppression                               |
| Knot solitons               | Localised θ solutions                                         |
| Dark energy                 | Residual collective inductance locked at reionization         |
| Dark matter                 | Phase-opaque knots trapped in fractal foam                    |
| Visibility V = e^{-σ|λ|}    | Exponential suppression from phase gradient                   |

## 5. Conserved Quantities (Noether Currents)

**Phase current**:

$$
J^\mu = 2 C_0 (\partial_t \theta - \Omega) \delta^\mu_0 + 2 \kappa \partial^\mu \theta
$$

**Energy density**:

$$
\rho = C_0 (\partial_t \theta - \Omega)^2 + \kappa |\nabla \theta|^2 + \alpha (\partial_t G - \nabla^2 \theta)^2 + \frac{1}{2} (\partial_t \Omega)^2 + V(\Omega)
$$

Both conserved.

## 6. Derivation of the Non-Commuting Phase Commutator

From non-local term:

$$
\mathcal{L}_{\text{non-local}} = -\frac{\kappa}{2} \int dt' \Omega(t') (\partial_t \theta(t))^2 \cdot \text{sign}(t - t')
$$

Peierls bracket gives:

$$
[\theta(t_1), \theta(t_2)] = i \kappa \bar{\Omega} (t_2 - t_1)
$$

Reduces to original form for slowly varying Ω.

## 7. Visibility Suppression (internal derivation)

$$
V(r) = \exp(-\sigma |\lambda(r)|)
$$

σ = 1/g ≈ 6.58 × 10^{-36} m/rad (visibility drops to 1/e at transition gradient).

## 8. Summary

This formulation bridges TCWT to standard field theory while preserving core mechanisms.  
Dark energy scaling remains open for refinement (phenomenological at present).

Current limitations: quantitative dark energy and cosmic untangling timescale need further work.
Important note on spacetime
This formulation uses a fixed Minkowski metric $  g_{\mu\nu}  $ for compatibility with standard field-theory notation. In the full TCWT ontology, spacetime itself emerges from distortions of the TimeWave (θ-field and knots). The metric is therefore an effective, low-energy construct, not fundamental.
