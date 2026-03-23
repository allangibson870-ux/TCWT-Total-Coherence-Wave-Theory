# TCWT Cosmological Perturbations

This document introduces the cosmological perturbation framework for the **Total Coherence Wave Theory (TCWT)**. It extends the TCWT Lagrangian into the cosmological regime, deriving the background expansion, linear perturbations, and the structure-growth equation that replaces the ΛCDM growth model.

## 1. Relativistic TCWT Action

TCWT is built on three interacting fields:

- the Hum phase field $\theta$,
- the local oscillation frequency $\Omega$,
- and the ghost-relaxation field $G$.

To connect the theory to cosmology, structure formation, and gravitational observables, we require a fully covariant action defined on a spacetime metric $g_{\mu\nu}$. The relativistic action must reduce to the Master Lagrangian in the weak-field, quasistatic limit.

### 1.1 Covariant Structure

We introduce:

- a unit timelike 4-velocity $u^\mu$ representing the cosmological rest frame,
- a spatial projector $h^{\mu\nu} = g^{\mu\nu} + u^\mu u^\nu$.

These allow us to define:

- temporal derivatives: $u^\mu \nabla_\mu$,
- spatial gradients: $h^{\mu\nu} \nabla_\nu$,
- spatial Laplacian: $h^{\mu\nu} \nabla_\mu \nabla_\nu$.

In an FLRW background, these reduce to:

$$
u^\mu \nabla_\mu \to \partial_t, \qquad
h^{\mu\nu} \nabla_\mu \to \nabla, \qquad
h^{\mu\nu} \nabla_\mu \nabla_\nu \to \nabla^2.
$$

### 1.2 The Relativistic TCWT Lagrangian

A covariant generalisation of the Master Lagrangian is:

$$
\begin{aligned}
\mathcal{L}_{\rm TCWT}
={}& -\frac{1}{2} C_0 \bigl( u^\mu \nabla_\mu \theta - \Omega \bigr)^2 \\
& - \kappa a_0^2 \, F\!\left( \frac{h^{\mu\nu} \nabla_\mu \theta \nabla_\nu \theta}{a_0^2} \right) \\
& - V_\Omega(\Omega) \\
& - \alpha \bigl( u^\mu \nabla_\mu G - h^{\mu\nu} \nabla_\mu \nabla_\nu \theta \bigr)^2 \\
& - \mathcal{L}_{\rm soliton}.
\end{aligned}
$$

Each term corresponds directly to a component of the non-relativistic theory:

- Temporal coherence:  
  $-\frac{1}{2} C_0 (u^\mu \nabla_\mu \theta - \Omega)^2 \quad \to \quad C_0 (\partial_t \theta - \Omega)^2$

- Nonlinear gradient sector:  
  $-\kappa a_0^2 F\!\left( \frac{h^{\mu\nu} \nabla_\mu \theta \nabla_\nu \theta}{a_0^2} \right) \quad \to \quad \kappa a_0^2 F(|\nabla \theta|^2 / a_0^2)$

- Frequency potential: $-V_\Omega(\Omega)$ → unchanged

- Ghost-leakage channel:  
  $-\alpha (u^\mu \nabla_\mu G - h^{\mu\nu} \nabla_\mu \nabla_\nu \theta)^2 \quad \to \quad \alpha (\partial_t G - \nabla^2 \theta)^2$

- Matter sector: $\mathcal{L}_{\rm soliton}$ encodes the effective behaviour of soliton matter

### 1.3 Full Relativistic Action

$$
S = \int d^4 x \, \sqrt{-g} \left[ \frac{1}{16\pi G} R + \mathcal{L}_{\rm TCWT} \right].
$$

This action is fully covariant, reduces to the Master Lagrangian in the weak-field limit, and provides the foundation for cosmology, perturbations, and structure formation.

## 2. Background Cosmology in TCWT

### 2.1 FLRW Metric and Homogeneous Fields

Spatially flat FLRW metric:

$$
ds^2 = -dt^2 + a(t)^2 \delta_{ij} \, dx^i dx^j,
$$

Hubble rate $H(t) = \dot{a}/a$.

Homogeneous fields: $\theta = \bar{\theta}(t)$, $\Omega = \bar{\Omega}(t)$, $G = \bar{G}(t)$.  
Spatial gradients vanish at background level.

### 2.2 Background TCWT Lagrangian Density

