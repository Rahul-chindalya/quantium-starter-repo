import pandas as pd

# Step 1: Read CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Step 2: Combine all data
df = pd.concat([df1, df2, df3])

# Step 3: Filter only Pink Morsel
df = df[df["product"] == "pink morsel"]

# Step 4: Clean price column (remove $ if present)
df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)

# Step 5: Create sales column
df["sales"] = df["quantity"] * df["price"]

# Step 6: Keep required columns
df = df[["sales", "date", "region"]]

# Step 7: Save output
df.to_csv("processed_data.csv", index=False)

print("Data processing complete!")