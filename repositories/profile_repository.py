# Repository for Financial Digital FinTwin operations.

from database.db import execute_query, fetch_one

def create_profile(user_id: int):
    """
    Create an empty financial profile for a new user.
    """
    query = """
    INSERT INTO financial_profiles (user_id)
    VALUES (%s)
    ON CONFLICT (user_id) DO NOTHING;
    """
    execute_query(query, (user_id,))
    return True

def get_profile(user_id: int):
    """
    Fetch a user's financial profile.
    """
    query = """
    SELECT *
    FROM financial_profiles
    WHERE user_id = %s;
    """
    return fetch_one(query, (user_id,))


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
    monthly_budget: float
):
    """
    Update a user's Financial Digital Twin.
    """

    query = """
    UPDATE financial_profiles
    SET
        monthly_income = %s,
        emergency_fund = %s,
        total_investments = %s,
        total_loans = %s,
        insurance_cover = %s,
        risk_appetite = %s,
        investment_style = %s,
        preferred_currency = %s,
        monthly_budget = %s,
        updated_at = CURRENT_TIMESTAMP
    WHERE user_id = %s;
    """

    execute_query(
        query,
        (
            monthly_income,
            emergency_fund,
            total_investments,
            total_loans,
            insurance_cover,
            risk_appetite,
            investment_style,
            preferred_currency,
            monthly_budget,
            user_id
        )
    )
    return True