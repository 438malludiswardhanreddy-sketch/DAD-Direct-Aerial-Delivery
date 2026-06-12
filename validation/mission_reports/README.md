# Flight Mission Reports
This directory compiles summaries of the simulation validation runs, comparing commanded paths with executed trajectories.

---

## 1. Flight Report Summary Matrix (SITL Runs)

| Scenario Name | Path Length | Target Duration | Expected Battery Use | Avoidance Action | Flight Result |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Urban Delivery** | 1.8 km | 100.0s | 18.1% | None (Clear airspace) | Successful landing |
| **Bird Avoidance** | 1.8 km | 105.0s | 19.5% | Sharp Yaw Bank (-40.0°) | Collision avoided, landed safely |
| **Wire Avoidance** | 1.8 km | 103.0s | 19.2% | Vertical Climb (+3.5m) | Obstacle cleared, landed safely |
| **Low Battery** | 0.8 km | 30.0s | 5.2% | Automatic RTL at 20.0% | Returned and landed safely |
| **Emergency Landing** | 0.2 km | 25.0s | 3.5% | Divert to Emergency Pad | Rain abort, landed safely |

---

## 2. Path tracking Precision Analysis
*   **Average Tracking Error (X/Y Plane)**:
    *   *Target Metric*: $<0.5$ m.
    *   *Simulation Placeholder*: $0.22$ m.
*   **Precision Landing Accuracy (Dual-RTK + Beacon)**:
    *   *Expected Metric*: $<0.15$ m error.
    *   *Simulation Placeholder*: $0.08$ m average landing offset.
*   **Maximum Wind Gust Tolerated**:
    *   *Target Metric*: $12.0$ m/s gusts.
    *   *Simulation Placeholder*: $10.0$ m/s gusts (with $<1.2$m path drift).
