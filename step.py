import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, encoding="latin1")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Remove duplicates and null rows
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Convert sales column to numeric
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    df.dropna(subset=["sales"], inplace=True)

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df.dropna(subset=["date"], inplace=True)

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
    return df.groupby("region")["sales"].sum().sort_values(ascending=False)


def top_products(df, n=5):
    return (
        df.groupby("product")["sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def monthly_sales_trend(df):
    df["month"] = df["date"].dt.to_period("M")
    return df.groupby("month")["sales"].sum()


