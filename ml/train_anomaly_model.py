# Financial Risk Detector model for FinTwin AI.

from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

BASE_DIR = Path(__file__).resolve().parent

DATASET = (
    BASE_DIR
    / "data"
    / "processed"
    / "financial_ml_dataset.csv"
)

MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATASET)

features = [
    "monthly_income_usd",
    "monthly_expenses_usd",
    "savings_usd",
    "loan_amount_usd",
    "monthly_emi_usd",
    "credit_score",
    "debt_to_income_ratio",
]

X = df[features]

pipeline = Pipeline(
    [
        ("scaler", StandardScaler()),
        (
            "model",
            IsolationForest(
                contamination=0.05,
                random_state=42,
            ),
        ),
    ]
)

pipeline.fit(X)

pred = pipeline.predict(X)

df["risk"] = pred

print("\nNormal Users: ", (pred == 1).sum())
print("High Risk Users: ", (pred == -1).sum())

joblib.dump(
    pipeline,
    MODEL_DIR / "financial_risk_model.pkl",
)

print("\nModel Saved Successfully.")