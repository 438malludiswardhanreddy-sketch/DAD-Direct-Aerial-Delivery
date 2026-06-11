"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Weather Monitor
Description: Reads simulated precipitation and wind velocities to adjust failsafe flight modes.
"""

class WeatherMonitor:
    def __init__(self, rain_threshold_percent=80.0, wind_limit_mps=15.0):
        self.rain_threshold = rain_threshold_percent
        self.wind_limit = wind_limit_mps
        print("[Autonomous] Weather monitor subsystem online.")

    def evaluate_flight_safety(self, current_rain_pct, current_wind_mps):
        """
        Analyses environment data to check if flight parameters are exceeded.
        """
        is_safe = True
        warnings = []

        if current_rain_pct >= self.rain_threshold:
            is_safe = False
            warnings.append(f"Precipitation level exceeds limit: {current_rain_pct}%")

        if current_wind_mps >= self.wind_limit:
            is_safe = False
            warnings.append(f"Wind velocity exceeds limit: {current_wind_mps} m/s")

        return {
            "flight_authorized": is_safe,
            "warnings": warnings,
            "recommended_action": "CONTINUE" if is_safe else "LAND_AT_NEAREST_HUB"
        }
