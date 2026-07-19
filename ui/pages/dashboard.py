# Premium Dashboard for FinTwin AI.

import streamlit as st
from services.dashboard_service import DashboardService
from ui.styles import load_global_styles
from ui.cards import inject_card_styles, kpi_card
from ui.components import page_header
from ui.charts import (
    financial_health_gauge,
    financial_ratios_chart,
)

def render_dashboard(user):
    """
    Render FinTwin AI Dashboard.
    """

    load_global_styles()
    inject_card_styles()

    dashboard = DashboardService.get_dashboard(
        user["user_id"]
    )

    profile = dashboard["profile"]
    health = dashboard["health"]

    page_header(
        "🏠 Dashboard",
        "Welcome back! Here's your financial overview."
    )

    # HEALTH SCORE
    col1, col2 = st.columns([1, 1])

    with col1:

        st.plotly_chart(
            financial_health_gauge(
                health["financial_health_score"]
            ),
            use_container_width=True,
        )

    with col2:

        st.markdown(
        f"""
<div class="ft-card">

<h2>🏆 Financial Status</h2>

<h1 style="
font-size:52px;
color:#22C55E;
">

{health['status']}

</h1>

<p>

Health Score

<b>{health['financial_health_score']}/100</b>

</p>

<p>

Monthly Savings

<b>₹ {health['monthly_savings']:,.0f}</b>

</p>

<p>

Emergency Fund

<b>{health['emergency_months']} Months</b>

</p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    # KPI CARDS
    col1, col2 = st.columns(2)

    col3, col4 = st.columns(2)

    with col1:

        kpi_card(

            "Monthly Income",

            f"₹ {profile['monthly_income']:,.0f}",

            "💰",

            "Income",

            100,
        )

    with col2:

        kpi_card(

            "Investments",

            f"₹ {profile['total_investments']:,.0f}",

            "📈",

            "Portfolio",

            75,
        )

    with col3:

        kpi_card(

            "Loans",

            f"₹ {profile['total_loans']:,.0f}",

            "💳",

            "Outstanding",

            45,
        )

    with col4:

        kpi_card(

            "Emergency Fund",

            f"₹ {profile['emergency_fund']:,.0f}",

            "🛡",

            "Available",

            85,
        )

    st.write("")

    st.plotly_chart(

        financial_ratios_chart(

            health["savings_rate"],

            health["debt_ratio"],

            health["investment_ratio"],

        ),

        use_container_width=True,
        
    )

    # FINANCIAL METRICS
    st.subheader("📊 Financial Metrics")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Savings Rate",
        f"{health['savings_rate']}%"
    )

    c2.metric(
        "Debt Ratio",
        f"{health['debt_ratio']}%"
    )

    c3.metric(
        "Investment Ratio",
        f"{health['investment_ratio']}%"
    )

    st.write("")

    # AI INSIGHTS
    st.subheader("🤖 AI Financial Insights")

    for insight in health["insights"]:

        st.success(insight)

    st.write("")

    # QUICK ACTIONS
    st.subheader("⚡ Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.button(
            "➕ Add Transaction",
            use_container_width=True
        )

    with col2:

        st.button(
            "🎯 Set Goal",
            use_container_width=True
        )

    with col3:

        st.button(
            "🤖 Ask AI",
            use_container_width=True
        )