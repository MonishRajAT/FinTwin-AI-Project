# Repository for dashboard metrics.

from database.db import execute_query, fetch_one

def save_dashboard_metrics(
    user_id: int,
    financial_health_score: float,
    monthly_cash_flow: float,
    savings_rate: float,
    debt_ratio: float,
    investment_ratio: float,
):
    """
    Insert or update dashboard metrics.
    """

    query = """
    INSERT INTO dashboard_metrics (
        user_id,
        financial_health_score,
        monthly_cash_flow,
        savings_rate,
        debt_ratio,
        investment_ratio
    )

    VALUES (
        %s,%s,%s,%s,%s,%s
    )

    ON CONFLICT (user_id)

    DO UPDATE SET

        financial_health_score = EXCLUDED.financial_health_score,

        monthly_cash_flow = EXCLUDED.monthly_cash_flow,

        savings_rate = EXCLUDED.savings_rate,

        debt_ratio = EXCLUDED.debt_ratio,

        investment_ratio = EXCLUDED.investment_ratio,

        updated_at = CURRENT_TIMESTAMP;
    """

    execute_query(
        query,
        (
            user_id,
            financial_health_score,
            monthly_cash_flow,
            savings_rate,
            debt_ratio,
            investment_ratio,
        ),
    )

def get_dashboard_metrics(user_id: int):
    """
    Fetch dashboard metrics.
    """

    query = """
    SELECT *

    FROM dashboard_metrics

    WHERE user_id = %s;
    """

    return fetch_one(query, (user_id,))