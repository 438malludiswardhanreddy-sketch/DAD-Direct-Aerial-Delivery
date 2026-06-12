import React, { useState } from 'react';
import { StyleSheet, Text, View, SafeAreaView, TouchableOpacity, ScrollView } from 'react-native';

import LoginScreen from './src/screens/Login';
import RegistrationScreen from './src/screens/Registration';
import OrderCreationScreen from './src/screens/OrderCreation';
import TrackingScreen from './src/screens/Tracking';
import NotificationsScreen from './src/screens/Notifications';
import ProfileScreen from './src/screens/Profile';
import SettingsScreen from './src/screens/Settings';

export default function App() {
  const [phone, setPhone] = useState('');
  const [tab, setTab] = useState('login'); // login, register, book, track, notifications, profile, settings
  const [orderLat, setOrderLat] = useState('17.6721');
  const [orderLon, setOrderLon] = useState('75.9125');

  const handleLoginSuccess = (phoneNum: string) => {
    setPhone(phoneNum);
    setTab('book');
  };

  const handleOrderConfirm = (lat: string, lon: string) => {
    setOrderLat(lat);
    setOrderLon(lon);
    setTab('track');
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>🛸 DAD - Direct Aerial Delivery</Text>
      </View>

      <ScrollView style={styles.main}>
        {tab === 'login' && <LoginScreen onLoginSuccess={handleLoginSuccess} />}
        {tab === 'register' && <RegistrationScreen />}
        {tab === 'book' && <OrderCreationScreen onOrderConfirm={handleOrderConfirm} />}
        {tab === 'track' && <TrackingScreen lat={orderLat} lon={orderLon} />}
        {tab === 'notifications' && <NotificationsScreen />}
        {tab === 'profile' && <ProfileScreen />}
        {tab === 'settings' && <SettingsScreen />}
      </ScrollView>

      {phone !== '' && (
        <View style={styles.tabsContainer}>
          <TouchableOpacity style={styles.tabBtn} onPress={() => setTab('book')}>
            <Text style={[styles.tabText, tab === 'book' && styles.activeTab]}>Book</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.tabBtn} onPress={() => setTab('track')}>
            <Text style={[styles.tabText, tab === 'track' && styles.activeTab]}>Track</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.tabBtn} onPress={() => setTab('notifications')}>
            <Text style={[styles.tabText, tab === 'notifications' && styles.activeTab]}>Alerts</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.tabBtn} onPress={() => setTab('profile')}>
            <Text style={[styles.tabText, tab === 'profile' && styles.activeTab]}>Profile</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.tabBtn} onPress={() => setTab('settings')}>
            <Text style={[styles.tabText, tab === 'settings' && styles.activeTab]}>Settings</Text>
          </TouchableOpacity>
        </View>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#0a0b0d' },
  header: { padding: 20, backgroundColor: '#121318', borderBottomWidth: 1, borderBottomColor: '#20222a', alignItems: 'center' },
  headerTitle: { color: '#00e5ff', fontWeight: 'bold', fontSize: 18, letterSpacing: 1 },
  main: { flex: 1, padding: 15 },
  tabsContainer: { flexDirection: 'row', backgroundColor: '#121318', borderTopWidth: 1, borderTopColor: '#20222a', paddingVertical: 10, justifyContent: 'space-around' },
  tabBtn: { padding: 10 },
  tabText: { color: '#888', fontWeight: 'bold' },
  activeTab: { color: '#00e5ff' }
});
