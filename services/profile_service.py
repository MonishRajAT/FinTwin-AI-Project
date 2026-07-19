# Business logic for the financial digital twin.

from repositories.profile_repository import (
    get_profile,
    update_profile
)


class ProfileService:
    """Business logic for financial profiles."""

    VALID_RISK_LEVELS = ["Low", "Medium", "High"]

    VALID_INVESTMENT_STYLES = [
        "Conservative",
        "Balanced",
        "Aggressive"
    ]

    VALID_CURRENCIES = ["INR", "USD", "EUR"]

    @staticmethod
    def get_profile(user_id: int):
        return get_profile(user_id)

    @staticmethod
    def update_profile(
        user_id: int,
        monthly_income: float,
        emergency_fund: float,
        total_investments: float,
        total_loans: float,
        insurance_cover: float,
        risk_appetite: str,
        investment_style: str,
        preferred_currency: str,
        monthly_budget: float,
    ):

        # Validation
        numeric_fields = {
            "Monthly Income": monthly_income,
            "Emergency Fund": emergency_fund,
            "Investments": total_investments,
            "Loans": total_loans,
            "Insurance": insurance_cover,
            "Monthly Budget": monthly_budget,
        }

        for field, value in numeric_fields.items():
            if value < 0:
                raise ValueError(f"{field} cannot be negative.")

        if monthly_budget > monthly_income:
            raise ValueError(
                "Monthly budget cannot exceed monthly income."
            )

        risk_appetite = risk_appetite.title()

        if risk_appetite not in ProfileService.VALID_RISK_LEVELS:
            raise ValueError("Invalid risk appetite.")

        investment_style = investment_style.title()

        if investment_style not in ProfileService.VALID_INVESTMENT_STYLES:
            raise ValueError("Invalid investment style.")

        preferred_currency = preferred_currency.upper()

        if preferred_currency not in ProfileService.VALID_CURRENCIES:
            raise ValueError("Unsupported currency.")

        update_profile(
            user_id=user_id,
            monthly_income=monthly_income,
            emergency_fund=emergency_fund,
            total_investments=total_investments,
            total_loans=total_loans,
            insurance_cover=insurance_cover,
            risk_appetite=risk_appetite,
            investment_style=investment_style,
            preferred_currency=preferred_currency,
            monthly_budget=monthly_budget,
        )

        return {
            "success": True,
            "message": "Financial profile updated successfully.",
        }