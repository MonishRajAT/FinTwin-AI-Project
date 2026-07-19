"""
Session management utilities for FinTwin AI.

This module provides a clean wrapper around Streamlit's
session_state and should be the only place that directly
manipulates authentication session variables.
"""

import streamlit as st

# Session keys
AUTH_KEY = "authenticated"
USER_KEY = "current_user"

def initialize_session():
    """
    Initialize session variables if they don't exist.
    Safe to call multiple times.
    """
    if AUTH_KEY not in st.session_state:
        st.session_state[AUTH_KEY] = False
    if USER_KEY not in st.session_state:
        st.session_state[USER_KEY] = None

def login(user: dict):
    """
    Store authenticated user in session.
    """
    initialize_session()
    st.session_state[AUTH_KEY] = True
    st.session_state[USER_KEY] = user

def logout():
    """
    Clear authentication session.
    """
    initialize_session()
    st.session_state[AUTH_KEY] = True
    st.session_state[USER_KEY] = None

def is_authenticated() -> bool:
    """
    Returns True if user is logged in.
    """
    initialize_session()
    return st.session_state[AUTH_KEY]

def get_current_user():
    """
    Returns the current logged-in user.

    Returns:
        dict | None
    """
    initialize_session()
    return st.session_state[USER_KEY]

def get_current_user_id():
    """
    Returns the logged-in user's ID.

    Return:
        int | None
    """
    user = get_current_user()
    if user is None:
        return None
    return user.get("user_id")

def require_authentication():
    """
    Stops page execution if the user is
    not authenticated.
    """
    initialize_session()
    if not is_authenticated():
        st.warning("Please login to continue.")
        st.stop()
