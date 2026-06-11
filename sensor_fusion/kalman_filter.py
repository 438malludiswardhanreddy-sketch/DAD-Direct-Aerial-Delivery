"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Range Kalman Filter
Description: Performs recursive state estimation to filter noise from LiDAR range readings.
"""

class RangeKalmanFilter:
    def __init__(self, process_variance=1e-5, measurement_variance=1e-2):
        # Initial estimate parameters
        self.post_state = 0.0     # posteriori state estimate
        self.post_error = 1.0     # posteriori error covariance
        
        # System parameters
        self.q = process_variance  # process variance
        self.r = measurement_variance # measurement variance

    def filter(self, measurement):
        """
        Executes Kalman filter iteration step.
        """
        if self.post_state == 0.0:
            self.post_state = measurement
            return measurement
            
        # Time Update (Predict)
        prior_state = self.post_state
        prior_error = self.post_error + self.q
        
        # Measurement Update (Correct)
        kalman_gain = prior_error / (prior_error + self.r)
        self.post_state = prior_state + kalman_gain * (measurement - prior_state)
        self.post_error = (1 - kalman_gain) * prior_error
        
        return self.post_state
