import pandas as pd

# ==============================
# LOAD & CLEAN DATA
# ==============================
def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, encoding="latin1")

    # Clean column names
    df.columns = df.columns.str.strip().str.upper()

    # Convert date column
    if "ORDERDATE" in df.columns:
        df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"], errors="coerce")

    # Drop missing sales
    df = df.dropna(subset=["SALES"])

    return df


# ==============================
# KPI CALCULATIONS
# ==============================
def calculate_kpis(df):
    kpis = {
        "Total Sales": round(df["SALES"].sum(), 2),
        "Average Sales": round(df["SALES"].mean(), 2),
        "Max Sale": round(df["SALES"].max(), 2),
        "Min Sale": round(df["SALES"].min(), 2),
        "Total Orders": df["ORDERNUMBER"].nunique()
    }
    return kpis


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
