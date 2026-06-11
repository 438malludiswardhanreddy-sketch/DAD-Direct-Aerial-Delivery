#!/bin/bash
# DAD PX4 Software In The Loop (SITL) Setup Script
# Configures the Gazebo simulator environment with Tarot hexacopter model.

echo "=========================================================="
echo "    Configuring DAD PX4 SITL Simulation Environment      "
echo "=========================================================="

# 1. Check for ROS 2 / Gazebo packages
if ! command -v gz &> /dev/null; then
    echo "[SIM] Warning: Gazebo (gz) simulator is not installed."
    echo "[SIM] Please install Gazebo Classic or Gz Sim to run scenarios."
fi

# 2. Clone PX4-Autopilot source repo if not existing
PX4_DIR="$HOME/PX4-Autopilot"
if [ ! -d "$PX4_DIR" ]; then
    echo "[SIM] PX4-Autopilot repository not found. Downloading..."
    git clone --recursive https://github.com/PX4/PX4-Autopilot.git "$PX4_DIR"
else
    echo "[SIM] Found existing PX4-Autopilot codebase at $PX4_DIR"
fi

# 3. Export simulation paths
export PX4_SIM_SPEED_FACTOR=1.0
export PX4_GZ_WORLD=urban_canyon

# 4. Run SITL
echo "[SIM] Starting Gazebo SITL mission: hexacopter_tarot in urban canyon..."
cd "$PX4_DIR" || exit
make px4_sitl gazebo-classic_typhoon_h480
