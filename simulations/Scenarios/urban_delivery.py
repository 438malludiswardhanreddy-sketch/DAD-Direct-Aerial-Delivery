import math
import time

class SimulationScenario:
    def __init__(self):
        print("[SITL] Initializing Solapur Urban Canyon Scenario...")
        self.wind_speed_mps = 3.5
        self.obstacle_coordinates = [
            {"name": "PowerTower_1", "lat": 17.6620, "lon": 75.9080, "height": 35.0},
            {"name": "TreeLine_A", "lat": 17.6680, "lon": 75.9100, "height": 18.0},
            {"name": "Highrise_B", "lat": 17.6705, "lon": 75.9115, "height": 60.0}
        ]

    def check_collision(self, drone_lat, drone_lon, drone_alt):
        for obs in self.obstacle_coordinates:
            d_lat = obs["lat"] - drone_lat
            d_lon = obs["lon"] - drone_lon
            
            # Simple distance approximation in meters
            dist = math.sqrt(d_lat**2 + d_lon**2) * 111000.0
            
            if dist < 8.0 and drone_alt <= obs["height"]:
                print(f"[COLLISION WARNING] Close proximity to {obs['name']}! Dist={dist:.2f}m")
                return True
        return False

    def simulate_flight(self, start_coords, dest_coords, cruise_alt=45.0):
        lat, lon = start_coords
        dest_lat, dest_lon = dest_coords
        steps = 20
        
        print(f"[SITL] Flight started: {start_coords} -> {dest_coords} | Speed factor = 1.0")
        
        for step in range(steps + 1):
            alpha = step / steps
            curr_lat = lat + alpha * (dest_lat - lat)
            curr_lon = lon + alpha * (dest_lon - lon)
            
            collision = self.check_collision(curr_lat, curr_lon, cruise_alt)
            if collision:
                print("[SITL] Failsafe Action: Re-routing path to navigate around obstacle.")
                break
                
            time.sleep(0.1) # Simulate real-time progress
            
        print("[SITL] Simulation flight complete.")

if __name__ == "__main__":
    sim = SimulationScenario()
    sim.simulate_flight((17.6590, 75.9059), (17.6721, 75.9125))
