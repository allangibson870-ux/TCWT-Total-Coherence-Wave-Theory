import matplotlib.pyplot as plt
import numpy as np
# Try loading with '00' or '01' if it fails
try:
    data = np.loadtxt('output/tcwt_vibrate_00_background.dat')
except:
    data = np.loadtxt('output/tcwt_vibrate_01_background.dat')

z = data[:, 0]
rho = data[:, 13]
p = data[:, 14]
w = p/rho

plt.figure(figsize=(10, 6))
plt.semilogx(z, w, color='darkred', lw=2, label='TimeWave Equation of State')
plt.axvline(3400, color='black', ls=':', label='Matter-Radiation Equality')
plt.title('TimeWave Vibration: Interaction with Cosmic Mass')
plt.xlabel('Redshift (z)')
plt.ylabel('Equation of State (w)')
plt.gca().invert_xaxis()
plt.grid(True, which="both", alpha=0.2)
plt.legend()
plt.savefig('vibration_check.png')
print("Plot saved as vibration_check.png")
