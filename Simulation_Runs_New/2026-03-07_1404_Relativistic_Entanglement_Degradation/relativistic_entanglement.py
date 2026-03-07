import numpy as np
import matplotlib.pyplot as plt

beta = np.linspace(0.0, 0.999, 200)
gamma = 1 / np.sqrt(1 - beta**2)

fidelity_loss = np.exp(-gamma * beta**2 * 0.5)
fidelity = 1 - (1 - fidelity_loss) * 0.3

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(beta, fidelity, color='cyan', lw=2.5, label='Entanglement Fidelity')
ax.axhline(0.707, color='red', linestyle='--', label='Tsirelson bound violation threshold (~0.707)')

ax.set_title('Relativistic Degradation of Entanglement (EPR pair)', color='white')
ax.set_xlabel('Boost speed β = v/c', color='white')
ax.set_ylabel('Entanglement Fidelity', color='white')
ax.set_ylim(0.65, 1.02)
ax.legend(facecolor='#111111', labelcolor='white')
ax.tick_params(colors='white')
ax.grid(True, alpha=0.3)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
plt.savefig("$PNG_NAME", dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
