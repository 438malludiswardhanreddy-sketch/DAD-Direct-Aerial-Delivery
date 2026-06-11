# DAD (Direct Aerial Delivery) Project Roadmap

This document outlines the planned future milestones and technical goals for the DAD platform.

## Phase 1: Foundations & SITL (Completed)
- [x] Initial design and multi-component directory structure.
- [x] Core FastAPI telemetry server and live dashboard interface.
- [x] YOLOv11 obstacle detection model and CNN weather classifier pipeline.
- [x] Simulation environment configuration for urban delivery routes.

## Phase 2: Hardware Integration & Field Tests (Q3 2026)
- [ ] Construct Tarot 680Pro hexacopter prototype with Pixhawk 6C.
- [ ] Integrate Benewake TFmini LiDAR and rain sensor arrays.
- [ ] Conduct short-range (LoS) autonomous flight testing with dummy cargo.
- [ ] Connect onboard companion computer (Raspberry Pi 5) for edge AI execution.

## Phase 3: Advanced BVLOS & Fleet Scale (Q4 2026)
- [ ] Implement secure 5G cellular telemetry channel fallback.
- [ ] Integrate dual RTK-GPS receivers for centimeter-level landing accuracy.
- [ ] Create multi-drone fleet collision avoidance algorithms.
- [ ] Obtain DGCA BVLOS flight clearance certification.

## Phase 4: Production & Smart Hubs (Q1-Q2 2027)
- [ ] Design and prototype automated drone landing and charging hubs.
- [ ] Integrate payment gateway (Stripe/Crypto) and dynamic shipping pricing.
- [ ] Launch pilot commercial delivery service in Solapur smart city.
