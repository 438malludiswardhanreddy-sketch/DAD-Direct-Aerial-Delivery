"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Database Session Manager
Description: Configures SQLAlchemy engine and sqlite local file session handlers.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

DATABASE_URL = "sqlite:///./dad_logistics.db"

# Create sqlite connection engine (disable multi-thread access checks for dev convenience)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initialises database tables and pre-populates default drones.
    """
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Pre-populate default fleet if empty
    from .models import DroneModel
    if db.query(DroneModel).count() == 0:
        db.add_all([
            DroneModel(id="drone_01", model_name="Tarot 680Pro Hexacopter", status="Active", battery_percentage=100.0),
            DroneModel(id="drone_02", model_name="Tarot 680Pro Hexacopter", status="Charging", battery_percentage=12.0),
            DroneModel(id="drone_03", model_name="Tarot 680Pro Hexacopter", status="Maintenance", battery_percentage=95.0),
        ])
        db.commit()
    db.close()

def get_db():
    """
    Dependency helper to acquire a thread session reference.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
