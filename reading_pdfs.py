import os
from pypdf import PdfReader

reader=PdfReader(r"C:\Users\ishan\Desktop\Minor Project\pdf_files\jesc101.pdf")
for i in reader.pages:
    print(i.extract_text())
   
