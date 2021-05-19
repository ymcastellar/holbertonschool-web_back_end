#!/usr/bin/env python3
""" SessionAuth class to manage API authentication """


from api.v1.auth.auth import Auth
import uuid


class SessionAuth (Auth):
    """ SessionAuth class to manage API authentication """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ create a Session ID for a user_id """
        if isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ session id """
        if isinstance(session_id, str):
            return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return a User instance based on a cookie value
        """
        return User.get(
            self.user_id_for_session_id(self.session_cookie(request)))