$$
\begin{aligned}
\mathcal{L}_{\rm TCWT}^{(\rm bg)}
={}& -\frac{1}{2} C_0 \bigl( \dot{\bar{\theta}} - \bar{\Omega} \bigr)^2
    - V_\Omega(\bar{\Omega}) \\
& - \alpha \, \dot{\bar{G}}^2
    - \mathcal{L}_{\rm soliton}^{(\rm bg)}.
\end{aligned}
$$

Effective background energy densities and pressures (schematic):

$$
\begin{aligned}
\rho_{\rm hum} &\sim \frac{1}{2} C_0 (\dot{\bar{\theta}} - \bar{\Omega})^2 + V_\Omega(\bar{\Omega}), &
p_{\rm hum} &\sim \frac{1}{2} C_0 (\dot{\bar{\theta}} - \bar{\Omega})^2 - V_\Omega(\bar{\Omega}), \\
\rho_G &\sim \alpha \, \dot{\bar{G}}^2, &
p_G &\sim \alpha \, \dot{\bar{G}}^2, \\
\rho_{\rm m} &= \rho_{\rm soliton}^{(\rm bg)}, & p_{\rm m} &\approx 0 \quad \text{(dust-like)}.
\end{aligned}
$$

### 2.3 Modified Friedmann Equations

$$
\begin{aligned}
H^2 &= \frac{8\pi G}{3} \bigl( \rho_{\rm hum} + \rho_G + \rho_{\rm m} + \rho_{\rm rad} + \dots \bigr), \\
\dot{H} &= -4\pi G \bigl( \rho_{\rm tot} + p_{\rm tot} \bigr).
\end{aligned}
$$

Background field equations:

$$
\begin{aligned}
\ddot{\bar{\theta}} + 3H \dot{\bar{\theta}} + \dots &= 0, \\
\frac{\partial V_\Omega}{\partial \bar{\Omega}} + C_0 (\dot{\bar{\theta}} - \bar{\Omega}) + \dots &= 0, \\
\ddot{\bar{G}} + 3H \dot{\bar{G}} + \dots &= 0.
\end{aligned}
$$

## 3. Linear Perturbations in TCWT

### 3.1 Perturbation Setup

Newtonian gauge metric:

$$
ds^2 = -(1 + 2\Phi) \, dt^2 + a(t)^2 (1 - 2\Psi) \delta_{ij} \, dx^i dx^j.
$$

Perturbed fields:

$$
\theta = \bar{\theta}(t) + \delta\theta(\vec{x},t), \quad
\Omega = \bar{\Omega}(t) + \delta\Omega(\vec{x},t), \quad
G    = \bar{G}(t)    + \delta G(\vec{x},t).
$$

Matter: $\rho_{\rm m} = \bar{\rho}_{\rm m}(t) (1 + \delta_{\rm m})$, $v_i = \partial_i v$.

### 3.2 Linearised TCWT Field Equations

$$
\begin{aligned}
&\delta\ddot{\theta} + 3H \delta\dot{\theta} + \frac{k^2}{a^2} \mu_\theta \, \delta\theta
    + C_0 (\delta\dot{\theta} - \delta\Omega) = S_\theta(\Phi,\Psi), \\
&C_0 (\delta\dot{\theta} - \delta\Omega)
    + V''_\Omega(\bar{\Omega}) \, \delta\Omega = S_\Omega(\Phi,\Psi), \\
&\delta\ddot{G} + 3H \delta\dot{G} + \alpha \frac{k^2}{a^2} \delta G
    = \alpha \frac{k^2}{a^2} \delta\theta + S_G(\Phi,\Psi).
\end{aligned}
$$

### 3.3 Modified Einstein Equations

Poisson-like equation:

$$
\frac{k^2}{a^2} \Psi = 4\pi G \bigl( \bar{\rho}_{\rm m} \delta_{\rm m} + \delta\rho_{\rm hum} + \delta\rho_G \bigr).
$$

Gravitational slip:

$$
\Phi - \Psi = \Pi_{\rm TCWT}.
$$

### 3.4 Matter Perturbations

$$
\begin{aligned}
\dot{\delta}_{\rm m} &= -\frac{k^2}{a^2} v + 3 \dot{\Psi}, \\
\dot{v} &= -\Phi.
\end{aligned}
$$

Modified growth rate: $f(a) = \dfrac{d \ln D}{d \ln a}$.

---
## Hum Sector Energy–Momentum Tensor (TCWT)

