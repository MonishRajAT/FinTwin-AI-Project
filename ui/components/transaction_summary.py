# Premium transaction summary cards.

import streamlit as st

def render_transaction_summary(df):
    """
    Render transaction summary cards.
    """

    if df.empty:

        st.info("No transaction data available.")

        return

    income = df.loc[
        df["transaction_type"] == "Income",
        "amount"
    ].sum()

    expense = df.loc[
        df["transaction_type"] == "Expense",
        "amount"
    ].sum()

    cash_flow = income - expense

    total_transactions = len(df)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "💰 Total Income",
            f"₹ {income:,.0f}"
        )

    with c2:
        st.metric(
            "💳 Total Expenses",
            f"₹ {expense:,.0f}"
        )

    with c3:
        st.metric(
            "📈 Net Cash Flow",
            f"₹ {cash_flow:,.0f}"
        )

    with c4:
        st.metric(
            "🧾 Transactions",
            total_transactions
        )