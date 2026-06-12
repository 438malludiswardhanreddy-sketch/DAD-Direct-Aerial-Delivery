# Outcome Report: Wire Avoidance

## 1. Input Context
UAV cruising at 45m. A thin line classified as `wire` is detected at 9m directly ahead by the onboard vision and range processor.

## 2. Decision Logic
*   **WireAvoidanceEngine**: Threat range (9.0m) is below the threshold limit (10.0m).
*   **Failsafe**: Trigger vertical climb adjustment of +3.5m.

## 3. Action Taken
*   Autopilot commands throttle increase, raising the hexacopter altitude to 48.5m.
*   The drone clears the overhead wire and stabilizes at 48.5m to complete the cruise.

## Simulation Result
*   **Flight Outcome**: Autonomous altitude climb adjustment and overhead wire clearance.
*   **Climb Rate**: 2.5 m/s (Simulated).
*   **Clearance Margin**: 3.5m vertical separation (Simulated).
*   **Safety Outcome**: Collision avoided; flight plan successfully resumed (Simulated).

## Expected Result
*   Detection of sub-centimetre wire structures at 9.0m.
*   Trigger of positive climb rate failsafe to bypass threat.
*   Safe elevation transit without entering stall or loss of control.

## Target Specification
*   **LiDAR Resolution**: 1 cm range resolution
*   **Failsafe Threshold**: 10.0m obstacle range
*   **Target Altitude Offset**: +3.5m vertical step
