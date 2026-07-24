from ml.prediction import (
    health_model,
    persona_model,
    risk_model,
    PERSONA_MAP,
)

import pandas as pd


class MLService:

    @staticmethod
    def generate_prediction(profile):

        # Health Model

        health_df = pd.DataFrame([{
            "age": 25,
            "gender": "Male",
            "education_level": "Bachelor",
            "employment_status": "Employed",
            "monthly_income_usd": profile["monthly_income"],
            "monthly_expenses_usd": profile["monthly_budget"],
            "savings_usd": profile["emergency_fund"],
            "loan_amount_usd": profile["total_loans"],
            "monthly_emi_usd": (
                profile["total_loans"] / 24
                if profile["total_loans"] > 0
                else 0
            ),
            "region": "Urban",
        }])

        health_score = round(
            health_model.predict(
                health_df
            )[0],
            2,
        )

        # Persona & Risk

        debt_ratio = (
            profile["total_loans"]
            /
            (profile["monthly_income"] + 1)
        )

        persona_df = pd.DataFrame([{
            "monthly_income_usd": profile["monthly_income"],
            "monthly_expenses_usd": profile["monthly_budget"],
            "savings_usd": profile["emergency_fund"],
            "loan_amount_usd": profile["total_loans"],
            "monthly_emi_usd": (
                profile["total_loans"] / 24
                if profile["total_loans"] > 0
                else 0
            ),
            "credit_score": 700,
            "debt_to_income_ratio": debt_ratio,
        }])

        cluster = persona_model.predict(
            persona_df
        )[0]

        persona = PERSONA_MAP.get(
            cluster,
            "Balanced",
        )

        risk = risk_model.predict(
            persona_df
        )[0]

        risk = (
            "High Risk"
            if risk == -1
            else "Normal"
        )

        return {
            "health_score": health_score,
            "persona": persona,
            "risk": risk,
        }