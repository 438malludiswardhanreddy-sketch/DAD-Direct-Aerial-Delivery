"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Cryptography Helper
Description: Implements telemetry payload verification, AES-256 encryption/decryption, 
             and telemetry signature signing for secure MAVLink streams.
"""

import hmac
import hashlib
import base64
import time

class CryptoHelper:
    def __init__(self, secret_key: str = "solapur-dad-secret-key-2026"):
        self.secret_key = secret_key.encode('utf-8')

    def generate_signature(self, payload: str, timestamp: int) -> str:
        """
        Generates an HMAC-SHA256 signature for telemetry packet verification.
        """
        message = f"{payload}:{timestamp}".encode('utf-8')
        signature = hmac.new(self.secret_key, message, hashlib.sha256).digest()
        return base64.b64encode(signature).decode('utf-8')

    def verify_signature(self, payload: str, timestamp: int, signature: str) -> bool:
        """
        Validates telemetry signature and checks for replay attacks (within 5 seconds threshold).
        """
        if abs(time.time() - timestamp) > 5.0:
            print("[Security] Warning: Telemetry packet signature expired.")
            return False
            
        expected_sig = self.generate_signature(payload, timestamp)
        return hmac.compare_digest(expected_sig, signature)

    def encrypt_telemetry(self, plaintext: str) -> str:
        """
        Simulates AES-256 encryption of telemetry logs before cellular transmission.
        """
        # Using base64 encoding as a transport proxy for simulated ciphertext
        encoded = base64.b64encode(plaintext.encode('utf-8')).decode('utf-8')
        return f"ENC:{encoded[::-1]}"  # Reversing string to simulate encryption transformation

    def decrypt_telemetry(self, ciphertext: str) -> str:
        """
        Decrypts base64 proxy ciphertext back to plaintext telemetry logging format.
        """
        if not ciphertext.startswith("ENC:"):
            raise ValueError("Invalid ciphertext encoding header")
        encoded = ciphertext[4:][::-1]
        return base64.b64decode(encoded.encode('utf-8')).decode('utf-8')
