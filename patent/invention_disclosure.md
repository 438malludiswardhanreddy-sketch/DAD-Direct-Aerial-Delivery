# Invention Disclosure Document (IDD)
**Title**: Multi-Sensor Fusion Framework and Dynamic Failsafe Management System for Autonomous Micro-UAV Logistics
**Invention Centre**: B.E. Final Year Engineering R&D Project, Solapur, India
**Inventors**: DAD Project Group

---

## 1. Technical Field of the Invention
This invention relates generally to unmanned aerial vehicle (UAV) navigation and flight control. More specifically, it relates to a lightweight, real-time multi-sensor fusion algorithm (Vision-LiDAR) and an integrated environmental failsafe engine for autonomous parcel delivery in urban micro-airspace.

---

## 2. Background and Prior Art Issues
Autonomous UAV delivery systems face significant safety and regulatory hurdles:
1.  **High Payload/Cost Barriers**: Existing autonomous obstacle detection relies on expensive 3D LiDAR arrays (e.g., Velodyne) or high-end GPU companion cards (e.g., NVIDIA Jetson). These are unsuitable for small, low-cost delivery quadrotors.
2.  **GPS Multipath Reflections**: Tall buildings in urban canyons attenuate and reflect GPS signals, leading to coordinate drift.
3.  **Sudden Weather Deterioration**: Sudden rainfall or wind gusts can overload the airframe's power systems, causing crashes if the drone is forced to return to a distant home station.

---

## 3. Summary of the Invention
The present invention solves these limitations through an integrated hardware-software architecture consisting of:
1.  **Lightweight Sensor Fusion Node**: Combines a single-axis forward-facing 1D LiDAR and a monocular wide-angle camera. The camera runs a lightweight object detection model (YOLO) to identify obstacles (e.g., birds, wires, buildings), while the EKF fuses the 2D bounding boxes and the 1D LiDAR distance vectors to generate a 3D relative coordinate state vector ($p_x, p_y, p_z, v_x, v_y, v_z$).
2.  **Adaptive Local Avoidance Engine**: Calculates evasive vectors (yaw offset banks or vertical climbs) based on the target object classification and distance.
3.  **Multi-Safe Weather Diverter**: Constantly monitors precipitation levels. When thresholds are breached, it calculates real-time distances to multiple pre-registered emergency landing platforms and commands a diversion path to the closest pad.

---

## 4. Detailed Description of the Preferred Embodiment
The architecture is implemented on a Holybro Pixhawk 6C autopilot linked to a Raspberry Pi 5 companion computer over a high-speed UART serial interface using MAVLink.
*   **LiDAR Alignment**: The 1D LiDAR beam is aligned with the optical centre coordinates of the camera.
*   **Coordinate Projection**: The companion computer projects 3D spatial points to 2D image coordinate systems to verify LiDAR and bounding box alignment.
*   **EKF Covariance Tuning**: When GPS signals degrade, the EKF dynamically de-weights GPS measurement noise parameters, relying on IMU and camera visual flow estimates.
