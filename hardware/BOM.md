# Bill of Materials (BOM) — DAD Tarot Hexacopter
This document lists the hardware components selected for the Direct Aerial Delivery (DAD) Tarot 680Pro hexacopter platform, serving as the hardware baseline for the B.E. final year engineering design project.

## 1. Primary Component List

| Component Category | Component Name / Model | Specs & Interface | Qty | Unit Price (USD) | Unit Price (INR) | Primary Purpose |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| **Airframe** | Tarot 680Pro Carbon Fibre Hexacopter Frame | 680mm wheel-base, foldable carbon tubes, integrated PCB | 1 | $145.00 | ₹12,000 | Primary structural chassis, power routing centre |
| **Autopilot** | Holybro Pixhawk 6C Flight Controller | STM32H7, dual IMUs, MAVLink, USB-C, serial ports | 1 | $280.00 | ₹23,200 | Flight control, attitude stabilization, failsafes |
| **Companion Computer** | Raspberry Pi 5 (8GB RAM) | Quad-core ARM Cortex-A76, PCIe 2.0, UART/I2C | 1 | $80.00 | ₹6,640 | Onboard YOLO computer vision, sensor fusion, cloud telemetry |
| **Power Module** | PM02 V3 Power Management Board | Up to 12S LiPo, 5.2V regulator output, I2C telemetry | 1 | $32.00 | ₹2,650 | Regulated power delivery to Pixhawk, current/voltage sensing |
| **LiDAR Sensor** | Benewake TFmini-S LiDAR Rangefinder | 100Hz sample rate, 0.1-12m range, UART/I2C | 1 | $39.00 | ₹3,200 | Forward obstacle detection and wire avoidance |
| **GNSS Module** | Holybro F9P RTK GPS System | Multi-band RTK, centimeter-level precision, UART | 2 | $120.00 | ₹9,960 | Precision waypoint guidance and landing station alignment |
| **Telemetry Radio** | Holybro Micro Telemetry Radio v3 (915MHz) | 100mW transmit power, serial interface, MAVLink | 1 Set | $45.00 | ₹3,730 | Ground Control Station (GCS) telemetry backup link |
| **Propulsion Motors** | T-Motor MN4014 400KV Brushless Motor | Max thrust 2.9kg/motor, 24V nominal operating voltage | 6 | $68.00 | ₹5,640 | Main hexacopter propulsion units |
| **ESCs** | T-Motor AIR40A 40A Brushless ESC | 6S LiPo input, 40A continuous, rapid throttle response | 6 | $25.00 | ₹2,070 | Motor electronic speed controllers |
| **Propellers** | Tarot 13-inch Carbon Fibre Folding Props | 1345 balance-optimized, folding hub adapter | 3 Pairs | $30.00 | ₹2,490 | Lift generation and propulsion efficiency |
| **Primary Battery** | Tattu Funfly 6S 16000mAh LiPo Battery | 22.2V, 15C discharge rating, XT90-S anti-spark | 2 | $190.00 | ₹15,770 | High-capacity main power supply |
| **Onboard Camera** | Raspberry Pi Camera Module 3 (Wide) | 12MP Sony IMX708, 120° FOV, CSI-2 ribbon connection | 1 | $35.00 | ₹2,900 | Optical feed for YOLO-based bird and obstacle detection |
| **Release Mechanism** | PWM Servo-Controlled Dropping Hook | Carbon fibre mount, metal gear servo, auxiliary channel | 1 | $15.00 | ₹1,240 | Remote-actuated cargo release mechanism |
| **Power Distribution** | Integrated PDB & XT90 Connectors | Heavy duty copper bus, 10AWG main leads | 1 Set | $10.00 | ₹830 | High-current power distribution to ESCs |

## 2. Totals and Project Budget Summary
*   **Total Estimated Hardware BOM (USD)**: ~$1,765.00
*   **Total Estimated Hardware BOM (INR)**: ~₹1,46,500.00

> [!NOTE]
> Component prices are based on local distributor listings in Maharashtra, India (including customs duties and GST). All hardware interfaces conform to standard PX4 and Raspberry Pi serial protocol specifications (UART, I2C, SPI, and CAN).
