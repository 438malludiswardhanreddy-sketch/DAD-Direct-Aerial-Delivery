"""
Developed as an undergraduate engineering research and development project.

Module: Drone Registry
Description: Manages active UAV identities and battery statuses in the fleet.
"""

class DroneRegistry:
    def __init__(self):
        self.drones = {
            "drone_01": {"model": "Tarot 680Pro Hexacopter", "status": "Active", "battery": 100.0},
            "drone_02": {"model": "Tarot 680Pro Hexacopter", "status": "Charging", "battery": 12.0},
            "drone_03": {"model": "Tarot 680Pro Hexacopter", "status": "Maintenance", "battery": 95.0}
        }

    def register(self, drone_id: str, model: str, battery: float):
        if drone_id in self.drones:
            return False
        self.drones[drone_id] = {"model": model, "status": "Active", "battery": battery}
        return True

    def get_drone(self, drone_id: str):
        return self.drones.get(drone_id, None)

    def update_battery(self, drone_id: str, battery: float):
        if drone_id in self.drones:
            self.drones[drone_id]["battery"] = battery
            return True
        return False
