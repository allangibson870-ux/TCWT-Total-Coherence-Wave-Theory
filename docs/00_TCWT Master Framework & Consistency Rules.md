# TCWT Master Framework & Consistency Rules
**Version:** V6 (RG Layer Added)  
**Status:** Living reference document — single source of truth

All other TCWT documents must reference this file for notation, constants, layer structure, and current equations.

## 1. Core Philosophy

TCWT is a 4-layer effective field theory (EFT) in which higher layers are strict coarse-grained limits of lower layers. No feedback from macroscopic gravity or measurement is allowed into the fundamental microdynamics. This protects the topological stability of matter knots (Hopfions).

**Critical Consistency Rule:** Higher layers cannot feed back into Layer 0.

## 2. Notation & Consistency Standard

### 2.1 MOND Interpolation Function
Canonical definition:  
μ(x) = 1 + √x  
where x = a / a₀ (acceleration form) or x = g / a₀ (gravitational form).

### 2.2 χ Calibration (MOND Constant)
From the action, the coupling constant is defined as:  
χ = c² κ / (C₀ Ω_max)

**Practical calibration example:**  
Using κ = 1.455, Ω_max = 16.91, C₀ = 0.0594 (with unit restoration) yields χ ≈ 1.30 × 10¹⁷ m
²/s², consistent with galactic acceleration scales.

Cross-reference relations:  
α ≈ (κ ² χ) / (2 a₀²)  
ℓ_P² ∼ α / κ

### 2.3 Mass-Lock Scaling
Canonical scaling:  
m_e(a) = m₀ · (H₀ / H(a))^γ  

where γ is expected to be ≪ 2 due to screening or weak coupling at late times. This scaling must satisfy precision constraints (Δm/m ≲ 10^{-16} from Oklo, quasar spectra, etc.). A suppression or screening mechanism is required for observational consistency.

### 2.4 Ghost Leakage Scaling
Canonical relation:  
Leakage rate ∝ α · Q² / R⁴  
where Q = Hopfion charge, R = coherence radius.

### 2.5 Units & Normalization Table

| Quantity   | Meaning                        | Units       | Typical Value |
|------------|--------------------------------|-------------|---------------|
| Ω_hum      | Hum oscillation frequency      | s⁻¹         | ~1e-18        |
| θ₀(t)      | Background phase               | dimensionless | 1.0 (at a=1) |
| α          | Coherence stiffness            | m²/s²       | ~1e17         |
| χ          | MOND constant                  | m²/s²       | 1.30e17 (calibrated) |
| C₀         | Hum coupling constant          | dimensionless | 0.0594      |
| κ          | Coherence curvature            | dimensionless | 1.455       |
| Ω_max      | Maximum Hum frequency          | dimensionless | 16.91       |

## 3. 4-Layer EFT Stack

- **Layer 0:** Fundamental Microdynamics (Planck scale / UV) — Fields: θ, Ω, G.
- **Layer 1:** Topological Sector (Intermediate) — Hopfion knots with chiral zero-modes.
- **Layer 2:** Linear Fluctuation (Quantum Limit) — Small perturbations δθ.
- **Layer 3:** Coarse-Grained Gravity (Macroscopic) — Emergent metric g_μν = η_μν + β ∂_μθ ∂_νθ.
- **Layer 4:** Emergent Effective Physics (Astrophysical) — MOND, galaxies, stellar spectra.

## 4. Current Core Equations (Living Section)

### 4.1 Master Lagrangian (Layer 0)
L = C₀(∂_t θ − Ω) ² − κ a₀² F(|∇θ|² / a₀²) − α(∂_t G − ∇² θ)² − V_Ω(Ω)  
with F(x) = x + (2/3) x^{3/2}, μ(x) = 1 + √x

### 4.2 Effective Dirac Operator on Hopfion Ring (Layer 1)
i ∂_t ψ(s) = [−i v ∂_s σ¹ + m_eff(s) σ³ + A(s) σ²] ψ(s)  
where v = √(κ / C₀), m_eff(s) ∝ α ∇² θ_Hopf.

