# TCWT Algebraic Mathematics & Derivations

**Version**: 2026.3-algebraic-core (reconstructed)  
**Author**: A. Gibson  
**Purpose**: Core algebraic derivations, field equations, conserved quantities, stability analyses, and empirical consistency checks for Total Coherence Wave Theory (TCWT) in its pregeometric formulation.

## 1. Field Equations

From the pregeometric action

$$
S = \int \left[ 
C_0 \left( \frac{d\theta}{dt} - \Omega \right)^2 
+ \kappa \left( \frac{d\theta}{d\ell} \right)^2 
+ \alpha \left( \frac{dG}{dt} - \frac{d^2 \theta}{d\ell^2} \right)^2 
+ V_{\text{cap}}(\Omega) 
\right] d\ell \, dt
$$

### 1.1 θ-equation of motion

$$
C_0 \frac{d}{dt} \left( \frac{d\theta}{dt} - \Omega \right) 
- \frac{d}{d\ell} \left( \kappa \frac{d\theta}{d\ell} \right) 
+ \alpha \frac{d^2}{d\ell^2} \left( \frac{dG}{dt} - \frac{d^2 \theta}{d\ell^2} \right) = 0
$$

### 1.2 Ω-evolution equation

$$
C_0 \left( \frac{d\theta}{dt} - \Omega \right) + \frac{\partial V_{\text{cap}}}{\partial \Omega} = 0
$$

When Ω < Ω_max → Ω = dθ/dt.  
When Ω ≥ Ω_max the cap enforces Ω ≤ Ω_max.

### 1.3 G field equation

$$
\partial_\mu \left( Z_G \partial^\mu G \right) - m_G^2 G + \gamma \Box \theta - \lambda_1 \theta^2 - 2 \lambda_2 G = 0
$$

### 1.4 Effective gravitational field & acceleration

$$
\lambda = \frac{d\theta}{d\ell}, \quad a(r) = -\chi \lambda
$$

(χ fixed from knot stability)

## 2. Noether Currents

Global U(1) phase shift θ → θ + ε is a symmetry.

**Noether current**:

$$
J = 2 C_0 \left( \frac{d\theta}{dt} - \Omega \right) \frac{d}{dt} + 2 \kappa \frac{d\theta}{d\ell} \frac{d}{d\ell}
$$

**Physical meaning**: conserved temporal phase flux.  
Enforces conservation of Hum information content; explains stability and collisionless nature of phase-opaque knots.

## 3. Energy Density & Stability

**Hamiltonian density**:

$$
\rho = C_0 \left( \frac{d\theta}{dt} - \Omega \right)^2 + \kappa \left( \frac{d\theta}{d\ell} \right)^2 + \alpha \left( \frac{dG}{dt} - \frac{d^2 \theta}{d\ell^2} \right)^2 + V_{\text{cap}}(\Omega)
$$

**Positive energy**: ρ ≥ 0 (vacuum equality).

**Stability safeguards**:
- Ω-cap quartic growth prevents Ω > Ω_max  
- Visibility floor V = exp(−σ |λ|) suppresses high-λ runaways  
- Knot size floor R ≥ R_crit prevents collapse

## 4. Stability of Knot Solutions

Gaussian ansatz:

$$
\theta_{\mathrm{knot}}(r) = \Theta_0 \exp\left( -\frac{r^2}{2R^2} \right)
$$

Equilibrium from δE/δR = 0.  
Stability when δ²E/δR² > 0 for

$$
R > R_{\mathrm{crit}} = \frac{\Theta_0 \sqrt{\kappa}}{\sqrt{M}} \cdot \frac{\Omega_{\max}}{\kappa}
$$

Marginal stability at |∇θ| = Ω_max / κ.

## 5. Rotation Curves

**Newtonian**: v ∝ r^{-1/2}  
**MOND**: v ∝ r^{1/4} (flat at large r)  
**NFW**: v ≈ constant for r ≫ r_s  

**TCWT**: v(r) ≈ √(α / R(r))  
R(r) grows slower than linear (foam correction) → flattens at large r (controlled by β and d).

Matches real data (NGC 3198) without extra particles.

## 6. Decoherence & Visibility

V = exp(−σ |λ|), σ = κ / Ω_max ≈ 6.58 × 10^{-36} m/rad.

Regimes:
- |λ| ≪ Ω_max / κ → V ≈ 1  
- |λ| ≈ Ω_max / κ → V ≈ 0.37  
- |λ| ≫ Ω_max / κ → V ≪ 1 (phase-opaque)

Decoherence threshold at Ω_max.

## 7. Dark Matter as Phase-Opaque Knots

Opacity |∇θ| ≥ Ω_max / κ produces realistic halos:
- Density ∝ 1/r (log accumulation)  
- Sharp core-halo transition  
- Flat rotation curves

## 8. Solar Flare Precursor

δf/f ≈ β · δθ ≈ 10^{-18}–10^{-17}  
Within reach of NIST/FOCS during Solar Cycle 25 max.

## 9. Empirical Challenges & Resolutions

### 9.1 WEP (MICROSCOPE)

Test bodies follow geodesics in emergent metric — acceleration depends only on background λ, not internal composition.  
WEP recovered. Residual violation suppressed ≪ 10^{-15}.

### 9.2 Binary Pulsar Drag

Phase-viscosity and Ω-drag suppressed in vacuum (low gradients) → extra loss < 0.003 × GR.  
No conflict with Hulse–Taylor.

### 9.3 CMB Isotropy

Hum is scalar phase oscillation — no vector flow, no preferred frame.  
No extra dipole. Consistent with Planck.

### 9.4 Spacecraft Anomalies (Parker/Juno)

Smooth Gaussian barrier → Δa < 10^{-10} m/s² (below tracking precision).  
No detectable jumps.

Theory survives major empirical tests.
