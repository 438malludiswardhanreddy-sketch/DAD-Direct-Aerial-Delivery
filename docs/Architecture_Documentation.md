# DAD Architecture Documentation

## 1. System Topology & Layers
The platform is organized into three principal layers:
*   **Hardware and Avionics**: Tarot 680Pro hexacopter chassis, Pixhawk 6C autopilot (running PX4), Raspberry Pi 5 companion computer, Benewake TFmini LiDAR, and USB wide-angle camera.
*   **Edge Processing**: Python-based ROS 2 nodes executing Kalman state filters and dynamic yaw/altitude trajectory offsets.
*   **Cloud Control Gateway**: Asynchronous FastAPI endpoints managing database logging and WebSocket telemetry streams to Leaflet dashboard clients.

---

## 2. Telemetry and Security Handshakes
1.  **JWT Verification**: Companion processors authenticate via `POST /api/v1/drone/auth` on boot. Telemetry uploads require a bearer token header.
2.  **MAVLink Signing**: Payload frames between the companion computer and Pixhawk core are signed using HMAC-SHA256 hashes to prevent spoofing.
3.  **Failsafes**: Loss of telemetry heartbeat for >3 seconds automatically triggers autopilot Return-to-Home (RTL).
