"""
Developed as an undergraduate engineering research and development project.

Module: Route Optimizer
Description: Adjusts waypoints dynamically to bypass no-fly zones and wind resistance.
"""

import math

class RouteOptimizer:
    def optimize_waypoints(self, waypoints, hazards):
        """
        Alters flight path nodes slightly to steer away from known hazard zones.
        """
        optimized = []
        for wp in waypoints:
            lat, lon = wp["lat"], wp["lon"]
            for hz in hazards:
                d_lat = hz["lat"] - lat
                d_lon = hz["lon"] - lon
                dist = math.sqrt(d_lat**2 + d_lon**2) * 111000.0
                if dist < 50.0:  # Within 50 metres of a static hazard
                    # Offset waypoint coordinate away from hazard center
                    lat -= (d_lat / dist) * 10.0 / 111000.0
                    lon -= (d_lon / dist) * 10.0 / 111000.0
            optimized.append({"seq": wp["seq"], "command": wp["command"], "lat": lat, "lon": lon, "alt": wp["alt"]})
        return optimized
