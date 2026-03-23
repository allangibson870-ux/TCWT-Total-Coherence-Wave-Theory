# TCWT Master Lagrangian  
### Pregeometric Hum Field Formulation  
**Version:** 2026.9  
**Status:** Core Theoretical Framework  

---

## 1. Introduction

Total Coherence Wave Theory (TCWT) is a **pregeometric** framework in which all observable physics emerges from the dynamics of a single coherent phase field called the **Hum**.  

There is:

- no fundamental metric,  
- no curvature tensor,  
- no Einstein–Hilbert term.  

Geometry, gravity, matter, waves, and cosmic expansion **emerge** from the behaviour of the Hum field and its auxiliary degrees of freedom.

---

## 2. Fundamental Fields

TCWT is built from three interacting fields:

| Field | Meaning |
|-------|---------|
| \( \theta(x,t) \) | Hum phase field |
| \( \Omega(x,t) \) | Local oscillation frequency |
| \( G(x,t) \) | Ghost‑leakage relaxation field |

All physical phenomena arise from interactions among these three fields.

---

## 3. Coherent Hum Vacuum

The coherent vacuum state is:

\[
\theta_0(t) = \Omega_{\rm hum}\, t,
\]

where \( \Omega_{\rm hum} \) is the global Hum frequency.

Small deviations from this state generate:

- matter (phase solitons),  
- gravity (phase gradients),  
- gravitational waves (phase oscillations),  
- dark‑matter‑like distortions (nonlinear gradient sector),  
- dark‑energy‑like relaxation (ghost leakage).

---

## 4. TCWT Master Lagrangian

The fundamental Lagrangian density is:

\[
\boxed{
\mathcal{L}
= C_0(\partial_t\theta - \Omega)^2
- \kappa a_0^2 F\!\left(\frac{|\nabla\theta|^2}{a_0^2}\right)
- \alpha(\partial_t G - \nabla^2\theta)^2
- V_\Omega(\Omega)
}
\]

with constants:

- \( C_0 \): temporal coherence stiffness  
- \( \kappa \): spatial phase stiffness  
- \( a_0 \): MOND acceleration scale  
- \( \alpha \): ghost‑leakage coupling  

This is a nonlinear scalar‑field theory with:

- a MOND‑like gradient sector,  
- a curvature‑leakage relaxation channel,  
- no metric,  
- no curvature tensor.

---

## 5. Nonlinear Gradient Function

The MOND‑motivated function is:

\[
F(x) = x + \frac{2}{3}x^{3/2},
\]

with derivative:

\[
\mu(x) = \frac{dF}{dx} = 1 + \sqrt{x}.
\]

This yields:

- Newtonian behaviour for \( |\nabla\theta| \gg a_0 \),  
- MOND‑like behaviour for \( |\nabla\theta| \ll a_0 \).

---

## 6. Euler–Lagrange Field Equations

### 6.1 Hum Phase Field \( \theta \)

\[
2C_0\,\partial_t(\partial_t\theta - \Omega)
- \nabla\cdot\left[
\kappa\,\mu\!\left(\frac{|\nabla\theta|}{a_0}\right)\nabla\theta
\right]
+ 2\alpha\,\nabla^2(\partial_t G - \nabla^2\theta)
= 0.
\]

---

### 6.2 Frequency Field \( \Omega \)

\[
-2C_0(\partial_t\theta - \Omega)
+ V_\Omega'(\Omega)
= 0.
\]

For the quadratic potential:

\[
V_\Omega(\Omega)
= \frac{1}{2} m_\Omega^2(\Omega - \Omega_{\rm hum})^2,
\]

the equation becomes:

\[
2C_0(\Omega - \partial_t\theta)
+ m_\Omega^2(\Omega - \Omega_{\rm hum})
= 0.
\]

---

### 6.3 Ghost‑Leakage Field \( G \)

\[
\partial_t\left[
2\alpha(\partial_t G - \nabla^2\theta)
\right] = 0.
\]

Low‑energy regime:

\[
\partial_t G \approx \nabla^2\theta.
\]

This term governs curvature leakage and emergent dark‑energy‑like behaviour.

---

## 7. Weak‑Field and Quasistatic Limit

Assumptions:

- \( \partial_t^2\theta \approx 0 \),  
- \( \partial_t G \approx 0 \),  
- ghost leakage is slow: \( \partial_t G - \nabla^2\theta \approx 0 \).

The Hum phase equation reduces to:

\[
\nabla\cdot\left[
\kappa\,\mu\!\left(\frac{|\nabla\theta|}{a_0}\right)\nabla\theta
\right]
= \rho_{\rm eff},
\]

