# Sensor Fusion Benchmark Report
This report outlines the latency and accuracy benchmarks of the Direct Aerial Delivery (DAD) sensor fusion subsystem, which integrates LiDAR telemetry, optical sensor feeds, and IMU data to estimate state and detect obstacle vectors.

---

## 1. Benchmarking Methodology
The fusion engine combines high-rate IMU readings (200Hz), Holybro F9P RTK GNSS positions (10Hz), and Benewake TFmini-S LiDAR range measurements (100Hz) using an Extended Kalman Filter (EKF) implemented in C++ and Python. Benchmarking was performed using simulated sensor streams under typical flight profiles.

---

## 2. Sensor Fusion Performance Metrics

### 2.1. Processing Latency
The time taken to ingest, parse, align, and fuse raw sensor packets into the estimated state vector.

| Metric | Metric Type | Target Value | Simulated Value |
| :--- | :--- | :---: | :---: |
| **LiDAR Parsing Latency** | Target Metric | <2.0 ms | 1.1 ms (Simulation Placeholder) |
| **EKF Update Step Latency** | Expected Metric | <1.5 ms | 0.8 ms (Simulation Placeholder) |
| **Optical Obstacle Detection Latency** | Expected Metric | <15.0 ms | 11.2 ms (Simulation Placeholder) |
| **State Vector Publish Delay** | Target Metric | <1.0 ms | 0.5 ms (Simulation Placeholder) |

### 2.2. State Estimation Accuracy
Discrepancy between the estimated state vector (fused coordinates and velocities) and the ground truth in the simulation environment.

| Dimension | Metric Type | Expected Max Error (Static) | Expected Max Error (Dynamic) |
| :--- | :--- | :---: | :---: |
| **X-Position (Latitude)** | Expected Metric | <0.02 m (RTK Lock) | <0.10 m (RTK Lock) |
| **Y-Position (Longitude)** | Expected Metric | <0.02 m (RTK Lock) | <0.10 m (RTK Lock) |
| **Z-Position (Altitude)** | Expected Metric | <0.05 m (LiDAR Fused) | <0.15 m (LiDAR Fused) |
| **Yaw Alignment** | Target Metric | <1.0 deg | <2.5 deg |

---

## 3. Collision Prediction Performance
Evaluating the accuracy of predicting imminent collisions (e.g., bird encounters or power lines) based on fused obstacle telemetry.

*   **Obstacle Detection Latency (Total)**:
    *   *Target Metric*: <120.0 ms
    *   *Simulation Placeholder*: ~95.0 ms
*   **Collision Prediction Accuracy (F1-Score)**:
    *   *Expected Metric*: 0.94 (Simulation Placeholder based on synthetic datasets)
    *   *Target Metric (Physical)*: >0.95 under clear weather conditions
*   **False Positive Rate (FPR)**:
    *   *Expected Metric*: 3.2% (Simulation Placeholder)

---

## 4. Key Engineering Observations
1.  **Vibration Sensitivity**: EKF covariance metrics show high sensitivity to simulated motor vibrations. Physical assembly must include high-quality silicone gel damping to prevent IMU signal degradation.
2.  **LiDAR Dropouts**: Temporary LiDAR signal losses (due to high roll angles during banks) are mitigated by relying on state extrapolation via IMU integration. The maximum duration of stable extrapolation is estimated at **350 ms** (Target Metric).
