#!/usr/bin/env python3
"""Session authentication with database storage module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta  # Import for expiration check


class SessionDBAuth(SessionExpAuth):
    """Session authentication with database storage class"""

    def create_session(self, user_id=None):
        """Create and store new instance of UserSession"""
        session_id = super().create_session(user_id)  # Could return None
        if session_id is None:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        # UserSession.save_to_file()  # No longer needed, save() handles it.
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns User ID by requesting UserSession in database"""
        if session_id is None:
            return None

        # UserSession.load_from_file()  # No longer needed.  search() handles.
        # Use a try-except block for potential database errors.
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None

        if not sessions:
            return None

        # Check for expiration, using logic from SessionExpAuth
        session = sessions[0]
        if self.session_duration <= 0:
            return session.user_id

        created_at = session.created_at
        if created_at is None:
            return None

        expired_time = created_at + timedelta(seconds=self.session_duration)
        if expired_time < datetime.now():
            # session.remove() #If expired, remove from db. Good practice.
            return None

        return session.user_id

    def destroy_session(self, request=None):
        """Destroys UserSession based on Session ID from request cookie"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # UserSession.load_from_file() # No longer needed, search() handles.
        try:
            sessions = UserSession.search({'session_id': session_id})
        except Exception:  # More specific exception.
            return False

        if not sessions:
            return False

        sessions[0].remove()
        # UserSession.save_to_file() # remove() should handle saving.
        return True
