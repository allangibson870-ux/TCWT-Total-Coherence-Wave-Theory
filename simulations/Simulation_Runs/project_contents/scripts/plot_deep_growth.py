import matplotlib.pyplot as plt
import numpy as np
import glob

# Find the latest deep background file
files = glob.glob('output/tcwt_deep_*background.dat')
if files:
    latest = sorted(files)[-1]
    data = np.loadtxt(latest)
    
    # Ignore the very last row (the spike) and plot z vs D
    z = data[:-1, 0]
    D = data[:-1, 17]

    plt.figure(figsize=(9, 6))
    plt.plot(z, D, label='TCWT Growth Factor (z=10)', color='crimson', lw=2.5)
    
    plt.xlabel('Redshift (z)', fontsize=12)
    plt.ylabel('Growth Factor D(z)', fontsize=12)
    plt.title('Evolution from Early Universe: TCWT Model', fontsize=14)
    plt.gca().invert_xaxis()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    
    plt.savefig('tcwt_deep_growth.png')
    print(f"\n✅ Success! Deep growth plot saved as tcwt_deep_growth.png")
else:
    print("\n❌ Error: No deep background files found.")
