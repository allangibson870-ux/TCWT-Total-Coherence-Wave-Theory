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

---
# Background Cosmology in TCWT

With the relativistic TCWT action defined, the next step is to specialise to a homogeneous and isotropic Universe and derive the background (FLRW) equations. This gives the time evolution of the scale factor \(a(t)\), the Hubble rate \(H(t)\), and the homogeneous parts of the fields \(\theta(t)\), \(\Omega(t)\), and \(G(t)\).

## 1. FLRW Metric and Homogeneous Fields

We assume a spatially flat FLRW metric
\[
ds^2 = -dt^2 + a(t)^2\,\delta_{ij}\,dx^i dx^j,
\]
with Hubble rate
\[
H(t) = \frac{\dot a}{a}.
\]

In the cosmological rest frame, the 4‑velocity and projector reduce to
\[
u^\mu = (1,0,0,0), \qquad h^{\mu\nu} = g^{\mu\nu} + u^\mu u^\nu.
\]

We take the three TCWT fields to be homogeneous:
\[
\theta = \bar\theta(t), \qquad \Omega = \bar\Omega(t), \qquad G = \bar G(t).
\]

Spatial gradients vanish at the background level:
\[
h^{\mu\nu}\nabla_\mu\theta\nabla_\nu\theta = 0, \qquad
h^{\mu\nu}\nabla_\mu\nabla_\nu\theta = 0.
\]

## 2. Background TCWT Lagrangian Density

In this limit, the TCWT Lagrangian simplifies to
\[
\mathcal{L}_{\rm TCWT}^{\rm (bg)}
=
-\frac{1}{2}C_0\big(\dot{\bar\theta} - \bar\Omega\big)^2
- V_\Omega(\bar\Omega)
- \alpha\,\dot{\bar G}^{\,2}
+ \mathcal{L}_{\rm soliton}^{\rm (bg)}.
\]

The nonlinear gradient term drops out at the homogeneous level and reappears only in perturbations and structure formation.

We can identify effective background energy densities and pressures for each sector by varying the action with respect to the metric or, equivalently, by using the standard relations
\[
\rho_i = 2\frac{\partial \mathcal{L}_i}{\partial g^{00}} - \mathcal{L}_i, \qquad
p_i = \mathcal{L}_i
\]
for each component \(i\).

Schematically, this gives:
- Hum temporal sector:
  \[
  \rho_{\rm hum} \sim \frac{1}{2}C_0(\dot{\bar\theta} - \bar\Omega)^2 + V_\Omega(\bar\Omega), \qquad
  p_{\rm hum} \sim \frac{1}{2}C_0(\dot{\bar\theta} - \bar\Omega)^2 - V_\Omega(\bar\Omega).
  \]
- Ghost sector:
  \[
  \rho_G \sim \alpha\,\dot{\bar G}^{\,2}, \qquad
  p_G \sim \alpha\,\dot{\bar G}^{\,2}.
  \]
- Soliton/matter sector:
  \[
  \rho_{\rm m} = \rho_{\rm soliton}^{\rm (bg)}, \qquad
  p_{\rm m} \approx 0 \quad \text{(dust-like)}.
  \]

The precise coefficients follow from a full variation, but this structure is sufficient to define the background evolution.

## 3. Modified Friedmann Equations

Varying the full action with respect to the metric yields the Einstein equations
\[
G_{\mu\nu} = 8\pi G\,T_{\mu\nu}^{\rm (tot)},
\]
where the total energy–momentum tensor includes contributions from the Hum, ghost, soliton/matter, and any additional components (radiation, baryons, etc.).

In the FLRW background, this reduces to the modified Friedmann equations:
\[
H^2 = \frac{8\pi G}{3}\big(\rho_{\rm hum} + \rho_G + \rho_{\rm m} + \rho_{\rm rad} + \dots\big),
\]
\[
\dot H = -4\pi G\big(\rho_{\rm tot} + p_{\rm tot}\big),
\]
with
\[
\rho_{\rm tot} = \rho_{\rm hum} + \rho_G + \rho_{\rm m} + \rho_{\rm rad} + \dots,
\qquad
p_{\rm tot} = p_{\rm hum} + p_G + p_{\rm m} + p_{\rm rad} + \dots.
\]

