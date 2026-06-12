"use client";
import React from 'react';

export default function WeatherCenter() {
  return (
    <div style={{ background: 'rgba(255,255,255,0.02)', padding: '20px', borderRadius: '12px', border: '1px solid rgba(255,255,255,0.08)' }}>
      <h2>Solapur Weather Monitoring Centre</h2>
      <p style={{ color: '#8c96a5' }}>Real-time meteorological conditions logged by hub and drone sensors.</p>
      
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '20px', marginTop: '20px' }}>
        <div style={{ padding: '15px', background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '8px' }}>
          <h4>PRECIPITATION</h4>
          <div style={{ fontSize: '24px', fontWeight: 'bold', margin: '10px 0' }}>14%</div>
          <span style={{ color: '#00ff66', fontSize: '12px' }}>● Safe for flight</span>
        </div>
        <div style={{ padding: '15px', background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '8px' }}>
          <h4>WIND VELOCITY</h4>
          <div style={{ fontSize: '24px', fontWeight: 'bold', margin: '10px 0' }}>4.2 m/s NW</div>
          <span style={{ color: '#00ff66', fontSize: '12px' }}>● Below threshold limit</span>
        </div>
        <div style={{ padding: '15px', background: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.05)', borderRadius: '8px' }}>
          <h4>VISIBILITY</h4>
          <div style={{ fontSize: '24px', fontWeight: 'bold', margin: '10px 0' }}>9.5 km</div>
          <span style={{ color: '#00ff66', fontSize: '12px' }}>● Clear Line-of-Sight</span>
        </div>
      </div>
    </div>
  );
}
