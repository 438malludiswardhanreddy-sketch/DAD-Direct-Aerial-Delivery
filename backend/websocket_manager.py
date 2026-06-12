"""
Developed as an undergraduate engineering research and development project.

Module: WebSocket Connection Manager
Description: Controls active WebSocket client streams broadcasting fleet updates.
"""

class TelemetryWebSocketManager:
    def __init__(self):
        self.connections = []

    def register_client(self, websocket_client):
        self.connections.append(websocket_client)
        print("[WS Manager] Registered new Leaflet Dashboard client.")

    def unregister_client(self, websocket_client):
        if websocket_client in self.connections:
            self.connections.remove(websocket_client)
            print("[WS Manager] Client disconnected.")

    def broadcast(self, message: dict):
        # In a real environment, this sends async calls
        active_count = len(self.connections)
        if active_count > 0:
            print(f"[WS Manager] Broadcasting packet to {active_count} active listeners.")
        return active_count
