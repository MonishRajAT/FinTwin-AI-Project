from pathlib import Path

import joblib
import pandas as pd

from sklearn.cluster import KMeans
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
            "kmeans",
            KMeans(
                n_clusters=5,
                random_state=42,
                n_init=20,
            ),
        ),
    ]
)

pipeline.fit(X)

joblib.dump(
    pipeline,
    MODEL_DIR / "financial_persona_model.pkl",
)

df["cluster"] = pipeline.predict(X)

print("\nCluster Counts\n")
print(df["cluster"].value_counts().sort_index())

centers = pipeline.named_steps["kmeans"].cluster_centers_

centers = pipeline.named_steps["scaler"].inverse_transform(
    centers
)

summary = pd.DataFrame(
    centers,
    columns=features,
)

print("\nCluster Centers\n")
print(summary.round(2))

print("\nModel Saved Successfully.")