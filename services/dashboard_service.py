"""
Dashboard service responsible for generating
all dashboard metrics from the Financial Digital Twin.
"""

from repositories.profile_repository import get_profile
from repositories.dashboard_repository import (
    save_dashboard_metrics,
    get_dashboard_metrics,
)
from services.financial_health_service import (
    FinancialHealthService,
)

class DashboardService:
    @staticmethod
    def refresh_dashboard(user_id: int):
        """
        Calculate dashboard metrics
        and persist them.
        """
        profile = get_profile(user_id)

        if profile is None:
            raise ValueError(
                "Financial profile not found."
            )

        health = FinancialHealthService.calculate(profile)
        save_dashboard_metrics(

            user_id=user_id,

            financial_health_score=health[
                "financial_health_score"
            ],

            monthly_cash_flow=health[
                "monthly_savings"
            ],

            savings_rate=health[
                "savings_rate"
            ],

            debt_ratio=health[
                "debt_ratio"
            ],

            investment_ratio=health[
                "investment_ratio"
            ],
        )

        return {
            "profile": profile,
            "health": health,
        }

    @staticmethod
    def get_dashboard(user_id: int):
        """
        Return dashboard data.
        """
        metrics = get_dashboard_metrics(user_id)

        if metrics is None:

            return DashboardService.refresh_dashboard(
                user_id
            )

        profile = get_profile(user_id)

        health = FinancialHealthService.calculate(
            profile
        )

        return {
            "profile": profile,
            "metrics": metrics,
            "health": health,
        }