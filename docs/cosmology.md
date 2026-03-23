# TCWT Cosmological Perturbations

This document introduces the cosmological perturbation framework for the **Total Coherence Wave Theory (TCWT)**. It extends the TCWT Lagrangian into the cosmological regime, deriving the background expansion, linear perturbations, and the structure-growth equation that replaces the ΛCDM growth model.

## 1. Relativistic TCWT Action

TCWT is built on three interacting fields:

- the Hum phase field $\theta$,
- the local oscillation frequency $\Omega$,
- the ghost-relaxation field $G$.

To connect the theory to cosmology, structure formation, and gravitational observables, we require a fully covariant action defined on a spacetime metric $g_{\mu\nu}$. The relativistic action must reduce to the Master Lagrangian in the weak-field, quasistatic limit.

### 1.1 Covariant Structure

We introduce:

- a unit timelike 4-velocity $u^\mu$ representing the cosmological rest frame,
- a spatial projector $h^{\mu\nu} = g^{\mu\nu} + u^\mu u^\nu$.

These define:

- temporal derivatives: $u^\mu \nabla_\mu$,
- spatial gradients: $h^{\mu\nu} \nabla_\nu$,
- spatial Laplacian: $h^{\mu\nu} \nabla_\mu \nabla_\nu$.

In an FLRW background these reduce to:

$$
u^\mu \nabla_\mu \to \partial_t, \qquad
h^{\mu\nu} \nabla_\mu \to \nabla, \qquad
h^{\mu\nu} \nabla_\mu \nabla_\nu \to \nabla^2.
$$

### 1.2 Covariant TCWT Lagrangian

$$
\begin{aligned}
\mathcal{L}_{\rm TCWT} ={}& -\frac{1}{2} C_0 \bigl( u^\mu \nabla_\mu \theta - \Omega \bigr)^2 \\
& - \kappa a_0^2 \, F\!\left( \frac{h^{\mu\nu} \nabla_\mu \theta \nabla_\nu \theta}{a_0^2} \right) \\
& - V_\Omega(\Omega) \\
& - \alpha \bigl( u^\mu \nabla_\mu G - h^{\mu\nu} \nabla_\mu \nabla_\nu \theta \bigr)^2 \\
& - \mathcal{L}_{\rm soliton}.
\end{aligned}
$$

### 1.3 Full Relativistic Action

$$
S = \int d^4x \, \sqrt{-g} \left[ \frac{1}{16\pi G} R + \mathcal{L}_{\rm TCWT} \right].
$$

## 2. Background Cosmology

### 2.1 FLRW Metric and Homogeneous Fields

$$
ds^2 = -dt^2 + a^2(t) \delta_{ij} dx^i dx^j,
$$

Hubble rate:

$$
H = \frac{\dot{a}}{a}.
$$

Homogeneous fields:

$$
\theta = \bar{\theta}(t), \qquad \Omega = \bar{\Omega}(t), \qquad G = \bar{G}(t).
$$

### 2.2 Background TCWT Lagrangian

$$
\begin{aligned}
\mathcal{L}^{\rm (bg)}_{\rm TCWT} ={}& -\frac{1}{2} C_0 \bigl( \dot{\bar{\theta}} - \bar{\Omega} \bigr)^2 \\
& - V_\Omega(\bar{\Omega}) \\
& - \alpha \, \dot{\bar{G}}^2 \\
& - \mathcal{L}_{\rm soliton}^{\rm (bg)}.
\end{aligned}
$$

Define:

$$
X \equiv \dot{\bar{\theta}} - \bar{\Omega}.
$$

Background energy densities and pressures:

$$
\bar{\rho}_{\rm hum} = \frac{1}{2} C_0 X^2 + V_\Omega(\bar{\Omega}), \qquad
\bar{p}_{\rm hum} = \frac{1}{2} C_0 X^2 - V_\Omega(\bar{\Omega}),
$$

