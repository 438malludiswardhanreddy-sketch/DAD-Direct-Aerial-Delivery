# System Requirements Specification

## 1. Hardware Subsystems
### 1.1 Airframe & Propulsion
*   **Chassis**: Tarot 680Pro Carbon Fibre Hexacopter Frame.
*   **Motors**: 6x 380KV Brushless Outrunner Motors (e.g. T-Motor MN4014) to enable heavy payload flight.
*   **ESC**: 6x 40A Electronic Speed Controllers with real-time temperature and current telemetry feedback.
*   **Propellers**: 13x5.5 inch carbon fibre folding propellers.

### 1.2 Avionics & Processing Units
*   **Autopilot**: Holybro Pixhawk 6C Flight Controller running PX4 Autopilot v1.14.
*   **Companion Processor**: Raspberry Pi 5 (8GB LPDDR5 RAM) running Ubuntu 22.04 LTS.
*   **Positioning**: Dual F9P RTK-GPS receiver modules for sub-decimetre localization accuracy.

### 1.3 Sensor Arrays
*   **Rangefinder**: Benewake TFmini-S LiDAR sensor (Forward-facing, range up to 12 metres).
*   **Visual Stream**: Sony IMX219 wide-angle camera module.
*   **Environment Sensor**: Digital micro precipitation and wind speed sensors.

---

## 2. Software Subsystems & Libraries
### 2.1 Embedded & Onboard Code
*   **Languages**: C++17 (for PX4 custom failsafe modules) and Python 3.10 (for companion computer tasks).
*   **Bindings**: MAVSDK-Python for serial API calls.
*   **Filtres**: Custom NumPy-based Kalman range filters for LiDAR noise reduction.

### 2.2 Telemetry Server Backend
*   **Framework**: FastAPI for asynchronous websocket telemetry loops.
*   **Logger**: SQLite database storing active flight coordinate paths.
*   **Hosting**: Dockerized container configuration.

### 2.3 Visual Interface
*   **Design Framework**: Glassmorphism dashboard layout built with HSL CSS variables, Leaflet map tiles, and HTML5 Canvas.
