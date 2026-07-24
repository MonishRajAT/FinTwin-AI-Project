# Feature Engineering Pipeline.

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent

RAW_DATA = BASE_DIR / "data" / "raw"
PROCESSED_DATA = BASE_DIR / "data" / "processed"

PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

def load_dataset():

    df = pd.read_csv(
        RAW_DATA / "synthetic_personal_finance_dataset.csv"
    )

    return df


def preprocess(df):

    df = df.copy()

    # Date Features

    df["record_date"] = pd.to_datetime(df["record_date"])

    df["year"] = df["record_date"].dt.year
    df["month"] = df["record_date"].dt.month
    df["quarter"] = df["record_date"].dt.quarter

    # Derived Features

    df["net_monthly_cashflow"] = (
        df["monthly_income_usd"]
        -
        df["monthly_expenses_usd"]
    )

    df["loan_to_income_ratio"] = (
        df["loan_amount_usd"]
        /
        (df["monthly_income_usd"] + 1)
    )

    df["emi_to_income_ratio"] = (
        df["monthly_emi_usd"]
        /
        (df["monthly_income_usd"] + 1)
    )

    # Missing Values

    df.fillna(
        {
            "loan_type": "No Loan",
            "job_title": "Unknown",
        },
        inplace=True,
    )

    return df


def save_dataset(df):

    df.to_csv(

        PROCESSED_DATA /

        "financial_ml_dataset.csv",

        index=False,

    )


def main():

    df = load_dataset()

    df = preprocess(df)

    save_dataset(df)

    print("=" * 60)

    print("Feature Engineering Completed Successfully")

    print("=" * 60)

    print()

    print(df.shape)

    print()

    print(df.head())


if __name__ == "__main__":

    main()