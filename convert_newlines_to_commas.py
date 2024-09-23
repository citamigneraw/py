def convert_numbers_to_comma_separated(input_file, output_file):
    try:
        # Read numbers from the input file
        with open(input_file, 'r') as file:
            numbers = file.readlines()
        
        # Strip any leading/trailing whitespace characters and join the numbers with commas
        numbers = [num.strip() for num in numbers if num.strip()]  # Filter out empty lines
        comma_separated = ','.join(numbers)
        
        # Write the comma-separated string to the output file
        with open(output_file, 'w') as file:
            file.write(comma_separated)
        
        print(f"Conversion successful. Check '{output_file}' for the result.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")

# Specify the input and output file paths
input_file = 'feesmonetera.txt'  # Replace with your input file path
output_file = 'feesmonetera1.txt'  # Replace with your output file path

# Convert the numbers
convert_numbers_to_comma_separated(input_file, output_file)

