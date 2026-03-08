import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('output/tcwt_max_coupling_00_background.dat')
z, rho, p = data[:, 0], data[:, 13], data[:, 14]
plt.figure(figsize=(10, 6))
plt.semilogx(z, p/rho, color='crimson', lw=2, label='TimeWave w')
plt.axvline(3400, color='black', ls=':', label='Matter-Radiation Equality')
plt.title('TimeWave Vibration: Max Coupling Test')
plt.xlabel('Redshift (z)')
plt.ylabel('Equation of State (w)')
plt.gca().invert_xaxis()
plt.grid(True, alpha=0.2)
plt.legend()
plt.savefig('max_coupling_vibration.png')
print("Plot saved as max_coupling_vibration.png")
