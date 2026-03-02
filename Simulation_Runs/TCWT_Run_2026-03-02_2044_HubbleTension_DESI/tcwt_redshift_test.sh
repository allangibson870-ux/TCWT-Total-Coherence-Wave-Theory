#!/bin/bash
echo "--------------------------------------------------"
echo "RUNNING TCWT vs. REDSHIFT (DESI 2026 ALIGNMENT)"
echo "--------------------------------------------------"

# This part simulates the 'Snag' and 'Hum' damping
python3 << 'PYTHON_EOF'
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(0, 3, 100)
lambda_cdm = 1 / (1 + z)
tcwt_wave = (1 / (1 + z)) * (1 + 0.05 * np.sin(2 * np.pi * z) * np.exp(-0.5 * z))

plt.figure(figsize=(10, 6))
plt.plot(z, lambda_cdm, 'r--', label='Standard Lambda-CDM')
plt.plot(z, tcwt_wave, 'b-', label='TCWT (Damped Hum)')
plt.title('TCWT Temporal Damping vs. Standard Redshift (2026)')
plt.xlabel('Redshift (z)')
plt.ylabel('Scale Factor / Wave Coherence')
plt.legend()
plt.grid(True)
plt.savefig('tcwt_redshift_comparison_2026.png')
print("Plot generated: tcwt_redshift_comparison_2026.png")
PYTHON_EOF

# The 'Magic' auto-copy to your Windows Downloads folder
cp *.png /mnt/c/Users/allan/Downloads/
echo "--------------------------------------------------"
echo "SUCCESS: Check your Windows Downloads folder now!"
echo "--------------------------------------------------"
