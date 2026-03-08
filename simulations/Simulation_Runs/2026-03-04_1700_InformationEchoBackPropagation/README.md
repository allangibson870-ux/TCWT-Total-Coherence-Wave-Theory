# TCWT Simulation Run: 2026-03-04_1700 Information Echo Back-Propagation

**Run Description**  
This simulation tests upstream information echo: after the knot damps post-Snag, a small fraction (~8%) of its final state is fed back as a perturbation into the pre-Snag Hum. The goal is to see if back-propagation creates observable pre-Breach ripples (e.g., CMB or DESI-like anomalies) without destabilizing the eternal Hum.

**Scientific Context**  
In TCWT, information is never lost — untangling knot modes release patterns that can echo backward into the Hum. This run models a weak, delayed echo (0.3 time units shift, 8% retention) from the main knot's decay. The echo appears as a faint ripple pre-t=0, while post-t=0 damping continues normally. This tests whether upstream feedback could explain subtle early-universe anomalies.

**Interpretation of the PNG**  
Two-panel plot (top: no echo, bottom: with echo):  
- **Top panel** — Baseline: Hum (cyan) + forward knot (magenta) + total (green). Knot activates at t=0, damps forward; Hum unchanged.  
- **Bottom panel** — With echo: adds yellow back-propagated ripple pre-t=0. Total wave shows faint pre-Snag oscillation from echo, while forward damping remains stable.  
Demonstrates controlled upstream feedback — echo imprints on pre-BB Hum without chaos.

**Parameters Used**  
- Time range: −5.0 to +2.0 (2000 points)  
- Hum amplitude: 0.05, frequency: 6π  
- Knot amplitude: 0.6, frequency: 20π, damping: 0.8  
- Echo retention: 0.08 (8%)  
- Echo delay: 0.3 time units  
- Echo damping: same as knot (0.8)

**Files in This Folder**  
- tcwt_information_echo_backprop.py — simulation script  
- tcwt_information_echo_backprop.png — two-panel plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-04 16:30
