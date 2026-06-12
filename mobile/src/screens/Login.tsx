import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function LoginScreen({ onLoginSuccess }: { onLoginSuccess: (phone: string) => void }) {
  const [phone, setPhone] = useState('');

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Secure Sign In</Text>
      <TextInput
        style={styles.input}
        placeholder="Enter Phone Number"
        placeholderTextColor="#888"
        keyboardType="phone-pad"
        value={phone}
        onChangeText={setPhone}
      />
      <TouchableOpacity style={styles.button} onPress={() => onLoginSuccess(phone)}>
        <Text style={styles.buttonText}>Authenticate via OTP</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#121318',
    borderRadius: 10,
  },
  title: {
    color: '#fff',
    fontSize: 18,
    fontWeight: 'bold',
    marginBottom: 15,
  },
  input: {
    backgroundColor: '#1c1e24',
    color: '#fff',
    padding: 12,
    borderRadius: 6,
    marginBottom: 15,
    borderWidth: 1,
    borderColor: '#2e323e',
  },
  button: {
    backgroundColor: '#00e5ff',
    padding: 15,
    borderRadius: 6,
    alignItems: 'center',
  },
  buttonText: {
    color: '#000',
    fontWeight: 'bold',
  }
});
