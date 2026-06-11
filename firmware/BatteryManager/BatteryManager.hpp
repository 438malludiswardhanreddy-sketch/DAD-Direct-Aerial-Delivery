#ifndef BATTERY_MANAGER_HPP
#define BATTERY_MANAGER_HPP

struct BatteryStatus {
    float voltage;
    float current;
    float capacity_percentage;
    float temperature;
    float health;
};

class BatteryManager {
private:
    float _nominal_capacity_mah;
    float _cell_count;
    float _emergency_threshold;
    BatteryStatus _current_status;

public:
    BatteryManager(float capacity_mah, int cell_count, float threshold);
    void updateTelemetry(float voltage, float current, float temperature);
    float getRemainingPercentage() const;
    bool isEmergencyThresholdReached() const;
    float estimateRemainingFlightTime(float speed_mps) const;
};

#endif // BATTERY_MANAGER_HPP
