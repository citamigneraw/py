import pandas as pd

# Sample data
data = {
    'County': ['COLUMBUS COUNTY',
'ACME DELCO FD',
'BOLTON FD',
'BRUNSWICK FD',
'CERRO GORDO FD',
'COLUMBUS RESCUE DIST',
'EAST COLUMBUS FD',
'EVERGREEN FD',
'HALLSBORO FD',
'KLONDYKE FD',
'NORTH WHITEVILLE FD',
'OLD DOCK / CYPRESS FD',
'WELCHES CREEK FD',
'WHITEVILLE RESCUE DIST',
'WILLIAMS FD',
'YAM CITY FD',
'CITY OF WHITEVILLE',
'COLUMBUS COUNTY',
'ACME DELCO FD',
'BOLTON FD',
'BUCKHEAD FD',
'COLUMBUS RESCUE DIST',
'RIEGELWOOD SAN DIST',
'TOWN OF BOLTON',
'COLUMBUS COUNTY'
],
    'AccountNumber': [
'5',
'6',
'6',
'6',
'6',
'20',
'6',
'6',
'6',
'6',
'6',
'6',
'6',
'21',
'6',
'6',
'4',
'5',
'6',
'6',
'6',
'20',
'19',
'4',
'5'
]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Group by County and District and list Account Numbers
grouped = df.groupby('AccountNumber').agg({
    'County': lambda x: list(x.unique()),
}).reset_index()

# Display the result
print("Matches for Each Account Number:")
print(grouped)

# Optional: Save to CSV or Excel if needed
# grouped.to_csv('grouped_data.csv', index=False)
# grouped.to_excel('grouped_data.xlsx', index=False)