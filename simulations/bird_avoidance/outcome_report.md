# Outcome Report: Bird Avoidance

## 1. Input Context
UAV cruises at 12.5 m/s. An object classified as `bird` is detected by the YOLO model on the companion computer, with LiDAR confirming range at 6.5m.

## 2. Decision Logic
*   **BirdAvoidanceEngine**: Threat range (6.5m) is below the safe clearance limit (8.0m). Azimuth is positive (+12.0°).
*   **Failsafe**: Steer opposite (yaw offset = -40.0°).

## 3. Action Taken
*   Autopilot receives override yaw target. Drone executes a sharp bank, changing heading from 90° to 50° within 1.5 seconds.
*   Once range checks show clear path, the drone resumes its course.

## 4. Result (Expected Metric)
*   **Expected Avoidance Reaction Latency**: <120ms.
*   **Expected Clearance Margin achieved**: 4.1m minimum distance to bird.
*   **Flight Safety outcome**: Collison successfully avoided.
