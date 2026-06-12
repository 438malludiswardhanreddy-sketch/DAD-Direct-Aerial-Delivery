# Telemetry Data Captures
This directory stores telemetry captures representing the data frames received by the web control interface.

---

## 1. Sample Telemetry Packets (JSON)
The following is an excerpt of telemetry packets transmitted via the WebSocket channel during a simulated mission:

```json
[
  {
    "timestamp_ms": 1781228519000,
    "drone_id": "drone_01",
    "state": {
      "latitude": 17.659021,
      "longitude": 75.905912,
      "altitude_m": 15.0,
      "speed_mps": 0.0,
      "battery_pct": 99.8,
      "flight_mode": "TAKEOFF"
    }
  },
  {
    "timestamp_ms": 1781228529000,
    "drone_id": "drone_01",
    "state": {
      "latitude": 17.660021,
      "longitude": 75.906512,
      "altitude_m": 45.0,
      "speed_mps": 12.5,
      "battery_pct": 98.2,
      "flight_mode": "CRUISE"
    }
  },
  {
    "timestamp_ms": 1781228539000,
    "drone_id": "drone_01",
    "state": {
      "latitude": 17.661021,
      "longitude": 75.907012,
      "altitude_m": 45.0,
      "speed_mps": 12.5,
      "battery_pct": 96.5,
      "flight_mode": "CRUISE"
    }
  }
]
```

---

## 2. Ingestion Rate Verification
*   **Target Ingestion Frequency**: 1.0Hz (1 packet per second per drone).
*   **Average Bandwidth consumption**: ~0.3 KB/s per connection.