$$
\bar{\rho}_{\rm ghost} = \alpha \, \dot{\bar{G}}^2, \qquad
\bar{p}_{\rm ghost} = \alpha \, \dot{\bar{G}}^2.
$$

### 2.3 Modified Friedmann Equations

$$
H^2 = \frac{8\pi G}{3} \left( \bar{\rho}_{\rm hum} + \bar{\rho}_{\rm ghost} + \bar{\rho}_m + \bar{\rho}_{\rm rad} \right),
$$

$$
\dot{H} = -4\pi G (\rho_{\rm tot} + p_{\rm tot}).
$$

## 3. Linear Perturbations

### 3.1 Newtonian Gauge

$$
ds^2 = -(1 + 2\Phi) \, dt^2 + a^2(t) (1 - 2\Psi) \delta_{ij} dx^i dx^j.
$$

Perturbed fields:

$$
\theta = \bar{\theta} + \delta\theta, \qquad
\Omega = \bar{\Omega} + \delta\Omega, \qquad
G = \bar{G} + \delta G.
$$

Matter perturbations:

$$
\rho_m = \bar{\rho}_m (1 + \delta_m), \qquad v_i = \partial_i v.
$$

## 4. Hum Sector Energy–Momentum Tensor

### 4.1 Covariant Hum Lagrangian

$$
\mathcal{L}_{\rm hum} = -\frac{1}{2} C_0 (u^\mu \nabla_\mu \theta - \Omega)^2
- V_\Omega(\Omega)
- \kappa \, h^{\mu\nu} \nabla_\mu \theta \nabla_\nu \theta.
$$

### 4.2 Background Energy Density and Pressure

$$
\bar{\rho}_{\rm hum} = \frac{1}{2} C_0 X^2 + V_\Omega(\bar{\Omega}), \qquad
\bar{p}_{\rm hum} = \frac{1}{2} C_0 X^2 - V_\Omega(\bar{\Omega}).
$$

### 4.3 Perturbations

$$
u^\mu \nabla_\mu \theta = \dot{\bar{\theta}} + \delta\dot{\theta} - \Phi \dot{\bar{\theta}},
$$

$$
u^\mu \nabla_\mu \theta - \Omega = X + (\delta\dot{\theta} - \delta\Omega - \Phi \dot{\bar{\theta}}).
$$

Perturbed energy density:

$$
\delta\rho_{\rm hum} = C_0 X (\delta\dot{\theta} - \delta\Omega - \Phi \dot{\bar{\theta}}) + V_\Omega'(\bar{\Omega}) \delta\Omega.
$$

Perturbed pressure:

$$
\delta p_{\rm hum} = C_0 X (\delta\dot{\theta} - \delta\Omega - \Phi \dot{\bar{\theta}}) + V_\Omega'(\bar{\Omega}) \delta\Omega.
$$

Anisotropic stress:

$$
\sigma_{\rm hum} = 0.
$$

## 5. Ghost Sector Energy–Momentum Tensor

### 5.1 Covariant Ghost Lagrangian

$$
\mathcal{L}_{\rm ghost} = -\alpha \bigl( u^\mu \nabla_\mu G - h^{\mu\nu} \nabla_\mu \nabla_\nu \theta \bigr)^2.
$$

### 5.2 Background Energy Density and Pressure

$$
\bar{\rho}_{\rm ghost} = \alpha \, \dot{\bar{G}}^2, \qquad
\bar{p}_{\rm ghost} = \alpha \, \dot{\bar{G}}^2.
$$

### 5.3 Perturbations

$$
u^\mu \nabla_\mu G = \dot{\bar{G}} + \delta\dot{G} - \Phi \dot{\bar{G}},
$$

$$
h^{\mu\nu} \nabla_\mu \nabla_\nu \theta = -\frac{k^2}{a^2} \delta\theta.
$$

Perturbed energy density:

$$
\delta\rho_{\rm ghost} = 2\alpha \dot{\bar{G}} \Bigl( \delta\dot{G} - \Phi \dot{\bar{G}} - \frac{k^2}{a^2} \delta\theta \Bigr).
$$

