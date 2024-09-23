import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import os
import csv

# Set tesseract cmd to the path to your tesseract engine executable 
# (where you installed tesseract from above urls)


# List of files (images and PDFs)
file_paths = [
 "/home/ep/test/secu/17.png",
  "/home/ep/test/secu/18.png",
  "/home/ep/test/secu/19.png"
]

def extract_text_from_image(path):
    """Extract text from an image file."""
    return pytesseract.image_to_string(Image.open(path))

def extract_text_from_pdf(path):
    """Extract text from a PDF file."""
    text = ""
    pdf_document = fitz.open(path)
    for page_number in range(len(pdf_document)):
        page = pdf_document.load_page(page_number)
        text += page.get_text()
    pdf_document.close()
    return text

def extract_text(path):
    """Extract text based on the file extension."""
    ext = os.path.splitext(path)[1].lower()
    if ext in ['.png', '.jpg', '.jpeg']:
        return extract_text_from_image(path)
    elif ext in ['.pdf']:
        return extract_text_from_pdf(path)
    else:
        return "Unsupported file type"

# Create CSV file and write data
with open("files_content.csv", "w+", newline='', encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["FilePath", "FileText"])
    for file_path in file_paths:
        text = extract_text(file_path)
        csv_writer.writerow([file_path, text])

print("Text extraction complete. Data saved to 'files_content.csv'.")
