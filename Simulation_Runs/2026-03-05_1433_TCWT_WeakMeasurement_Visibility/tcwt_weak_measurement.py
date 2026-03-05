import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

measurement_strength = np.linspace(0, 1, 50)  # 0=weak, 1=strong

# TCWT duality: higher Ω → higher path knowledge → lower visibility
path_knowledge = measurement_strength
visibility = np.sqrt(1 - path_knowledge**2)  # D² + V² ≤ 1

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#0a0a0a')
ax.set_facecolor('#0a0a0a')

ax.plot(measurement_strength, visibility, color='#00FF88', lw=2.5, label='Fringe Visibility (V)')
ax.plot(measurement_strength, path_knowledge, color='#FF4444', lw=2.5, label='Path Knowledge (D)')
ax.set_title('TCWT Weak Measurement: Visibility vs Path Knowledge', color='white')
ax.set_xlabel('Measurement Strength (Ω increase)', color='white')
ax.set_ylabel('Value', color='white')
ax.legend(facecolor='#111111', labelcolor='white')
ax.tick_params(colors='white')
ax.grid(alpha=0.15)

for s in ax.spines.values():
    s.set_color('white')

plt.tight_layout()
png_path = os.path.join(os.getcwd(), "$PNG_NAME")
plt.savefig(png_path, dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close(fig)

print(f"Saved to: {png_path}")
