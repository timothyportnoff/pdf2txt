# Pdf2txt
Created for the purpose of analyzing PDF files to scrape for textual information.
The extracted text can be useful for various tasks, such as text analysis, search, or data extraction.
This program uses the PyPDF2 library to extract text from a PDF file and save it to a text file. o
Note: the PDF must contain plain text (Not text within an image) for this to be successful.

## Usage

1. Make sure you have Python installed on your system. The version used for this is Python 3.11

2. Make sure you have PyPDF2 library. It should be in the virtual python environment.

   ```bash
   pip install PyPDF2
   ```

3. Replace `'input.pdf'` with the path to your input PDF file and `'output.txt'` with the desired output text file in the code.



4. Run the python script with a filename for the argument, and it will perform the text extraction.

```bash
python3 main.py printdocumentfile.pdf
```

   This script will open the PDF file, extract the text from each page, and save it to the specified text file.

5. The extracted text will be available in `'extracted_text.txt'`.

## Important Notes

- If using pip within the virtual environment `'./venv/'` make sure to not use sudo. This causes an error to be thrown, saying that package managers may be being mixed.

- Ensure that you have the necessary permissions to access the input PDF file and create the output text file in the specified location.

- This script is designed for text-based PDFs. It may not work correctly with scanned documents or PDFs containing only images.
