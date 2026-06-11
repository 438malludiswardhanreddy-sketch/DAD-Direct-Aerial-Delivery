# Security Threat Model & Safeguards

## 1. MAVLink Interception & Spoofing
*   **Threat**: Attackers intercept MAVLink signals on 915MHz or 5G telemetry channels, injecting commands to hijack flight path controls (e.g. forced landing, redirection).
*   **Impact**: Critical. Loss of asset or cargo; safety hazard.
*   **Safeguards**:
    *   Deploy **Secure MAVLink** (MAVLink v2 Signing). All telemetry frames require an SHA-256 signature hash containing a shared secret key configured on both companion computer and ground control station.
    *   Automatic RTL (Return-To-Launch) failsafe triggered immediately upon connection validation loss exceeding 3.0 seconds.

---

## 2. API / Websocket Authorization Abuse
*   **Threat**: Unauthorized requests sent to cloud backend server endpoint `POST /api/v1/orders` or telemetry sockets to trigger fake deliveries or drain batteries.
*   **Impact**: High. Operational disruption.
*   **Safeguards**:
    *   Enforce **JWT Token Validation** on all endpoints. Companion computers authenticate during startup and receive a transient session token.
    *   Strict IP rate-limiting policies for telemetry upload APIs.

---

## 3. GPS Spoofing & Signal Jamming
*   **Threat**: Attacker broadcasts fake GPS signals indicating the drone is at a different location.
*   **Impact**: High. Navigation error, potential crash.
*   **Safeguards**:
    *   Integrate **dual redundant RTK-GPS** receivers. Discrepancies between modules exceeding 1.5 meters trigger an immediate hover/failsafe mode.
    *   Compare GPS movements with IMU accelerometer integrations. If GPS indicates high-velocity movements mismatching IMU telemetry, revert control to Optical Flow navigation and land immediately.
