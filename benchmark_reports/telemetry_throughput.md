# Telemetry Throughput Report
This document evaluates the communication link budget, packet throughput, and packet-loss rate metrics for the Direct Aerial Delivery (DAD) system telemetry pipeline.

---

## 1. Communication Architecture
Telemetry operates on a dual-link architecture:
1.  **Primary Link (4G/LTE)**: Secure WebSocket connection (TCP/TLS) between the Raspberry Pi 5 companion computer and the FastAPI backend.
2.  **Backup Link (915MHz Radio)**: Holybro Micro Telemetry Radio (MAVLink over point-to-point serial link).

---

## 2. Bandwidth and Throughput Metrics

### 2.1. Telemetry Packet Structure
A standard telemetry packet consists of GPS coordinates, battery level, pitch/roll/yaw, system health flags, and current flight mode.
*   **Average Raw JSON Packet Size**: 280 Bytes
*   **Average Compressed Protocol Buffer Packet Size**: 110 Bytes (Expected Metric)

### 2.2. Transmission Rate and Bandwidth
Bandwidth measurements are simulated at standard update frequencies (10Hz telemetry stream).

| Connection Type | Update Frequency | Target Bandwidth | Expected Bandwidth |
| :--- | :--- | :---: | :---: |
| **WebSocket (JSON)** | 10 Hz | <15.0 KB/s | 2.8 KB/s (Simulation Placeholder) |
| **WebSocket (Protobuf)** | 10 Hz | <5.0 KB/s | 1.1 KB/s (Simulation Placeholder) |
| **MAVLink (Radio)** | 5 Hz | <2.0 KB/s | 0.9 KB/s (Simulation Placeholder) |

---

## 3. Telemetry Link Reliability

### 3.1. Packet Loss and Dropouts
Simulated under varying network latency (simulate urban canyon signal drops).

| Simulated Network Condition | Target Packet Loss | Expected Packet Loss | Simulation Status |
| :--- | :--- | :---: | :--- |
| **Ideal Link (0ms latency, 0% drop)** | 0.0% | 0.0% | Simulation Placeholder |
| **Moderate Interference (100ms jitter, 2% drop)** | <1.0% | 0.2% | Simulation Placeholder |
| **Severe Interference (500ms delay, 15% drop)** | <5.0% | 3.5% | Simulation Placeholder |

### 3.2. Telemetry Delay
Telemetry delay is defined as the time between a physical sensor update on the drone and the rendering of that update on the QGroundControl/Web dashboard.

*   **Expected Telemetry Delay (WebSocket over LTE)**:
    *   *Target Metric*: <150 ms
    *   *Simulation Placeholder*: ~80 ms
*   **Expected Telemetry Delay (915MHz Telemetry Radio)**:
    *   *Target Metric*: <250 ms
    *   *Simulation Placeholder*: ~120 ms

---

## 4. Key Findings
1.  **Serialization Efficiency**: Transitioning from JSON payloads to Google Protocol Buffers yields a **60.7% reduction** in raw data throughput (Expected Metric).
2.  **Failsafe Reconnection**: In the event of a total network dropout, the companion computer buffers telemetry packets locally. The buffer supports up to **60 minutes** of offline telemetry logs before wrapping (Target Metric).
