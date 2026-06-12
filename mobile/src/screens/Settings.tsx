import React, { useState } from 'react';
import { View, Text, Switch, StyleSheet } from 'react-native';

export default function SettingsScreen() {
  const [notificationsEnabled, setNotificationsEnabled] = useState(true);
  const [secureMode, setSecureMode] = useState(true);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Application Settings</Text>
      
      <View style={styles.row}>
        <Text style={styles.label}>Push Notifications</Text>
        <Switch value={notificationsEnabled} onValueChange={setNotificationsEnabled} trackColor={{ true: '#00e5ff' }} />
      </View>

      <View style={styles.row}>
        <Text style={styles.label}>Secure Telemetry (Signing)</Text>
        <Switch value={secureMode} onValueChange={setSecureMode} trackColor={{ true: '#00e5ff' }} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: '#121318', borderRadius: 10 },
  title: { color: '#fff', fontSize: 18, fontWeight: 'bold', marginBottom: 20 },
  row: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', paddingVertical: 15, borderBottomWidth: 1, borderBottomColor: '#2e323e' },
  label: { color: '#ccc', fontSize: 15 }
});
