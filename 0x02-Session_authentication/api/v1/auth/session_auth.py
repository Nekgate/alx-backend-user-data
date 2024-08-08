#!/usr/bin/env python3
"""Session authentication module.
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session authentication class.
    Inherits from Auth but does not implement any methods yet
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a user_id.
        Args:
            user_id (str): The user ID for which to create a session.
        Returns:
            str: The session ID if successful.
            None: If user_id is None or not a string.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a new UUID for the session ID
        session_id = str(uuid.uuid4())
        # Store the session ID and associate user ID
        self.user_id_by_session_id[session_id] = user_id

        return session_id
