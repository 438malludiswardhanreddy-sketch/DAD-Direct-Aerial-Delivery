# Hexacopter Flight Operations Checklist
This document provides the standard operating procedures (SOPs) and flight checklists for field operations of the Direct Aerial Delivery (DAD) Tarot 680Pro hexacopter platform.

---

## 1. Pre-Flight Inspection (Standard Ground Test)

### 1.1. Structural Inspection
- [ ] **Frame arms**: Verify all six carbon fibre folding arms are locked and bracket clamps are secure.
- [ ] **Fasteners**: Check that all motor mounting and frame plate screws are tight.
- [ ] **Propellers**: Inspect folding hubs for stress fractures. Verify propellers swing freely but have no vertical play.
- [ ] **Landing Gear**: Ensure retracting/folding struts lock into the extended landing position.

### 1.2. Electrical & Wiring Checks
- [ ] **ESC Soldering**: Inspect lower distribution board PCB joints for cracks or signs of heating.
- [ ] **Power Harness**: Verify main XT90-S connectors are pushed fully home.
- [ ] **Regulator Outputs**: Confirm the companion buck converter displays the green 5.1V indicator LED.
- [ ] **Signal Harnessing**: Inspect Pixhawk power, UART, and I2C connector clips to ensure they are fully seated.

### 1.3. Onboard Sensors & Software Initialization
- [ ] **Companion Boot**: Verify Raspberry Pi 5 boots successfully.
- [ ] **YOLO Node**: Confirm the camera stream is active and YOLO inference starts.
- [ ] **LiDAR feed**: Check TFmini-S output values in QGroundControl.
- [ ] **GNSS Lock**: Verify GPS 1 and GPS 2 show active 3D Fix or RTK Fix state. Dilution of Precision (HDOP) must be $<1.0$.
- [ ] **NPNT Licence**: Verify the signed XML flight key is uploaded to the companion computer and the arming lock is released.

---

## 2. Takeoff & In-Flight Procedures

### 2.1. Armed & Takeoff Protocol
- [ ] **Clear Area**: Ensure the flight centre launch zone has a 10m radius clear of personnel.
- [ ] **Wind Check**: Verify wind speeds are below 8.0 m/s using the hand-held anemometer.
- [ ] **Arm Command**: Set QGroundControl flight mode to **GUIDED** and command arming. Confirm motor rotation is uniform.
- [ ] **Takeoff**: Command auto-takeoff to 5.0m. Hover for 15 seconds to check attitude stability and heading lock.

### 2.2. Mission Execution & Telemetry Monitoring
- [ ] **Telemetry Heartbeat**: Monitor the live WebSocket feed on the dashboard. Packet loss must be 0%.
- [ ] **Voltage Log**: Verify total battery voltage stays above 22.0V during vertical climb.
- [ ] **Avoidance Engines**: Keep a visual watch on path offsets when passing near trees or simulated hazards.
- [ ] **Failsafe Monitoring**: Verify weather precipitation warnings in case of sudden changes.

---

## 3. Landing & Post-Flight Operations

### 3.1. Landing Procedure
- [ ] **Clear Zone**: Ensure the landing hub coordinates are free of obstructions.
- [ ] **Descent Rate**: Confirm descent speed is controlled to $<1.5$ m/s below 5.0m altitude.
- [ ] **Touchdown**: Confirm motors automatically disarm within 3 seconds of ground contact.

### 3.2. Post-Flight Procedures
- [ ] **Battery Disconnect**: Unplug the XT90-S main battery connector immediately.
- [ ] **Log Retrieval**: Copy telemetry logs and YOLO target files to storage.
- [ ] **Inspection**: Check motors and ESC temperature by hand. Surface temperature must be $<45^\circ\text{C}$.
- [ ] **Battery Storage**: Verify battery voltage is stored at $3.82\text{V}$ per cell ($22.9\text{V}$ total) if flight operations are suspended.
