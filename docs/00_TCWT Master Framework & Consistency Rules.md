# TCWT Master Framework — Version V7
**RG Layer + Critical Fixes**  
**Status:** Living Reference Document  
*All other TCWT documents must reference this file.*

---

## 1. Core Philosophy

TCWT is a 4‑layer effective field theory (EFT) in which higher layers are strict coarse‑grained limits of lower layers.  
No feedback from macroscopic gravity or measurement is allowed into the fundamental microdynamics.  
This protects the topological stability of matter knots (Hopfions).

**Critical Consistency Rule:**  
Higher layers cannot feed back into Layer 0.  
Regimes where layers might mix (singularities, extreme curvature) are regulated by the Ω‑cap and global Hum coherence.

---

## 2. Notation & Consistency Standards

### 2.1 MOND Interpolation Function

Define the dimensionless MOND argument:

$$x = \frac{|\nabla\theta|}{a_0}$$

with $a_0$ a **gradient scale** (units 1/m).

**Interpolation:**
$$\mu(x) = 1 + \sqrt{x}$$

**Limits:**
- **Newtonian** ($x \gg 1$): $\mu \to 1$  
- **Deep MOND** ($x \ll 1$): $\mu \approx \sqrt{x} \implies a \approx \sqrt{a_M g_N}$

where the **physical MOND acceleration** is:
$$a_M = \chi a_0$$

---

### 2.2 χ Calibration (MOND Constant)

$$\chi = \frac{c^2 \kappa}{C_0 \Omega_{\max}}$$

**Example calibration:**  
κ = 1.455, Ω_max = 16.91, C₀ = 0.0594 →  
$$\chi \approx 1.30 \times 10^{17}\ \text{m}^2/\text{s}^2$$

**Cross‑relations (dimensionally corrected):**
$$\alpha \approx \frac{\kappa^2 \chi}{2 a_0^2}$$
$$\ell_P^2 \sim \frac{\alpha}{\kappa}$$

---

### 2.3 Mass‑Lock Scaling

$$m_e(a) = m_0 \left(\frac{H_0}{H(a)}\right)^\gamma$$

$\gamma \ll 2$ due to screening.  
Must satisfy $\Delta m/m \lesssim 10^{-16}$ → requires suppression mechanism.

---

### 2.4 Ghost Leakage Scaling

$$\text{Leakage} \propto \frac{\alpha Q^2}{R^4}$$

---

### 2.5 Units & Normalization Table


| Quantity | Meaning | Units | Typical Value |
|:---|:---|:---|:---|
| $\Omega_{hum}$ | Hum oscillation frequency | s⁻¹ | ~1e‑18 |
| $\theta_0(t)$ | Background phase | dimensionless | 1.0 |
| $\alpha$ | Ghost stiffness (Layer‑0) | m⁴/s² | ~1e17 |
| $\chi$ | MOND constant | m²/s² | 1.30e17 |
| $C_0$ | Hum coupling | dimensionless | 0.0594 |
| $\kappa$ | Coherence curvature | dimensionless | 1.455 |
| $\Omega_{max}$ | Max Hum frequency | dimensionless | 16.91 |

**Clarification (V6 IR Parameterization):**  
$\alpha_0$ is the dimensionless IR‑renormalized stiffness entering the smoothed $G_{\mathrm{eff}}$ and growth equation.  
Physical $\alpha$ remains $\sim 10^{17}$ m⁴/s² and is recovered via $\chi$, $a_0$, $\kappa$, $\Omega_{max}$ normalization.  
**V6 fit:** $\alpha_0 = 0.0502$.

---

## 3. The 4‑Layer EFT Stack

*   **Layer 0 — Fundamental Microdynamics**  
    Fields: $\theta$, $\Omega$, $G$ (Planck/UV scale)
*   **Layer 1 — Topological Sector**  
    Hopfion knots, chiral zero‑modes
*   **Layer 2 — Linear Fluctuation Sector**  
    Small perturbations $\delta\theta$
*   **Layer 3 — Coarse‑Grained Gravity**  
    $g_{\mu\nu} = \eta_{\mu\nu} + \beta\,\partial_\mu\theta\,\partial_\nu\theta$
*   **Layer 4 — Emergent Effective Physics**  
    MOND, galaxies, stellar spectra, cosmology

---

## 4. Current Core Equations

### 4.1 Master Lagrangian (Layer 0)

$$L = C_0(\partial_t\theta - \Omega)^2 - \kappa a_0^2\,F\!\left(\frac{|\nabla\theta|}{a_0}\right) - \alpha(\partial_t G - \nabla^2\theta)^2 - V_\Omega(\Omega)$$

