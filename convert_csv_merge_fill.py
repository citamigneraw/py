import pandas as pd

# Read original items from a text file
with open('all.txt', 'r') as file:
    original_items = [line.strip() for line in file.readlines()]

# Read new data from the CSV file
new_data = pd.read_csv('test.csv')

# Create DataFrame for original items
df_original = pd.DataFrame({'Item': original_items})

# Merge the original items with new data, using a default value of $ 0.00 for missing items
df_merged = pd.merge(df_original, new_data, on='Item', how='left')

# Fill missing values with $ 0.00
df_merged['Value'].fillna('$ 0.00', inplace=True)

# Save the merged DataFrame to a CSV file
df_merged.to_csv('merged_output.csv', index=False)

print("Merged data has been saved to 'merged_output.csv'.")
