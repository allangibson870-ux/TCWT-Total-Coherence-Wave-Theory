## 1. Emergent Quantum Field Mechanics (QFM) in TCWT

### 1.1 Goal
We extend TCWT beyond classical field dynamics and show how quantum field behaviour emerges from the coherence properties of the Hum phase field.

The objective is to reproduce:

- discrete particle states  
- wave–particle duality  
- interference phenomena  
- vacuum fluctuations  

without introducing fundamental probabilistic axioms.

---

### 1.2 Core Principle: Phase-Coherence Quantization

In TCWT, quantization does not arise from operator postulates but from **global phase-coherence constraints**.

Allowed field configurations must satisfy:

∮ ∇θ · dl = 2π n

where:

- n ∈ ℤ  
- the integral is taken over closed loops in configuration space  

This enforces **topological phase quantization**, analogous to:

- superfluid circulation  
- magnetic flux quantization  

---

### 1.3 Particles as Quantized Solitons

Matter corresponds to stable phase knots:

θ_knot(r) = Θ₀ exp(−r² / 2R²)

Quantization arises because:

- only specific phase-winding numbers are stable  
- energy is minimized at discrete configurations  

Thus:

E_n ∝ n²

This produces **discrete particle-like states without operators**.

---

### 1.4 Emergent Wavefunction

Define an effective complex field:

ψ(x,t) ≡ exp(i θ(x,t))

Then:

- |ψ|² encodes phase coherence density  
- interference patterns arise from θ superposition  

The Schrödinger-like equation emerges in the weak-field limit:

i ∂_t ψ = −(c² / 2Ω_hum) ∇² ψ + nonlinear terms

---

### 1.5 Interference Without Probability Postulates

From Section 8:

Detection events correspond to **knot nucleation**, not wavefunction collapse.

Probability emerges as:

P(x) ∝ f(|∇θ|, ∇²θ)

Thus:

- high phase curvature → high detection likelihood  
- destructive interference → suppressed knot formation  

This reproduces quantum interference patterns deterministically.

---

### 1.6 Vacuum Fluctuations

The Hum vacuum is not static:

θ₀(t) = Ω_hum t

Small perturbations:

δθ(x,t)

generate:

- zero-point fluctuations  
- stochastic phase noise  

These act as the TCWT analogue of:

quantum vacuum fluctuations.

---

### 1.7 Effective Field Quantization

Linear perturbations satisfy:

□ δθ = 0

Mode expansion:

δθ(x,t) = ∫ d³k [A_k e^{ikx} + A_k* e^{-ikx}]

In TCWT:

- A_k are classical amplitudes  
- statistical ensembles of phase configurations reproduce quantum statistics  

Thus QFT emerges as a **coarse-grained statistical description of the Hum field**.

---

### 1.8 Interactions

Interactions arise from nonlinear terms in the Lagrangian:

- κ F(|∇θ|²) → self-interaction  
- α (Ġ − ∇²θ)² → dissipative coupling  
- V_Ω(Ω) → saturation effects  

These replace:

- gauge interactions  
- potential terms  

in conventional QFT.

---

### 1.9 Correspondence with Standard Quantum Theory

| Quantum Concept | TCWT Interpretation |
|------|------|
| Wavefunction ψ | exp(iθ) |
| Particle | phase soliton |
| Quantization | phase winding constraint |
| Vacuum fluctuations | δθ fluctuations |
| Measurement | knot formation |
| Probability | curvature-dependent nucleation |

---

### 1.10 Key Result

Quantum behaviour in TCWT is not fundamental.

It emerges from:

- phase coherence  
- nonlinear field dynamics  
- topological constraints  

Thus:

TCWT provides a **deterministic underlying theory** whose coarse-grained limit reproduces quantum field mechanics.

---

### 1.11 Open Problems

To fully match quantum field theory, TCWT must still derive:

- spin and fermionic statistics  
- gauge symmetry structure  
- renormalization behaviour  
- scattering amplitudes  

These define the next stage of development.

---
## 2. Quantum Field Emergence from TCWT

### 2.1 Goal

We derive the emergence of quantum field theory from the TCWT phase field by:

- identifying canonical variables
- constructing the Hamiltonian
- imposing quantisation
- deriving mode expansions and dispersion relations

This demonstrates that quantum behaviour arises as the **linear coherence limit** of the Hum field.

---

### 2.2 Quadratic Effective Lagrangian

Starting from the TCWT Lagrangian, in the weak-field, low-energy regime:

- MOND nonlinearity negligible
- ghost backreaction subleading
- Ω relaxes to equilibrium

