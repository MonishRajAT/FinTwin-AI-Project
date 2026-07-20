# AI-like spending insights generated from transaction data.

import streamlit as st

def render_ai_spending_insights(df):

    if df.empty:
        return

    expense_df = df[
        df["transaction_type"] == "Expense"
    ]

    if expense_df.empty:
        st.info("No expenses available yet.")
        return

    total_expense = expense_df["amount"].sum()

    top_category = (
        expense_df.groupby("category")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    category = top_category.index[0]

    category_amount = top_category.iloc[0]

    percentage = (
        category_amount /
        total_expense
    ) * 100

    highest_transaction = expense_df.loc[
        expense_df["amount"].idxmax()
    ]

    st.subheader("🤖 AI Spending Insights")

    st.success(
        f"📌 You spent the most on **{category}** "
        f"(₹{category_amount:,.0f}), "
        f"which is **{percentage:.1f}%** of your total expenses."
    )

    st.info(
        f"💸 Your largest expense was "
        f"**₹{highest_transaction['amount']:,.0f}** "
        f"at **{highest_transaction['merchant']}**."
    )

    if percentage > 40:

        st.warning(
            "⚠️ A large portion of your spending is concentrated "
            "in one category. Consider diversifying your expenses."
        )

    else:

        st.success(
            "✅ Your spending appears reasonably balanced."
        )