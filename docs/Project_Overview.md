# Project Overview - Direct Aerial Delivery (DAD)

## 1. Introduction & Academic Framework
This project report has been compiled by the final year project group of the **Department of Electronics and Telecommunication Engineering, Solapur University**, in partial fulfilment of the requirements for the award of the Degree of Bachelor of Engineering (B.E.).

The project, titled **Direct Aerial Delivery (DAD)**, addresses the last-mile logistics bottleneck. In rapidly growing Indian tier-2 smart cities like Solapur, traffic congestion, poor road layouts, and the rising overheads of traditional delivery methods make ground transport slow and inefficient. This research and development platform focuses on building an autonomous drone-based logistics framework to transport lightweight medical supplies and parcels across designated corridors.

---

## 2. System Architecture Design
The project is split into key functional subsystems:
*   **Onboard Autopilot Core**: Holybro Pixhawk 6C running the PX4 Autopilot firmware, responsible for real-time stabilization, attitude estimation, and motor speed control.
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
