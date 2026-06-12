"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Failsafe Engines
Description: Handles emergency landing hub selection, battery range prediction, 
             and operational risk index assessments.
"""

import math

class EmergencyLandingPlanner:
    def __init__(self):
        # Solapur region coordinate landing hubs
        self.hubs = [
            {"id": "hub_solapur_south", "lat": 17.6410, "lon": 75.8950},
            {"id": "hub_solapur_north", "lat": 17.6721, "lon": 75.9125},
            {"id": "hub_launch_station", "lat": 17.6590, "lon": 75.9059}
        ]

    def select_nearest_hub(self, drone_lat, drone_lon):
        """
        Determines the closest safe landing hub to the drone coordinates.
        """
        min_dist = float('inf')
        selected_hub = self.hubs[0]
        
        for hub in self.hubs:
            d_lat = hub["lat"] - drone_lat
            d_lon = hub["lon"] - drone_lon
            dist = math.sqrt(d_lat**2 + d_lon**2) * 111000.0
            if dist < min_dist:
                min_dist = dist
                selected_hub = hub
                
        return selected_hub

class BatteryPredictionEngine:
    def __init__(self, mah_capacity=16000.0):
        self.capacity = mah_capacity

    def predict_remaining_range_m(self, voltage, current_draw, speed_mps):
        """
        Calculates safe remaining flight distance based on current discharge rates.
        """
        # Convert Current (Amps) to discharge rate
        if current_draw <= 0.1:
            return 99999.0
        # Remaining range calculation proxy
        capacity_fraction = (voltage / 25.2)  # Assuming 6S battery
        remaining_capacity_mah = capacity_fraction * self.capacity
        hours_remaining = remaining_capacity_mah / (current_draw * 1000.0)
        
        remaining_metres = hours_remaining * 3600.0 * speed_mps
        return max(0.0, remaining_metres)

class RiskAssessmentEngine:
    def calculate_risk_index(self, drone_alt_m, speed_mps, is_over_populated=False):
        """
        Generates a dynamic risk score between 1 (safe) and 10 (unsafe).
        """
        risk_score = 1
        
        # Lower altitudes increase ground collision risk
        if drone_alt_m < 20.0:
            risk_score += 3
        elif drone_alt_m > 80.0:
            risk_score += 1 # High altitude airspace clearance risk
            
        # Speeds above cruise speed increase momentum hazards
        if speed_mps > 15.0:
            risk_score += 2
            
        # Population density proxy impact
        if is_over_populated:
            risk_score += 4
            
        return min(risk_score, 10)