### 4.3 Exact Derivation of G_eff(a,k) from the Full Action (Layer 3)
In Newtonian gauge and the quasi-static sub-horizon limit (k ≫ aH), integrating out auxiliary fields Ω and G yields:

G_eff(k,a) = G [ 1 + κ μ(k) / (4π G ρ_m a² C₀) + α k⁴ / (4π G ρ_m a⁴ C₀) ]^{-1}

In practice for cosmological codes we use the smoothed phenomenological form (p ≈ 1.6):

G_eff(k,a) = G / [1 + (k / k_g)^{2p}]

### 4.4 Modified Growth Equation
δ̈ + 2H δ̇ − 4π G_eff(k,a) ρ_m δ − β (k⁴ / a⁴) δ = 0  
where β = α / C₀

### 4.5 Evaporation Cutoff for Generations
Lifetime: τ(Q) ∝ R⁴ / (α Q² Γ_leak)  
For Q ≥ 4 the leakage becomes rapid → topological evaporation. This limits stable matter to three generations.

### 4.6 Neutrino Sector (Summary)
Neutrinos occupy shallower mass wells → stronger redshift dependence m_ν(a) ≈ m_ν₀ (H₀ / H(a))^β (β ≳ 3). Ghost leakage from overlapping wells can generate weak, density-dependent self-interactions.

## 5. Renormalization Group Flow Layer (RG-TCWT)

**Add-on layer above the Master Framework**

TCWT parameters are scale-dependent couplings over resolution scale λ (or momentum k), with λ ∼ physical resolution scale, k ∼ 1/λ.

We define RG flow:  
dg_i / d ln k = β_i(g_j)

where g_i ∈ {κ, C₀, α, χ, a₀, Ω_max}

### 5.1 Physical Interpretation of RG Scale
- High k (UV): particle physics / Hopfion core
- Mid k: galactic dynamics
- Low k (IR): cosmology / Hum background

### 5.2 Running Couplings (Key Examples)
- MOND scale: da₀ / d ln k = η_a a₀ → a₀(k) = a₀^IR (k / k₀)^η_a  
  (high k → MOND disappears; low k → MOND emerges)

- Ghost coupling: dα / d ln k = −γ_α α + δ_α χ²  
  (UV: α small → stable QFT; IR: α grows → k⁴ suppression)

- Coherence stiffness: dκ / d ln k = β_κ κ (1 − κ/κ_*)  
  (UV: κ → 0 → quantum limit; IR: κ → κ_* → classical gravity)

### 5.3 Emergent χ as Running Quantity
χ(k) = c² κ(k) / (C₀(k) Ω_max(k))

Result: χ is IR-enhanced → MOND regime emerges naturally at galactic scales.

### 5.4 Modified Dispersion Relation (RG-corrected)
ω²(k) = c_s²(k) k² + β(k) k⁴  
with c_s²(k) = κ(k)/C₀(k), β(k) = α(k)/C₀(k)

### 5.5 RG Consistency Condition
d/d ln k (α / κ²) ≤ 0  
This prevents UV ghost explosion and ensures stable MOND transition.

## 6. Caveats & Future Work

- Mass-Lock scaling requires a suppression/screening mechanism to satisfy tight observational bounds (Δm/m ≲ 10^{-16}).
- Fermion sector (gauge fields, quantitative masses, multi-Hopfion solutions) is under development.
- RG flow is a consistent organizing layer but requires explicit β-functions from the full action for rigor.

## 7. Cross-Document Requirements

Every TCWT document must:
- Reference this Master Framework at the top.
- Use canonical μ(x) = 1 + √x and derived χ = c ² κ / (C₀ Ω_max).
- Point to the Living Equations section (Section 4) and RG Layer (Section 5) for current mathematical content.

**Last updated:** April 20, 2026  
This document is the single source of truth. When mathematics change, update only here.

---

