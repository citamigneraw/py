import csv
list1 = ['County Taxes - Current', 'LFUF - Current', 'Afton Elberon - Current', 'Arcola - Current', 'Central Warren - Current', 'Churchill - Current', 'Drewry - Current', 'Hawtree - Current', 'Inez - Current', 'Littleton - Current', 'Long Bridge - Current', 'Macon - Current', 'Ridgeway - Current', 'Roanoke WW - Current', 'Town of Norlina - Current', 'Town of Warrenton - Current', 'Interest - Delinquent', 'Interest on LFUF - Del', 'Advertising - Delinquent', 'County Tax - Delinquent', 'LLP - Delinquent', 'LFUF - Delinquent', 'Afton Elberon- Delinquent', 'Arcola - Delinquent', 'Central Warren - Delinquent', 'Roanoke WW - Delinquent', 'Certified Mail', 'Over/Short Explained', 'Advance Payments', 'Bad Check Charge']
list2 = ['Interest on Current', 'Interest on LFUF - Current', 'Advertising - Current', 'County Taxes - Current', 'Late Listing Pen - Current', 'LFUF - Current', 'Town of Macon LFUF - Current', 'Dog Taxes Current', 'Afton Elberon - Current', 'Arcola - Current', 'Central Warren - Current', 'Churchill - Current', 'Drewry - Current', 'Ebony Fire - Current', 'Hawtree - Current', 'Inez - Current', 'Littleton - Current', 'Long Bridge - Current', 'Macon - Current', 'Ridgeway - Current', 'Roanoke WW - Current', 'Smith Creek - Current', 'Soul City - Current', 'Town of Macon - Current', 'Town of Norlina - Current', 'Town of Warrenton - Current', 'Interest - Delinquent', 'Interest on LFUF - Delinquent', 'Advertising - Delinquent', 'County Tax - Delinquent', 'Bella Russell Road Project', 'LLP - Delinquent', 'LFUF - Delinquent', 'Town of Macon LFUF - Delinquent', 'Dog Taxes - Delinquent', 'Afton Elberon - Delinquent', 'Arcola - Delinquent', 'Central Warren - Delinquent', 'Churchill - Delinquent', 'Drewry - Delinquent', 'Hawtree - Delinquent', 'Inez - Delinquent', 'Littleton - Delinquent', 'Long Bridge - Delinquent', 'Macon - Delinquent', 'Ridgeway - Delinquent', 'Roanoke WW - Delinquent', 'Smith Creek - Delinquent', 'Soul City - Delinquent', 'Town of Macon - Delinquent', 'Town of Norlina - Delinquent', 'Town of Warrenton - Delinquent', 'Certified Mail', 'Over/Short Explained', 'Advance Payments', 'Beer and Wine Licenses', 'Accounts Payable', 'Returned Checks', 'Bad Check Charge', 'Foreclosures/Contract', 'Delinquent Taxes', 'Public Utilities', 'Health Department', 'EMS', 'Recording Fee', 'Surplus Sales', 'Contract Service', 'Advertising Fee', 'Attorney Fee', 'Office Supplies']

set1 = set(list1)
set2 = set(list2)

only_in_list1 = set1 - set2
only_in_list2 = set2 - set1
common_elements = set1 & set2

print("Only in list1:", only_in_list1)
print("Only in list2:", only_in_list2)
print("Common elements:", common_elements)

with open('only_in_list1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for string in only_in_list1:
        writer.writerow([string])

with open('only_in_list2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for string in only_in_list2:
        writer.writerow([string])


with open('common_elements.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for string in common_elements:
        writer.writerow([string])