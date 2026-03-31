# TCWT Pregeometric Lagrangian (Corrected & MOND-Extended)
**Version: 2026.7 + MOND Extension (2026.9)**  
**Status: Corrected field equations, Newtonian limit derivation + full MOND interpolation included**

## 1. Fundamental Fields
Total Coherence Wave Theory (TCWT) describes physics in terms of a coherence phase field.

**Primary fields:**

| Field          | Meaning                        |
|----------------|--------------------------------|
| $\theta(x,t)$  | Coherence phase field          |
| $\Omega(x,t)$  | Informational drag density     |
| $G(x,t)$       | Ghost / leakage regulator      |

Derived quantity: $\lambda = \nabla \theta$, which represents the phase gradient responsible for gravitational acceleration.

## 2. Hum Vacuum State
The vacuum of TCWT is a coherent oscillation called the Hum.

Background solution: $\theta_0(t) = \Omega_{\rm hum} t$

Perturbations describe physical structure:  
$\theta(x,t) = \theta_0(t) + \delta\theta(x,t)$

Matter corresponds to localized phase knots in $\delta\theta$.

## 3. Pregeometric Lagrangian Density (MOND-Extended)
The TCWT Lagrangian density is

$L = C_0 (\partial_t \theta - \Omega)^2 - \kappa a_0^2 F\left( \frac{|\nabla \theta|^2}{a_0^2} \right) - \alpha (\partial_t G - \nabla^2 \theta)^2 - V_\Omega(\Omega)$,

where the MOND nonlinear function is

$F(x) = x + \frac{2}{3} x^{3/2}$, $\quad \mu(x) = \frac{dF}{dx} = 1 + \sqrt{x}$.

**Constants:**

| Constant | Meaning                        |
|----------|--------------------------------|
| $C_0$    | Temporal coherence coefficient |
| $\kappa$ | Spatial phase stiffness        |
| $\alpha$ | Ghost coupling strength        |
| $a_0$    | MOND acceleration scale        |

**Ω-Cap Potential:**
$V_\Omega(\Omega) = \frac{\lambda_\Omega}{4} (\Omega^2 - \Omega_{\rm max}^2)^2$

This prevents runaway gradients and eliminates singularities.

## 4. Action
The full action of the theory is

$S = \int L \, d^3x \, dt$

All field equations are obtained by requiring the variation of the action to vanish: $\delta S = 0$.

## 5. Euler–Lagrange Equation (general form)
For a generic field $\phi$, the Euler–Lagrange equation reads:

$\frac{\partial L}{\partial \phi} - \partial_\mu \left( \frac{\partial L}{\partial (\partial_\mu \phi)} \right) + \partial_\mu \partial_\nu \left( \frac{\partial L}{\partial (\partial_\mu \partial_\nu \phi)} \right) = 0$

Higher-order derivatives appear due to the $\nabla^2 \theta$ term inside the ghost-leakage sector.

## 6. Phase Field Equation (with MOND term)
Variation of the action with respect to $\theta$ yields the fundamental propagation equation for the phase field:

$2 C_0 \partial_t (\partial_t \theta - \Omega) - \nabla \cdot \Bigl[ \kappa \mu\left( \frac{|\nabla \theta|}{a_0} \right) \nabla \theta \Bigr] - 2 \alpha \nabla^2 (\partial_t G - \nabla^2 \theta) = 0$.

This is the core dynamical equation of TCWT.

## 7. Informational Drag Equation
Variation with respect to $\Omega$:

$-2 C_0 (\partial_t \theta - \Omega) - \frac{d V_\Omega}{d \Omega} = 0$.

Low-energy regime: $\Omega \approx \partial_t \theta$

Cap regime (saturation): $\Omega \to \Omega_{\rm max}$

## 8. Ghost Field Equation
Variation with respect to $G$:

$\partial_t [ 2 \alpha (\partial_t G - \nabla^2 \theta) ] = 0$.

Low-energy approximation: $\partial_t G \approx \nabla^2 \theta$

This slow leakage channel is associated with emergent dark-energy-like behaviour.

## 9. Knot Solutions (Matter)
Matter corresponds to localized phase structures.

Example Gaussian solution:  
$\theta_{\rm knot}(r) = \Theta_0 \exp(-r^2 / (2 R^2))$

Gradient energy (nonlinear form):  
$E = \int \kappa a_0^2 F\left( \frac{|\nabla \theta|^2}{a_0^2} \right) d^3x$

These behave as particle-like solitons.

## 10. Gravity from Phase Gradients
Test-particle acceleration is defined by

$a = -\chi \nabla \theta$, $\quad \chi = c^2 \kappa / (C_0 \Omega_{\rm max})$

This links the phase field directly to gravitational acceleration.

## 11. Newtonian + MOND Limits

**Strong-field (Newtonian) regime** ($|\nabla \theta| \gg a_0$):  
$\mu(x) \to 1$ → reduces to $\kappa \nabla^2 \theta \approx \rho_{\rm eff}$

