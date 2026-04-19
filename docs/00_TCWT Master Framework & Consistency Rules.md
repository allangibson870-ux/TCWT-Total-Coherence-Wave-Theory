# TCWT Master Framework & Consistency Rules
**Version:** V1 (Soft-Cap + Layered EFT)  
**Status:** Living reference document — updated as core mathematics evolves

This is the single source of truth for notation, constants, layer structure, and current equations in Total Coherence Wave Theory (TCWT). All other documents must reference this file.

## 1. Core Philosophy

TCWT is a 4-layer effective field theory (EFT) in which higher layers are strict coarse-grained limits of lower layers. No feedback from macroscopic gravity or measurement is allowed into the fundamental microdynamics. This rule protects the topological stability of matter knots.

**Critical Consistency Rule:** Higher layers cannot feed back into Layer 0. Matter knots (Hopfions) remain stable against quantum measurement or macroscopic gravitational fluctuations.

## 2. Notation & Consistency Standard

### 2.1 MOND Interpolation Function
Canonical definition:  
μ(x) = 1 + sqrt(x)  
where x = a / a₀ (acceleration form) or x = g / a₀ (gravitational form).

### 2.2 χ Calibration (MOND Constant)
Canonical value: χ ≈ 1.30 × 10¹⁷ m²/s²  
Calibration parameters: κ = 1.455, Ω_max = 16.91, C₀ = 0.0594  

Cross-reference relations:  
α ≈ κ² / (2 a₀² C₀)  
ℓ_P² ∼ α / κ

### 2.3 Mass-Lock Scaling
Canonical scaling:  
m_e(a) = m₀ · (H₀ / H(a))²  
where m₀ is fixed by α(R) → Ω-cap.

### 2.4 Ghost Leakage Scaling
Canonical relation:  
Leakage rate ∝ α · Q² / R⁴  
where Q = Hopfion charge, R = coherence radius.

### 2.5 Units & Normalization Table

| Quantity   | Meaning                        | Units       | Typical Value |
|------------|--------------------------------|-------------|---------------|
| Ω_hum      | Hum oscillation frequency      | s⁻¹         | ~1e-18        |
| θ₀(t)      | Background phase               | dimensionless | normalized to 1 at a=1 |
| α          | Coherence stiffness            | m²/s²       | ~1e17         |
| χ          | MOND constant                  | m²/s²       | 1.30e17       |
| C₀         | Hum coupling constant          | dimensionless | 0.0594      |
| κ          | Coherence curvature            | dimensionless | 1.455       |
| Ω_max      | Maximum Hum frequency          | dimensionless | 16.91       |

## 3. 4-Layer EFT Stack

**Layer 0: Fundamental Microdynamics (Pregeometric)**  
Domain: Planck scale / UV / strong curvature.  
Fields: θ(x,t), Ω(x,t), G(x,t).  
Action: S₀ = ∫ d⁴x √(-g) [C₀(∇_μθ − u_μΩ)² − κ|∇θ|² − α(G − □θ)² − V_Ω(Ω)]  
(with Soft-Cap V_Ω in v2026.9.1)

**Layer 1: Topological / Soliton Sector**  
Domain: Intermediate / nonlinear regime.  
Objects: Hopfion knots (π₃ topology) with chiral zero-modes.  
Emergent physics: Matter as stable topological defects.

**Layer 2: Linear Fluctuation / Quantum Limit**  
Domain: Small perturbations δθ.  
Action: S₂ = ∫ d⁴x [C₀(∂_t δθ)² − κ(∇ δθ)² − α(∇² δθ)²]  
Commutator: [δθ(x), π(y)] = i δ³(x−y)

**Layer 3: Coarse-Grained Gravity & Cosmology**  
Domain: Macroscopic / long-wavelength.  
Emergent metric: g_μν = η_μν + β ∂_μθ ∂_νθ  
Einstein limit: G_μν = 8π G_eff T_μν with G_eff ∼ 1/κ  
Dispersion: ω² = c_s² k² + β k⁴

**Layer 4: Emergent Effective Physics**  
Domain: Astrophysical and laboratory scales.  
Phenomena: Newtonian gravity, MOND, galaxy dynamics, atomic physics, chemistry, stellar spectra.

## 4. Current Core Equations (Living Section)

### 4.1 Master Lagrangian (Layer 0)
L = C₀(∂_t θ − Ω)² − κ a₀² F(|∇θ|² / a₀
²) − α(∂_t G − ∇² θ)² − V_Ω(Ω)  
with F(x) = x + (2/3) x^{3/2}, μ(x) = 1 + sqrt(x)

### 4.2 Effective Dirac Operator on Hopfion Ring (Layer 1)
i ∂_t ψ(s) = [−i v ∂_s σ¹ + m_eff(s) σ³ + A(s) σ²] ψ(s)  
where v = sqrt(κ / C₀), m_eff(s) ∝ α ∇² θ_Hopf, and A(s) is the Berry connection from the Hopfion twist.

### 4.3 Modified Gravity & Growth Equations (Layer 3)
Modified Poisson:  
k² Ψ = −4π G_eff(k,a) a² ρ_m δ_m  

with  
G_eff(k,a) = G / [1 + (k / k_g)^{2p}]   (p ≈ 1.6 recommended)

Modified growth:  
δ̈ + 2H δ̇ − 4π G_eff(k,a) ρ_m δ − β (k⁴ / a⁴) δ = 0  
where β = α / C₀

### 4.4 Evaporation Cutoff for Generations
Lifetime: τ(Q) ∝ R⁴ / (α Q² Γ_leak)  
For Q ≥ 4 the leakage becomes rapid → topological evaporation. This explains the observed three light generations.

### 4.5 Neutrino Sector
Neutrinos occupy shallower mass wells → stronger redshift dependence:  
m_ν(a) ≈ m_ν₀ (H₀ / H(a))^β   (β ≳ 3)  

Ghost leakage from overlapping wells generates weak, density-dependent self-interactions. The same mechanism that allows self-interactions causes rapid evaporation for any Q ≥ 4 states.

## 5. Cross-Document Requirements

Every TCWT document must:
- Reference this Master Framework at the top.
- Use canonical μ(x), χ, Mass-Lock scaling, and ghost leakage scaling.
- Point to the Living Equations section for current mathematical content.

**Last updated:** April 2026  
This document is the single source of truth. When mathematics change, update only here and propagate references.

---

