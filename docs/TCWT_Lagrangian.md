# TCWT Lagrangian  
## Core Pregeometric Field Theory of the Hum, MOND, Ghost Sector, and Knot Matter  
Version: 2026.9  
Status: Consolidated, MOND‑extended, covariant‑ready

---

# 1. Overview

Total Coherence Wave Theory (TCWT) describes the universe as a nonlinear coherence field whose vacuum is an eternal oscillation called the **Hum**.

| Concept | Meaning |
|--------|---------|
| Hum | coherent oscillatory vacuum |
| knots | localized phase structures (matter) |
| phase gradients | gravity |
| ghost leakage | dark energy |
| opaque knots | dark matter |

Spacetime and gravity emerge from the dynamics of a fundamental phase field.

---

# 2. Fundamental Fields

TCWT uses three scalar fields:

| Field | Meaning |
|-------|---------|
| $\theta(x,t)$ | coherence phase field |
| $\Omega(x,t)$ | informational drag density |
| $G(x,t)$ | ghost / leakage regulator |

Derived quantity:

$$\lambda = \nabla \theta$$

which produces gravitational acceleration.

---

# 3. Hum Vacuum

The vacuum is not $\theta = 0$ but a coherent oscillation:

$$\theta_0(t) = \Omega_{\rm hum} t$$

Physical structure arises from perturbations:

$$\theta(x,t) = \theta_0(t) + \delta\theta(x,t)$$

Matter corresponds to localized knots in $\delta\theta$.

---

# 4. TCWT Lagrangian (MOND‑Extended)

The pregeometric Lagrangian density is:

$$L = C_0(\dot\theta - \Omega)^2 - \kappa a_0^2 F(|\nabla\theta|^2 / a_0^2) - \alpha(\dot G - \nabla^2\theta)^2 - V_\Omega(\Omega)$$

with MOND function:

$$F(x) = x + \frac{2}{3} x^{3/2}, \quad \mu(x) = 1 + x$$

Constants:

| Constant | Meaning |
|----------|---------|
| $C_0$ | temporal coherence |
| $\kappa$ | spatial phase stiffness |
| $\alpha$ | ghost coupling |
| $a_0$ | MOND acceleration scale |

Ω‑cap potential:

$$V_\Omega(\Omega) = \lambda_\Omega^4 (\Omega^2 - \Omega_{\max}^2)^2$$

This prevents runaway gradients and removes singularities.

---

# 5. Action and Variational Principle

The action is:

$$S = \int L \, d^3x \, dt$$

Field equations follow from $\delta S = 0$.

Higher derivatives appear due to the $\nabla^2\theta$ term.

---

# 6. Field Equations

## 6.1 Phase Field Equation

$$2C_0 \partial_t(\dot\theta - \Omega) - \nabla \cdot [\kappa \mu(|\nabla\theta|/a_0)\nabla\theta] - 2\alpha \nabla^2(\dot G - \nabla^2\theta) = 0$$

This is the core dynamical equation of TCWT.

## 6.2 Informational Drag Equation

$$-2C_0(\dot\theta - \Omega) - V_\Omega'(\Omega) = 0$$

Low‑energy: $\Omega \approx \dot\theta$  
Cap regime: $\Omega \to \Omega_{\max}$

## 6.3 Ghost Field Equation

## Ghost Sector: Full Equation of Motion

The ghost field $G$ encodes curvature storage and relaxation in TCWT. Its dynamics follow from the curvature‑penalty term in the action, which enforces that the ghost sector tracks the Laplacian of the Hum phase.

### Ghost Lagrangian

The ghost contribution to the TCWT action is

$$ \mathcal{L}_G = \alpha\,(\dot{G} - \nabla^2\theta)^2, $$

where $\alpha$ sets the strength of curvature storage.

### Variation and Euler–Lagrange Equation

Varying the action with respect to $G$ gives

$$ \partial_t\big[2\alpha(\dot{G} - \nabla^2\theta)\big] = 0. $$

This states that the curvature‑excess quantity

$$ T = \dot{G} - \nabla^2\theta $$

is locally conserved in time in the absence of damping or external sources.

### Full Ghost PDE with Relaxation

To allow realistic relaxation of curvature excess, introduce a damping coefficient $\gamma > 0$. The full equation of motion becomes

$$ \partial_t\big[2\alpha(\dot{G} - \nabla^2\theta)\big] = -\gamma(\dot{G} - \nabla^2\theta). $$

Expanding this gives the driven, damped second‑order PDE

$$ 2\alpha\,\ddot{G} + \gamma\,\dot{G} = 2\alpha\,\partial_t(\nabla^2\theta) + \gamma\,\nabla^2\theta. $$

This is the complete ghost‑sector evolution equation in TCWT.

### Leakage Limit

In the low‑frequency or relaxed regime, the second‑order and time‑derivative curvature terms are negligible, giving the leakage approximation

$$ \dot{G} \approx \nabla^2\theta. $$

This is the regime used in the strong‑field reduction and in the $\lambda/T$ diagnostic maps.


---

# 7. Hamiltonian Formulation

Canonical momenta:

