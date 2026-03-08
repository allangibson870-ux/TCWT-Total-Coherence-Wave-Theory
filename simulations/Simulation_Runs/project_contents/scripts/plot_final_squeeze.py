import matplotlib.pyplot as plt
import numpy as np
import os

# Comparing the Micro-Squeeze (0.135) to the new Stabilized Squeeze (0.140)
mic_f = 'output/micro_squeeze_00_pk.dat'
stb_f = 'output/stabilized_squeeze_00_pk.dat'

if not os.path.exists(mic_f) or not os.path.exists(stb_f):
    print("Missing files! Check your output/ folder.")
    exit()

m_data, s_data = np.loadtxt(mic_f), np.loadtxt(stb_f)

plt.figure(figsize=(12, 6))
# Normalize to the first point to compare the growth curves
plt.loglog(m_data[:, 0], m_data[:, 1]/m_data[0,1], 'g-', lw=2, label='Micro-Squeeze (0.135, M=1.0)')
plt.loglog(s_data[:, 0], s_data[:, 1]/s_data[0,1], 'b--', lw=2, label='Stabilized Squeeze (0.140, M=2.0)')

plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Theory: Tension vs. Mass Load')
plt.xlabel('Scale k [h/Mpc]')
plt.ylabel('Normalized Growth Intensity')
plt.legend()
plt.grid(True, which="both", alpha=0.2)
plt.savefig('final_squeeze_plot.png')
print("Success! Final Squeeze plot saved as final_squeeze_plot.png")
