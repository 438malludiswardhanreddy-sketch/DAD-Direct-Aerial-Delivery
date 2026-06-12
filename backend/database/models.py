"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Database Models
Description: Defines SQLAlchemy models representing flight tracking entities.
"""

from sqlalchemy import Column, String, Float, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class DroneModel(Base):
    __tablename__ = "drones"
    
    id = Column(String, primary_key=True, index=True)
    model_name = Column(String, default="Tarot 680Pro Hexacopter")
    status = Column(String, default="Active")  # Active, Charging, Maintenance
    battery_percentage = Column(Float, default=100.0)
    last_update = Column(DateTime, default=datetime.datetime.utcnow)
    
    missions = relationship("MissionModel", back_populates="drone")

class MissionModel(Base):
    __tablename__ = "missions"
    
    id = Column(String, primary_key=True, index=True)
    drone_id = Column(String, ForeignKey("drones.id"))
    start_lat = Column(Float, nullable=False)
    start_lon = Column(Float, nullable=False)
    dest_lat = Column(Float, nullable=False)
    dest_lon = Column(Float, nullable=False)
    status = Column(String, default="Pending") # Pending, InFlight, Completed, Aborted
    
    drone = relationship("DroneModel", back_populates="missions")

class TelemetryLogModel(Base):
    __tablename__ = "telemetry_logs"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    drone_id = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    altitude = Column(Float, nullable=False)
    speed = Column(Float, nullable=False)
    battery = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
