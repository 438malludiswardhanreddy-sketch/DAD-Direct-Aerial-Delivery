"""
Developed as an undergraduate engineering research and development project.

Module: MQTT Client Link
Description: Simulates telemetry broker connections publishing to 'solapur/telemetry'.
"""

class TelemetryMqttClient:
    def __init__(self, broker_address="localhost", port=1883):
        self.broker = broker_address
        self.port = port
        self.connected = False

    def connect(self):
        print(f"[MQTT] Connecting to broker at {self.broker}:{self.port}...")
        self.connected = True
        return True

    def publish_telemetry(self, topic: str, payload: dict):
        if not self.connected:
            print("[MQTT] Warning: Cannot publish, client disconnected.")
            return False
            
        print(f"[MQTT] Publish to '{topic}': {payload}")
        return True
