# Financial Analytics Dashboard.

import streamlit as st
from auth.session import get_current_user
from services.analytics_service import AnalyticsService
from ui.components import page_header
from ui.styles import load_global_styles
from ui.cards import inject_card_styles
from ui.analytics_charts import (
    expense_distribution_chart,
    monthly_income_expense_chart,
    top_merchants_chart,
    cash_flow_trend_chart,
    top_categories_chart,
    budget_gauge,
)

def render_analytics():

    load_global_styles()
    inject_card_styles()

    user = get_current_user()

    page_header(
        "📈 Financial Analytics",
        "Understand your financial behaviour with intelligent insights."
    )

    analytics = AnalyticsService.get_dashboard_analytics(
        user["user_id"]
    )

    # KPI CARDS

    # KPI ROW 1

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "💰 Total Income",
            f"₹ {analytics['total_income']:,.0f}"
        )
    
    with c2:
        st.metric(
            "💳 Total Expenses",
            f"₹ {analytics['total_expense']:,.0f}"
        )

    with c3:
        st.metric(
            "💵 Savings",
            f"₹ {analytics['savings']:,.0f}"
        )

    with c4:
        st.metric(
            "📈 Cash Flow",
            f"₹ {analytics['cash_flow']:,.0f}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # KPI ROW 2

    c5, c6, c7, c8 = st.columns(4)

    with c5:
        st.metric(
            "🏦 Net Worth",
            f"₹ {analytics['net_worth']:,.0f}"
        )

    with c6:
        st.metric(
            "📊 Savings Rate",
            f"{analytics['savings_rate']:.1f}%"
        )

    with c7:
        st.metric(
            "⚠️ Debt Ratio",
            f"{analytics['debt_to_income']:.1f}%"
        )

    with c8:
        st.metric(
            "🎯 Budget Used",
            f"{analytics['budget_utilization']:.1f}%"
        )

    st.divider()

    # ANALYTICS DASHBOARD

    st.divider()

    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:

        fig = expense_distribution_chart(
            analytics["expense_by_category"]
        )

        if fig:
            st.plotly_chart(
                fig,
                use_container_width=True,
            )

    with row1_col2:

        fig = cash_flow_trend_chart(
            analytics["df"]
        )

        if fig:
            st.plotly_chart(
                fig,
                use_container_width=True,
            )

    st.divider()

    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:

        fig = top_categories_chart(
            analytics["expense_by_category"]
        )

        if fig:
            st.plotly_chart(
                fig,
                use_container_width=True,
            )

    with row2_col2:

        fig = budget_gauge(
            analytics["budget_utilization"]
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.divider()

    fig = top_merchants_chart(
        analytics["top_merchants"]
    )

    if fig:

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.divider()

    fig = monthly_income_expense_chart(
        analytics["monthly_summary"]
    )

    if fig:

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    # AI SUMMARY

    st.divider()

    st.subheader("🤖 AI Financial Health Report")

    report = AnalyticsService.get_financial_health_report(
        user["user_id"]
    )

    for item in report:

        if item["type"] == "success":

            st.success(
                f"✅ {item['title']}\n\n{item['message']}"
            )

        elif item["type"] == "warning":

            st.warning(
                f"⚠️ {item['title']}\n\n{item['message']}"
            )

        elif item["type"] == "error":

            st.error(
                f"❌ {item['title']}\n\n{item['message']}"
            )

        else:

            st.info(
                f"ℹ️ {item['title']}\n\n{item['message']}"
            )