# RTK GNSS Calibration & Accuracy Logs
This document details the accuracy testing, multipath reflection analyses, and lock benchmarks for the dual Holybro F9P RTK GPS setup.

---

## 1. GNSS Test Protocol
*   **Setup**: The Tarot 680Pro hexacopter is placed on a stationary survey benchmark point (Solapur R&D centre coordinates: `17.659021, 75.905912`) with a clear sky view. The RTK Base Station is configured and broadcasts RTCM 3.X corrections over the telemetry link to the onboard GPS receiver.
*   **Duration**: Continuous tracking for 30 minutes.
*   **Parameters Logged**: Latitude, longitude, altitude, GPS lock state (3D Fix, RTK Float, RTK Fix), and horizontal/vertical dilution of precision (HDOP, VDOP).

---

## 2. Lock State and Precision Benchmarks

### 2.1. Satellite Tracking Metrics
*   **Average Satellites Tracked**:
    *   *Target Metric*: >18 satellites (GPS + GLONASS + Galileo + BeiDou).
    *   *Simulation Placeholder*: 24 satellites.
*   **Time to First Fix (TTFF) — Cold Start**:
    *   *Target Metric*: <45.0 seconds.
    *   *Simulation Placeholder*: 32.5 seconds.
*   **RTK Fix Convergence Time**:
    *   *Expected Metric*: <120.0 seconds from base station lock.
    *   *Simulation Placeholder*: 85.0 seconds.

### 2.2. Deviation Metrics (Stationary Bench Test)

| GNSS Mode | Target Horizontal Precision (CEP) | Target Vertical Precision (CEP) | Simulated Average Deviation |
| :--- | :---: | :---: | :---: |
| **Standard GPS (No RTK)** | <2.5 m | <5.0 m | 1.82 m (Simulation Placeholder) |
| **RTK Float (Corrections lock)** | <0.5 m | <1.0 m | 0.28 m (Simulation Placeholder) |
| **RTK Fix (Centimeter lock)** | <0.02 m | <0.05 m | 0.012 m (Simulation Placeholder) |

---

## 3. Multipath and Obstruction Validation (Urban Canyon Simulation)
Multipath reflections from surrounding concrete walls in urban canyon environments degrade GNSS accuracy. 

*   **Multipath Rejection Latency**:
    *   *Target Metric*: The EKF must reject outliers (sudden coordinate jumps > 2.0m) within **100ms** by de-weighting GPS covariance matrices and relying on visual-inertial odometry.
    *   *Simulation Placeholder*: 60ms correction time.
*   **Dual GPS Heading Precision**:
    *   *Expected Metric*: Moving-baseline RTK GPS provides heading accuracy of **<0.5°** at 0.5m antenna separation.
    *   *Simulation Placeholder*: 0.38° heading deviation.
