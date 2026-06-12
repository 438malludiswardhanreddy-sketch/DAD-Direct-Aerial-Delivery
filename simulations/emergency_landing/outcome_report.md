# Outcome Report: Emergency Landing

## 1. Input Context
During a cruise flight at an altitude of 45.0m and a speed of 12.5 m/s, the drone encounters a sudden localised storm. Onboard environmental sensors report precipitation levels of 12.0 mm/hr, which exceeds the design safety threshold of 8.0 mm/hr for the airframe. The battery level is at 74.2%.

## 2. Decision Logic
*   **WeatherMonitor Module**: Analysing real-time precipitation sensor feeds. Flags a weather abort condition when threshold is breached.
*   **EmergencyDiverter Module**: Evaluates the distance to all registered landing stations. Determines that returning to Launch Station A `(17.6590, 75.9059)` (310m away) or continuing to Landing Hub B `(17.6721, 75.9125)` (850m away) presents higher risk than landing at the nearest Emergency Pad E1 `(17.6635, 75.9090)` (165m away).
*   **Failsafe Engine**: Initiates diversion to Emergency Pad E1.

## 3. Action Taken
*   The flight controller aborts the current mission path and sets Emergency Pad E1 as the new target.
*   The drone decreases speed to 8.0 m/s and descends to 30.0m to reduce wind exposure.
*   The drone aligns with the IR precision landing beacon on Emergency Pad E1 and executes a vertical descent.
*   Autonomous landing is successfully completed, and the motors are disarmed.

## 4. Result (Expected Metric)
*   **Expected Diversion Latency**: <200ms from sensor threshold breach.
*   **Expected Diversion Flight Duration**: 25.0 seconds.
*   **Precision Landing Accuracy**: <0.3m deviation from beacon centre.
*   **Failsafe Execution outcome**: Safe recovery of drone, payload, and flight log data at an emergency site.
