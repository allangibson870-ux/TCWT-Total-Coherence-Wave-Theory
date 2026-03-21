# TCWT Master Lagrangian  
**Pregeometric Hum Field Formulation**  
**Version: 2026.9**  
**Status: Core Theoretical Framework**

---

# 1. Fundamental Fields

Total Coherence Wave Theory (TCWT) describes all physical phenomena as excitations of a coherent phase field called the **Hum**.  
There is **no metric** and **no curvature tensor** at the fundamental level.  
Geometry, gravity, and cosmic expansion emerge from the dynamics of the Hum field.

The fundamental degrees of freedom are:

| Field | Description |
|-------|-------------|
| \( \theta(x,t) \) | Hum phase field |
| \( \Omega(x,t) \) | Local oscillation frequency |
| \( G(x,t) \) | Ghost‑leakage field |

All observable physics arises from interactions among these fields.

---

# 2. Coherent Hum Vacuum

The coherent vacuum state is defined by

\[
\theta_0(t) = \Omega_{\rm hum}\, t,
\]

where \( \Omega_{\rm hum} \) is the fundamental Hum frequency.

Small deviations from this state generate:

- matter  
- gravity  
- waves  
- dark‑matter‑like distortions  
- dark‑energy‑like relaxation  

---

# 3. Master Lagrangian

The TCWT dynamics follow from the Lagrangian density

\[
\mathcal{L}
= C_0(\partial_t\theta - \Omega)^2
- \kappa a_0^2 F\!\left(\frac{|\nabla\theta|^2}{a_0^2}\right)
- \alpha(\partial_t G - \nabla^2\theta)^2
- V_\Omega(\Omega),
\]

with constants:

- \( C_0 \): temporal coherence constant  
- \( \kappa \): spatial phase stiffness  
- \( a_0 \): MOND acceleration scale  
- \( \alpha \): ghost‑leakage coupling  

This is a **nonlinear scalar‑field theory** with:

- a MOND‑like gradient sector  
- a curvature‑leakage relaxation channel  
- no metric  
- no Einstein–Hilbert term  

---

# 4. Nonlinear Gradient Function

The spatial term uses the MOND‑motivated function

\[
F(x) = x + \frac{2}{3}x^{3/2}.
\]

Its derivative defines the interpolation function

\[
\mu(x) = \frac{dF}{dx} = 1 + x^{1/2}.
\]

This produces:

- Newtonian behaviour at high accelerations  
- MOND‑like behaviour at low accelerations  

---

# 5. Euler–Lagrange Field Equations

## 5.1 Hum Phase Equation

# TCWT Master Lagrangian — Three-Field Dynamical System

## Lagrangian Density

\[
\mathcal{L} =
C_0(\partial_t\theta - \Omega)^2
- \kappa a_0^2 F\!\left(\frac{|\nabla\theta|^2}{a_0^2}\right)
+ \alpha(\partial_t G - \nabla^2\theta)^2
- V_\Omega(\Omega)
\]

with

\[
F(x) = x + \frac{2}{3}x^{3/2}, \qquad
\mu(x) = \frac{dF}{dx} = 1 + x^{1/2}.
\]

A simple choice for the Ω‑potential is

\[
V_\Omega(\Omega) = \frac{1}{2}m_\Omega^2(\Omega - \Omega_{\rm hum})^2.
\]

---

# Field Equations

## 1. Hum Phase Field Equation (θ)

\[
2C_0\,\partial_t(\partial_t\theta - \Omega)
- \nabla\cdot\!\left[
\kappa\,\mu\!\left(\frac{|\nabla\theta|}{a_0}\right)\nabla\theta
\right]
- 2\alpha\,\nabla^2(\partial_t G - \nabla^2\theta)
= 0.
\]

This is the primary dynamical equation of the Hum field.

---

## 2. Frequency Field Equation (Ω)

Variation with respect to Ω gives

\[
-2C_0(\partial_t\theta - \Omega)
- \frac{dV_\Omega}{d\Omega} = 0.
\]

For the quadratic potential above:

\[
2C_0(\Omega - \partial_t\theta)
+ m_\Omega^2(\Omega - \Omega_{\rm hum}) = 0.
\]

This relates the local oscillation frequency to the time‑derivative of the Hum phase.

---

## 3. Ghost‑Leakage Field Equation (G)

\[
\partial_t\left[2\alpha(\partial_t G - \nabla^2\theta)\right] = 0.
\]

In the low‑energy regime:

\[
\partial_t G \approx \nabla^2\theta.
\]

This term governs curvature‑leakage and the emergent dark‑energy‑like behaviour.

---

## 6. Weak-Field and Quasistatic Limit

In the nonrelativistic, quasistatic regime relevant for galaxies and bound systems, we assume:

- time derivatives are small compared to spatial variations:
  \[
  \partial_t^2\theta \approx 0, \qquad \partial_t G \approx 0,
  \]
