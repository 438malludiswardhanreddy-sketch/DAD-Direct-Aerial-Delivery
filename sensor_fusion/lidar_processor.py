"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: LiDAR Range Processor
Description: Standardises and parses serial streams from Benewake TFmini sensors, 
             converting values into metric units and filtering signal noise.
"""

class LidarProcessor:
    def __init__(self, max_range_m=12.0):
        self.max_range = max_range_m
        print("[Sensor Fusion] LiDAR range processor module initialised.")

    def parse_serial_reading(self, raw_buffer):
        """
        Parses TFmini serial data packet (usually 9 bytes starting with 0x59 0x59).
        Calculates distance values in metres.
        """
        # TFmini protocol mock check
        if len(raw_buffer) < 9:
            return -1.0 # Invalid frame length
            
        if raw_buffer[0] != 0x59 or raw_buffer[1] != 0x59:
            return -1.0 # Invalid header bytes
            
        # Dist_L (Byte 2) and Dist_H (Byte 3) represent distance in cm
        dist_cm = raw_buffer[2] + raw_buffer[3] * 256
        dist_m = dist_cm / 100.0
        
        # Clamp value within sensor range limits
        if dist_m > self.max_range:
            return self.max_range
        return dist_m
