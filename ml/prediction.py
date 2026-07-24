# Integration of all the 3 models of FinTwin AI.

from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

MODEL_DIR = BASE_DIR / "models"

health_model = joblib.load(
    MODEL_DIR / "financial_health_model.pkl"
)

persona_model = joblib.load(
    MODEL_DIR / "financial_persona_model.pkl"
)

risk_model = joblib.load(
    MODEL_DIR / "financial_risk_model.pkl"
)


PERSONA_MAP = {
    0: "Balanced",
    1: "Saver",
    2: "Investor",
    3: "Debt Heavy",
    4: "High Spender",
}