Perturbed pressure:

$$
\delta p_{\rm ghost} = \delta\rho_{\rm ghost}.
$$

Anisotropic stress:

$$
\sigma_{\rm ghost} = 0.
$$

## 6. Modified Einstein Equations

### 6.1 Explicit Poisson Equation (Option 1)

$$
\frac{k^2}{a^2} \Psi = 4\pi G \Biggl[ \bar{\rho}_m \delta_m
+ C_0 X (\delta\dot{\theta} - \delta\Omega - \Phi \dot{\bar{\theta}})
+ V_\Omega'(\bar{\Omega}) \delta\Omega
+ 2\alpha \dot{\bar{G}} \Bigl( \delta\dot{G} - \Phi \dot{\bar{G}} - \frac{k^2}{a^2} \delta\theta \Bigr) \Biggr].
$$

### 6.2 Slip Relation

$$
\sigma_{\rm hum} = \sigma_{\rm ghost} = 0 \quad \Rightarrow \quad \Phi = \Psi.
$$

## 7. Matter Perturbations

$$
\dot{\delta}_m = -\frac{k^2}{a^2} v + 3 \dot{\Psi},
$$

$$
\dot{v} = -\Phi.
$$

## 8. TCWT Growth Equation

Using the mapping

$$
\delta_m \propto -k^2 \delta\theta,
$$

and substituting into the perturbation equations yields the TCWT growth equation:

$$
\ddot{\delta} + 2 H_{\rm TCWT} \dot{\delta} - 4\pi G_{\rm eff}(a) \bar{\rho}_m \delta + \mathcal{F}_{\rm wilt}(a,k) \delta = 0,
$$

where:

- $G_{\rm eff}(a)$ encodes Hum + Ghost modifications,
- $\mathcal{F}_{\rm wilt}(a,k)$ is the phase-relaxation damping term.

## 9. Effective Dark-Matter-Like Behaviour for CMB Peaks

On CMB scales, TCWT must reproduce the ΛCDM-like acoustic peak structure without a cold dark matter particle. This requires that the combined Hum+Ghost sector behaves as an effectively pressureless clustering component before recombination.

### 9.1 Effective DM-like density and sound speed

Define the effective TCWT clustering density

$$
\bar{\rho}_{\rm TCWT,cl}(a) \equiv \bar{\rho}_{\rm hum}(a) + \bar{\rho}_{\rm ghost}(a),
$$

and its perturbation

$$
\delta_{\rm TCWT,cl} \equiv \frac{\delta\rho_{\rm hum} + \delta\rho_{\rm ghost}}{\bar{\rho}_{\rm hum} + \bar{\rho}_{\rm ghost}}.
$$

Effective sound speed:

$$
c_{s,{\rm TCWT}}^2 \equiv \frac{\delta p_{\rm hum} + \delta p_{\rm ghost}}{\delta\rho_{\rm hum} + \delta\rho_{\rm ghost}}.
$$

For TCWT to mimic cold dark matter at CMB acoustic scales ($k \sim k_{\rm peak}$), we require

$$
c_{s,{\rm TCWT}}^2(k_{\rm peak}, a_{\rm rec}) \ll 1,
$$

so that the Hum+Ghost sector does not support significant pressure waves at recombination.

### 9.2 Modified Poisson equation in DM-like limit

In the regime where $c_{s,{\rm TCWT}}^2 \to 0$ and Hum+Ghost cluster like CDM:

$$
\frac{k^2}{a^2} \Psi \simeq 4\pi G \Bigl[ \bar{\rho}_b \delta_b + \bar{\rho}_{\rm TCWT,cl} \delta_{\rm TCWT,cl} \Bigr],
$$

with $\bar{\rho}_b$ the baryon density. Matching the ΛCDM CMB peak pattern then imposes

$$
\bar{\rho}_{\rm TCWT,cl}(a_{\rm rec}) \simeq \bar{\rho}_{\rm CDM}^{\Lambda{\rm CDM}}(a_{\rm rec}),
$$

