# Transactions charts for FinTwin AI.

import plotly.express as px

def expense_category_chart(df):

    expense_df = df[
        df["transaction_type"] == "Expense"
    ]

    if expense_df.empty:
        return None
    
    grouped = (
        expense_df
        .groupby("category")["amount"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        grouped,
        names="category",
        values="amount",
        hole=0.6,
        title="Expense Distribution",
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=420,
    )

    return fig

def income_vs_expense_chart(df):

    grouped = (
        df.groupby("transaction_type")["amount"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        grouped,
        x="transaction_type",
        y="amount",
        color="transaction_type",
        title="Income vs Expense",
    )

    fig.update_layout(
        paper_bgcolor="#0B1120",
        plot_bgcolor="#0B1120",
        font=dict(color="white"),
        height=420,
    )

    return fig