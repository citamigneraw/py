import pdfplumber
from PIL import Image
import pytesseract
from pathlib import Path

def pdf_to_text_with_ocr(pdf_path, text_path):
    try:
        # Open the PDF file
        with pdfplumber.open(pdf_path) as pdf:
            # Open the output text file
            with open(text_path, 'w', encoding='utf-8') as text_file:
                for i, page in enumerate(pdf.pages):
                    # Extract text
                    text = page.extract_text()
                    if text:
                        text_file.write(text)
                    else:
                        # Perform OCR if no text is found
                        img = page.to_image()
                        ocr_text = pytesseract.image_to_string(img.original)
                        text_file.write(ocr_text)
                    text_file.write('\n' + '-'*40 + '\n')  # Optional: Add a separator between pages
        
        print(f"Converted {pdf_path} to {text_path}")
    except Exception as e:
        print(f"Failed to convert {pdf_path}: {e}")

def process_pdfs_in_current_directory():
    # Get the current working directory
    #current_dir = Path('.')
    current_dir = Path('/home/ep/test/python_scripts')
    # Output directory
    output_dir = current_dir / 'converted_text'
    output_dir.mkdir(exist_ok=True)  # Create output directory if it doesn't exist

    # Loop through all PDF files in the current directory
    for pdf_file in current_dir.glob('*.pdf'):
        # Define output text path
        text_filename = pdf_file.stem + '.txt'
        text_path = output_dir / text_filename
        
        # Convert PDF to text
        pdf_to_text_with_ocr(pdf_file, text_path)

# Run the function
process_pdfs_in_current_directory()
