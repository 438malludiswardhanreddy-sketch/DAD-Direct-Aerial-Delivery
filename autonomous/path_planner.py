"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Path Planning Subsystems
Description: Dynamic trajectory planning and weather-aware route adjustments.
"""

import math

class DynamicPathPlanner:
    def __init__(self, step_size_m=5.0):
        self.step_size = step_size_m

    def generate_waypoints(self, start_gps, dest_gps, altitude=45.0):
        """
        Generates linear waypoint coordinate paths from start coordinates to destination coordinates.
        """
        lat_start, lon_start = start_gps
        lat_dest, lon_dest = dest_gps
        
        # Calculate coordinate distances
        d_lat = lat_dest - lat_start
        d_lon = lon_dest - lon_start
        total_dist = math.sqrt(d_lat**2 + d_lon**2) * 111000.0 # Metre conversion proxy
        
        num_steps = max(int(total_dist / self.step_size), 2)
        route = []
        for i in range(num_steps + 1):
            alpha = i / num_steps
            lat = lat_start + alpha * d_lat
            lon = lon_start + alpha * d_lon
            route.append({"lat": lat, "lon": lon, "alt": altitude})
            
        return route

class WeatherAwarePlanner:
    def __init__(self, max_wind_limit=12.0):
        self.wind_limit = max_wind_limit

    def adapt_path(self, route, current_wind_mps, is_rainy=False):
        """
        Adjusts target altitude or reroutes depending on meteorological conditions.
        """
        if is_rainy:
            print("[Weather Planner] Precipitation exceeds flight parameters. Dropping cruise altitude by 10m to improve visibility.")
            for wp in route:
                wp["alt"] = max(20.0, wp["alt"] - 10.0)
                
        if current_wind_mps > self.wind_limit:
            print("[Weather Planner] Wind velocity too high. Engaging emergency hover failsafe.")
            return [] # Empty route indicates immediate hold command
            
        return route
