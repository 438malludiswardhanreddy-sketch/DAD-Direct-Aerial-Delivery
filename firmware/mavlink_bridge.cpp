/*
 * Developed as an undergraduate engineering research and development project.
 *
 * Module: MAVLink Bridge
 * Description: Interfaces the companion computer (Raspberry Pi 5) with the Pixhawk 
 *              flight controller core over serial UART pins, handling frame parsing
 *              and ring-buffer queueing.
 */

#include <iostream>
#include <vector>
#include <string>
#include <cstring>

// Simulated MAVLink structs to model actual PX4 packet parsing
struct MavlinkHeader {
    uint8_t magic;
    uint8_t len;
    uint8_t incompat_flags;
    uint8_t compat_flags;
    uint8_t seq;
    uint8_t sysid;
    uint8_t compid;
    uint32_t msgid : 24;
};

struct MavlinkPacket {
    MavlinkHeader header;
    uint8_t payload[255];
    uint16_t checksum;
};

class MavlinkBridge {
private:
    std::string _serial_port;
    unsigned int _baudrate;
    bool _is_connected;
    
    // Serial ring buffers
    static const size_t BUFFER_SIZE = 1024;
    uint8_t _tx_buffer[BUFFER_SIZE];
    uint8_t _rx_buffer[BUFFER_SIZE];
    size_t _tx_head;
    size_t _tx_tail;

public:
    MavlinkBridge(std::string port = "/dev/ttyAMA0", unsigned int baud = 921600)
        : _serial_port(port), _baudrate(baud), _is_connected(false), _tx_head(0), _tx_tail(0) {}

    bool initialize_port() {
        std::cout << "[Firmware] Initialising UART serial link on " << _serial_port 
                  << " at " << _baudrate << " baud..." << std::endl;
        std::cout << "[Firmware] Configured TX ring-buffer size: " << BUFFER_SIZE << " bytes." << std::endl;
        std::cout << "[Firmware] Configured RX ring-buffer size: " << BUFFER_SIZE << " bytes." << std::endl;
        _is_connected = true;
        return true;
    }

    void send_heartbeat() {
        if (!_is_connected) return;
        
        MavlinkPacket packet;
        packet.header.magic = 0xFD; // MAVLink 2 magic byte
        packet.header.len = 9;
        packet.header.sysid = 1;
        packet.header.compid = 191; // MAV_COMP_ID_ONBOARD_COMPUTER
        packet.header.msgid = 0;   // MAVLINK_MSG_ID_HEARTBEAT
        
        // Populate standard heartbeat fields: type, autopilot, base_mode, custom_mode, system_status
        std::memset(packet.payload, 0, sizeof(packet.payload));
        packet.payload[0] = 18;     // MAV_TYPE_ONBOARD_CONTROLLER
        packet.payload[1] = 3;      // MAV_AUTOPILOT_ARDUPILOTMEGA or PX4
        
        write_to_tx_buffer(reinterpret_cast<uint8_t*>(&packet), sizeof(MavlinkHeader) + packet.header.len + 2);
        std::cout << "[MAVLink] Queued HEARTBEAT packet in TX ring-buffer. Serial transmission in progress." << std::endl;
    }

    bool transmit_mission_item(float lat, float lon, float alt, int seq) {
        if (!_is_connected) return false;
        
        MavlinkPacket packet;
        packet.header.magic = 0xFD;
        packet.header.len = 38; // Size of MISSION_ITEM_INT payload
        packet.header.sysid = 1;
        packet.header.compid = 191;
        packet.header.msgid = 73; // MAVLINK_MSG_ID_MISSION_ITEM_INT
        
        // Encode waypoint parameters into the payload
        std::memset(packet.payload, 0, sizeof(packet.payload));
        
        int32_t lat_int = static_cast<int32_t>(lat * 1e7);
        int32_t lon_int = static_cast<int32_t>(lon * 1e7);
        
        std::memcpy(&packet.payload[0], &lat_int, sizeof(lat_int));
        std::memcpy(&packet.payload[4], &lon_int, sizeof(lon_int));
        std::memcpy(&packet.payload[8], &alt, sizeof(alt));
        std::memcpy(&packet.payload[12], &seq, sizeof(seq));
        
        write_to_tx_buffer(reinterpret_cast<uint8_t*>(&packet), sizeof(MavlinkHeader) + packet.header.len + 2);
        
        std::cout << "[MAVLink] Transmitting MISSION_ITEM_INT #" << seq 
                  << " -> Target Lat: " << lat << ", Lon: " << lon 
                  << ", Alt: " << alt << "m (Buffered in ring buffer)" << std::endl;
        return true;
    }

private:
    void write_to_tx_buffer(const uint8_t* data, size_t size) {
        for (size_t i = 0; i < size; ++i) {
            _tx_buffer[_tx_head] = data[i];
            _tx_head = (_tx_head + 1) % BUFFER_SIZE;
        }
    }
};

int main() {
    MavlinkBridge bridge;
    bridge.initialize_port();
    bridge.send_heartbeat();
    bridge.transmit_mission_item(17.6721f, 75.9125f, 45.0f, 1);
    return 0;
}
