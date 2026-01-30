import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("sales_data.csv")

# Display first rows
print(df.head())

# Data Info
print(df.info())

# Check missing values
print(df.isnull().sum())

# Remove missing values
df.dropna(inplace=True)

# Remove duplicate records
df.drop_duplicates(inplace=True)

# Descriptive statistics
print(df.describe())

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

# Sales by Product
product_sales = df.groupby("Product")["Sales"].sum()
print(product_sales)

# Visualization - Sales by Region
plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# Visualization - Sales by Product
plt.figure()
product_sales.plot(kind='bar')
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# Monthly Sales Trend
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure()
plt.plot(monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()