#include <iostream>
#include <vector>
#include <cmath>

struct Position {
    double lat;
    double lon;
    float alt;
};

class EmergencyLandingController {
private:
    std::vector<Position> _power_hubs;
    Position _current_pos;
    bool _weather_emergency;
    bool _battery_emergency;

public:
    EmergencyLandingController() : _weather_emergency(false), _battery_emergency(false) {
        // Initialize mock landing hubs in Solapur region
        _power_hubs.push_back({17.6599, 75.9064, 0.0f});
        _power_hubs.push_back({17.6721, 75.9125, 0.0f});
        _power_hubs.push_back({17.6410, 75.8950, 0.0f});
    }

    void setStatus(double lat, double lon, float alt, bool weather_ok, bool battery_ok) {
        _current_pos = {lat, lon, alt};
        _weather_emergency = !weather_ok;
        _battery_emergency = !battery_ok;
    }

    Position calculateNearestSafeHub() {
        double min_distance = 9999999.0;
        Position nearest_hub = _current_pos;

        for (const auto& hub : _power_hubs) {
            double d_lat = hub.lat - _current_pos.lat;
            double d_lon = hub.lon - _current_pos.lon;
            
            // Euclidean distance proxy
            double distance = std::sqrt(d_lat*d_lat + d_lon*d_lon) * 111000.0; // Approximation of meters
            if (distance < min_distance) {
                min_distance = distance;
                nearest_hub = hub;
            }
        }
        return nearest_hub;
    }

    bool shouldTriggerEmergencyLanding() const {
        return _weather_emergency || _battery_emergency;
    }

    void executeLandingOverride() {
        if (!shouldTriggerEmergencyLanding()) return;

        Position target = calculateNearestSafeHub();
        std::cout << "[EMERGENCY FAILSAFE] Route Override: Heading to Hub at (" 
                  << target.lat << ", " << target.lon << ") for immediate descent." << std::endl;
    }
};
