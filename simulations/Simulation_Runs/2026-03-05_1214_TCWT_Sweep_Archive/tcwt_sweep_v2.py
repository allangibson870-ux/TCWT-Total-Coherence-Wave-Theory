import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, random, getpass, shutil
from datetime import datetime

random.seed(101)
np.random.seed(101)

def gen_correlation(angle_A, angle_B, freq_ratio):
    delta_theta = (angle_A - angle_B)
    correlation_val = np.cos(delta_theta * freq_ratio)
    results = [1 if random.random() < (0.5 + 0.5 * correlation_val) else -1 for _ in range(1000)]
    return np.mean(results)

ratios = np.linspace(0.5, 2.5, 50)
s_values = []
a, ap, b, bp = 0, np.pi/2, np.pi/4, 3*np.pi/4

for r in ratios:
    s_values.append(abs(gen_correlation(a, b, r) - gen_correlation(a, bp, r) + gen_correlation(ap, b, r) + gen_correlation(ap, bp, r)))

win_user = os.popen("powershell.exe '$env:UserName'").read().strip() or getpass.getuser()
outdir = f"/mnt/c/Users/{win_user}/Downloads/{datetime.now().strftime('%Y-%m-%d_%H%M')}_TCWT_Sweep_Archive"
os.makedirs(outdir, exist_ok=True)

plt.figure(figsize=(10,6))
plt.plot(ratios, s_values, color='firebrick', label='TCWT Response')
plt.axhline(2.0, color='black', linestyle='--')
plt.axhline(2.828, color='blue', linestyle=':')
plt.savefig(f"{outdir}/sweep_plot.png")

# NEW: Save the script itself into the folder
shutil.copy(__file__, f"{outdir}/tcwt_sweep_v2.py")

with open(f"{outdir}/README.md", "w") as f:
    f.write("# TCWT Sweep Archive\nIncluded .py source for reproducibility.")

print(f"Sweep Re-run Complete. Files + Script saved to: {outdir}")
