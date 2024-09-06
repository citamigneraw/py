import csv
def analyze_text(input_file, output_file):
    try:
        # Read the entire content from the input file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Process lines: split by new lines and strip whitespace
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Function to determine the type based on keywords
        def determine_type(text):
            text_lower = text.lower()
            if 'dist' in text_lower or 'fd' in text_lower:
                return 'D'
            elif 'town' in text_lower or 'city' in text_lower:
                return 'M'
            elif 'county' in text_lower:
                return 'C'
            else:
                return ''
        
        # Create a list of tuples with line and type
        analyzed_lines = [(line, determine_type(line)) for line in lines]
        
        # Sort the items alphabetically by the line text
        #sorted_items = sorted(analyzed_lines, key=lambda x: x[0])
        
        # Write the sorted results with types to the output file
        with open(output_file, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Line', 'Type'])  # Write header
            for line, mark in analyzed_lines:
                writer.writerow([line, mark])
        
        print(f"Analysis successful. Check '{output_file}' for the result.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")

# Specify the input and output file paths
input_file = 'output_cleaned.txt'  # Replace with your input file path
output_file = 'columbusypes.csv'  # Replace with your output file path

# Perform the analysis
analyze_text(input_file, output_file)
