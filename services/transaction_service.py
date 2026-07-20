# Business logic for transaction management.

from repositories.transaction_repository import (
    create_transaction,
    get_transaction,
    get_transactions,
    update_transaction,
    delete_transaction,
)
from services.dashboard_service import DashboardService

class TransactionService:

    VALID_CATEGORIES = [
        "Food",
        "Shopping",
        "Transport",
        "Bills",
        "Entertainment",
        "Healthcare",
        "Education",
        "Investment",
        "Salary",
        "Other",
    ]

    VALID_TRANSACTION_TYPES = [
        "Income",
        "Expense",
    ]

    VALID_PAYMENT_METHODS = [
        "Cash",
        "UPI",
        "Debit Card",
        "Credit Card",
        "Net Banking",
        "Wallet",
    ]

    VALID_CURRENCIES = [
        "INR",
        "USD",
        "EUR",
    ]

    @staticmethod
    def add_transaction(
        user_id: int,
        transaction_date,
        merchant: str,
        category: str,
        amount: float,
        transaction_type: str,
        payment_method: str,
        currency: str,
        recurring: bool,
        notes: str,
    ):

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )

        if category not in TransactionService.VALID_CATEGORIES:
            raise ValueError(
                "Invalid transaction category."
            )

        if (
            transaction_type
            not in TransactionService.VALID_TRANSACTION_TYPES
        ):
            raise ValueError(
                "Invalid transaction type."
            )

        if (
            payment_method
            not in TransactionService.VALID_PAYMENT_METHODS
        ):
            raise ValueError(
                "Invalid payment method."
            )

        currency = currency.upper()

        if currency not in TransactionService.VALID_CURRENCIES:
            raise ValueError(
                "Unsupported currency."
            )

        create_transaction(
            user_id=user_id,
            transaction_date=transaction_date,
            merchant=merchant.strip(),
            category=category,
            amount=amount,
            transaction_type=transaction_type,
            payment_method=payment_method,
            currency=currency,
            recurring=recurring,
            notes=notes.strip(),
        )

        # Refresh dashboard metrics
        DashboardService.refresh_dashboard(user_id)

        return {
            "success": True,
            "message": "Transaction added successfully.",
        }

    @staticmethod
    def get_all_transactions(user_id: int):
        return get_transactions(user_id)

    @staticmethod
    def get_transaction(transaction_id: int):
        return get_transaction(transaction_id)

    @staticmethod
    def update_transaction(
        transaction_id,
        transaction_date,
        merchant,
        category,
        amount,
        transaction_type,
        payment_method,
        currency,
        recurring,
        notes,
        user_id,
    ):

        if amount <= 0:
            raise ValueError(
                "Amount must be greater than zero."
            )

        update_transaction(
            transaction_id,
            transaction_date,
            merchant.strip(),
            category,
            amount,
            transaction_type,
            payment_method,
            currency.upper(),
            recurring,
            notes.strip(),
        )

        DashboardService.refresh_dashboard(user_id)

        return {
            "success": True,
            "message": "Transaction updated successfully.",
        }

    @staticmethod
    def delete_transaction(
        transaction_id: int,
        user_id: int,
    ):

        delete_transaction(transaction_id)

        DashboardService.refresh_dashboard(user_id)

        return {
            "success": True,
            "message": "Transaction deleted successfully.",
        }