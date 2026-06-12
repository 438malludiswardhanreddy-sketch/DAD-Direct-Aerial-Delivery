# Telemetry Communication Validation Logs
This document details the testing protocols, signal strength benchmarks, transmission latencies, and link redundancy validation for the dual-link telemetry system (915MHz Radio and 4G/LTE WebSocket link).

---

## 1. Telemetry Test Protocol
*   **Setup**: The Tarot 680Pro companion computer (Raspberry Pi 5) is placed on a gimbal test stand. The Ground Control Station (GCS) is stationed at the control centre.
*   **Range Trials**: The drone is flown along a radial path up to 2.5 km (BVLOS corridor).
*   **Data Collected**: Received Signal Strength Indication (RSSI), packet loss rate (%), round-trip time (RTT) latency, and reconnection timeout periods.

---

## 2. Signal Strength and Range Benchmarks

### 2.1. 915MHz Telemetry Radio Link (Holybro Micro v3)
*   **Transmit Power**: 20 dBm (100 mW).
*   **Receiver Sensitivity**: -110 dBm.

| Distance (km) | Signal Strength (RSSI, dBm) | Packet Loss (%) | Simulation Status |
| :--- | :---: | :---: | :--- |
| **0.5 km** | -65 dBm | 0.0% | Simulation Placeholder |
| **1.0 km** | -78 dBm | 0.2% | Simulation Placeholder |
| **1.5 km** | -88 dBm | 1.1% | Simulation Placeholder |
| **2.0 km** | -94 dBm | 3.5% | Simulation Placeholder |
| **2.5 km (Max Range)** | -99 dBm | 8.2% | Simulation Placeholder (Signal edge) |

*   **Average Round-Trip Latency (915MHz Radio)**:
    *   *Target Metric*: <200 ms.
    *   *Simulation Placeholder*: 115 ms.

### 2.2. 4G/LTE WebSocket Connection
*   **Service Provider**: Local cellular network interface (Jio/Airtel 4G LTE).
*   **Average Cellular Latency (RTT)**:
    *   *Target Metric*: <120 ms.
    *   *Simulation Placeholder*: 78 ms.

---

## 3. Redundancy and Reconnection Timeout Limits

### 3.1. Link Swapping (Failsafe Verification)
The system must automatically handle loss of primary cellular connectivity by falling back to the 915MHz serial link.

*   **Loss Detection Timeout**:
    *   *Target Metric*: <3.0 seconds.
    *   *Simulation Placeholder*: 1.5 seconds.
*   **Reconnection Lock Latency (LTE re-association)**:
    *   *Expected Metric*: <10.0 seconds when cellular coverage returns.
    *   *Simulation Placeholder*: 6.4 seconds.
*   **Data Buffer Backlog Storage**:
    *   *Target Metric*: Local SQLite telemetry buffer must support **3600 frames** of offline records (at 1Hz) during coverage dropouts, pushing queued frames upon link re-establishment.
    *   *Simulation Placeholder*: Buffering tested successfully.
