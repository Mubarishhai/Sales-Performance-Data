from analysis import (
    load_and_clean_data,
    calculate_kpis,
    sales_by_region,
    top_products,
    monthly_sales_trend
)

# ==============================
# MAIN APPLICATION
# ==============================

def main():

    print("\n📊 SALES DATA ANALYSIS PROJECT\n")

    # Load data
    file_path = "data/sales_data.csv"
    df = load_and_clean_data(file_path)

    # ================= KPIs =================
    print("===== KEY PERFORMANCE INDICATORS =====")
    kpis = calculate_kpis(df)

    for key, value in kpis.items():
        print(f"{key}: {value}")

    # ================= REGION SALES =================
    print("\n===== SALES BY REGION =====")
    print(sales_by_region(df))

    # ================= TOP PRODUCTS =================
    print("\n===== TOP 5 PRODUCT LINES =====")
    print(top_products(df))

    # ================= MONTHLY TREND =================
    print("\n===== MONTHLY SALES TREND =====")
    print(monthly_sales_trend(df))


if __name__ == "__main__":
    main()