where \( \rho_{\rm eff} \) is an effective source term (matter knots + phase distortions).

Gravitational acceleration:

\[
\mathbf{a} = -\chi\,\nabla\theta.
\]

---

## 8. Newtonian Limit

Strong‑field regime \( |\nabla\theta| \gg a_0 \):

\[
\mu(x) \to 1,
\]

\[
\kappa\nabla^2\theta \approx \rho_{\rm eff}.
\]

Identifying \( \rho_{\rm eff} \propto \rho \) gives a Poisson‑like equation and Newtonian gravity with effective \( G \).

---

## 9. MOND Regime

Weak‑field regime \( |\nabla\theta| \ll a_0 \):

\[
\mu(x) \approx \sqrt{x} = \frac{|\nabla\theta|}{a_0}.
\]

The equation becomes:

\[
\nabla\cdot\left[
\frac{|\nabla\theta|}{a_0}\nabla\theta
\right]
= \rho_{\rm eff},
\]

yielding flat rotation curves and the baryonic Tully–Fisher relation.

---

## 10. Energy Density of the Hum–Ghost System

\[
\mathcal{E}
= C_0(\partial_t\theta - \Omega)^2
+ \kappa a_0^2 F\!\left(\frac{|\nabla\theta|^2}{a_0^2}\right)
+ \alpha(\partial_t G - \nabla^2\theta)^2
+ V_\Omega(\Omega).
\]

Interpretation:

- Hum temporal coherence → kinetic energy  
- Hum gradient → gravity / MOND  
- Ghost leakage → dark‑energy‑like relaxation  
- Frequency potential → coherence saturation  

Energy slowly transfers:

\[
\text{gradient} \;\to\; \text{ghost} \;\to\; \text{dark‑energy‑like behaviour}.
\]

---

## 11. Matter Knots (Phase Solitons)

Localized matter corresponds to stable solitons:

\[
\theta_{\rm knot}(r)
= \Theta_0 \exp\!\left(-\frac{r^2}{2R^2}\right).
\]

Matter is a **phase configuration**, not an added substance.

---

## 12. Gravitational Waves

Linear perturbations \( \delta\theta \) satisfy:

\[
\Box\,\delta\theta = 0,
\]

representing Hum‑phase gravitational waves propagating at speed \( c \), with:

\[
c^2 = \frac{\kappa}{C_0}.
\]

---

## 13. Ghost Leakage and Dark Energy

Ghost energy density:

\[
\rho_G = \alpha(\partial_t G - \nabla^2\theta)^2.
\]

This behaves as a **time‑varying dark‑energy‑like component**.

---

## 14. Metric‑Free Cosmology

Cosmic expansion emerges from ghost leakage:

\[
H^2(t)
= \frac{\rho_G(t)}{3M_{\rm eff}^2},
\qquad
\rho_G(t) = \alpha(\nabla^2\theta)^2.
\]

Thus:

\[
H(t) \propto |\nabla^2\theta|.
\]

Acceleration is a direct consequence of curvature leakage.

---

## 15. Linear Perturbations (Metric‑Free)

\[
\delta\ddot{\theta}
+ \Gamma(t)\,\delta\dot{\theta}
- c_s^2(t)\,\nabla^2\delta\theta
+ m_{\rm eff}^2(t)\,\delta\theta
= 0.
\]

Density contrast:

\[
\delta\rho \propto \nabla^2\delta\theta.
\]

Growth equation:

\[
\delta\ddot{\delta}
+ 2H\delta\dot{\delta}
- 4\pi G_{\rm eff}(t)\rho\,\delta
+ F_{\rm leak}(t)\,\delta
= 0.
\]

---

## 16. Emergent Gravitational Lensing

Light follows Fermat’s principle with refractive index:

\[
n(x) = 1 + \frac{2\chi}{c^2}\theta(x).
\]

Deflection angle:

\[
\alpha
= -\int_{-\infty}^{\infty}
\frac{1}{n}\,\nabla_\perp n\,ds.
\]

Regimes:

- **Strong field:** recovers Einsteinian lensing  
- **Weak field:** extra MOND‑like term explains galactic lensing without dark matter  

---

## 17. Interpretation Summary

| Phenomenon | TCWT Interpretation |
|------------|---------------------|
| Matter | Phase solitons |
| Gravity | Phase‑gradient acceleration |
| Dark Matter | Opaque phase distortions |
| Dark Energy | Ghost‑leakage relaxation |
| Gravitational Waves | Hum‑phase oscillations |
| Cosmic Expansion | Ghost‑leakage energy |

---

# End of Document
