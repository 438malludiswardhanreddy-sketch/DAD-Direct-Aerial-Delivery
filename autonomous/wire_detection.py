"""
Developed as an undergraduate engineering research and development project.

Module: Wire Detection & Avoidance
Description: Triggers vertical climb offsets to clear horizontal overhead structures.
"""

class WireAvoidanceEngine:
    def __init__(self, climb_clearance_m=3.5):
        self.climb = climb_clearance_m

    def check_wire_hazard(self, wire_threat):
        """
        Calculates altitude adjustment values.
        """
        if wire_threat["distance_m"] > 10.0:
            return 0.0 # Safe distance
            
        print(f"[Wire Avoidance] Adjusting flight plan altitude by +{self.climb}m.")
        return self.climb
