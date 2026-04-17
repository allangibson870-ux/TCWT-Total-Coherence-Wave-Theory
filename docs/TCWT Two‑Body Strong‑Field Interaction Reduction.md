# TCWT Two‑Body Strong‑Field Interaction Reduction

## 1. Purpose
This section links the full TCWT Lagrangian to a reduced two‑body interaction picture in terms of a phase‑gradient field $\lambda$ and a ghost‑tension diagnostic $T$ for two strongly interacting Hopfion knots in a stationary regime.

---

## 2. Setup: two stationary knots
We consider two localized Hopfion knots at fixed positions $\mathbf{x}_1$ and $\mathbf{x}_2$, and work in a stationary regime where time derivatives of the background are negligible on the interaction timescale.

Phase field decomposition:

$$ \theta(\mathbf{x}) = \theta_{\text{Hum}} + \theta_1(\mathbf{x}) + \theta_2(\mathbf{x}) + \delta\theta_{\text{int}}(\mathbf{x}) $$

We focus on a 2D slice (e.g. the mid‑plane between the knots), with coordinates $(x,y)$.

---

## 3. Effective fields: $\lambda$ and $T$

### 3.1 Phase-gradient field $\lambda$

In TCWT the phase-gradient field is:

$$ \boldsymbol{\lambda}(\mathbf{x}) = \nabla\theta(\mathbf{x}), \qquad \lambda(\mathbf{x}) = |\boldsymbol{\lambda}(\mathbf{x})| $$

On a 2D slice:

$$ \lambda(x,y) = |\nabla_\perp\theta(x,y)| $$

Omega-cap constraint:

$$ \lambda(x,y) \le \lambda_{\text{cap}}, \qquad \lambda_{\text{cap}} = \Omega_{\max}/\kappa $$

### 3.2 Ghost-tension diagnostic $T$

Ghost equation:

$$ \partial_t[2\alpha(\dot{G} - \nabla^2\theta)] = 0 $$

Low-energy leakage:

$$ \dot{G} \approx \nabla^2\theta $$

Diagnostic:

$$ T(\mathbf{x}) = |\dot{G}(\mathbf{x}) - \nabla^2\theta(\mathbf{x})| $$

On the slice:

$$ T(x,y) = |\dot{G}(x,y) - \nabla_\perp^2\theta(x,y)| $$

---

## 4. Static strong-field reduction

Full phase equation:

$$ 2C_0\,\partial_t(\dot{\theta} - \Omega) - \nabla\cdot[\kappa\,\mu(|\nabla\theta|/a_0)\nabla\theta] - 2\alpha\,\nabla^2(\dot{G} - \nabla^2\theta) = 0 $$

Strong-field stationary limit:

$$ \partial_t(\dot{\theta} - \Omega) \approx 0, \qquad |\nabla\theta| \gtrsim a_0 \Rightarrow \mu \to 1 $$

Reduced equation:

$$ \nabla\cdot(\kappa\nabla\theta) + 2\alpha\nabla^2(\dot{G} - \nabla^2\theta) = 0 $$

On the slice:

$$ \nabla_\perp\cdot(\kappa\nabla_\perp\theta) + 2\alpha\nabla_\perp^2 T = 0 $$

Using $\lambda_\perp = \nabla_\perp\theta$ and $T = \dot{G} - \nabla_\perp^2\theta$:

$$ \nabla_\perp\cdot(\kappa\lambda_\perp) + 2\alpha\nabla_\perp^2 T = 0 $$

Unsaturated:

$$ \nabla_\perp\cdot(\kappa\lambda_\perp) \approx 0 $$

Saturated:

$$ |\lambda_\perp| \to \lambda_{\text{cap}} $$

---

## 5. Two-body superposition and effective composition rule

Linear far-field:

$$ \lambda_{\text{lin}}(x,y) = \lambda_1(x,y) + \lambda_2(x,y) $$

Saturated regime:

$$ \lambda(x,y) \le \lambda_{\text{cap}} $$

Effective gradient:

$$ \lambda_{\text{eff}}(x,y) = \min(\lambda_1(x,y) + \lambda_2(x,y),\ \lambda_{\text{cap}}) $$

Ghost-tension excess:

$$ T_{\text{eff}}(x,y) = \max(0,\ \lambda_1(x,y) + \lambda_2(x,y) - \lambda_{\text{cap}}) $$

---

## 6. Axial profiles

Along $y=0$:

$$ \lambda_{\text{eff}}(x) = \lambda_{\text{eff}}(x,0), \qquad T_{\text{eff}}(x) = T_{\text{eff}}(x,0) $$
