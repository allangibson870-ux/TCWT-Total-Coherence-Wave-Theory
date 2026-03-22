# TCWT Master Lagrangian  
**Pregeometric Hum Field Formulation**  
**Version:** 2026.9  
**Status:** Core Theoretical Framework

## 1. Fundamental Fields

Total Coherence Wave Theory (**TCWT**) describes all physical phenomena as excitations of a coherent phase field called the **Hum**.

There is **no metric** and **no curvature tensor** at the fundamental level.  
Geometry, gravity, and cosmic expansion **emerge** from the dynamics of the Hum field.

The fundamental degrees of freedom are:

| Field          | Description                  |
|----------------|------------------------------|
| $\theta(x,t)$  | Hum phase field              |
| $\Omega(x,t)$  | Local oscillation frequency  |
| $G(x,t)$       | Ghost-leakage field          |

All observable physics arises from interactions among these three fields.

## 2. Coherent Hum Vacuum

The coherent vacuum state is defined by

$$
\theta_0(t) = \Omega_{\rm hum}\, t
$$

where $\Omega_{\rm hum}$ is the fundamental Hum frequency.

Small deviations from this state generate:

- matter
- gravity
- waves
- dark-matter-like distortions
- dark-energy-like relaxation

## 3. Master Lagrangian

The TCWT dynamics follow from the Lagrangian density

$$
\begin{aligned}
\mathcal{L} ={}& C_0 (\partial_t \theta - \Omega)^2 \\
& - \kappa a_0^2 \, F\!\left( \frac{|\nabla \theta|^2}{a_0^2} \right) \\
& - \alpha (\partial_t G - \nabla^2 \theta)^2 \\
& - V_\Omega(\Omega),
\end{aligned}
$$

with constants:

- $C_0$ — temporal coherence constant  
- $\kappa$ — spatial phase stiffness  
- $a_0$ — MOND acceleration scale  
- $\alpha$ — ghost-leakage coupling

This is a nonlinear scalar-field theory with:

- a MOND-like gradient sector  
- a curvature-leakage relaxation channel  
- **no metric**  
- **no Einstein–Hilbert term**

## 4. Nonlinear Gradient Function

The spatial term uses the MOND-motivated function

$$
F(x) = x + \frac{2}{3} x^{3/2}
$$

Its derivative defines the interpolation function

$$
\mu(x) = \frac{dF}{dx} = 1 + \sqrt{x}
$$

This produces:

- Newtonian behaviour at high accelerations  
- MOND-like behaviour at low accelerations

## 5. Euler–Lagrange Field Equations

### 5.1 Lagrangian Density (recap)

$$
\begin{aligned}
\mathcal{L} ={}& C_0 (\partial_t \theta - \Omega)^2
    - \kappa a_0^2 \, F\!\left( \frac{|\nabla \theta|^2}{a_0^2} \right) \\
& - \alpha (\partial_t G - \nabla^2 \theta)^2
    - V_\Omega(\Omega)
\end{aligned}
$$

with

$$
F(x) = x + \frac{2}{3} x^{3/2}, \qquad \mu(x) = 1 + \sqrt{x}.
$$

A simple choice for the $\Omega$-potential is

$$
V_\Omega(\Omega) = \frac{1}{2} m_\Omega^2 (\Omega - \Omega_{\rm hum})^2.
$$

### 5.2 Field Equations

**1. Hum Phase Field Equation ($\theta$)**

$$
2 C_0 \partial_t (\partial_t \theta - \Omega)
- \nabla \cdot \left[ \kappa \mu\!\left( \frac{|\nabla \theta|}{a_0} \right) \nabla \theta \right]
+ 2 \alpha \nabla^2 (\partial_t G - \nabla^2 \theta) = 0.
$$

**2. Frequency Field Equation ($\Omega$)**

$$
-2 C_0 (\partial_t \theta - \Omega) + \frac{d V_\Omega}{d \Omega} = 0.
$$

For the quadratic potential:

$$
2 C_0 (\Omega - \partial_t \theta) + m_\Omega^2 (\Omega - \Omega_{\rm hum}) = 0.
$$

**3. Ghost-Leakage Field Equation ($G$)**

$$
\partial_t \Bigl[ 2 \alpha (\partial_t G - \nabla^2 \theta) \Bigr] = 0.
$$

In the low-energy regime:

$$
\partial_t G \approx \nabla^2 \theta.
$$

This term governs curvature leakage and emergent dark-energy-like behaviour.

## 6. Weak-Field and Quasistatic Limit

Assumptions:

- $\partial_t^2 \theta \approx 0$, $\partial_t G \approx 0$  
- ghost-leakage channel is slow: $\partial_t G - \nabla^2 \theta \approx 0$

The Hum phase equation reduces to

$$
\nabla \cdot \left[ \kappa \mu\!\left( \frac{|\nabla \theta|}{a_0} \right) \nabla \theta \right] = \rho_{\rm eff},
$$

where $\rho_{\rm eff}$ is an effective source term (matter knots + phase distortions).

