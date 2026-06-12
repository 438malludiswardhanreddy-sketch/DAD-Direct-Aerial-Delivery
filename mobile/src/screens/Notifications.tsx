import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function NotificationsScreen() {
  const notifications = [
    { id: 1, title: "Order Booked", body: "Drone has been scheduled for your package." },
    { id: 2, title: "Takeoff confirmed", body: "Hexacopter has launched from Station A." },
    { id: 3, title: "Landed & Delivered", body: "Package dropped safely at your coordinates." }
  ];

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Notifications</Text>
      {notifications.map((n) => (
        <View key={n.id} style={styles.card}>
          <Text style={styles.cardTitle}>{n.title}</Text>
          <Text style={styles.cardBody}>{n.body}</Text>
        </View>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: '#121318', borderRadius: 10 },
  title: { color: '#fff', fontSize: 18, fontWeight: 'bold', marginBottom: 15 },
  card: { padding: 12, borderBottomWidth: 1, borderBottomColor: '#2e323e' },
  cardTitle: { color: '#00e5ff', fontWeight: 'bold', marginBottom: 5 },
  cardBody: { color: '#ccc' }
});
