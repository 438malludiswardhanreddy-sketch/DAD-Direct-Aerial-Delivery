#include "../firmware/BatteryManager/BatteryManager.hpp"
#include <iostream>
#include <cassert>

void test_battery_normal_discharge() {
    // 16000mAh battery, 6S cell count, 20% emergency threshold
    BatteryManager bm(16000.0f, 6, 20.0f);
    
    // Telemetry update: 25.2V (4.2V per cell), 10 Amps load, 30 deg C
    bm.updateTelemetry(25.2f, 10.0f, 30.0f);
    
    assert(bm.getRemainingPercentage() == 100.0f);
    assert(!bm.isEmergencyThresholdReached());
    
    // Telemetry update: 21.0V (3.5V per cell)
    bm.updateTelemetry(21.0f, 15.0f, 32.0f);
    
    float expected_pct = (3.5f - 3.3f) / (4.2f - 3.3f) * 100.0f; // ~22.2%
    assert(std::abs(bm.getRemainingPercentage() - expected_pct) < 1.0f);
    assert(!bm.isEmergencyThresholdReached());
    
    // Telemetry update: 20.0V (3.33V per cell) -> below 20% threshold
    bm.updateTelemetry(20.0f, 12.0f, 35.0f);
    assert(bm.isEmergencyThresholdReached());
    
    std::cout << "[TEST] test_battery_normal_discharge passed!" << std::endl;
}

int main() {
    test_battery_normal_discharge();
    std::cout << "[TEST] All firmware unit tests completed successfully." << std::endl;
    return 0;
}
