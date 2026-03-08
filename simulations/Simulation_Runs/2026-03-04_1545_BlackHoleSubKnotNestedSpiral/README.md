# TCWT Simulation Run: 2026-03-04_1545 BlackHole Sub-Knot Nested Spiral

**Run Description**  
This simulation extends the main knot with a nested black-hole-like sub-knot. The goal is to explore whether extreme local squeeze (black-hole analog) can trigger a secondary phase shift (mini-Snag) that resolves faster than the main knot, while keeping the overall TimeWave stable. The sub-knot forms near t=0 (main Snag), shows tighter curvature, and damps more quickly — demonstrating hierarchical untangling without chaos or infinite recursion.

**Scientific Context**  
In TCWT, the Eternal Hum is the eternal, low-amplitude background oscillation. Knots are localized phase shifts (Snags) that drive structure and the dark sector. Black holes are modeled as ultra-tight sub-knots: extreme density compresses the wave to a threshold where a new, nested Snag activates. This run shows a controlled embedding: the sub-knot inherits information from the main knot, resolves faster, and leaves a subtle imprint on the total wave without destabilizing the Hum baseline.

**Interpretation of the PNG**  
Single figure with two panels (side-by-side):  
- **Left panel (Nested Spiral)**: Plots total wave (black), main knot (blue), sub-knot (red) in the curvature/amplitude vs. time-parameter plane. Shows the large outer spiral (Hum + main knot) with a tighter inner spiral (sub-knot) embedded near t=0. Demonstrates nesting without runaway.  
- **Right panel (Waveform Components)**: Time-series view of the same components. Shows main knot activation at t=0, sub-knot snapping in near t=0 with higher frequency and faster decay. Total wave shows combined effect — slight bump from sub-knot but overall damping forward.

**Parameters Used**  
- Time range: −10.0 to +10.0 (dimensionless)  
- Steps: 4000  
- Background Hum amplitude: 1.0  
- Background Hum frequency: 0.12  
- Main knot amplitude: 2.0  
- Main knot frequency: 0.25  
- Main knot damping: 0.04  
- Sub-knot amplitude: 3.0  
- Sub-knot frequency: 0.6  
- Sub-knot base damping: 0.06  
- Sub-knot extra damping (after snap): 0.10  
- Sub-knot center time: −2.0  
- Sub-knot width: 1.0  
- Sub-knot snap threshold factor: 0.7  
- Sub-knot post-snap frequency drop: 0.4  

**Files in This Folder**  
- forever_timewave_blackhole_subknot.py — the simulation script  
- tcwt_blackhole_subknot.png — combined two-panel visualization  
- README.md — this explanatory document  

**Timestamp**  
Generated on: 2026-03-04 15:45
