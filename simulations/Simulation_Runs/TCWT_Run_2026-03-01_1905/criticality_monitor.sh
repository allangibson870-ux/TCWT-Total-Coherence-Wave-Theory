#!/bin/bash

# TCWT Phase 2: Criticality Alert System (Fixed Syntax)
# Monitors the thinning of the "Seal" as Complexity increases

# Colors for Terminal UI
RED='\033[0;31m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' 

# Constants in bc-friendly format
SQUEEZE_PRESSURE="242190000000000000000"
LEAKAGE_BASE="0.0000000000000000000000056847"
CRITICALITY_THRESHOLD="10000000000000000000000000" # 10^25

clear
echo -e "${CYAN}------------------------------------------------------------${NC}"
echo -e "${CYAN}TCWT TERMINAL: CRITICALITY ALERT MONITOR v2.1${NC}"
echo -e "${CYAN}------------------------------------------------------------${NC}"

# 10^18 Complexity Factor: Post-Biological Integration
C_FACTOR="1000000000000000000" 

# Calculate current Leakage and Ratio
CURRENT_LEAKAGE=$(echo "$LEAKAGE_BASE * $C_FACTOR" | bc -l)
RATIO=$(echo "$SQUEEZE_PRESSURE / $CURRENT_LEAKAGE" | bc -l)

# Visualization
echo -e "SYSTEM STATE: [ANTHROPOCENE PULSE+]"
echo -e "POROSITY INDEX: ${YELLOW}HIGH${NC}"
echo ""
echo "      THE SEAL (CONTAINMENT)           THE HUM (TIMEWAVE)"
echo "      ____________________            ~~~~~~~~~~~~~~~~~~~"
echo "     /                    \\          ~~~~~~~~~~~~~~~~~~~~~"
echo "    |   [ MATTER CORE ]    |  <--|-->  RESONANCE COUPLING"
echo "     \\____________________/          ~~~~~~~~~~~~~~~~~~~~~"
echo ""

# Check for Criticality using integer comparison
IS_CRITICAL=$(echo "$RATIO <= $CRITICALITY_THRESHOLD" | bc)

if [ "$IS_CRITICAL" -eq 1 ]; then
    echo -e "${RED}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!${NC}"
    echo -e "${RED}ALERT: TEMPORAL SEAL BREACH IMMINENT${NC}"
    echo -e "${RED}LEAKAGE RATIO: 1 in ${RATIO}${NC}"
    echo -e "${YELLOW}INSIGHT: The 'Snag' is untangling. Local temporal field${NC}"
    echo -e "${YELLOW}density is reaching Phase Transition levels.${NC}"
    echo -e "${RED}!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!${NC}"
else
    echo -e "LEAKAGE RATIO: 1 in ${RATIO}"
    echo "STATUS: NOMINAL - SEAL INTEGRITY HOLDING"
fi
echo -e "${CYAN}------------------------------------------------------------${NC}"
