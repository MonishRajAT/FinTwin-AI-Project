# Authentication page for FinTwin AI.

import streamlit as st
from auth.auth_service import AuthService
from auth.session import login as create_session

def render_login_page():
    """
    Render Login / Register page.
    """

    st.title("💰 FinTwin AI")
    st.caption("Your Financial Digital Twin for Smarter Financial Decisions")

    login_tab, register_tab = st.tabs(
        ["🔐 Login", "📝 Register"]
    )

    # LOGIN
    with login_tab:

        st.subheader("Welcome Back")

        with st.form("login_form"):

            email = st.text_input(
                "Email",
                placeholder="Enter your email"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            login_button = st.form_submit_button(
                "Sign In",
                use_container_width=True
            )

        if login_button:

            try:

                response = AuthService.login_user(
                    email=email,
                    password=password
                )

                create_session(response["user"])

                st.success("Login successful!")

                st.rerun()

            except Exception as e:

                st.error(str(e))

    # REGISTER
    with register_tab:

        st.subheader("Create Account")

        with st.form("register_form"):

            full_name = st.text_input(
                "Full Name"
            )

            email = st.text_input(
                "Email"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password"
            )

            register_button = st.form_submit_button(
                "Create Account",
                use_container_width=True
            )

        if register_button:

            if password != confirm_password:

                st.error("Passwords do not match.")

            else:

                try:

                    AuthService.register_user(
                        full_name=full_name,
                        email=email,
                        password=password
                    )

                    st.success(
                        "Account created successfully! Please login."
                    )

                except Exception as e:

                    st.error(str(e))