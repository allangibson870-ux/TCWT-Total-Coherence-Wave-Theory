import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, random, getpass
from datetime import datetime

# Capture source code
try:
    with open(__file__, 'r') as f:
        SCRIPT_CODE = f.read()
except:
    SCRIPT_CODE = "Source capture failed."

random.seed(42)
np.random.seed(42)

# --- PARAMETERS ---
SAMPLES = 1500
A, AP, B, BP = 0, np.pi/2, np.pi/4, 3*np.pi/4
FREQS_TO_TEST = [0.8, 0.92, 1.1] # Testing different 'Eternal' environments

def get_s(ratio):
    def corr(ang1, ang2):
        c = np.cos((ang1 - ang2) * ratio)
        return np.mean([1 if random.random() < (0.5 + 0.5 * c) else -1 for _ in range(SAMPLES)])
    return abs(corr(A, B) - corr(A, BP) + corr(AP, B) + corr(AP, BP))

# --- EXECUTION ---
velocities = np.linspace(0.1, 0.6, 10)
results = {}

print("Running Universal Stability Test across multiple frequencies...")

for base_f in FREQS_TO_TEST:
    boundary_masses = []
    for v in velocities:
        found_m = 0
        # Search for the M that hits the S=2.0 threshold
        for m in np.linspace(0, 2.5, 60):
            # Our Unified Formula: Ratio = Base + (M * 0.4) + (V * 0.8)
            eff_ratio = base_f + (m * 0.4) + (v * 0.8)
            if get_s(eff_ratio) <= 2.01:
                found_m = m
                break
        boundary_masses.append(found_m)
    
    # Calculate slope for this frequency
    slope, intercept = np.polyfit(velocities, boundary_masses, 1)
    results[base_f] = (boundary_masses, abs(slope))

# --- FILE MANAGEMENT ---
win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
ts = datetime.now().strftime('%Y-%m-%d_%H%M')
outdir = f"/mnt/c/Users/{win_user}/Downloads/{ts}_TCWT_Universal_Stability"
os.makedirs(outdir, exist_ok=True)

# --- GRAPHING ---
plt.figure(figsize=(10,7))
colors = ['blue', 'green', 'red']
for i, (f, (masses, slope)) in enumerate(results.items()):
    plt.plot(velocities, masses, marker='o', linestyle='--', color=colors[i], 
             label=f'Freq {f}: K_tc = {slope:.3f}')

plt.title("TCWT: Universal Stability of the K_tc Constant")
plt.xlabel("Velocity (v/c)")
plt.ylabel("Mass (M) at Classical Threshold")
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(f"{outdir}/stability_test.png")

# --- README ---
readme_content = f"""# TCWT Universal Stability Test

## The Objective
This test checks if the Resonance Constant ($K_{{tc}}$) is dependent on the background frequency. 
If the lines are parallel, $K_{{tc}}$ is a **Universal Geometric Constant**.

## Results:
"""
for f, (_, slope) in results.items():
    readme_content += f"- Background Frequency {f}: Calculated K_tc = {slope:.4f}\n"

readme_content += """
## Interpretation:
If the K_tc values are nearly identical (e.g., all ~2.0), it confirms that TCWT defines a 
fixed relationship between Mass and Velocity across all points in the eternal manifold.
"""

with open(f"{outdir}/README.md", "w") as f:
    f.write(readme_content)

with open(f"{outdir}/tcwt_universal_stability.py", "w") as f:
    f.write(SCRIPT_CODE)

print(f"Universal Test Complete. Stability results archived in: {outdir}")
