"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Mission Router
Description: Coordinates waypoint route construction, mission cancelation, 
             and status updates in the SQLite database.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..database.db_session import get_db
from ..database.models import MissionModel, DroneModel

router = APIRouter(prefix="/api/v1/mission", tags=["Missions"])

class MissionPlanSchema(BaseModel):
    drone_id: str
    target_lat: float
    target_lon: float
    altitude_agl: float

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_mission_plan(plan: MissionPlanSchema, db: Session = Depends(get_db)):
    """
    Creates and records a flight mission in the local database.
    """
    drone = db.query(DroneModel).filter(DroneModel.id == plan.drone_id).first()
    if not drone:
        raise HTTPException(status_code=404, detail="Drone registration record not found")
        
    import random
    mission_id = f"msn_{random.randint(1000, 9999)}"
    
    new_mission = MissionModel(
        id=mission_id,
        drone_id=plan.drone_id,
        start_lat=17.6590,
        start_lon=75.9059,
        dest_lat=plan.target_lat,
        dest_lon=plan.target_lon,
        status="Pending"
    )
    
    db.add(new_mission)
    db.commit()
    
    return {
        "mission_id": mission_id,
        "status": "Scheduled",
        "waypoints": [
            {"seq": 0, "command": "TAKEOFF", "lat": 17.6590, "lon": 75.9059, "alt": plan.altitude_agl},
            {"seq": 1, "command": "WAYPOINT", "lat": plan.target_lat, "lon": plan.target_lon, "alt": plan.altitude_agl},
            {"seq": 2, "command": "LAND", "lat": plan.target_lat, "lon": plan.target_lon, "alt": 0.0}
        ]
    }

@router.post("/cancel/{mission_id}")
def cancel_mission(mission_id: str, db: Session = Depends(get_db)):
    """
    Updates the mission status in the database to Aborted.
    """
    mission = db.query(MissionModel).filter(MissionModel.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
        
    mission.status = "Aborted"
    db.commit()
    return {"status": "success", "message": f"Mission {mission_id} cancelled."}

@router.get("/status/{mission_id}")
def get_mission_status(mission_id: str, db: Session = Depends(get_db)):
    """
    Returns the current tracking status of the mission.
    """
    mission = db.query(MissionModel).filter(MissionModel.id == mission_id).first()
    if not mission:
        raise HTTPException(status_code=404, detail="Mission not found")
        
    return {
        "mission_id": mission.id,
        "drone_id": mission.drone_id,
        "destination": {"lat": mission.dest_lat, "lon": mission.dest_lon},
        "status": mission.status
    }
