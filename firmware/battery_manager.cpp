/*
 * Developed as an undergraduate engineering research and development project.
 *
 * Module: Battery Manager
 * Description: Monitors cell voltages and calculates remain limits before failsafes.
 */

#include <iostream>
#include <algorithm>

class BatteryManager {
private:
    float _capacity_mah;
    int _cell_count;
    float _failsafe_threshold_pct;
    float _current_pct;

public:
    BatteryManager(float cap = 16000.0f, int cells = 6, float limit = 20.0f)
        : _capacity_mah(cap), _cell_count(cells), _failsafe_threshold_pct(limit), _current_pct(100.0f) {}

    void process_voltage_telemetry(float total_voltage) {
        float cell_volts = total_voltage / _cell_count;
        
        // Voltage mapping equation
        if (cell_volts >= 4.2f) {
            _current_pct = 100.0f;
        } else if (cell_volts <= 3.5f) {
            _current_pct = 0.0f;
        } else {
            _current_pct = (cell_volts - 3.5f) / (4.2f - 3.5f) * 100.0f;
        }
        _current_pct = std::clamp(_current_pct, 0.0f, 100.0f);
    }

    bool is_failsafe_needed() const {
        return _current_pct <= _failsafe_threshold_pct;
    }

    float get_capacity_pct() const {
        return _current_pct;
    }
};

int main() {
    BatteryManager bm;
    bm.process_voltage_telemetry(21.6f); // 3.6V per cell (approx 14%)
    std::cout << "[Firmware] Current capacity: " << bm.get_capacity_pct() << "%" << std::endl;
    if (bm.is_failsafe_needed()) {
        std::cout << "[Firmware] Low Battery Failsafe Active! Sending RTL command." << std::endl;
    }
    return 0;
}
