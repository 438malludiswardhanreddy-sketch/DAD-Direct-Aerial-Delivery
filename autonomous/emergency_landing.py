"""
Developed as an undergraduate engineering research and development project.

Module: Emergency Landing Planner
Description: Searches for the closest safe landing zones/hubs during failsafes.
"""

import math

class EmergencyLandingPlanner:
    def __init__(self):
        # Designated Solapur landing platforms
        self.platforms = [
            {"id": "platform_launch", "lat": 17.6590, "lon": 75.9059},
            {"id": "platform_north", "lat": 17.6721, "lon": 75.9125},
            {"id": "platform_south", "lat": 17.6410, "lon": 75.8950}
        ]

    def find_nearest_platform(self, current_lat, current_lon):
        """
        Locates coordinates of the closest landing platform.
        """
        nearest = self.platforms[0]
        min_dist = float('inf')
        for p in self.platforms:
            d_lat = p["lat"] - current_lat
            d_lon = p["lon"] - current_lon
            dist = math.sqrt(d_lat**2 + d_lon**2)
            if dist < min_dist:
                min_dist = dist
                nearest = p
        return nearest
