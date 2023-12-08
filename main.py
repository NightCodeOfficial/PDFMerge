# A simple program to merge all pdfs in a directory

from pypdf import PdfMerger
from pypdf import PdfReader
from tkinter import filedialog


source_dir = filedialog.askdirectory()
merger = PdfMerger(strict=False)


for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        # Add the pdf with visual confirmation
        pdf = PdfReader(source_dir+"/" + item, strict=False)
        print(item)
        merger.append(pdf)

file_name = str(input("Enter the file name for the finished merge: "))

# Save the file and close the merger
merger.write(source_dir+f'/{file_name} - Complete.pdf')
merger.close()