up to small corrections from residual TCWT pressure and scale dependence.

### 9.3 Phase-stiffness constraint

The phase-stiffness parameters $C_0$, $\kappa$, and the Hum potential $V_\Omega(\Omega)$ must be chosen such that

$$
\left| \frac{\delta p_{\rm hum} + \delta p_{\rm ghost}}{\delta\rho_{\rm hum} + \delta\rho_{\rm ghost}} \right| \ll 1
\quad \text{for} \quad k \sim k_{\rm peak},\ a \sim a_{\rm rec},
$$

ensuring that the Hum+Ghost sector behaves as a nearly pressureless clustering component at recombination.

## 10. CMB Peak Matching and the $C_0$ Constraint

To reproduce the ΛCDM-like acoustic peak structure without cold dark matter, TCWT must generate the same gravitational potential at the acoustic scale ($k_{\rm peak}$) during recombination. This imposes a direct constraint on the temporal coherence stiffness $C_0$.

### 10.1 Matching the gravitational potential at recombination

ΛCDM Poisson equation at recombination:

$$
\frac{k^2}{a^2} \Psi_{\Lambda{\rm CDM}} = 4\pi G \Bigl[ \bar{\rho}_b \delta_b + \bar{\rho}_{\rm cdm} \delta_{\rm cdm} \Bigr].
$$

TCWT version:

$$
\frac{k^2}{a^2} \Psi_{\rm TCWT} = 4\pi G \Biggl[ \bar{\rho}_m \delta_m
+ C_0 X (\delta\dot{\theta} - \delta\Omega - \Phi \dot{\bar{\theta}})
+ V_\Omega'(\bar{\Omega}) \delta\Omega
+ 2\alpha \dot{\bar{G}} \Bigl( \delta\dot{G} - \Phi \dot{\bar{G}} - \frac{k^2}{a^2} \delta\theta \Bigr) \Biggr].
$$

Requiring $\Psi_{\rm TCWT}(k_{\rm peak}, a_{\rm rec}) = \Psi_{\Lambda{\rm CDM}}(k_{\rm peak}, a_{\rm rec})$ yields a constraint on $C_0$.

### 10.2 Exact constraint equation for $C_0$

$$
\boxed{
C_0(k,a) = \frac{
\bar{\rho}_b \delta_b + \bar{\rho}_{\rm cdm} \delta_{\rm cdm}
- \bar{\rho}_m \delta_m
- V_\Omega'(\bar{\Omega}) \delta\Omega
- 2\alpha \dot{\bar{G}} \Bigl( \delta\dot{G} - \Phi \dot{\bar{G}} - \frac{k^2}{a^2} \delta\theta \Bigr)
}{
X (\delta\dot{\theta} - \delta\Omega - \Phi \dot{\bar{\theta}})
}
}
$$

evaluated at $k = k_{\rm peak}$, $a = a_{\rm rec}$.

### 10.3 Interpretation

- The numerator is the ΛCDM gravitational source minus non-temporal TCWT contributions.
- The denominator is the Hum temporal coherence response.
- Larger $C_0$ → stiffer Hum field → better reproduction of potential wells that drive CMB acoustic oscillations.
- **Parameter degeneracy note**: The potential at recombination can be supported by multiple TCWT sectors (temporal Hum, $V_\Omega' \delta\Omega$, ghost leakage). Different combinations of $(C_0, V_\Omega, \alpha)$ and background evolution can reproduce the same CMB peaks. Thus the constraint defines a family of allowed parameter sets, not a unique value of $C_0$.

This provides the direct link between TCWT microphysics and CMB observables.

## 11. Summary

This document provides the full cosmological layer of TCWT:

- covariant action
- background expansion
- linear perturbation theory
- explicit Hum and Ghost energy–momentum tensors
- explicit modified Poisson equation
- matter perturbations
- TCWT growth equation
- CMB acoustic peak matching and $C_0$ constraint

This completes the theoretical machinery needed to compare TCWT with ΛCDM across cosmological scales.
