# TCWT Cosmological Perturbations

This document extends the TCWT Lagrangian into the cosmological regime. It derives the background expansion, linear perturbations, modified Einstein equations, and the structure-growth equation, providing the machinery needed to compare TCWT with ΛCDM on cosmological scales.

## 1. Relativistic TCWT Action

TCWT is built on three interacting fields: the Hum phase field θ, the local oscillation frequency Ω, and the ghost-relaxation field G.

### 1.1 Covariant Structure
We work in a general spacetime with metric \( g_{\mu\nu} \). Introduce:
- A unit timelike 4-velocity \( u^\mu \) representing the cosmological rest frame,
- The spatial projector \( h_{\mu\nu} = g_{\mu\nu} + u_\mu u_\nu \).

These define:
- Temporal derivative: \( D_t \equiv u^\mu \nabla_\mu \),
- Spatial gradient: \( \nabla_\perp^\mu = h^{\mu\nu} \nabla_\nu \),
- Spatial Laplacian: \( \Delta = h^{\mu\nu} \nabla_\mu \nabla_\nu \).

In an FLRW background these reduce to ordinary time derivatives and spatial gradients.

### 1.2 Covariant TCWT Lagrangian
\[
\mathcal{L}_{\rm TCWT} = - \frac{1}{2} C_0 (D_t \theta - \Omega)^2 - \kappa a_0^2 F\left( \frac{h^{\mu\nu} \nabla_\mu \theta \nabla_\nu \theta}{a_0^2} \right) - V_\Omega(\Omega) - \alpha (D_t G - \Delta \theta)^2 + \mathcal{L}_{\rm soliton}
\]

### 1.3 Full Action
\[
S = \int d^4x \sqrt{-g} \left[ \frac{R}{16\pi G} + \mathcal{L}_{\rm TCWT} \right]
\]

## 2. Background Cosmology

### 2.1 FLRW Metric and Homogeneous Fields
\[
ds^2 = -dt^2 + a^2(t) \delta_{ij} dx^i dx^j, \qquad H = \frac{\dot{a}}{a}
\]

Homogeneous background fields: \( \bar{\theta}(t) \), \( \bar{\Omega}(t) \), \( \bar{G}(t) \).

Define \( X \equiv \dot{\bar{\theta}} - \bar{\Omega} \).

### 2.2 Background Energy Densities and Pressures
**Hum sector:**
\[
\bar{\rho}_{\rm hum} = \frac{1}{2} C_0 X^2 + V_\Omega(\bar{\Omega}), \qquad \bar{p}_{\rm hum} = \frac{1}{2} C_0 X^2 - V_\Omega(\bar{\Omega})
\]

**Ghost sector:**
\[
\bar{\rho}_{\rm ghost} = \alpha \dot{\bar{G}}^2, \qquad \bar{p}_{\rm ghost} = \alpha \dot{\bar{G}}^2
\]

### 2.3 Modified Friedmann Equations
\[
H^2 = \frac{8\pi G}{3} (\bar{\rho}_{\rm hum} + \bar{\rho}_{\rm ghost} + \bar{\rho}_m + \bar{\rho}_{\rm rad})
\]

\[
\dot{H} = -4\pi G (\bar{\rho}_{\rm tot} + \bar{p}_{\rm tot})
\]

## 3. Linear Perturbations

### 3.1 Newtonian Gauge
\[
ds^2 = -(1 + 2\Phi) dt^2 + a^2(t) (1 - 2\Psi) \delta_{ij} dx^i dx^j
\]

Perturbed fields: \( \theta = \bar{\theta} + \delta\theta \), \( \Omega = \bar{\Omega} + \delta\Omega \), \( G = \bar{G} + \delta G \).

Matter perturbations: \( \rho_m = \bar{\rho}_m (1 + \delta_m) \), velocity \( v_i = \partial_i v \).

## 4. Hum Sector Energy-Momentum Tensor

Perturbed energy density:
\[
\delta\rho_{\rm hum} = C_0 X (\dot{\delta\theta} - \delta\Omega - \Phi \dot{\bar{\theta}}) + V_\Omega'(\bar{\Omega}) \delta\Omega
\]

Perturbed pressure is similar (adiabatic to leading order). Anisotropic stress \( \sigma_{\rm hum} = 0 \).

## 5. Ghost Sector Energy-Momentum Tensor

Perturbed energy density:
\[
\delta\rho_{\rm ghost} = 2\alpha \dot{\bar{G}} (\dot{\delta G} - \Phi \dot{\bar{G}} - \frac{k^2}{a^2} \delta\theta)
\]

Perturbed pressure \( \delta p_{\rm ghost} \approx \delta\rho_{\rm ghost} \). Anisotropic stress \( \sigma_{\rm ghost} = 0 \).

## 6. Modified Poisson Equation

In the Newtonian gauge, the gravitational potential is sourced by:
\[
\frac{k^2}{a^2} \Psi = 4\pi G \Bigl[ \bar{\rho}_m \delta_m + \delta\rho_{\rm hum} + \delta\rho_{\rm ghost} \Bigr]
\]

Since anisotropic stress vanishes from both sectors, \( \Phi = \Psi \) (no gravitational slip at linear level).

## 7. Matter Perturbations
\[
\dot{\delta}_m = - \frac{k^2}{a^2} v + 3 \dot{\Psi}, \qquad \dot{v} = - \Phi
\]

## 8. TCWT Growth Equation

Using the mapping \( \delta_m \propto -k^2 \delta\theta \) (valid on sub-horizon scales), the density contrast evolves as:
\[
\ddot{\delta} + 2 H_{\rm TCWT} \dot{\delta} - 4\pi G_{\rm eff}(a) \bar{\rho}_m \delta + \mathcal{F}_{\rm wilt}(a,k) \delta = 0
\]

where \( G_{\rm eff}(a) \) encodes modifications from the Hum and Ghost sectors, and \( \mathcal{F}_{\rm wilt}(a,k) \propto \beta k^4 / a^4 \) is the phase-relaxation damping term.

## 9. Effective CDM-like Behaviour for CMB Peaks

To reproduce ΛCDM acoustic peaks without a cold dark matter particle, the combined Hum + Ghost sector must behave as an effectively pressureless clustering component at recombination.

Require:
\[
c_{s,{\rm TCWT}}^2 (k_{\rm peak}, a_{\rm rec}) \ll 1
\]

and
\[
\bar{\rho}_{\rm TCWT,cl}(a_{\rm rec}) \approx \bar{\rho}_{\rm CDM}(a_{\rm rec})
\]

This imposes constraints on \( C_0 \), \( V_\Omega(\Omega) \), and \( \alpha \).

## 10. Summary

This document provides the cosmological layer of TCWT:
- Covariant action and background expansion
- Linear perturbation theory
- Explicit Hum and Ghost energy-momentum tensors
- Modified Poisson and growth equations
- Conditions for matching CMB acoustic peaks

Together with the Master Framework, this completes the theoretical machinery needed to test TCWT against precision cosmological data.

**Next steps**: Implement the perturbation system in CLASS, perform MCMC fits, and quantify how well the Hum + Ghost sector can simultaneously satisfy CMB peaks and galactic MOND behaviour.
