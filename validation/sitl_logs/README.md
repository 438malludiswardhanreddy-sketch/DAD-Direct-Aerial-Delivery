# PX4 SITL Simulation Logs
This directory stores console outputs, boot sequences, and parameter logs captured from the PX4 Software-in-the-Loop (SITL) simulator.

---

## 1. PX4 SITL Boot Sequence log (Simulation Placeholder)
The following is a console log captured during the initialization of the PX4 flight controller shell (connecting to Gazebo Classic):

```text
INFO  [px4] Startup script: /etc/init.d-posix/rcS 0
INFO  [param] Selected parameter file: eeprom/parameters
INFO  [dataman] Unknown raw dataman file: /eeprom/dataman, creating new one.
INFO  [simulator] Waiting for simulator connection on TCP port 4560...
Simulator connected on TCP port 4560.
INFO  [commander] LED: pattern set to 2 (Blue heartbeat)
INFO  [mavlink] mode: Normal, data rate: 100000 B/s on udp port 14556 to 127.0.0.1:14550
INFO  [mavlink] mode: Onboard, data rate: 120000 B/s on udp port 14540 to 127.0.0.1:14540
INFO  [commander] Home position set to: 17.659021, 75.905912, 478.5m AGL
INFO  [ekf2] EKF2 IMU 0 primary.
INFO  [ekf2] EKF2 GPS 0 primary.
INFO  [commander] armed by onboard telemetry bridge.
```

---

## 2. Parameter Configurations
Key PX4 parameters configured for DAD flight operations:
*   `NAV_RTL_ALT`: 30.0m (Return-to-home altitude)
*   `COM_RC_IN_MODE`: 1 (Flight controller rejects arming without telemetry link heartbeat)
*   `GF_ACTION`: 2 (Polygonal Geofence violation triggers Return-to-Launch)
*   `MPC_XY_VEL_MAX`: 12.5 m/s (Maximum horizontal cruise speed)
