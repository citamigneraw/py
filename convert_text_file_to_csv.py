import csv

def parse_text_file(text_file_path):
    """Parse the text file and return a list of dictionaries."""
    data = []
    with open(text_file_path, 'r') as file:
        lines = file.readlines()
        
        person = {}
        for line in lines:
            line = line.strip()
            if not line:  # Empty line indicates the end of a person's data
                if person:  # Only add non-empty dictionaries
                    data.append(person)
                    person = {}
            else:
                key, value = line.split(': ', 1)
                person[key] = value
        
        if person:  # Add the last person if there is no trailing empty line
            data.append(person)
    
    return data

def write_to_csv(data, csv_file_path):
    """Write the list of dictionaries to a CSV file."""
    if not data:
        return
    
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Paths to the input text file and output CSV file
text_file_path = '/home/ep/test/publicutils_columbus2024/converted_text/2024 COLUMBUS COUNTY CERTIFICATION.txt'
csv_file_path = 'data.csv'

# Parse the text file and write to CSV
data = parse_text_file(text_file_path)
write_to_csv(data, csv_file_path)

print(f"Data has been successfully written to {csv_file_path}.")
