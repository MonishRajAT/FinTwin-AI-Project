"""
Calculates the Financial Health Score and
generates personalized financial insights.
"""

class FinancialHealthService:
    @staticmethod
    def calculate(profile: dict) -> dict:
        """
        Calculate financial health metrics.
        """

        income = float(profile["monthly_income"])
        emergency_fund = float(profile["emergency_fund"])
        investments = float(profile["total_investments"])
        loans = float(profile["total_loans"])
        budget = float(profile["monthly_budget"])

        # Metrics
        monthly_savings = max(income - budget, 0)

        savings_rate = (
            (monthly_savings / income) * 100
            if income > 0 else 0
        )

        investment_ratio = (
            (investments / income) * 100
            if income > 0 else 0
        )

        debt_ratio = (
            (loans / income) * 100
            if income > 0 else 0
        )

        emergency_months = (
            emergency_fund / budget
            if budget > 0 else 0
        )

        # Financial Health Score
        score = 0

        # Savings Rate (30)
        if savings_rate >= 30:
            score += 30
        elif savings_rate >= 20:
            score += 24
        elif savings_rate >= 10:
            score += 16
        else:
            score += 8

        # Emergency Fund (25)
        if emergency_months >= 6:
            score += 25
        elif emergency_months >= 3:
            score += 18
        elif emergency_months >= 1:
            score += 10

        # Investments (20)
        if investment_ratio >= 100:
            score += 20
        elif investment_ratio >= 50:
            score += 15
        elif investment_ratio >= 20:
            score += 10

        # Debt (25)
        if debt_ratio <= 20:
            score += 25
        elif debt_ratio <= 50:
            score += 18
        elif debt_ratio <= 80:
            score += 10

        score = min(score, 100)

        # Health Status
        if score >= 85:
            status = "Excellent"

        elif score >= 70:
            status = "Good"

        elif score >= 50:
            status = "Average"

        else:
            status = "Needs Attention"

        # Insights
        insights = []

        if savings_rate < 20:
            insights.append(
                "Increase your monthly savings."
            )

        if emergency_months < 3:
            insights.append(
                "Build an emergency fund covering at least 3 months of expenses."
            )

        if debt_ratio > 40:
            insights.append(
                "Reduce outstanding loans to improve financial stability."
            )

        if investment_ratio < 20:
            insights.append(
                "Increase investments for long-term wealth creation."
            )

        if not insights:
            insights.append(
                "Excellent financial discipline. Keep it up!"
            )

        return {

            "financial_health_score": score,

            "status": status,

            "monthly_savings": monthly_savings,

            "savings_rate": round(
                savings_rate,
                2
            ),

            "investment_ratio": round(
                investment_ratio,
                2
            ),

            "debt_ratio": round(
                debt_ratio,
                2
            ),

            "emergency_months": round(
                emergency_months,
                2
            ),

            "insights": insights
        }