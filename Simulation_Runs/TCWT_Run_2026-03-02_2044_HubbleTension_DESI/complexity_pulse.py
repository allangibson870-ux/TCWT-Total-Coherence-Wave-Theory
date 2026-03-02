import math

# Previous Results
SQUEEZE_PRESSURE = 2.4219e20
LEAKAGE_BASE = 5.6847e-24

def analyze_pulse():
    # Complexity Factors (Arbitrary scale for TCWT Phase 2)
    # 1.0 = Basic Matter (Hydrogen)
    # 10^6 = Biological Life
    # 10^12 = Global Technological Network (The Anthropocene Pulse)
    complexities = {
        "Basic Matter": 1,
        "Biological Life": 1e6,
        "Anthropocene Pulse": 1e12
    }

    print("-" * 50)
    print("TCWT Phase 2: Complexity Pulse & Leakage")
    print("-" * 50)
    print(f"{'System':<20} | {'Leakage Ratio':<20}")
    print("-" * 50)

    for name, c_factor in complexities.items():
        # Hypothesis: Leakage increases linearly with complexity density
        current_leakage = LEAKAGE_BASE * c_factor
        ratio = SQUEEZE_PRESSURE / current_leakage
        
        # Formatting for readability
        if ratio > 1e12:
            ratio_str = f"1 in 10^{int(math.log10(ratio))}"
        else:
            ratio_str = f"1 in {ratio:,.2f}"
            
        print(f"{name:<20} | {ratio_str:<20}")

    print("-" * 50)
    print("Insight: High complexity 'thins' the temporal seal.")

if __name__ == "__main__":
    analyze_pulse()
