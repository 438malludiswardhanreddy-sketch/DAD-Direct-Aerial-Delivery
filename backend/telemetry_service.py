"""
Developed as an undergraduate engineering research and development project.

Module: Telemetry Service
Description: Validates, logs, and processes telemetry streams from companion computer.
"""

class TelemetryService:
    def __init__(self):
        self.logs_history = {}

    def log_telemetry(self, drone_id: str, telemetry_data: dict):
        """
        Stores telemetry records in memory for quick history access.
        """
        if drone_id not in self.logs_history:
            self.logs_history[drone_id] = []
        
        self.logs_history[drone_id].append(telemetry_data)
        if len(self.logs_history[drone_id]) > 100:
            self.logs_history[drone_id].pop(0)

        # Basic alert threshold verification
        alerts = []
        if telemetry_data.get("battery", 100.0) <= 20.0:
            alerts.append("LOW_BATTERY_WARNING")
        
        return alerts
