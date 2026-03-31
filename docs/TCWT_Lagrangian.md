# TCWT Field Theory
**Pregeometric Lagrangian, Hum Vacuum, and Knot Matter**  
**Version: 2026.6**  
**Status: consolidated and mathematically corrected formulation**

## 1. Overview
Total Coherence Wave Theory (TCWT) describes the universe as a nonlinear coherence field whose ground state is an eternal oscillation known as the Hum.

In this framework:

| Concept          | Interpretation                  |
|------------------|---------------------------------|
| Hum              | coherent phase vacuum           |
| knots            | localized phase structures (matter) |
| phase gradients  | gravity                         |
| ghost leakage    | dark energy                     |
| opaque knots     | dark matter                     |

Spacetime and gravity emerge from the dynamics of a fundamental phase field.

## 2. Fundamental Fields
TCWT uses three scalar fields:

| Field       | Meaning                        |
|-------------|--------------------------------|
| $\theta(x,t)$ | coherence phase field        |
| $\Omega(x,t)$ | informational drag density   |
| $G(x,t)$      | ghost / leakage regulator    |

Derived quantity: $\lambda = \nabla \theta$, which represents the phase gradient responsible for gravitational acceleration.

## 3. The Hum Vacuum
The vacuum state of the theory is not a zero field.

Instead the universe exists in a coherent oscillatory ground state:

$\theta_0(t) = \Omega_{\rm hum} t$

where $\Omega_{\rm hum}$ is the intrinsic hum frequency.

Physical phenomena arise from perturbations:

$\theta(x,t) = \theta_0(t) + \delta\theta(x,t)$

## 4. TCWT Lagrangian Density
The pregeometric Lagrangian density is

$L = C_0 (\dot{\theta} - \Omega)^2 - \kappa (\nabla \theta)^2 - \alpha (\dot{G} - \nabla^2 \theta)^2 - V_\Omega(\Omega)$

**Parameters:**

| Constant | Meaning                     |
|----------|-----------------------------|
| $C_0$    | temporal coherence          |
| $\kappa$ | spatial phase stiffness     |
| $\alpha$ | ghost-coupling strength     |

## 5. Ω-Cap Potential
The informational drag field is limited by a cap potential:

$V_\Omega(\Omega) = \frac{\lambda_\Omega}{4} (\Omega^2 - \Omega_{\rm max}^2)^2$

This term prevents runaway gradients and removes singularities.

## 6. Action
The action is

$S = \int L \, d^3x \, dt$

Field equations follow from $\delta S = 0$.

## 7. Euler–Lagrange Equations
For a field $\phi$:

$\frac{\partial L}{\partial \phi} - \partial_\mu \left( \frac{\partial L}{\partial (\partial_\mu \phi)} \right) + \partial_\mu \partial_\nu \left( \frac{\partial L}{\partial (\partial_\mu \partial_\nu \phi)} \right) = 0$

Second derivatives appear due to the $\nabla^2 \theta$ term.

## 8. Phase Field Equation
Variation with respect to $\theta$ gives

$\partial_t [2 C_0 (\dot{\theta} - \Omega)] - \nabla \cdot [2 \kappa \nabla \theta] - \nabla^2 [2 \alpha (\dot{G} - \nabla^2 \theta)] = 0$

This governs propagation of the Hum phase field.

## 9. Informational Drag Equation
Variation with respect to $\Omega$ gives

$-2 C_0 (\dot{\theta} - \Omega) - \frac{d V_\Omega}{d \Omega} = 0$

Low-energy regime: $\Omega \approx \dot{\theta}$

When the cap is reached: $\Omega \to \Omega_{\rm max}$

## 10. Ghost Field Equation
Variation with respect to $G$:

$\partial_t [2 \alpha (\dot{G} - \nabla^2 \theta)] = 0$

Low-energy approximation: $\dot{G} \approx \nabla^2 \theta$

This field regulates curvature leakage.

## 11. Conserved Phase Flux
The Lagrangian is invariant under a global phase shift $\theta \to \theta + \varepsilon$.

