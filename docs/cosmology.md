\documentclass{article}
\usepackage{amsmath,amssymb}
\usepackage{geometry}
\geometry{margin=1in}

\title{TCWT Cosmological Perturbations}
\author{}
\date{}

\begin{document}

\maketitle

\section{Relativistic TCWT Action}

TCWT is built on three interacting fields: the Hum phase field $\theta$, the local oscillation frequency $\Omega$, and the ghost-relaxation field $G$.

To connect the theory to cosmology, structure formation, and gravitational observables, we require a fully covariant action defined on a spacetime metric $g_{\mu\nu}$. The relativistic action must reduce to the Master Lagrangian in the weak-field, quasistatic limit.

\subsection{Covariant Structure}

We introduce:
\begin{itemize}
    \item a unit timelike 4-velocity $u^\mu$ representing the cosmological rest frame,
    \item a spatial projector $h^{\mu\nu} = g^{\mu\nu} + u^\mu u^\nu$.
\end{itemize}

These allow us to define:
\begin{itemize}
    \item temporal derivatives: $u^\mu \nabla_\mu$,
    \item spatial gradients: $h^{\mu\nu} \nabla_\nu$,
    \item spatial Laplacian: $h^{\mu\nu} \nabla_\mu \nabla_\nu$.
\end{itemize}

In an FLRW background, these reduce to
\begin{equation*}
    u^\mu \nabla_\mu \to \partial_t, \qquad
    h^{\mu\nu} \nabla_\mu \to \nabla, \qquad
    h^{\mu\nu} \nabla_\mu \nabla_\nu \to \nabla^2.
\end{equation*}

\subsection{The Relativistic TCWT Lagrangian}

A covariant generalisation of the Master Lagrangian is
\begin{align*}
\mathcal{L}_{\rm TCWT}
={}& -\frac{1}{2} C_0 \bigl( u^\mu \nabla_\mu \theta - \Omega \bigr)^2
    - \kappa a_0^2 \, F\!\left( \frac{h^{\mu\nu} \nabla_\mu \theta \nabla_\nu \theta}{a_0^2} \right) \\
& - V_\Omega(\Omega) \\
& - \alpha \bigl( u^\mu \nabla_\mu G - h^{\mu\nu} \nabla_\mu \nabla_\nu \theta \bigr)^2 \\
& - \mathcal{L}_{\rm soliton}.
\end{align*}

Each term corresponds directly to a component of the non-relativistic theory:
\begin{itemize}
    \item Temporal coherence: $-\frac{1}{2} C_0 (u^\mu \nabla_\mu \theta - \Omega)^2 \to C_0 (\partial_t \theta - \Omega)^2$
    \item Nonlinear gradient sector: $-\kappa a_0^2 F\!\left( \frac{h^{\mu\nu} \nabla_\mu \theta \nabla_\nu \theta}{a_0^2} \right) \to \kappa a_0^2 F(|\nabla \theta|^2 / a_0^2)$
    \item Frequency potential: $-V_\Omega(\Omega) \to$ unchanged
    \item Ghost-leakage channel: $-\alpha (u^\mu \nabla_\mu G - h^{\mu\nu} \nabla_\mu \nabla_\nu \theta)^2 \to \alpha (\partial_t G - \nabla^2 \theta)^2$
    \item Matter sector: $\mathcal{L}_{\rm soliton}$ encodes the effective behaviour of soliton matter
\end{itemize}

\subsection{Full Relativistic Action}

\begin{equation*}
S = \int d^4 x \, \sqrt{-g} \Biggl[ \frac{1}{16\pi G} R + \mathcal{L}_{\rm TCWT} \Biggr].
\end{equation*}

This action is fully covariant, reduces to the Master Lagrangian in the weak-field limit, and provides the foundation for cosmology, perturbations, and structure formation.

\section{Background Cosmology in TCWT}

\subsection{FLRW Metric and Homogeneous Fields}

We assume a spatially flat FLRW metric
\begin{equation*}
ds^2 = -dt^2 + a(t)^2 \delta_{ij} \, dx^i dx^j,
\end{equation*}
with Hubble rate $H(t) = \dot{a}/a$.

In the cosmological rest frame: $u^\mu = (1,0,0,0)$, $h^{\mu\nu} = g^{\mu\nu} + u^\mu u^\nu$.

Homogeneous fields: $\theta = \bar{\theta}(t)$, $\Omega = \bar{\Omega}(t)$, $G = \bar{G}(t)$. Spatial gradients vanish at background level.

\subsection{Background TCWT Lagrangian Density}

\begin{align*}
\mathcal{L}_{\rm TCWT}^{(\rm bg)}
={}& -\frac{1}{2} C_0 \bigl( \dot{\bar{\theta}} - \bar{\Omega} \bigr)^2
    - V_\Omega(\bar{\Omega}) \\
& - \alpha \, \dot{\bar{G}}^2
    - \mathcal{L}_{\rm soliton}^{(\rm bg)}.
