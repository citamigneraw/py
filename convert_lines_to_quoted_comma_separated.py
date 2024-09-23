def convert_lines_to_quoted_comma_separated(input_file, output_file):
    try:
        # Read lines from the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Process each line to wrap with single quotes and add a comma
        quoted_lines = [f"'{line.strip()}'" for line in lines if line.strip()]  # Filter out empty lines
        
        # Join the quoted lines with commas and maintain new lines
        quoted_lines_with_commas = ', '.join(quoted_lines)
        
        # Write the result to the output file
        with open(output_file, 'w') as file:
            file.write(quoted_lines_with_commas + '\n')  # Add a newline at the end
        
        print(f"Conversion successful. Check '{output_file}' for the result.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")

# Specify the input and output file paths
for i in range(1,3):  # Files named 2.txt to 11.txt
    input_file = f'{i}.txt'
    output_file = f'{i}_del.txt'  # Output files will be named like '2_del.txt', '3_del.txt', etc.
    
    convert_lines_to_quoted_comma_separated(input_file, output_file)
