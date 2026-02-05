import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from analysis import (
    load_and_clean_data,
    calculate_kpis,
    sales_by_region,
    top_products,
    monthly_sales_trend
)

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# ==============================
# LOAD DATA (🔥 FIXED)
# ==============================
@st.cache_data
def load_data():
    df = load_and_clean_data("sales_data_sample.csv")
    return df

df = load_data()

# ==============================
# TITLE
# ==============================
st.title("📊 Sales Performance Dashboard")
st.markdown("Interactive Sales Analysis using **Python, Pandas & Streamlit**")

# ==============================
# KPIs
# ==============================
kpis = calculate_kpis(df)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("💰 Total Sales", f"{kpis['Total Sales']:,.2f}")
col2.metric("📦 Avg Sales", f"{kpis['Average Sales']:,.2f}")
col3.metric("⬆ Max Sale", kpis["Max Sale"])
col4.metric("⬇ Min Sale", kpis["Min Sale"])
col5.metric("🧾 Orders", kpis["Total Orders"])

st.divider()

# ==============================
# SALES BY REGION
# ==============================
st.subheader("🌍 Sales by Region")
region_sales = sales_by_region(df)

fig1, ax1 = plt.subplots()
region_sales.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Sales")
st.pyplot(fig1)

# ==============================
# TOP PRODUCTS
# ==============================
st.subheader("🏆 Top 5 Products")
top_prod = top_products(df)

fig2, ax2 = plt.subplots()
top_prod.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Sales")
st.pyplot(fig2)

# ==============================
# MONTHLY TREND
# ==============================
st.subheader("📅 Monthly Sales Trend")
monthly_sales = monthly_sales_trend(df)

fig3, ax3 = plt.subplots()
monthly_sales.plot(marker="o", ax=ax3)
ax3.set_ylabel("Sales")
st.pyplot(fig3)

# ==============================
# DATA PREVIEW
# ==============================
st.subheader("🔍 Data Preview")
st.dataframe(df.head(20))