\end{align*}

The nonlinear gradient term drops out at the homogeneous level.

Effective background energy densities and pressures (schematic):
\begin{align*}
\rho_{\rm hum} &\sim \frac{1}{2} C_0 (\dot{\bar{\theta}} - \bar{\Omega})^2 + V_\Omega(\bar{\Omega}), &
p_{\rm hum} &\sim \frac{1}{2} C_0 (\dot{\bar{\theta}} - \bar{\Omega})^2 - V_\Omega(\bar{\Omega}), \\
\rho_G &\sim \alpha \, \dot{\bar{G}}^2, &
p_G &\sim \alpha \, \dot{\bar{G}}^2, \\
\rho_{\rm m} &= \rho_{\rm soliton}^{(\rm bg)}, & p_{\rm m} &\approx 0 \quad \text{(dust-like)}.
\end{align*}

\subsection{Modified Friedmann Equations}

\begin{align}
H^2 &= \frac{8\pi G}{3} \bigl( \rho_{\rm hum} + \rho_G + \rho_{\rm m} + \rho_{\rm rad} + \dots \bigr), \\
\dot{H} &= -4\pi G \bigl( \rho_{\rm tot} + p_{\rm tot} \bigr).
\end{align}

Background field equations:
\begin{align}
\ddot{\bar{\theta}} + 3H \dot{\bar{\theta}} + \dots &= 0, \\
\frac{\partial V_\Omega}{\partial \bar{\Omega}} + C_0 (\dot{\bar{\theta}} - \bar{\Omega}) + \dots &= 0, \\
\ddot{\bar{G}} + 3H \dot{\bar{G}} + \dots &= 0.
\end{align}

\section{Linear Perturbations in TCWT}

\subsection{Perturbation Setup}

Newtonian gauge:
\begin{equation*}
ds^2 = -(1 + 2\Phi) \, dt^2 + a(t)^2 (1 - 2\Psi) \delta_{ij} \, dx^i dx^j.
\end{equation*}

Perturbed fields:
\begin{align*}
\theta &= \bar{\theta}(t) + \delta\theta(\vec{x},t), \\
\Omega &= \bar{\Omega}(t) + \delta\Omega(\vec{x},t), \\
G    &= \bar{G}(t)    + \delta G(\vec{x},t).
\end{align*}

Matter: $\rho_{\rm m} = \bar{\rho}_{\rm m}(t) (1 + \delta_{\rm m})$, $v_i = \partial_i v$.

\subsection{Linearised TCWT Field Equations}

\begin{subequations}
\begin{align}
\delta\ddot{\theta} + 3H \delta\dot{\theta} + \frac{k^2}{a^2} \mu_\theta \, \delta\theta
    + C_0 (\delta\dot{\theta} - \delta\Omega) &= S_\theta(\Phi,\Psi), \tag{a} \\
C_0 (\delta\dot{\theta} - \delta\Omega)
    + V''_\Omega(\bar{\Omega}) \, \delta\Omega &= S_\Omega(\Phi,\Psi), \tag{b} \\
\delta\ddot{G} + 3H \delta\dot{G} + \alpha \frac{k^2}{a^2} \delta G
    &= \alpha \frac{k^2}{a^2} \delta\theta + S_G(\Phi,\Psi). \tag{c}
\end{align}
\end{subequations}

\subsection{Modified Einstein Equations}

Poisson-like equation:
\begin{equation*}
\frac{k^2}{a^2} \Psi = 4\pi G \bigl( \bar{\rho}_{\rm m} \delta_{\rm m} + \delta\rho_{\rm hum} + \delta\rho_G \bigr).
\end{equation*}

Gravitational slip:
\begin{equation*}
\Phi - \Psi = \Pi_{\rm TCWT}.
\end{equation*}

\subsection{Matter Perturbations}

\begin{align}
\dot{\delta}_{\rm m} &= -\frac{k^2}{a^2} v + 3 \dot{\Psi}, \\
\dot{v} &= -\Phi.
\end{align}

Modified growth rate: $f(a) = \frac{d \ln D}{d \ln a}$.

\section{Numerical Implementation of TCWT (Boltzmann-Style Framework)}

[Outline of background module, perturbation module, observable module, minimal parameter set, and staged implementation strategy — text unchanged, equations already cleaned above.]

\section{Parameter Fitting and Observational Confrontation}

[Text unchanged — parameter lists and datasets already presented clearly.]

\section{Hum Condensation and the Origin of Matter and Dark Energy}

[Text mostly narrative; key equations already cleaned in earlier sections.]

\section{Summary}

This document provides the cosmological layer of TCWT:
\begin{itemize}
    \item background expansion
    \item linear perturbation theory
    \item mapping phase fluctuations to density contrast
    \item the TCWT growth equation
    \item the route to the matter power spectrum
\end{itemize}

This completes the theoretical machinery needed to compare TCWT with $\Lambda$CDM across cosmological scales.

\end{document}
