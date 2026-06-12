import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function OrderCreationScreen({ onOrderConfirm }: { onOrderConfirm: (lat: string, lon: string) => void }) {
  const [lat, setLat] = useState('17.6721');
  const [lon, setLon] = useState('75.9125');
  const [type, setType] = useState('Medical');

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Book Aerial Delivery</Text>
      <TextInput style={styles.input} placeholder="Payload Type" placeholderTextColor="#888" value={type} onChangeText={setType} />
      <TextInput style={styles.input} placeholder="Destination Latitude" placeholderTextColor="#888" value={lat} onChangeText={setLat} />
      <TextInput style={styles.input} placeholder="Destination Longitude" placeholderTextColor="#888" value={lon} onChangeText={setLon} />
      <TouchableOpacity style={styles.button} onPress={() => onOrderConfirm(lat, lon)}>
        <Text style={styles.buttonText}>Confirm Booking</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 20, backgroundColor: '#121318', borderRadius: 10 },
  title: { color: '#fff', fontSize: 18, fontWeight: 'bold', marginBottom: 15 },
  input: { backgroundColor: '#1c1e24', color: '#fff', padding: 12, borderRadius: 6, marginBottom: 15, borderWidth: 1, borderColor: '#2e323e' },
  button: { backgroundColor: '#00e5ff', padding: 15, borderRadius: 6, alignItems: 'center' },
  buttonText: { color: '#000', fontWeight: 'bold' }
});
