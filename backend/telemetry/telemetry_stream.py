"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Telemetry Ingestion Router
Description: Handles HTTP telemetry uploads, WS broadcasts, and live fleet telemetry listings.
"""

from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database.db_session import get_db
from ..database.models import TelemetryLogModel, DroneModel
import time
import asyncio

router = APIRouter(prefix="/api/v1/telemetry", tags=["Telemetry"])

class TelemetryUploadSchema(BaseModel):
    drone_id: str
    latitude: float
    longitude: float
    altitude: float
    speed: float
    battery: float

active_sockets = []

@router.post("/upload")
def upload_telemetry(data: TelemetryUploadSchema, db: Session = Depends(get_db)):
    """
    HTTP endpoint to ingest telemetry values from the companion computer.
    """
    log = TelemetryLogModel(
        drone_id=data.drone_id,
        latitude=data.latitude,
        longitude=data.longitude,
        altitude=data.altitude,
        speed=data.speed,
        battery=data.battery
    )
    
    # Update drone status table
    drone = db.query(DroneModel).filter(DroneModel.id == data.drone_id).first()
    if drone:
        drone.battery_percentage = data.battery
        
    db.add(log)
    db.commit()
    
    # Broadcast to websocket clients asynchronously
    asyncio.run(broadcast_telemetry({
        "drone_id": data.drone_id,
        "latitude": data.latitude,
        "longitude": data.longitude,
        "altitude": data.altitude,
        "speed": data.speed,
        "battery": data.battery
    }))
    
    return {"status": "ACK"}

@router.get("/live")
def get_live_telemetry(db: Session = Depends(get_db)):
    """
    Acquires latest logged telemetry status for all active assets.
    """
    # Simple query to return the latest logs grouped by drone
    # For SQLite, we mock or query all logs and return the latest entry per drone
    drones = db.query(DroneModel).filter(DroneModel.status == "Active").all()
    results = {}
    for d in drones:
        latest_log = db.query(TelemetryLogModel).filter(TelemetryLogModel.drone_id == d.id).order_by(TelemetryLogModel.id.desc()).first()
        if latest_log:
            results[d.id] = {
                "latitude": latest_log.latitude,
                "longitude": latest_log.longitude,
                "altitude": latest_log.altitude,
                "speed": latest_log.speed,
                "battery": latest_log.battery
            }
        else:
            results[d.id] = {
                "latitude": 17.6590,
                "longitude": 75.9059,
                "altitude": 0.0,
                "speed": 0.0,
                "battery": d.battery_percentage
            }
    return results

async def broadcast_telemetry(payload):
    for ws in active_sockets:
        try:
            await ws.send_json({"type": "telemetry", "data": payload})
        except Exception:
            pass

# WebSocket router registration helper
ws_router = APIRouter(tags=["WebSockets"])

@ws_router.websocket("/ws/fleet")
async def fleet_telemetry_socket(websocket: WebSocket):
    """
    WebSocket channel for real-time control room feeds.
    """
    await websocket.accept()
    active_sockets.append(websocket)
    try:
        while True:
            # Keep socket alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        active_sockets.remove(websocket)
