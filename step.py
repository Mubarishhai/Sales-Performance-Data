import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============================
# LOAD DATA
# ==============================
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "sales_data_sample.csv")

print("Looking for file at:", file_path)
print("Files available in folder:", os.listdir(base_path))

df = pd.read_csv(file_path, encoding='latin1')


# Standardize column names (removes hidden spaces)
df.columns = df.columns.str.strip()

# ==============================
# BASIC DATA OVERVIEW
# ==============================
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# ==============================
# DATA CLEANING
# ==============================
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

print("\nAfter Cleaning Shape:", df.shape)

print("\nDescriptive Statistics:")
print(df.describe())

# ==============================
# SALES BY REGION
# ==============================
if "Region" in df.columns and "Sales" in df.columns:
    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    print("\nSales by Region:")
    print(region_sales)

    plt.figure()
    region_sales.plot(kind='bar')
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()
else:
    print("⚠ Column 'Region' or 'Sales' not found in dataset")

# ==============================
# SALES BY PRODUCT
# ==============================
if "Product" in df.columns and "Sales" in df.columns:
    product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
    print("\nSales by Product:")
    print(product_sales)

    plt.figure()
    product_sales.plot(kind='bar')
    plt.title("Total Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.tight_layout()
    plt.show()
else:
    print("⚠ Column 'Product' or 'Sales' not found in dataset")

# ==============================
# MONTHLY SALES TREND
# ==============================
if "Date" in df.columns and "Sales" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df.dropna(subset=["Date"], inplace=True)

    df["Month"] = df["Date"].dt.month
    monthly_sales = df.groupby("Month")["Sales"].sum().sort_index()

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
    print("⚠ Column 'Date' or 'Sales' not found in dataset")
