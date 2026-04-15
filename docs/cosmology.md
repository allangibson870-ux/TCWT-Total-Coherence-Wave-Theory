# TCWT Cosmological Perturbations  
## Covariant Action, FLRW Background, Linear Perturbations, Growth Equation, and CMB Constraints  
Version: 2026.9  
Status: Complete cosmology layer for CLASS implementation

---

# 1. Covariant TCWT Action

TCWT is built from three interacting fields:

- $\theta$ — Hum phase field  
- $\Omega$ — informational drag field  
- $G$ — ghost‑relaxation field  

To embed TCWT in curved spacetime, define:

- metric $g_{\mu\nu}$  
- unit timelike vector $u_\mu$  
- spatial projector $h_{\mu\nu} = g_{\mu\nu} + u_\mu u_\nu$

Covariant derivatives:

- Temporal: $D_t = u^\mu \nabla_\mu$  
- Spatial: $\nabla^\perp_\mu = h_\mu^{\ \nu} \nabla_\nu$  
- Spatial Laplacian: $\Delta = h^{\mu\nu} \nabla_\mu \nabla_\nu$

## 1.1 Covariant TCWT Lagrangian

$$L_{\rm TCWT} = C_0(D_t\theta - \Omega)^2 - \kappa a_0^2 F(\nabla^\perp_\mu\theta \nabla^\perp_\mu\theta / a_0^2) - \alpha(D_t G - \Delta\theta)^2 - V_\Omega(\Omega)$$

Full action:

$$S = \int d^4x \sqrt{-g} \left[ \frac{R}{16\pi G} + L_{\rm TCWT} \right]$$

---

# 2. FLRW Background Evolution

Metric:

$$ds^2 = -dt^2 + a(t)^2 \delta_{ij} dx^i dx^j$$

Hubble parameter:

$$H = \dot a / a$$

Homogeneous fields:

- $\bar\theta(t)$  
- $\bar\Omega(t)$  
- $\bar G(t)$  

Define:

$$X(t) = \dot{\bar\theta} - \bar\Omega$$

## 2.1 Background Energy Density and Pressure

Hum sector:

$$\bar\rho_{\rm hum} = \frac12 C_0 X^2 + V_\Omega(\bar\Omega)$$  
$$\bar p_{\rm hum} = \frac12 C_0 X^2 - V_\Omega(\bar\Omega)$$

Ghost sector:

$$\bar\rho_{\rm ghost} = \alpha \dot{\bar G}^2$$  
$$\bar p_{\rm ghost} = \alpha \dot{\bar G}^2$$

## 2.2 Modified Friedmann Equations

$$H^2 = \frac{8\pi G}{3} (\bar\rho_{\rm hum} + \bar\rho_{\rm ghost} + \bar\rho_m + \bar\rho_r)$$

$$\dot H = -4\pi G (\bar\rho_{\rm tot} + \bar p_{\rm tot})$$

## 2.3 Algebraic Constraint from Ω Variation

$$X = \frac{1}{2C_0} V_\Omega'(\bar\Omega)$$

## 2.4 Ghost Evolution

$$\dot{\bar G} = \dot{\bar G}_0 = \text{constant}$$

## 2.5 Drag‑Field Relaxation Law

To interpolate between matter‑like and dark‑energy‑like behaviour:

$$\frac{d\bar\Omega}{d\ln a} = -\gamma(\bar\Omega - \Omega_{\min})$$

or equivalently:

$$\dot{\bar\Omega} = -H \gamma(\bar\Omega - \Omega_{\min})$$

Parameters:

- $\gamma$ — relaxation rate  
- $\Omega_{\min}$ — late‑time floor  
- $\Omega_{\rm ini}$ — early‑time value  
- $\dot{\bar G}_0$ — constant ghost leakage  

This closes the background system.

---

# 3. Linear Perturbations

Work in Newtonian gauge:

$$ds^2 = -(1 + 2\Phi) dt^2 + a(t)^2 (1 - 2\Psi) \delta_{ij} dx^i dx^j$$

Perturbed fields:

- $\theta = \bar\theta + \delta\theta$  
- $\Omega = \bar\Omega + \delta\Omega$  
- $G = \bar G + \delta G$  

Matter:

- $\rho_m = \bar\rho_m (1 + \delta_m)$  
- velocity potential $v$  

---

# 4. Hum Sector Perturbations

Perturbed energy density:

$$\delta\rho_{\rm hum} = C_0 X (\delta\dot\theta - \delta\Omega - \Phi \dot{\bar\theta}) + V_\Omega'(\bar\Omega)\delta\Omega$$

Pressure perturbation is similar (adiabatic to leading order).

Anisotropic stress:

$$\sigma_{\rm hum} = 0$$

---

# 5. Ghost Sector Perturbations

Perturbed energy density:

$$\delta\rho_{\rm ghost} = 2\alpha \dot{\bar G} (\delta\dot G - \Phi \dot{\bar G} - (k^2/a^2)\delta\theta)$$

Pressure:

$$\delta p_{\rm ghost} \approx \delta\rho_{\rm ghost}$$

Anisotropic stress:

$$\sigma_{\rm ghost} = 0$$

---

# 6. Modified Poisson Equation

Since both sectors have zero anisotropic stress:

$$\Phi = \Psi$$

Poisson equation:

