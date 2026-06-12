# autonomous/px4_mavlink_bridge.py
"""
PX4 Autopilot MAVLink Bridge Subsystem.
Handles physical communication with PX4 SITL or flight controllers via pymavlink,
including mission uploading and live telemetry aggregation.
Developed as part of the B.E. final year engineering design project.
"""

import sys
import time
import logging

logging.basicConfig(level=logging.INFO, format="[MAVLink Bridge] %(levelname)s: %(message)s")

# Gracefully handle environment setup without pymavlink
MAVLINK_AVAILABLE = False
try:
    from pymavlink import mavutil
    MAVLINK_AVAILABLE = True
except ImportError:
    logging.warning("pymavlink library not detected on the host system. Initialising Simulation Mock Mode.")

class PX4MavlinkBridge:
    def __init__(self, connection_string: str = "udp:127.0.0.1:14540", system_id: int = 1, force_mock: bool = False):
        self.connection_string = connection_string
        self.system_id = system_id
        self.connection = None
        self.is_connected = False
        self.mock_mode = force_mock or not MAVLINK_AVAILABLE
        
        # Telemetry Cache
        self.telemetry = {
            "latitude": 17.6590,
            "longitude": 75.9059,
            "altitude_m": 0.0,
            "speed_mps": 0.0,
            "battery_pct": 100.0,
            "flight_mode": "DISARMED",
            "heartbeat_recv": False
        }

    def connect(self) -> bool:
        """Establishes connection to the PX4 autopilot."""
        if self.mock_mode:
            logging.info(f"Connecting to MAVLink endpoint {self.connection_string} (MOCK ACTIVE)")
            self.is_connected = True
            self.telemetry["heartbeat_recv"] = True
            return True
            
        try:
            logging.info(f"Connecting to physical MAVLink endpoint {self.connection_string}...")
            self.connection = mavutil.mavlink_connection(self.connection_string)
            # Wait for heartbeat
            logging.info("Waiting for PX4 autopilot heartbeat...")
            self.connection.wait_heartbeat(timeout=5.0)
            logging.info(f"Heartbeat received from System ID: {self.connection.target_system}")
            self.is_connected = True
            self.telemetry["heartbeat_recv"] = True
            return True
        except Exception as e:
            logging.error(f"Failed to connect to PX4 SITL: {str(e)}. Falling back to Mock Mode.")
            self.mock_mode = True
            self.is_connected = True
            self.telemetry["heartbeat_recv"] = True
            return True

    def upload_mission(self, waypoints: list) -> bool:
        """
        Uploads a list of waypoints to the PX4 Autopilot.
        Waypoints are dicts: {"lat": float, "lon": float, "alt": float}
        """
        if not self.is_connected:
            logging.error("Cannot upload mission: Not connected to autopilot.")
            return False
            
        logging.info(f"Preparing to upload mission with {len(waypoints)} waypoints...")
        
        if self.mock_mode:
            for idx, wp in enumerate(waypoints):
                logging.info(f"[Mock Upload] Waypoint {idx+1}: Lat={wp['lat']}, Lon={wp['lon']}, Alt={wp['alt']}m")
            time.sleep(0.1) # Simulate transmission delay
            logging.info("Mission upload successful (MOCK).")
            return True
            
        try:
            # Clear existing mission
            self.connection.mav.mission_clear_all_send(self.connection.target_system, self.connection.target_component)
            
            # Send mission count
            count = len(waypoints) + 1 # +1 for takeoff/home waypoint
            self.connection.mav.mission_count_send(self.connection.target_system, self.connection.target_component, count)
            
            # Upload loops
            for i in range(count):
                msg = self.connection.recv_match(type='MISSION_REQUEST', blocking=True, timeout=2.0)
                if not msg:
                    logging.error("Mission upload timed out waiting for request.")
                    return False
                    
                seq = msg.seq
                if seq == 0:
                    # Home / Takeoff
                    self.connection.mav.mission_item_int_send(
                        self.connection.target_system, self.connection.target_component, seq,
                        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
                        mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
                        1, 1, 0, 0, 0, 0,
                        int(self.telemetry["latitude"] * 1e7),
                        int(self.telemetry["longitude"] * 1e7),
                        15.0 # Takeoff altitude
                    )
                else:
                    wp = waypoints[seq - 1]
                    self.connection.mav.mission_item_int_send(
                        self.connection.target_system, self.connection.target_component, seq,
                        mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,
                        mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
                        0, 1, 0, 0, 0, 0,
                        int(wp["lat"] * 1e7),
                        int(wp["lon"] * 1e7),
                        wp["alt"]
                    )
                    
            # Wait for mission ack
            ack = self.connection.recv_match(type='MISSION_ACK', blocking=True, timeout=2.0)
            if ack and ack.type == mavutil.mavlink.MAV_MISSION_ACCEPTED:
                logging.info("Mission upload verified and accepted by PX4 flight controller.")
                return True
            else:
                logging.error("Mission upload failed or rejected by autopilot.")
                return False
        except Exception as e:
            logging.error(f"Error occurred during MAVLink mission upload: {str(e)}")
            return False

    def update_telemetry(self):
        """Polls the MAVLink connection for latest state estimates."""
        if not self.is_connected:
            return
            
        if self.mock_mode:
            # Simulate slight fluctuations in state telemetry
            self.telemetry["altitude_m"] = max(0.0, self.telemetry["altitude_m"] + 0.1)
            self.telemetry["battery_pct"] = max(15.0, self.telemetry["battery_pct"] - 0.05)
            self.telemetry["flight_mode"] = "GUIDED" if self.telemetry["altitude_m"] > 5.0 else "TAKEOFF"
            return
            
        try:
            # Read non-blocking messages
            msg = self.connection.recv_match(blocking=False)
            while msg is not None:
                msg_type = msg.get_type()
                
                if msg_type == "GLOBAL_POSITION_INT":
                    self.telemetry["latitude"] = msg.lat / 1e7
                    self.telemetry["longitude"] = msg.lon / 1e7
                    self.telemetry["altitude_m"] = msg.relative_alt / 1000.0
                    self.telemetry["speed_mps"] = ((msg.vx**2 + msg.vy**2)**0.5) / 100.0
                    
                elif msg_type == "SYS_STATUS":
                    self.telemetry["battery_pct"] = msg.battery_remaining
                    
                elif msg_type == "HEARTBEAT":
                    # Decode base mode / custom mode if possible
                    self.telemetry["flight_mode"] = mavutil.mode_string_v10(msg)
                    self.telemetry["heartbeat_recv"] = True
                    
                msg = self.connection.recv_match(blocking=False)
        except Exception as e:
            logging.debug(f"Telemetry parsing idle or read error: {str(e)}")

    def get_telemetry(self) -> dict:
        """Returns the current telemetry snapshot."""
        self.update_telemetry()
        return self.telemetry

if __name__ == "__main__":
    bridge = PX4MavlinkBridge()
    if bridge.connect():
        print("Connected! Initialising telemetry poll stream (Ctrl+C to stop)...")
        try:
            while True:
                data = bridge.get_telemetry()
                print(f"\r[Telemetry] Mode={data['flight_mode']} | Lat={data['latitude']:.5f} | Alt={data['altitude_m']:.1f}m | Bat={data['battery_pct']}%", end="")
                time.sleep(1.0)
        except KeyboardInterrupt:
            print("\nExiting telemetry poll stream.")
