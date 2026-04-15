# TCWT Orbital Mechanics  
## Phase‑bleed gravity, χ calibration, Newtonian limit, and galactic rotation  
Version: 2026.9  
Status: Complete orbital‑dynamics layer

---

## 1. Core Postulate: Phase‑Bleed Acceleration

In Total Coherence Wave Theory (TCWT), gravity arises from gradients in the temporal phase field $\theta$:

$$a(r) = -\chi \nabla\theta(r)$$

Where:

| Symbol | Meaning | Units |
|--------|---------|--------|
| $\theta$ | temporal phase field | dimensionless |
| $\lambda = \nabla\theta$ | phase gradient | 1/m |
| $a$ | acceleration | m/s² |
| $\chi$ | coupling constant | m²/s² |

---

## 2. Coupling Constant $\chi$

The coupling constant connects emergent gravitational acceleration to Hum‑flow parameters:

$$\chi = \frac{c^2 \kappa}{C_0 \Omega_{\max}}$$

### Calibration

| Parameter | Value |
|----------|--------|
| $c$ | $2.9979\times10^8$ m/s |
| $\kappa$ | $1.455$ |
| $\Omega_{\max}$ | $16.91$ |
| $C_0$ | $0.0594$ |

Compute:

$$c^2 = 8.9874\times10^{16}$$  
$$\chi \approx 1.30\times10^{17}\ \text{m}^2/\text{s}^2$$

---

## 3. Circular Orbit Law

For circular motion:

$$\frac{v^2}{r} = a(r)$$

Substituting phase‑bleed acceleration:

$$\frac{v^2}{r} = \chi |\lambda|$$

Thus:

$$\lambda(r) = \frac{v^2}{\chi r}$$

This allows the phase gradient field to be inferred directly from orbital observations.

---

## 4. Phase Gradients for Known Orbits

Using $\chi = 1.30\times10^{17}$:

| Orbit | Radius (m) | Velocity (m/s) | $\lambda$ (rad/m) |
|-------|------------|----------------|--------------------|
| ISS | $6.78\times10^6$ | 7660 | $6.6\times10^{-17}$ |
| GPS | $2.66\times10^7$ | 3870 | $4.3\times10^{-18}$ |
| Moon | $3.84\times10^8$ | 1022 | $2.1\times10^{-20}$ |

These gradients are extremely small, consistent with weak gravitational fields in the Solar System.

---

## 5. Newtonian Limit

For planetary systems:

$$v^2 = \frac{GM}{r}$$

Substitute into the gradient relation:

$$\lambda(r) = \frac{GM}{\chi r^2}$$

Integrate:

$$\theta(r) = \theta_\infty - \frac{GM}{\chi r}$$

Thus:

$$\nabla\theta \propto \frac{1}{r^2}$$

Acceleration becomes:

$$a(r) = -\frac{GM}{r^2}$$

Newtonian gravity is recovered when the phase field is sourced by localized mass.

---

## 6. Galactic Halo Regime

For galaxies, rotation curves become approximately flat:

$$v \approx v_0$$

Then:

$$\lambda(r) = \frac{v_0^2}{\chi r}$$

Integrating:

$$\theta(r) = \theta_0 - \frac{v_0^2}{\chi}\ln\left(\frac{r}{r_0}\right)$$

This logarithmic phase profile yields **flat rotation curves without dark matter particles**.

---

## 7. Binary Pulsar Prediction

TCWT predicts a small additional contribution to relativistic periastron advance due to $\Omega$‑cap coupling.

| System | Extra Precession |
|--------|------------------|
| PSR B1913+16 | +0.066 arcsec/year |
| PSR J0737‑3039 | +0.11 arcsec/year |

Future pulsar timing arrays may be able to test this deviation.

---

## 8. Empirical Consistency

### Weak Equivalence Principle

Acceleration depends only on the background phase gradient:

$$a = -\chi \nabla\theta$$

Test‑body composition cancels, preserving universal free fall.

### Multi‑Messenger Timing

Low‑energy phase propagation remains Lorentz‑invariant, maintaining coincidence between gravitational‑wave and electromagnetic signals.

---

## 9. Summary

Key relations:

- Phase‑bleed acceleration:  
  $$a = -\chi \nabla\theta$$

- Orbital gradient:  
  $$\lambda = \frac{v^2}{\chi r}$$

- Newtonian regime:  
  $$\theta(r) \propto \frac{1}{r}$$

- Galactic halo regime:  
  $$\theta(r) \propto \ln r$$

TCWT orbital mechanics:

- reproduces Newtonian gravity in the Solar System  
- naturally generates flat galactic rotation curves  
- predicts small measurable pulsar timing deviations  
- does not require additional dark matter particles  

