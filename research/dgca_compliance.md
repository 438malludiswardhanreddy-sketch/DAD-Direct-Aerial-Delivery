# DGCA Compliance Whitepaper: Regulatory Integration for Autonomous UAVs
This whitepaper analyses the regulatory requirements established by the Directorate General of Civil Aviation (DGCA) under the Indian Ministry of Civil Aviation, detailing the technical implementation required to achieve full compliance for the Direct Aerial Delivery (DAD) project.

---

## 1. Regulatory Context and Classification
All civil drone operations in Indian airspace are governed by the **Drone Rules 2021** (with subsequent amendments in 2022 and 2023). Under these rules, UAVs are categorized based on their Maximum Take-Off Weight (MTOW). 

The DAD Tarot 680Pro hexacopter prototype is classified as a **Small Category UAV**:
*   **Nano**: MTOW $\le$ 250 g
*   **Micro**: MTOW > 250 g and $\le$ 2.0 kg
*   **Small**: MTOW > 2.0 kg and $\le$ 25.0 kg  *(DAD Hexacopter MTOW: ~6.8 kg)*
*   **Medium**: MTOW > 25.0 kg and $\le$ 150.0 kg
*   **Large**: MTOW > 150.0 kg

Small category UAVs require a **Type Certificate** and a **Unique Identification Number (UIN)** registered on the DigitalSky platform prior to conducting any flight operations.

---

## 2. No Permission-No Takeoff (NPNT) Architecture
NPNT is a mandatory software and hardware enforcement mechanism defined by the DGCA. A drone cannot arm its motors unless it has received a valid digital flight permission artifact from the DigitalSky server.

```
  [DigitalSky GCS App] ──(Request Permission)──> [DigitalSky Server]
           │                                             │
           ▼                                             │
   [Receive XML Licence] <─────(Signed Permission)───────┘
           │
           ▼ (Upload via MAVLink)
   [PX4 Flight Controller]
           │
           ▼ (Validate Signature & Geofence)
   [Motors Armed / Takeoff Allowed]
```

### 2.1. Permission Artifact Structure
The flight permission is delivered as a signed XML document (Licence File) containing:
1.  **UIN**: Unique identification number of the drone.
2.  **Time Window**: Specific start and end times for the flight.
3.  **Boundary Coordinates**: A polygon defining the approved horizontal flight volume (Geofence).
4.  **Altitude Limit**: Maximum permissible height Above Ground Level (AGL), typically capped at 120m (400ft) for Green Zones.
5.  **Digital Signature**: Signed using the DigitalSky public-private key infrastructure.

### 2.2. Autopilot Guard Module
The companion computer (Raspberry Pi 5) runs a background daemon that interfaces with the Pixhawk 6C via MAVLink.
*   Upon power-on, the Pixhawk is placed in an `ARMING LOCK` state.
*   The Ground Control Station (GCS) uploads the XML licence to the companion computer.
*   The companion computer parses the licence, validates the cryptographic signature against the DGCA root certificate, and verifies that the current GPS coordinates match the start point.
*   If validation succeeds, the companion computer transmits a custom MAVLink message (`MAV_CMD_COMPONENT_ARM_DISARM` with parameter overrides) to release the arming lock.

---

## 3. Geofencing and Failsafe Rules
Under the DGCA guidelines, the drone must remain within the approved flight boundary.

### 3.1. Geofence Violations (Breach Prevention)
The Pixhawk 6C is configured with a hard cylindrical or polygonal geofence matching the approved flight corridor.
*   **Warning Zone**: Located 10m inside the geofence boundary. If breached, the QGroundControl GCS issues an audible alarm, and the telemetry logs log a Warning.
*   **Action Boundary**: If the drone reaches the hard geofence limit, the PX4 autopilot overrides manual/mission controls and executes an automatic **Return-to-Launch (RTL)** or **Land-in-Place** protocol.

### 3.2. Airspace Zone Restrictions
DigitalSky maps Indian airspace into three dynamic zones:
*   **Green Zone**: Up to 400ft (120m) AGL. No prior flight permission is required for micro/small category drones, but NPNT logging is still mandatory.
*   **Yellow Zone**: Controlled airspace. Requires permission from the local Air Traffic Control (ATC).
*   **Red Zone**: Prohibited airspace (near airports, military installations, and sensitive government centres). Takeoff is strictly locked.

---

## 4. Compliance Implementation Status
The DAD software stack implements compliance parameters in simulated environments:
*   **NPNT Emulator**: Located in `security/npnt_validation.py`. It simulates the validation of signed XML flight keys before releasing the PX4 lock.
*   **Geofence Verification**: Pre-configured in Pixhawk parameters to prevent deviation from the Solapur R&D test site boundaries.
*   **Telemetry Encryption**: Encrypts companion-to-backend WebSocket links using TLS 1.3 to meet regulatory secure data transmission guidelines.
