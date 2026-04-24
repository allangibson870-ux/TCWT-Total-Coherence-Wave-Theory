# TCWT Quantum Limit  
**Linear phase-field quantization, probability, interference, and entanglement**  
**Version:** V2 (V10 Compatible)  
**Status:** Complete quantum-mechanical layer  

---

## 1. Overview
In Total Coherence Wave Theory (TCWT), quantum behaviour emerges from linear dynamics of small perturbations of the Hum phase field. No probabilistic postulates are added. Instead, quantum structure arises from:

- Linear wave dynamics of $\delta\theta$  
- Quadratic action $\rightarrow$ Gaussian probability measure  
- Interference of phase configurations  
- Correlations of the underlying coherence field  

This is the quantum limit of TCWT: the regime where perturbations behave as a quantized scalar field.

---

## 2. Phase Field Decomposition
**Hum background:**  
$$\theta_0(t) = \Omega_{hum} t$$

**Perturbations:**  
$$\theta(x,t) = \theta_0(t) + \delta\theta(x,t)$$

To quadratic order, perturbations behave as a scalar field with dispersion:  
$$\omega^2 = c_s^2 k^2 + m_{eff}^2$$

Where:
- $c_s^2 = \kappa / C_0$  
- $m_{eff}$ arises from the TCWT Lagrangian  

---

## 3. Quadratic Action
$$S^{(2)} = \int d^4x \left[ \frac{1}{2} C_0 (\partial_t \delta\theta)^2 + \frac{1}{2} \kappa (\nabla\delta\theta)^2 + \frac{1}{2} m_{eff}^2 (\delta\theta)^2 \right]$$

This is the standard action for a free scalar field.

---

## 4. Canonical Momentum and Commutator
**Canonical momentum:**  
$$\pi(x,t) = C_0 \partial_t \delta\theta$$

**Equal-time commutation relation:**  
$$[\delta\theta(x,t), \pi(y,t)] = i \delta^3(x - y)$$

---

## 5. Mode Expansion
$$\delta\theta(x,t) = \int \frac{d^3k}{(2\pi)^3} \frac{1}{\sqrt{2 C_0 \omega_k}} \left[ a_k e^{i(k \cdot x - \omega_k t)} + a_k^\dagger e^{-i(k \cdot x - \omega_k t)} \right]$$

**With dispersion:**  
$$\omega_k^2 = c_s^2 k^2 + m_{eff}^2$$

**Ladder operator algebra:**  
$$[a_k, a_{k'}^\dagger] = (2\pi)^3 \delta^3(k - k')$$

---

## 6. Hamiltonian Operator
$$H = \int \frac{d^3k}{(2\pi)^3} \omega_k \left( a_k^\dagger a_k + \frac{1}{2} \right)$$

---

## 7. Propagator
**Time-ordered propagator:**  
$$D_F(x - y) = \langle 0| T \delta\theta(x) \delta\theta(y) |0 \rangle$$

**Momentum-space form:**  
$$D_F(k) = \frac{i C_0}{k_0^2 - c_s^2 k^2 - m_{eff}^2 + i\epsilon}$$

---

## 8. Emergent Probability Measure
The quadratic action implies a Gaussian path integral:  
$$P(k) \propto |a_k|^2$$

This reproduces the Born-rule probability distribution without introducing it as a postulate.

---

## 9. Interference and Detection
**Superposition:**  
$$\theta = \theta_1 + \theta_2$$

**Detection probability:**  
$$P_{knot}(x) \propto f(|\nabla\theta|, \nabla^2\theta)$$

- **Constructive interference:** Enhanced knot formation.
- **Destructive interference:** Suppression of knot formation.

---

## 10. Entanglement as Phase Correlation
$$\langle \delta\theta(x_1) \delta\theta(x_2) \rangle \neq 0$$

Entanglement arises from correlations in the coherent Hum field and respects relativistic causality.

---

## 11. Classical–Quantum Transition
**Quantum regime:**
- Coherence is large.
- Nonlinearities are weak.
- Linear $\delta\theta$ dynamics dominate.

**Classical regime:**
- Coherence decays.
- Fluctuations average out.
- Effective decoherence emerges.

---

## 12. Summary
TCWT provides a deterministic foundation for quantum mechanics:

- Linear phase dynamics $\rightarrow$ wave behaviour.
- Quadratic action $\rightarrow$ probabilistic weighting.
- Interference $\rightarrow$ superposition.
- Entanglement $\rightarrow$ field correlations.
- Decoherence $\rightarrow$ classical limit.

The quantized phase field $\delta\theta$ reproduces quantum field theory structure without introducing independent probabilistic axioms.
