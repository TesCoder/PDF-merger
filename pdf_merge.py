# This program merges two PDFs together.
# requires PyPDF2; install with "pip install PyPDF2" or "pip3 install PyPDF2 "

#!/usr/local/bin/python3
from PyPDF2 import PdfReader, PdfWriter

print("This program merges two PDFs together.")

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()

    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    file1 = input("Enter path of first file: ")
    file2 = input("Enter path of second file: ")
    paths = [file1, file2]
    merge_pdfs(paths, output='merged_upd.pdf')
