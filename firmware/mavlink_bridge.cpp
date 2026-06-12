/*
 * Developed as an undergraduate engineering research and development project.
 *
 * Module: MAVLink Bridge
 * Description: Interfaces the companion computer (Raspberry Pi 5) with the Pixhawk 
 *              flight controller core over serial UART pins.
 */

#include <iostream>
#include <vector>
#include <string>

class MavlinkBridge {
private:
    std::string _serial_port;
    unsigned int _baudrate;
    bool _is_connected;

public:
    MavlinkBridge(std::string port = "/dev/ttyAMA0", unsigned int baud = 57600)
        : _serial_port(port), _baudrate(baud), _is_connected(false) {}

    bool initialize_port() {
        std::cout << "[Firmware] Initializing UART serial link on " << _serial_port 
                  << " at " << _baudrate << " baud..." << std::endl;
        _is_connected = true;
        return true;
    }

    void send_heartbeat() {
        if (!_is_connected) return;
        std::cout << "[MAVLink] Broadcasting HEARTBEAT packet (Component ID: Companion)" << std::endl;
    }

    bool transmit_mission_item(float lat, float lon, float alt, int seq) {
        if (!_is_connected) return false;
        std::cout << "[MAVLink] Transmitting MISSION_ITEM #" << seq 
                  << " -> Target Lat: " << lat << ", Lon: " << lon 
                  << ", Alt: " << alt << std::endl;
        return true;
    }
};

int main() {
    MavlinkBridge bridge;
    bridge.initialize_port();
    bridge.send_heartbeat();
    bridge.transmit_mission_item(17.6721f, 75.9125f, 45.0f, 1);
    return 0;
}
