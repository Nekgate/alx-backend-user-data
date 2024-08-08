#!/usr/bin/env python3
"""Session authentication module.
"""
import uuid
from typing import TypeVar, Dict
from flask import request
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session authentication class.
    """
    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a user.
        """
        if user_id is None:
            return None

        # Generate a new UUID for the session ID
        session_id = str(uuid.uuid4())
        # Store the session ID and associate user ID
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Gets the User ID based on a Session ID.
        """
        if not isinstance(session_id, str):
            return None
        # Retrieve the user ID for the given session ID
        return self.user_id_by_session_id.get(session_id, None)

    def session_cookie(self, request=None) -> str:
        """Gets the session cookie value from the request.
        """
        if request is None:
            return None
        session_name = getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name, None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user based on the session ID.
        """
        if request is None:
            return None

        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return None

        return User.get(user_id)