The Noether current is $J^\mu = \partial L / \partial (\partial_\mu \theta)$

Components:
- $J^0 = 2 C_0 (\dot{\theta} - \Omega)$
- $\mathbf{J} = 2 \kappa \nabla \theta$

Conservation law: $\partial_\mu J^\mu = 0$

This represents conservation of global phase flux.

## 12. Hamiltonian Density
Canonical momenta:
- $\pi_\theta = 2 C_0 (\dot{\theta} - \Omega)$
- $\pi_G = 2 \alpha (\dot{G} - \nabla^2 \theta)$

Hamiltonian density:
$H = C_0 (\dot{\theta} - \Omega)^2 + \kappa (\nabla \theta)^2 + \alpha (\dot{G} - \nabla^2 \theta)^2 + V_\Omega(\Omega)$

All terms are non-negative: $H \ge 0$, ensuring vacuum stability.

## 13. Knot Solutions (Matter)
Matter corresponds to localized phase structures in the coherence field.

Example radial ansatz:
$\theta_{\rm knot}(r) = \Theta_0 \exp(-r^2 / 2 R^2)$

Energy arises from gradient energy:
$E = \int \kappa (\nabla \theta)^2 \, d^3x$

These structures behave as particle-like solitons.

## 14. Knot Stability
A stable knot occurs when $dE/dR = 0$.

The Ω-cap imposes a minimum size: $R_{\rm crit} \sim \kappa / \Omega_{\rm max}$

Knots smaller than this radius cannot exist.

## 15. Gravity as Phase Gradient
Define $\lambda = \nabla \theta$

Acceleration of matter: $a = -\chi \nabla \theta$

The coupling constant $\chi = (c^2 \kappa) / (C_0 \Omega_{\rm max})$ connects the field theory to gravitational dynamics.

## 16. Black Holes Without Singularities
In TCWT singularities cannot form.

Instead a black hole corresponds to a saturated knot where $|\nabla \theta| \to \Omega_{\rm max} / \kappa$

The Ω-cap prevents further growth. This produces a phase-opaque region rather than infinite density.

## 17. Dark Matter
Dark matter corresponds to phase-opaque knots where $|\nabla \theta| \gtrsim \Omega_{\rm max} / \kappa$

These structures produce gravitational fields, interact weakly with radiation, and remain stable over cosmological times.

## 18. Dark Energy
Slow relaxation of phase curvature through the ghost field produces vacuum pressure.

Low-energy relation: $\dot{G} \approx \nabla^2 \theta$

This leakage acts as a small background expansion force.

## 19. Cosmological Interpretation
The universe evolves through phases of knot formation and decay:

Hum (coherent vacuum) → Phase instability → Rapid knot formation → Energy release (Big Bang) → Matter-dominated universe → Gradual knot unwinding → Return toward Hum coherence

The Big Bang therefore represents a large-scale phase instability, not a singular origin.

## 20. Entropy in TCWT
The Hum is the most ordered state of the system.

Knots store distortion energy in the phase field.

Entropy corresponds to knot relaxation: $E_{\rm knot} \to 0$

The long-term evolution of the universe tends toward the coherent background state.

## 21. Covariant Formulation (Recommended)
For relativistic symmetry the Lagrangian can be written as

$C (\partial_\mu \theta - U_\mu)^2$

where $U_\mu = (\Omega_{\rm hum}, 0, 0, 0)$ represents the background Hum flow.

This preserves Lorentz symmetry in the low-energy limit.

## 22. Summary
TCWT describes reality as a coherence field with an oscillatory vacuum.

From this structure emerge:
- matter as phase knots
- gravity from phase gradients
- dark matter from opaque knots
- dark energy from ghost leakage
- a cosmology driven by knot formation and decay

The governing Lagrangian remains

$L = C_0 (\dot{\theta} - \Omega)^2 - \kappa (\nabla \theta)^2 - \alpha (\dot{G} - \nabla^2 \theta)^2 - V_\Omega(\Omega)$

from which the observable universe emerges as a dynamic structure within the background Hum.
