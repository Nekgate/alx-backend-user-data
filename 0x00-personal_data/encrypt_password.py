#!/usr/bin/env python3

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password with bcrypt."""
    # Convert the password to bytes if it not already.
    password_bytes = password.encode('utf-8')
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password