Gravitational acceleration is defined as

$$
\mathbf{a} = -\chi \nabla \theta.
$$

## 7. Newtonian Limit

Strong-field regime ($|\nabla \theta| \gg a_0$):

$$
\mu(x) \to 1 \quad \Rightarrow \quad \kappa \nabla^2 \theta \approx \rho_{\rm eff}.
$$

Identifying $\rho_{\rm eff} \propto \rho$ gives a Poisson-like equation and Newtonian gravity with effective $G$.

## 8. MOND Regime

Weak-field regime ($|\nabla \theta| \ll a_0$):

$$
\mu(x) \approx \sqrt{x} = \frac{|\nabla \theta|}{a_0}.
$$

The equation becomes

$$
\nabla \cdot \left[ \left( \frac{|\nabla \theta|}{a_0} \right) \nabla \theta \right] = \rho_{\rm eff},
$$

yielding flat rotation curves without dark matter.

## 9. Energy Density of the Hum–Ghost System

Effective energy density (non-relativistic regime):

$$
\mathcal{E} = C_0 (\partial_t \theta - \Omega)^2
+ \kappa a_0^2 F\!\left( \frac{|\nabla \theta|^2}{a_0^2} \right)
+ \alpha (\partial_t G - \nabla^2 \theta)^2
+ V_\Omega(\Omega).
$$

Contributions:

- Hum temporal coherence: $C_0 (\partial_t \theta - \Omega)^2$  
- Hum gradient (gravity/MOND): $\kappa a_0^2 F(\dots)$  
- Ghost leakage (curvature relaxation): $\alpha (\partial_t G - \nabla^2 \theta)^2$  
- Frequency potential: $V_\Omega(\Omega)$

Energy slowly transfers from gradient → ghost sector → dark-energy-like behaviour.

## 10. Matter Knots (Phase Solitons)

Localized matter = stable solitons, e.g.

$$
\theta_{\rm knot}(r) = \Theta_0 \exp\!\left( -\frac{r^2}{2 R^2} \right).
$$

Matter is a **phase configuration**, not an added substance.

## 11. Gravitational Waves

Linear perturbations $\delta\theta$ obey

$$
\square \delta\theta = 0
$$

→ Hum-phase gravitational waves propagating at speed $c$.

## 12. Ghost Leakage and Dark Energy

$$
\rho_G = \alpha (\partial_t G - \nabla^2 \theta)^2
$$

behaves as time-varying dark-energy-like component.

## 13. Cosmological Background (Metric-Free)

Cosmic expansion defined by

$$
H^2(t) = \frac{\rho_G(t)}{3 M_{\rm eff}^2}, \qquad \rho_G(t) = \alpha (\nabla^2 \theta)^2.
$$

$$
H(t) \propto |\nabla^2 \theta|.
$$

Acceleration = direct consequence of curvature leakage.

## 14. Linear Perturbations (Metric-Free)

$$
\ddot{\delta\theta} + \Gamma(t) \dot{\delta\theta} - c_s^2(t) \nabla^2 \delta\theta + m_{\rm eff}^2(t) \delta\theta = 0.
$$

Density contrast: $\delta \rho \propto \nabla^2 \delta\theta$.

Growth equation:

$$
\ddot{\delta} + 2 H \dot{\delta} - 4\pi G_{\rm eff}(t) \rho \delta + \mathcal{F}_{\rm leak}(t) \delta = 0.
$$

## 15. Interpretation Summary

| Phenomenon          | TCWT Interpretation                     |
|---------------------|------------------------------------------|
| Matter              | Phase solitons                           |
| Gravity             | Phase-gradient acceleration              |
| Dark Matter         | Opaque phase distortions                 |
| Dark Energy         | Ghost-leakage relaxation                 |
| Gravitational Waves | Hum phase oscillations                   |
| Cosmic Expansion    | Ghost-leakage energy                     |

## 16. Emergent Gravitational Lensing

Light follows Fermat’s principle with variable effective refractive index:

$$
n(x) = 1 + \frac{2 \chi}{c^2} \theta(x).
$$

Deflection angle:

$$
\alpha = -\int_{-\infty}^{\infty} \frac{1}{n} \nabla_\perp n \, ds.
$$

**Regimes:**

- Strong field ($|\nabla\theta| \gg a_0$): recovers Einsteinian $\alpha \approx \frac{4GM}{b c^2}$  
- Weak field ($|\nabla\theta| \ll a_0$): extra term $\sim \frac{2\pi G M}{a_0 c^2 b}$

The extra term explains galactic lensing without dark matter — purely from nonlinear Hum gradient stiffness.

## 17. Cosmological Picture

The universe emerges from large-scale Hum instabilities → relaxes toward coherent vacuum → ghost leakage drives acceleration → matter forms as phase knots → gravity from gradients → no fundamental dark matter or fixed cosmological constant.

**TCWT is fully pregeometric and metric-free**: all geometry and dynamics **emerge** from the Hum field.
