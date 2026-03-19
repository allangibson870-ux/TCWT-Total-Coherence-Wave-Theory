# TCWT Cosmological Perturbations

This document introduces the cosmological perturbation framework for the Total Coherence Wave Theory (TCWT). It extends the TCWT Lagrangian into the cosmological regime, deriving the background expansion, linear perturbations, and the structure‑growth equation that replaces the ΛCDM growth model.

---

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

## 5. Summary

This document provides the cosmological layer of TCWT:

- background expansion  
- linear perturbation theory  
- mapping phase fluctuations to density contrast  
- the TCWT growth equation  
- the route to the matter power spectrum  

This completes the theoretical machinery needed to compare TCWT with ΛCDM across cosmological scales.# Cosmology
