# DGCA Drone Regulations Analysis

## 1. Indian Regulatory Framework
Unmanned Aerial Vehicle (UAV) operations inside Indian airspace are strictly regulated by the **Directorate General of Civil Aviation (DGCA)** under the **Drone Rules 2021** (amended in 2022 and 2023). Any drone logistics project or prototype must align with these statutes to be certified for field testing.

## 2. Classification Criteria
The DAD Tarot 680Pro hexacopter prototype falls under the **Small Category** based on its maximum takeoff weight (MTOW):
*   **Nano**: MTOW <= 250 grams
*   **Micro**: MTOW > 250 grams and <= 2 kilograms
*   **Small**: MTOW > 2 kilograms and <= 25 kilograms  <-- *DAD MTOW: ~6.8 kg*
*   **Medium**: MTOW > 25 kilograms and <= 150 kilograms
*   **Large**: MTOW > 150 kilograms

## 3. Mandatory Compliance Checklist
For the project group to conduct flight tests in Solapur, the following steps must be completed:
1.  **Unique Identification Number (UIN)**: Acquire a registration number via the DGCA DigitalSky portal.
2.  **No Permission-No Takeoff (NPNT)**: Implement a firmware module that restricts arming commands unless a geo-fenced flight plan has been approved by the DigitalSky server.
3.  **BVLOS Corridor Clearance**:
    *   BVLOS operations require dedicated testing sandbox clearance.
    *   Onboard Detect and Avoid (DAA) failsafes must be certified in software-in-the-loop (SITL) simulations before flight.
    *   Secure telemetry transmission must run with AES-256 encryption.
