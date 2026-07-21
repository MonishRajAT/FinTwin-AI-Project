# Central analytics engine for FinTwin AI.

import pandas as pd
from repositories.analytics_repository import (
    get_transactions,
)

class AnalyticsService:

    @staticmethod
    def get_dashboard_analytics(user_id: int):

        transactions = get_transactions(user_id)

        if not transactions:

            return {
                "df": pd.DataFrame(),
                "total_income": 0,
                "total_expense": 0,
                "cash_flow": 0,
                "expense_by_category": pd.DataFrame(),
                "income_by_category": pd.DataFrame(),
                "top_merchants": pd.DataFrame(),
                "monthly_summary": pd.DataFrame(),
            }
        
        df = pd.DataFrame(transactions)

        # Income

        income_df = df[
            df["transaction_type"] == "Income"
        ]

        total_income = income_df["amount"].sum()

        # Expense

        expense_df = df[
            df["transaction_type"] == "Expense"
        ]

        total_expense = expense_df["amount"].sum()

        # Cash Flow

        cash_flow = total_income - total_expense

        # Expense by Category

        expense_by_category = (

            expense_df
            .groupby("category")["amount"]
            .sum()
            .reset_index()
            .sort_values(
                "amount",
                ascending=False
            )

        )

        # Income by Category

        income_by_category = (

            income_df
            .groupby("category")["amount"]
            .sum()
            .reset_index()

        )

        # Top Merchants

        top_merchants = (

            expense_df
            .groupby("merchant")["amount"]
            .sum()
            .reset_index()
            .sort_values(
                "amount",
                ascending=False
            )
            .head(10)

        )

        # Monthly summary

        df["transaction_date"] = pd.to_datetime(
            df["transaction_date"]
        )

        df["month"] = df[
            "transaction_date"
        ].dt.strftime("%b %Y")

        monthly_summary = (

            df.groupby(
                [
                    "month",
                    "transaction_type",
                ]
            )["amount"]
            .sum()
            .reset_index()

        )

        # Financial KPI's

        savings = total_income - total_expense

        savings_rate = (
            (savings / total_income) * 100
            if total_income > 0
            else 0
        )

        debt_to_income = (
            (expense_df["amount"].sum() / total_income) * 100
            if total_income > 0
            else 0
        )

        profile = None

        try:
            from repositories.profile_repository import get_profile

            profile = get_profile(user_id)

        except Exception:
            pass

        emergency_fund = 0
        investments = 0
        loans = 0
        monthly_budget = 0

        if profile:

            emergency_fund = profile.get(
                "emergency_fund",
                0,
            )

            investments = profile.get(
                "total_investments",
                0,
            )

            loans = profile.get(
                "total_loans",
                0,
            )

            monthly_budget = profile.get(
                "monthly_budget",
                0,
            )

        net_worth = (
            emergency_fund
            + investments
            - loans
        )

        budget_utilization = (
            (total_expense / monthly_budget) * 100
            if monthly_budget > 0
            else 0
        )

        return {
            "df": df,

            "total_income": total_income,

            "total_expense": total_expense,

            "cash_flow": cash_flow,

            "expense_by_category": expense_by_category,

            "income_by_category": income_by_category,

            "top_merchants": top_merchants,

            "monthly_summary": monthly_summary,

            "savings": savings,

            "savings_rate": savings_rate,

            "debt_to_income": debt_to_income,

            "net_worth": net_worth,

            "budget_utilization": budget_utilization,
        }
    
    @staticmethod
    def get_financial_health_report(user_id: int):

        analytics = AnalyticsService.get_dashboard_analytics(
            user_id
        )

        report = []

        # Savings Rate
        if analytics["savings_rate"] >= 30:
            report.append({
                "type": "success",
                "title": "Excellent Savings Rate",
                "message": "You are saving more than 30% of your income."
            })

        elif analytics["savings_rate"] >= 20:
            report.append({
                "type": "info",
                "title": "Healthy Savings",
                "message": "Your savings rate is healthy. Keep it consistent."
            })

        else:
            report.append({
                "type": "warning",
                "title": "Low Savings",
                "message": "Try increasing your monthly savings."
            })

        # Budget
        if analytics["budget_utilization"] > 100:

            report.append({

                "type": "error",

                "title": "Budget Exceeded",

                "message": "Your expenses exceeded your monthly budget."

            })

        elif analytics["budget_utilization"] > 80:

            report.append({

                "type": "warning",

                "title": "Budget Alert",

                "message": "You are approaching your monthly budget."

            })

        else:

            report.append({

                "type": "success",

                "title": "Budget Healthy",

                "message": "You are within your planned budget."

            })

        # Net Worth

        if analytics["net_worth"] > 0:

            report.append({

                "type": "success",

                "title": "Positive Net Worth",

                "message": "Your assets exceed your liabilities."

            })

        else:

            report.append({

                "type": "warning",

                "title": "Negative Net Worth",

                "message": "Focus on reducing liabilities."

            })

        return report