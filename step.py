# step.py

from analysis import (
    load_and_clean_data,
    calculate_kpis,
    sales_by_region,
    top_products,
    monthly_sales_trend
)

# =====================================
# STEP BY STEP SALES ANALYSIS
# =====================================

def run_steps():

    print("\n==============================")
    print(" STEP 1: Loading Dataset")
    print("==============================")

    file_path = "data/sales_data.csv"
    df = load_and_clean_data(file_path)

    print("Dataset Loaded Successfully ✅")
    print("Shape of data:", df.shape)
    print(df.head())


    # ---------------------------------
    print("\n==============================")
    print(" STEP 2: Calculating KPIs")
    print("==============================")

    kpis = calculate_kpis(df)

    for key, value in kpis.items():
        print(f"{key}: {value}")


    # ---------------------------------
    print("\n==============================")
    print(" STEP 3: Sales by Region")
    print("==============================")

    region_sales = sales_by_region(df)
    print(region_sales)


    # ---------------------------------
    print("\n==============================")
    print(" STEP 4: Top Products")
    print("==============================")

    top_prod = top_products(df)
    print(top_prod)


    # ---------------------------------
    print("\n==============================")
    print(" STEP 5: Monthly Sales Trend")
    print("==============================")

    monthly_trend = monthly_sales_trend(df)
    print(monthly_trend)

    print("\n✅ Analysis Completed Successfully!")


# Run program
if __name__ == "__main__":
    run_steps()
