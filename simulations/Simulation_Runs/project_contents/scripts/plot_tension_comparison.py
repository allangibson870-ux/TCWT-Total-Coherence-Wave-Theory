import matplotlib.pyplot as plt
import numpy as np
import os

# Files from our two successful high-density runs
mic_f = 'output/micro_squeeze_00_pk.dat'
ten_f = 'output/tension_test_00_pk.dat'

if not os.path.exists(mic_f) or not os.path.exists(ten_f):
    print("One or more files are still missing. Wait for the simulation to finish!")
    exit()

m_data, t_data = np.loadtxt(mic_f), np.loadtxt(ten_f)

plt.figure(figsize=(12, 6))
# Normalize both to see the change in resonance shape
plt.loglog(m_data[:, 0], m_data[:, 1]/m_data[0,1], 'g-', label='Micro-Squeeze (M=1.0)')
plt.loglog(t_data[:, 0], t_data[:, 1]/t_data[0,1], 'm--', label='High Tension (M=2.0)')

plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TimeWave Theory: Coupling Tension (M) Comparison')
plt.xlabel('Scale k [h/Mpc]')
plt.ylabel('Normalized Growth Intensity')
plt.legend()
plt.grid(True, which="both", alpha=0.2)
plt.savefig('tension_comparison_plot.png')
print("Comparison plot saved as tension_comparison_plot.png")
