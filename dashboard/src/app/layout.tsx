import React from 'react';

export const metadata = {
  title: 'DAD - Direct Aerial Delivery Control Centre',
  description: 'Solapur University Final Year Project',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body style={{ backgroundColor: '#050608', color: '#f0f2f5', fontFamily: 'sans-serif', margin: 0 }}>
        <header style={{ padding: '20px', borderBottom: '1px solid rgba(255,255,255,0.08)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h1 style={{ margin: 0, fontSize: '20px', letterSpacing: '1px', color: '#00e5ff' }}>DAD CONTROL CENTRE</h1>
          <nav style={{ display: 'flex', gap: '20px' }}>
            <a href="/" style={{ color: '#ccc', textDecoration: 'none' }}>Overview</a>
            <a href="/drones" style={{ color: '#ccc', textDecoration: 'none' }}>Drones</a>
            <a href="/mission" style={{ color: '#ccc', textDecoration: 'none' }}>Mission Planner</a>
            <a href="/weather" style={{ color: '#ccc', textDecoration: 'none' }}>Weather Centre</a>
            <a href="/alerts" style={{ color: '#ccc', textDecoration: 'none' }}>Alert Centre</a>
          </nav>
        </header>
        <main style={{ padding: '20px' }}>{children}</main>
      </body>
    </html>
  );
}
