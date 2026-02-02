import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, encoding="latin1")

    df.columns = df.columns.str.strip()
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df.dropna(subset=["Sales"], inplace=True)

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.dropna(subset=["Date"], inplace=True)

    return df


def calculate_kpis(df):
    return {
        "Total Sales": round(df["Sales"].sum(), 2),
        "Average Sales": round(df["Sales"].mean(), 2),
        "Max Sale": round(df["Sales"].max(), 2),
        "Min Sale": round(df["Sales"].min(), 2),
        "Total Orders": len(df)
    }


def sales_by_region(df):
    return df.groupby("Region")["Sales"].sum().sort_values(ascending=False)


def top_products(df, n=5):
    return (
        df.groupby("Product")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )


def monthly_sales_trend(df):
    df["Month"] = df["Date"].dt.to_period("M")
    return df.groupby("Month")["Sales"].sum()
