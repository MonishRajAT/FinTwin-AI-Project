# Financial health score prediction model.

from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

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

# Financial Health Score

df["financial_health_score"] = (
    0.30 * df["credit_score"] / 850
    + 0.25 * df["savings_to_income_ratio"]
    + 0.20 * (1 - df["debt_to_income_ratio"])
    + 0.15 * (
        df["monthly_income_usd"]
        / df["monthly_income_usd"].max()
    )
    + 0.10 * (
        1
        - df["monthly_emi_usd"]
        / (df["monthly_income_usd"] + 1)
    )
) * 100

df["financial_health_score"] = (
    df["financial_health_score"]
    .clip(0, 100)
)

target = "financial_health_score"

features = [
    "age",
    "gender",
    "education_level",
    "employment_status",
    "monthly_income_usd",
    "monthly_expenses_usd",
    "savings_usd",
    "loan_amount_usd",
    "monthly_emi_usd",
    "region",
]

X = df[features]
y = df[target]

categorical = [
    "gender",
    "education_level",
    "employment_status",
    "region",
]

numerical = [
    col for col in features
    if col not in categorical
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical,
        ),
        (
            "num",
            "passthrough",
            numerical,
        ),
    ]
)

model = Pipeline(
    [
        ("preprocessor", preprocessor),
        (
            "model",
            RandomForestRegressor(
                n_estimators=300,
                random_state=42,
            ),
        ),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print(f"MAE : {mean_absolute_error(y_test, pred):.2f}")
print(f"R²  : {r2_score(y_test, pred):.3f}")

joblib.dump(
    model,
    MODEL_DIR / "financial_health_model.pkl",
)

print("Model Saved Successfully.")