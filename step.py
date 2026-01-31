import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============================
# LOAD DATA
# ==============================
try:
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "sales_data_sample.csv")

    print("Looking for file at:", file_path)
    print("Files available in folder:", os.listdir(base_path))

    df = pd.read_csv(file_path, encoding='latin1')
    print("✅ File loaded successfully!\n")

except FileNotFoundError:
    print("❌ CSV file not found. Check file name and path.")
    exit()

# Clean column names
df.columns = df.columns.str.strip()

# ==============================
# BASIC DATA OVERVIEW
# ==============================
print("First 5 Rows:\n", df.head(), "\n")
print("Dataset Info:\n")
df.info()
print("\nMissing Values:\n", df.isnull().sum())

# ==============================
# DATA CLEANING
# ==============================
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

print("\nAfter Cleaning Shape:", df.shape)
print("\nDescriptive Statistics:\n", df.describe())

# ==============================
# SALES BY REGION
# ==============================
if {"Region", "Sales"}.issubset(df.columns):
    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

    print("\nSales by Region:\n", region_sales)

    plt.figure()
    region_sales.plot(kind='bar')
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()
else:
    print("⚠ 'Region' or 'Sales' column not found.")

# ==============================
# SALES BY PRODUCT
# ==============================
if {"Product", "Sales"}.issubset(df.columns):
    product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

    print("\nSales by Product:\n", product_sales)

    plt.figure()
    product_sales.plot(kind='bar')
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()
else:
    print("⚠ 'Product' or 'Sales' column not found.")

# ==============================
# MONTHLY SALES TREND
# ==============================
if {"Date", "Sales"}.issubset(df.columns):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.dropna(subset=["Date"], inplace=True)

    df["Month"] = df["Date"].dt.month
    monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()

    print("\nMonthly Sales:\n", monthly_sales)

    plt.figure()
    plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(range(1, 13))
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("⚠ 'Date' or 'Sales' column not found.")
