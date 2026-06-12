"""
Developed as an undergraduate engineering research and development project.

Module: Collision Predictor
Description: Performs Time-To-Collision (TTC) calculations on track states.
"""

class CollisionPredictor:
    def __init__(self, safe_ttc_seconds=3.0):
        self.safe_ttc = safe_ttc_seconds

    def estimate_ttc(self, distance_m, closing_speed_mps):
        """
        Calculates remaining seconds before expected impact.
        """
        if closing_speed_mps <= 0.05:
            return 999.0
            
        ttc = distance_m / closing_speed_mps
        return ttc

    def is_collision_imminent(self, distance_m, closing_speed_mps):
        return self.estimate_ttc(distance_m, closing_speed_mps) <= self.safe_ttc
