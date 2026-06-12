# backend/telemetry/px4_listener.py
"""
PX4 Telemetry Listener Daemon.
Listens to MAVLink telemetry streams from the autopilot and feeds them into the
FastAPI WebSocket, database, and MQTT ingestion pipeline.
Developed as part of the B.E. final year engineering design project.
"""

import sys
import os
import time
import logging
import threading

# Adjust path to import autonomous modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from autonomous.px4_mavlink_bridge import PX4MavlinkBridge
from backend.telemetry_service import TelemetryService

logging.basicConfig(level=logging.INFO, format="[Telemetry Listener] %(levelname)s: %(message)s")

class PX4TelemetryListener:
    def __init__(self, connection_string: str = "udp:127.0.0.1:14540", drone_id: str = "drone_01"):
        self.drone_id = drone_id
        self.bridge = PX4MavlinkBridge(connection_string=connection_string, force_mock=True)
        self.telemetry_service = TelemetryService()
        self.is_running = False
        self.thread = None

    def start(self):
        """Starts the background telemetry listening loop."""
        if self.is_running:
            logging.warning("Listener is already running.")
            return
            
        self.is_running = True
        self.bridge.connect()
        self.thread = threading.Thread(target=self._run_loop, daemon=True)
        self.thread.start()
        logging.info("PX4 Telemetry listener loop started in background.")

    def stop(self):
        """Stops the telemetry loop."""
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=2.0)
            logging.info("PX4 Telemetry listener loop stopped.")

    def _run_loop(self):
        while self.is_running:
            try:
                # Fetch telemetry snapshot from the bridge
                data = self.bridge.get_telemetry()
                
                # Format payload for the backend telemetry service
                payload = {
                    "latitude": data["latitude"],
                    "longitude": data["longitude"],
                    "altitude": data["altitude_m"],
                    "speed": data["speed_mps"],
                    "battery": data["battery_pct"],
                    "flight_mode": data["flight_mode"]
                }
                
                # Ingest into the telemetry service (database checks and MQTT alerts)
                self.telemetry_service.log_telemetry(self.drone_id, payload)
                
                time.sleep(1.0) # Poll rate (1Hz telemetry feed)
            except Exception as e:
                logging.error(f"Error in telemetry collection loop: {str(e)}")
                time.sleep(2.0)

if __name__ == "__main__":
    listener = PX4TelemetryListener()
    listener.start()
    try:
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        listener.stop()
