# MAVLink Packet Logs
This directory stores MAVLink transaction logs captured during mission execution.

---

## 1. MAVLink Transaction Sequence
Below is a raw packet dump of the mission upload transaction between the companion computer and the Pixhawk flight controller:

```text
[10:14:02.102] TX: MAVLINK_MSG_ID_MISSION_CLEAR_ALL (ID: 45) -> Target System: 1, Component: 1
[10:14:02.115] RX: MAVLINK_MSG_ID_MISSION_ACK (ID: 47) -> Type: MAV_MISSION_ACCEPTED
[10:14:02.120] TX: MAVLINK_MSG_ID_MISSION_COUNT (ID: 44) -> Count: 3
[10:14:02.132] RX: MAVLINK_MSG_ID_MISSION_REQUEST (ID: 40) -> Sequence: 0
[10:14:02.140] TX: MAVLINK_MSG_ID_MISSION_ITEM_INT (ID: 73) -> Seq: 0, Command: MAV_CMD_NAV_TAKEOFF, Lat: 17.659021, Lon: 75.905912, Alt: 15.0m
[10:14:02.155] RX: MAVLINK_MSG_ID_MISSION_REQUEST (ID: 40) -> Sequence: 1
[10:14:02.162] TX: MAVLINK_MSG_ID_MISSION_ITEM_INT (ID: 73) -> Seq: 1, Command: MAV_CMD_NAV_WAYPOINT, Lat: 17.661021, Lon: 75.907012, Alt: 45.0m
[10:14:02.174] RX: MAVLINK_MSG_ID_MISSION_REQUEST (ID: 40) -> Sequence: 2
[10:14:02.180] TX: MAVLINK_MSG_ID_MISSION_ITEM_INT (ID: 73) -> Seq: 2, Command: MAV_CMD_NAV_LAND, Lat: 17.663521, Lon: 75.909012, Alt: 0.0m
[10:14:02.195] RX: MAVLINK_MSG_ID_MISSION_ACK (ID: 47) -> Type: MAV_MISSION_ACCEPTED (Upload Complete)
```

---

## 2. Heartbeat Monitoring
The companion computer broadcasts a `HEARTBEAT` packet every **1.0 second** (Target Metric). If the flight controller does not receive this packet within 3.0 seconds, it triggers the loss-of-communication failsafe (Failsafe 0).
