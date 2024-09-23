import pandas as pd

# Original list of items (Column A)
original_items = [
'Interest on Current',
'Interest on LFUF - Current',
'Advertising - Current',
'County Taxes - Current',
'Late Listing Pen - Current',
'LFUF - Current',
'Town of Macon LFUF - Current',
'Dog Taxes Current',
'Afton Elberon - Current',
'Arcola - Current',
'Central Warren - Current',
'Churchill - Current',
'Drewry - Current',
'Ebony Fire - Current',
'Hawtree - Current',
'Inez - Current',
'Littleton - Current',
'Long Bridge - Current',
'Macon - Current',
'Ridgeway - Current',
'Roanoke WW - Current',
'Smith Creek - Current',
'Soul City - Current',
'Town of Macon - Current',
'Town of Norlina - Current',
'Town of Warrenton - Current',
'Interest - Delinquent',
'Interest on LFUF - Del',
'Advertising - Delinquent',
'County Tax - Delinquent',
'Bella Russell Road Project',
'LLP - Delinquent',
'LFUF - Delinquent',
'Town of Macon LFUF - Delinquent',
'Dog Taxes - Delinquent',
'Afton Elberon- Delinquent',
'Arcola - Delinquent',
'Central Warren - Delinquent',
'Churchill - Delinquent',
'Drewry - Delinquent',
'Hawtree - Delinquent',
'Inez - Delinquent',
'Littleton - Delinquent',
'Long Bridge - Delinquent',
'Macon - Delinquent',
'Ridgeway - Delinquent',
'Roanoke WW - Delinquent',
'Smith Creek - Delinquent',
'Soul City - Delinquent',
'Town of Macon - Delinquent',
'Town of Norlina - Delinquent',
'Town of Warrenton - Delinquent',
'Certified Mail',
'Over/Short Explained',
'Advance Payments',
'Beer and Wine Licenses',
'Accounts Payable',
'Returned Checks',
'Bad Check Charge',
'Foreclosures/Contract',
'Delinquent Taxes',
'Public Utilities',
'Health Department',
'EMS',
'Recording Fee',
'Surplus Sales',
'Contract Service',
'Advertising Fee',
'Attorney Fee',
'Office Supplies'
]

# New data (Column B)
data = {
    'Item': ['County Taxes - Current', 'LFUF - Current', 'Afton Elberon - Current', 'Arcola - Current', 'Central Warren - Current', 'Churchill - Current', 'Drewry - Current', 'Hawtree - Current', 'Inez - Current', 'Littleton - Current', 'Long Bridge - Current', 'Macon - Current', 'Ridgeway - Current', 'Roanoke WW - Current', 'Town of Norlina - Current', 'Town of Warrenton - Current', 'Interest - Delinquent', 'Interest on LFUF - Del', 'Advertising - Delinquent', 'County Tax - Delinquent', 'LLP - Delinquent', 'LFUF - Delinquent', 'Afton Elberon- Delinquent', 'Arcola - Delinquent', 'Central Warren - Delinquent', 'Roanoke WW - Delinquent', 'Certified Mail', 'Over/Short Explained', 'Advance Payments', 'Bad Check Charge'
],
    'Value': ['$ 95,364.52', '$ 3,000.00', '$ 73.95', '$ 178.81', '$ 120.68', '$ 574.48', '$ 690.69', '$ 158.85', '$ 8.89', '$ 28.78', '$ 2,943.13', '$ 134.15', '$ 6.31', '$ 498.06', '$ 855.49', '$ 21.45', '$ 16.83', '$ 8.59', '$ 4.00', '$ 354.90', '$ 0.40', '$ 308.64', '$ 0.58', '$ 4.58', '$ 14.19', '$ 0.21', '$ 60.00', '$ 0.00', '$ 740.00', '$ 25.00']}

# Create DataFrame for new data
df_new = pd.DataFrame(data)

# Create DataFrame for original items
df_original = pd.DataFrame({'Item': original_items})

# Merge data with default value of 0 for missing items
df_merged = pd.merge(df_original, df_new, on='Item', how='left')

# Fill missing values with 0
df_merged['Value'].fillna('$ 0.00', inplace=True)

df_merged.to_excel('mergeabdfill240918.xlsx', index=False)
