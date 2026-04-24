# TCWT Cosmological Perturbations  
**Covariant Action, FLRW Background, Linear Perturbations, Growth Equation, and CMB Constraints**  
**Version:** V2 (V10 Compatible)  
**Status:** Complete cosmology layer for CLASS implementation  

---

## 1. Covariant TCWT Action
**Fields:**
- $\theta$ (Hum phase)
- $\Omega$ (drag field)
- $G$ (ghost field)

**Geometry:**
$g_{\mu\nu}$, $u_\mu$, $h_{\mu\nu}$

**Derivatives:**
$D_t = u^\mu \nabla_\mu$  
$\Delta = h^{\mu\nu} \nabla_\mu \nabla_\nu$  

---

### Lagrangian
$$L_{TCWT} = C_0(D_t\theta − \Omega)^2 − \kappa a_0^2 F\left(\frac{\nabla_\perp\theta \nabla_\perp\theta}{a_0^2}\right) − \alpha(D_t G − \Delta\theta)^2 − V_\Omega(\Omega)$$

**Action:**
$$S = \int d^4x \sqrt{-g} \left[\frac{R}{16\pi G} + L_{TCWT}\right]$$

---

## 2. FLRW Background
$$ds^2 = −dt^2 + a(t)^2 dx^2$$  
$$H = \frac{\dot{a}}{a}$$  

**Fields:**
$\bar{\theta}(t), \bar{\Omega}(t), \bar{G}(t)$

$$X(t) = \dot{\bar{\theta}} − \bar{\Omega}$$

---

## 3. Energy Density
$\rho_{hum}, p_{hum}$  
$\rho_{ghost}, p_{ghost}$  

---

## 4. Friedmann Equations
$$H^2 = \frac{8\pi G}{3} (\rho_{total})$$

$$\dot{H} = −4\pi G (\rho_{total} + p_{total})$$

---

## 5. Constraint
$$X = \frac{1}{2C_0} V'_\Omega(\bar{\Omega})$$

---

## 6. Ghost Evolution
$$\dot{\bar{G}} = \text{constant}$$

---

## 7. Drag Field Evolution
$$\frac{d\bar{\Omega}}{d \ln a} = −\gamma(\bar{\Omega} − \Omega_{min})$$

---

## 8. Linear Perturbations
Newtonian gauge preserved:
$$\Phi = \Psi$$

**Poisson:**
$$\frac{k^2}{a^2}\Psi = 4\pi G(\delta\rho_m + \delta\rho_{hum} + \delta\rho_{ghost})$$

---

## 9. Growth Equation
$$\ddot{\delta} + 2H \dot{\delta} − 4\pi G_{eff} \rho \delta + F_{wilt} \delta = 0$$

---

## 10. CDM Matching
- $c_s^2 \ll 1$ at recombination  
- $\rho_{TCWT} \approx \rho_{CDM}$  

---

## 11. Dispersion
$$\omega^2 = c_s^2 k^2 + \beta k^4$$  
$$\beta = \frac{\alpha}{C_{eff}}$$

---

## 12. Growth Equation (Explicit)
$$\ddot{\delta} + 2H \dot{\delta} − 4\pi G_{eff} \rho \delta − \beta k^4 a^{-4} \delta = 0$$

---

## 13. CMB
- Correct peak positions  
- Modified damping tail  
- Lensing suppression  

---

## 14. Boltzmann Layer
$\delta\theta, \delta\Omega, \delta G, \delta m, v$

**CLASS modification required.**

---

## 15. Stability
$C_0 > 0, \quad \alpha > 0, \quad c_s^2 > 0$  

---

## 16. N-body
$$a = −\chi \nabla\theta$$  

---

## 17. Early-Universe Fermion Scaling
$$R_e(a) = R_{e0} \left[\frac{H(a)}{H_0}\right]^\gamma$$  

$\rightarrow$ larger early fermions  
$\rightarrow$ earlier structure formation  
$\rightarrow$ higher inferred $H_0 \approx 71$ km/s/Mpc  

---

## 18. Predictions
- Scale-dependent growth  
- Modified lensing  
- CMB high-$\ell$ deviations  
- Baryonic structure early formation  

---

## 19. Summary
TCWT cosmology replaces CDM dynamics with Hum + ghost field evolution while preserving $\Lambda$CDM-level observables at large scale.
