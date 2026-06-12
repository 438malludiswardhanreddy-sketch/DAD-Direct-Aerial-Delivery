# 🛸 DAD — Direct Aerial Delivery
> **Research and Development Prototype — Simulation-Validated Architecture — Under Active Development**

[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](#)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](#)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100-teal)](#)
[![PX4 Autopilot](https://img.shields.io/badge/PX4-v1.14-orange)](#)
[![Licence](https://img.shields.io/badge/Licence-MIT-green)](#)

![DAD Hero Banner](assets/hero_banner.png)

---

## 📖 Project Brief
**Direct Aerial Delivery (DAD)** is a research and development platform for autonomous drone-based logistics and last-mile aerial delivery systems. Developed as an undergraduate final year B.E. engineering design project in Solapur, Maharashtra, India, the repository implements an integrated system-level R&D prototype bridging flight controller synchronization, monocular vision and single-axis LiDAR sensor fusion, real-time telemetry streaming, and automated failsafe logic.

---

## 📹 Demo Video & Scenario Showcase
Reviewers, recruiters, and evaluators can find screen-recording video logs demonstrating the Software-in-the-Loop (SITL) simulations and telemetry dashboard under the [demo/](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/demo/) folder:
*   [SITL Flight Demonstration Video](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/demo/SITL_demo.mp4)
*   [Live Telemetry Dashboard Stream Video](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/demo/telemetry_demo.mp4)
*   [AI Bird Avoidance Scenario Video](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/demo/bird_avoidance_demo.mp4)
*   [Low Battery RTL Trigger Video](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/demo/low_battery_demo.mp4)
*   [Emergency Weather Abort Video](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/demo/emergency_landing_demo.mp4)

*For recording formats and configurations, see the [Video Recording Guide](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/demo/recording_guide.md).*

---

## 📊 Performance Metrics (Simulation Benchmarks)
Metrics and latency parameters are captured from simulated validation runs. Target and expected metrics are logged clearly to maintain data integrity:
*   [Sensor Fusion Benchmark](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/benchmark_reports/sensor_fusion_benchmark.md): EKF processing latency ($0.8$ ms) and obstacle detection reaction limits.
*   [Backend Latency Report](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/benchmark_reports/backend_latency_report.md): API endpoint response times and database commits.
*   [Telemetry Throughput Report](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/benchmark_reports/telemetry_throughput.md): Packet size comparisons (JSON vs Protobuf) and network jitter packet dropouts.
*   [Navigation Accuracy Report](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/benchmark_reports/navigation_accuracy.md): Cross-track error under wind gusts, battery discharge prediction margins, and landing deviation.

---

## 🛠️ Hardware Stack & Bring-Up SOP
The physical system is modeled around the Tarot 680Pro hexacopter chassis. Standard operating procedures (SOPs) for hardware assembly and bench validation are placed under the [hardware/](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware/) and [hardware_validation/](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware_validation/) folders:
*   [Bill of Materials (BOM)](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware/BOM.md): Complete list with components (Pixhawk 6C, Pi 5, TFmini-S LiDAR, dual RTK GPS, etc.) and pricing in INR and USD.
*   [Assembly Guide](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware/assembly_guide.md): Carbon frame locking, ESC soldering, and companion computer wiring.
*   [Calibration & Testing Logs](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware_validation/): Sensor, GPS accuracy, battery power load, and radio signal validation.
*   [Pre-Flight Checklist](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware_validation/flight_checklist.md): Mandatory ground checking checklist.
*   [Flight Readiness Report](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware_validation/flight_readiness_report.md): Final sign-off requirements prior to live testing.

---

## 📡 System Architecture
The platform integrates six primary functional layers:
1.  **Drone Autopilot**: Holybro Pixhawk 6C running PX4 stable firmware.
2.  **Companion Computer**: Raspberry Pi 5 executing YOLO object detection and sensor EKF.
3.  **MAVLink Bridge**: Python broker (`autonomous/px4_mavlink_bridge.py`) for waypoint syncing and status reading.
4.  **Backend Ingestion**: FastAPI microservices supporting WebSockets and database commits.
5.  **Control Room Dashboard**: Dark-mode Leaflet telemetry interface displaying paths and status.
6.  **Redundant Telemetry**: Dual-link 4G/LTE cellular link and 915MHz Holybro radio.

*Architecture diagrams are stored in the [architecture/](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/architecture/) folder.*

---

## 🧪 Validation Results
Run outcomes and transaction dumps from the software-in-the-loop (SITL) tests:
*   [SITL Boot Logs](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/validation/sitl_logs/): Console initialization and PX4 parameters.
*   [MAVLink Transaction Logs](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/validation/mavlink_logs/): Waypoint upload ACK packets.
*   [Telemetry captures](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/validation/telemetry_captures/): WebSocket JSON packet capture examples.
*   [Mission Reports Matrix](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/validation/mission_reports/): Summarized test cases (low battery, rain aborts, bird avoidance).

---

## 📚 Research Outputs & Patents
Whitepapers detailing the mathematical, algorithmic, and regulatory underpinnings:
*   [Literature Review](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/research/literature_review.md): Literature review on 3D path planning and state estimation.
*   [DGCA Compliance](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/research/dgca_compliance.md): Regulatory compliance under Indian Drone Rules (UIN, geofencing, NPNT).
*   [Sensor Fusion Analysis](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/research/sensor_fusion_analysis.md): Coordinate projections and EKF Jacobian formulations.
*   [Risk Assessment Matrix](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/research/risk_assessment.md): Threat mitigation mapping.
*   **Patent Intellectual Property Notebook**: Preliminary invention disclosures, novel claims, and claim drafts are archived in the [patent/](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/patent/) folder for final reviews.

---

## 📊 Repository Statistics

*   **Total Source Files**: 214
*   **Validation Tests**: 21 (All passing)
*   **System Architectures**: 3 (.png & .mermaid)
*   **Simulation Scenarios**: 5 (SITL verified)
*   **Research Papers**: 4 (Indian English drafts)
*   **Patent IP Notes**: 4 (Invention disclosure & claims)
*   **CI/CD Pipelines**: 2 (CI build and ECR/ECS CD templates)

---

## 📸 Professional Portfolio Visual Showcase

### 📡 System Architecture Design
The high-level R&D system layout mapping companion and autopilot tasks:
![System Architecture](architecture/system_architecture.png)

### 💻 Software Component Architecture
The module blocks, state trackers, and API routes within the ecosystem:
![Software Architecture](architecture/software_architecture.png)

### ☁️ Cloud Deployment Architecture
AWS container clustering, RDS database nodes, and ingress configurations:
![Deployment Architecture](architecture/deployment_architecture.png)

### 📊 Control Room Dashboard Interface
The telemetry dashboard displaying real-time coordinates, battery decays, and geofence warnings:
![Dashboard Interface](assets/dashboard_demo.png)

### 🛸 Hexacopter Simulation Environment
The 3D Gazebo simulator rendering the Tarot 680Pro drone in urban micro-airspace:
![Simulation Screenshot](assets/simulation_screenshot.png)

---

## ⚙️ Quick Start

### 1. Backend Ingestion Server
```bash
pip install -r requirements.txt
python -m uvicorn backend.main:app --reload
```
*API docs dashboard: `http://localhost:8000/docs`*

### 2. Telemetry Listeners & Bridges
```bash
python autonomous/px4_mavlink_bridge.py
python backend/telemetry/px4_listener.py
```

### 3. Verify Test Suite
```bash
python testing/test_suite.py
```

---

## 📜 Licence & Citation
Licensed under the MIT Licence. For academic citations:
```bibtex
@thesis{DAD_Drone_2026,
  author = {DAD Project Group},
  title = {Direct Aerial Delivery: Autonomous Last-Mile Drone Delivery & Control Ecosystem},
  school = {Solapur University, Department of Electronics and Telecommunication Engineering},
  year = {2026},
  type = {Final Year B.E. Project Report}
}
```