$$\pi_\theta = 2C_0(\dot\theta - \Omega)$$  
$$\pi_G = 2\alpha(\dot G - \nabla^2\theta)$$  
$$\pi_\Omega = 0$$

Primary constraint: $\pi_\Omega \approx 0$.

Reduced Hamiltonian:

$$H_{\rm red} = \int d^3x \left[ \frac{\pi_\theta^2}{4C_0} + \kappa a_0^2 F(|\nabla\theta|^2/a_0^2) + \alpha(\nabla^2\theta)^2 + V_\Omega(\Omega(\pi_\theta)) \right]$$

All terms are non‑negative → **no Ostrogradsky ghosts**.

---

# 8. Noether Current (Phase Flux)

Global shift symmetry $\theta \to \theta + \epsilon$ gives:

$$J^0 = 2C_0(\dot\theta - \Omega)$$  
$$\mathbf{J} = 2\kappa \nabla\theta$$  
$$\partial_\mu J^\mu = 0$$

This is conservation of global phase flux.

---

# 9. Gravity from Phase Gradients

Define:

$$a = -\chi \nabla\theta$$  
$$\chi = \frac{c^2 \kappa}{C_0 \Omega_{\max}}$$

Define gravitational potential:

$$\Phi = \chi \theta$$

Then:

$$\nabla^2\Phi = \chi \nabla^2\theta$$

TCWT reproduces the Newtonian Poisson equation:

$$\nabla^2\Phi = 4\pi G \rho$$

with:

$$G = \frac{\chi}{4\pi\kappa}$$

---

# 10. Newtonian and MOND Limits

Strong field ($|\nabla\theta| \gg a_0$):

$$\mu(x) \to 1$$  
Newtonian gravity recovered.

Weak field ($|\nabla\theta| \ll a_0$):

$$\mu(x) \approx x = |\nabla\theta|/a_0$$  
$$\nabla \cdot[(|\nabla\theta|/a_0)\nabla\theta] = \rho/\kappa$$

This yields flat rotation curves and the baryonic Tully–Fisher relation.

---

# 11. Knot Matter (Solitons)

Example Gaussian knot:

$$\theta_{\rm knot}(r) = \Theta_0 \exp(-r^2 / 2R^2)$$

Gradient energy:

$$E = \int \kappa a_0^2 F(|\nabla\theta|^2/a_0^2) \, d^3x$$

Stability condition:

$$\frac{dE}{dR} = 0$$

Ω‑cap imposes minimum radius:

$$R_{\rm crit} \sim \kappa / \Omega_{\max}$$

Opaque knots behave as dark matter.

---

# 12. Black Holes Without Singularities

Maximum gradient:

$$|\nabla\theta| \le \Omega_{\max}/\kappa$$

Collapse saturates at finite density → **no singularities**.

Black holes are **phase‑opaque knots**, not infinite curvature.

---

# 13. Dark Energy from Ghost Leakage

Low‑energy ghost equation:

$$\dot G \approx \nabla^2\theta$$

This slow relaxation produces vacuum pressure → dark‑energy‑like acceleration.

---

# 14. Cosmological Interpretation (Background Only)

Universe evolves through:

Hum vacuum → phase instability → knot formation → energy release → matter era → knot relaxation → return to coherence.

Entropy corresponds to knot unwinding.

---

# 15. Planck Scale and Holographic Relation

Minimum correlation length:

$$L_{\min} \propto \sqrt{\alpha \kappa}$$

Planck length emerges from:

$$\ell_P^2 \sim \alpha / \kappa$$

Gravity is information pressure resisting Ω‑cap saturation.

---

# 16. Ghost–MOND–Hubble Unification

Ghost coupling from MOND:

$$\alpha \approx \kappa^2 / (2 a_0^2 C_0)$$

Ghost coupling from Hubble tension:

$$\alpha \approx \rho_{\rm info} / H_0^4$$

Holographic relation:

$$\ell_P^2 \sim \alpha / \kappa$$

Together:

- $a_0$ (galaxies)  
- $H_0$ (cosmology)  
- $\ell_P$ (quantum gravity)  

are unified by the same parameter $\alpha$.

---

# 17. Mass‑Lock and Fine‑Structure Constant

Electron mass scaling:

$$m_e \propto \alpha / R^3$$  
$$R \propto (\kappa/\alpha)^{1/4}$$  
$$m_e \propto 1/H_0^2$$

Fine‑structure constant:

$$\alpha_{\rm em} \approx 1/137$$

arises as a soliton self‑consistency number.

---

# 18. Worked Examples

## 18.1 Rotation Curve

MOND‑regime equation:

$$\nabla \cdot[\mu(|\nabla\theta|/a_0)\nabla\theta] = \rho/\kappa$$

In vacuum:

$$\theta' \propto 1/r$$  
$$a = -\chi \theta' \propto 1/r$$  
$$v^2 = \text{constant}$$

## 18.2 Gravitational Lensing

Refractive index:

$$n(x) = 1 + (2\chi/c^2)\theta(x)$$

Deflection angle:

$$\alpha \approx -(2\chi/c^2)\int \nabla_\perp\theta \, ds$$

TCWT predicts enhanced lensing without dark matter.

---



