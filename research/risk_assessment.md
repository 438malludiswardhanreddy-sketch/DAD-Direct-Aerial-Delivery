# Risk Assessment and Hazard Analysis: Drone Delivery Operations
This document presents the risk assessment and hazard mitigation matrix developed for the Direct Aerial Delivery (DAD) project. It identifies operational, environmental, hardware, and software risks, proposing mitigations and backup protocols to ensure safe flight trials.

---

## 1. Risk Assessment Methodology
Risks are evaluated using a standard $5 \times 5$ Risk Matrix:
*   **Likelihood**: 1 (Rare) to 5 (Almost Certain)
*   **Severity**: 1 (Negligible) to 5 (Catastrophic)
*   **Risk Level (R)**: $\text{Likelihood} \times \text{Severity}$
    *   *Low Risk (1-6)*: Acceptable; monitored under standard operations.
    *   *Medium Risk (8-12)*: Mitigation required; software/hardware constraints must be verified.
    *   *High Risk (15-25)*: Unacceptable; flight trials must be suspended until mitigations are implemented.

---

## 2. Risk Matrix Table

| Hazard Description | Initial Likelihood | Initial Severity | Initial Risk (R) | Technical Mitigation Strategy | Residual Likelihood | Residual Severity | Residual Risk (R) |
| :--- | :---: | :---: | :---: | :--- | :---: | :---: | :---: |
| **Complete GNSS Signal Loss** (Urban Multipath / Jamming) | 3 | 4 | **12** | Implement Tightly-Coupled EKF & Visual-Inertial Odometry drift backup. Autopilot triggers Hover or Land-in-Place failsafe. | 2 | 2 | **4** |
| **Battery Depletion mid-flight** (Incorrect estimation) | 3 | 4 | **12** | Real-time Battery Manager triggers Return-to-Launch (RTL) at 20% capacity. Continuous estimation updates based on dynamic current draw. | 1 | 3 | **3** |
| **Obstacle Collision** (Dynamic bird/kite or static wire) | 4 | 4 | **16** | Combined YOLO vision and TFmini LiDAR obstacle avoidance. Steers opposite yaw offset (-40°) or climbs vertically (+3.5m). | 2 | 2 | **4** |
| **Structural Frame Failure** (Propeller/Motor structural crack) | 2 | 5 | **10** | Hexacopter frame configuration (Tarot 680Pro) provides motor redundancy. The PX4 mixer maintains attitude stability even if one motor fails. | 1 | 4 | **4** |
| **Adverse Weather / Precipitation** (Sudden heavy rainfall) | 3 | 4 | **12** | Environmental sensors monitor precipitation rate. If rainfall >8.0 mm/hr, system triggers an immediate diversion to the closest emergency pad. | 1 | 3 | **3** |
| **Telemetry Link Loss** (LTE network loss) | 4 | 3 | **12** | Dual-link architecture. If WebSocket link drops, the Holybro 915MHz telemetry radio provides backup. | 2 | 2 | **4** |

---

## 3. Detailed Mitigation Architectures

### 3.1. Loss of Control Link (Failsafe 0)
*   **Trigger**: Loss of both WebSocket and 915MHz radio heartbeats for more than **5.0 seconds**.
*   **Action**: Autopilot enters `HOLD` mode, hovering in place for 10.0 seconds. If connection is not re-established, the vehicle automatically engages `RTL` (Return-to-Launch).

### 3.2. Critical Battery Failsafe (Failsafe 1)
*   **First Alert (25%)**: Ground Control Station displays warning; telemetry rate increases.
*   **Failsafe Trigger (20%)**: Drone aborts mission path and executes an automatic return journey.
*   **Emergency Level (10%)**: If battery drops to 10% during return, drone overrides home coordinate target and performs a vertical descent at its current position to protect the airframe.

### 3.3. Weather Abort and Safe Havens (Failsafe 2)
*   **Trigger**: Onboard precipitation sensor reads $>8.0$ mm/hr or wind speed exceeds $12.0$ m/s for a continuous duration of **3.0 seconds**.
*   **Action**: The system queries the database for the nearest designated emergency landing location. It recalculates the shortest path, sets speed to 8.0 m/s, and diverts to land immediately.
