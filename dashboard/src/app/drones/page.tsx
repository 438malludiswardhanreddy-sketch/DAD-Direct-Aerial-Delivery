"use client";
import React from 'react';

export default function DronesPage() {
  const analytics = [
    { id: "drone_01", temperature: "32°C", chargeCycles: 142, health: "98%", remainingLife: "2.4 years" },
    { id: "drone_02", temperature: "38°C", chargeCycles: 210, health: "91%", remainingLife: "1.8 years" }
  ];

  return (
    <div style={{ background: 'rgba(255,255,255,0.02)', padding: '20px', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
      <h2>Battery Analytics & Drone Details</h2>
      <table style={{ width: '100%', borderCollapse: 'collapse', marginTop: '20px' }}>
        <thead>
          <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.08)', textAlign: 'left' }}>
            <th style={{ padding: '12px' }}>Drone ID</th>
            <th style={{ padding: '12px' }}>Temperature</th>
            <th style={{ padding: '12px' }}>Charge Cycles</th>
            <th style={{ padding: '12px' }}>State of Health</th>
            <th style={{ padding: '12px' }}>Estimated Lifespan</th>
          </tr>
        </thead>
        <tbody>
          {analytics.map((d) => (
            <tr key={d.id} style={{ borderBottom: '1px solid rgba(255,255,255,0.04)' }}>
              <td style={{ padding: '12px' }}>{d.id.toUpperCase()}</td>
              <td style={{ padding: '12px' }}>{d.temperature}</td>
              <td style={{ padding: '12px' }}>{d.chargeCycles}</td>
              <td style={{ padding: '12px', color: '#00ff66' }}>{d.health}</td>
              <td style={{ padding: '12px' }}>{d.remainingLife}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
