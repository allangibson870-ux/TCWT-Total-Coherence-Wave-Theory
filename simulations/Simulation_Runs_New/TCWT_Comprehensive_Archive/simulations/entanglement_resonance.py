import numpy as np
import matplotlib.pyplot as plt

def plot_phase_coupling():
    # Parameters for two entangled knots
    t = np.linspace(0, 10, 500)
    omega = 5.0 # Shared frequency
    coupling_strength = 0.8
    
    # Phase of Knot A and B (Phase-Locked)
    phase_a = np.sin(omega * t)
    # Introducing a small perturbation at t=5
    perturbation = np.where(t > 5, 0.5 * np.sin(omega * t), 0)
    phase_b = np.sin(omega * t) + (coupling_strength * perturbation)

    plt.figure(figsize=(10, 5))
    plt.plot(t, phase_a, label='Knot A Phase', color='cyan')
    plt.plot(t, phase_b, label='Knot B (Phase-Locked)', color='magenta', ls='--')
    plt.axvline(x=5, color='red', ls=':', label='Measurement Perturbation')
    plt.title('TCWT Entanglement: Shared Hum Resonance')
    plt.xlabel('Time (t)')
    plt.ylabel('Phase Amplitude')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('entanglement_plot.png')

if __name__ == "__main__":
    plot_phase_coupling()
