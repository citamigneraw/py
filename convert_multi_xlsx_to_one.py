import pandas as pd
import os

# Directory where the Excel files are located
input_directory = 'warren_vouchers_new_with0802/converted_xlsx2'
# Path for the output Excel file
output_file = 'warren_vouchers_new_with0802/converted_xlsx2/combined_excel_file.xlsx'

dfs = []

# Get the list of files in the directory and sort them numerically
file_names = [f for f in os.listdir(input_directory) if f.endswith('.xlsx')]
file_names.sort(key=lambda x: int(x.split('.')[0]))  # Sort by the numeric part of the file name

# Process each file
for file_name in file_names:
    file_path = os.path.join(input_directory, file_name)
    
    # Read the Excel file
    excel_file = pd.ExcelFile(file_path)
    
    # Iterate over each sheet in the Excel file
    for sheet_name in excel_file.sheet_names:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        # Add a new column to identify the source file and sheet
        df['Source File'] = file_name
        df['Sheet Name'] = sheet_name
        dfs.append(df)

# Concatenate all DataFrames
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a new Excel file
combined_df.to_excel(output_file, index=False)