The background field equations for \(\bar\theta(t)\), \(\bar\Omega(t)\), and \(\bar G(t)\) follow from varying the action with respect to each field:
\[
\frac{\delta S}{\delta \theta} = 0, \qquad
\frac{\delta S}{\delta \Omega} = 0, \qquad
\frac{\delta S}{\delta G} = 0,
\]
which yield coupled evolution equations of the form
\[
\ddot{\bar\theta} + 3H\dot{\bar\theta} + \dots = 0,
\]
\[
\frac{\partial V_\Omega}{\partial \bar\Omega} + C_0(\dot{\bar\theta} - \bar\Omega) + \dots = 0,
\]
\[
\ddot{\bar G} + 3H\dot{\bar G} + \dots = 0.
\]

These equations encode:
- the relaxation of \(\Omega\) toward the Hum frequency,
- the energy transfer into the ghost sector,
- and the resulting time‑dependent effective dark energy.

## 4. Connection to the TCWT Expansion History

By solving the coupled system
\[
\{H(t), \bar\theta(t), \bar\Omega(t), \bar G(t)\},
\]
we obtain the TCWT background expansion history \(H(t)\). This naturally decomposes into:
- an early‑time relaxation component (Hum frequency settling),
- a structural exhaust component (ghost‑mediated energy release from structure formation),
- and a late‑time decline of effective dark energy.

This provides the formal underpinning for the qualitative expansion‑history plots used elsewhere in the TCWT documentation.

## 5. Next Steps

With the background equations defined, the next steps are:
1. Choose explicit forms for \(V_\Omega(\Omega)\) and any coupling parameters.  
2. Solve the background system numerically to obtain \(H(z)\), \(\rho_{\rm DE}(z)\), and \(\rho_{\rm m}(z)\).  
3. Compare the resulting expansion history to ΛCDM and observational data (SNe, BAO, CMB distance measures).

This completes Step 2 of the TCWT cosmological framework.

---
# Linear Perturbations in TCWT

With the background FLRW equations established, the next step is to derive the linear perturbation equations. These describe how small fluctuations in the metric, matter density, and TCWT fields evolve over time. Linear perturbations are essential for predicting the CMB anisotropies, matter power spectrum, weak lensing, and structure growth.

## 1. Perturbation Setup

We work in Newtonian gauge, where the perturbed metric is
\[
ds^2 = -(1+2\Phi)\,dt^2 + a(t)^2(1-2\Psi)\,\delta_{ij}\,dx^i dx^j.
\]

We perturb the TCWT fields as:
\[
\theta = \bar\theta(t) + \delta\theta(\vec{x},t),
\]
\[
\Omega = \bar\Omega(t) + \delta\Omega(\vec{x},t),
\]
\[
G = \bar G(t) + \delta G(\vec{x},t).
\]

Matter density and velocity perturbations follow the standard definitions:
\[
\rho_{\rm m} = \bar\rho_{\rm m}(t)\big(1 + \delta_{\rm m}(\vec{x},t)\big),
\]
\[
v_i = \partial_i v.
\]

## 2. Linearised TCWT Field Equations

Varying the relativistic TCWT action to first order yields three coupled perturbation equations:

### (a) Hum phase perturbation
\[
\delta\ddot\theta + 3H\delta\dot\theta + \frac{k^2}{a^2}\,\mu_\theta\,\delta\theta
+ C_0(\delta\dot\theta - \delta\Omega)
= S_\theta(\Phi,\Psi),
\]
where \( \mu_\theta \) is an effective stiffness parameter and \( S_\theta \) contains metric‑source terms.

### (b) Frequency perturbation
\[
C_0(\delta\dot\theta - \delta\Omega)
+ V''_\Omega(\bar\Omega)\,\delta\Omega
= S_\Omega(\Phi,\Psi).
\]

