#include "BatteryManager.hpp"
#include <algorithm>

BatteryManager::BatteryManager(float capacity_mah, int cell_count, float threshold)
    : _nominal_capacity_mah(capacity_mah), _cell_count(cell_count), _emergency_threshold(threshold) {
    _current_status = {0.0f, 0.0f, 100.0f, 25.0f, 100.0f};
}

void BatteryManager::updateTelemetry(float voltage, float current, float temperature) {
    _current_status.voltage = voltage;
    _current_status.current = current;
    _current_status.temperature = temperature;

    // Simplified calculation of remaining capacity based on cell voltage mapping
    float cell_voltage = voltage / _cell_count;
    float percentage = 0.0f;
    if (cell_voltage >= 4.2f) {
        percentage = 100.0f;
    } else if (cell_voltage <= 3.3f) {
        percentage = 0.0f;
    } else {
        percentage = (cell_voltage - 3.3f) / (4.2f - 3.3f) * 100.0f;
    }
    _current_status.capacity_percentage = std::clamp(percentage, 0.0f, 100.0f);
}

float BatteryManager::getRemainingPercentage() const {
    return _current_status.capacity_percentage;
}

bool BatteryManager::isEmergencyThresholdReached() const {
    return _current_status.capacity_percentage <= _emergency_threshold;
}

float BatteryManager::estimateRemainingFlightTime(float speed_mps) const {
    if (_current_status.current <= 0.05f) {
        return 999.0f; // Minimal discharge, drone on standby
    }
    
    // Convert current (Amps) to mAh discharge rate per minute
    // Current (A) * 1000 = mA. mA / 60 = mAh per minute
    float discharge_rate_mah_per_min = (_current_status.current * 1000.0f) / 60.0f;
    float remaining_mah = (_current_status.capacity_percentage / 100.0f) * _nominal_capacity_mah;
    
    float minutes_remaining = remaining_mah / discharge_rate_mah_per_min;
    
    // Wind factor compensation (mocked impact of high speeds)
    if (speed_mps > 15.0f) {
        minutes_remaining *= 0.8f;
    }
    return minutes_remaining;
}
