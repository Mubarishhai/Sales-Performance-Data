import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ==============================
# LOAD DATA (Automatic Path)
# ==============================
base_path = os.path.dirname(__file__)  # Folder where script exists
file_path = os.path.join(base_path, "sales_data.csv")

print("Looking for file at:", file_path)
print("Files available in folder:", os.listdir(base_path))

df = pd.read_csv(file_path)

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
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)

# ==============================
# SALES BY PRODUCT
# ==============================
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
print("\nSales by Product:")
print(product_sales)

# ==============================
# VISUALIZATION - REGION SALES
# ==============================
plt.figure()
region_sales.plot(kind='bar')
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ==============================
# VISUALIZATION - PRODUCT SALES
# ==============================
plt.figure()
product_sales.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# ==============================
# MONTHLY SALES TREND
# ==============================
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
