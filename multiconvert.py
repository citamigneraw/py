import os
import pandas as pd
import tabula
from pathlib import Path

def pdf_to_excel(pdf_path, excel_path):
    try:
        # Read tables from PDF using tabula
        dfs = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
        if dfs:
            # Concatenate all tables into a single DataFrame
            df = pd.concat(dfs, ignore_index=True)
            df.to_excel(excel_path, index=False, engine='openpyxl')
            print(f"Converted {pdf_path} to {excel_path}")
        else:
            print(f"No tables found in {pdf_path}")
    except Exception as e:
        print(f"Failed to convert {pdf_path}: {e}")

def process_pdfs_in_current_directory():
    # Get the current working directory
    current_dir = Path('.')
    # Output directory (can be set to current directory or another location)
    output_dir = current_dir / 'converted_xlsx'
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
