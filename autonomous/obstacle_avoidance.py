"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Obstacle Avoidance Guidance
Description: Dynamically recalculates path vector adjust variables to bypass obstacles.
"""

class ObstacleAvoidanceController:
    def __init__(self, safe_clearance_metres=5.0):
        self.clearance = safe_clearance_metres
        print("[Autonomous] Autonomous path guidance controller initialised.")

    def calculate_avoidance_yaw(self, fused_threat):
        """
        Analyses threat states and provides a corrected heading offset in degrees.
        """
        if not fused_threat["threat_detected"]:
            return 0.0 # Proceed on track

        # If range is critically low, signal emergency brake
        dist = fused_threat["distance_m"]
        azimuth = fused_threat["azimuth_deg"]

        if dist < 2.0:
            print("[Autonomous] Urgent: Obstacle distance below safety limit! Engaging brakes.")
            return 999.0 # Special indicator code for override hover

        # Calculate steering offset in opposite direction to threat azimuth
        steering_sign = -1.0 if azimuth >= 0 else 1.0
        
        # Steering angle increases as threat distance decreases
        scaling_factor = (self.clearance / max(dist, 0.1)) * 15.0
        heading_offset = steering_sign * min(scaling_factor, 45.0) # Cap offset at 45 degrees
        
        print(f"[Autonomous] Corrective trajectory recalculation: Heading Offset = {heading_offset:.1f} degrees.")
        return heading_offset
