# TCWT Simulation Run: 2026-03-06_1143 Hum Distortion Around Varying Masses

**Run Description**  
Shows how the background Hum amplitude is suppressed at the surface of objects with different masses (from proton to solar-mass black hole).

**Scientific Context**  
In TCWT, all mass is small knots. Distortion Ω = G M² / (4π r⁴ P_squeeze).  
Hum amplitude = exp(-Ω).  
Small masses → negligible suppression.  
Large masses (stars) → noticeable.  
Black holes → Hum completely suppressed.

**Interpretation of the PNG**  
- Points: Hum amplitude at surface of each object.  
- Line: Guides the eye across mass scale (log).  
- Hum is virtually untouched around atoms/humans, slightly reduced around planets/stars, and completely gone near black hole horizons.

**Parameters Used**  
- P_squeeze = 2.4219e20 Pa (from hydrogen knot)  
- Masses & radii are typical values

**Files in This Folder**  
- tcwt_hum_distortion_varying_mass.py — script  
- hum_distortion_varying_mass.png — plot  
- README.md — document  

**Timestamp**  
2026-03-06 1143
