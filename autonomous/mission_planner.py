"""
Developed as an undergraduate engineering research and development project.

Module: Mission Planner
Description: Generates waypoint route structures and coordinate steps for UAV flights.
"""

class MissionPlanner:
    def __init__(self, cruise_altitude_m=45.0):
        self.cruise_altitude = cruise_altitude_m

    def generate_flight_plan(self, start_lat, start_lon, dest_lat, dest_lon):
        """
        Creates waypoint arrays from origin to destination coordinates.
        """
        return [
            {"seq": 0, "command": "TAKEOFF", "lat": start_lat, "lon": start_lon, "alt": self.cruise_altitude},
            {"seq": 1, "command": "WAYPOINT", "lat": dest_lat, "lon": dest_lon, "alt": self.cruise_altitude},
            {"seq": 2, "command": "LAND", "lat": dest_lat, "lon": dest_lon, "alt": 0.0}
        ]
