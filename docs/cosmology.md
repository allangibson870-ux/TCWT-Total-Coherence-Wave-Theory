# TCWT Cosmological Perturbations

This document introduces the cosmological perturbation framework for the Total Coherence Wave Theory (TCWT). It extends the TCWT Lagrangian into the cosmological regime, deriving the background expansion, linear perturbations, and the structure‑growth equation that replaces the ΛCDM growth model.

---
# Relativistic TCWT Action

TCWT is built on three interacting fields:
- the Hum phase field \( \theta \),
- the local oscillation frequency \( \Omega \),
- and the ghost‑relaxation field \( G \).

To connect the theory to cosmology, structure formation, and gravitational observables, we require a fully covariant action defined on a spacetime metric \( g_{\mu\nu} \). The relativistic action must reduce to the Master Lagrangian in the weak‑field, quasistatic limit.

## 1. Covariant Structure

We introduce:
- a unit timelike 4‑velocity \( u^\mu \) representing the cosmological rest frame,
- a spatial projector \( h^{\mu\nu} = g^{\mu\nu} + u^\mu u^\nu \).

These allow us to define:
- temporal derivatives: \( u^\mu \nabla_\mu \),
- spatial gradients: \( h^{\mu\nu}\nabla_\nu \),
- spatial Laplacian: \( h^{\mu\nu}\nabla_\mu\nabla_\nu \).

In an FLRW background, these reduce to:
\[
u^\mu \nabla_\mu \to \partial_t, \qquad
h^{\mu\nu}\nabla_\mu \to \nabla, \qquad
h^{\mu\nu}\nabla_\mu\nabla_\nu \to \nabla^2.
\]

## 2. The Relativistic TCWT Lagrangian

A covariant generalisation of the Master Lagrangian is:

\[
\mathcal{L}_{\rm TCWT}
=
-\frac{1}{2}C_0\big(u^\mu\nabla_\mu\theta - \Omega\big)^2
-\kappa a_0^2\,F\!\left(\frac{h^{\mu\nu}\nabla_\mu\theta\nabla_\nu\theta}{a_0^2}\right)
- V_\Omega(\Omega)
- \alpha\Big(u^\mu\nabla_\mu G - h^{\mu\nu}\nabla_\mu\nabla_\nu\theta\Big)^2
+ \mathcal{L}_{\rm soliton}.
\]

Each term corresponds directly to a component of the non‑relativistic theory:

- **Temporal coherence:**  
  \[
  -\frac{1}{2}C_0(u^\mu\nabla_\mu\theta - \Omega)^2
  \]
  → becomes \( C_0(\partial_t\theta - \Omega)^2 \).

- **Nonlinear gradient sector:**  
  \[
  -\kappa a_0^2 F\!\left(\frac{h^{\mu\nu}\nabla_\mu\theta\nabla_\nu\theta}{a_0^2}\right)
  \]
  → becomes \( \kappa a_0^2 F(|\nabla\theta|^2/a_0^2) \).

- **Frequency potential:**  
  \[
  -V_\Omega(\Omega)
  \]
  → unchanged.

- **Ghost‑leakage channel:**  
  \[
  -\alpha\big(u^\mu\nabla_\mu G - h^{\mu\nu}\nabla_\mu\nabla_\nu\theta\big)^2
  \]
  → becomes \( \alpha(\partial_t G - \nabla^2\theta)^2 \).

- **Matter sector:**  
  \(\mathcal{L}_{\rm soliton}\) encodes the effective behaviour of soliton matter.

## 3. Full Relativistic Action

\[
S = \int d^4x\,\sqrt{-g}\,\Bigg[
\frac{1}{16\pi G}R
+\mathcal{L}_{\rm TCWT}
\Bigg].
\]

This action:
- is fully covariant,
- reduces to the Master Lagrangian in the weak‑field limit,
- provides the foundation for cosmology, perturbations, and structure formation.

## 4. Next Steps

With the relativistic action defined, the next tasks are:
1. Derive the background (FLRW) equations.  
2. Derive linear perturbations.  
3. Implement numerical evolution for comparison with observations.

This completes Step 1 of the TCWT cosmological framework.

## 1. Background Dynamics

TCWT begins with the phase‑field Lagrangian:

\[
\mathcal{L}[\theta] =
\frac{1}{2}\,\Omega(\theta)\,(\partial_\mu\theta)(\partial^\mu\theta)
- V_{\mathrm{sat}}(\nabla\theta)
- U(\theta)
\]

where:

- \( \theta \) is the Hum phase  
- \( \Omega(\theta) \) is the informational density  
- \( V_{\mathrm{sat}} \) enforces gradient saturation  
- \( U(\theta) \) encodes slow ghost‑leakage dynamics  

We decompose:

\[
\theta(x,t) = \bar{\theta}(t) + \delta\theta(x,t)
\]

The background obeys:

\[
\frac{d}{dt}\left[\Omega(\bar{\theta})\,\dot{\bar{\theta}}\right]
+ U'(\bar{\theta}) = 0
\]

Ghost‑leakage contributes an effective energy density:

\[
\dot{G} \simeq \nabla^2\theta
\]

The TCWT analogue of the Friedmann equation becomes:

\[
H_{\mathrm{TCWT}}^2(a)
= \frac{8\pi G}{3}\rho_m(a)
+ \frac{1}{3M_{\mathrm{eff}}^2}
\left[
\frac{1}{2}\Omega(\bar{\theta})\dot{\bar{\theta}}^2
+ U(\bar{\theta})
+ \rho_G
\right]
\]

This defines the background expansion history.

---

## 2. Linear Perturbations

Expanding the action to second order in \( \delta\theta \):

