import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, TextInput, TouchableOpacity, ScrollView, SafeAreaView } from 'react-native';

export default function App() {
  const [phoneNumber, setPhoneNumber] = useState('');
  const [otp, setOtp] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [step, setStep] = useState(1); // 1: Login, 2: Book, 3: Track

  const [destLat, setDestLat] = useState('17.6721');
  const [destLon, setDestLon] = useState('75.9125');
  const [weight, setWeight] = useState('1.5');
  const [payloadType, setPayloadType] = useState('Medical');
  
  const [orderId, setOrderId] = useState('');
  const [droneTelemetry, setDroneTelemetry] = useState({
    lat: 17.6590,
    lon: 75.9059,
    alt: 0.0,
    speed: 0.0,
    battery: 100
  });

  const handleLogin = () => {
    if (phoneNumber.length >= 10) {
      setStep(2);
    }
  };

  const handleBook = () => {
    // Simulated API Call to FastAPI endpoint `/api/v1/orders`
    console.log("Booking delivery payload...");
    setOrderId(`ord_${Math.floor(Math.random() * 90000) + 10000}`);
    setStep(3);
  };

  // Simulate WebSocket or HTTP Polling telemetry tracking
  useEffect(() => {
    if (step === 3) {
      const interval = setInterval(() => {
        setDroneTelemetry(prev => {
          const targetLat = parseFloat(destLat);
          const targetLon = parseFloat(destLon);
          const newLat = prev.lat + (targetLat - prev.lat) * 0.1;
          const newLon = prev.lon + (targetLon - prev.lon) * 0.1;
          const newBattery = Math.max(prev.battery - 1, 40);
          
          return {
            lat: parseFloat(newLat.toFixed(5)),
            lon: parseFloat(newLon.toFixed(5)),
            alt: 45.0,
            speed: 12.5,
            battery: newBattery
          };
        });
      }, 1000);
      return () => clearInterval(interval);
    }
  }, [step]);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>🛸 DAD - Direct Aerial Delivery</Text>
      </View>

      {step === 1 && (
        <View style={styles.card}>
          <Text style={styles.title}>Secure Sign In</Text>
          <Text style={styles.subtitle}>Enter your phone number to receive a one-time passcode.</Text>
          <TextInput
            style={styles.input}
            placeholder="Phone Number"
            placeholderTextColor="#888"
            keyboardType="phone-pad"
            value={phoneNumber}
            onChangeText={setPhoneNumber}
          />
          <TouchableOpacity style={styles.button} onPress={handleLogin}>
            <Text style={styles.buttonText}>Get OTP</Text>
          </TouchableOpacity>
        </View>
      )}

      {step === 2 && (
        <ScrollView style={styles.scroll}>
          <View style={styles.card}>
            <Text style={styles.title}>Book Aerial Delivery</Text>
            <Text style={styles.subtitle}>Fill in payload dimensions and target coordinates.</Text>
            
            <Text style={styles.label}>Payload Type</Text>
            <TextInput
              style={styles.input}
              placeholder="e.g. Medical, Emergency Supplies, Parcel"
              placeholderTextColor="#888"
              value={payloadType}
              onChangeText={setPayloadType}
            />

            <Text style={styles.label}>Weight (kg)</Text>
            <TextInput
              style={styles.input}
              placeholder="Max 5.0 kg"
              placeholderTextColor="#888"
              keyboardType="decimal-pad"
              value={weight}
              onChangeText={setWeight}
            />

            <Text style={styles.label}>Destination Latitude</Text>
            <TextInput
              style={styles.input}
              placeholder="e.g. 17.6721"
              placeholderTextColor="#888"
              keyboardType="decimal-pad"
              value={destLat}
              onChangeText={setDestLat}
            />

            <Text style={styles.label}>Destination Longitude</Text>
            <TextInput
              style={styles.input}
              placeholder="e.g. 75.9125"
              placeholderTextColor="#888"
              keyboardType="decimal-pad"
              value={destLon}
              onChangeText={setDestLon}
            />

            <TouchableOpacity style={styles.button} onPress={handleBook}>
              <Text style={styles.buttonText}>Confirm Delivery Request</Text>
            </TouchableOpacity>
          </View>
        </ScrollView>
      )}

      {step === 3 && (
        <View style={styles.card}>
          <Text style={styles.title}>Drone Dispatch Tracking</Text>
          <Text style={styles.statusBadge}>STATUS: IN-FLIGHT</Text>
          <Text style={styles.telemetryText}>Order ID: {orderId}</Text>
          <Text style={styles.telemetryText}>Latitude: {droneTelemetry.lat}</Text>
          <Text style={styles.telemetryText}>Longitude: {droneTelemetry.lon}</Text>
          <Text style={styles.telemetryText}>Altitude: {droneTelemetry.alt} m</Text>
          <Text style={styles.telemetryText}>Speed: {droneTelemetry.speed} m/s</Text>
          <Text style={styles.telemetryText}>Drone Battery: {droneTelemetry.battery}%</Text>

          <TouchableOpacity style={[styles.button, styles.cancelButton]} onPress={() => setStep(2)}>
            <Text style={styles.buttonText}>Cancel Flight Mission</Text>
          </TouchableOpacity>
        </View>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0a0b0d',
  },
  header: {
    padding: 20,
    backgroundColor: '#121318',
    borderBottomWidth: 1,
    borderBottomColor: '#20222a',
    alignItems: 'center'
  },
  headerTitle: {
    color: '#00e5ff',
    fontWeight: 'bold',
    fontSize: 18,
    letterSpacing: 1
  },
  scroll: {
    flex: 1,
  },
  card: {
    backgroundColor: '#121318',
    borderRadius: 12,
    padding: 20,
    margin: 20,
    borderWidth: 1,
    borderColor: '#20222a',
  },
  title: {
    color: '#fff',
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  subtitle: {
    color: '#888',
    fontSize: 14,
    marginBottom: 20,
  },
  label: {
    color: '#00e5ff',
    fontSize: 12,
    fontWeight: 'bold',
    marginBottom: 5,
    textTransform: 'uppercase',
  },
  input: {
    backgroundColor: '#1c1e24',
    borderRadius: 8,
    padding: 12,
    color: '#fff',
    fontSize: 15,
    marginBottom: 15,
    borderWidth: 1,
    borderColor: '#2e323e',
  },
  button: {
    backgroundColor: '#00e5ff',
    borderRadius: 8,
    padding: 15,
    alignItems: 'center',
    marginTop: 10,
  },
  cancelButton: {
    backgroundColor: '#ff3d00',
    marginTop: 20,
  },
  buttonText: {
    color: '#0a0b0d',
    fontWeight: 'bold',
    fontSize: 16,
  },
  statusBadge: {
    color: '#00ff66',
    fontWeight: 'bold',
    fontSize: 14,
    backgroundColor: '#00ff6615',
    padding: 8,
    borderRadius: 6,
    alignSelf: 'flex-start',
    marginBottom: 15,
    letterSpacing: 1
  },
  telemetryText: {
    color: '#ccc',
    fontSize: 15,
    marginBottom: 8,
    fontFamily: 'monospace'
  }
});
