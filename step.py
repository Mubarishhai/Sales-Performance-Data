import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, encoding="latin1")
    df.columns = df.columns.str.strip().str.lower()

    required_cols = ["sales", "orderdate", "territory", "productline"]
    missing = [c for c in required_cols if c not in df.columns]

    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")

    df.drop_duplicates(inplace=True)

    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    df["orderdate"] = pd.to_datetime(df["orderdate"], errors="coerce")

    df.dropna(subset=["sales", "orderdate"], inplace=True)
    return df


def calculate_kpis(df):
    return {
        "Total Sales": round(df["sales"].sum(), 2),
        "Average Sales": round(df["sales"].mean(), 2),
        "Max Sale": round(df["sales"].max(), 2),
        "Min Sale": round(df["sales"].min(), 2),
        "Total Orders": len(df)
    }



def sales_by_region(df):
    # 🔥 region equivalent = territory
    return (
        df.groupby("territory")["sales"]
        .sum()
        .sort_values(ascending=False)
    )


def top_products(df, n=5):
    return (
        df.groupby("productline")["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def monthly_sales_trend(df):
    df["month"] = df["orderdate"].dt.to_period("M")
    return df.groupby("month")["sales"].sum()