**Weak-field (MOND) regime** ($|\nabla \theta| \ll a_0$):  
$\mu(x) \approx \sqrt{x} = |\nabla \theta| / a_0$ →  
$\nabla \cdot \left[ \left( \frac{|\nabla \theta|}{a_0} \right) \nabla \theta \right] = \frac{\rho_{\rm eff}}{\kappa}$

This yields flat rotation curves without dark matter.

## 12. Mapping to the Gravitational Potential
Define the gravitational potential $\Phi = \chi \theta$

Then $\nabla^2 \Phi = \chi \nabla^2 \theta$

Substituting the Newtonian-limit field equation gives

$\nabla^2 \Phi = 4\pi G \rho$, $\quad G = \chi / (4\pi \kappa)$

Thus TCWT reproduces the Newtonian Poisson equation $\nabla^2 \Phi = 4\pi G \rho$.

## 13. Newtonian Acceleration Law
Acceleration becomes $a = -\nabla \Phi$, which yields the standard inverse-square law

$a(r) = -G M / r^2$

for a localized knot mass $M$.

## 14. Interpretation
In TCWT:
- gravity is not curvature of spacetime directly,
- it arises from phase gradients in the coherence field generated by knot structures,
- spacetime curvature appears as an emergent macroscopic description of these gradients.

## 15. Singularities Avoided
The Ω-cap limits the maximum phase gradient: $|\nabla \theta| \leq \Omega_{\rm max} / \kappa$

Therefore:
- no curvature singularities,
- no infinite-density black holes,
- collapse stops at a finite knot core.

## 16. Cosmological Interpretation
The universe evolves through knot formation and decay:

Hum vacuum → phase instability → knot creation → energy release (Big Bang analogue) → matter-dominated universe → gradual knot relaxation.

Entropy corresponds to the unwinding of phase knots, returning the system toward the coherent Hum state.

## 17. Simple Numerical Toy Model – Gaussian Knot + Energy & Acceleration Profile
Goal: Simulate a single 2D radial Gaussian knot, compute total gradient energy (linear vs. full MOND), Newtonian acceleration profile, full MOND-nonlinear acceleration profile, and toy rotation curve.

**Runnable Python code (copy-paste ready):**

```python
import numpy as np
import matplotlib.pyplot as plt

# ================== PARAMETERS ==================
Theta0 = 5.0          # amplitude
R      = 1.0          # knot radius
kappa  = 1.0
a0     = 1.0          # MOND scale
chi    = 1.0          # coupling constant

# Grid (radial, avoid r=0 singularity)
r  = np.linspace(0.01, 8, 800)
dr = r[1] - r[0]

# Gaussian knot phase
theta = Theta0 * np.exp(-r**2 / (2 * R**2))

# |∇θ| magnitude (radial derivative)
grad_theta = Theta0 * (r / R**2) * np.exp(-r**2 / (2 * R**2))

# ================== ENERGY ==================
# Linear (quadratic) gradient energy
E_linear = kappa * np.trapz(2 * np.pi * r * grad_theta**2, r)

# Full MOND energy using F(x)
x = (grad_theta / a0)**2
F = x + (2/3) * x**1.5
E_mond = kappa * a0**2 * np.trapz(2 * np.pi * r * F, r)

print(f"Total gradient energy (linear approx): {E_linear:.3f}")
print(f"Total gradient energy (full MOND):    {E_mond:.3f}")

# ================== ACCELERATION ==================
accel_newton = chi * grad_theta
mu           = 1 + np.sqrt(x)               # interpolation function
accel_mond   = chi * mu * grad_theta        # effective acceleration

# ================== PLOTS ==================
fig, axs = plt.subplots(2, 2, figsize=(12, 9))

axs[0,0].plot(r, theta)
axs[0,0].set_title('Phase profile θ(r)')
axs[0,0].set_xlabel('r'); axs[0,0].grid(alpha=0.3)

axs[0,1].plot(r, grad_theta)
axs[0,1].set_title('Phase gradient |∇θ|(r)')
axs[0,1].set_xlabel('r'); axs[0,1].grid(alpha=0.3)

axs[1,0].plot(r, accel_newton, label='Newtonian')
axs[1,0].plot(r, accel_mond, '--', label='MOND effective')
axs[1,0].set_title('Acceleration profile a(r)')
axs[1,0].set_xlabel('r'); axs[1,0].legend(); axs[1,0].grid(alpha=0.3)

axs[1,1].plot(r, mu)
axs[1,1].set_title('Interpolation μ(x)')
axs[1,1].set_xlabel('r'); axs[1,1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Bonus: toy rotation curve (v²/r = |a|)
v_newton = np.sqrt(accel_newton * r)
v_mond   = np.sqrt(accel_mond   * r)

plt.figure(figsize=(8,5))
plt.plot(r, v_newton, label='Newtonian (falls off)')
plt.plot(r, v_mond, '--', label='MOND (flattens)')
plt.xlabel('r'); plt.ylabel('circular velocity v'); plt.legend()
plt.title('Toy Rotation Curve Demonstration')
plt.grid(alpha=0.3)
plt.show()
