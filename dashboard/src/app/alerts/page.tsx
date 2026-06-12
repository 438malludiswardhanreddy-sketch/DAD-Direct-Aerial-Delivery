"use client";
import React from 'react';

export default function AlertCenter() {
  const alerts = [
    { id: 1, time: "01:04:12 UTC", type: "CRITICAL", msg: "Drone-01 rain sensor limit exceeded. RTL triggered." },
    { id: 2, time: "00:42:09 UTC", type: "WARNING", msg: "Drone-02 battery charge level critically low (12%)." },
    { id: 3, time: "23:15:00 UTC", type: "INFO", msg: "Ground Launch Station A GPS RTK receiver re-calibrated." }
  ];

  return (
    <div style={{ background: 'rgba(255,255,255,0.02)', padding: '20px', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
      <h2>Alert Centre Log</h2>
      <div style={{ marginTop: '20px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
        {alerts.map((a) => (
          <div key={a.id} style={{ display: 'flex', gap: '15px', padding: '12px', borderRadius: '8px', background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.04)' }}>
            <span style={{ color: '#8c96a5', fontFamily: 'monospace' }}>[{a.time}]</span>
            <strong style={{ color: a.type === 'CRITICAL' ? '#ff3d00' : a.type === 'WARNING' ? '#ffc107' : '#00e5ff' }}>[{a.type}]</strong>
            <span>{a.msg}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
