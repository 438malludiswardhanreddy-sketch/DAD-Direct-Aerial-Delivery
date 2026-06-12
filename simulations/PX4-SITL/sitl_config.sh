#!/bin/bash
# DAD final year design project - Solapur University
# PX4 Software-In-The-Loop (SITL) Launch Configuration

echo "[SITL] Initialising PX4 SITL parameters..."
export PX4_HOME_LAT=17.6590
export PX4_HOME_LON=75.9059
export PX4_HOME_ALT=470.0  # Solapur average elevation above sea level in metres

# Compile and run SITL simulator typhoon hexacopter model
cd "$HOME/PX4-Autopilot" || { echo "PX4-Autopilot repository not found."; exit 1; }
make px4_sitl gazebo-classic_typhoon_h480
