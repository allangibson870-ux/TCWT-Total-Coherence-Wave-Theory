# TCWT Cosmological Perturbations

This document extends the TCWT Lagrangian into the cosmological regime. It derives the background expansion, linear perturbations, modified Einstein equations, and the structure-growth equation, providing the machinery needed to compare TCWT with ΛCDM on cosmological scales.

## 1. Relativistic TCWT Action

TCWT is built on three interacting fields: the Hum phase field θ, the local oscillation frequency Ω, and the ghost-relaxation field G.

### 1.1 Covariant Structure
We work in a general spacetime with metric $g_μν$. Introduce:
- A unit timelike 4-velocity $u^μ$ representing the cosmological rest frame,
- The spatial projector $h_μν = g_μν + u_μ u_ν$.

These define:
- Temporal derivative: $D_t ≡ u^μ ∇_μ$,
- Spatial gradient: $∇_⊥^μ = h^μν ∇_ν$,
- Spatial Laplacian: $Δ = h^μν ∇_μ ∇_ν$.

In an FLRW background these reduce to ordinary time derivatives and spatial gradients.

### 1.2 Covariant TCWT Lagrangian
$L_{TCWT} = - (1/2) C_0 (D_t θ - Ω)^2 - κ a_0² F( (h^μν ∇_μ θ ∇_ν θ) / a_0² ) - V_Ω(Ω) - α (D_t G - Δ θ)^2 + L_soliton$

### 1.3 Full Action
$S = ∫ d^4x √(-g) [ R/(16πG) + L_TCWT ]$

## 2. Background Cosmology

### 2.1 FLRW Metric and Homogeneous Fields
$ds² = -dt² + a²(t) δ_ij dx^i dx^j$, $H = ȧ/a$

Homogeneous background fields: $\bar θ(t)$, $\bar Ω(t)$, $\bar G(t)$.

Define $X ≡ \dot{\bar θ} - \bar Ω$.

### 2.2 Background Energy Densities and Pressures

**Hum sector:**
$\bar ρ_{hum} = (1/2) C_0 X² + V_Ω(\bar Ω)$, $\bar p_{hum} = (1/2) C_0 X² - V_Ω(\bar Ω)$

**Ghost sector:**
$\bar ρ_{ghost} = α \dot{\bar G}²$, $\bar p_{ghost} = α \dot{\bar G}²$

### 2.3 Modified Friedmann Equations
$H² = (8πG/3) (ρ-bar_hum + ρ-bar_ghost + ρ-bar_m + ρ-bar_rad)$

$\dot H = -4πG (ρ-bar_tot + p-bar_tot)$

## 3. Linear Perturbations

### 3.1 Newtonian Gauge
$ds² = -(1 + 2Φ) dt² + a²(t) (1 - 2Ψ) δ_ij dx^i dx^j$

Perturbed fields: θ = $\bar θ$ + δθ, Ω = $\bar Ω$ + δΩ, G = $\bar G$ + δG.

Matter perturbations: ρ_m = $\bar ρ_m$ (1 + δ_m), velocity $v_i = ∂_i v$.

## 4. Hum Sector Energy-Momentum Tensor

Perturbed energy density:
$δρ_hum = C_0 X (\dot{δθ} - δΩ - Φ \dot{\bar θ}) + V_Ω'( \bar Ω ) δΩ$

Perturbed pressure is similar (adiabatic to leading order). Anisotropic stress $σ_hum = 0$.

## 5. Ghost Sector Energy-Momentum Tensor

Perturbed energy density:
$δρ_ghost = 2α \dot{\bar G} (\dot{δG} - Φ \dot{\bar G} - (k²/a²) δθ)$

Perturbed pressure $δp_ghost ≈ δρ_ghost$. Anisotropic stress $σ_ghost = 0$.

## 6. Modified Poisson Equation

In the Newtonian gauge, the gravitational potential is sourced by:

$(k²/a
²) Ψ = 4πG [ \bar ρ_m δ_m + δρ_hum + δρ_ghost ]$

Since anisotropic stress vanishes from both sectors, Φ = Ψ (no gravitational slip at linear level).

## 7. Matter Perturbations
$ \dot{δ_m} = - (k²/a²) v + 3 \dot Ψ $, $ \dot v = - Φ $

## 8. TCWT Growth Equation

Using the mapping $δ_m ∝ -k² δθ$ (valid on sub-horizon scales), the density contrast evolves as:

$ \ddot δ + 2 H_{TCWT} \dot δ - 4π G_eff(a) \bar ρ_m δ + F_wilt(a,k) δ = 0 $

