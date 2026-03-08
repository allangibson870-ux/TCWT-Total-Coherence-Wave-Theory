# TCWT Simulation Run: 2026-03-04_1612 TCWT vs MOND H(z) Comparison

**Run Description**  
Compares TCWT's resonant late-time modulation of H(z) against a toy MOND-inspired adjustment. TCWT starts at local H₀ ≈73.1 km/s/Mpc, declines toward early-universe ≈67.4 with damped ripples. MOND toy adds a small low-z boost to baseline early H₀.

**Scientific Context**  
TCWT predicts H(z) modulation from TimeWave untangling/leakage in late universe. MOND modifies gravity at low accelerations but does not naturally bridge Hubble tension; this toy version adds minimal late-time effect for comparison. Plot tests if TCWT's mechanism bridges local and early H₀ more naturally.

**Interpretation of the PNG**  
Single plot (H(z) vs. z, 0 to 20):  
- **Green line** — TCWT: starts at local H₀ (~73.1), smooth decline + damped ripples toward early H₀ (~67.4).  
- **Dashed orange** — Local SH0ES H₀ (~73.1).  
- **Dashed green** — Early Planck/CMB H₀ (~67.4).  
- **Red line** — MOND toy: baseline early H₀ with small low-z boost.  
TCWT threads the gap; MOND toy stays near early value.

**Parameters Used**  
- Redshift range: z = 0.0 to 20.0 (500 points)  
- TCWT local H₀: 73.1 km/s/Mpc  
- TCWT early H₀: 67.4 km/s/Mpc  
- TCWT decay scale: 5.0  
- TCWT ripple amp: 0.8 km/s/Mpc  
- TCWT ripple freq: 0.8  
- MOND toy late-time factor: 1 + 0.02 * exp(-z/2)  

**Files in This Folder**  
- tcwt_vs_mond_hz_comparison.py — simulation script  
- tcwt_vs_mond_hz_comparison.png — H(z) comparison plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-04 16:12
