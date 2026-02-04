import pandas as pd
import glob

# Get all csv files from data folder
files = glob.glob("data/*.csv")

df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

# Combine all files into one DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# Convert date column to datetime
combined_df['date'] = pd.to_datetime(combined_df['date'])

# Keep only Pink Morsel rows
pink_df = combined_df[combined_df['product'] == 'Pink Morsel']

# Create sales column (quantity * price)
pink_df['sales'] = pink_df['quantity'] * pink_df['price']

# Select only required columns
final_df = pink_df[['sales', 'date', 'region']]

# Save to new CSV file
final_df.to_csv("processed_data.csv", index=False)

print("Data processing complete. File saved as processed_data.csv")

