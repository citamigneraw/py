import pdfplumber
import pandas as pd

# Path to your PDF file
pdf_path = '20240801.pdf'
excel_path = '240801.xlsx'

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    # Extract text from each page
    pages = pdf.pages
    data = []
    for page in pages:
        table = page.extract_table()
        if table:
            data.extend(table)

if len(data) > 0:
    # Check if the first row is indeed headers
    if len(data[0]) > 1:  # Example condition, adjust as necessary
        df = pd.DataFrame(data[1:], columns=data[0])
    else:
        # Handle the case where headers might be missing or data is not structured as expected
        df = pd.DataFrame(data)  # Adjust based on what your data actually contains
else:
    print("No table data found.")
    df = pd.DataFrame()  # Create an empty DataFrame as a fallback

# Save to Excel if df is not empty
if not df.empty:
    df.to_excel(excel_path, index=False, engine='openpyxl')
else:
    print("DataFrame is empty. No file was saved.")
# Save to Excel
