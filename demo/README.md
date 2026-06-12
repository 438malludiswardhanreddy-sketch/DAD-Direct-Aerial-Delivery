# DAD System Demonstration Guide
This guide provides the step-by-step instructions to run the Software-in-the-Loop (SITL) simulation, start the FastAPI telemetry service, connect Ground Control, and monitor the live drone state on the dashboard.

---

## 1. System Components
The Direct Aerial Delivery (DAD) software stack comprises three primary modules:
1.  **PX4 Autopilot SITL**: The flight control firmware running inside a Gazebo physics simulator.
2.  **MAVLink Bridge**: The python broker (`autonomous/px4_mavlink_bridge.py`) that handles waypoint uploads and telemetry polling.
3.  **FastAPI Backend**: The server (`backend/main.py`) which ingests telemetry logs and exposes WebSocket channels.
4.  **Leaflet Dashboard**: The front-end control interface that renders the real-time position overlay and flight telemetry.

---

## 2. Bootstrapping the Environment

### Step 2.1: Start the FastAPI Server
From the root of the repository, install Python dependencies and run the server using Uvicorn:
```bash
pip install -r requirements.txt
python -m uvicorn backend.main:app --reload --host 127.0.0.1 --port 8000
```
Verify the server is running by visiting the API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Step 2.2: Launch the PX4 SITL & Gazebo Simulator
Set up your local PX4 development environment (see the [PX4 Autopilot guide](https://docs.px4.io/main/en/simulation/gazebo.html)) and launch the hexacopter Gazebo target:
```bash
cd /path/to/PX4-Autopilot
DONT_RUN=1 make px4_sitl_default gazebo-classic_typhoon_h480
```
This boots the simulated typhoon hexacopter at the default home coordinates.

### Step 2.3: Start QGroundControl (GCS)
*   Open the QGroundControl application on your desktop.
*   QGroundControl automatically connects to the PX4 SITL instance over port `14550`.
*   Ensure that the virtual flight map centers on the launch coordinates.

---

## 3. Running the Telemetry Pipeline

### Step 3.1: Connect the MAVLink Bridge
Run the python companion bridge script to link the simulated flight controller with the backend services:
```bash
python autonomous/px4_mavlink_bridge.py
```
This script establishes MAVLink connections over port `14540` and begins translating state outputs to the backend server.

### Step 3.2: Launch the Telemetry Ingestion Daemon
In a separate terminal, launch the telemetry listener daemon to broadcast status frames to the WebSocket channel:
```bash
python backend/telemetry/px4_listener.py
```
Once active, the dashboard will render live coordinate movements, velocity spikes, and battery decay logs.
