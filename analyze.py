from collections import Counter
import re

def analyze_text(input_file, output_file):
    try:
        # Read the entire content from the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Use a regular expression to split content by new lines and clean up whitespace
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Count occurrences of each line
        counter = Counter(lines)
        sorted_items = sorted(counter.items(), key=lambda x: x[0])
        
        # Write the counts to the output file
        with open(output_file, 'w') as file:
            for item, count in counter.items():
                file.write(f"'{item}': {count}\n")
        
        print(f"Analysis successful. Check '{output_file}' for the result.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")

# Specify the input and output file paths
input_file = 'munic.txt'  # Replace with your input file path
output_file = 'output_analyzed2.txt'  # Replace with your output file path

# Perform the analysis
analyze_text(input_file, output_file)
