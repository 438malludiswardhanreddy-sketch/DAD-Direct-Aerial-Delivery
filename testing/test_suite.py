"""
Developed as an undergraduate engineering research and development project.

Module: DAD System Test Suite
Description: Unit tests verifying sensor fusion, autonomous failsafes, and backend services.
"""

import sys
import os
import unittest

# Ensure parent directory is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import core modules
from sensor_fusion.sensor_fusion_node import SensorFusionNode
from sensor_fusion.kalman_filter import RangeKalmanFilter
from sensor_fusion.camera_detection import CameraObstacleDetector
from sensor_fusion.lidar_processor import LidarProcessor

# Import new autonomous modules
from autonomous.obstacle_avoidance import ObstacleAvoidanceController
from autonomous.weather_monitor import WeatherMonitor
from autonomous.mission_planner import MissionPlanner
from autonomous.route_optimizer import RouteOptimizer
from autonomous.battery_predictor import BatteryPredictor
from autonomous.emergency_landing import EmergencyLandingPlanner
from autonomous.weather_risk_engine import WeatherRiskEngine
from autonomous.geofence_manager import GeofenceManager
from autonomous.bird_avoidance import BirdAvoidanceEngine
from autonomous.wire_detection import WireAvoidanceEngine
from autonomous.collision_predictor import CollisionPredictor

# Import new backend modules
from backend.telemetry_service import TelemetryService
from backend.mqtt_client import TelemetryMqttClient
from backend.websocket_manager import TelemetryWebSocketManager
from backend.mission_service import MissionService
from backend.drone_registry import DroneRegistry
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

    def test_lidar_processor(self):
        processor = LidarProcessor(max_range_m=12.0)
        valid_buf = [0x59, 0x59, 100, 0, 0, 0, 0, 0, 0]
        dist = processor.parse_serial_reading(valid_buf)
        self.assertAlmostEqual(dist, 1.0)

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

    def test_obstacle_avoidance(self):
        controller = ObstacleAvoidanceController(safe_clearance_metres=5.0)
        threat = {"distance_m": 4.0, "azimuth_deg": 10.0, "threat_detected": True}
        offset = controller.calculate_avoidance_yaw(threat)
        self.assertLess(offset, 0.0)

    def test_weather_monitor(self):
        monitor = WeatherMonitor()
        res = monitor.evaluate_flight_safety(current_rain_pct=90.0, current_wind_mps=5.0)
        self.assertFalse(res["flight_authorized"])

    def test_mission_planner(self):
        mp = MissionPlanner()
        plan = mp.generate_flight_plan(17.6590, 75.9059, 17.6721, 75.9125)
        self.assertEqual(len(plan), 3)
        self.assertEqual(plan[0]["command"], "TAKEOFF")

    def test_route_optimizer(self):
        ro = RouteOptimizer()
        wps = [{"seq": 1, "command": "WAYPOINT", "lat": 17.6600, "lon": 75.9060, "alt": 45.0}]
        hazards = [{"lat": 17.6601, "lon": 75.9061}]
        opt = ro.optimize_waypoints(wps, hazards)
        self.assertNotEqual(opt[0]["lat"], wps[0]["lat"])

    def test_battery_predictor(self):
        bp = BatteryPredictor()
        time_left = bp.predict_flight_time_seconds(cell_voltage=4.0, current_draw=10.0)
        self.assertGreater(time_left, 0.0)

    def test_emergency_landing(self):
        el = EmergencyLandingPlanner()
        platform = el.find_nearest_platform(17.6601, 75.9082)
        self.assertEqual(platform["id"], "platform_launch")

    def test_weather_risk_engine(self):
        wre = WeatherRiskEngine()
        risk = wre.assess_risk(wind_mps=15.0, rain_pct=10.0)
        self.assertEqual(risk["status"], "UNSAFE")

    def test_geofence_manager(self):
        gm = GeofenceManager()
        self.assertTrue(gm.is_within_fence(17.6600, 75.9060))
        self.assertFalse(gm.is_within_fence(18.9000, 78.9000))

    def test_bird_avoidance(self):
        ba = BirdAvoidanceEngine()
        steer = ba.avoid_bird({"distance_m": 4.0, "azimuth_deg": 10.0})
        self.assertEqual(steer, -35.0)

    def test_wire_detection(self):
        wa = WireAvoidanceEngine()
        climb = wa.check_wire_hazard({"distance_m": 5.0})
        self.assertEqual(climb, 3.5)

    def test_collision_predictor(self):
        cp = CollisionPredictor()
        self.assertTrue(cp.is_collision_imminent(distance_m=10.0, closing_speed_mps=5.0))

    def test_backend_services(self):
        # Telemetry Service
        ts = TelemetryService()
        alerts = ts.log_telemetry("drone_01", {"battery": 15.0})
        self.assertIn("LOW_BATTERY_WARNING", alerts)
        
        # MQTT Client
        mc = TelemetryMqttClient()
        mc.connect()
        self.assertTrue(mc.publish_telemetry("solapur/telemetry", {"battery": 80.0}))
        
        # WS Manager
        wm = TelemetryWebSocketManager()
        wm.register_client("dummy_ws")
        self.assertEqual(wm.broadcast({"battery": 80.0}), 1)
        
        # Mission Service
        ms = MissionService()
        clearance = ms.verify_npnt_clearance("drone_01", 17.6590, 75.9059)
        self.assertTrue(clearance["authorized"])
        
        # Drone Registry
        dr = DroneRegistry()
        self.assertTrue(dr.register("drone_04", "Tarot 680Pro Hexacopter", 88.0))
        self.assertEqual(dr.get_drone("drone_04")["battery"], 88.0)

    def test_database_init(self):
        db_path = "test_dad_logistics.db"
        if os.path.exists(db_path):
            os.remove(db_path)
            
        from backend.database.db_session import engine, init_db, SessionLocal
        init_db()
        
        db = SessionLocal()
        drone = db.query(DroneModel).filter(DroneModel.id == "drone_01").first()
        self.assertIsNotNone(drone)
        db.close()
        
        if os.path.exists(db_path):
            os.remove(db_path)

if __name__ == "__main__":
    unittest.main()
