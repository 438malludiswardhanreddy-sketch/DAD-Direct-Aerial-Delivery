"""
Developed as an undergraduate engineering research and development project.

Module: Bird Avoidance Engine
Description: Recalculates yaw angles to steer around dynamic flying obstacles (birds).
"""

class BirdAvoidanceEngine:
    def __init__(self, safe_distance_m=8.0):
        self.safe_dist = safe_distance_m

    def avoid_bird(self, bird_threat):
        """
        Determines if immediate evasive steer action is required.
        """
        if bird_threat["distance_m"] >= self.safe_dist:
            return 0.0 # No action required
            
        # Steer sharply in opposite direction
        return -35.0 if bird_threat["azimuth_deg"] >= 0 else 35.0
