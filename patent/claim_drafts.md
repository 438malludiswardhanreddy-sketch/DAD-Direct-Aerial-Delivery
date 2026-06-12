# Patent Claim Drafts
This document drafts the preliminary patent claims for the DAD multi-sensor fusion and failsafe routing system.

---

## 1. Independent Claim 1
**We claim:**
1.  An autonomous navigation and failsafe routing system for an unmanned aerial vehicle (UAV), comprising:
    *   an autopilot flight controller configured to execute attitude stabilization and waypoint navigation;
    *   a companion computer linked to the autopilot flight controller;
    *   a monocular camera mounted on the UAV and configured to capture a forward-facing 2D video feed; and
    *   a single-beam LiDAR rangefinder aligned with the optical axis of the monocular camera;
    *   wherein the companion computer runs a processing loop to:
        *   detect and classify obstacles in the 2D video feed using an object detection neural network;
        *   project the 1D distance measurements from the LiDAR rangefinder onto the 2D bounding boxes of the classified obstacles;
        *   estimate the 3D position and velocity vectors of the obstacles relative to the UAV using an Extended Kalman Filter (EKF); and
        *   command the autopilot flight controller to execute evasive maneuvers when the estimated distance is below a safety threshold.

---

## 2. Dependent Claims
2.  The system as claimed in claim 1, wherein the evasive maneuvers comprise a horizontal yaw offset bank away from the obstacle or a vertical climb over the obstacle.
3.  The system as claimed in claim 1, further comprising a precipitation sensor mounted on the UAV and linked to the companion computer.
4.  The system as claimed in claim 3, wherein the companion computer continuously monitors the precipitation rate and commands the autopilot flight controller to abort the current mission and divert to the nearest pre-registered emergency landing pad if the precipitation rate exceeds a safety limit.
5.  The system as claimed in claim 4, wherein the landing diversion is calculated by comparing distances to multiple pre-registered emergency coordinates and selecting the path that minimizes energy consumption.
