import matplotlib.pyplot as plt
import numpy as np

# Load the indexed file
data = np.loadtxt('output/tcwt_high_sig_01_background.dat')

z = data[:, 0]
phi_prime = data[:, 18] # Column 19 (index 18) is the velocity

plt.figure(figsize=(10, 6))
plt.semilogx(z, phi_prime, color='royalblue', lw=2, label='TCWT Velocity')
plt.axhline(0, color='black', ls='--', alpha=0.3)

plt.xlabel('Redshift (z)', fontsize=12)
plt.ylabel(r"Field Velocity (\phi')", fontsize=12)
plt.title('The Eternal TimeWave: High-Redshift Velocity Evolution', fontsize=14)
plt.gca().invert_xaxis() # High z to Low z
plt.grid(True, which="both", alpha=0.2)
plt.legend()

plt.savefig('timewave_evolution.png', dpi=300)
print("Success! Plot saved as timewave_evolution.png")
