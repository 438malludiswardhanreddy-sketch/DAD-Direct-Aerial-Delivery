/*
 * Developed as an undergraduate engineering research and development project.
 *
 * Module: Emergency Land Core
 * Description: Low-level control overrides to select emergency landing platforms.
 */

#include <iostream>
#include <vector>
#include <cmath>

struct Position {
    double latitude;
    double longitude;
};

class EmergencyLandingFailsafe {
private:
    std::vector<Position> _platforms;

public:
    EmergencyLandingFailsafe() {
        // Solapur regional hubs
        _platforms.push_back({17.6590, 75.9059});
        _platforms.push_back({17.6721, 75.9125});
    }

    Position get_closest_platform(double current_lat, double current_lon) {
        Position closest = _platforms[0];
        double min_dist = 999999.0;
        
        for (const auto& p : _platforms) {
            double d_lat = p.latitude - current_lat;
            double d_lon = p.longitude - current_lon;
            double dist = std::sqrt(d_lat * d_lat + d_lon * d_lon);
            if (dist < min_dist) {
                min_dist = dist;
                closest = p;
            }
        }
        return closest;
    }
};

int main() {
    EmergencyLandingFailsafe elf;
    Position current = {17.6601, 75.9082};
    Position target = elf.get_closest_platform(current.latitude, current.longitude);
    std::cout << "[Firmware] Emergency Target Platform Locked: " 
              << target.latitude << ", " << target.longitude << std::endl;
    return 0;
}
