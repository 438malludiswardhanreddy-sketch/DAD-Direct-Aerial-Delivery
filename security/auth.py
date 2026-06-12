"""
Solapur University - Final Year Engineering Project
Department of Electronics and Telecommunication Engineering

Module: Authentication & Authorization Helper
Description: Handles JWT token generation, role verification, and drone registration hashes.
"""

import jwt
import datetime
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

SECRET_KEY = "solapur-secret-session-key"
ALGORITHM = "HS256"
security_bearer = HTTPBearer()

class AuthHandler:
    def hash_password(self, password: str) -> str:
        """
        Simple hashing algorithm for user database records.
        """
        import hashlib
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def generate_token(self, subject: str, role: str = "operator") -> str:
        """
        Encodes a JWT session token valid for 2 hours.
        """
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2),
            "iat": datetime.datetime.utcnow(),
            "sub": subject,
            "role": role
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def decode_token(self, token: str) -> dict:
        """
        Decodes and validates the signature of a session token.
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Session token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid authorization token")

    def get_current_user(self, credentials: HTTPAuthorizationCredentials = Security(security_bearer)) -> dict:
        """
        FastAPI router dependency to inject the current authenticated session claims.
        """
        return self.decode_token(credentials.credentials)

    def check_permissions(self, token_payload: dict, required_role: str) -> bool:
        """
        Validates if the user contains the required RBAC privilege levels.
        """
        role = token_payload.get("role", "operator")
        role_hierarchy = {"student": 1, "operator": 2, "admin": 3}
        return role_hierarchy.get(role, 0) >= role_hierarchy.get(required_role, 0)
