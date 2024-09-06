def process_text_file(input_file, output_file):
    try:
        # Read the data from the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # Process lines: remove blank lines and strip leading asterisks and spaces
        cleaned_lines = [line.strip().lstrip('*').strip() for line in lines if line.strip()]

        # Write the cleaned lines to the output file
        with open(output_file, 'w') as file:
            for line in cleaned_lines:
                file.write(line + '\n')
        
        print(f"Data cleaned and saved to {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")

# Specify the input and output file paths
input_file = 'columbus.txt'  # Replace with your input text file path
output_file = 'output_cleaned.txt'  # Replace with your desired output text file path

# Process the text file
process_text_file(input_file, output_file)
