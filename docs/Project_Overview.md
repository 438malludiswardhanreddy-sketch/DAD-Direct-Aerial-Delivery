# DAD Project Overview

## 1. Problem Statement
Last-mile delivery is the most expensive and least efficient part of the logistics supply chain, accounting for over 50% of overall delivery costs. In rapidly growing cities, traffic congestion, poor road infrastructure, and high labor costs further degrade delivery speeds and predictability. 

**Direct Aerial Delivery (DAD)** resolves these bottlenecks by establishing an autonomous, zero-emission last-mile aerial delivery system capable of moving payloads directly from sorting hubs to customers or specialized landing zones.

## 2. Platform Architecture
The DAD system operates as a distributed system:
*   **Edge Autopilot (PX4/ArduPilot)**: Handles high-rate stabilization, attitude control, and low-level path tracking.
*   **Onboard Companion Computer (RPi 5/Jetson Orin Nano)**: Processes high-bandwidth sensors (camera and LiDAR) to perform object avoidance and weather categorization.
*   **Cloud API Server (FastAPI)**: Serves as the central mission coordinator, tracking the location, state, and telemetry of the entire fleet.
*   **Control Center Dashboard**: Allows human-in-the-loop oversight to override autonomous paths, monitor weather patterns, and manage battery charging routines.

## 3. Mission Workflow
1.  **Order Placement**: A user orders a package via the Customer App, specifying the target coordinates.
2.  **Mission Generation**: The Backend API calculates the optimal flight path, avoiding no-fly zones and terrain obstacles.
3.  **Pre-Flight Failsafes**: The drone runs onboard self-checks (battery, sensors, GPS signal lock) before takeoff.
4.  **Autonomous Cruise**: The drone flies BVLOS towards the destination, using YOLOv11 and LiDAR to steer around unexpected structures, wires, and birds.
5.  **Safe Payload Delivery**: Using a camera-based precision landing algorithm, the drone descends, releases the payload, and climbs back to cruise altitude.
6.  **Return & Recharge**: The drone returns to the closest automated charging hub to prepare for the next mission.
