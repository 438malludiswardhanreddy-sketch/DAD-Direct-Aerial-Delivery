# Project Overview - Direct Aerial Delivery (DAD)

## 1. Introduction & Academic Framework
This project report has been compiled as an undergraduate engineering research and development project, in partial fulfilment of the requirements for the award of the Degree of Bachelor of Engineering (B.E.).

The project, titled **Direct Aerial Delivery (DAD)**, addresses the last-mile logistics bottleneck. In rapidly growing Indian tier-2 smart cities like Solapur, traffic congestion, poor road layouts, and the rising overheads of traditional delivery methods make ground transport slow and inefficient. This research and development platform focuses on building an autonomous drone-based logistics framework to transport lightweight medical supplies and parcels across designated corridors.

---

## 2. System Architecture Design
The project is split into key functional subsystems:
*   **Onboard Autopilot Core**: Holybro Pixhawk 6C running the PX4 Autopilot firmware, responsible for real-time stabilisation, attitude estimation, and motor speed control.
*   **Onboard Companion Computer**: Raspberry Pi 5 module performing local range filtering and sensor fusion tasks.
*   **Sensor Fusion Node**: Merges distance inputs from a forward-facing Benewake TFmini LiDAR with video camera detection boundaries.
*   **Cloud Control Centre Backend**: FastAPI server handling telemetry reporting and client order dispatch.
*   **Control Centre Dashboard**: A glassmorphic web browser dashboard allowing supervisors to monitor flights and command emergency landing overrides.

---

## 3. Flight Mission Workflow
```
[Client Booking] -> [FastAPI Path Planner] -> [UIN & Flight Cleared (DigitalSky)]
                                                     │
                                                     ▼
[Emergency RTL Hub Locked] <- [Failsafe Check] <- [Takeoff]
            │
            ▼
[Autonomous Cruise] -> [Sensor Fusion Threat Check] -> [Obstacle Avoidance steering]
            │
            ▼
[Precision Descent at Destination] -> [Cargo Released] -> [Return & Recharge]
```

1.  **Order Booking**: The customer books a delivery via the app. The FastAPI server validates the request and schedules a flight path.
2.  **NPNT Flight Clearance**: Before takeoff, the system checks UIN registry compliance on the national DigitalSky platform.
3.  **Autonomous Launch & Cruise**: The hexacopter climbs to a cruise altitude of 45 metres. The companion computer continually executes the Kalman filter on LiDAR ranges.
4.  **Detect & Avoid Override**: If a power line or tree is identified within the flight vector, the guidance module alters the autopilot heading offset.
5.  **Failsafe Actions**: If heavy rain or low battery (<20%) is detected, the autopilot prioritises immediate landing at the nearest designated power hub.

---

## 4. DAD Validation Philosophy

The Direct Aerial Delivery (DAD) project follows a strict evidence-based engineering methodology. Every technical claim, performance metric, and validation result must be supported by traceable engineering evidence.

Validation within DAD is built upon four fundamental pillars:

$$\text{Photo} \rightarrow \text{Evidence} \quad\Big|\quad \text{Video} \rightarrow \text{Demonstration} \quad\Big|\quad \text{CSV / Log Data} \rightarrow \text{Measurements} \quad\Big|\quad \text{Report} \rightarrow \text{Analysis}$$

These pillars establish a complete chain of verification from system implementation to engineering conclusions.

### Evidence Hierarchy

*   **Photo $\rightarrow$ Evidence**: Photographs provide proof of hardware configuration, assembly status, wiring integrity, sensor installation, calibration procedures, and test environments.
*   **Video $\rightarrow$ Demonstration**: Videos provide visual confirmation that system behaviours occur as intended, including mission execution, obstacle avoidance, telemetry operation, emergency landing procedures, and autonomous flight actions.
*   **CSV / Log Data $\rightarrow$ Measurements**: Telemetry logs, MAVLink records, PX4 ULog files, calibration datasets, and benchmark outputs provide objective numerical measurements used for performance evaluation.
*   **Report $\rightarrow$ Analysis**: Engineering reports interpret the collected evidence, document procedures, explain observations, evaluate results, identify limitations, and propose future improvements.

### Traceability Principle

Every statement within DAD should be traceable to one or more forms of supporting evidence.

*   No performance claim without measurements.
*   No validation claim without logs.
*   No operational claim without demonstration.
*   No engineering conclusion without analysis.
