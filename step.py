import pandas as pd
from typing import Dict


def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """
    Load sales data from CSV, clean it, and prepare it for analysis.

    Steps performed:
    - Normalize column names
    - Validate required columns
    - Remove duplicates
    - Convert sales to numeric
    - Convert orderdate to datetime
    - Drop invalid rows

    Returns:
        Cleaned Pandas DataFrame
    """
    df = pd.read_csv(file_path, encoding="latin1")

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # Required columns check
    required_cols = ["sales", "orderdate", "territory", "productline"]
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")

    # Remove duplicates
    df = df.drop_duplicates().copy()

    # Data type conversions
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")

    # Remove invalid rows
    df = df.dropna(subset=["sales", "orderdate"])

    return df


def calculate_kpis(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate key business KPIs from sales data.
    """
    return {
        "Total Sales": round(df["sales"].sum(), 2),
        "Average Sales": round(df["sales"].mean(), 2),
        "Max Sale": round(df["sales"].max(), 2),
        "Min Sale": round(df["sales"].min(), 2),
        "Total Orders": int(len(df))
    }


def sales_by_region(df: pd.DataFrame) -> pd.Series:
    """
    Aggregate total sales by business region (territory).
    """
    return (
        df.groupby("territory", as_index=True)["sales"]
        .sum()
        .sort_values(ascending=False)
    )


def top_products(df: pd.DataFrame, n: int = 5) -> pd.Series:
    """
    Return top N product lines by total sales.
    """
    return (
        df.groupby("productline", as_index=True)["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def monthly_sales_trend(df: pd.DataFrame) -> pd.Series:
    """
    Generate monthly sales trend using order date.
    """
    temp_df = df.copy()
    temp_df["month"] = temp_df["orderdate"].dt.to_period("M")

    return (
        temp_df.groupby("month", as_index=True)["sales"]
        .sum()
    )
