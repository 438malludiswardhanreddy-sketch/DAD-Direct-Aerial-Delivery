# Sensor Calibration Parameters
This directory stores parameter logs, sensor bias values, and calibration coefficients calculated from physical hardware tests.

---

## 1. Autopilot IMU & Magnetometer Calibration Logs
Calibration parameters configured in PX4 using QGroundControl:

### 1.1. Accelerometer Calibration
*   **Scale Factors (X, Y, Z)**:
    *   *Simulation Placeholder*: `1.0024`, `0.9982`, `1.0015`
*   **Offsets (m/s²)**:
    *   *Simulation Placeholder*: `0.024`, `-0.015`, `0.112`

### 1.2. Gyroscope Calibration
*   **Offsets (rad/s)**:
    *   *Simulation Placeholder*: `<0.0015` across all axes.

### 1.3. Magnetometer Calibration
*   **Offsets (mG)**:
    *   *Simulation Placeholder*: `12.4`, `-18.2`, `45.1`

---

## 2. Sensor Offsets & Alignments
*   **LiDAR Range Offset**:
    *   *Simulation Placeholder*: `0.05`m correction offset.
*   **Camera Extrinsic Matrix (Rotation offset)**:
    *   *Simulation Placeholder*: `Roll=0.0°`, `Pitch=1.5°` (downward tilt adjustment), `Yaw=0.0°`.
