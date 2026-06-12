# Prior Art Review
This document logs prior patent publications and academic literature, highlighting the differentiators of the DAD system.

---

## 1. Relevant Patent Registrations

### 1.1. US Patent US10452062B2: "Unmanned aerial vehicle obstacle avoidance system"
*   **Assignee**: SZ DJI Technology Co Ltd
*   **Summary**: Discloses an obstacle avoidance system using multiple stereoscopic cameras and ultrasonic sensors to construct a local 3D map.
*   **DAD Differentiator**: DJI relies on stereo depth estimation (which requires high processing power on the companion card) and ultrasonic rangefinders (which have a short range of <5m). DAD uses a single-beam LiDAR (up to 12m range) combined with 2D YOLO classification, reducing weight and computational costs.

### 1.2. US Patent US9823661B2: "Methods and systems for safe landing of unmanned aerial vehicles"
*   **Assignee**: Amazon Technologies Inc
*   **Summary**: Discloses emergency landing procedures where a drone evaluates the ground terrain using cameras to find a flat landing area.
*   **DAD Differentiator**: Amazon's method requires real-time 3D terrain reconstruction (which is prone to errors during heavy rain or low light). DAD uses pre-registered coordinates of secure emergency landing platforms combined with infrared precision beacon alignment, ensuring high reliability during bad weather.

---

## 2. Academic Literature Comparison

### 2.1. "Monocular camera and 1D LiDAR fusion for autonomous flight"
*   **Analysis**: Existing academic research (e.g., in IEEE Robotics letters) focuses on indoor SLAM (Simultaneous Localization and Mapping). 
*   **DAD Differentiator**: DAD integrates this sensor configuration with PX4 autopilot failsafes and DGCA geofencing rules, targeting outdoor, urban package delivery.