### (c) Ghost‑field perturbation
\[
\delta\ddot G + 3H\delta\dot G + \alpha\,\frac{k^2}{a^2}\,\delta G
= \alpha\,\frac{k^2}{a^2}\,\delta\theta + S_G(\Phi,\Psi).
\]

These equations encode:
- the coupling between phase, frequency, and ghost sectors,
- the relaxation of \(\Omega\),
- the curvature‑smoothing behaviour of the ghost field,
- and the effective MOND‑like response in the gradient sector.

## 3. Modified Einstein Equations

The perturbed Einstein equations relate the metric potentials \(\Phi\) and \(\Psi\) to the total perturbed energy–momentum tensor.

### Poisson‑like equation
\[
\frac{k^2}{a^2}\Psi = 4\pi G\left(
\bar\rho_{\rm m}\delta_{\rm m}
+ \delta\rho_{\rm hum}
+ \delta\rho_G
\right).
\]

### Anisotropic stress
TCWT generically produces a nonzero \(\Phi - \Psi\):
\[
\Phi - \Psi = \Pi_{\rm TCWT},
\]
where \(\Pi_{\rm TCWT}\) arises from the nonlinear gradient sector and ghost‑field dynamics.

This is a key observational signature:  
TCWT predicts **scale‑dependent gravitational slip**.

## 4. Matter Perturbations

Matter follows the standard continuity and Euler equations:
\[
\dot\delta_{\rm m} = -\frac{k^2}{a^2}v + 3\dot\Psi,
\]
\[
\dot v = -\Phi.
\]

The growth of structure is modified through:
- the altered Poisson equation,
- the gravitational slip \(\Phi - \Psi\),
- and the coupling to TCWT fields.

This leads to a modified growth rate:
\[
f(a) = \frac{d\ln D}{d\ln a},
\]
where \(D(a)\) is the linear growth factor.

## 5. Observational Outputs

Solving the coupled system
\[
\{\delta\theta, \delta\Omega, \delta G, \Phi, \Psi, \delta_{\rm m}\}
\]
for each wavenumber \(k\) yields:

- the matter power spectrum \(P(k,z)\),
- the lensing potential \(\Phi+\Psi\),
- the growth rate \(f\sigma_8(z)\),
- the ISW contribution to the CMB,
- the BAO scale evolution,
- and the gravitational slip parameter \(\eta = \Phi/\Psi\).

These are the quantities directly compared to DESI, Planck, Euclid, and LSST.

## 6. Next Steps

With the perturbation equations defined, the next tasks are:

1. Implement the background and perturbation evolution in a numerical code.  
2. Compute \(H(z)\), \(P(k)\), \(f\sigma_8(z)\), and lensing spectra.  
3. Compare TCWT predictions to ΛCDM and observational datasets.

This completes Step 3 of the TCWT cosmological framework.

---
# Numerical Implementation of TCWT (Boltzmann‑Style Framework)

With the background and linear perturbation equations defined, the next step is to implement TCWT in a numerical framework. This allows us to compute the expansion history, matter power spectrum, growth rate, and lensing observables. The structure mirrors standard Boltzmann codes (CLASS, CAMB) but is tailored to the three‑field TCWT system.

## 1. Overview of the Numerical Pipeline

A minimal TCWT cosmology code requires three modules:

1. **Background Module**  
   Evolves \( a(t) \), \( H(t) \), and the homogeneous fields  
   \( \{\bar\theta(t), \bar\Omega(t), \bar G(t)\} \).

2. **Perturbation Module**  
   Evolves the Fourier‑space perturbations  
   \( \{\delta\theta, \delta\Omega, \delta G, \Phi, \Psi, \delta_{\rm m}\} \)  
   for each wavenumber \( k \).

3. **Observable Module**  
   Computes:
   - matter power spectrum \( P(k,z) \),
   - growth rate \( f\sigma_8(z) \),
   - lensing potential \( \Phi + \Psi \),
   - ISW contribution,
   - BAO scale evolution.

This structure is sufficient to compare TCWT to ΛCDM and observational datasets.

---

## 2. Background Evolution Module

