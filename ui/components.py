"""
Reusable UI components for FinTwin AI.
"""

import streamlit as st

# PAGE HEADER
def page_header(title: str, subtitle: str):
    st.markdown(
        f"""
        <div class="fade-in">
            <div class="page-title">{title}</div>
            <div class="page-subtitle">{subtitle}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# SECTION TITLE
def section_title(title: str):
    st.markdown(
        f"""
        <div class="section-title">
            {title}
        </div>
        """,
        unsafe_allow_html=True,
    )

# METRIC CARD
def metric_card(
    title: str,
    value: str,
    change: str = "",
    icon: str = "📊",
):
    st.markdown(
        f"""
        <div class="metric-card fade-in">

            <div style="font-size:34px;">
                {icon}
            </div>

            <div class="metric-label">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div style="
                color:#22C55E;
                font-weight:600;
                margin-top:8px;
            ">
                {change}
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

# SUCCESS BOX
def success_box(message: str):

    st.markdown(
        f"""
        <div class="success-box">
            ✅ {message}
        </div>
        """,
        unsafe_allow_html=True,
    )

# WARNING BOX
def warning_box(message: str):

    st.markdown(
        f"""
        <div class="warning-box">
            ⚠️ {message}
        </div>
        """,
        unsafe_allow_html=True,
    )

# ERROR BOX
def error_box(message: str):

    st.markdown(
        f"""
        <div class="error-box">
            ❌ {message}
        </div>
        """,
        unsafe_allow_html=True,
    )

# GLASS CARD
def glass_card(content: str):

    st.markdown(
        f"""
        <div class="metric-card fade-in">
            {content}
        </div>
        """,
        unsafe_allow_html=True,
    )

# EMPTY STATE
def empty_state(
    title: str,
    subtitle: str,
    icon: str = "📭",
):

    st.markdown(
        f"""
        <div class="metric-card fade-in"
            style="text-align:center;">

            <div style="font-size:60px;">
                {icon}
            </div>

            <h3>{title}</h3>

            <p style="color:#94A3B8;">
                {subtitle}
            </p>

        </div>
        """,
        unsafe_allow_html=True,
    )

# DIVIDER
def divider():

    st.markdown(
        """
        <hr style="
            border:1px solid rgba(255,255,255,.08);
            margin-top:20px;
            margin-bottom:20px;
        ">
        """,
        unsafe_allow_html=True,
    )

# COMING SOON
def coming_soon(feature: str):

    glass_card(
        f"""
        <h2>🚀 {feature}</h2>

        <p style="color:#94A3B8;">
            This feature is currently under development.
        </p>
        """
    )