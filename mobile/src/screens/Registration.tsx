import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function RegistrationScreen() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Register Account</Text>
      <TextInput style={styles.input} placeholder="Full Name" placeholderTextColor="#888" value={name} onChangeText={setName} />
      <TextInput style={styles.input} placeholder="Email ID" placeholderTextColor="#888" value={email} onChangeText={setEmail} />
      <TouchableOpacity style={styles.button}>
        <Text style={styles.buttonText}>Submit Details</Text>
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
