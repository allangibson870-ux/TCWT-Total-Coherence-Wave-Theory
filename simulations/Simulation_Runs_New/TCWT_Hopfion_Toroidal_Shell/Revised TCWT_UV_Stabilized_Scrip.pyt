import numpy as np
import matplotlib.pyplot as plt

def generate_tcwt_uv_derived():
    # Frequency / energy scale
    k = np.logspace(-1, 4, 600)

    # ----------------------------
    # 1. Standard UV divergence
    # ----------------------------
    standard_energy = k**2

    # ----------------------------
    # 2. TCWT Physical Parameters
    # ----------------------------

    # Ghost sector (derived scale)
    # k_g^6 ~ κ γ^2 / α^4  → treat k_g as effective fit parameter
    k_g = 300.0   # ghost damping scale

    # Omega-cap scale (physical saturation)
    k_cap = 500.0  # corresponds to λ_cap mapping

    # ----------------------------
    # 3. Derived Transfer Function
    # ----------------------------
    T_k = 1.0 / ((1 + (k / k_g)**6) * (1 + (k / k_cap)**4))

    # TCWT energy spectrum
    tcwt_energy = k**2 * T_k

    # ----------------------------
    # 4. Plotting
    # ----------------------------
    plt.figure(figsize=(10, 6), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')

    # Curves
    plt.loglog(k, standard_energy, 'r--', lw=2,
               label='Standard Theory (UV Catastrophe)')
    plt.loglog(k, tcwt_energy, 'cyan', lw=2.5,
               label='TCWT (Derived Ghost + Ω-Cap)')

    # Mark scales
    plt.axvline(k_g, color='yellow', linestyle='--',
                label='Ghost Damping Scale (k_g)')
    plt.axvline(k_cap, color='magenta', linestyle=':',
                label='Ω-Cap Scale (k_cap)')

    # Labels
    plt.title("TCWT Derived UV Stabilization", color='white', fontsize=14)
    plt.xlabel("k (Phase Frequency / Energy Scale)", color='white')
    plt.ylabel("Interaction Energy Density", color='white')

    # Style
    plt.tick_params(colors='white', which='both')
    plt.grid(color='gray', alpha=0.2)
    plt.legend(facecolor='black', edgecolor='white', labelcolor='white')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    generate_tcwt_uv_derived()
