"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Obstacle Avoidance Engines
Description: Consolidates specialized engines for bypassing birds, wires, 
             trees, and building elements.
"""

class ObstacleAvoidanceEngine:
    def __init__(self, clearance_m=5.0):
        self.clearance = clearance_m

    def process_threat(self, threat):
        return {"action": "HOLD" if threat["distance_m"] < 2.0 else "STEER"}

class BirdAvoidanceEngine(ObstacleAvoidanceEngine):
    """
    Bird Avoidance Module: Bird obstacles exhibit dynamic, fast-changing vectors.
    Triggers sharp lateral yaw maneuvers.
    """
    def calculate_avoidance(self, threat):
        if threat["distance_m"] > 8.0:
            return 0.0
        # Fast evasive maneuver offset (up to 40 degrees)
        evasion_offset = -40.0 if threat["azimuth_deg"] >= 0 else 40.0
        print(f"[Failsafe] Bird detected! Initiating fast lateral evasive steer: {evasion_offset}°")
        return evasion_offset

class WireAvoidanceEngine(ObstacleAvoidanceEngine):
    """
    Wire Avoidance Module: Power lines and wires are thin and horizontal.
    Triggers vertical climb adjustments rather than horizontal yaw.
    """
    def calculate_climb(self, threat):
        if threat["distance_m"] > 10.0:
            return 0.0
        # Climb altitude adjustment (rise by 3.5 metres above threat)
        climb_adjust = 3.5
        print(f"[Failsafe] Wire detected ahead! Initiating target altitude climb: +{climb_adjust}m")
        return climb_adjust

class TreeAvoidanceEngine(ObstacleAvoidanceEngine):
    """
    Tree Avoidance Module: Trees are static canopy structures.
    Triggers standard yaw correction away from foliage.
    """
    def calculate_avoidance(self, threat):
        if threat["distance_m"] > 6.0:
            return 0.0
        yaw_offset = -20.0 if threat["azimuth_deg"] >= 0 else 20.0
        return yaw_offset

class BuildingAvoidanceEngine(ObstacleAvoidanceEngine):
    """
    Building Avoidance Module: High-rise concrete structures have massive bounding boxes.
    Requires wider horizontal clearance curves.
    """
    def calculate_avoidance(self, threat):
        if threat["distance_m"] > self.clearance:
            return 0.0
        # Wide detour offset
        yaw_offset = -35.0 if threat["azimuth_deg"] >= 0 else 35.0
        print(f"[Failsafe] Highrise building block detected! Engaging wide detour route: {yaw_offset}°")
        return yaw_offset

class ObstacleAvoidanceController(ObstacleAvoidanceEngine):
    def __init__(self, safe_clearance_metres=5.0):
        super().__init__(clearance_m=safe_clearance_metres)

    def calculate_avoidance_yaw(self, fused_threat):
        if not fused_threat["threat_detected"]:
            return 0.0
        dist = fused_threat["distance_m"]
        azimuth = fused_threat["azimuth_deg"]
        if dist < 2.0:
            return 999.0
        steering_sign = -1.0 if azimuth >= 0 else 1.0
        scaling_factor = (self.clearance / max(dist, 0.1)) * 15.0
        heading_offset = steering_sign * min(scaling_factor, 45.0)
        return heading_offset

