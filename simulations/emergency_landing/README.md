# Emergency Landing Scenario

## 1. Scenario Objective
Demonstrate the autonomous weather abort and diversion capability of the drone when the onboard sensors detect heavy rainfall exceeding the safe operational limit, forcing the system to locate and land at the nearest designated emergency landing platform rather than attempting to return to home or continuing the mission.

## 2. Input Conditions
*   **Cruise Altitude**: 45.0m AGL
*   **Cruise Speed**: 12.5 m/s
*   **Weather Sensors**: Detect precipitation level increasing from 2.0 mm/hr (nominal) to 12.0 mm/hr (heavy rain, threshold is 8.0 mm/hr).
*   **Target Coordinates**: 17.6721, 75.9125 (Landing Hub B)
*   **Emergency Landing Pad (Diverted Location)**: 17.6635, 75.9090 (Emergency Pad E1)
*   **Failsafe Action**: Abort current mission and perform an immediate diversion and landing at the closest emergency pad.
