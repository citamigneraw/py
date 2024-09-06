def convert_lines_to_quoted_comma_separated(input_file, output_file):
    try:
        # Read lines from the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # Process each line to wrap with single quotes and add a comma
        quoted_lines = [f"'{line.strip()}'" for line in lines if line.strip()]  # Filter out empty lines
        
        # Join the quoted lines with commas and maintain new lines
        quoted_lines_with_commas = ',\n'.join(quoted_lines)
        
        # Write the result to the output file
        with open(output_file, 'w') as file:
            file.write(quoted_lines_with_commas + '\n')
        
        print(f"Conversion successful. Check '{output_file}' for the result.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")

# Specify the input and output file paths
input_file = 'munic.txt'  # Replace with your input file path
output_file = 'munic22.txt'  # Replace with your output file path

# Convert the lines
convert_lines_to_quoted_comma_separated(input_file, output_file)
