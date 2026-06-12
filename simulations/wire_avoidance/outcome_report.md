# Outcome Report: Wire Avoidance

## 1. Input Context
UAV cruising at 45m. A thin line classified as `wire` is detected at 9m directly ahead by the onboard vision and range processor.

## 2. Decision Logic
*   **WireAvoidanceEngine**: Threat range (9.0m) is below the threshold limit (10.0m).
*   **Failsafe**: Trigger vertical climb adjustment of +3.5m.

## 3. Action Taken
*   Autopilot commands throttle increase, raising the hexacopter altitude to 48.5m.
*   The drone clears the overhead wire and stabilizes at 48.5m to complete the cruise.

## 4. Result (Expected Metric)
*   **Expected Climb Rate**: 2.5 m/s.
*   **Expected Clearance Margin achieved**: 3.5m above the wire.
*   **Flight Safety outcome**: Collision avoided; flight plan preserved.
