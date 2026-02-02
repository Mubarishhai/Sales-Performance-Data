import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================
# CONFIG
# ==============================
plt.rcParams["figure.figsize"] = (8, 5)

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = "sales_data_sample.csv"
OUTPUT_DIR = os.path.join(BASE_PATH, "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


# ==============================
# LOAD DATA
# ==============================
def load_data():
    try:
        file_path = os.path.join(BASE_PATH, DATA_FILE)
        print(f"📂 Loading data from: {file_path}")
        df = pd.read_csv(file_path, encoding="latin1")
        print("✅ Data loaded successfully\n")
        return df
    except FileNotFoundError:
        print("❌ File not found. Please check file name or path.")
        exit()


# ==============================
# DATA CLEANING
# ==============================
def clean_data(df):
    df.columns = df.columns.str.strip()
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    if "Sales" in df.columns:
        df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
        df.dropna(subset=["Sales"], inplace=True)

    print("🧹 Data cleaning completed")
    print("Final Shape:", df.shape, "\n")
    return df


# ==============================
# KPI METRICS
# ==============================
def calculate_kpis(df):
    metrics = {
        "Total Sales": round(df["Sales"].sum(), 2),
        "Average Sales per Order": round(df["Sales"].mean(), 2),
        "Max Order Value": round(df["Sales"].max(), 2),
        "Min Order Value": round(df["Sales"].min(), 2),
        "Total Orders": len(df)
    }

    print("📌 KEY BUSINESS METRICS")
    for k, v in metrics.items():
        print(f"{k}: {v}")
    print()
    return metrics


# ==============================
# SALES BY REGION
# ==============================
def sales_by_region(df):
    if {"Region", "Sales"}.issubset(df.columns):
        region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

        region_sales.plot(kind="bar", title="Total Sales by Region")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, "sales_by_region.png"))
        plt.close()

        print("🌍 Sales by Region analysis completed")


# ==============================
# TOP PRODUCTS
# ==============================
def top_products(df, n=5):
    if {"Product", "Sales"}.issubset(df.columns):
        top_prod = (
            df.groupby("Product")["Sales"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

        top_prod.plot(kind="bar", title=f"Top {n} Products by Sales")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, "top_products.png"))
        plt.close()

        print(f"🏆 Top {n} products analysis completed")


# ==============================
# TIME SERIES ANALYSIS
# ==============================
def monthly_trend(df):
    if {"Date", "Sales"}.issubset(df.columns):
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.dropna(subset=["Date"], inplace=True)

        df["YearMonth"] = df["Date"].dt.to_period("M")
        monthly_sales = df.groupby("YearMonth")["Sales"].sum()

        best_month = monthly_sales.idxmax()

        print(f"📅 Best Sales Month: {best_month}")
        print(f"💰 Sales in Best Month: {monthly_sales.max()}\n")

        monthly_sales.plot(marker="o", title="Monthly Sales Trend")
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_DIR, "monthly_sales_trend.png"))
        plt.close()

        print("📈 Monthly sales trend analysis completed")


# ==============================
# EXPORT REPORT
# ==============================
def export_summary(metrics):
    summary_df = pd.DataFrame([metrics])
    output_file = os.path.join(OUTPUT_DIR, "sales_summary_report.xlsx")
    summary_df.to_excel(output_file, index=False)
    print(f"📁 Summary report saved at: {output_file}")


# ==============================
# MAIN EXECUTION
# ==============================
def main():
    df = load_data()
    df = clean_data(df)

    metrics = calculate_kpis(df)
    sales_by_region(df)
    top_products(df)
    monthly_trend(df)
    export_summary(metrics)

    print("\n✅ Sales Data Analysis Project Completed Successfully")


if __name__ == "__main__":
    main()

