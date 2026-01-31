import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================
# LOAD DATA
# ==============================
try:
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "sales_data_sample.csv")

    print("Looking for file at:", file_path)
    df = pd.read_csv(file_path, encoding="latin1")
    print("✅ File loaded successfully!\n")

except FileNotFoundError:
    print("❌ CSV file not found. Check file name and path.")
    exit()

# Clean column names
df.columns = df.columns.str.strip()

# ==============================
# BASIC OVERVIEW
# ==============================
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing Values:\n", df.isnull().sum())

# ==============================
# DATA CLEANING
# ==============================
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Ensure Sales is numeric
if "Sales" in df.columns:
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df.dropna(subset=["Sales"], inplace=True)

print("\nAfter Cleaning Shape:", df.shape)

# ==============================
# 🔑 KEY PERFORMANCE INDICATORS
# ==============================
total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()
total_orders = len(df)

print("\n📌 KEY METRICS")
print("Total Sales:", round(total_sales, 2))
print("Average Sales per Order:", round(avg_sales, 2))
print("Total Orders:", total_orders)

# ==============================
# SALES BY REGION
# ==============================
if {"Region", "Sales"}.issubset(df.columns):
    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    print("\n🌍 Sales by Region:\n", region_sales)

    region_sales.plot(kind="bar", title="Total Sales by Region")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

# ==============================
# TOP 5 PRODUCTS
# ==============================
if {"Product", "Sales"}.issubset(df.columns):
    product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
    top_products = product_sales.head(5)

    print("\n🏆 Top 5 Products by Sales:\n", top_products)

    top_products.plot(kind="bar", title="Top 5 Products")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

# ==============================
# MONTHLY SALES TREND
# ==============================
if {"Date", "Sales"}.issubset(df.columns):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.dropna(subset=["Date"], inplace=True)

    df["Month"] = df["Date"].dt.month
    monthly_sales = df.groupby("Month")["Sales"].sum()

    best_month = monthly_sales.idxmax()
    print("\n📅 Best Sales Month:", best_month)
    print("Sales in Best Month:", monthly_sales.max())

    monthly_sales.plot(marker="o", title="Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ==============================
# EXPORT SUMMARY REPORT
# ==============================
summary = {
    "Total Sales": [total_sales],
    "Average Sales": [avg_sales],
    "Total Orders": [total_orders]
}

summary_df = pd.DataFrame(summary)
output_path = os.path.join(base_path, "sales_summary_report.xlsx")
summary_df.to_excel(output_path, index=False)

print(f"\n📁 Summary report exported to: {output_path}")
