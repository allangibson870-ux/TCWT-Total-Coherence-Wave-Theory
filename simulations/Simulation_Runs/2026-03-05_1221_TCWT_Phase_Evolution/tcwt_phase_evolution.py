import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, random, getpass
from datetime import datetime

# Capture source for the folder
try:
    with open(__file__, 'r') as f:
        SCRIPT_CODE = f.read()
except:
    SCRIPT_CODE = "Source capture failed."

random.seed(42)
np.random.seed(42)

# --- PARAMETERS ---
SAMPLES = 2000          # Events per phase point
PHASE_STEPS = 60        # Resolution of the cycle (0 to 2*pi)
RATIO = 0.92            # The 'Quantum Sweet Spot' from our previous sweep
A, AP = 0, np.pi/2      # Bell Angles (Setting A)
B, BP = np.pi/4, 3*np.pi/4 # Bell Angles (Setting B)

def run_bell_at_phase(global_phase):
    """Tests the S-value at a specific point in the Eternal Wave cycle"""
    def get_corr(ang1, ang2):
        # The correlation is a function of the settings AND the global wave phase
        # This models the "Small World" interacting with the "Eternal Wave"
        c = np.cos((ang1 - ang2) * RATIO + global_phase)
        results = [1 if random.random() < (0.5 + 0.5 * c) else -1 for _ in range(SAMPLES)]
        return np.mean(results)
    
    Eab   = get_corr(A, B)
    Eabp  = get_corr(A, BP)
    Eapb  = get_corr(AP, B)
    Eapbp = get_corr(AP, BP)
    return abs(Eab - Eabp + Eapb + Eapbp)

# --- EXECUTION ---
phase_range = np.linspace(0, 2 * np.pi, PHASE_STEPS)
s_values = []

print(f"Testing Temporal Phase Evolution across {PHASE_STEPS} points...")
for p in phase_range:
    s_values.append(run_bell_at_phase(p))

# --- FILE MANAGEMENT ---
win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
ts = datetime.now().strftime('%Y-%m-%d_%H%M')
outdir = f"/mnt/c/Users/{win_user}/Downloads/{ts}_TCWT_Phase_Evolution"
os.makedirs(outdir, exist_ok=True)

# --- GRAPHING ---
plt.figure(figsize=(12,6))
plt.plot(phase_range, s_results if 's_results' in locals() else s_values, color='mediumslateblue', linewidth=2)
plt.axhline(2.0, color='red', linestyle='--', label='Classical Limit (S=2.0)')
plt.axhline(2.828, color='green', linestyle=':', label='Quantum Bound (S=2.82)')
plt.fill_between(phase_range, 2.0, 3.0, color='blue', alpha=0.05, label='Non-Local Zone')

plt.title("TCWT: Temporal Phase Evolution (The 'Eternal Pulse')")
plt.xlabel("Global Wave Phase (Radians 0 to 2π)")
plt.ylabel("Bell Violation (S-Value)")
plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ['0', 'π/2', 'π', '3π/2', '2π'])
plt.legend(loc='upper right')
plt.grid(True, alpha=0.2)
plt.savefig(f"{outdir}/phase_evolution_plot.png")

# --- README GENERATION ---
readme_content = f"""# TCWT Simulation: Temporal Phase Evolution

## What is being tested?
This simulation explores how the **Eternal Wave Phase** ($\Phi$) affects the strength of quantum entanglement. In **Temporal Curvature Wave Theory**, the manifold is not static; it oscillates. We are testing if the S-value (Bell violation) changes as the global wave progresses through one full cycle ($0$ to $2\pi$).

## Why is this important?
If the S-value oscillates, it suggests that "Quantumness" is a phase-dependent phenomenon. This would mean that entanglement is a **Resonant State** that reaches peak strength only at specific intervals in the eternal cycle.

## Parameters Used:
*   **Frequency Ratio (r)**: {RATIO} (Optimized for maximum resonance)
*   **Samples per point**: {SAMPLES}
*   **Phase Resolution**: {PHASE_STEPS} steps
*   **Bell Settings**: Standard CHSH angles (0, 45, 90, 135 degrees)

## Expected Result:
A sinusoidal or periodic wave showing the "Breathing" of the temporal manifold.
"""

with open(f"{outdir}/README.md", "w") as f:
    f.write(readme_content)

with open(f"{outdir}/tcwt_phase_evolution.py", "w") as f:
    f.write(SCRIPT_CODE)

print(f"Simulation Complete. Folder created: {outdir}")
