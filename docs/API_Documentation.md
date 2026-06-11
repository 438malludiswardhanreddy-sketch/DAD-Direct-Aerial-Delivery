# DAD Cloud API Reference

This document describes the REST API and WebSocket endpoints provided by the DAD backend server.

---

## 1. REST Endpoints

### 1.1 Create Order
*   **Method**: `POST`
*   **Path**: `/api/v1/orders`
*   **Description**: Dispatch a new parcel delivery order.
*   **Request Body**:
    ```json
    {
      "customer_id": "cust_99812",
      "destination_lat": 17.6599,
      "destination_lon": 75.9064,
      "weight_kg": 1.5,
      "payload_type": "Medical"
    }
    ```
*   **Response**: `201 Created`
    ```json
    {
      "order_id": "ord_66723b",
      "status": "Pending",
      "estimated_flight_time_mins": 12.4
    }
    ```

### 1.2 Get Telemetry Status
*   **Method**: `GET`
*   **Path**: `/api/v1/tracking/{order_id}`
*   **Description**: Get the current tracking information for an active delivery.
*   **Response**: `200 OK`
    ```json
    {
      "order_id": "ord_66723b",
      "drone_id": "drone_01",
      "latitude": 17.6590,
      "longitude": 75.9059,
      "altitude_m": 45.2,
      "velocity_mps": 12.5,
      "battery_percentage": 78.4,
      "status": "InFlight"
    }
    ```

### 1.3 Post Drone Telemetry
*   **Method**: `POST`
*   **Path**: `/api/v1/telemetry/report`
*   **Description**: Ingest real-time status data from the companion computer.
*   **Request Body**:
    ```json
    {
      "drone_id": "drone_01",
      "latitude": 17.6590,
      "longitude": 75.9059,
      "altitude": 45.2,
      "speed": 12.5,
      "battery": 78.4
    }
    ```

---

## 2. WebSockets Endpoints

### 2.1 Live Fleet Stream
*   **Path**: `/ws/fleet`
*   **Description**: Real-time broadcast channel of the coordinates and health statuses of all active drones. Use this endpoint to feed the control room dashboard.
