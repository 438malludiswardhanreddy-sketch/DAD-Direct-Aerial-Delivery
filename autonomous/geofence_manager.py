"""
Developed as an undergraduate engineering research and development project.

Module: Geofence Manager
Description: Assesses coordinate locations to ensure compliance with green, yellow, and red zones.
"""

import math

class GeofenceManager:
    def __init__(self, Solapur_centre=(17.6590, 75.9059), max_radius_metres=5000.0):
        self.centre_lat, self.centre_lon = Solapur_centre
        self.radius = max_radius_metres

    def is_within_fence(self, current_lat, current_lon):
        """
        Validates if coordinates remain inside the designated flight perimeter.
        """
        d_lat = current_lat - self.centre_lat
        d_lon = current_lon - self.centre_lon
        dist = math.sqrt(d_lat**2 + d_lon**2) * 111000.0
        
        return dist <= self.radius