\[
S^{(2)} = \int d^4x \Big[
\frac{1}{2}\Omega(\bar{\theta})(\partial_\mu\delta\theta)(\partial^\mu\delta\theta)
+ \frac{1}{2}\Omega'(\bar{\theta})\dot{\bar{\theta}}\,\delta\theta\,\dot{\delta\theta}
- \frac{1}{2}V''_{\mathrm{sat}}(\nabla\bar{\theta})(\nabla\delta\theta)^2
- \frac{1}{2}U''(\bar{\theta})\,\delta\theta^2
\Big]
\]

The resulting perturbation equation is:

\[
\ddot{\delta\theta}
+ \left(3H_{\mathrm{TCWT}} + \frac{\dot{\Omega}}{\Omega}\right)\dot{\delta\theta}
+ \left[
\frac{k^2}{a^2}c_s^2
+ m_{\mathrm{eff}}^2
+ \Gamma_{\mathrm{wilt}}
\right]\delta\theta
= 0
\]

with:

- \( c_s^2 = V''_{\mathrm{sat}} / \Omega \)  
- \( m_{\mathrm{eff}}^2 = U'' / \Omega \)  
- \( \Gamma_{\mathrm{wilt}} \): damping from phase‑relaxation  

This is the TCWT analogue of the Mukhanov–Sasaki equation.

---

## 3. Mapping Phase Perturbations to Density Contrast

Matter knots respond to perturbations in the phase gradient:

\[
\delta\rho_m \propto \nabla^2\delta\theta
\]

In Fourier space:

\[
\delta(k,t) = -\alpha\,k^2\,\delta\theta(k,t)
\]

Substituting into the perturbation equation yields the TCWT growth equation:

\[
\ddot{\delta}
+ 2H_{\mathrm{TCWT}}\dot{\delta}
- 4\pi G_{\mathrm{eff}}(a)\rho_m\,\delta
+ \mathcal{F}_{\mathrm{wilt}}(a,k)\,\delta
= 0
\]

Where:

- \( G_{\mathrm{eff}}(a) \) is the modified gravitational coupling  
- \( \mathcal{F}_{\mathrm{wilt}} \) is a scale‑dependent damping term  

This replaces the ΛCDM growth equation.

---

## 4. Matter Power Spectrum

Solving the growth equation gives the growth factor:

\[
\delta(a) = D(a)\,\delta(a_{\mathrm{init}})
\]

The matter power spectrum is:

\[
P_{\mathrm{TCWT}}(k,z)
= D^2(z)\,P_{\mathrm{prim}}(k)
\]

This is directly comparable to ΛCDM predictions for:

- large‑scale structure  
- BAO  
- weak lensing  
- redshift‑space distortions  

---

## 5 Hum Condensation and the Origin of Matter and Dark Energy

The early Universe in TCWT is governed by the dynamics of the three-field Hum system:
- the phase field \( \theta \),
- the local oscillation frequency \( \Omega \),
- and the ghost‑leakage field \( G \).

At high “Hum temperature” (large desynchronisation), the system sits far from its ground state:
\[
\partial_t\theta \neq \Omega, \qquad \Omega \neq \Omega_{\rm hum}.
\]
Both the temporal coherence term
\[
C_0(\partial_t\theta - \Omega)^2
\]
and the frequency potential
\[
V_\Omega(\Omega)
\]
are large, storing significant energy in the early Hum.

### 1. The Condensation Point \(T_C\)

As the Universe expands and the Hum cools, the system approaches a critical point \(T_C\) where the phase field becomes sufficiently coherent for stable solitonic structures (matter knots) to form. Above \(T_C\), no long-lived knots exist; below \(T_C\), they nucleate rapidly.

This transition is analogous to a phase condensation:
- the Hum field becomes more ordered,
- gradients sharpen,
- and the nonlinear sector \(F(|\nabla\theta|^2/a_0^2)\) begins to dominate locally.

### 2. Latent Heat and the Ghost Surge

During condensation, the mismatch
\[
(\partial_t G - \nabla^2\theta)
\]
becomes large as curvature is created faster than the ghost field can relax it. The ghost term in the Lagrangian,
\[
\alpha(\partial_t G - \nabla^2\theta)^2,
\]
therefore spikes. This produces a transient “latent heat” release into the ghost sector.

This ghost surge:
- is largest at the moment solitons form,
- decays as the Hum approaches synchrony,
- and provides a natural analogue of dark-energy-like behaviour during and after condensation.

### 3. Post-Condensation Evolution

After the condensation epoch:
- the Hum field becomes increasingly synchronized,
- the frequency field relaxes toward its preferred value,
  \[
  \Omega \to \Omega_{\rm hum},
  \]
- matter knots stabilize,
- and ghost leakage becomes slow and diffuse.

The late-time behaviour is governed by the approximate relation
\[
\partial_t G \approx \nabla^2\theta,
\]
which smooths curvature over cosmological timescales and contributes to the observed accelerated expansion.

### 4. Physical Interpretation

In TCWT, the emergence of matter and dark energy is unified:
- **Matter** arises from the condensation of the Hum phase into stable solitons.
- **Dark energy** arises from the relaxation of curvature into the ghost sector, especially during and after condensation.
- **Inflation-like behaviour** corresponds to the early, highly desynchronized Hum relaxing toward its synchronized ground state.

This provides a single, coherent mechanism for:
- the origin of structure,
- the latent-energy surge at condensation,
- and the long-term acceleration of the Universe.

## 6. Summary

This document provides the cosmological layer of TCWT:

- background expansion  
- linear perturbation theory  
- mapping phase fluctuations to density contrast  
- the TCWT growth equation  
- the route to the matter power spectrum  

This completes the theoretical machinery needed to compare TCWT with ΛCDM across cosmological scales.# Cosmology
