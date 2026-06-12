import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function TrackingScreen({ lat, lon }: { lat: string, lon: string }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Live Flight Path Tracker</Text>
      <Text style={styles.badge}>STATUS: IN-FLIGHT</Text>
      <Text style={styles.text}>Target Coordinates: ({lat}, {lon})</Text>
      <Text style={styles.text}>Altitude: 45.0m AGL</Text>
      <Text style={styles.text}>Wind Speed: 4.2 m/s NW</Text>
      <View style={styles.mapPlaceholder}>
        <Text style={styles.mapText}>[Map Stream Live View]</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: '#121318', borderRadius: 10 },
  title: { color: '#fff', fontSize: 18, fontWeight: 'bold', marginBottom: 10 },
  badge: { color: '#00ff66', fontWeight: 'bold', marginBottom: 15 },
  text: { color: '#ccc', marginBottom: 8, fontFamily: 'monospace' },
  mapPlaceholder: { height: 180, borderStyle: 'dashed', borderWidth: 1, borderColor: '#2e323e', borderRadius: 8, justifyContent: 'center', alignItems: 'center', marginTop: 15 },
  mapText: { color: '#888' }
});
