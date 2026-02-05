import pandas as pd

# Load raw data
df = pd.read_csv("data/daily_sales_data_0.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Aggregate daily sales (use correct column!)
df_grouped = df.groupby("date", as_index=False)["quantity"].sum()

# Rename for Dash app
df_grouped.rename(columns={"quantity": "sales"}, inplace=True)

# Save processed data
df_grouped.to_csv("data/processed_data.csv", index=False)

print("processed_data.csv created successfully")
