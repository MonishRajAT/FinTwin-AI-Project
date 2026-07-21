# Reusable Plotly charts for FinTwin AI Analytics.

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def expense_distribution_chart(expense_by_category):

    if expense_by_category.empty:
        return None

    fig = px.pie(
        expense_by_category,
        names="category",
        values="amount",
        hole=0.65,
        title="Expense Distribution",
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=450,
        margin=dict(l=20, r=20, t=60, b=20),
    )

    return fig

def monthly_income_expense_chart(monthly_summary):

    if monthly_summary.empty:
        return None

    fig = px.bar(
        monthly_summary,
        x="month",
        y="amount",
        color="transaction_type",
        barmode="group",
        title="Monthly Income vs Expense",
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=450,
        xaxis_title="Month",
        yaxis_title="Amount (₹)",
    )

    return fig

def top_merchants_chart(top_merchants):

    if top_merchants.empty:
        return None

    fig = px.bar(
        top_merchants,
        x="amount",
        y="merchant",
        orientation="h",
        title="Top Spending Merchants",
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=450,
        xaxis_title="Amount (₹)",
        yaxis_title="",
    )

    return fig

def cash_flow_trend_chart(df):

    if df.empty:
        return None

    temp = df.copy()

    temp["transaction_date"] = pd.to_datetime(
        temp["transaction_date"]
    )

    temp["month"] = temp["transaction_date"].dt.strftime("%b %Y")

    income = (
        temp[temp["transaction_type"] == "Income"]
        .groupby("month")["amount"]
        .sum()
    )

    expense = (
        temp[temp["transaction_type"] == "Expense"]
        .groupby("month")["amount"]
        .sum()
    )

    summary = (
        income.subtract(expense, fill_value=0)
        .reset_index()
    )

    summary.columns = ["month", "cash_flow"]

    fig = px.line(

        summary,
        x="month",
        y="cash_flow",
        markers=True,
        title="Monthly Cash Flow",

    )

    fig.update_layout(

        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=420,

    )

    return fig

def top_categories_chart(expense_by_category):

    if expense_by_category.empty:
        return None

    fig = px.bar(

        expense_by_category,
        x="amount",
        y="category",
        orientation="h",
        title="Top Spending Categories",

    )

    fig.update_layout(

        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=420,

    )

    return fig

def budget_gauge(utilization):

    fig = go.Figure(

        go.Indicator(

            mode="gauge+number",
            value=utilization,
            number={"suffix": "%"},
            title={"text": "Budget Utilization"},
            gauge={

                "axis": {

                    "range": [0, 100]

                },

                "bar": {

                    "color": "#2563EB"

                },

                "steps": [

                    {

                        "range": [0, 60],

                        "color": "#10B981"

                    },

                    {

                        "range": [60, 85],

                        "color": "#F59E0B"

                    },

                    {

                        "range": [85, 100],

                        "color": "#EF4444"

                    },

                ],

            },

        )

    )

    fig.update_layout(

        paper_bgcolor="#0B1120",
        font=dict(color="white"),
        height=420,

    )

    return fig

