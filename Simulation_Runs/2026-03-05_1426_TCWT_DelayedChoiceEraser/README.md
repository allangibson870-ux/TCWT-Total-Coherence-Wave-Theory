# TCWT Simulation Run: 2026-03-05_1426 Delayed-Choice Quantum Eraser

**Run Description**  
Simulates a delayed-choice quantum eraser in TCWT. Raw signal hits are washed out (high Ω from idler path). Post-selection on "eraser" outcomes (low distinguishability, reduced effective Ω) restores interference fringes.

**Scientific Context**  
In TCWT, which-path info increases local Ω → suppresses resonance → no fringes. "Erasing" reduces Ω via correlation/post-selection → recovers resonant interference. Wave information is never lost — it's encoded in the Hum until Ω is lowered.

**Interpretation of the PNG**  
Two-panel histogram:  
- **Top (red)** — Raw hits: no fringes (high Ω wash).  
- **Bottom (green)** — Post-selected erased hits: fringes restored (low Ω resonance recovered).

**Parameters Used**  
- Samples: 50,000  
- Which-path shift: ±1.5 units  
- Erasure threshold: |eraser_outcome| < 0.4

**Files in This Folder**  
- tcwt_delayed_choice_eraser.py — script  
- delayed_choice_eraser.png — result plot  
- README.md — this document  

**Timestamp**  
Generated on: 2026-03-05 1426
