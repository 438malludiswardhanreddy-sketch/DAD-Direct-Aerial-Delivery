import sys
import os
import unittest

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sensor_fusion.sensor_fusion_node import SensorFusionNode
from sensor_fusion.kalman_filter import RangeKalmanFilter
from autonomous.obstacle_avoidance import ObstacleAvoidanceController
from autonomous.weather_monitor import WeatherMonitor
from backend.database import DatabaseManager

class TestDADSystem(unittest.TestCase):
    def test_kalman_filter(self):
        kf = RangeKalmanFilter()
        # Feed readings converging on 5.0m
        readings = [5.2, 4.8, 5.1, 4.9, 5.0]
        filtered = 0.0
        for r in readings:
            filtered = kf.filter(r)
        self.assertAlmostEqual(filtered, 5.0, places=1)

    def test_sensor_fusion(self):
        node = SensorFusionNode()
        # Mock visual box and range
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
        self.assertLess(offset, 0.0) # Steering away from positive azimuth angle

    def test_weather_monitor(self):
        monitor = WeatherMonitor()
        res = monitor.evaluate_flight_safety(current_rain_pct=90.0, current_wind_mps=5.0)
        self.assertFalse(res["flight_authorized"])
        self.assertEqual(res["recommended_action"], "LAND_AT_NEAREST_HUB")

    def test_database_init(self):
        db_path = "test_dad_logistics.db"
        if os.path.exists(db_path):
            os.remove(db_path)
            
        db = DatabaseManager(db_path)
        drones = db.get_all_drones()
        self.assertEqual(len(drones), 3)
        self.assertEqual(drones[0]["id"], "drone_01")
        
        # Cleanup
        if os.path.exists(db_path):
            os.remove(db_path)

if __name__ == "__main__":
    unittest.main()