with:
$$F(x) = x + \frac{2}{3}x^{3/2}$$
$$\mu(x) = 1 + \sqrt{x}$$

---

### 4.2 Effective Dirac Operator on Hopfion Ring (Layer 1)

$$i\partial_t\psi = \left[ -i v\,\partial_s\sigma^1 + m_{\mathrm{eff}}\sigma^3 + A\,\sigma^2 \right]\psi$$

$$v = \sqrt{\kappa/C_0}$$
$$m_{\mathrm{eff}} \propto \alpha\,\nabla^2\theta_{\mathrm{Hopf}}$$

---

### 4.3 Exact and Smoothed $G_{\mathrm{eff}}$ (Layer 3)

**Exact (schematic structure only):**
$$G_{\mathrm{eff}} = G\left[ 1 + \frac{\kappa\,\mu(k)}{4\pi G\rho_m a^2 C_0} + \frac{\alpha k^4}{4\pi G\rho_m a^4 C_0} \right]^{-1}$$

**Updated V6 Smoothed Form (operational definition):**
$$G_{\mathrm{eff}}(k,a) = \frac{G}{1 + (k/k_g)^{2p}}$$

with:
- $p = 1.602$  
- $k_g = k_\star = 0.498\,h/\mathrm{Mpc}$

---

### 4.4 Modified Growth Equation

$$\ddot{\delta} + 2H\dot{\delta} - 4\pi G_{\mathrm{eff}}\rho_m\,\delta - \beta\frac{k^4}{a^4}\delta = 0$$

$$\beta = \frac{\alpha}{C_0}$$
(IR‑renormalized → $\beta \approx 3.48$)

---

### 4.5 Evaporation Cutoff for Generations

$$\tau(Q) \propto \frac{R^4}{\alpha Q^2 \Gamma_{\mathrm{leak}}}$$

$Q \ge 4 \implies$ rapid evaporation $\to$ **three stable generations**

---

### 4.6 Neutrino Sector (Updated V6)

$$m_\nu(a) \approx m_{\nu0} \left(\frac{H_0}{H(a)}\right)^\beta$$

**V6 fit:** $\beta = 3.48$  
Ghost leakage induces weak density‑dependent self‑interactions.

---

## 5. Renormalization Group Flow (RG‑TCWT)

Scale: $k \sim 1/\lambda$

$$\frac{dg_i}{d\ln k} = \beta_i(g_j)$$

**Key running couplings:**
$$\frac{da_0}{d\ln k} = \eta_a a_0$$
$$\frac{d\alpha}{d\ln k} = -\gamma_\alpha \alpha + \delta_\alpha \chi^2$$
$$\frac{d\kappa}{d\ln k} = \beta_\kappa \kappa (1 - \kappa/\kappa_\star)$$
$$\chi(k) = \frac{c^2 \kappa(k)}{C_0(k)\Omega_{\max}(k)}$$

**RG Consistency Condition**
$$\frac{d}{d\ln k}\left(\frac{\alpha}{\kappa^2}\right) \le 0$$

**Fixed Points**
- **UV:** κ → 0, α → 0  
- **Galactic:** κ → κ*  
- **IR:** α → α* → dark‑energy‑like behaviour

---

## 6. V6 Best‑Fit Cosmological Parameter Set

From full‑stack MCMC + Fisher analysis:


| Parameter | Value | Notes |
|:---|:---|:---|
| $\alpha_0$ | 0.0502 | IR stiffness (scaled) |
| $k_\star$ | 0.498 h/Mpc | MOND/RG transition scale |
| $p$ | 1.602 | Smoothing exponent |
| $\beta$ | 3.48 | Neutrino mass‑running |
| $H_0$ | 71.4 km/s/Mpc | Hubble tension resolved |
| $S_8$ | 0.772 | Growth tension resolved |

These values satisfy the **RG Consistency Condition** and ensure GR‑compliance at galactic scales while modifying cosmological growth.

---

## 7. Cross‑Document Requirements

All TCWT documents must:
- Reference this Master Framework at the top.  
- Use canonical:
  - $\mu(x) = 1 + \sqrt{x}$
  - $\chi = c^2 \kappa / (C_0 \Omega_{\max})$
- Use the updated V6 smoothed $G_{\mathrm{eff}}$ with $p = 1.602$ and $k_\star = 0.498\,h/\mathrm{Mpc}$.  
- Use $\beta = 3.48$ for neutrino mass‑running.  
- Reference the **V6 Best‑Fit Cosmological Parameter Set** for all astrophysical or cosmological predictions.  
- Point to **Section 4** for core equations and **Section 5** for RG flow.

---

**Last updated:** April 21, 2026  
**This document is the single source of truth.**
