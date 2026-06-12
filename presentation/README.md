# B.E. Final Year Project Presentation Outlines
This directory contains presentation templates and guidelines for undergraduate engineering project evaluations (Solapur University standard).

---

## 1. Project Proposal Outline (`Project_Proposal.pptx`)
*Target Duration: 10 mins | Audience: Internal Department Panel*

*   **Slide 1: Title Slide**: Project title (Direct Aerial Delivery), group members, supervisor name, department, and institution.
*   **Slide 2: Introduction**: Problem definition of last-mile logistics (congestion, cost, delivery delays).
*   **Slide 3: Literature Survey**: Differentiators from existing UAV research and battery RTH failsafes.
*   **Slide 4: Project Objectives**: Small Category MTOW constraints, vision-LiDAR EKF, and DGCA NPNT compliance.
*   **Slide 5: Proposed Methodology**: Block diagram of companion Pi 5, Pixhawk 6C, and FastAPI WebSocket pipeline.
*   **Slide 6: Hardware BOM**: Tarot 680Pro frame and Holybro sensor list (in INR).
*   **Slide 7: Project Plan & Gantt Chart**: Milestones from simulation validations to hardware assembly.
*   **Slide 8: Expected Outcomes & References**: Simulation validations and flight checklists.

---

## 2. Mid-Review Outline (`Mid_Review.pptx`)
*Target Duration: 15 mins | Audience: Project Assessment Committee*

*   **Slide 1: Project Title & Group Details**
*   **Slide 2: Summary of Proposal Objectives** (Brief recall).
*   **Slide 3: Work Completed (Software Stack)**:
    *   EKF Kalman Filter and YOLO perception nodes implemented.
    *   FastAPI backend database, MQTT, and WebSocket managers active.
*   **Slide 4: Work Completed (Simulations)**:
    *   Gazebo scenario validations (urban cruise, low battery, rain aborts).
*   **Slide 5: Verification Outputs**: Show console logs of the 21 passing unit tests.
*   **Slide 6: Current Hardware procurement**: Holybro Pixhawk 6C and sensor purchases.
*   **Slide 7: Immediate Plan (Next Semester)**: Physical frame integration, hardware validations, and calibration logs.

---

## 3. Final Defense / Viva Outline (`Final_Defense.pptx`)
*Target Duration: 20 mins | Audience: External University Examiner & Head of Department*

*   **Slide 1: Title Slide & Candidate IDs**
*   **Slide 2: Problem Recap & Objectives**
*   **Slide 3: Final System Architecture**: Reference `system_architecture.png`.
*   **Slide 4: EKF Sensor Fusion & Perception**: Projecting 1D LiDAR into 2D camera bounding boxes (show mathematical matrix equations).
*   **Slide 5: Autonomous Failsafe Logic**: Weather abort, geofencing cylinder constraints, and RTL battery curves.
*   **Slide 6: Hardware Integration & BOM**: Final assembled weight (~6.8kg) and power distributions.
*   **Slide 7: Simulation Scenario Validation Results**: Performance metrics tables (latency, packet sizes, path tracking errors).
*   **Slide 8: Patent & Research Notebook**: Outline claims and literature publications.
*   **Slide 9: Conclusion & Future Scope**: Moving from simulation-validated prototype to physical flight trials.
