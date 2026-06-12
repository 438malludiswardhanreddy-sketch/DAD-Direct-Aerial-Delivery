# DAD Platform Maintenance Guide

## 1. Hardware Inspection Checklist (Every 10 Flights)
*   **Chassis Check**: Inspect carbon frame joints on the Tarot 680Pro hexacopter.
*   **Propeller Check**: Check carbon folding blades for stress lines or chips.
*   **Wiring Check**: Ensure sensor serial connections (Pixhawk telemetry, LiDAR) are securely mounted.

## 2. Battery Life-Cycle Maintenance
*   Store 6S LiPo batteries at 3.85V per cell storage charge.
*   Retire any battery with state-of-health <80% (visible in the dashboard analytics page).

## 3. Database Log Rotation
The SQLite backend file `dad_logistics.db` logs range updates at high rates. Run the rotation script weekly to archive telemetry tables older than 30 days.
