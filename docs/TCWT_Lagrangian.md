# TCWT Field Theory
## Pregeometric Lagrangian, Hum Vacuum, and Knot Matter

Version: 2026.6  
Status: consolidated and mathematically corrected formulation

---

# 1. Overview

**Total Coherence Wave Theory (TCWT)** describes the universe as a nonlinear coherence field whose ground state is an eternal oscillation known as the **Hum**.

In this framework:

| Concept | Interpretation |
|------|------|
| Hum | coherent phase vacuum |
| knots | localized phase structures (matter) |
| phase gradients | gravity |
| ghost leakage | dark energy |
| opaque knots | dark matter |

Spacetime and gravity emerge from the dynamics of a fundamental phase field.

---

# 2. Fundamental Fields

TCWT uses three scalar fields:

| Field | Meaning |
|------|------|
| θ(x,t) | coherence phase field |
| Ω(x,t) | informational drag density |
| G(x,t) | ghost / leakage regulator |

Derived quantity:

λ = ∇θ

which represents the **phase gradient responsible for gravitational acceleration**.

---

# 3. The Hum Vacuum

The vacuum state of the theory is not a zero field.

Instead the universe exists in a coherent oscillatory ground state:

θ₀(t) = Ω_hum t

where:

| Symbol | Meaning |
|------|------|
| Ω_hum | intrinsic hum frequency |

Physical phenomena arise from perturbations:

θ(x,t) = θ₀(t) + δθ(x,t)

---

# 4. TCWT Lagrangian Density

The pregeometric Lagrangian density is

L =
C₀(θ̇ − Ω)²  
+ κ(∇θ)²  
+ α(Ġ − ∇²θ)²  
− VΩ(Ω)

Parameters:

| Constant | Meaning |
|------|------|
| C₀ | temporal coherence |
| κ | spatial phase stiffness |
| α | ghost-coupling strength |

---

# 5. Ω-Cap Potential

The informational drag field is limited by a cap potential:

VΩ(Ω) = (λΩ / 4)(Ω² − Ω_max²)²

This term prevents runaway gradients and removes singularities.

---

# 6. Action

The action is

S = ∫ L d³x dt

Field equations follow from

δS = 0

---

# 7. Euler–Lagrange Equations

For a field φ:

∂L/∂φ − ∂μ(∂L/∂(∂μφ)) + ∂μ∂ν(∂L/∂(∂μ∂νφ)) = 0

Second derivatives appear due to the ∇²θ term.

---

# 8. Phase Field Equation

Variation with respect to θ gives

∂t[2C₀(θ̇ − Ω)]  
− ∇·[2κ∇θ]  
+ ∇²[2α(Ġ − ∇²θ)] = 0

This governs propagation of the **Hum phase field**.

---

# 9. Informational Drag Equation

Variation with respect to Ω gives

−2C₀(θ̇ − Ω) − dVΩ/dΩ = 0

Low-energy regime:

Ω ≈ θ̇

When the cap is reached:

Ω → Ω_max

---

# 10. Ghost Field Equation

Variation with respect to G:

∂t[2α(Ġ − ∇²θ)] = 0

Low-energy approximation:

Ġ ≈ ∇²θ

This field regulates curvature leakage.

---

# 11. Conserved Phase Flux

The Lagrangian is invariant under a global phase shift

θ → θ + ε

The Noether current is

J^μ = ∂L / ∂(∂_μ θ)

Components:

J⁰ = 2C₀(θ̇ − Ω)

J⃗ = 2κ∇θ

Conservation law:

∂_μ J^μ = 0

This represents conservation of **global phase flux**.

---

# 12. Hamiltonian Density

Canonical momenta:

π_θ = 2C₀(θ̇ − Ω)

π_G = 2α(Ġ − ∇²θ)

Hamiltonian density:

H =
C₀(θ̇ − Ω)²  
+ κ(∇θ)²  
+ α(Ġ − ∇²θ)²  
+ VΩ(Ω)

All terms are non-negative:

H ≥ 0

ensuring vacuum stability.

---

# 13. Knot Solutions (Matter)

Matter corresponds to **localized phase structures** in the coherence field.

Example radial ansatz:

θ_knot(r) = Θ₀ exp(−r² / 2R²)

Energy arises from gradient energy:

E = ∫ κ(∇θ)² d³x

These structures behave as **particle-like solitons**.

---

# 14. Knot Stability

A stable knot occurs when

dE/dR = 0

The Ω-cap imposes a minimum size:

R_crit ~ κ / Ω_max

Knots smaller than this radius cannot exist.

---

# 15. Gravity as Phase Gradient

Define

λ = ∇θ

Acceleration of matter:

a = −χ∇θ

The coupling constant

χ = (c² κ) / (C₀ Ω_max)

connects the field theory to gravitational dynamics.

---

# 16. Black Holes Without Singularities

In TCWT singularities cannot form.

Instead a black hole corresponds to a saturated knot where

|∇θ| → Ω_max / κ

The Ω-cap prevents further growth.

This produces a **phase-opaque region** rather than infinite density.

---

# 17. Dark Matter

Dark matter corresponds to **phase-opaque knots** where

|∇θ| ≳ Ω_max / κ

These structures:

- produce gravitational fields
- interact weakly with radiation
- remain stable over cosmological times.

---

# 18. Dark Energy

Slow relaxation of phase curvature through the ghost field produces vacuum pressure.

Low-energy relation:

Ġ ≈ ∇²θ

This leakage acts as a small background expansion force.

---

# 19. Cosmological Interpretation

The universe evolves through phases of knot formation and decay.

Hum (coherent vacuum)  
↓  
Phase instability  
↓  
Rapid knot formation  
↓  
Energy release (Big Bang)  
↓  
Matter-dominated universe  
↓  
Gradual knot unwinding  
↓  
Return toward Hum coherence

The Big Bang therefore represents a **large-scale phase instability**, not a singular origin.

---

# 20. Entropy in TCWT

The Hum is the most ordered state of the system.

Knots store distortion energy in the phase field.

Entropy corresponds to **knot relaxation**:

E_knot → 0

The long-term evolution of the universe tends toward the coherent background state.

---

# 21. Covariant Formulation (Recommended)

For relativistic symmetry the Lagrangian can be written as

C(∂_μθ − U_μ)²

where

U_μ = (Ω_hum, 0, 0, 0)

represents the background Hum flow.

This preserves Lorentz symmetry in the low-energy limit.

---

# 22. Summary

TCWT describes reality as a **coherence field** with an oscillatory vacuum.

From this structure emerge:

- matter as phase knots
- gravity from phase gradients
- dark matter from opaque knots
- dark energy from ghost leakage
- a cosmology driven by knot formation and decay

The governing Lagrangian remains

L =
C₀(θ̇ − Ω)²  
+ κ(∇θ)²  
+ α(Ġ − ∇²θ)²  
− VΩ(Ω)

from which the observable universe emerges as a dynamic structure within the background **Hum**.
