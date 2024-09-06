import os
import pandas as pd
import pdfplumber
from pathlib import Path

def pdf_to_excel(pdf_path, excel_path):
    try:
        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            # Extract text from each page
            data = []
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    data.extend(table)
        
        # Check if data is available
        if data:
            # Convert to DataFrame
            df = pd.DataFrame(data[1:], columns=data[0])
            # Save to Excel
            df.to_excel(excel_path, index=False, engine='openpyxl')
            print(f"Converted {pdf_path} to {excel_path}")
        else:
            print(f"No tables found in {pdf_path}")
    except Exception as e:
        print(f"Failed to convert {pdf_path}: {e}")

def process_pdfs_in_current_directory():
    # Get the current working directory
    #current_dir = Path('.')
    current_dir = Path('/home/ep/test/publicutils_columbus2024')
    # Output directory
    output_dir = current_dir / 'converted_xlsx2'
    output_dir.mkdir(exist_ok=True)  # Create output directory if it doesn't exist

    # Loop through all PDF files in the current directory
    for pdf_file in current_dir.glob('*.pdf'):
        # Define output Excel path
        excel_filename = pdf_file.stem + '.xlsx'
        excel_path = output_dir / excel_filename
        
        # Convert PDF to Excel
        pdf_to_excel(pdf_file, excel_path)

# Run the function
process_pdfs_in_current_directory()
