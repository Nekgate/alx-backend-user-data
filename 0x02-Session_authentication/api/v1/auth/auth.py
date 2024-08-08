#!/usr/bin/env python3
"""Authentication module for the API.
"""
import re
import os
from typing import List, TypeVar
from flask import request


class Auth:
    """Authentication class for handling
    various authentication-related tasks.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a path requires authentication based on excluded paths.
        Args:
            path (str): The path to check.
            excluded_paths (List[str]): List of
            paths that do not require authentication.
        Returns:
            bool: True if authentication is required,
            False otherwise.
        """
        if path and excluded_paths:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                if exclusion_path.endswith('*'):
                    pattern = '{}.*'.format(exclusion_path[:-1])
                elif exclusion_path.endswith('/'):
                    pattern = '{}/*'.format(exclusion_path[:-1])
                else:
                    pattern = '{}/*'.format(exclusion_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """Gets the authorization header field from the request.
        """
        if request:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Gets the current user from the request.
        """
        return None

    def session_cookie(self, request=None) -> str:
        """Gets the session cookie value from the request.
        Args:
            request (flask.Request, optional): The Flask request object.
        Returns:
            str: The value of the session cookie
            or None if the cookie is not present.
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name, None)
