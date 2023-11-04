import PyPDF2
import sys

def extract_text_from_pdf(pdf_path, text_path):
    # Open the PDF file
    pdf_file = open(pdf_path, 'rb')
    
    # Create a PDF reader object
    #pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Create a text file for writing
    text_file = open(text_path, 'w')
    
    # Loop through each page of the PDF and extract text
    #for page_num in range(pdf_reader.numPages):
    for page_num in range(len(pdf_reader.pages)):
        # page = pdf_reader.getPage(page_num)
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        
        # Write the extracted text to the text file
        text_file.write(text)
    
    # Close the PDF and text files
    pdf_file.close()
    text_file.close()

def print_string(input_file):
    print("Input File:", input_file)

#MAIN
if len(sys.argv) != 2: print("Usage: python3 main.py 'file_name 2.pdf'")
else:
    input_file = sys.argv[1]
    print_string(input_file)

    # Define the input PDF file and output text file
    pdf_file_path = input_file
    output_text_file = 'output.txt'

    # Call the function to extract text from the PDF
    extract_text_from_pdf(pdf_file_path, output_text_file)
    print("Text extraction completed. The text is saved in", output_text_file)

