"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: DAD System Test Suite
Description: Unit tests for sensor fusion, autonomous guidance, and backend databases.
"""

import sys
import os
import unittest

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sensor_fusion.sensor_fusion_node import SensorFusionNode
from sensor_fusion.kalman_filter import RangeKalmanFilter
from sensor_fusion.camera_detection import CameraObstacleDetector
from sensor_fusion.lidar_processor import LidarProcessor
from autonomous.obstacle_avoidance import ObstacleAvoidanceController
from autonomous.weather_monitor import WeatherMonitor
from backend.database.models import DroneModel

class TestDADSystem(unittest.TestCase):
    
    def test_camera_detection(self):
        detector = CameraObstacleDetector(confidence_cutoff=0.6)
        mock_raw = [
            {"class": "wire", "confidence": 0.85, "bbox": [280, 200, 80, 20]},
            {"class": "bird", "confidence": 0.42, "bbox": [120, 90, 30, 20]}
        ]
        results = detector.parse_detections(frame_id=101, mock_onnx_outputs=mock_raw)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["class_name"], "wire")
        self.assertEqual(results[0]["confidence"], 0.85)

    def test_lidar_processor(self):
        processor = LidarProcessor(max_range_m=12.0)
        
        # Valid 9-byte TFmini buffer: 0x59 0x59 Dist_L=100 Dist_H=0 Strength_L=0 Strength_H=0 Temp_L=0 Temp_H=0
        # 100cm = 1.0m
        valid_buf = [0x59, 0x59, 100, 0, 0, 0, 0, 0, 0]
        dist = processor.parse_serial_reading(valid_buf)
        self.assertAlmostEqual(dist, 1.0, places=2)
        
        # Invalid buffer header
        invalid_buf = [0x00, 0x00, 100, 0, 0, 0, 0, 0, 0]
        dist_err = processor.parse_serial_reading(invalid_buf)
        self.assertEqual(dist_err, -1.0)

    def test_kalman_filter(self):
        kf = RangeKalmanFilter()
        readings = [5.2, 4.8, 5.1, 4.9, 5.0]
        filtered = 0.0
        for r in readings:
            filtered = kf.filter(r)
        self.assertAlmostEqual(filtered, 5.0, places=1)

    def test_sensor_fusion(self):
        node = SensorFusionNode()
        mock_box = [280, 200, 80, 80]
        res = node.fuse_data(mock_box, 8.2)
        self.assertIn("distance_m", res)
        self.assertTrue(res["threat_detected"])

    def test_obstacle_avoidance(self):
        controller = ObstacleAvoidanceController(safe_clearance_metres=5.0)
        threat = {
            "distance_m": 4.0,
            "azimuth_deg": 10.0,
            "threat_detected": True
        }
        offset = controller.calculate_avoidance_yaw(threat)
        self.assertLess(offset, 0.0) # Correct steering direction

    def test_weather_monitor(self):
        monitor = WeatherMonitor()
        res = monitor.evaluate_flight_safety(current_rain_pct=90.0, current_wind_mps=5.0)
        self.assertFalse(res["flight_authorized"])
        self.assertEqual(res["recommended_action"], "LAND_AT_NEAREST_HUB")

    def test_database_init(self):
        db_path = "test_dad_logistics.db"
        if os.path.exists(db_path):
            os.remove(db_path)
            
        # Re-importing legacy manager pattern for schema verification
        # or verify SQLite engine initialization
        from backend.database.db_session import engine, init_db, SessionLocal
        init_db()
        
        db = SessionLocal()
        drone = db.query(DroneModel).filter(DroneModel.id == "drone_01").first()
        self.assertIsNotNone(drone)
        self.assertEqual(drone.status, "Active")
        db.close()
        
        # Cleanup
        if os.path.exists(db_path):
            os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
