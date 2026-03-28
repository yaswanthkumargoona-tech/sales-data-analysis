import pandas as pd

# -------------------------------
# Step 1: Create Dataset
# -------------------------------
data = {
    "product": ["Laptop", "Shirt", "Mobile", "Shoes", "Tablet", "T-shirt"],
    "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics", "Clothing"],
    "price": [50000, 1000, 20000, 3000, 15000, 800],
    "quantity": [5, 10, 3, 7, 4, 12],
    "city": ["Hyderabad", "Chennai", "Hyderabad", "Bangalore", "Chennai", "Bangalore"]
}

df = pd.DataFrame(data)

print(" Full Data:")
print(df)

# -------------------------------
# Step 2: Add Revenue Column
# -------------------------------
df["revenue"] = df["price"] * df["quantity"]

print("\n Data with Revenue:")
print(df)

# -------------------------------
# Step 3: Total Revenue
# -------------------------------
total_revenue = df["revenue"].sum()
print("\n Total Revenue:", total_revenue)

# -------------------------------
# Step 4: Top Selling Product
# -------------------------------
top_product = df[df["revenue"] == df["revenue"].max()]
print("\n Top Selling Product:")
print(top_product)

# -------------------------------
# Step 5: Category-wise Revenue
# -------------------------------
category_revenue = df.groupby("category")["revenue"].sum()
print("\n Category-wise Revenue:")
print(category_revenue)

# -------------------------------
# Step 6: City-wise Revenue
# -------------------------------
city_revenue = df.groupby("city")["revenue"].sum()
print("\n City-wise Revenue:")
print(city_revenue)

# -------------------------------
# Step 7: Low Sales Products
# -------------------------------
low_sales = df[df["quantity"] < 5]
print("\n Low Sales Products (quantity < 5):")
print(low_sales)

# -------------------------------
# Step 8: Sort by Revenue
# -------------------------------
sorted_df = df.sort_values(by="revenue", ascending=False)
print("\n Products Sorted by Revenue (High → Low):")
print(sorted_df)
import matplotlib.pyplot as plt
#-------------------------------
#step 8: Bar Chart
#-------------------------------
# Category-wise Revenue Bar Chart
category_revenue.plot(kind='bar', color='skyblue', title='Revenue by Category')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.show()

# City-wise Revenue Bar Chart
city_revenue.plot(kind='bar', color='orange', title='Revenue by City')
plt.xlabel('City')
plt.ylabel('Revenue')
plt.show()
#-----------------------------
#step 9: pie chart
#-----------------------------
# Top Products Revenue Pie Chart
top_products = df.sort_values(by='revenue', ascending=False).head(5)
top_products.plot(kind='pie', y='revenue', labels=top_products['product'], autopct='%1.1f%%', legend=False, title='Top 5 Products by Revenue')
plt.ylabel('')
plt.show()
