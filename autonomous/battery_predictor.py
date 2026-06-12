"""
Developed as an undergraduate engineering research and development project.

Module: Battery Predictor
Description: Calculates remaining voltage and capacity profiles to predict flight time.
"""

class BatteryPredictor:
    def __init__(self, capacity_mah=16000.0):
        self.capacity = capacity_mah

    def predict_flight_time_seconds(self, cell_voltage, current_draw):
        """
        Estimates operational seconds left before battery reaches 20% limit.
        """
        if current_draw <= 0.1:
            return 99999.0
            
        remaining_fraction = max(0.0, (cell_voltage - 3.5) / (4.2 - 3.5))
        remaining_mah = remaining_fraction * self.capacity
        # Current in Amps to mA
        discharge_rate_ma = current_draw * 1000.0
        
        hours_remaining = remaining_mah / discharge_rate_ma
        return hours_remaining * 3600.0
