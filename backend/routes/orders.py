"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Orders Router
Description: Handles order dispatching and parcel delivery parameters.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database.db_session import get_db
from ..database.models import MissionModel
import random

router = APIRouter(prefix="/api/v1/orders", tags=["Orders"])

class OrderCreateSchema(BaseModel):
    customer_id: str
    destination_lat: float
    destination_lon: float
    weight_kg: float
    payload_type: str

@router.post("")
def create_order(order: OrderCreateSchema, db: Session = Depends(get_db)):
    """
    Submits a new order, creating a corresponding flight mission reference.
    """
    # Pick first active drone
    from ..database.models import DroneModel
    active_drone = db.query(DroneModel).filter(DroneModel.status == "Active").first()
    if not active_drone:
        raise HTTPException(status_code=503, detail="No active drones available in fleet")
        
    mission_id = f"msn_{random.randint(1000, 9999)}"
    new_mission = MissionModel(
        id=mission_id,
        drone_id=active_drone.id,
        start_lat=17.6590,  # Launch Station A
        start_lon=75.9059,
        dest_lat=order.destination_lat,
        dest_lon=order.destination_lon,
        status="Pending"
    )
    
    db.add(new_mission)
    db.commit()
    
    return {
        "order_id": f"ord_{random.randint(10000, 99999)}",
        "mission_id": mission_id,
        "drone_assigned": active_drone.id,
        "status": "Scheduled",
        "eta_minutes": round(random.uniform(8.0, 18.0), 1)
    }
