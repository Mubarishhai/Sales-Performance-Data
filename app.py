import streamlit as st
from analysis import (
    load_and_clean_data,
    calculate_kpis,
    sales_by_region,
    top_products,
    monthly_sales_trend
)

# ==============================
# PAGE TITLE
# ==============================
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Data Analysis Dashboard")

# ==============================
# LOAD DATA
# ==============================
# LOAD DATA
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "data", "sales_data_sample.csv")

df = load_and_clean_data(file_path)


# ==============================
# KPIs
# ==============================
kpis = calculate_kpis(df)

st.subheader("📌 Key Performance Indicators")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total Sales", f"{kpis['Total Sales']:.0f}")
col2.metric("Average Sales", f"{kpis['Average Sales']:.0f}")
col3.metric("Max Sale", f"{kpis['Max Sale']:.0f}")
col4.metric("Min Sale", f"{kpis['Min Sale']:.0f}")
col5.metric("Total Orders", kpis["Total Orders"])

# ==============================
# SALES BY REGION
# ==============================
st.subheader("🌍 Sales by Region")
region_sales = sales_by_region(df)
st.bar_chart(region_sales)

# ==============================
# TOP PRODUCTS
# ==============================
st.subheader("🏆 Top Product Lines")
top_prod = top_products(df)
st.bar_chart(top_prod)

# ==============================
# MONTHLY TREND
# ==============================
st.subheader("📈 Monthly Sales Trend")
monthly_trend = monthly_sales_trend(df)
st.line_chart(monthly_trend)

# ==============================
# RAW DATA
# ==============================
st.subheader("📄 Raw Data Preview")
st.dataframe(df.head(20))