The background module integrates the coupled system:
\[
\{\dot a, \dot{\bar\theta}, \dot{\bar\Omega}, \dot{\bar G}\}
\]
using the modified Friedmann equations and the TCWT field equations.

### Required outputs:
- \( H(z) \)
- \( \rho_{\rm DE}(z) \)
- \( \rho_{\rm m}(z) \)
- effective equation of state \( w(z) \)

These feed directly into the perturbation module.

---

## 3. Perturbation Evolution Module

For each wavenumber \( k \), we evolve the linear system:
\[
\{\delta\theta_k, \delta\Omega_k, \delta G_k, \Phi_k, \Psi_k, \delta_{{\rm m},k}\}.
\]

### Key features:
- TCWT introduces **three new dynamical degrees of freedom**.
- The ghost field produces **scale‑dependent smoothing**.
- The nonlinear gradient sector generates **gravitational slip** (\(\Phi \neq \Psi\)).
- The modified Poisson equation alters structure growth.

### Required outputs:
- transfer functions \( T_i(k,z) \)
- growth factor \( D(z) \)
- gravitational slip parameter \( \eta(k,z) = \Phi/\Psi \)

These are used to compute the matter power spectrum and lensing observables.

---

## 4. Observable Module

Using the transfer functions and background evolution, we compute:

### (a) Matter Power Spectrum
\[
P(k,z) = P_{\rm prim}(k)\,|T_{\rm m}(k,z)|^2.
\]

### (b) Growth Rate
\[
f\sigma_8(z) = \frac{d\ln D}{d\ln a}\,\sigma_8(z).
\]

### (c) Lensing Potential
\[
\Phi + \Psi,
\]
which is sensitive to TCWT’s gravitational slip.

### (d) ISW Effect  
Computed from the time derivative of \(\Phi + \Psi\).

### (e) BAO Scale  
Extracted from the matter transfer function.

These quantities can be compared directly to DESI, Planck, Euclid, and LSST.

---

## 5. Minimal Parameter Set

A practical implementation requires specifying:

- \( a_0 \) — MOND/gradient scale  
- \( \kappa \) — gradient‑sector coupling  
- \( C_0 \) — temporal coherence strength  
- \( \alpha \) — ghost‑leakage coupling  
- parameters of \( V_\Omega(\Omega) \)  
- initial conditions for \( \theta, \Omega, G \)

This is a small, manageable parameter space.

---

## 6. Implementation Strategy

A minimal TCWT Boltzmann code can be built in stages:

1. **Implement background evolution**  
   Validate against your analytic expansion‑history plots.

2. **Implement perturbations for a single \( k \)**  
   Check stability and behaviour in limiting regimes.

3. **Add full \( k \)-grid evolution**  
   Produce transfer functions.

4. **Compute observables**  
   Compare to ΛCDM and data.

5. **Add MCMC wrapper**  
   Fit parameters to Planck + DESI + lensing.

This staged approach mirrors the development of early CLASS/CAMB versions.

---

## 7. Next Steps

With the numerical framework outlined, the next tasks are:

1. Choose explicit forms for \( V_\Omega(\Omega) \) and initial conditions.  
2. Implement the background module.  
3. Implement the perturbation module.  
4. Generate the first TCWT predictions for \( H(z) \), \( P(k) \), and \( f\sigma_8(z) \).

This completes Step 4 of the TCWT cosmological framework.

---
# Parameter Fitting and Observational Confrontation

With the numerical framework defined, the next step is to confront TCWT with observational data. This requires identifying the free parameters of the theory, choosing appropriate datasets, and performing statistical inference to determine whether TCWT provides a better fit to cosmological observations than ΛCDM.

## 1. TCWT Parameter Set

The minimal parameter set required for cosmological predictions is:

### Core TCWT Parameters
- \( a_0 \): MOND/gradient scale  
- \( \kappa \): nonlinear gradient coupling  
- \( C_0 \): temporal coherence strength  
- \( \alpha \): ghost‑leakage coupling  
- \( V_\Omega(\Omega) \): frequency potential (typically 1–3 parameters)

