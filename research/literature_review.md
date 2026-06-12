# Literature Review: Autonomous Aerial Delivery Systems
This literature review compiles state-of-the-art research on key domains underpinning the Direct Aerial Delivery (DAD) project: path planning algorithms, multi-sensor fusion, and autonomous collision avoidance in urban micro-airspace. It provides the theoretical basis for our final year engineering design.

---

## 1. Path Planning Algorithms in Urban micro-Airspace
Autonomous flight in urban environments requires path-planning algorithms to negotiate complex three-dimensional obstacle fields (such as buildings, towers, and power lines). 

### 1.1. Global Path Planning
Global path planning computes an optimal trajectory prior to takeoff based on static map data.
*   **A\* Search Algorithm**: Hart et al. (1968) introduced the A\* search, which remains a staple in grid-based path planning. In drone applications, three-dimensional implementations of A\* (3D-A\*) discretize the airspace into voxels. While finding the optimal path, its computational complexity increases exponentially with search-space size, causing latencies in dynamic recalculation.
*   **Rapidly-exploring Random Trees (RRT and RRT\*)**: Karaman and Frazzoli (2011) proved that RRT\* achieves asymptotic optimality, making it highly suitable for high-dimensional configuration spaces. However, RRT\* paths tend to be jagged, requiring post-processing smoothing (e.g., cubic splines or Bezier curves) to match the physical flight characteristics of multirotors.

### 1.2. Local Path Planning and Reactive Steering
Local planning handles dynamic obstacles and sensor-detected threats in real time.
*   **Vector Field Histogram (VFH)**: Originally developed for ground robots by Borenstein and Koren (1991), VFH has been adapted for quadrotors. It maps sensor readings (like LiDAR range scans) into a polar histogram of obstacle density, allowing the vehicle to select paths that minimise collision risk. Its drawback is its susceptibility to local minima in concave obstacle configurations.
*   **Dynamic Window Approach (DWA)**: Fox et al. (1997) proposed DWA, which operates directly in the velocity space of the vehicle, accounting for acceleration and torque limits. It is highly effective for fast-moving multirotors but requires precise dynamic models of the airframe.

---

## 2. Multi-Sensor Fusion for State Estimation and Navigation
Reliable state estimation is critical for closed-loop flight control. Relying solely on Global Navigation Satellite Systems (GNSS) is hazardous due to signal attenuation and multipath reflections in urban canyons.

### 2.1. Inertial-Navigation Integration
*   **Loosely-Coupled EKF**: Integrates GNSS position updates and IMU accelerations as independent inputs. If GNSS is lost, the state estimator drifts rapidly.
*   **Tightly-Coupled EKF**: Fuses raw GNSS pseudo-ranges directly with inertial measurements. This provides superior state tracking even when fewer than four satellites are visible, which is common when flying between tall buildings.

### 2.2. Visual-Inertial Odometry (VIO)
When GNSS signal is lost completely, VIO systems use onboard camera feeds to track environmental features, combining them with IMU readings to estimate vehicle velocity. Systems like **ORB-SLAM3** (Campos et al., 2021) and **ROVIO** (Bloesch et al., 2017) demonstrate sub-decimeter drift rates, but their computational demands exceed the hardware limits of low-cost companion computers unless hardware-accelerated.

---

## 3. Sensor Fusion for Collision Avoidance
Integrating vision and range sensors is a primary research area for drone safety.
*   **Camera-LiDAR Fusion**: Cameras excel at classification (e.g., classifying an object as a bird or a kite using YOLO models), but struggle with depth estimation. LiDAR provides millimeter-accurate range measurements but lacks semantic understanding. Fusing these sensors provides a rich 3D representation of the environment.
*   **Coordinate Projection**: Projecting 3D LiDAR point clouds onto 2D camera frames requires spatial calibration (extrinsic calibration matrices). In small UAVs, calibration errors due to frame flex and motor vibrations require robust software filters (like Kalman tracking filters) to prevent false positives and alignment mismatches.

---

## 4. Synthesis and Project Gap Analysis
While advanced systems combine 3D LiDAR arrays and high-performance GPU companion computers, undergraduate engineering projects face strict budget and payload constraints. This project addresses this gap by implementing a lightweight, low-cost sensor fusion stack. It integrates a single-beam 1D LiDAR and a Raspberry Pi 5 camera module, utilizing a custom Extended Kalman Filter to achieve reliable obstacle avoidance within DGCA regulatory guidelines.
