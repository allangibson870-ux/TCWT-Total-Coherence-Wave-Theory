import matplotlib.pyplot as plt
import numpy as np
import os
import glob

# Find the latest background file
bg_files = glob.glob('output/*background.dat')

if not bg_files:
    print("\n❌ Error: No background files found.")
else:
    latest_file = sorted(bg_files)[-1]
    print(f"✅ Found data in: {latest_file}")
    
    with open(latest_file, 'r') as f:
        # Get the header and clean it up
        header = f.readline().replace('#', '').strip().split()
    
    data = np.loadtxt(latest_file)

    # Fuzzy search for the 'z' column (often '1:z' or 'z_evolution')
    z_idx = next((i for i, h in enumerate(header) if 'z' in h.lower()), 0)
    
    # Fuzzy search for 'sigma8' or 'rho' (density)
    s8_idx = next((i for i, h in enumerate(header) if 'sigma8' in h.lower()), -1)
    
    print(f"📊 Using columns: {header[z_idx]} (x) and {header[s8_idx]} (y)")

    plt.figure(figsize=(9, 6))
    plt.plot(data[:, z_idx], data[:, s8_idx], color='darkorange', lw=2.5)
    
    plt.xlabel(header[z_idx], fontsize=12)
    plt.ylabel(header[s8_idx], fontsize=12)
    plt.title(f'Evolution: {latest_file.split("/")[-1]}', fontsize=14)
    plt.gca().invert_xaxis()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.savefig('tcwt_growth_plot.png')
    print(f"🚀 Success! Plot saved as tcwt_growth_plot.png")
