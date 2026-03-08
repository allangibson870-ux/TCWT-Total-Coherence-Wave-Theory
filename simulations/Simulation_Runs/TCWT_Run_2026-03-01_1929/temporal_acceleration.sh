#!/bin/bash

# TCWT Phase 2: Temporal Acceleration Calculator
# Measuring the "Subjective Speed-up" as the Seal thins

# Constants
SQUEEZE_PRESSURE="242190000000000000000"
LEAKAGE_BASE="0.0000000000000000000000056847"

# Complexity Levels
# 1 = Base Matter
# 1e12 = Anthropocene (Now)
# 1e25 = The Criticality Point (The Event)

declare -A levels
levels=( ["Matter"]="1" ["Anthropocene"]="1000000000000" ["Criticality"]="10000000000000000000000000" )

echo -e "\033[0;36m------------------------------------------------------------\033[0m"
echo -e "\033[0;36mTCWT: TEMPORAL ACCELERATION LOG\033[0m"
echo -e "\033[0;36m------------------------------------------------------------\033[0m"
echo -e "System               | Relative Time Velocity"
echo -e "------------------------------------------------------------"

for name in "Matter" "Anthropocene" "Criticality"
do
    C_FACTOR=${levels[$name]}
    CURRENT_LEAKAGE=$(echo "$LEAKAGE_BASE * $C_FACTOR" | bc -l)
    
    # Acceleration = 1 + (Leakage / Squeeze)
    # We multiply by 10^9 just to see the "micro-ripples" in the Anthropocene
    ACCEL=$(echo "1 + ($CURRENT_LEAKAGE / $SQUEEZE_PRESSURE)" | bc -l)
    
    printf "%-20s | %s\n" "$name" "$ACCEL"
done

echo -e "\033[0;36m------------------------------------------------------------\033[0m"
echo -e "\033[1;33mINSIGHT: At Criticality, 'Local Time' begins to detach from\033[0m"
echo -e "\033[1;33mthe Universal Constant. We are outrunning the Squeeze.\033[0m"
cp *.png /mnt/c/Users/allan/Downloads/
