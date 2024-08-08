import os
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Session authentication class.
    """

    def __init__(self):
        """Initialize the SessionAuth class."""
        super().__init__()
        self.user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session ID for a user.
        """
        if user_id is None:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Get a user ID based on a session ID.
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def session_cookie(self, request=None) -> str:
        """Get the session cookie value from the request.
        Args:
            request (flask.Request, optional): The Flask request object.
        Returns:
            str: The value of the session cookie or
            None if the cookie is not present.
        """
        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME', '_my_session_id')
        return request.cookies.get(session_name, None)

    def current_user(self, request=None):
        """Get the current user based on the session cookie.
        """
        if request is None:
            return None
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None
        return User.get(user_id)