- the ghost-leakage channel is slow:
  \[
  \partial_t G - \nabla^2\theta \approx 0.
  \]

Under these assumptions, the Hum phase equation reduces to

\[
\nabla\cdot\!\left[
\kappa\,\mu\!\left(\frac{|\nabla\theta|}{a_0}\right)\nabla\theta
\right]
= \rho_{\rm eff},
\]

where \(\rho_{\rm eff}\) is an effective source term encoding matter knots and phase distortions. This is the fundamental quasistatic field equation of TCWT.

The gravitational acceleration is defined by

\[
\mathbf{a} = -\chi\,\nabla\theta.
\]

---

## 7. Newtonian Limit

In the strong-field regime \(|\nabla\theta| \gg a_0\), the interpolation function tends to

\[
\mu(x) \to 1,
\]

and the field equation becomes approximately linear:

\[
\kappa\,\nabla^2\theta \approx \rho_{\rm eff}.
\]

Identifying \(\rho_{\rm eff}\) with the mass density \(\rho\) up to a constant factor, we obtain a Poisson-like equation

\[
\nabla^2\theta = \frac{\rho}{\kappa}.
\]

The acceleration

\[
\mathbf{a} = -\chi\,\nabla\theta
\]

then reproduces Newtonian gravity with an effective gravitational constant set by \(\chi\) and \(\kappa\).

---

## 8. MOND Regime

In the weak-field regime \(|\nabla\theta| \ll a_0\), the interpolation function behaves as

\[
\mu(x) \approx x^{1/2}
= \left(\frac{|\nabla\theta|}{a_0}\right).
\]

The quasistatic field equation becomes

\[
\nabla\cdot\left[
\left(\frac{|\nabla\theta|}{a_0}\right)\nabla\theta
\right]
= \rho_{\rm eff}.
\]

With \(\mathbf{a} = -\chi\,\nabla\theta\), this yields a MOND-like acceleration law that produces flat galactic rotation curves without invoking dark matter. The transition between the Newtonian and MOND regimes is controlled by the nonlinear function \(\mu(x)\) inherited from the TCWT Lagrangian.
---

## 9. Energy Density of the Hum–Ghost System

Although TCWT is pregeometric and does not assume a spacetime metric, the Lagrangian density still defines a natural energy density and energy flux for the Hum and ghost fields.

In the nonrelativistic regime, we define the effective energy density as

\[
\mathcal{E} =
C_0(\partial_t\theta - \Omega)^2
+ \kappa a_0^2 F\!\left(\frac{|\nabla\theta|^2}{a_0^2}\right)
+ \alpha(\partial_t G - \nabla^2\theta)^2
+ V_\Omega(\Omega).
\]

The four contributions are:

- Hum temporal coherence energy:
  \[
  \mathcal{E}_{\rm hum,time}
  = C_0(\partial_t\theta - \Omega)^2,
  \]
- Hum gradient (gravitational/MOND) energy:
  \[
  \mathcal{E}_{\rm hum,grad}
  = \kappa a_0^2 F\!\left(\frac{|\nabla\theta|^2}{a_0^2}\right),
  \]
- ghost‑leakage (curvature‑relaxation) energy:
  \[
  \mathcal{E}_{\rm ghost}
  = \alpha(\partial_t G - \nabla^2\theta)^2,
  \]
- frequency potential energy:
  \[
  \mathcal{E}_{\Omega}
  = V_\Omega(\Omega).
  \]

The total Hum–ghost energy density is

\[
\mathcal{E}_{\rm total}
= \mathcal{E}_{\rm hum,time}
+ \mathcal{E}_{\rm hum,grad}
+ \mathcal{E}_{\rm ghost}
+ \mathcal{E}_{\Omega}.
\]

In regions where the ghost‑leakage channel is active
\((\partial_t G - \nabla^2\theta \neq 0)\),
energy is slowly transferred from the Hum gradient sector into the ghost sector. This provides a natural interpretation of dark‑energy‑like behaviour as long‑timescale relaxation of stored Hum curvature energy.

# 10. Matter Knots (Phase Solitons)

Localized matter corresponds to stable soliton solutions:

\[
\theta_{\rm knot}(r)
= \Theta_0\,\exp\!\left(-\frac{r^2}{2R^2}\right).
\]

These represent:

- particles  
- stars  
- compact objects  

Matter is **not added** to the theory — it is a **phase configuration**.

---

# 11. Gravitational Waves

Linear perturbations

\[
\theta = \theta_0 + \delta\theta
\]

yield the wave equation

\[
\square\,\delta\theta = 0,
\]

with propagation speed \( c \).

These are **Hum‑phase gravitational waves**.

---

# 12. Ghost Leakage and Dark Energy

The ghost equation

\[
\partial_t G \approx \nabla^2\theta
\]