### 4. Covariant Hum Lagrangian

The Hum sector of TCWT is governed by the covariant Lagrangian

\[
\mathcal{L}_{\rm hum}
= -\frac{1}{2} C_0 \left(u^\mu \nabla_\mu \theta - \Omega\right)^2
- V_\Omega(\Omega)
- \kappa\, h^{\mu\nu} \nabla_\mu \theta \nabla_\nu \theta,
\]

where:

- \(u^\mu\) is the cosmological 4‑velocity  
- \(h^{\mu\nu} = g^{\mu\nu} + u^\mu u^\nu\) projects spatially  
- \(\theta\) is the Hum phase  
- \(\Omega\) is the informational drag  
- \(C_0, \kappa\) are TCWT constants  

The stress–energy tensor is

\[
T_{\mu\nu} = -2\frac{\partial \mathcal{L}}{\partial g^{\mu\nu}} + g_{\mu\nu}\mathcal{L}.
\]

---

### 2. Background FLRW Fields

Metric:

\[
ds^2 = -dt^2 + a^2(t)\,\delta_{ij}dx^i dx^j.
\]

Homogeneous fields:

\[
\theta = \bar{\theta}(t), \qquad \Omega = \bar{\Omega}(t).
\]

Define the background kinetic combination:

\[
X \equiv \dot{\bar{\theta}} - \bar{\Omega}.
\]

---

### 3. Background Energy Density and Pressure

The background Hum Lagrangian is

\[
\mathcal{L}^{\rm (bg)}_{\rm hum}
= -\frac{1}{2} C_0 X^2 - V_\Omega(\bar{\Omega}).
\]

This yields the explicit background energy density and pressure:

\[
\bar{\rho}_{\rm hum}
= \frac{1}{2} C_0 X^2 + V_\Omega(\bar{\Omega}),
\]

\[
\bar{p}_{\rm hum}
= \frac{1}{2} C_0 X^2 - V_\Omega(\bar{\Omega}).
\]

---

### 4. Perturbations in Newtonian Gauge

Metric:

\[
ds^2 = -(1+2\Phi)\,dt^2 + a^2(t)(1-2\Psi)\delta_{ij}dx^i dx^j.
\]

Perturbed fields:

\[
\theta = \bar{\theta} + \delta\theta, \qquad
\Omega = \bar{\Omega} + \delta\Omega.
\]

To first order:

\[
u^\mu \nabla_\mu \theta
= \dot{\bar{\theta}} + \delta\dot{\theta} - \Phi\,\dot{\bar{\theta}}.
\]

Thus:

\[
u^\mu\nabla_\mu\theta - \Omega
= X + \left(\delta\dot{\theta} - \delta\Omega - \Phi\,\dot{\bar{\theta}}\right).
\]

---

### 5. Perturbed Energy Density

\[
\delta\rho_{\rm hum}
= C_0 X\left(\delta\dot{\theta} - \delta\Omega - \Phi\,\dot{\bar{\theta}}\right)
+ V_\Omega'(\bar{\Omega})\,\delta\Omega.
\]

---

### 6. Perturbed Pressure

\[
\delta p_{\rm hum}
= C_0 X\left(\delta\dot{\theta} - \delta\Omega - \Phi\,\dot{\bar{\theta}}\right)
- V_\Omega'(\bar{\Omega})\,\delta\Omega.
\]

---

### 7. Anisotropic Stress

Because the Hum background has no spatial gradients, the gradient sector contributes only at second order.

Thus the Hum sector has no linear anisotropic stress:

\[
\sigma_{\rm hum} = 0.
\]

## 5. Numerical Implementation of TCWT (Boltzmann-Style Framework)

[Outline of background module, perturbation module, observable module, minimal parameter set, and staged implementation strategy — content as in original document.]

## 6. Parameter Fitting and Observational Confrontation

[Parameter lists, datasets, statistical inference framework, key signatures, model comparison — content as in original document.]

## 7. Hum Condensation and the Origin of Matter and Dark Energy

[Condensation point, latent heat and ghost surge, post-condensation evolution, physical interpretation — content as in original document.]

## Summary

This document provides the cosmological layer of TCWT:

- background expansion
- linear perturbation theory
- mapping phase fluctuations to density contrast
- the TCWT growth equation
- the route to the matter power spectrum

This completes the theoretical machinery needed to compare TCWT with $\Lambda$CDM across cosmological scales.
