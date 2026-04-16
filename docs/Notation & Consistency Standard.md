# TCWT — Notation & Consistency Standard (v1.0)

## 1. MOND Interpolation Function μ(x)

**Canonical definition:**  
`μ(x) = 1 + sqrt(x)`

Where:
- `x = a / a0` (acceleration form)  
- `x = g / a0` (gravitational form)

Used consistently in:
- [MOND limit](ca://s?q=Refine_MOND_limit)
- [Lagrangian](ca://s?q=Refine_TCWT_Lagrangian)
- [Cosmology](ca://s?q=Refine_TCWT_Cosmology)
- [Ghost sector](ca://s?q=Refine_Ghost_Sector)

---

## 2. χ Calibration (MOND Constant)

**Canonical value:**  
`χ ≈ 1.30 × 10^17 m²/s²`

**Calibration parameters:**  
- `κ = 1.455`  
- `Ω_max = 16.91`  
- `C0 = 0.0594`

**Cross‑reference relations:**  
`α ≈ κ² / (2 a0² C0)`  
`ℓ_P² ∼ α / κ`

Referenced in:
- [Unification relations](ca://s?q=Unification_Relations)
- [Orbital mechanics calibration](ca://s?q=Orbital_Mechanics_Calibration)

---

## 3. Mass‑Lock Scaling

**Canonical scaling:**  
`m_e(a) = m0 · (H0 / H(a))²`

Where:
- `m0` fixed by α(R) → Ω‑cap  
- `H(a)` is the Hubble parameter  
- `H0` is the present value  

Referenced in:
- [Fermions](ca://s?q=Refine_TCWT_Fermions)
- [Cosmology](ca://s?q=Refine_TCWT_Cosmology)
- [Master Summary](ca://s?q=Update_Master_Summary)

---

## 4. Ghost Leakage Scaling

**Canonical relation:**  
`Leakage rate ∝ α · Q² / R⁴`

Where:
- `Q` = Hopfion charge  
- `R` = coherence radius  
- `α` = stiffness parameter  

Referenced in:
- [Ghost sector](ca://s?q=Refine_Ghost_Sector)
- [Fermion stability](ca://s?q=Fermion_Stability)
- [Cosmological damping](ca://s?q=Cosmological_Damping)

---

## 5. Units & Normalization Table

| Quantity | Meaning | Units | Typical Value |
|---------|---------|--------|----------------|
| `Ω_hum` | Hum oscillation frequency | s⁻¹ | ~1e‑18 |
| `θ0(t)` | Background phase | dimensionless | normalized to 1 at a=1 |
| `α` | Coherence stiffness | m²/s² | ~1e17 |
| `χ` | MOND constant | m²/s² | 1.30e17 |
| `C0` | Hum coupling constant | dimensionless | 0.0594 |
| `κ` | Coherence curvature | dimensionless | 1.455 |
| `Ω_max` | Maximum Hum frequency | dimensionless | 16.91 |

---

## 6. Cross‑Document Requirements

Every TCWT document must reference:
- canonical `μ(x)`  
- canonical χ derivation  
- mass‑lock scaling  
- ghost leakage scaling  
- the units table  

---



Referenced via:
- [Prepare_v3](ca://s?q=Prepare_v3)
- [Zenodo_v3_Structure](ca://s?q=Zenodo_v3_Structure)