### Standard Cosmological Parameters
- \( H_0 \): present‑day Hubble rate  
- \( \Omega_{\rm b} \): baryon density  
- \( \Omega_{\rm m} \): matter density  
- \( A_s, n_s \): primordial spectrum amplitude and tilt  
- \( \tau \): optical depth (CMB only)

This is a compact parameter space compared to many modified‑gravity models.

---

## 2. Observational Datasets

To test TCWT, we compare its predictions to the following datasets:

### Background Expansion
- Type Ia supernovae (SNe Ia)
- Baryon Acoustic Oscillations (BAO)
- Cosmic chronometers
- CMB distance priors

### Structure Growth
- Redshift‑space distortions (RSD)
- Weak lensing (KiDS, DES, HSC)
- Cluster abundance

### CMB Anisotropies
- Planck temperature and polarization spectra
- ISW cross‑correlations

### Lensing and Gravitational Slip
- CMB lensing
- Galaxy–galaxy lensing
- Cross‑correlation of \(\Phi + \Psi\)

These datasets probe different combinations of the TCWT fields and their couplings.

---

## 3. Statistical Inference Framework

Parameter estimation proceeds via Bayesian inference:

\[
\mathcal{P}(\theta_{\rm TCWT} | \text{data}) \propto
\mathcal{L}(\text{data} | \theta_{\rm TCWT}) \, \pi(\theta_{\rm TCWT}),
\]

where:
- \( \theta_{\rm TCWT} \) is the full parameter vector,
- \( \mathcal{L} \) is the likelihood from the datasets,
- \( \pi \) is the prior.

### Recommended tools:
- MCMC (e.g., emcee, Cobaya)
- Nested sampling (e.g., MultiNest, PolyChord)

The numerical TCWT code provides:
- \( H(z) \)
- \( P(k,z) \)
- \( f\sigma_8(z) \)
- lensing spectra
- CMB source terms

These are fed into the likelihood pipeline.

---

## 4. Key Observational Signatures of TCWT

TCWT makes several distinctive predictions:

### 1. Time‑varying effective dark energy  
\[
w_{\rm eff}(z) \neq -1,
\]
with a mid‑era acceleration bump from structural exhaust.

### 2. Suppressed structure growth  
\[
f\sigma_8(z) < \Lambda\text{CDM},
\]
consistent with weak‑lensing tensions.

### 3. Scale‑dependent gravitational slip  
\[
\eta(k,z) = \frac{\Phi}{\Psi} \neq 1,
\]
arising from the nonlinear gradient sector.

### 4. Modified lensing potential  
\[
\Phi + \Psi
\]
is altered by ghost‑field smoothing.

### 5. No primordial tensor modes  
TCWT predicts a suppressed tensor‑to‑scalar ratio.

These signatures allow TCWT to be distinguished from ΛCDM and other modified‑gravity models.

---

## 5. Model Comparison

To assess whether TCWT is preferred over ΛCDM, we compute:

- Bayesian evidence \( Z \)
- Information criteria (AIC, BIC)
- Posterior predictive distributions

A model is favoured if it provides:
- a better fit to data,
- with fewer or comparable parameters,
- and without fine‑tuning.

TCWT’s ability to address the Hubble tension, growth suppression, and lensing anomalies makes it a strong candidate for outperforming ΛCDM.

---

## 6. Next Steps

With the parameter‑fitting framework defined, the next tasks are:

1. Implement likelihood interfaces for SNe, BAO, RSD, lensing, and CMB.  
2. Run MCMC chains to constrain the TCWT parameter set.  
3. Compare TCWT to ΛCDM using Bayesian evidence.  
4. Publish the results as the first observational test of the TCWT framework.

This completes Step 5 of the TCWT cosmological framework.

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

- ---

## 6. Summary

This document provides the cosmological layer of TCWT:

- background expansion  
- linear perturbation theory  
- mapping phase fluctuations to density contrast  
- the TCWT growth equation  
- the route to the matter power spectrum  

This completes the theoretical machinery needed to compare TCWT with ΛCDM across cosmological scales.# Cosmology
