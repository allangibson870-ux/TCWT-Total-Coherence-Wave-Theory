Two-component forever timewave run on 2026-03-03_1526

TCWT Simulation: Analysis of the Calibrated Two‑Component Timewave
Run Description
This simulation presents a calibrated two‑component TCWT timewave consisting of a background hum and a knot mode. The purpose of this run is to visualise how these two components interact across cosmic time, including the Big Bang and the present epoch, and to demonstrate the calibrated amplitude ratio that matches the observed visible and dark sector energy fractions.

Scientific Context
The TCWT framework models the universe as the interference of two oscillatory components:

Background Hum — a stable, low‑amplitude oscillation representing the visible/baryonic sector of the universe.

Knot Mode — a wound, high‑energy, out‑of‑phase component representing the dark sector (dark matter + dark energy). It tightens approaching the Big Bang and loosens afterwards.

In this run, the knot amplitude is calibrated so that at the chosen “now” marker, the energy ratio between the knot and background components matches the observed cosmic composition: approximately 95% dark sector and 5% visible matter.

The time axis is dimensionless, with:

t = 0 marking the Big Bang

t = 1 representing a far‑future state where the knot mode has effectively decayed

t = 0.7 chosen as the present epoch (“now”)

Interpretation of the PNG
The generated PNG contains three vertically stacked panels:

Background Hum Panel  
Shows the stable sinusoidal background component. The yellow dashed line marks the Big Bang, and the green dashed line marks the present epoch.

Knot Mode Panel  
Displays the wound knot component. It peaks sharply near the Big Bang and decays gradually afterwards. Its amplitude at t = 0.7 has been calibrated to match the dark sector fraction.

Total Wave Panel  
Shows the combined interference of the background and knot components. This represents the observable TCWT timewave, including the transition from early‑universe dominance of the knot to the present‑day mixture.

Parameters Used
These are the actual numerical values used in this run:

Background amplitude: 0.05

Background frequency: 6π

Knot frequency: 20π

Knot phase offset: π/2

Envelope (pre‑BB): exponential growth with strength 4.0

Envelope (post‑BB): exponential decay with strength 1.5

Present epoch marker: t_now = 0.7

Target amplitude ratio (knot/background): √19 ≈ 4.36

Calibrated knot amplitude: (value computed in the run)

Files in This Folder
forever_timewave_two_component.py — the simulation script used for this run

forever_timewave_two_component.png — the rendered three‑panel visualisation

README.md — this explanatory document

NOTES.txt — timestamp and run note

Timestamp
This run was generated on: 2026‑03‑03
