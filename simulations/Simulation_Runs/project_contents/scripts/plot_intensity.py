import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('output/tcwt_high_sig_01_background.dat')
z = data[:, 0]
rho_smg = data[:, 13] # Adjust based on your header count!
p_smg = data[:, 14]   # Adjust based on your header count!

# Calculate Equation of State w = P/rho 
# (Vibrational intensity often shows up as oscillations in w)
w_smg = p_smg / rho_smg

plt.figure(figsize=(10, 6))
plt.semilogx(z, w_smg, color='darkorange', lw=2)
plt.axvline(3400, color='black', ls=':', label='Matter-Radiation Equality')

plt.xlabel('Redshift (z)')
plt.ylabel('Equation of State (w_smg)')
plt.title('TimeWave Oscillation Intensity vs. Cosmic Eras')
plt.gca().invert_xaxis()
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('timewave_intensity.png')
print("Intensity plot saved as timewave_intensity.png")