where $G_eff(a)$ encodes modifications from the Hum and Ghost sectors, and $F_wilt(a,k) ∝ β k^4 / a^4$ is the phase-relaxation damping term.

## 9. Effective CDM-like Behaviour for CMB Peaks

To reproduce ΛCDM acoustic peaks without a cold dark matter particle, the combined Hum + Ghost sector must behave as an effectively pressureless clustering component at recombination.

Require:
$c_{s,TCWT}^2 (k_peak, a_rec) ≪ 1$

and
$\bar ρ_{TCWT,cl}(a_rec) ≈ \bar ρ_CDM(a_rec)$

This imposes constraints on $C_0$, $V_Ω(Ω)$, and $α$.

## TCWT FLRW Background Evolution

### Background Variables
We work in a flat FLRW universe with metric $ds^2 = -dt^2 + a^2(t)\delta_{ij}dx^idx^j$ and Hubble parameter $H = \dot{a}/a$.

The homogeneous background fields are:
- $\bar{\theta}(t)$ — background Hum phase field
- $\bar{\Omega}(t)$ — background informational drag field
- $\bar{G}(t)$ — background ghost regulator field

We define the key derived variable:
$$
X(t) \equiv \dot{\bar{\theta}} - \bar{\Omega}
$$
which drives the Hum sector energy density.

On the homogeneous background, spatial gradients vanish, so the MOND nonlinearity $F(x)$ is inactive.

### Exact Energy Density and Pressure
The TCWT contribution to the background is:

$$
\rho_{\rm TCWT} = \frac{1}{2} C_0 X^2 + V_\Omega(\bar{\Omega}) + \alpha \dot{\bar{G}}^2
$$

$$
p_{\rm TCWT} = \frac{1}{2} C_0 X^2 - V_\Omega(\bar{\Omega}) + \alpha \dot{\bar{G}}^2
$$

### Algebraic Constraint
From variation with respect to $\Omega$ we have the algebraic relation:

$$
X = \frac{1}{2 C_0} V_\Omega'(\bar{\Omega})
$$

### Ghost Evolution
The ghost field evolves as a constant leakage rate:

$$
\dot{\bar{G}} = \dot{\bar{G}}_0 = \text{constant}
$$

### Relaxation Dynamics for the Drag Field
To allow $\rho_{\rm TCWT}$ to evolve from early-time matter-like behaviour to late-time dark-energy-like behaviour, we introduce a relaxation law for the drag field:

$$
\frac{d\bar{\Omega}}{d\ln a} = -\gamma \, (\bar{\Omega} - \Omega_{\rm min})
$$

or equivalently in cosmic time:

$$
\dot{\bar{\Omega}} = -H \gamma \, (\bar{\Omega} - \Omega_{\rm min})
$$

where $\gamma > 0$ is the dimensionless relaxation rate and $\Omega_{\rm min}$ is the late-time minimum value of $\bar{\Omega}$.

### Full Background System
The complete background evolution is governed by:
- The Friedmann and acceleration equations using $\rho_{\rm TCWT}$ and $p_{\rm TCWT}$ above,
- The algebraic constraint relating $X$ and $\bar{\Omega}$,
- The constant ghost leakage $\dot{\bar{G}} = \dot{\bar{G}}_0$,
- The relaxation equation for $\bar{\Omega}$.

This closes the system and provides a genuine, evolving TCWT-driven cosmology without relying on an external $\Lambda$ term.

### New Parameters Introduced
- `gamma_tcwt` — relaxation rate $\gamma$
- `omega_min_tcwt` — late-time floor $\Omega_{\rm min}$
- `omega_ini_tcwt` — initial value of $\bar{\Omega}$ at early times
- `gdot0_tcwt` — constant ghost leakage rate $\dot{\bar{G}}_0$

These parameters allow TCWT to transition naturally from radiation/matter domination at early times to accelerated expansion at late times.

## 10. Summary

This document provides the cosmological layer of TCWT:
- Covariant action and background expansion
- Linear perturbation theory
- Explicit Hum and Ghost energy-momentum tensors
- Modified Poisson and growth equations
- Conditions for matching CMB acoustic peaks

Together with the Master Framework, this completes the theoretical machinery needed to test TCWT against precision cosmological data.

**Next steps**: Implement the perturbation system in CLASS, perform MCMC fits, and quantify how well the Hum + Ghost sector can simultaneously satisfy CMB peaks and galactic MOND behaviour.
