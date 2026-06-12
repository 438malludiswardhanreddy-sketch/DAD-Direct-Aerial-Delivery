# testing/px4_integration_test.py
"""
Integration tests for the PX4 MAVLink Bridge Subsystem.
Verifies mission synchronization, command translation, and telemetry aggregation.
Developed as part of the B.E. final year engineering design project.
"""

import unittest
import sys
import os

# Adjust path to import main packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from autonomous.px4_mavlink_bridge import PX4MavlinkBridge
from backend.telemetry.px4_listener import PX4TelemetryListener

class TestPX4MavlinkBridge(unittest.TestCase):
    def setUp(self):
        # Initialise with local loopback configuration and force mock mode for unit tests
        self.bridge = PX4MavlinkBridge(connection_string="udp:127.0.0.1:14540", force_mock=True)

    def test_bridge_connection(self):
        """Verifies that the MAVLink bridge connects successfully (falls back to mock if needed)."""
        success = self.bridge.connect()
        self.assertTrue(success, "Bridge connection should return True.")
        self.assertTrue(self.bridge.is_connected, "Bridge should show connected status.")

    def test_mission_upload(self):
        """Verifies waypoint parsing and upload loop execution."""
        self.bridge.connect()
        waypoints = [
            {"lat": 17.6610, "lon": 75.9070, "alt": 45.0},
            {"lat": 17.6635, "lon": 75.9090, "alt": 30.0}
        ]
        success = self.bridge.upload_mission(waypoints)
        self.assertTrue(success, "Mission upload sequence should complete successfully.")

    def test_telemetry_polling(self):
        """Verifies telemetry data structure is populated and holds expected fields."""
        self.bridge.connect()
        telemetry_data = self.bridge.get_telemetry()
        
        # Verify structure keys
        self.assertIn("latitude", telemetry_data)
        self.assertIn("longitude", telemetry_data)
        self.assertIn("altitude_m", telemetry_data)
        self.assertIn("speed_mps", telemetry_data)
        self.assertIn("battery_pct", telemetry_data)
        self.assertIn("flight_mode", telemetry_data)

class TestPX4TelemetryListener(unittest.TestCase):
    def test_listener_lifecycle(self):
        """Verifies starting and stopping the background telemetry daemon."""
        listener = PX4TelemetryListener()
        self.assertFalse(listener.is_running)
        listener.start()
        self.assertTrue(listener.is_running)
        listener.stop()
        self.assertFalse(listener.is_running)

if __name__ == "__main__":
    unittest.main()

