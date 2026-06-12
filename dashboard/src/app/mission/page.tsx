"use client";
import React, { useState } from 'react';

export default function MissionPlanner() {
  const [targetLat, setTargetLat] = useState("17.6721");
  const [targetLon, setTargetLon] = useState("75.9125");
  const [altitude, setAltitude] = useState("45.0");
  const [result, setResult] = useState<any>(null);

  const handlePlan = () => {
    setResult({
      status: "APPROVED",
      clearance_code: "NPNT-CLR-887123",
      waypoints: [
        { seq: 0, command: "TAKEOFF", lat: 17.6590, lon: 75.9059, alt: parseFloat(altitude) },
        { seq: 1, command: "WAYPOINT", lat: parseFloat(targetLat), lon: parseFloat(targetLon), alt: parseFloat(altitude) },
        { seq: 2, command: "LAND", lat: parseFloat(targetLat), lon: parseFloat(targetLon), alt: 0.0 }
      ]
    });
  };

  return (
    <div style={{ background: 'rgba(255,255,255,0.02)', padding: '20px', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
      <h2>BVLOS Mission Planner & Waypoint Generator</h2>
      
      <div style={{ marginTop: '20px', display: 'flex', flexDirection: 'column', gap: '15px', maxWidth: '400px' }}>
        <div>
          <label style={{ display: 'block', marginBottom: '5px' }}>Latitude</label>
          <input value={targetLat} onChange={(e) => setTargetLat(e.target.value)} style={{ padding: '10px', background: '#1c1e24', border: '1px solid #2e323e', color: '#fff', borderRadius: '6px', width: '100%' }} />
        </div>
        <div>
          <label style={{ display: 'block', marginBottom: '5px' }}>Longitude</label>
          <input value={targetLon} onChange={(e) => setTargetLon(e.target.value)} style={{ padding: '10px', background: '#1c1e24', border: '1px solid #2e323e', color: '#fff', borderRadius: '6px', width: '100%' }} />
        </div>
        <div>
          <label style={{ display: 'block', marginBottom: '5px' }}>Cruise Altitude (m)</label>
          <input value={altitude} onChange={(e) => setAltitude(e.target.value)} style={{ padding: '10px', background: '#1c1e24', border: '1px solid #2e323e', color: '#fff', borderRadius: '6px', width: '100%' }} />
        </div>
        <button onClick={handlePlan} style={{ padding: '12px', background: '#00e5ff', color: '#000', border: 'none', borderRadius: '6px', fontWeight: 'bold', cursor: 'pointer' }}>Generate Flight Route</button>
      </div>

      {result && (
        <div style={{ marginTop: '30px', padding: '15px', background: 'rgba(0, 229, 255, 0.05)', borderRadius: '8px', border: '1px solid #00e5ff' }}>
          <h4>Clearance Code: {result.clearance_code}</h4>
          <h5>Waypoints Output:</h5>
          <pre style={{ color: '#00ff66' }}>{JSON.stringify(result.waypoints, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}
