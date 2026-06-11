# Obstacle Avoidance using LiDAR and YOLO Fusion

## 1. Abstract
Autonomous BVLOS drone delivery requires robust obstacle detection and tracking. Traditional methods rely solely on either active sensors (LiDAR) or passive sensors (cameras). However, LiDAR lacks semantic understanding (e.g., distinguishing a bird from a branch), while camera detection is vulnerable to poor lighting. This paper details our sensor-fusion approach combining 1D/3D LiDAR distance maps and YOLOv11 deep learning object classification.

## 2. Sensor Integration Strategy
The DAD system uses:
*   **Primary Sensor**: 120° Wide-Angle Front Camera.
*   **Secondary Sensor**: Benewake TFmini LiDAR (pointing forward alongside the camera).
*   **Sensor Fusion Model**: Early-fusion overlay. The distance measured by LiDAR is matched with the center coordinates of YOLO bounding boxes.

```
       [Camera Feed]             [LiDAR Range]
             │                         │
             ▼                         ▼
      [YOLOv11 Inference]     [Kalman Filter Scan]
             │                         │
             └───────────┬─────────────┘
                         ▼
                [Semantic Fusion]
                         │
                         ▼
           [Dynamic Threat Vector Map]
                         │
                         ▼
            [Flight Controller Override]
```

## 3. Decision Logic
1.  **Object Detection**: YOLOv11 categorizes objects (e.g., `wire`, `bird`, `pole`).
2.  **Severity Matrix**:
    *   If a `wire` is detected at >10 meters: The flight controller executes a slow pitch change to gain 3 meters of altitude.
    *   If a `bird` is detected at <5 meters: The autopilot executes a lateral bank to avoid collision.
    *   If any obstacle distance drops below 2 meters: The autopilot activates emergency loiter mode.
