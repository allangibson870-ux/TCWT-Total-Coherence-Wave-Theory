import matplotlib.pyplot as plt
import numpy as np
import os

# Targeting the '03' series from your output
output_root = 'output/tcwt_deep_03_'
redshifts = ['0', '1.0', '2.0', '5.0', '10.0']
colors = plt.cm.plasma(np.linspace(0, 0.8, len(redshifts)))

plt.figure(figsize=(10, 6))

for i, z in enumerate(redshifts):
    filename = f'{output_root}z{i+1}_pk.dat'
    if os.path.exists(filename):
        data = np.loadtxt(filename)
        plt.loglog(data[:, 0], data[:, 1], label=f'z = {z}', color=colors[i], lw=2)
    else:
        print(f'Missing: {filename}')

plt.title('Matter Power Spectrum Evolution (TCWT Model - Run 03)', fontsize=14)
plt.xlabel('k [h/Mpc]', fontsize=12)
plt.ylabel('P(k) [(Mpc/h)^3]', fontsize=12)
plt.legend()
plt.grid(True, which='both', ls='-', alpha=0.2)
plt.tight_layout()
plt.savefig('tcwt_pk_evolution_updated.png')
print('SUCCESS: tcwt_pk_evolution_updated.png created')