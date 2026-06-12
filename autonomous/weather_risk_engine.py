"""
Developed as an undergraduate engineering research and development project.

Module: Weather Risk Engine
Description: Assigns operational safety risk factor metrics based on wind speed and rain parameters.
"""

class WeatherRiskEngine:
    def __init__(self, max_safe_wind=12.0, max_safe_rain_pct=75.0):
        self.max_wind = max_wind_limit = max_safe_wind
        self.max_rain = max_safe_rain_pct

    def assess_risk(self, wind_mps, rain_pct):
        """
        Returns a risk classification dict.
        """
        is_wind_hazard = wind_mps > self.max_wind
        is_rain_hazard = rain_pct > self.max_rain
        
        if is_wind_hazard or is_rain_hazard:
            return {"status": "UNSAFE", "code": 100, "reason": "Precipitation/wind limits exceeded"}
        return {"status": "SAFE", "code": 0, "reason": "Weather conditions nominal"}
