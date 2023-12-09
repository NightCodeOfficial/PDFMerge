# A simple program to merge all pdfs in a directory

import os
from pypdf import PdfMerger
from pypdf import PdfReader
from tkinter import filedialog


merger = PdfMerger(strict=False)

def main():
    source_dir = filedialog.askdirectory()

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


if __name__ == '__main__':
    main()
