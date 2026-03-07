import numpy as np
import matplotlib.pyplot as plt

h = 6.626e-34
m_e = 9.109e-31
c = 3e8

slit_separation = 1e-6
screen_distance = 1.0
wavelength_rest = 1e-10

beta = np.linspace(0.0, 0.999, 200)
gamma = 1 / np.sqrt(1 - beta**2)
p_rel = gamma * m_e * beta * c
lambda_rel = h / p_rel

x = np.linspace(-0.01, 0.01, 1000)
theta = x / screen_distance

I = []
for lam in lambda_rel:
    delta = (2 * np.pi * slit_separation * np.sin(theta)) / lam
    intensity = np.cos(delta / 2)**2 * (np.sinc(delta / (2 * np.pi)))**2
    I.append(intensity / np.max(intensity))
I = np.array(I)

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

for i in [0, 50, 100, 150, 199]:
    b = beta[i]
    ax.plot(x * 1e3, I[i], label=f'β = {b:.3f} (γ = {gamma[i]:.1f})')

ax.set_title('Relativistic Double-Slit Interference (electron)', color='white')
ax.set_xlabel('Position on screen (mm)', color='white')
ax.set_ylabel('Normalised Intensity', color='white')
ax.legend(facecolor='#111111', labelcolor='white')
ax.tick_params(colors='white')
ax.grid(True, alpha=0.3)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
plt.savefig("$PNG_NAME", dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
