import pandas as pd

# Read the sales data file
data = pd.read_csv("sales_data.csv")

# Show the data
print("=== SALES DATA ===")
print(data)

# Total sales
print("\n=== TOTAL SALES ===")
print(data["Sales"].sum())

# Sales by product
print("\n=== SALES BY PRODUCT ===")
print(data.groupby("Product")["Sales"].sum())

# Sales by region
print("\n=== SALES BY REGION ===")
print(data.groupby("Region")["Sales"].sum())
print(data.groupby("Region")["Sales"].sum())