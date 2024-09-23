import csv
import re

# Specify input and output filenames
input_filename = 'postedReport.txt'
output_filename = 'financial_data.csv'

# Define a regex pattern to extract the desired information
pattern = re.compile(r'(\d{2}/\d{2}/\d{4})\s+(\w+)\s+\$([\d,\.]+).*?\$([\d,\.]+)$')

# List to store extracted data
data = []

# Read the data from the text file
with open(input_filename, 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        
        # Search for the pattern in the line
        match = pattern.search(line)
        if match:
            date = match.group(1)
            category = match.group(2)
            amount = match.group(3)
            data.append((date, category, amount))

# Write the data to a CSV file
with open(output_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Date", "Category", "Amount"])
    # Write the data
    writer.writerows(data)

print(f"Data has been read from {input_filename} and written to {output_filename}")
