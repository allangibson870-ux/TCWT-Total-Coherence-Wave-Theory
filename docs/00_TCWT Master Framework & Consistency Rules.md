# TCWT Master Framework — Version V7
**RG Layer + Critical Fixes**  
**Status: Living Reference Document**  
_All other TCWT documents must reference this file._

---

# 1. Core Philosophy

TCWT is a **4‑layer effective field theory (EFT)** in which higher layers are strict coarse‑grained limits of lower layers.  
No feedback from macroscopic gravity or measurement is allowed into the fundamental microdynamics.  
This protects the topological stability of matter knots (Hopfions).

**Critical Consistency Rule:**  
Higher layers cannot feed back into Layer 0.  
Regimes where layers might mix (singularities, extreme curvature) are regulated by the **Ω‑cap** and **global Hum coherence**.

---

# 2. Notation & Consistency Standards

## 2.1 MOND Interpolation Function

μ(x) = 1 + √x

Limits:  
- Newtonian (x ≫ 1): μ → 1  
- Deep MOND (x ≪ 1): μ ≈ √x → a ≈ √(a₀ g_N)

---

## 2.2 χ Calibration (MOND Constant)

χ = c² κ / (C₀ Ω_max)

Example calibration:  
κ = 1.455, Ω_max = 16.91, C₀ = 0.0594 → χ ≈ 1.30 × 10¹⁷ m²/s².

Cross‑relations:

α ≈ (κ² χ) / (2 a₀²)  
ℓ_P² ∼ α / κ

---

## 2.3 Mass‑Lock Scaling

m_e(a) = m₀ · (H₀ / H(a))^γ

γ ≪ 2 due to screening.  
Must satisfy Δm/m ≲ 10⁻¹⁶ → requires suppression mechanism.

---

## 2.4 Ghost Leakage Scaling

Leakage ∝ α · Q² / R⁴

---

## 2.5 Units & Normalization Table

| Quantity | Meaning | Units | Typical Value |
|---------|---------|--------|---------------|
| Ω_hum | Hum oscillation frequency | s⁻¹ | ~1e‑18 |
| θ₀(t) | Background phase | dimensionless | 1.0 |
| α | Coherence stiffness (Layer‑0) | m²/s² | ~1e17 |
| χ | MOND constant | m²/s² | 1.30e17 |
| C₀ | Hum coupling | dimensionless | 0.0594 |
| κ | Coherence curvature | dimensionless | 1.455 |
| Ω_max | Max Hum frequency | dimensionless | 16.91 |

### Clarification (V6 IR Parameterization)

α₀ is the **dimensionless IR‑renormalized stiffness** entering the smoothed G_eff and growth equation.  
Physical α remains ~10¹⁷ m²/s² and is recovered via χ, a₀, κ, Ω_max normalization.  
**V6 fit: α₀ = 0.0502.**

---

# 3. The 4‑Layer EFT Stack

**Layer 0 — Fundamental Microdynamics**  
Fields: θ, Ω, G (Planck/UV scale)

**Layer 1 — Topological Sector**  
Hopfion knots, chiral zero‑modes

**Layer 2 — Linear Fluctuation Sector**  
Small perturbations δθ

**Layer 3 — Coarse‑Grained Gravity**  
g_μν = η_μν + β ∂_μθ ∂_νθ

**Layer 4 — Emergent Effective Physics**  
MOND, galaxies, stellar spectra, cosmology

---

# 4. Current Core Equations

## 4.1 Master Lagrangian (Layer 0)

L = C₀(∂ₜθ − Ω)²  
  − κ a₀² F(|∇θ|² / a₀²)  
  − α(∂ₜG − ∇²θ)²  
  − V_Ω(Ω)

F(x) = x + (2/3)x^(3/2)  
μ(x) = 1 + √x

---

## 4.2 Effective Dirac Operator on Hopfion Ring (Layer 1)

i ∂ₜ ψ = [−i v ∂ₛ σ¹ + m_eff σ³ + A σ²] ψ  
v = √(κ / C₀)  
m_eff ∝ α ∇² θ_Hopf

---

## 4.3 Exact and Smoothed G_eff (Layer 3)

Exact:

G_eff = G [1 + κ μ(k)/(4πGρ_m a² C₀) + α k⁴/(4πGρ_m a⁴ C₀)]⁻¹

### Updated V6 Smoothed Form

G_eff(k,a) = G / [1 + (k/k_g)^(2p)]

with:  
- p = **1.602**  
- k_g = k★ = **0.498 h/Mpc**

---

## 4.4 Modified Growth Equation

δ̈ + 2H δ̇ − 4π G_eff ρ_m δ − β (k⁴/a⁴) δ = 0  
β = α / C₀ (IR‑renormalized → β ≈ **3.48**)

---

## 4.5 Evaporation Cutoff for Generations

τ(Q) ∝ R⁴ / (α Q² Γ_leak)  
Q ≥ 4 → rapid evaporation → **three stable generations**

---

## 4.6 Neutrino Sector (Updated V6)

m_ν(a) ≈ m_ν₀ (H₀/H(a))^β  
**V6 fit: β = 3.48**  
Ghost leakage induces weak density‑dependent self‑interactions.

---

# 5. Renormalization Group Flow (RG‑TCWT)

Scale: k ∼ 1/λ

dg_i / d ln k = β_i(g_j)

Key running couplings:

- da₀/d ln k = η_a a₀  
- dα/d ln k = −γ_α α + δ_α χ²  
- dκ/d ln k = β_κ κ (1 − κ/κ_*)  
- χ(k) = c² κ(k) / (C₀(k) Ω_max(k))

### RG Consistency Condition

d/d ln k (α / κ²) ≤ 0

### Fixed Points

- UV: κ → 0, α → 0  
- Galactic: κ → κ_*  
- IR: α → α_* → dark‑energy‑like behaviour

---

# 6. V6 Best‑Fit Cosmological Parameter Set

From full‑stack MCMC + Fisher analysis:

| Parameter | Value | Notes |
|----------|--------|-------|
| α₀ | **0.0502** | IR stiffness (scaled) |
| k★ | **0.498 h/Mpc** | MOND/RG transition scale |
| p | **1.602** | Smoothing exponent |
| β | **3.48** | Neutrino mass‑running |
| H₀ | **71.4 km/s/Mpc** | Hubble tension resolved |
| S₈ | **0.772** | Growth tension resolved |

These values satisfy:

d/d ln k (α/κ²) ≤ 0

and ensure GR‑compliance at galactic scales while modifying cosmological growth.

---

# 7. Cross‑Document Requirements

All TCWT documents must:

- Reference this Master Framework at the top.  
- Use canonical μ(x) = 1 + √x and χ = c² κ / (C₀ Ω_max).  
- Use the updated V6 smoothed G_eff with p = 1.602 and k★ = 0.498 h/Mpc.  
- Use β = 3.48 for neutrino mass‑running.  
- Reference the **V6 Best‑Fit Cosmological Parameter Set** for all astrophysical or cosmological predictions.  
- Point to Section 4 for core equations and Section 5 for RG flow.

**Last updated: April 21, 2026**  
**This document is the single source of truth.**
