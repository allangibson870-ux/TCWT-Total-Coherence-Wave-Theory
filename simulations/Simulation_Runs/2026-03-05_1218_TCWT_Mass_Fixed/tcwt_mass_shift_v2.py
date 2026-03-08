import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, random, getpass
from datetime import datetime

# The Code Content (to be saved)
SCRIPT_CONTENT = open(__file__).read() if os.path.exists(__file__) else "Source capture failed."

random.seed(101)
np.random.seed(101)

def run_bell_test(ratio):
    a, ap, b, bp = 0, np.pi/2, np.pi/4, 3*np.pi/4
    def corr(ang1, ang2):
        c = np.cos((ang1 - ang2) * ratio)
        return np.mean([1 if random.random() < (0.5 + 0.5 * c) else -1 for _ in range(1500)])
    return abs(corr(a, b) - corr(a, bp) + corr(ap, b) + corr(ap, bp))

mass_range = np.linspace(0, 3.0, 30)
s_results = []

for m in mass_range:
    ratio = 0.9 + (m * 0.5) # The "Mass-Frequency Link"
    s_results.append(run_bell_test(ratio))

win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
ts = datetime.now().strftime('%Y-%m-%d_%H%M')
outdir = f"/mnt/c/Users/{win_user}/Downloads/{ts}_TCWT_Mass_Fixed"
os.makedirs(outdir, exist_ok=True)

plt.figure(figsize=(10,6))
plt.plot(mass_range, s_results, color='darkorange', marker='o', markersize=4)
plt.fill_between(mass_range, 2.0, 2.828, color='green', alpha=0.1, label='Quantum Zone')
plt.axhline(2.0, color='red', linestyle='--', label='Classical Limit')
plt.title("TCWT: Mass/Energy Shift of the Temporal Manifold")
plt.xlabel("Local Mass/Energy Density (M)")
plt.ylabel("Bell Violation (S-Value)")
plt.legend()
plt.savefig(f"{outdir}/mass_shift_plot.png")

# Manual force-write of the source code
with open(f"{outdir}/tcwt_mass_shift_v2.py", "w") as f:
    f.write(SCRIPT_CONTENT)

print(f"Success. Check Downloads/{ts}_TCWT_Mass_Fixed for the PNG and the .py file.")
