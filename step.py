import pandas as pd

# ==============================
# LOAD & CLEAN DATA
# ==============================
def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    # Standardize column names (safe practice)
    df.columns = df.columns.str.strip()

    # Convert ORDERDATE to datetime
    if "ORDERDATE" in df.columns:
        df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

    # Remove rows with missing SALES
    df = df.dropna(subset=["SALES"])

    return df


# ==============================
# KPI CALCULATIONS
# ==============================
def calculate_kpis(df):
    return {
        "Total Sales": df["SALES"].sum(),
        "Average Sales": df["SALES"].mean(),
        "Max Sale": df["SALES"].max(),
        "Min Sale": df["SALES"].min(),
        "Total Orders": df["ORDERNUMBER"].nunique()
    }


# ==============================
# SALES BY REGION
# ==============================
def sales_by_region(df):
    return (
        df.groupby("TERRITORY")["SALES"]
        .sum()
        .sort_values(ascending=False)
    )


# ==============================
# TOP PRODUCTS
# ==============================
def top_products(df, n=5):
    return (
        df.groupby("PRODUCTLINE")["SALES"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


# ==============================
# MONTHLY SALES TREND
# ==============================
def monthly_sales_trend(df):
    df["Month"] = df["ORDERDATE"].dt.to_period("M")

    return (
        df.groupby("Month")["SALES"]
        .sum()
        .sort_index()
    )
