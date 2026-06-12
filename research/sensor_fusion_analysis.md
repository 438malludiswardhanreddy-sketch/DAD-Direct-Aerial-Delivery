# Sensor Fusion Analysis: Camera and LiDAR Integration
This research paper analyses the mathematical and algorithmic framework implemented for sensor fusion on the Direct Aerial Delivery (DAD) companion computer. The system fuses 2D optical bounding boxes from a camera with 1D range measurements from a LiDAR to estimate obstacle positions in real time.

---

## 1. Coordinate Systems and Spatial Calibration
To fuse optical and distance measurements, we define three primary coordinate systems:
1.  **LiDAR Coordinate System ($C_L$)**: A 3D coordinate system centred on the LiDAR emitter. Since we use a single-beam rangefinder, measurements are represented as a distance vector $d$ along the sensor's optical axis ($Z_L$).
2.  **Camera Coordinate System ($C_C$)**: Centred on the camera optical centre. The $Z_C$ axis represents depth, $X_C$ points to the right, and $Y_C$ points downwards.
3.  **Body Coordinate System ($C_B$)**: Centred at the drone's centre of gravity, aligned with the PX4 autopilot IMU axis (forward-left-up).

```
          [LiDAR Frame] (X_L, Y_L, Z_L)
                 │
                 ▼ (Extrinsic Calibration: [R | T])
          [Camera Frame] (X_C, Y_C, Z_C)
                 │
                 ▼ (Intrinsic Matrix: K)
          [Image Plane] (u, v)
```

### 1.1. Extrinsic Transformation
The translation and rotation between the LiDAR and camera sensors are defined by the extrinsic matrix:
$$P_C = R_{L}^C P_L + T_{L}^C$$

where:
*   $R_{L}^C \in \mathbb{R}^{3\times 3}$ is the rotation matrix.
*   $T_{L}^C \in \mathbb{R}^{3\times 1}$ is the translation vector.
*   $P_L$ is the coordinate point in the LiDAR frame, and $P_C$ is the projected coordinate point in the camera frame.

### 1.2. Intrinsic Camera Projection
A 3D point $P_C = [X_C, Y_C, Z_C]^T$ in the camera frame is projected onto the 2D image plane coordinate $[u, v]^T$ using the camera intrinsic matrix $K$:
$$\lambda \begin{bmatrix} u \\ v \\ 1 \end{bmatrix} = K P_C = \begin{bmatrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} X_C \\ Y_C \\ Z_C \end{bmatrix}$$

where:
*   $f_x, f_y$ are the focal lengths in pixel units.
*   $c_x, c_y$ are the principal point coordinates.
*   $\lambda = Z_C$ represents the depth parameter.

---

## 2. Extended Kalman Filter (EKF) for Obstacle Tracking
To mitigate sensor noise and handle temporary occlusions, an Extended Kalman Filter (EKF) tracks the state of detected obstacles.

### 2.1. State Vector
The state vector $x_k$ at time step $k$ represents the relative position and velocity of the obstacle in the drone's body frame:
$$x_k = \begin{bmatrix} p_x & p_y & p_z & v_x & v_y & v_z \end{bmatrix}^T$$

### 2.2. State Transition Model
Assuming a constant velocity model between updates:
$$x_k = A x_{k-1} + w_k$$

where $A$ is the state transition matrix:
$$A = \begin{bmatrix} I_{3\times 3} & \Delta t \cdot I_{3\times 3} \\ 0_{3\times 3} & I_{3\times 3} \end{bmatrix}$$

and $w_k \sim \mathcal{N}(0, Q_k)$ represents the process noise.

### 2.3. Measurement Model
The measurement vector $z_k$ consists of the 2D image coordinates of the obstacle centre $[u, v]^T$ from the camera and the range $d$ from the LiDAR:
$$z_k = \begin{bmatrix} u & v & d \end{bmatrix}^T$$

The non-linear measurement function $h(x_k)$ maps the estimated state vector to the measurement space:
$$h(x_k) = \begin{bmatrix} \frac{f_x \cdot p_x}{p_z} + c_x \\ \frac{f_y \cdot p_y}{p_z} + c_y \\ \sqrt{p_x^2 + p_y^2 + p_z^2} \end{bmatrix}$$

### 2.4. Measurement Jacobian Matrix
The measurement mapping is linearized using the Jacobian matrix $H_k$:
$$H_k = \frac{\partial h(x)}{\partial x} \Big|_{x = \hat{x}_{k|k-1}}$$

$$H_k = \begin{bmatrix} \frac{f_x}{p_z} & 0 & -\frac{f_x \cdot p_x}{p_z^2} & 0 & 0 & 0 \\ 0 & \frac{f_y}{p_z} & -\frac{f_y \cdot p_y}{p_z^2} & 0 & 0 & 0 \\ \frac{p_x}{d} & \frac{p_y}{d} & \frac{p_z}{d} & 0 & 0 & 0 \end{bmatrix}$$

This Jacobian scales the Kalman gain, ensuring that range updates from the LiDAR adjust the depth estimate ($p_z$) while visual bounding boxes refine the lateral offsets ($p_x, p_y$).

---

## 3. Algorithm Flow and Validation
1.  **Bounding Box Detection**: The YOLO model processes camera frames to output bounding boxes.
2.  **Gating and Association**: The system verifies if the LiDAR rangefinder beam aligns with the detected bounding box center.
3.  **Correction Step**:
    *   If both camera and LiDAR detect the obstacle, the EKF updates using the complete measurement vector $z_k = [u, v, d]^T$.
    *   If the camera view is occluded but the LiDAR maintains a lock, the EKF updates using only the range component ($z_k = [d]$).
    *   If the LiDAR beam misses the obstacle (e.g. during rapid pitch adjustments) but the camera maintains tracking, the EKF updates using the visual coordinates ($z_k = [u, v]^T$) to extrapolate depth.
