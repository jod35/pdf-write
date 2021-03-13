from PyPDF2 import PdfFileReader

import os

base_dir = os.path.dirname(os.path.abspath(__file__))

pdf_path=os.path.join(base_dir,'Chapter10.pdf')

pdf=PdfFileReader(str(pdf_path))

#get the first page of the pdf file

first_page=pdf.getPage(0)

print(type(first_page))

print(first_page.extractText())

with open('doc2.txt','w') as log_document:
    title=pdf.documentInfo.title
    num_pages=pdf.getNumPages()

    log_document.write(f"Title \n{title} \n Number of pages \n{num_pages}")


    for page in pdf.pages:
        text=page.extractText()
        log_document.write(text)

for page in pdf.pages:
    print(page.extractText())