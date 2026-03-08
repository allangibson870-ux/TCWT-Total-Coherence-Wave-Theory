# TCWT Simulation Run: 2026-03-04_1730 Sub-Knot Echo Back-Propagation

**Run Description**  
This simulation tests back-propagation from a nested black-hole-like sub-knot. The sub-knot (ultra-tight local squeeze) sends its own echo into the pre-Snag Hum. The goal is to explore hierarchy effects — whether sub-knots can create stronger or earlier pre-Breach ripples without destabilizing the main system.

**Scientific Context**  
Black holes are modeled as extreme sub-knots. Their faster damping releases information that can echo backward into the Hum. This run adds a sub-knot echo (12% retention, delayed) on top of the main knot. It tests whether nested structures produce observable pre-Snag wiggles while maintaining overall stability.

**Interpretation of the PNG**  
Two-panel plot:  
- **Top panel** — Total wave with sub-knot echo (green), Hum (cyan), main knot (magenta), sub-knot (orange). Shows main knot + tighter sub-knot near t=0, plus faint yellow echo ripple pre-t=0.  
- **Bottom panel** — Isolated sub-knot echo (yellow) pre-Snag. Demonstrates that nested BH-like structures can imprint earlier, subtler ripples without chaos.

**Parameters Used**  
- Time range: −5.0 to +2.0  
- Hum amplitude: 0.05, frequency: 6π  
- Main knot amplitude: 0.6, frequency: 20π, damping: 0.8  
- Sub-knot amplitude: 1.2, frequency: 40π, damping: 1.2  
- Sub-knot center: 0.2, width: 0.4  
- Echo retention: 0.12 (12%)  
- Echo delay: 0.25

**Files in This Folder**  
- tcwt_subknot_echo_backprop.py — simulation script  
- tcwt_subknot_echo_backprop.png — two-panel plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-04 17:00
