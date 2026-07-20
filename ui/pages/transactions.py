# Transaction Management Page

import pandas as pd
import streamlit as st
from auth.session import get_current_user
from services.transaction_service import TransactionService
from ui.components import page_header
from ui.styles import load_global_styles
from ui.cards import inject_card_styles
from ui.components.transaction_summary import (
    render_transaction_summary,
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

    # DISPLAY

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
    )