Using:

Ω ≈ ∂ₜθ

the Lagrangian reduces to:

L_eff = C₀ (∂ₜθ)² − κ (∇θ)²

This is the leading-order coherent phase dynamics.

---

### 2.3 Canonical Momentum

The conjugate momentum is:

π(x,t) = ∂L_eff / ∂(∂ₜθ) = 2C₀ ∂ₜθ

---

### 2.4 Hamiltonian Density

The Hamiltonian density:

H = π ∂ₜθ − L_eff

gives:

H = π² / (4C₀) + κ (∇θ)²

This is a positive-definite energy density.

---

### 2.5 Canonical Quantisation

We impose equal-time commutation relations:

[ θ(x), π(y) ] = i ℏ_eff δ³(x − y)

[ θ(x), θ(y) ] = 0  
[ π(x), π(y) ] = 0  

where ℏ_eff is an emergent coherence scale.

---

### 2.6 Field Normalisation

Define a canonically normalised field:

φ ≡ √(2C₀) θ

Then:

π_φ = ∂ₜφ

and the Lagrangian becomes:

L_eff = ½ (∂ₜφ)² − ½ c² (∇φ)²

with:

c² = κ / C₀

This is the standard relativistic scalar field form.

---

### 2.7 Mode Expansion

The field φ admits a plane-wave expansion:

φ(x,t) = ∫ d³k / (2π)³ (1 / √(2ω_k))
         [ a_k e^{i(k·x − ω_k t)} + a_k† e^{-i(k·x − ω_k t)} ]

with dispersion relation:

ω_k² = c² k²

---

### 2.8 Ladder Operators

Canonical commutation implies:

