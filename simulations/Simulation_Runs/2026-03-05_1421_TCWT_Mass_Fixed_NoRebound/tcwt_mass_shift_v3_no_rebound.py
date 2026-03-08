import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, random, getpass
from datetime import datetime

SCRIPT_CONTENT = open(__file__).read() if os.path.exists(__file__) else "Source capture failed."

random.seed(101)
np.random.seed(101)

def run_bell_test(ratio):
    a, ap, b, bp = 0, np.pi/2, np.pi/4, 3*np.pi/4
    def corr(ang1, ang2):
        c = np.cos((ang1 - ang2) * ratio)
        return np.mean([1 if random.random() < (0.5 + 0.5 * c) else -1 for _ in range(3000)])  # more samples for smoother result
    return abs(corr(a, b) - corr(a, bp) + corr(ap, b) + corr(ap, bp))

mass_range = np.linspace(0, 3.0, 40)  # more points for smoother curve
s_results = []

for m in mass_range:
    # Soft saturation: linear at low M, exponential decay at high M
    ratio = 0.9 + (m * 0.5) * np.exp(-0.35 * m)
    s_results.append(run_bell_test(ratio))

win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
ts = datetime.now().strftime('%Y-%m-%d_%H%M')
outdir = f"/mnt/c/Users/{win_user}/Downloads/{ts}_TCWT_Mass_Fixed_NoRebound"
os.makedirs(outdir, exist_ok=True)

plt.figure(figsize=(10,6))
plt.plot(mass_range, s_results, color='darkorange', marker='o', markersize=4, label='S-value (soft saturation)')
plt.fill_between(mass_range, 2.0, 2.828, color='green', alpha=0.12, label='Quantum Zone')
plt.axhline(2.0, color='red', linestyle='--', label='Classical Limit (S=2.0)')
plt.title("TCWT: Mass/Energy Shift of the Temporal Manifold (No Rebound)")
plt.xlabel("Local Mass/Energy Density (M)")
plt.ylabel("Bell Violation (S-Value)")
plt.legend()
plt.grid(alpha=0.15)
plt.savefig(f"{outdir}/mass_shift_no_rebound.png")

with open(f"{outdir}/tcwt_mass_shift_v3_no_rebound.py", "w") as f:
    f.write(SCRIPT_CONTENT)

print(f"Success. Check Downloads/{ts}_TCWT_Mass_Fixed_NoRebound for the PNG and .py file.")
