"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Sensor Fusion Node
Description: This script fuses real-time distance measurements from the LiDAR sensor 
             with bounding box outputs from the camera camera stream. It helps in 
             analysing local threats for obstacle avoidance in autonomous flight.
"""

import time
import math
from .kalman_filter import RangeKalmanFilter

class SensorFusionNode:
    def __init__(self, lidar_port="/dev/ttyAMA0", camera_index=0):
        print("[Sensor Fusion] Initialising node for sensor data processing...")
        self.kf = RangeKalmanFilter()
        self.threat_threshold_metres = 10.0
        self.is_sensor_active = True
        
    def fuse_data(self, camera_box, raw_lidar_reading):
        """
        Fuses the visual bounding box coordinates with the raw distance reading.
        Uses a Kalman filter to smooth range measurement anomalies.
        """
        # Filter raw distance from the LiDAR sensor
        filtered_distance = self.kf.filter(raw_lidar_reading)
        
        # Calculate horizontal offset from frame centre
        # Assuming camera resolution is 640x480
        frame_centre_x = 320
        box_centre_x = camera_box[0] + (camera_box[2] / 2)
        offset_pixels = box_centre_x - frame_centre_x
        
        # Approximate azimuth angle in degrees
        fov_degrees = 62.2
        azimuth_deg = (offset_pixels / 640.0) * fov_degrees
        
        # Output fused threat state
        threat_detected = filtered_distance < self.threat_threshold_metres
        
        fused_state = {
            "distance_m": round(filtered_distance, 2),
            "azimuth_deg": round(azimuth_deg, 1),
            "threat_detected": threat_detected,
            "status": "CRITICAL_AVOID" if filtered_distance < 3.0 else "SAFE"
        }
        
        return fused_state

if __name__ == "__main__":
    node = SensorFusionNode()
    # Mock visual box of a bird [x, y, w, h] and raw LiDAR range of 8.2m
    mock_box = [280, 200, 80, 80]
    result = node.fuse_data(mock_box, 8.2)
    print(f"[Sensor Fusion] Fused state analysed: {result}")
