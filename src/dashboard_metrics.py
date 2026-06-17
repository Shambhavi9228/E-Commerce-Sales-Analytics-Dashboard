import pandas as pd

# Load cleaned dataset
df = pd.read_csv("../data/cleaned_superstore.csv")

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

print("===== DASHBOARD KPIs =====")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")

# Save KPI report
with open("../results/kpi_report.txt", "w") as f:
    f.write("E-Commerce Sales Analytics Dashboard KPIs\n")
    f.write("----------------------------------------\n")
    f.write(f"Total Sales: ${total_sales:,.2f}\n")
    f.write(f"Total Profit: ${total_profit:,.2f}\n")
    f.write(f"Total Orders: {total_orders}\n")
    f.write(f"Total Customers: {total_customers}\n")

print("\nKPI report saved successfully!")