import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import random
import time

app = FastAPI(
    title="DAD Drone Telemetry & Dispatch API",
    description="Backend microservice for Direct Aerial Delivery fleet operations",
    version="1.0.0"
)

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class OrderCreate(BaseModel):
    customer_id: str
    destination_lat: float
    destination_lon: float
    weight_kg: float
    payload_type: str

class TelemetryReport(BaseModel):
    drone_id: str
    latitude: float
    longitude: float
    altitude: float
    speed: float
    battery: float

# In-memory storage for active tracking and fleet states
active_orders = {}
fleet_status = {
    "drone_01": {"latitude": 17.6590, "longitude": 75.9059, "altitude": 0.0, "speed": 0.0, "battery": 100.0, "status": "Active"},
    "drone_02": {"latitude": 17.6721, "longitude": 75.9125, "altitude": 0.0, "speed": 0.0, "battery": 12.0, "status": "Charging"},
    "drone_03": {"latitude": 17.6410, "longitude": 75.8950, "altitude": 0.0, "speed": 0.0, "battery": 95.0, "status": "Maintenance"}
}

@app.post("/api/v1/orders")
async def create_order(order: OrderCreate):
    order_id = f"ord_{random.randint(10000, 99999)}"
    active_orders[order_id] = {
        "customer_id": order.customer_id,
        "destination_lat": order.destination_lat,
        "destination_lon": order.destination_lon,
        "weight_kg": order.weight_kg,
        "payload_type": order.payload_type,
        "status": "Pending",
        "timestamp": time.time()
    }
    return {
        "order_id": order_id,
        "status": "Pending",
        "estimated_flight_time_mins": round(random.uniform(5.0, 15.0), 1)
    }

@app.get("/api/v1/tracking/{order_id}")
async def get_tracking(order_id: str):
    if order_id not in active_orders:
        raise HTTPException(status_code=404, detail="Order not found")
    
    # Associate order with drone_01 for telemetry demonstration
    drone_telemetry = fleet_status["drone_01"]
    return {
        "order_id": order_id,
        "drone_id": "drone_01",
        "latitude": drone_telemetry["latitude"],
        "longitude": drone_telemetry["longitude"],
        "altitude_m": drone_telemetry["altitude"],
        "velocity_mps": drone_telemetry["speed"],
        "battery_percentage": drone_telemetry["battery"],
        "status": active_orders[order_id]["status"]
    }

@app.post("/api/v1/telemetry/report")
async def report_telemetry(telemetry: TelemetryReport):
    if telemetry.drone_id not in fleet_status:
        fleet_status[telemetry.drone_id] = {}
    
    fleet_status[telemetry.drone_id].update({
        "latitude": telemetry.latitude,
        "longitude": telemetry.longitude,
        "altitude": telemetry.altitude,
        "speed": telemetry.speed,
        "battery": telemetry.battery,
        "status": "Active"
    })
    return {"status": "success"}

@app.get("/api/v1/fleet/health")
async def get_fleet_health():
    return fleet_status

# WebSocket broadcast manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except Exception:
                pass

manager = ConnectionManager()

@app.websocket("/ws/fleet")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    # Start background telemetry generator loop for dynamic dashboard visualization
    lat_start, lon_start = 17.6590, 75.9059
    lat_dest, lon_dest = 17.6721, 75.9125
    steps = 100
    current_step = 0
    altitude = 0.0
    battery = 100.0

    try:
        while True:
            # Linear interpolation mock flight
            alpha = current_step / steps
            lat = lat_start + alpha * (lat_dest - lat_start)
            lon = lon_start + alpha * (lon_dest - lon_start)
            
            # Alt phase: ascent, cruise, descent
            if current_step < 10:
                altitude += 4.5
            elif current_step > 90:
                altitude = max(0.0, altitude - 4.5)
            else:
                altitude = 45.0 + random.uniform(-1.0, 1.0)
            
            speed = 12.5 if current_step in range(10, 90) else 2.0
            battery = max(0.0, battery - 0.4)
            
            # Update drone_01 database representation
            fleet_status["drone_01"].update({
                "latitude": lat,
                "longitude": lon,
                "altitude": round(altitude, 1),
                "speed": round(speed, 1),
                "battery": round(battery, 1)
            })

            # Broadcast update
            await manager.broadcast({
                "type": "telemetry",
                "timestamp": time.time(),
                "drones": fleet_status
            })

            current_step = (current_step + 1) % steps
            await asyncio.sleep(1.0)

    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
