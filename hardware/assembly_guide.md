# Assembly and Integration Guide — DAD Tarot Hexacopter
This document provides the technical instructions for assembling, wiring, and integrating the physical hardware for the Direct Aerial Delivery (DAD) Tarot 680Pro hexacopter.

---

## 1. Structural Assembly
The structural chassis is built around the Tarot 680Pro carbon fibre folding frame.

### Step 1.1: Centre Plate Assembly
*   Lay out the upper and lower central plates.
*   Secure the metal folding brackets to the plates using the provided M2.5 socket head screws. Ensure thread-locking compound (e.g., Loctite 243) is applied to all metal-to-metal threads.
*   Route the motor and ESC cabling through the carbon fibre arm tubes before clamping them into the folding brackets.

### Step 1.2: Arm and Motor Mount Assembly
*   Mount the six T-Motor MN4014 motors to the carbon fibre motor mount brackets at the end of each arm.
*   Orient the motor wires towards the centre plate.
*   Slide the folding landing gear clamps onto the designated rear arms, ensuring they lock firmly in the extended position.

---

## 2. Power Distribution
The Tarot 680Pro features an integrated PCB on the lower centre plate, simplifying power routing.

### Step 2.1: Main Power Solder Connections
*   Solder the six T-Motor AIR40A ESC power leads (positive and negative) directly to the copper landing pads on the lower PCB.
*   Solder the 10AWG main battery lead with an XT90-S anti-spark connector to the primary input pads.
*   Solder the input leads of the PM02 V3 Power Module to the secondary high-current pads on the PCB.

### Step 2.2: Dual Voltages and Regulation
*   **Pixhawk Power**: The PM02 V3 Power Module steps down the 6S battery voltage to a regulated 5.2V (up to 3A). Connect the 6-pin Clik-Mate cable from the PM02 output port to the **POWER1** port of the Pixhawk 6C.
*   **Raspberry Pi 5 Power**: The Raspberry Pi 5 requires a dedicated 5.1V, 5A supply to prevent undervoltage throttling, especially under GPU load during YOLO inference. Mount a high-efficiency 5V/5A DC-DC buck regulator to the lower plate, connect its input to the main PCB, and route its output to the Pi 5 via a custom USB-C connection or the GPIO 5V pins (Pins 2, 4 for 5V, Pin 6 for Ground).

---

## 3. Electronics Mount and Connections

### Step 3.1: Pixhawk 6C Installation
*   Mount the Pixhawk 6C in the geometric centre of the upper plate using anti-vibration damping foam pads. Alignment is critical for IMU calibration.
*   Ensure the arrow on the Pixhawk case points toward the nose of the hexacopter.
*   Connect the ESC signal leads to the Pixhawk FMU Out ports (Main 1-6) corresponding to the standard PX4 hexacopter mixer configuration.

### Step 3.2: Raspberry Pi 5 Mounting
*   Install the Raspberry Pi 5 in a protective, ventilated enclosure on the top deck.
*   Connect the Raspberry Pi Camera Module 3 (Wide-Angle) to the CSI port, mounting the camera on a forward-facing 2-axis gimbal or fixed vibration-damped nose mount.
*   Mount the TFmini-S LiDAR sensor adjacent to the camera, pointing directly forward to detect obstacles and overhead wires.

---

## 4. Communication and Interfacing

### Step 4.1: Autopilot to Companion Link
*   Connect the Pixhawk **TELEM1** port to the Raspberry Pi 5 **UART0** (via GPIO Pins 8/TXD and 10/RXD) or via an FTDI USB-to-UART adapter connected to a Pi USB 3.0 port.
*   Configure the serial connection parameters:
    *   **Baud Rate**: `921600` bps
    *   **Protocol**: MAVLink 2

### Step 4.2: Sensor and Telemetry Layout
*   **RTK GPS**: Mount the Holybro F9P GPS modules on carbon fibre poles at least 15cm above the top plate to avoid magnetic interference. Connect GPS 1 to Pixhawk's **GPS1** port and GPS 2 (for yaw determination/heading) to the **GPS2** port.
*   **LiDAR**: Connect the TFmini-S LiDAR UART TX/RX lines to the Pixhawk **TELEM2** port or directly to the Raspberry Pi GPIO serial pins for edge processing.
*   **Telemetry Radio**: Connect the 915MHz Holybro Telemetry Radio to the **TELEM3** port of the Pixhawk 6C to establish a backup communication link with the Ground Control Station (QGroundControl).

---

## 5. Wiring Schematic References
For detailed visual mappings of the system connections, refer to the following local schematics:
*   [Wiring Diagram](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware/wiring_diagram.png)
*   [Power Distribution Schematic](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware/power_distribution.png)
*   [Pixhawk 6C Connections Layout](file:///C:/Users/mallu/.gemini/antigravity/scratch/DAD-Direct-Aerial-Delivery/hardware/pixhawk_connections.png)

---

## 6. Pre-Flight Safety Inspections
Before attaching propellers and powering the system for flight tests:
1.  **Continuity Check**: Measure resistance across the XT90 power input to ensure there are no short circuits on the distribution board.
2.  **Structural Integrity**: Verify all arm locks are securely clicked into place and motor mounting screws are tight.
3.  **Failsafe Check**: Test the RC transmitter connection and verify that switching off the transmitter triggers the FailSafe mode in QGroundControl.
