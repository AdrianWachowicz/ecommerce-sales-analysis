import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/Pakistan Largest Ecommerce Dataset.csv")

print(df.columns)

df["Revenue"] = df["price"] * df["qty_ordered"]

df.columns = df.columns.str.strip()

df["Date"] = pd.to_datetime(df["created_at"])
df["Month"] = df["Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Revenue"].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../outputs/figures/monthly_revenue_trend.png")
plt.show()

category_sales = df.groupby("category_name_1")["Revenue"].sum().sort_values(ascending=False).head(10)

plt.figure()
category_sales.plot(kind="bar")
plt.title("Top Categories by Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("../outputs/figures/top_categories_revenue.png")
plt.show()


payment = df["payment_method"].value_counts()

plt.figure()
payment.plot(kind="bar")
plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Orders")
plt.tight_layout()
plt.savefig("../outputs/figures/payment_methods.png")
plt.show()