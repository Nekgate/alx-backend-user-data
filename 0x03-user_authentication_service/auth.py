#!/usr/bin/env python3
"""Authentication
"""
import bcrypt

def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt and
    return the hashed password as bytes.
    """
    # Convert the password string to bytes.
    password_bytes = password.encode('utf-8')
    # Genarate a salt and hash the password
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password
