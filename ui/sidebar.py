"""
Reusable sidebar for FinTwin AI.
"""

import streamlit as st

PAGES = {
    "🏠 Dashboard": "dashboard",
    "👤 Financial Twin": "financial_profile",
    "💳 Transactions": "transactions",
    "📈 Analytics": "analytics",
    "🤖 AI Copilot": "copilot",
    "📄 Documents": "documents",
    "🎯 Simulator": "simulator",
    "⚙️ Settings": "settings",
}


def render_sidebar(user: dict):
    """
    Render application sidebar.

    Returns
    -------
    str
        Selected page identifier.
    """

    with st.sidebar:

        st.markdown(
            """
            # 💰 FinTwin AI
            ### Financial Intelligence Platform
            """
        )

        st.divider()

        st.markdown("### 👤 Logged In")

        st.write(f"**{user['full_name']}**")
        st.caption(user["email"])

        st.divider()

        if "selected_page" not in st.session_state:
            st.session_state.selected_page = "dashboard"

        for title, page in PAGES.items():

            if st.button(
                title,
                use_container_width=True,
                key=page
            ):
                st.session_state.selected_page = page
                st.rerun()

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True,
            type="primary",
        ):
            from auth.session import logout

            logout()
            st.rerun()

    return st.session_state.selected_page