# TCWT Simulation Run: 2026-03-04_1800 Multi-Echo from Multiple Knots (Safe)

**Run Description**  
This simulation models multiple damped knots feeding back at staggered times, creating a complex pre-Snag echo pattern. Three knots untangle post-t=0 and send overlapping echoes backward into the Hum. Reduced steps and dpi for stability.

**Scientific Context**  
Multiple knots (main + secondary) release information at different rates. Their echoes overlap pre-Snag, producing layered ripples. This run tests whether hierarchical feedback creates rich pre-BB patterns (potential CMB/DESI signatures) while keeping the Hum stable.

**Interpretation of the PNG**  
Two-panel plot:  
- **Top panel** — Total wave (green) with Hum (cyan) and three knots (magenta/orange/yellow). Shows forward damping + pre-Snag ripple from multi-echo.  
- **Bottom panel** — Combined echoes (yellow) + individual contributions. Demonstrates overlapping, delayed imprints from multiple knots.

**Parameters Used**  
- Time range: −5.0 to +2.0 (1500 points)  
- Hum amplitude: 0.05, frequency: 6π  
- Knot 1: amp 0.6, freq 20π, damping 0.8, center 0.0  
- Knot 2: amp 0.4, freq 30π, damping 1.0, center 0.3  
- Knot 3: amp 0.3, freq 45π, damping 1.2, center 0.6  
- Echo retention: 0.10  
- Echo delays: 0.25, 0.35, 0.45

**Files in This Folder**  
- tcwt_multi_echo_multiple_knots.py — simulation script  
- tcwt_multi_echo_multiple_knots.png — two-panel plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-04 17:00
