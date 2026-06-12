"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: FastAPI Application Entrypoint
Description: Orchestrates modular routers and sets up sqlite connections on boot.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database.db_session import init_db
from .routes import orders, mission, drones
from .telemetry import telemetry_stream

app = FastAPI(
    title="DAD Drone Telemetry & Dispatch API",
    description="Undergraduate design project: Telemetry gateway and fleet coordinator",
    version="2.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(orders.router)
app.include_router(mission.router)
app.include_router(drones.router)
app.include_router(telemetry_stream.router)
app.include_router(telemetry_stream.ws_router)

@app.on_event("startup")
def startup_event():
    print("[SYSTEM] Initialising local SQLite database tables...")
    init_db()
    print("[SYSTEM] DAD API server online.")

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
