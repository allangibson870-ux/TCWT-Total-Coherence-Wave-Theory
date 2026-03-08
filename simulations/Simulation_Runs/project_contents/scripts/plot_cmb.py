import matplotlib.pyplot as plt
import numpy as np

# Load your TCWT data
data = np.loadtxt('output/tcwt_high_sig_01_cl.dat')
ell = data[:, 0]
tt = data[:, 1]

# Convert Cl to Dl (the standard format)
# Dl = l*(l+1)*Cl / (2 * pi)
dl_factor = ell * (ell + 1) / (2 * np.pi)

plt.figure(figsize=(10, 6))
plt.plot(ell, tt * dl_factor * 1e12, color='darkgreen', lw=2, label='TCWT Simulation')

plt.xlabel(r'Multipole $\ell$', fontsize=12)
plt.ylabel(r'$\ell(\ell+1)C_\ell^{TT} / 2\pi$ [$\mu K^2$]', fontsize=12)
plt.title('CMB Temperature Power Spectrum (TCWT Model)', fontsize=14)
plt.xlim(2, 2500)
plt.grid(True, which="both", ls='--', alpha=0.3)
plt.legend(frameon=False)

plt.savefig('tcwt_cmb_plot.png', dpi=300)
print("Success! CMB plot saved as tcwt_cmb_plot.png")
