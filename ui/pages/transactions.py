# Transaction Management Page

import pandas as pd
import streamlit as st
from auth.session import get_current_user
from services.transaction_service import TransactionService
from ui.components import page_header
from ui.styles import load_global_styles
from ui.cards import inject_card_styles
from ui.transaction_summary import (
    render_transaction_summary,
)
from datetime import datetime
from ui.transaction_charts import (
    expense_category_chart,
    income_vs_expense_chart,
)
from ui.ai_spending_insights import (
    render_ai_spending_insights,
)

def render_transactions():

    load_global_styles()
    inject_card_styles()

    user = get_current_user()

    page_header(
        "💳 Transactions",
        "Track your income and expenses."
    )

    # ADD TRANSACTION

    with st.expander(
        "➕ Add Transaction",
        expanded=True,
    ):

        col1, col2 = st.columns(2)

        with col1:

            transaction_date = st.date_input(
                "Transaction Date"
            )

            merchant = st.text_input(
                "Merchant"
            )

            category = st.selectbox(
                "Category",
                TransactionService.VALID_CATEGORIES,
            )

            amount = st.number_input(
                "Amount",
                min_value=0.0,
                step=100.0,
            )

        with col2:

            transaction_type = st.selectbox(
                "Transaction Type",
                TransactionService.VALID_TRANSACTION_TYPES,
            )

            payment_method = st.selectbox(
                "Payment Method",
                TransactionService.VALID_PAYMENT_METHODS,
            )

            recurring = st.checkbox(
                "Recurring Transaction"
            )

            notes = st.text_area(
                "Notes"
            )

        if st.button(
            "💾 Save Transaction",
            use_container_width=True,
            type="primary",
        ):

            try:

                TransactionService.add_transaction(

                    user_id=user["user_id"],

                    transaction_date=transaction_date,

                    merchant=merchant,

                    category=category,

                    amount=amount,

                    transaction_type=transaction_type,

                    payment_method=payment_method,

                    currency="INR",

                    recurring=recurring,

                    notes=notes,
                )

                st.success(
                    "Transaction added successfully."
                )

                st.rerun()

            except Exception as e:

                st.error(str(e))

    st.divider()

    # TRANSACTION HISTORY

    page_header(
        "📜 Transaction History",
        ""
    )

    transactions = TransactionService.get_all_transactions(
        user["user_id"]
    )

    if not transactions:

        st.info(
            "No transactions found."
        )

        return

    df = pd.DataFrame(transactions)
    render_transaction_summary(df)
    col1, col2 = st.columns(2)

    with col1:

        fig = expense_category_chart(df)

        if fig:
            st.plotly_chart(
                fig,
                use_container_width=True,
            )

    with col2:

        st.plotly_chart(

            income_vs_expense_chart(df),

            use_container_width=True,
        )

    render_ai_spending_insights(df)

    # SEARCH

    search = st.text_input(
        "🔍 Search Merchant"
    )

    if search:

        df = df[
            df["merchant"]
            .str.contains(
                search,
                case=False,
                na=False,
            )
        ]

    # FILTERS

    col1, col2 = st.columns(2)

    with col1:

        category_filter = st.selectbox(
            "Category Filter",
            ["All"] + TransactionService.VALID_CATEGORIES,
        )

    with col2:

        type_filter = st.selectbox(
            "Type Filter",
            ["All"] + TransactionService.VALID_TRANSACTION_TYPES,
        )

    if category_filter != "All":

        df = df[
            df["category"] == category_filter
        ]

    if type_filter != "All":

        df = df[
            df["transaction_type"] == type_filter
        ]

    # EDIT TRANSACTION

    if "edit_transaction" in st.session_state:

        transaction = TransactionService.get_transaction(
            st.session_state.edit_transaction
        )

        if transaction:

            st.divider()
            st.subheader("✏️ Edit Transaction")

            with st.form("edit_transaction_form"):

                col1, col2 = st.columns(2)

                with col1:

                    transaction_date = st.date_input(
                        "Transaction Date",
                        value=transaction["transaction_date"],
                    )

                    merchant = st.text_input(
                        "Merchant",
                        value=transaction["merchant"],
                    )

                    category = st.selectbox(
                        "Category",
                        TransactionService.VALID_CATEGORIES,
                        index=TransactionService.VALID_CATEGORIES.index(
                            transaction["category"]
                        ),
                    )

                    amount = st.number_input(
                        "Amount",
                        value=float(transaction["amount"]),
                        min_value=0.0,
                    )

                with col2:

                    transaction_type = st.selectbox(
                        "Transaction Type",
                        TransactionService.VALID_TRANSACTION_TYPES,
                        index=TransactionService.VALID_TRANSACTION_TYPES.index(
                            transaction["transaction_type"]
                        ),
                    )

                    payment_method = st.selectbox(
                        "Payment Method",
                        TransactionService.VALID_PAYMENT_METHODS,
                        index=TransactionService.VALID_PAYMENT_METHODS.index(
                            transaction["payment_method"]
                        ),
                    )

                    recurring = st.checkbox(
                        "Recurring",
                        value=transaction["recurring"],
                    )

                    notes = st.text_area(
                        "Notes",
                        value=transaction["notes"] or "",
                    )

                submitted = st.form_submit_button(
                    "💾 Update Transaction",
                    use_container_width=True,
                )

                if submitted:

                    TransactionService.update_transaction(

                        transaction_id=transaction["transaction_id"],

                        transaction_date=transaction_date,

                        merchant=merchant,

                        category=category,

                        amount=amount,

                        transaction_type=transaction_type,

                        payment_method=payment_method,

                        currency=transaction["currency"],

                        recurring=recurring,

                        notes=notes,

                        user_id=user["user_id"],
                    )

                    del st.session_state.edit_transaction

                    st.success("Transaction updated successfully.")

                    st.rerun()

    # DISPLAY

    st.subheader("📜 Your Transactions")

    for _, row in df.iterrows():

        with st.container(border=True):

            c1, c2, c3, c4 = st.columns([3, 2, 2, 2])

            with c1:

                st.markdown(f"### {row['merchant']}")
                st.caption(row["transaction_date"])

                st.write(
                    f"**Category:** {row['category']}"
                )

                st.write(
                    f"**Payment:** {row['payment_method']}"
                )

            with c2:

                st.metric(
                    "Amount",
                    f"₹ {row['amount']:,.2f}"
                )

            with c3:

                st.write("")

                if st.button(
                    "✏️ Edit",
                    key=f"edit_{row['transaction_id']}"
                ):
                    st.session_state.edit_transaction = row["transaction_id"]

            with c4:

                st.write("")

                if st.button(
                    "🗑 Delete",
                    key=f"delete_{row['transaction_id']}"
                ):

                    TransactionService.delete_transaction(

                        transaction_id=row["transaction_id"],

                        user_id=user["user_id"]

                    )

                    st.success(
                        "Transaction deleted."
                    )

                    st.rerun()