$$(k^2/a^2)\Psi = 4\pi G (\bar\rho_m \delta_m + \delta\rho_{\rm hum} + \delta\rho_{\rm ghost})$$

---

# 7. Matter Perturbations

Continuity:

$$\dot\delta_m = -(k^2/a^2) v + 3\dot\Psi$$

Euler:

$$\dot v = -\Phi$$

---

# 8. TCWT Growth Equation

Using the sub‑horizon mapping $\delta_m \propto -k^2 \delta\theta$:

$$\ddot\delta + 2H_{\rm TCWT}\dot\delta - 4\pi G_{\rm eff}(a)\bar\rho_m \delta + F_{\rm wilt}(a,k)\delta = 0$$

where:

- $G_{\rm eff}(a)$ encodes Hum + Ghost modifications  
- $F_{\rm wilt}(a,k) \propto \beta k^4 / a^4$ is ghost‑induced damping  

---

# 9. Effective CDM‑Like Behaviour at Recombination

To match ΛCDM acoustic peaks:

1. TCWT must behave as a pressureless clustering component:

$$c_{s,{\rm TCWT}}^2(k_{\rm peak}, a_{\rm rec}) \ll 1$$

2. TCWT background density must mimic CDM:

$$\bar\rho_{\rm TCWT,cl}(a_{\rm rec}) \approx \bar\rho_{\rm CDM}(a_{\rm rec})$$

This constrains $C_0$, $V_\Omega$, and $\alpha$.

---

# 10. Dispersion Relation (Perturbations)

Quadratic perturbation Lagrangian:

$$L_{(2)} = C_{\rm eff}\delta\dot\theta^2 - \kappa\mu_0(\nabla\delta\theta)^2 + \alpha(\delta\dot G - \nabla^2\delta\theta)^2$$

After integrating out $\delta G$:

$$\omega^2(k) = c_s^2 k^2 + \beta k^4$$

with:

$$c_s^2 = \kappa\mu_0 / C_{\rm eff}, \quad \beta = \alpha / C_{\rm eff}$$

Interpretation:

- Large scales: standard wave propagation  
- Small scales: strong $k^4$ suppression  

This produces **phase‑relaxation damping**.

---

# 11. Modified Growth Equation (Explicit)

$$\ddot\delta + 2H\dot\delta - 4\pi G_{\rm eff}\bar\rho_m \delta - \beta k^4 a^{-4}\delta = 0$$

Ghost‑induced $k^4$ term suppresses small‑scale power.

---

# 12. CMB Acoustic Peaks in TCWT

TCWT reproduces ΛCDM‑like peaks if:

- TCWT clusters like CDM at recombination  
- gravitational potentials remain nearly constant  
- sound speed is small  

Peak positions follow standard photon‑baryon oscillations.

Peak heights include:

- baryon loading  
- ISW driving  
- ghost‑induced modifications  

---

# 13. Damping Tail (High‑ℓ)

Ghost‑induced $k^4$ suppression steepens the damping tail:

- sharper high‑ℓ falloff  
- reduced small‑scale lensing  
- distinctive signature vs ΛCDM  

---

# 14. CMB Polarization and Lensing

Polarization:

- similar to ΛCDM at low ℓ  
- sharper peaks at high ℓ  

Lensing:

- weaker small‑scale lensing  
- reduced smoothing of acoustic peaks  

---

# 15. Boltzmann Layer (CLASS Implementation)

Evolve the coupled system:

- $\delta\theta$  
- $\delta\Omega$  
- $\delta G$  
- $\delta_m$  
- $v$  

Replace Poisson equation with TCWT version.  
Add scale‑dependent $G_{\rm eff}(a,k)$ and $k^4$ damping.

---

# 16. Parameter Estimation

Free parameters:

- $C_0$  
- $\kappa$  
- $a_0$  
- $\alpha$  
- $V_\Omega$ parameters  

Datasets:

- Planck CMB  
- BAO  
- SNe  
- DES / Euclid weak lensing  
- RSD  

Pipeline:

- Modified CLASS  
- MCMC (MontePython / Cobaya)  
- Compare with ΛCDM likelihoods  

---

# 17. Stability Conditions

- $C_0 > 0$  
- $\alpha > 0$  
- $c_s^2 = \kappa/C_0 > 0$  
- $c_s^2 \le c_{\rm light}^2$  
- $m_{\rm eff}^2 \ge 0$  

No tachyons, no ghosts, no gradient instabilities.

---

# 18. Nonlinear Structure Formation (N‑Body)

Replace Newtonian Poisson equation with:

$$\nabla \cdot[\mu(|\nabla\theta|/a_0)\nabla\theta] = \rho$$

Particle acceleration:

$$a = -\chi \nabla\theta$$

Goals:

- halo formation without CDM particles  
- MOND rotation curves  
- large‑scale structure  

---

# 19. Key Testable Predictions

- scale‑dependent growth rate  
- modified weak lensing maps  
- ΛCDM‑like CMB peaks + deviations at high ℓ  
- flat rotation curves  
- baryonic Tully–Fisher relation  

---

# 20. Summary

This document provides the full cosmological layer of TCWT:

- covariant action  
- FLRW background  
- linear perturbations  
- modified Poisson equation  
- growth equation  
- CMB predictions  
- CLASS implementation  
- stability conditions  
- nonlinear extensions  

Together with the core Lagrangian, Einstein limit, quantum limit, and fermion sector, this completes the TCWT theoretical framework.

