#The `sort_numbers` function reads a list of integers from a specified input text file, sorts them in ascending order, and writes the sorted list to an output text file. It handles common errors, including file not found, non-numeric values, and general I/O errors. After sorting, the function prints the total count of numbers and a message indicating that the sorting is complete, helping users verify the operation's success.
def sort_numbers(input_file, output_file):
    try:
        # Read numbers from the input file
        with open(input_file, 'r') as file:
            numbers = file.readlines()
        
        # Strip any leading/trailing whitespace and convert to integers
        numbers = [int(num.strip()) for num in numbers if num.strip()]
        
        # Sort the numbers
        numbers.sort()
        
        # Count the number of numbers
        count = len(numbers)
        
        # Write the sorted numbers to the output file
        with open(output_file, 'w') as file:
            for number in numbers:
                file.write(f"{number}\n")
        
        # Output the total count to the console
        print(f"Total numbers: {count}")
        print(f"Sorting complete. Check '{output_file}' for the sorted list.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except ValueError:
        print("Error: The file contains non-numeric values.")
    except IOError as e:
        print(f"Error: An I/O error occurred. Details: {e}")

# Specify the input and output file paths
input_file = 'numberstosort.txt'  # Replace with your input file path
output_file = 'sorted_numbers.txt'  # Replace with your output file path

# Sort the numbers and output the count
sort_numbers(input_file, output_file)


