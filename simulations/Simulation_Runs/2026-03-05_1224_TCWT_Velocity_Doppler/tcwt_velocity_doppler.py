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

random.seed(77)
np.random.seed(77)

# --- PARAMETERS ---
SAMPLES = 2000
BASE_RATIO = 0.92  # Our resonant 'Sweet Spot'
C = 1.0            # Normalized Speed of Light

def get_s_value(effective_ratio):
    a, ap, b, bp = 0, np.pi/2, np.pi/4, 3*np.pi/4
    def corr(ang1, ang2):
        # Wave correlation modulated by the Doppler-shifted ratio
        c = np.cos((ang1 - ang2) * effective_ratio)
        results = [1 if random.random() < (0.5 + 0.5 * c) else -1 for _ in range(SAMPLES)]
        return np.mean(results)
    return abs(corr(a, b) - corr(a, bp) + corr(ap, b) + corr(ap, bp))

# --- EXECUTION ---
# Testing velocity from 0 to 95% the speed of light
velocities = np.linspace(0, 0.95, 40)
s_values = []

print("Simulating Temporal Doppler Shift (Velocity vs S-Value)...")
for v in velocities:
    # Doppler Shift Formula for the Temporal Wave frequency ratio
    # Relativistic Doppler Effect: f_obs = f_src * sqrt((1+v/c)/(1-v/c))
    # For TCWT, we test the linear shift of the ratio: r_eff = r_base * (1 + v/c)
    doppler_ratio = BASE_RATIO * (1 + v/C) 
    s_values.append(get_s_value(doppler_ratio))

# --- FILE MANAGEMENT ---
win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
ts = datetime.now().strftime('%Y-%m-%d_%H%M')
outdir = f"/mnt/c/Users/{win_user}/Downloads/{ts}_TCWT_Velocity_Doppler"
os.makedirs(outdir, exist_ok=True)

# --- GRAPHING ---
plt.figure(figsize=(10,6))
plt.plot(velocities, s_values, color='crimson', marker='x', markersize=4, label='TCWT Doppler Response')
plt.axhline(2.0, color='black', linestyle='--', label='Classical Limit (S=2.0)')
plt.fill_between(velocities, 2.0, 3.0, color='red', alpha=0.1, label='Quantum Zone')

plt.title("TCWT: Velocity-Induced Temporal Frequency Shift")
plt.xlabel("Velocity (v/c)")
plt.ylabel("Bell Violation (S-Value)")
plt.legend()
plt.grid(True, alpha=0.2)
plt.savefig(f"{outdir}/velocity_doppler_plot.png")

# --- README ---
readme_content = f"""# TCWT Simulation: Velocity Doppler Shift

## What is being tested?
This simulation explores the **Doppler Effect** on the temporal manifold. If time is a wave, moving through it at a velocity ($v$) shifts the perceived frequency of the "Eternal Wave." We are testing how this shift moves the observer out of the "Quantum Resonance" peak.

## Parameters:
- **Base Resonant Ratio**: {BASE_RATIO}
- **Velocity Range**: 0 to 0.95c
- **Sample Density**: {SAMPLES} per point

## Implications:
If the S-value drops as velocity increases, TCWT predicts that relativistic travel acts as a **De-coherence mechanism**, effectively forcing the universe to behave "Classically" for fast-moving observers.
"""

with open(f"{outdir}/README.md", "w") as f:
    f.write(readme_content)

with open(f"{outdir}/tcwt_velocity_doppler.py", "w") as f:
    f.write(SCRIPT_CODE)

print(f"Simulation Complete. Results saved to Downloads/{ts}_TCWT_Velocity_Doppler")
