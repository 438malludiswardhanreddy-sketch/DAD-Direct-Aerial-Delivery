"use client";
import React, { useState, useEffect } from 'react';

export default function FleetOverview() {
  const [telemetry, setTelemetry] = useState<any>({
    "drone_01": { latitude: 17.6590, longitude: 75.9059, altitude: 45.0, speed: 12.5, battery: 98.0 },
    "drone_02": { latitude: 17.6721, longitude: 75.9125, altitude: 0.0, speed: 0.0, battery: 12.0 }
  });

  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '20px' }}>
      <div style={{ background: 'rgba(255,255,255,0.02)', padding: '20px', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
        <h2>Active Fleet status</h2>
        {Object.keys(telemetry).map((id) => (
          <div key={id} style={{ padding: '12px', background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.04)', borderRadius: '8px', marginBottom: '10px' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '5px' }}>
              <strong>{id.toUpperCase()}</strong>
              <span style={{ color: '#00ff66' }}>Active</span>
            </div>
            <div>Battery: {telemetry[id].battery}%</div>
            <div>Altitude: {telemetry[id].altitude}m</div>
            <div>Speed: {telemetry[id].speed}m/s</div>
          </div>
        ))}
      </div>

      <div style={{ background: 'rgba(255,255,255,0.02)', padding: '20px', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)', minHeight: '400px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div style={{ textAlign: 'center', color: '#8c96a5' }}>
          <h3>Live Telemetry Map</h3>
          <p>Tracking coordinates: (17.6590, 75.9059) -> (17.6721, 75.9125)</p>
          <div style={{ width: '100%', height: '300px', border: '1px dashed #2e323e', borderRadius: '8px', marginTop: '10px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            [Leaflet Map Stream Initialised]
          </div>
        </div>
      </div>
    </div>
  );
}
