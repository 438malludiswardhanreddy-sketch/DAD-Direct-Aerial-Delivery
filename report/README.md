# B.E. Final Year Project Report Guidelines
This directory contains outlines and structural templates for writing the thesis, synopsis, and research paper drafts (Solapur University standard).

---

## 1. Project Synopsis Structure (`Synopsis.docx`)
*Target Length: 3-5 pages | Submitted in Semester I*

*   **Abstract**: High-level summary of the DAD simulation-validated UAV logistics prototype.
*   **Introduction & Problem Definition**: Current constraints of UAV last-mile delivery and GPS signal degradations.
*   **Objectives**: List key objectives (BOM planning, EKF perception, telemetry, failsafe algorithms).
*   **Proposed Methodology & Block Diagram**: Spatial calibrations and backend architectures.
*   **Expected Hardware BOM & Costing**: Tarot 680Pro specifications and budget in INR.
*   **Gantt Chart**: Semester timeline.
*   **Conclusion & References**: Academic prior art citations.

---

## 2. Final Project Report Chapter Layout (`Final_Report.docx`)
*Target Length: 80-120 pages | Submitted in Semester II*

*   **Preliminary Pages**: Title page, Certificate from Guide/HOD, Declaration, Acknowledgements, Abstract, Table of Contents, List of Figures, List of Tables.
*   **Chapter 1: Introduction**: Background, motivation, problem statement, objectives, and thesis organization.
*   **Chapter 2: Literature Review**: Survey of global/local planners, tightly-coupled state estimation, and vision-LiDAR fusion models.
*   **Chapter 3: System Architecture & Software Stack Design**: Functional details of PX4 autopilot, Pi 5 companion computer, MAVLink, FastAPI WebSocket, and MQTT services.
*   **Chapter 4: Sensor Fusion & Perception Mathematics**: 3D extrinsic calibrations, 2D focal projection, and EKF state transition/Jacobian matrix equations.
*   **Chapter 5: Autonomous Failsafe Logic**: Low battery RTH calculations, weather-abort voronoi partitioning, and geofencing limits.
*   **Chapter 6: Hardware Integration & Power Management**: Solder layouts, buck step-downs, and weights.
*   **Chapter 7: Simulation Scenario Validation & Results**: Performance metric tables, p95 latencies, packet sizes, and path deviations.
*   **Chapter 8: Conclusion & Future Scope**: Summary of work, limits, and steps for physical flight trials.
*   **References**: IEEE bibliography style.

---

## 3. IEEE Research Paper Sections (`IEEE_Paper.docx`)
*Target Length: 6-8 pages (Double column IEEE template)*

*   **Abstract**: Summary of the Vision-LiDAR EKF obstacle avoidance and weather-abort diversion system.
*   **I. Introduction**: Motivation, scope, and key contributions.
*   **II. Related Work**: Prior art in UAV navigation and low-cost depth estimation.
*   **III. System Design & Sensor Fusion**: Extrinsic coordinate equations and EKF Jacobian formulations.
*   **IV. Autonomous Decision and Failsafes**: Low battery RTL profiles and precipitation diversion algorithms.
*   **V. Simulation Experiments & Performance**: Latency tables, bandwidth throughput graphs, and path tracking accuracy metrics.
*   **VI. Conclusion & Future Work**: Wrap-up and hardware testing schedule.
*   **References**: IEEE numbered style.
