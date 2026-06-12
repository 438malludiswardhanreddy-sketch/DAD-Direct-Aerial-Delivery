"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Drones Router
Description: Handles fleet status, live list, drone registration, and JWT authorization.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database.db_session import get_db
from ..database.models import DroneModel
from ...security.auth import AuthHandler

router = APIRouter(prefix="/api/v1/drone", tags=["Drones"])
auth_handler = AuthHandler()

class DroneRegisterSchema(BaseModel):
    id: str
    model_name: str
    battery_percentage: float

class DroneAuthSchema(BaseModel):
    id: str
    auth_key: str

@router.get("/status")
def get_fleet_status(db: Session = Depends(get_db)):
    """
    Returns the status and battery details of all active drones.
    """
    drones = db.query(DroneModel).all()
    return {
        d.id: {
            "model": d.model_name,
            "battery": d.battery_percentage,
            "status": d.status
        } for d in drones
    }

@router.get("/fleet/live")
def get_live_fleet(db: Session = Depends(get_db)):
    """
    Returns the coordinates and details of active drones.
    """
    active_drones = db.query(DroneModel).filter(DroneModel.status == "Active").all()
    return [
        {
            "drone_id": d.id,
            "battery": d.battery_percentage,
            "status": d.status
        } for d in active_drones
    ]

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register_drone(drone: DroneRegisterSchema, db: Session = Depends(get_db)):
    """
    Registers a new drone model in the local database.
    """
    existing_drone = db.query(DroneModel).filter(DroneModel.id == drone.id).first()
    if existing_drone:
        raise HTTPException(status_code=400, detail="Drone with this ID already registered")
        
    new_drone = DroneModel(
        id=drone.id,
        model_name=drone.model_name,
        status="Active",
        battery_percentage=drone.battery_percentage
    )
    db.add(new_drone)
    db.commit()
    return {"status": "success", "message": f"Drone {drone.id} registered."}

@router.post("/auth")
def auth_drone(auth_data: DroneAuthSchema, db: Session = Depends(get_db)):
    """
    Authenticates a registered drone, returning a JWT token for telemetry signing.
    """
    drone = db.query(DroneModel).filter(DroneModel.id == auth_data.id).first()
    if not drone:
        raise HTTPException(status_code=404, detail="Drone not registered")
        
    # Check credentials (mock check for demo)
    if auth_data.auth_key != "solapur-dad-secret-key-2026":
        raise HTTPException(status_code=401, detail="Invalid credential key")
        
    token = auth_handler.generate_token(drone.id, role="operator")
    return {"token": token, "token_type": "bearer"}
