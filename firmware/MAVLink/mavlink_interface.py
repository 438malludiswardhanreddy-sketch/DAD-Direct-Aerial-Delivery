import time
import sys

# Mock pymavlink or MAVSDK bindings for compatibility/testing
class MavlinkInterface:
    def __init__(self, connection_string="/dev/ttyACM0", baudrate=57600):
        print(f"[MAVLink] Connecting to autopilot at {connection_string} ({baudrate} baud)...")
        self.connected = True
        self.drone_state = {
            "lat": 17.6590,
            "lon": 75.9059,
            "alt": 45.0,
            "heading": 90.0,
            "mode": "HOLD",
            "armed": False
        }

    def arm_disarm(self, arm_state: bool) -> bool:
        if arm_state:
            print("[MAVLink] Sending Arm command...")
            self.drone_state["armed"] = True
        else:
            print("[MAVLink] Sending Disarm command...")
            self.drone_state["armed"] = False
        return self.drone_state["armed"]

    def set_flight_mode(self, mode: str):
        valid_modes = ["GUIDED", "RTL", "AUTO", "HOLD", "LAND"]
        if mode in valid_modes:
            print(f"[MAVLink] Changing flight mode from {self.drone_state['mode']} to {mode}...")
            self.drone_state["mode"] = mode
            return True
        print(f"[MAVLink] Unsupported mode: {mode}")
        return False

    def send_global_coordinate_target(self, lat: float, lon: float, alt: float):
        if not self.drone_state["armed"]:
            print("[MAVLink] Warning: Cannot set target coordinates. Drone is disarmed.")
            return False
        
        self.set_flight_mode("GUIDED")
        print(f"[MAVLink] SET_POSITION_TARGET_GLOBAL_INT: Target Lat={lat}, Lon={lon}, Alt={alt}")
        self.drone_state["lat"] = lat
        self.drone_state["lon"] = lon
        self.drone_state["alt"] = alt
        return True

    def get_telemetry(self):
        return self.drone_state

if __name__ == "__main__":
    mav = MavlinkInterface()
    mav.arm_disarm(True)
    mav.send_global_coordinate_target(17.6599, 75.9064, 50.0)
    print(f"[MAVLink] State: {mav.get_telemetry()}")
