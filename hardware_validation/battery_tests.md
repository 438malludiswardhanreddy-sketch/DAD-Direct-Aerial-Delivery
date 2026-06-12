# Battery Management & Power Calibration Logs
This document details the load tests, current sensor calibrations, cell balance metrics, and failsafe voltage triggers for the PM02 V3 Power Module and Tattu 6S 16000mAh LiPo battery.

---

## 1. Power Calibration Protocol
*   **Setup**: Connect the Tarot 680Pro hexacopter to a regulated DC electronic load bank. 
*   **Measurement**: Calibrate the Pixhawk voltage and current sensing coefficients using a high-precision digital multimeter (Fluke 179) connected in series.
*   **Steps**: Increase the current draw from 1.0A (idle companion computer state) to 80.0A (simulated maximum hexacopter thrust load) in steps of 10.0A.

---

## 2. Sensor Accuracy and Calibration

### 2.1. Voltage Sensing Accuracy
*   **Input Range**: 18.0V to 25.2V (6S LiPo operational range).
*   **Voltage Sensing Error**:
    *   *Target Metric*: <0.1V deviation.
    *   *Simulation Placeholder*: 0.04V.

### 2.2. Current Sensing Calibration
*   **Operational Range**: 0.0A to 120.0A.
*   **Current Sensing Error (Low load: <10A)**:
    *   *Expected Metric*: <0.5A error.
    *   *Simulation Placeholder*: 0.22A.
*   **Current Sensing Error (High load: 10A to 80A)**:
    *   *Target Metric*: <1.5% of true current.
    *   *Simulation Placeholder*: 1.1% (average 0.65A deviation).

---

## 3. Battery Discharge Profile and Failsafe Thresholds

### 3.1. Cell Voltage Failsafe Actions
The onboard `battery_manager.cpp` firmware enforces two primary low-power safety thresholds:

| Warning Level | Cell Voltage Threshold | Battery Capacity | Failsafe Action |
| :--- | :---: | :---: | :--- |
| **Low Battery Alert** | 3.6V per cell (21.6V total) | 25.0% | QGroundControl warning; dashboard flashes alert |
| **Critical Failsafe (RTL)** | 3.5V per cell (21.0V total) | 20.0% | Mission abort; hexacopter returns to home immediately |
| **Emergency Landing** | 3.4V per cell (20.4V total) | 10.0% | Immediate vertical descent at current coordinates |

### 3.2. Discharge Curve Validation Metrics
*   **Expected Internal Resistance**: <2.5 m$\Omega$ per cell (Target Metric).
*   **Estimated Thermal Dissipation (LiPo temperature under 60A continuous draw)**:
    *   *Expected Metric*: <45.0 °C.
    *   *Simulation Placeholder*: 38.5 °C (with active carbon airflow ducts).
*   **Dynamic Voltage Sag Compensation**:
    *   *Target Metric*: Filter transient sag spikes (lasting < 2.0 seconds) to prevent false RTL triggers.
    *   *Simulation Placeholder*: Verified 3.0 second moving average filter.
