# FinTwin AI: Application entry point.

import streamlit as st
from auth.session import (
    initialize_session,
    is_authenticated,
    logout,
    get_current_user
)
from ui.pages.login import render_login_page
from repositories.profile_repository import get_profile
from ui.pages.financial_profile import render_financial_profile
from ui.sidebar import render_sidebar
from ui.pages.dashboard import render_dashboard


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="FinTwin AI",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Initialize Session
# ---------------------------------------------------------

initialize_session()

# ---------------------------------------------------------
# Authentication
# ---------------------------------------------------------

if not is_authenticated():

    render_login_page()

    st.stop()

# ---------------------------------------------------------
# Current User
# ---------------------------------------------------------

user = get_current_user()

profile = get_profile(user["user_id"])

# ---------------------------------------------------------
# First Time User
# ---------------------------------------------------------

if (
    profile is None
    or profile["monthly_income"] == 0
):

    render_financial_profile()

    st.stop()

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------

selected_page = render_sidebar(user)

# ---------------------------------------------------------
# Dashboard
# ---------------------------------------------------------

if selected_page == "dashboard":
    render_dashboard(user)

elif selected_page == "financial_profile":

    render_financial_profile()

elif selected_page == "transactions":

    st.info("Transactions Module Coming Soon.")

elif selected_page == "analytics":

    st.info("Analytics Module Coming Soon.")

elif selected_page == "copilot":

    st.info("AI Copilot Coming Soon.")

elif selected_page == "documents":

    st.info("Document Intelligence Coming Soon.")

elif selected_page == "simulator":

    st.info("Scenario Simulator Coming Soon.")

elif selected_page == "settings":

    st.info("Settings Coming Soon.")