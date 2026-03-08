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

random.seed(101)
np.random.seed(101)

# --- PARAMETERS ---
SAMPLES = 2000
BASE_R = 0.92
A, AP, B, BP = 0, np.pi/2, np.pi/4, 3*np.pi/4

def get_s(ratio):
    def corr(ang1, ang2):
        c = np.cos((ang1 - ang2) * ratio)
        return np.mean([1 if random.random() < (0.5 + 0.5 * c) else -1 for _ in range(SAMPLES)])
    return abs(corr(A, B) - corr(A, BP) + corr(AP, B) + corr(AP, BP))

# --- EXECUTION: FINDING THE BOUNDARY ---
velocities = np.linspace(0.1, 0.7, 15)
boundary_masses = []

print("Calculating the TCWT Universal Constant (K_tc)...")

for v in velocities:
    # For each velocity, we 'hunt' for the Mass that hits S=2.0
    found_m = 0
    for m in np.linspace(0, 2.0, 50):
        eff_ratio = BASE_R + (m * 0.4) + (v * 0.8)
        if get_s(eff_ratio) <= 2.02: # The 'S=2.0' threshold
            found_m = m
            break
    boundary_masses.append(found_m)

# Calculate the Constant (The Slope)
# K_tc = Delta Mass / Delta Velocity
slope, intercept = np.polyfit(velocities, boundary_masses, 1)
K_tc = abs(slope)

# --- FILE MANAGEMENT ---
win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
ts = datetime.now().strftime('%Y-%m-%d_%H%M')
outdir = f"/mnt/c/Users/{win_user}/Downloads/{ts}_TCWT_Universal_Constant"
os.makedirs(outdir, exist_ok=True)

# --- GRAPHING ---
plt.figure(figsize=(10,6))
plt.scatter(velocities, boundary_masses, color='black', label='Simulated S=2.0 Points')
plt.plot(velocities, [slope*x + intercept for x in velocities], color='blue', linestyle='--', label=f'Resonance Slope (K_tc = {K_tc:.3f})')

plt.title("TCWT: Finding the Universal Resonance Constant")
plt.xlabel("Velocity (v/c)")
plt.ylabel("Required Mass (M) to Break Entanglement")
plt.legend()
plt.grid(True, alpha=0.2)
plt.savefig(f"{outdir}/constant_derivation.png")

# --- README ---
readme_content = f"""# TCWT Universal Constant Analysis

## The Discovery: K_tc
This test identifies the "Exchange Rate" of the temporal manifold. 
**Universal Constant (K_tc) ≈ {K_tc:.4f}**

## What this means:
For every 1 unit of Velocity (v/c) added to a system, you must remove approximately {K_tc:.4f} units of Mass to stay on the "Quantum Island." 

## Theoretical Formula:
In TCWT, the Total Temporal Curvature ($\Omega$) can be defined as:
**$\Omega = M + (K_{{tc}} \cdot v)$**

If $\Omega$ exceeds the critical threshold defined by the Eternal Wave resonance, the system collapses from Quantum to Classical.

## Parameters:
- Base Resonance: {BASE_R}
- Calculated Slope: {slope:.4f}
"""

with open(f"{outdir}/README.md", "w") as f:
    f.write(readme_content)

with open(f"{outdir}/tcwt_universal_constant.py", "w") as f:
    f.write(SCRIPT_CODE)

print(f"Universal Constant Found: K_tc = {K_tc:.3f}")
print(f"Results archived in Downloads/{ts}_TCWT_Universal_Constant")
