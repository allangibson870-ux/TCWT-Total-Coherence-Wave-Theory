# TCWT Master Framework & Consistency Rules
**Version:** V3 (Soft-Cap + Layered EFT + G_eff Derivation)  
**Status:** Living reference document — updated as core mathematics evolves

This is the single source of truth for notation, constants, layer structure, and current equations in Total Coherence Wave Theory (TCWT). All other documents must reference this file.

---

## 1. Core Philosophy

TCWT is a 4-layer effective field theory (EFT) in which higher layers are strict coarse-grained limits of lower layers. No feedback from macroscopic gravity or measurement is allowed into the fundamental microdynamics. This rule protects the topological stability of matter knots.

**Critical Consistency Rule:** Higher layers cannot feed back into Layer 0. Matter knots (Hopfions) remain stable against quantum measurement or macroscopic gravitational fluctuations.

---

## 2. Notation & Consistency Standard

### 2.1 MOND Interpolation Function
Canonical definition:  
$\mu(x) = 1 + \sqrt{x}$  
where $x = a / a_0$ (acceleration form) or $x = g / a_0$ (gravitational form).

### 2.2 $\chi$ Calibration (MOND Constant)
Canonical value: $\chi \approx 1.30 \times 10^{17}$ m²/s²  
Calibration parameters: $\kappa = 1.455$, $\Omega_{\text{max}} = 16.91$, $C_0 = 0.0594$  

Cross-reference relations:  
$\alpha \approx \kappa^2 / (2 a_0^2 C_0)$  
$\ell_P^2 \sim \alpha / \kappa$

### 2.3 Mass-Lock Scaling
Canonical scaling:  
$m_e(a) = m_0 \cdot (H_0 / H(a))^2$  
where $m_0$ is fixed by $\alpha(R) \to \Omega$-cap.

### 2.4 Ghost Leakage Scaling
Canonical relation:  
Leakage rate $\propto \alpha \cdot Q^2 / R^4$  
where $Q = \text{Hopfion charge}$, $R = \text{coherence radius}$.

### 2.5 Units & Normalization Table


| Quantity   | Meaning                        | Units       | Typical Value |
|------------|--------------------------------|-------------|---------------|
| $\Omega_{\text{hum}}$      | Hum oscillation frequency      | s⁻¹         | ~1e-18        |
| $\theta_0(t)$      | Background phase               | dimensionless | normalized to 1 at a=1 |
| $\alpha$          | Coherence stiffness            | m²/s²       | ~1e17         |
| $\chi$          | MOND constant                  | m²/s²       | 1.30e17       |
| $C_0$         | Hum coupling constant          | dimensionless | 0.0594      |
| $\kappa$          | Coherence curvature            | dimensionless | 1.455       |
| $\Omega_{\text{max}}$      | Maximum Hum frequency          | dimensionless | 16.91       |

---

## 3. 4-Layer EFT Stack

**Layer 0: Fundamental Microdynamics (Pregeometric)**  
Domain: Planck scale / UV / strong curvature.  
Fields: $\theta(x,t)$, $\Omega(x,t)$, $G(x,t)$.  
Action: $S_0 = \int d^4x \sqrt{-g} [C_0(\nabla_\mu\theta - u_\mu\Omega)^2 - \kappa|\nabla\theta|^2 - \alpha(G - \square\theta)^2 - V_\Omega(\Omega)]$ (with Soft-Cap).

**Layer 1: Topological / Soliton Sector**  
Domain: Intermediate / nonlinear regime.  
Objects: Hopfion knots with chiral zero-modes.

**Layer 2: Linear Fluctuation / Quantum Limit**  
Domain: Small perturbations $\delta\theta$.

**Layer 3: Coarse-Grained Gravity & Cosmology**  
Domain: Macroscopic / long-wavelength.  
Emergent metric: $g_{\mu\nu} = \eta_{\mu\nu} + \beta \partial_\mu\theta \partial_\nu\theta$.

