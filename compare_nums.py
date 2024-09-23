# Define the two lists of numbers
from collections import Counter
list1 = ['362,214.10',
'104.82',
'16,995.84',
'820.54',
'1,707.30',
'2,853.36',
'4,497.71',
'1,998.86',
'1,414.59',
'688.43',
'135.45',
'1,954.89',
'2,575.37',
'1,301.69',
'74.82',
'3,024.74',
'649.02',
'838.87',
'542.64',
'2,095.69',
'128.83',
'29.79',
'363.83',
'7.52',
'346.64',
'2.98',
'0.97',
'18.88',
'7.13',
'0.23',
'0.20',
'76.09',
'96.74',
'1.62',
'8.68',
'61.59',
'25.00'
]
list2 = [
]
# Convert lists to sets for easier comparison
#set1 = set(list1)
#set2 = set(list2)
counter = Counter(list3)

# Find and print duplicates
print("Duplicates in list3:")
for number, count in counter.items():
    if count > 1:
        print(f"{number}: {count}")
#set3 = set(list3)
#count = len(set3)
#print(f"Total numbers not common: {count}")
#unique_numbers = set3
#common_numbers = unique_numbers

# Find numbers only in list2
#unique_to_list3 = set2.difference(set1)

# Print the results
#print("Common Numbers:")
#print(sorted(common_numbers))
#count = len(list3)
#print(f"Total numbers not common: {count}")
#count2 = len(unique_numbers)
#print(f"Total numbers common: {count}")


#print("\nUnique to List 2:")
#print(sorted(unique_to_list2))

# monetera 13266,13267,13268,13270,13271,13273,13274,13275,13276,13278,13279,13280,13281
# db 13260,13261,13262,13263,13264,13266,13267,13268,13270,13271,13273,13274,13275,13276,13278,13279,13280,13281


#[100894, 102183, 400927, 9000323, 9000523, 9000747, 9000870, 9000871, 9001204, 9001611, 9002760, 9003146, 9003732, 9004503, 9004702, 9005132, 9005148, 9005331, 9005932]