# System Requirements Specification

## 1. Hardware Requirements
### 1.1 Drone Frame & Propulsion
*   **Airframe**: Tarot 680Pro Carbon Fiber Hexacopter.
*   **Motors**: 6x brushless motors (380KV to 410KV, e.g., T-Motor MN4014).
*   **ESC**: 6x 40A Electronic Speed Controllers with ESC telemetry support.
*   **Propellers**: 13-inch or 14-inch carbon fiber folding propellers.

### 1.2 Flight Controller & Companion Computer
*   **Autopilot**: Pixhawk 6C or Orange Cube (running PX4 Autopilot firmware).
*   **Companion Computer**: Raspberry Pi 5 (8GB RAM) or NVIDIA Jetson Orin Nano (8GB developer kit).
*   **GPS**: Dual RTK-GPS receiver modules (e.g., Holybro M9N or F9P) for centimeter-level coordinates.

### 1.3 Sensors
*   **Obstacle Sensor**: Benewake TFmini-S or TF390 LiDAR sensor.
*   **Camera**: Sony IMX219 camera module or wide-angle USB camera.
*   **Environment Sensor**: Digital micro rain/humidity sensor.

---

## 2. Software Requirements
### 2.1 Embedded & Onboard Software
*   **Autopilot OS**: PX4 Autopilot v1.14+.
*   **Companion OS**: Ubuntu 22.04 LTS (Server Edition).
*   **APIs**: MAVSDK-Python or pymavlink for control communication.
*   **AI Frameworks**: PyTorch, OpenCV, TensorRT, YOLOv11-nano.

### 2.2 Backend & Telemetry Server
*   **Runtime**: Python 3.10+.
*   **Framework**: FastAPI for asynchronous telemetry endpoints.
*   **Database**: PostgreSQL or SQLite for storing mission logs and drone configurations.
*   **Real-time Protocols**: WebSockets for low-latency dashboard updates.

### 2.3 Dashboard UI
*   **Frontend**: Vanilla HTML5, Canvas, Leaflet.js, HSL-based CSS.
*   **Visual Style**: Sleek modern dark mode (glassmorphism/translucent panels).
