# Sensor Calibration & Validation Logs
This document outlines the validation procedures, laboratory bench test protocols, and target performance limits for the onboard perception sensors: the Benewake TFmini-S LiDAR rangefinder and the Raspberry Pi Camera Module 3.

---

## 1. Benewake TFmini-S LiDAR Validation

### 1.1. Test Protocol
*   **Setup**: Mount the LiDAR module on a linear calibration rail at the Electronics Lab centre, aiming at a flat, non-reflective white target wall.
*   **Steps**: Measure distance increments from 0.5m to 10.0m in intervals of 0.5m. Record the serial readings from the companion computer.
*   **Test Script**: Run `autonomous/wire_detection.py` and output raw distance floats.

### 1.2. Accuracy Benchmarks

| True Distance (m) | Measured Result (m) | Deviation (m) | Status |
| :--- | :--- | :--- | :--- |
| 1.00 | 1.01 (Simulation Placeholder) | +0.01 | Pass |
| 2.00 | 1.98 (Simulation Placeholder) | -0.02 | Pass |
| 5.00 | 4.95 (Simulation Placeholder) | -0.05 | Pass |
| 8.00 | 7.91 (Simulation Placeholder) | -0.09 | Pass |
| 10.00 | 9.87 (Simulation Placeholder) | -0.13 | Pass |

*   **Average Measurement Error**:
    *   *Expected Metric*: <1.5% of true distance.
    *   *Simulation Placeholder*: 1.15% average error.
*   **Max Operational Range (Indoors)**:
    *   *Target Metric*: 12.0m.
    *   *Simulation Placeholder*: 11.8m.

---

## 2. Raspberry Pi Camera Module 3 Validation

### 2.1. Test Protocol
*   **Setup**: Secure the camera to the forward-facing vibration-isolated mounts on the Tarot 680Pro frame. Light levels are controlled to simulate sunny, overcast, and low-light delivery environments.
*   **Target**: Place a 3D silhouette model of a bird (obstacle target) at varying horizontal offsets to calibrate the YOLO bounding boxes.

### 2.2. Frame Processing Latency
Measuring YOLO inference times on the Raspberry Pi 5 companion computer using dynamic quantisation (INT8) and NCNN/ONNX runtimes.

*   **Inference Latency (FP32 precision)**:
    *   *Target Metric*: <45ms.
    *   *Simulation Placeholder*: 38.2ms.
*   **Inference Latency (INT8 quantised)**:
    *   *Expected Metric*: <20ms.
    *   *Simulation Placeholder*: 12.4ms.
*   **Optical Flow Tracker Update Latency**:
    *   *Target Metric*: <5.0ms.
    *   *Simulation Placeholder*: 2.1ms.

---

## 3. Sensor Coordinate Calibration Validation
Verification of the Extrinsic Transformation Matrix ($R_{L}^C, T_{L}^C$) between the camera optical centre and the LiDAR axis:

*   **Angular Alignment Error**:
    *   *Target Metric*: <0.5 degrees.
    *   *Simulation Placeholder*: 0.18 degrees.
*   **Projection Displacement Error (pixel space)**:
    *   *Expected Metric*: <5 pixels.
    *   *Simulation Placeholder*: 2.3 pixels at 5.0m range.
