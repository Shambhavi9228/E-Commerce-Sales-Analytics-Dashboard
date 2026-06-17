import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("../data/cleaned_superstore.csv")

# Convert Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# -------------------------
# Monthly Sales Trend
# -------------------------
monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("../results/monthly_sales_trend.png")
plt.close()

# -------------------------
# Top 10 Products
# -------------------------
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("../results/top_products.png")
plt.close()

# -------------------------
# Sales by Category
# -------------------------
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7,5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("../results/sales_by_category.png")
plt.close()

print("Sales analysis graphs generated successfully!")