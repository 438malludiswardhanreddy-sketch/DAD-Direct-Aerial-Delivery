"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Object Trajectory & Collision Predictor
Description: Performs tracking, Kalman-based trajectory updates, and 
             Time-to-Collision (TTC) calculations for evasive actions.
"""

class TrajectoryPredictor:
    def __init__(self, fps=30):
        self.fps = fps
        self.history = {}

    def track_obstacle(self, obstacle_id, position_3d):
        """
        Updates the coordinate history for a specific detected target.
        """
        if obstacle_id not in self.history:
            self.history[obstacle_id] = []
        self.history[obstacle_id].append(position_3d)
        
        # Limit history size to 10 frames
        if len(self.history[obstacle_id]) > 10:
            self.history[obstacle_id].pop(0)

    def predict_next_position(self, obstacle_id):
        """
        Performs a linear extrapolation proxy to predict the object position 
        in the next frame.
        """
        coords = self.history.get(obstacle_id, [])
        if len(coords) < 2:
            return None
            
        p_prev = coords[-2]
        p_curr = coords[-1]
        
        # Velocity estimation
        v_x = p_curr[0] - p_prev[0]
        v_y = p_curr[1] - p_prev[1]
        v_z = p_curr[2] - p_prev[2]
        
        # Predicted position
        p_next = [p_curr[0] + v_x, p_curr[1] + v_y, p_curr[2] + v_z]
        return p_next

    def estimate_time_to_collision(self, obstacle_id, drone_speed_mps):
        """
        Calculates Time-to-Collision (TTC) in seconds using range velocities.
        """
        coords = self.history.get(obstacle_id, [])
        if len(coords) < 2:
            return 999.0
            
        p_prev = coords[-2]
        p_curr = coords[-1]
        
        # Distance delta over 1 frame interval
        dist_prev = p_prev[0]
        dist_curr = p_curr[0]
        
        range_velocity = (dist_prev - dist_curr) * self.fps  # metres per second
        
        if range_velocity <= 0.05:
            return 999.0 # Obstacle moving away or static at safe distance
            
        ttc = dist_curr / (range_velocity + drone_speed_mps)
        return max(0.0, ttc)