[ a_k, a_{k'}† ] = (2π)³ δ³(k − k')

These operators create and annihilate **Hum phase quanta**.

---

### 2.9 Interpretation of Quanta

In TCWT:

- linear excitations → propagating phase waves  
- nonlinear stable solutions → soliton knots  

Thus:

| Concept | TCWT Interpretation |
|--------|--------------------|
| quantum | phase excitation |
| particle | stable knot |
| vacuum | coherent Hum state |

---

### 2.10 Ghost-Induced Corrections

Including the ghost sector:

L_ghost = α (∂ₜG − ∇²θ)²

Integrating out G yields a correction:

ΔL ≈ −β (∇²θ)²

with:

β ∼ α / C₀

---

### 2.11 Modified Dispersion Relation

The full quadratic action becomes:

L = C₀ (∂ₜθ)² − κ (∇θ)² − β (∇²θ)²

leading to:

ω² = c² k² + (β / C₀) k⁴

---

### 2.12 Physical Meaning of the k⁴ Term

The higher-order term produces:

- UV regularisation (no divergences)
- finite-energy knot cores
- scale-dependent propagation speed
- suppression of short-wavelength modes

This same structure appears in:

- matter power suppression
- CMB damping tail
- structure formation cutoff

---

### 2.13 Emergence of ℏ

From:

[ θ, π ] = i ℏ_eff δ³

and:

π = 2C₀ ∂ₜθ

we identify:

ℏ_eff ∝ 1 / C₀

Thus:

- large C₀ → classical limit  
- small C₀ → strong quantum fluctuations  

Quantum mechanics is therefore controlled by **Hum coherence stiffness**.

---

### 2.14 Lorentz Symmetry

At leading order:

ω² = c² k²

so the theory is Lorentz invariant with emergent light speed:

c² = κ / C₀

Higher-order k⁴ terms softly break Lorentz symmetry only at high energy.

---

### 2.15 Summary

In TCWT:

- quantum fields emerge from phase dynamics  
- canonical structure follows from coherence  
- particles correspond to nonlinear knots  
- ℏ is an emergent parameter  
- higher-order terms regulate UV behaviour  

This provides a unified origin for:

- quantum mechanics  
- classical fields  
- cosmological structure  
- gravitational dynamics  

from a single phase-coherence field.

---
## 3. Born Rule from Knot Nucleation Statistics

### 3.1 Goal

We derive the Born rule within TCWT by showing that measurement probabilities emerge from the statistics of **knot nucleation** in the Hum phase field.

In this framework:

- there is no wavefunction collapse
- there is no fundamental probability postulate
- probabilities arise from phase-field dynamics

---

### 3.2 Measurement as Knot Formation

In TCWT, a detection event corresponds to the formation of a **localized soliton knot**.

A knot forms when the phase field satisfies a local instability condition:

|∇θ| ≥ λ_c  
and  
|∇²θ| ≥ κ_c  

where λ_c and κ_c are threshold values determined by the nonlinear sector of the Lagrangian.

Thus:

- no detection → smooth phase field  
- detection → localized nonlinear collapse (knot)

---

### 3.3 Phase Decomposition

Consider a general phase configuration:

θ(x,t) = Re[ A(x,t) e^{iS(x,t)} ]

where:

- A(x,t) = amplitude of phase coherence  
- S(x,t) = local phase  

The observable field is real, but this decomposition allows separation of:

- coherence magnitude (A)
- phase structure (S)

---

### 3.4 Local Energy Density

From the quadratic Hamiltonian:

H = π² / (4C₀) + κ (∇θ)²

we identify the dominant contribution near detection as:

E(x) ≈ κ (∇θ)²

Using the decomposition:

∇θ ≈ A ∇S + (∇A) cos(S)

In regions of smooth amplitude variation:

|∇θ|² ≈ A² |∇S|²

---

### 3.5 Knot Nucleation Probability

Assume knot formation probability is proportional to local energy density exceeding threshold:

P_knot(x) ∝ max[0, E(x) − E_c]

For weak perturbations near threshold:

P_knot(x) ∝ E(x)

Thus:

P_knot(x) ∝ κ A² |∇S|²

---

### 3.6 Phase Averaging

Measurements do not resolve the microscopic phase S(x,t). Averaging over rapid phase oscillations:

⟨|∇S|²⟩ ≈ constant

Therefore:

P_knot(x) ∝ A²(x)

---

### 3.7 Born Rule Emergence

Identifying:

ψ(x) ≡ A(x) e^{iS(x)}

we obtain:

|ψ(x)|² = A²(x)

Thus:

\[
\boxed{
P(x) \propto |ψ(x)|^2
}
\]

This is the **Born rule**, derived from:

- phase-gradient energy
- nonlinear knot formation
- coarse-grained phase averaging

---

### 3.8 Normalisation

Total probability is fixed by total knot formation rate:

∫ P(x) d³x = 1

which corresponds to:

∫ |ψ(x)|² d³x = 1

This is not imposed, but arises from conservation of total phase flux (Section 11).

---

### 3.9 Double-Slit Interpretation

In interference experiments:

- phase field forms interference pattern in θ
- amplitude A(x) encodes phase-coherence envelope
- knot probability follows:

P(x) ∝ A²(x)

Thus:

- fringes arise from phase structure
- detection pattern arises from knot statistics
- no wave–particle duality is required

---

### 3.10 Entanglement Interpretation

For two entangled regions:

θ_total = θ₁ + θ₂

The joint phase structure produces correlated gradients:

P(x₁, x₂) ∝ A²(x₁, x₂)

This yields:

- nonlocal correlations from shared phase field
- no superluminal signalling
- Bell correlations limited by phase coherence (Section 18)

---

### 3.11 Role of Ghost Field

The ghost sector modifies the nucleation condition via:

ΔE ≈ α (∂ₜG − ∇²θ)²

This introduces:

- small-scale smoothing
- suppression of high-frequency knots
- effective decoherence at short scales

Thus the ghost field acts as a **coherence regulator**.

---

### 3.12 No Collapse Postulate

In TCWT:

- evolution of θ is deterministic
- measurement corresponds to instability + nonlinear transition
- probabilities reflect unresolved phase microstructure

Thus:

wavefunction collapse → replaced by knot nucleation

---

### 3.13 Classical Limit

For large C₀ (strong coherence):

- ℏ_eff → small
- fluctuations suppressed
- knot nucleation becomes deterministic

Thus classical behaviour emerges smoothly.

---

### 3.14 Summary

The Born rule emerges naturally in TCWT:

- probability ∝ phase-gradient energy
- energy ∝ A²
- therefore P ∝ |ψ|²

No additional postulates are required.

Quantum mechanics is recovered as the **statistical description of phase-field instabilities** in the Hum.

---
## 4. Path Integral Formulation of TCWT

### 4.1 Goal

We show that the standard quantum path integral emerges naturally from the dynamics of the TCWT phase field.

This provides:

- a bridge to conventional quantum field theory
- a derivation of interference from phase dynamics
- a unification of classical action and quantum amplitudes

---

### 4.2 Starting Point: TCWT Action

The fundamental action is:

S[θ, Ω, G] = ∫ d⁴x  
[ C₀(∂ₜθ − Ω)² − κ(∇θ)² − α(∂ₜG − ∇²θ)² − V_Ω(Ω) ]

In the low-energy limit:

Ω ≈ ∂ₜθ  
ghost backreaction small  

giving:

S_eff[θ] = ∫ d⁴x [ C₀(∂ₜθ)² − κ(∇θ)² − β(∇²θ)² ]

---

### 4.3 Classical Trajectories

The classical evolution follows from:

δS_eff = 0

which yields the phase-field equation:

∂ₜ²θ − c² ∇²θ + (β / C₀) ∇⁴θ = 0

with:

c² = κ / C₀

---

### 4.4 Sum Over Phase Configurations

In TCWT, the system does not follow a single trajectory.

Instead, all phase configurations contribute, weighted by their action:

\[
\boxed{
\mathcal{Z} = \int \mathcal{D}\theta \; e^{i S_{\rm eff}[\theta] / \hbar_{\rm eff}}
}
\]

This is the **partition function**, identical in structure to the quantum path integral.

---

### 4.5 Emergence of the Wavefunction

Define a transition amplitude between configurations:

\[
\Psi[\theta_f, t_f] = \int_{\theta_i}^{\theta_f} \mathcal{D}\theta \; e^{i S_{\rm eff}[\theta] / \hbar_{\rm eff}}
\]

Thus:

- the wavefunction is not fundamental  
- it emerges as a sum over phase histories  

---

### 4.6 Stationary Phase Limit

In the limit:

ℏ_eff → 0

the integral is dominated by stationary paths:

δS_eff = 0

Thus:

- classical physics emerges from phase coherence  
- quantum fluctuations arise from deviations around stationary paths  

---

### 4.7 Interference from Phase Action

For two competing configurations θ₁ and θ₂:

\[
\mathcal{A} = e^{i S[\theta_1]/\hbar_{\rm eff}} + e^{i S[\theta_2]/\hbar_{\rm eff}}
\]

Probability:

\[
P = |\mathcal{A}|^2
\]

This produces interference terms:

\[
P \sim 1 + \cos\left(\frac{S[\theta_1] - S[\theta_2]}{\hbar_{\rm eff}}\right)
\]

Thus:

interference arises from differences in **phase action**, not wavefunction superposition.

---

### 4.8 Connection to Double-Slit

In the double-slit setup:

- each path corresponds to a different phase configuration
- action difference:

ΔS ≈ p Δℓ

Thus:

\[
P(x) \propto \cos^2\left(\frac{ΔS}{2\hbar_{\rm eff}}\right)
\]

which reproduces standard interference fringes.

---

### 4.9 Role of Knot Formation

The path integral gives amplitudes, but observations correspond to knot formation.

Thus:

- path integral → amplitude distribution  
- knot nucleation → actual detection  

Combining:

P_detection(x) ∝ |Ψ(x)|²

recovering the Born rule derived in Section 23.

---

### 4.10 Ghost Sector Contribution

Including the ghost term:

S_ghost ≈ − ∫ d⁴x β (∇²θ)²

This modifies the weight:

\[
e^{iS/\hbar} \rightarrow e^{iS/\hbar} \times e^{- \beta k^4 / \hbar}
\]

Thus:

- high-k paths are suppressed  
- UV divergences are regulated  
- path integral becomes naturally finite  

---

### 4.11 Effective Action and Renormalisation

Integrating out small-scale fluctuations yields an effective action:

S_eff → S_eff + ΔS

with corrections:

- renormalised C₀ and κ  
- scale-dependent β  
- induced interaction terms  

Thus TCWT naturally supports a **renormalisation flow**.

---

### 4.12 Interpretation

In TCWT:

| Concept | Interpretation |
|--------|--------------|
| path integral | sum over phase configurations |
| action S | phase-coherence cost |
| ℏ | coherence scale |
| interference | action-phase difference |
| measurement | knot nucleation |

Quantum mechanics is therefore:

> the statistical mechanics of phase-field configurations.

---

### 4.13 No Fundamental Wavefunction

The wavefunction is not a physical object.

Instead:

- θ is the fundamental field  
- Ψ emerges as a computational tool  
- probabilities arise from knot statistics  

---

### 4.14 Summary

The path integral formulation of TCWT shows:

- quantum amplitudes emerge from phase dynamics  
- interference arises from action differences  
- ℏ is a coherence parameter  
- UV behaviour is regulated by ghost terms  
- measurement corresponds to nonlinear field transitions  

This unifies:

- classical action principles  
- quantum interference  
- statistical interpretation  

within a single phase-coherence framework.

---
## 5. Born Rule from Quadratic Action and Mode Expansion

### 5.1 Goal

We derive the Born rule:

P(x) = |ψ(x)|²

directly from:
- the **quadratic TCWT action**
- canonical quantization of phase perturbations
- detector coupling to the Hum field

No probabilistic postulates are introduced.

---

### 5.2 Quadratic Action for Phase Perturbations

Expand around the coherent background:

θ(x,t) = θ̄(t) + δθ(x,t)

In the low-energy, quasistatic, CDM-like regime:

Ω ≈ θ̇,  
Ġ ≈ ∇²θ

The quadratic action reduces to:

S^{(2)} = ∫ d⁴x \left[
C₀ (δ\dot{θ})² 
− κ (∇δθ)²
− α (∇²δθ)²
\right]

This is a linear field theory with higher-derivative correction.

---

### 5.3 Canonical Normalization

Define canonically normalized field:

φ ≡ √(2C₀) δθ

Then:

S^{(2)} = ∫ d⁴x \left[
\frac{1}{2} (\dot{φ})² 
− \frac{c²}{2} (∇φ)²
− \frac{β}{2} (∇²φ)²
\right]

with:

c² = κ / C₀,  
β = α / C₀

---

### 5.4 Mode Expansion

Expand in Fourier modes:

φ(x,t) = ∫ \frac{d³k}{(2π)³} \left[
a_k u_k(t) e^{i k·x} + a_k† u_k^*(t) e^{-i k·x}
\right]

Mode functions satisfy:

ü_k + ω_k² u_k = 0

with dispersion:

ω_k² = c² k² + β k⁴

---

### 5.5 Quantization

Impose canonical commutation:

[φ(x), π(y)] = i δ³(x − y)

where:

π = \dot{φ}

This yields:

[a_k, a_{k'}†] = (2π)³ δ³(k − k')

The vacuum is defined by:

a_k |0⟩ = 0

---

### 5.6 One-Particle State

Define a normalized one-excitation state:

|ψ⟩ = ∫ d³k f(k) a_k† |0⟩

with:

∫ d³k |f(k)|² = 1

Define position-space wavefunction:

ψ(x,t) ≡ ⟨0| φ(x,t) |ψ⟩

Substituting expansion:

ψ(x,t) = ∫ \frac{d³k}{(2π)³} f(k) u_k(t) e^{i k·x}

---

### 5.7 Detector Coupling

A physical detector responds to **local energy deposition** in the field.

Leading interaction:

H_int = g ∫ d³x D(x) φ(x,t)

where:
- D(x) is detector profile
- g is coupling constant

Transition probability per unit time:

Γ ∝ |⟨0| φ(x,t) |ψ⟩|²

Thus:

Γ(x) ∝ |ψ(x,t)|²

---

### 5.8 Emergence of the Born Rule

The detection probability density is proportional to:

P(x) ∝ Γ(x)

Therefore:

\boxed{
P(x) = |ψ(x,t)|²
}

after normalization.

---

### 5.9 Uniqueness of the Result

The quadratic action enforces:

1. Linear field equation → superposition principle  
2. Canonical commutation → Hilbert space structure  
3. Local detector coupling → linear field insertion  
4. Transition probability → modulus squared  

No alternative power law arises.

Thus the exponent 2 is fixed by:
- linearity of field operators
- bilinear structure of transition amplitudes

---

### 5.10 Role of the k⁴ Term

The ghost-induced correction modifies dispersion:

ω_k² = c² k² + β k⁴

This affects:
- phase evolution
- small-scale propagation
- decoherence rates

But **does not modify the Born rule**, since:

P(x) depends only on operator algebra, not dispersion.

---

### 5.11 Interpretation in TCWT

In standard QFT:
- ψ is a probability amplitude

In TCWT:
- ψ(x,t) = ⟨0|φ|ψ⟩ is a **coarse-grained phase excitation**

Detection corresponds to:
- localized energy transfer
- onset of nonlinear knot formation

Thus:

|ψ|² = energy density of the excitation field

Probability emerges from:
- field quantization
- detector coupling
- transition amplitudes

---

### 5.12 Final Result

The Born rule in TCWT is:

\boxed{
P(x) = \frac{|ψ(x,t)|^2}{\int d^3x\, |ψ(x,t)|^2}
}

derived from:
- the quadratic action
- canonical quantization
- local detector interaction

No probabilistic axiom is required.

---

### 5.13 Key Insight

Quantum probability is not fundamental.

It arises because:

- excitations of the Hum field are quantized
- detectors couple linearly to the field
- transition rates are quadratic in amplitudes

Therefore:

Probability = squared field amplitude

is a structural consequence of the theory.
