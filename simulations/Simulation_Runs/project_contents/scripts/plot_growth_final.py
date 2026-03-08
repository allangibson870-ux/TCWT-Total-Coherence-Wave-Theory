import matplotlib.pyplot as plt
import numpy as np
import os

# Load the file we found in your last screen
data_file = 'output/tcwt_growth_02_background.dat'

if os.path.exists(data_file):
    data = np.loadtxt(data_file)
    
    # Based on your 'head' output:
    # Column 0 is Redshift (z)
    # Column 17 is Growth Factor D
    z = data[:, 0]
    growth_D = data[:, 17]

    plt.figure(figsize=(9, 6))
    plt.plot(z, growth_D, label='Growth Factor (D)', color='darkorange', lw=2.5)
    
    plt.xlabel('Redshift (z)', fontsize=12)
    plt.ylabel('Growth Factor D(z)', fontsize=12)
    plt.title('Cosmic Growth Evolution: TCWT Model', fontsize=14)
    
    # Move from past (high z) to today (z=0)
    plt.gca().invert_xaxis()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend()
    
    plt.savefig('tcwt_growth_D_plot.png')
    print("\n✅ Success! Plot saved as tcwt_growth_D_plot.png")
else:
    print(f"\n❌ Error: {data_file} not found.")
