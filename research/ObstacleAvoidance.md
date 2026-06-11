# Obstacle Avoidance via Camera and LiDAR Fusion

## 1. Introduction
This research paper outlines our local path planning method for autonomous drones. In final year engineering laboratories, constructing high-cost 3D LiDAR arrays is often not feasible. We propose a cost-effective sensor fusion design integrating a 1D/2D LiDAR rangefinder (e.g. Benewake TFmini) with a standard camera stream. The camera classifies obstacle types, while the LiDAR provides accurate range values.

## 2. Methodology
Our implementation coordinates:
*   **Sensor Inputs**: Wide-angle video frames and serial LiDAR distance scans.
*   **Filtre Algorithm**: A Kalman filter resolves range measurement noise and outliers.
*   **Bounding Box Projection**: The camera frames are processed to locate obstacle edges (wires, towers, birds). The LiDAR beam width is aligned with the frame center coordinates.

```
       [Camera Feed]             [LiDAR Range]
             │                         │
             ▼                         ▼
      [Object Detection]       [Kalman Range Filter]
             │                         │
             └───────────┬─────────────┘
                         ▼
                [Semantic Fusion]
                         │
                         ▼
          [Dynamic Trajectory Controller]
                         │
                         ▼
            [Flight Autopilot Override]
```

## 3. Threat Assessment Criteria
The companion computer processes the fused state and prioritises corrective flight modes:
1.  **Low Threat (>10m)**: Standard cruise path is maintained.
2.  **Medium Threat (5m - 10m)**: The navigation controller recalculates a yaw offset vector to steer around the coordinate box.
3.  **High Threat (<2m)**: Failsafe override engages immediately. The autopilot switches to hover mode and triggers a Return-to-Home trajectory.
