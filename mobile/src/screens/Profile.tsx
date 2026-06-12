import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function ProfileScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Customer Profile</Text>
      <View style={styles.infoRow}>
        <Text style={styles.label}>Name</Text>
        <Text style={styles.value}>Engineering Student</Text>
      </View>
      <View style={styles.infoRow}>
        <Text style={styles.label}>Institution</Text>
        <Text style={styles.value}>Solapur University</Text>
      </View>
      <View style={styles.infoRow}>
        <Text style={styles.label}>UIN Registered</Text>
        <Text style={styles.value}>UIN-UAV-SMALL-9921</Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: '#121318', borderRadius: 10 },
  title: { color: '#fff', fontSize: 18, fontWeight: 'bold', marginBottom: 20 },
  infoRow: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 12, borderBottomWidth: 1, borderBottomColor: '#2e323e' },
  label: { color: '#888' },
  value: { color: '#fff', fontWeight: '600' }
});
