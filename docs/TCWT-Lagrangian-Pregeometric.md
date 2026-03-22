# TCWT Pregeometric Lagrangian (Corrected & MOND-Extended)
**Version:** 2026.7 + MOND Extension (2026.9)  
**Status:** Corrected field equations, Newtonian limit + full MOND interpolation included

## 1. Fundamental Fields

Total Coherence Wave Theory (**TCWT**) describes physics in terms of a coherence phase field.

**Primary fields:**

| Field         | Meaning                       |
|---------------|-------------------------------|
| $\theta(x,t)$ | Coherence phase field         |
| $\Omega(x,t)$ | Informational drag density    |
| $G(x,t)$      | Ghost / leakage regulator     |

**Derived quantity:** $\lambda = \nabla \theta$ (phase gradient responsible for gravitational acceleration).

## 2. Hum Vacuum State

Background solution:  
$$
\theta_0(t) = \Omega_{\rm hum}\, t
$$

Perturbations:  
$$
\theta(x,t) = \theta_0(t) + \delta\theta(x,t)
$$

Matter = localized phase knots in $\delta\theta$.

## 3. Pregeometric Lagrangian Density (MOND-Extended)

$$
\begin{aligned}
\mathcal{L} ={}& C_0 (\partial_t \theta - \Omega)^2 \\
& - \kappa a_0^2 \, F\!\left( \frac{|\nabla \theta|^2}{a_0^2} \right) \\
& - \alpha (\partial_t G - \nabla^2 \theta)^2 \\
& - V_\Omega(\Omega),
\end{aligned}
$$

where the **MOND nonlinear function** is

$$
F(x) = x + \frac{2}{3} x^{3/2}, \qquad \mu(x) = \frac{dF}{dx} = 1 + \sqrt{x}.
$$

**Constants:** $C_0$, $\kappa$, $\alpha$, $a_0$ (MOND scale).

**Ω-Cap Potential:**  
$$
V_\Omega(\Omega) = \frac{\lambda_\Omega}{4} (\Omega^2 - \Omega_{\rm max}^2)^2.
$$

## 4.–6. Action and General Euler–Lagrange (unchanged from previous)

## 7. Phase Field Equation (with MOND term)

$$
2 C_0 \partial_t (\partial_t \theta - \Omega) 
- \nabla \cdot \Bigl[ \kappa \mu\!\left( \frac{|\nabla \theta|}{a_0} \right) \nabla \theta \Bigr]
- 2 \alpha \nabla^2 (\partial_t G - \nabla^2 \theta) = 0.
$$

## 8.–9. Ω and Ghost Equations (unchanged)

## 10. Knot Solutions (Matter)

Example Gaussian knot (2D or 3D):

$$
\theta_{\rm knot}(r) = \Theta_0 \exp\!\left( -\frac{r^2}{2 R^2} \right)
$$

Gradient energy now uses the full nonlinear $F$.

## 11. Gravity from Phase Gradients

$$
\mathbf{a} = -\chi \nabla \theta, \qquad \chi = \frac{c^2 \kappa}{C_0 \Omega_{\rm max}}.
$$

## 12. Newtonian + MOND Limits

**Strong-field (Newtonian) regime** ($|\nabla \theta| \gg a_0$):  
$\mu(x) \to 1$ → recovers $\kappa \nabla^2 \theta \approx \rho_{\rm eff}$.

**Weak-field (MOND) regime** ($|\nabla \theta| \ll a_0$):  
$\mu(x) \approx \sqrt{x} = |\nabla \theta|/a_0$ →  
$$
\nabla \cdot \left[ \left( \frac{|\nabla \theta|}{a_0} \right) \nabla \theta \right] = \frac{\rho_{\rm eff}}{\kappa}
$$
→ flat rotation curves without dark matter.

## 13.–14. Mapping to Potential & Inverse-Square Law (Newtonian core unchanged; MOND extension above)

## 15.–17. Interpretation, Singularities, Cosmology (unchanged)

## 18. Simple Numerical Toy Model – Gaussian Knot + Energy & Acceleration Profile

**Toy model goal:** Simulate a single 2D Gaussian knot, compute  
- total gradient energy $E_{\rm grad}$  
- Newtonian acceleration profile  
- **full MOND-nonlinear acceleration profile**  
- visual plots (easy to run in < 30 lines)

### Runnable Python Code (copy-paste)

```python
import numpy as np
import matplotlib.pyplot as plt

# ================== PARAMETERS ==================
Theta0 = 5.0          # amplitude
R = 1.0               # knot radius
kappa = 1.0
a0 = 1.0              # MOND scale
chi = 1.0             # coupling

# Grid
r = np.linspace(0.01, 5, 500)
dr = r[1] - r[0]

# Gaussian knot (radial)
theta = Theta0 * np.exp(-r**2 / (2 * R**2))

# Gradient |∇θ|
grad_theta = Theta0 * (r / R**2) * np.exp(-r**2 / (2 * R**2))

# ================== ENERGY ==================
# Linear energy (for reference)
E_linear = kappa * np.trapz(2 * np.pi * r * grad_theta**2, r)   # 2πr dr integral

# Full MOND energy using F(x)
x = (grad_theta / a0)**2
F = x + (2/3) * x**1.5
E_mond = kappa * a0**2 * np.trapz(2 * np.pi * r * F, r)

print(f"Total gradient energy (linear): {E_linear:.3f}")
print(f"Total gradient energy (MOND):   {E_mond:.3f}")

# ================== ACCELERATION ==================
accel_newton = chi * grad_theta

mu = 1 + np.sqrt(x)          # interpolation
accel_mond = chi * mu * grad_theta   # effective g = χ μ |∇θ|

# ================== PLOTS ==================
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs[0,0].plot(r, theta); axs[0,0].set_title('Phase θ(r)'); axs[0,0].set_xlabel('r')
axs[0,1].plot(r, grad_theta); axs[0,1].set_title('|∇θ|(r)'); axs[0,1].set_xlabel('r')
axs[1,0].plot(r, accel_newton, label='Newtonian'); 
axs[1,0].plot(r, accel_mond, '--', label='MOND'); 
axs[1,0].set_title('Acceleration profile'); axs[1,0].legend(); axs[1,0].set_xlabel('r')
axs[1,1].plot(r, mu); axs[1,1].set_title('μ(x) interpolation'); axs[1,1].set_xlabel('r')

plt.tight_layout()
plt.show()

# Bonus: rotation curve v²/r = |a|
v_newton = np.sqrt(accel_newton * r)
v_mond   = np.sqrt(accel_mond * r)
plt.figure(); plt.plot(r, v_newton, label='Newton'); plt.plot(r, v_mond, '--', label='MOND flat-ish');
plt.xlabel('r'); plt.ylabel('v'); plt.legend(); plt.title('Toy Rotation Curve'); plt.show()