**Layer 4: Emergent Effective Physics**  
Domain: Astrophysical and laboratory scales (MOND, galaxies, atoms, chemistry, stellar spectra).

---

## 4. Current Core Equations (Living Section)

### 4.1 Master Lagrangian (Layer 0)
$L = C_0(\partial_t \theta - \Omega)^2 - \kappa a_0^2 F(|\nabla\theta|^2 / a_0^2) - \alpha(\partial_t G - \nabla^2 \theta)^2 - V_\Omega(\Omega)$  
with $F(x) = x + (2/3) x^{3/2}$, $\mu(x) = 1 + \sqrt{x}$

### 4.2 Effective Dirac Operator on Hopfion Ring (Layer 1)
$i \partial_t \psi(s) = [-i v \partial_s \sigma^1 + m_{\text{eff}}(s) \sigma^3 + A(s) \sigma^2] \psi(s)$  
where $v = \sqrt{\kappa / C_0}$, $m_{\text{eff}}(s) \propto \alpha \nabla^2 \theta_{\text{Hopf}}$.

### 4.3 Exact Derivation of $G_{\text{eff}}(a,k)$ from the Full Action (Layer 3)

From the full covariant action, in Newtonian gauge and the quasi-static, sub-horizon limit ($k \gg aH$, time derivatives suppressed), we integrate out the auxiliary fields $\Omega$ and $G$.

The quadratic action for $\delta\theta$ after elimination becomes (schematic Fourier space):

$S^{(2)} \approx \int [ C_0 (\partial_t \delta\theta)^2 - \kappa \mu(|\nabla\theta|) (\nabla \delta\theta)^2 - \alpha (\Delta \delta\theta)^2 ]$

The ghost term $-\alpha (\Delta \delta\theta)^2$ produces the $k^4$ contribution. Mapping the TCWT stress-energy perturbation to the matter source via $\delta_m \propto -k^2 \delta\theta$, the (00) Einstein equation yields the **exact effective gravitational constant**:

$$G_{\text{eff}}(k,a) = G \left[ 1 + \frac{\kappa \mu(k)}{4\pi G \rho_m a^2 C_0} + \frac{\alpha k^4}{4\pi G \rho_m a^4 C_0} \right]^{-1}$$

In cosmological codes we use the smoothed phenomenological form (with $p \approx 1.6$):

$$G_{\text{eff}}(k,a) = \frac{G}{1 + (k / k_g)^{2p}}$$

where $k_g$ is calibrated to galactic/MOND scales (typically ~0.12 h/Mpc) and the $k^4$ term provides the ghost damping.

### 4.4 Modified Growth Equation
$\ddot{\delta} + 2H \dot{\delta} - 4\pi G_{\text{eff}}(k,a) \rho_m \delta - \beta (k^4 / a^4) \delta = 0$  
with $\beta = \alpha / C_0$

### 4.5 Evaporation Cutoff for Generations
Lifetime: $\tau(Q) \propto R^4 / (\alpha Q^2 \Gamma_{\text{leak}})$  
For $Q \geq 4$ the leakage becomes rapid $\to$ topological evaporation. This explains the observed three light generations.

### 4.6 Neutrino Sector
Neutrinos occupy shallower mass wells $\to$ stronger redshift dependence:  
$m_\nu(a) \approx m_{\nu 0} (H_0 / H(a))^\beta$ ($ \beta \gtrsim 3$)  

Ghost leakage from overlapping wells generates weak, density-dependent self-interactions. The same mechanism that allows self-interactions causes rapid evaporation for any $Q \geq 4$ states.

---

## 5. Cross-Document Requirements

Every TCWT document must:
- Reference this Master Framework at the top.
- Use canonical $\mu(x)$, $\chi$, Mass-Lock scaling, and ghost leakage scaling.
- Point to the Living Equations section (Section 4) for current mathematical content.

**Last updated:** April 19th 2026  
This document is the single source of truth. When mathematics change, update only here and propagate references.
