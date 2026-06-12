# Demonstration Video Recording Guide
This guide provides the specifications and recording layouts to capture screen recordings of the DAD system, verifying software-in-the-loop (SITL) correctness.

---

## 1. Video Asset Specifications

| Video Filename | Target Duration | Interface Layout | Scenario Actions to Record |
| :--- | :---: | :--- | :--- |
| **SITL_demo.mp4** | ~90 seconds | QGroundControl + Gazebo split | Takeoff, path cruising across Solapur coordinates, auto-landing. |
| **bird_avoidance.mp4** | ~45 seconds | Gazebo + YOLO console logs | Drone cruising, bird object detection box trigger, evasive bank maneuver. |
| **emergency_landing.mp4** | ~60 seconds | Gazebo + Precipitation dashboard | Storm simulation trigger, nearest emergency site lookup, automatic landing diversion. |
| **dashboard_demo.mp4** | ~90 seconds | Web Dashboard UI | WebSocket telemetry graphs updating in real time, geofence violations, failsafe alarms. |

---

## 2. Recording Layout Configurations

### 2.1. Dual Window Capture (SITL, Bird and Wire Avoidance)
To capture both physical simulation states and telemetry logs:
*   **Resolution**: 1920x1080 (1080p) at 30 fps or 60 fps.
*   **Layout**: Place the Gazebo 3D simulation on the left half of the screen (960x1080) and the terminal logs / console output on the right half (960x1080).
*   **Tooling**: Use OBS Studio or equivalent open-source recording software.

### 2.2. Web Dashboard Capture
*   **Resolution**: 1920x1080.
*   **Layout**: Full-screen browser window showing the Leaflet control room map and live telemetry chart feeds.
*   **Actions**: Show drone status transitions from `DISARMED` to `TAKEOFF`, `CRUISE`, and `RTH`. Trigger a manual geofence breach to show the critical alert banner.

---

## 3. Video Compression and Codec SOP
To ensure files remain lightweight for repository uploads:
*   **Container Format**: MP4 (`.mp4`).
*   **Video Codec**: H.264 (AAC audio, if any).
*   **Compression Profile**: Constant Rate Factor (CRF) set to `23` or `24` in FFmpeg.
*   **Encoding Command**:
    ```bash
    ffmpeg -i raw_recording.mkv -vcodec libx264 -crf 24 -acodec aac -b:a 128k compressed_output.mp4
    ```
*   **Storage Location**: Videos should be stored under the `demo/` folder or uploaded as assets/releases on the remote GitHub repository to avoid bloating the git history.
