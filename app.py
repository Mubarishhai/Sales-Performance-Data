

# ==============================
# TITLE
# ==============================
st.title("📊 Sales Performance Dashboard")
st.markdown("Interactive Sales Analysis using **Python & Streamlit**")

# ==============================
# KPIs
# ==============================
total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()
total_orders = len(df)

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"{total_sales:,.2f}")
col2.metric("📦 Avg Order Value", f"{avg_sales:,.2f}")
col3.metric("🧾 Total Orders", total_orders)

st.divider()

# ==============================
# SALES BY REGION
# ==============================
st.subheader("🌍 Sales by Region")
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

fig1, ax1 = plt.subplots()
region_sales.plot(kind="bar", ax=ax1)
ax1.set_ylabel("Sales")
st.pyplot(fig1)

# ==============================
# TOP PRODUCTS
# ==============================
st.subheader("🏆 Top 5 Products")
top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

fig2, ax2 = plt.subplots()
top_products.plot(kind="bar", ax=ax2)
ax2.set_ylabel("Sales")
st.pyplot(fig2)

# ==============================
# MONTHLY TREND
# ==============================
st.subheader("📅 Monthly Sales Trend")
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()

fig3, ax3 = plt.subplots()
monthly_sales.plot(marker="o", ax=ax3)
ax3.set_ylabel("Sales")
st.pyplot(fig3)

# ==============================
# DATA PREVIEW
# ==============================
st.subheader("🔍 Raw Data Preview")
st.dataframe(df.head(20))