acts as a slow relaxation channel for curvature energy.

Define the **ghost‑leakage energy density**:

\[
\rho_G = \alpha(\partial_t G - \nabla^2\theta)^2.
\]

This behaves as a **time‑varying dark‑energy‑like component**.

---

# 13. Cosmological Background (Metric‑Free)

TCWT does **not** assume a metric or Einstein equations.

Cosmic expansion is defined by the **ghost‑leakage energy density**:

\[
H^2(t) = \frac{\rho_G(t)}{3M_{\rm eff}^2}.
\]

Here \( M_{\rm eff} \) is an emergent scale determined by the Hum field.

Since

\[
\partial_t G \approx \nabla^2\theta,
\]

we obtain

\[
\rho_G(t) = \alpha\left(\nabla^2\theta\right)^2.
\]

Thus:

\[
H(t) \propto |\nabla^2\theta|.
\]

Cosmic acceleration is therefore a **direct consequence of curvature leakage**.

---

# 14. Linear Perturbations (Metric‑Free)

Let

\[
\theta = \bar{\theta}(t) + \delta\theta(x,t).
\]

Linearizing the master equation gives

\[
\ddot{\delta\theta}
+ \Gamma(t)\dot{\delta\theta}
- c_s^2(t)\nabla^2\delta\theta
+ m_{\rm eff}^2(t)\delta\theta
= 0,
\]

where:

- \( \Gamma(t) \): damping from background relaxation  
- \( c_s^2(t) \): effective sound speed from gradient sector  
- \( m_{\rm eff}^2(t) \): curvature of the potential  

Density contrast is defined by

\[
\delta\rho \propto \nabla^2\delta\theta.
\]

This yields the **TCWT growth equation**:

\[
\ddot{\delta}
+ 2H\dot{\delta}
- 4\pi G_{\rm eff}(t)\rho\,\delta
+ \mathcal{F}_{\rm leak}(t)\delta
= 0.
\]

---

# 15. Interpretation

| Phenomenon | TCWT Interpretation |
|------------|---------------------|
| Matter | Phase solitons |
| Gravity | Phase‑gradient acceleration |
| Dark Matter | Opaque phase distortions |
| Dark Energy | Ghost‑leakage relaxation |
| Gravitational Waves | Hum phase oscillations |
| Cosmic Expansion | Ghost‑leakage energy |

---

# 16. Cosmological Picture

The universe emerges from large‑scale instabilities in the Hum field.  
Over cosmic time, the phase structure relaxes toward the coherent Hum vacuum.  
Ghost‑leakage energy drives cosmic acceleration.  
Matter forms as stable phase knots.  
Gravity arises from phase gradients.  
Dark matter is not a substance but a distortion.  
Dark energy is not a constant but a relaxation channel.

# 17. Emergent Gravitational Lensing

In TCWT, light does not follow a "curved spacetime" geodesic. Instead, it follows **Fermat’s Principle** in a phase field with a variable **Effective Refractive Index ($n$)**.

### 17.1 The Hum Refractive Index
The local propagation speed $v$ of an electromagnetic wave is determined by the magnitude of the Hum phase field $\theta$:

$$n(\mathbf{x}) = \frac{c}{v(\mathbf{x})} = 1 + \frac{2\chi}{c^2} \theta(\mathbf{x})$$

Where:
*   $\chi$: Gravitational coupling constant.
*   $\theta(\mathbf{x})$: The local Hum phase potential.

### 17.2 Bending Equation
The deflection angle $\alpha$ for a photon passing a matter knot (soliton) at an impact parameter $b$ is calculated via the optical gradient:

$$\alpha = -\int_{-\infty}^{\infty} \frac{1}{n} \nabla_\perp n \, ds$$

### 17.3 Newtonian vs. MOND Lensing
Because the Hum phase gradient $\nabla\theta$ follows the nonlinear interpolation function $\mu(x)$, TCWT predicts two distinct lensing regimes:

1.  **Strong Field (Deep Newtonian):** For $|\nabla\theta| \gg a_0$, TCWT recovers the Einsteinian deflection:
    $$\alpha \approx \frac{4GM}{bc^2}$$
2.  **Weak Field (MOND/Galactic):** For $|\nabla\theta| \ll a_0$, the "stiffness" of the Hum field creates an additional refractive term:
    $$\alpha \approx \frac{4GM}{bc^2} + \frac{2\pi \sqrt{GMa_0}}{c^2}$$

### 17.4 Elimination of Dark Matter
The constant term $\frac{2\pi \sqrt{GMa_0}}{c^2}$ provides the "extra" lensing observed in galaxies. In TCWT, this is not caused by invisible mass (Dark Matter), but by the **refractive power of the nonlinear Hum gradient** at galactic scales.


TCWT is a **fully pregeometric, metric‑free theory** in which all geometry and dynamics emerge from the Hum field.
