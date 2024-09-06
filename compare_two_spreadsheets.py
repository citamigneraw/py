import pandas as pd

# Define file paths
file1 = 'warren_vouchers_old/converted_xlsx2/combined_excel_file_old.xlsx'
file2 = 'warren_vouchers_new/converted_xlsx2/combined_excel_file_new.xlsx'

# Load Excel files
df1 = pd.read_excel(file1, sheet_name=None)  # Load all sheets into a dictionary
df2 = pd.read_excel(file2, sheet_name=None)  # Load all sheets into a dictionary

# Create a list to store differences
differences = []

# Compare sheets
for sheet_name in df1.keys():
    if sheet_name in df2:
        df1_sheet = df1[sheet_name]
        df2_sheet = df2[sheet_name]

        # Compare the DataFrames
        comparison = df1_sheet.compare(df2_sheet)
        
        if not comparison.empty:
            differences.append((sheet_name, comparison))
    else:
        differences.append((sheet_name, 'Sheet not found in the second file'))

# Output differences
if differences:
    for sheet, diff in differences:
        print(f"Differences in sheet '{sheet}':")
        print(diff)
else:
    print("No differences found")


