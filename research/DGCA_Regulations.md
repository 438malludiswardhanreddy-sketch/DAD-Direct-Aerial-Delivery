# DGCA Drone Regulations Analysis

## 1. Regulatory Context (Indian Airspace)
The Directorate General of Civil Aviation (DGCA) regulates all drone operations in India under the **Drone Rules 2021** (and its subsequent updates).

## 2. Drone Classification
DAD hexacopters fall under the **Small Category** (weight > 2 kg and <= 25 kg) based on their cargo lifting capacity:
*   **Nano**: <= 250g
*   **Micro**: > 250g and <= 2 kg
*   **Small**: > 2 kg and <= 25 kg  <-- *DAD Tarot 680Pro (approx. 6.5 kg)*
*   **Medium**: > 25 kg and <= 150 kg
*   **Large**: > 150 kg

## 3. Compliance Requirements for Small Drones
1.  **Unique Identification Number (UIN)**: Every DAD drone must be registered on the DigitalSky platform and receive a UIN.
2.  **Unmanned Aircraft Operator Permit (UAOP)**: Operational clearance for commercial logistics.
3.  **No Permission-No Takeoff (NPNT)**: Hardware-level software lock connected to DigitalSky. Takeoff is disabled unless a flight plan has been submitted and approved.
4.  **BVLOS (Beyond Visual Line of Sight)**:
    *   BVLOS operations require special approval under sandbox guidelines or official delivery corridors.
    *   Autonomous avoidance systems (DAA - Detect and Avoid) must be verified through simulation and flight testing.
    *   Dynamic geo-fencing must be active onboard the autopilot.
